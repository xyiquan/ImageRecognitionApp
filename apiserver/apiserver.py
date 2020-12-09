import mxnet as mx
import numpy as np
import os
from collections import namedtuple
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, Response
from mxnet.gluon.data.vision import transforms
from mxnet.contrib.onnx.onnx2mx.import_model import import_model

# Web Server Config
app = Flask(__name__)
app.config["DEBUG"] = False

# Read image
batch = namedtuple('Batch', ['data'])

# Download categories for classification (from ImageNet)
with open('synset.txt', 'r') as f:
    labels = [l.rstrip() for l in f]

# Import ONNX model
model_path = "squeezenet1.1-7.onnx"
sym, arg_params, aux_params = import_model(model_path)

# Load the classification network for inference
if len(mx.test_utils.list_gpus()) == 0:
    ctx = mx.cpu()
else:
    ctx = mx.gpu(0)
mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
mod.bind(
    for_training=False,
    data_shapes=[('data', (1, 3, 224, 224))],
    label_shapes=mod._label_shapes
)
mod.set_params(arg_params, aux_params, allow_missing=True, allow_extra=True)

# Transform images into standard image size for classification
def preprocess(img):
    transform_fn = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    img = transform_fn(img)
    img = img.expand_dims(axis=0)
    return img

# Classify the image into most probable category
def predict(image):
    # Prepare image for classification
    img = mx.image.imdecode(image)
    img = preprocess(img)
    mod.forward(batch([img]))

    # Perform image classification, generate probabilities for each category
    scores = mx.ndarray.softmax(mod.get_outputs()[0]).asnumpy()

    # Return the category with the highest probability
    scores = np.squeeze(scores)
    a = np.argsort(scores)[::-1]
    classification = ('%s; probability=%f' % (labels[a[0]], scores[a[0]]))
    return classification

# API for external clients/servers to call
@app.route('/api/classify', methods=['POST'])
def classify():
    uploaded_file = request.files['file']
    predictions = predict(uploaded_file.read())
    return predictions

# Listen for requests on all network interfaces
app.run(host='0.0.0.0', port=5001)