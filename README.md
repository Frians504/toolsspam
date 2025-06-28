pkg update && pkg upgrade -y

pkg install git python python-pip

git clone https://github.com/Frians/toolsspam

cd toolsspam

pip install -r requirements.txt

python run.py
