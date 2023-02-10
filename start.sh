apt update && apt upgrade -y
apt install ffmpeg -y
pip3 install -U -r requirements.txt
echo "Starting the Bot...."
python3 loader.py
