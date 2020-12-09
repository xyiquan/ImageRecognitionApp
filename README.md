# ImageRecognitionApp

## Setup steps
1. Reserve resources on GENI using Rspec file <a href="https://github.com/xyiquan/ImageRecognitionApp/raw/master/rspec_geni_project.xml">rspec_geni_project.xml</a>.
   1. Ensure webserver has a public IP.
1. Setup Webserver
   1. SSH into Webserver and run environment setup script:
      1. Run: wget https://github.com/xyiquan/ImageRecognitionApp/raw/master/setupEnvWebserver.sh
      1. Run: sh setupEnvWebserver.sh
   1. Go to ./geni_project/webserver/ and update the IP of APIserver in <a href="https://github.com/xyiquan/ImageRecognitionApp/tree/master/webserver">config.txt</a>.
   1. Run "python3 webserver.py".
1. Setup APIserver  
   1. SSH into APIserver and run environment setup script:
      1. Run: wget https://github.com/xyiquan/ImageRecognitionApp/raw/master/setupEnvAPIserver.sh
      1. Run: sh setupEnvAPIserver.sh
   1. Go to ./geni_project/apiserver/ and run "python3 apiserver.py"
      1. Note: If there is an error about Numpy, run "pip3 uninstall numpy" a few times until there is no more numpy installations, then install by running "pip3 install --user numpy"
1. Access the app at http://"webserver public IP":5000/
