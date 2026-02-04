
clear          
echo "INSTALLATION STARTED"
git pull
apt update && apt upgrade -y          
apt install python3 -y
apt install figlet -y                                                     
pip install -r requirements.txt
clear                                                                                                                 
echo "INSTALLATION SUCCESSFUL. NOW RUN 'python details.py'"
