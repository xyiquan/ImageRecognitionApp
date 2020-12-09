sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install git
pip3 install --user numpy
pip3 install --user flask
mkdir geni_project
cd geni_project
git init
git remote add ImageRecognitionApp https://github.com/xyiquan/ImageRecognitionApp.git
git fetch ImageRecognitionApp
git checkout ImageRecognitionApp/master -- webserver/
echo "*****"
echo "Done. Go to ./geni_project/webserver and run: python3 webserver.py"
echo "*****"