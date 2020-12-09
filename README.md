# ImageRecognitionApp

## Setup steps
1. Reserve resources on GENI using Rspec file <a href="https://github.com/xyiquan/ImageRecognitionApp/blob/master/rspec_geni_project.xml">rspec_geni_project.xml</a>.
1. Setup Webserver
   1. SSH into Webserver and run environment setup script.
   1. Download the code onto Webserver.
   1. Update the IP of APIserver in <a href="https://github.com/xyiquan/ImageRecognitionApp/tree/master/webserver">config.txt</a>.
   1. In the folder where webserver.py is run "python3 webserver.py".
1. Setup APIserver  
   1. SSH into APIserver and run environment setup script.
   1. Download the code onto APIserver
   1. In the folder where webserver.py is run "python3 apiserver.py".
