sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install git
pip3 install --user numpy
pip3 install --user flask
pip3 install --user mxnet==1.4
pip3 install --user onnx==1.5
mkdir geni_project
cd geni_project
git init
git remote add ImageRecognitionApp https://github.com/xyiquan/ImageRecognitionApp.git
git fetch ImageRecognitionApp
git checkout ImageRecognitionApp/master -- apiserver/
echo "*****"
echo "Done. Go to ./geni_project/apiserver and run: python3 apiserver.py"
echo "*****"