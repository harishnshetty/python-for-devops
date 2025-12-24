# python-for-devops

sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.14 python3.14-venv python3.14-dev -y

python3.14 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
