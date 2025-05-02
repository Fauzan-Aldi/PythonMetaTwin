if [ "$(id -u)" -ne 0 ]; then
	echo "[!] Must be run as root"
	exit 1
fi
echo "[+] Updating package list"
sudo apt-get update

echo "[+] Installing Wine"
sudo apt-get install -y wine

echo "[+] Installing Python 3"
sudo apt-get install -y python3 python3-pip

echo "[+] Installing python package subprocess32"
sudo pip3 install subprocess32

echo "[+] Installation complete"