#!/bin/sh

#! Verify and activate virtual Python environment
install_python_virtual_env() {
	if [ ! -d "env" ]; then
		echo 'Creating virtual environment...'
		python -m venv env
	else
		echo 'Virtual environment is already created.'
	fi
	echo 'Initializing virtual environment.'
	. env/bin/activate
}

#! Display Python version
show_python_version() {
	pythonVersion=$(python --version)
	echo 'Python version: ' "$pythonVersion"
}

#! Installing SQLite
install_db_tools() {
	sudo apt update
	sudo apt install sqlite3 sqlitebrowser python3-sqlalchemy -y
	sudo apt install python3-gpiozero -y
	sudo apt install python3-picamera -y
}

sudo apt update
sudo apt install python3 python3-pip python3-sqlalchemy sqlite3


#! Installing required dependencies
install_requirements() {
	if [ ! -f "lib-requirements.txt" ]; then
		echo 'Project does not contain Python requirements file.'
	else
		echo 'Downloading project dependencies...'
		python -m pip install -r lib-requirements.txt
	fi
}

install_db_tools
show_python_version
#install_requirements
#export 	PYTHONPATH=$(pwd)
#python $(pwd)/data/db_manager.py
