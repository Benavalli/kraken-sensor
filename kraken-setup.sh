#!/bin/sh

exist_venv() {
	if [ ! -d "env" ]; then
		echo '**Creating virtual environment...'
		python3 -m venv env
	else
		echo '**Virtual environment already created.'
	fi
	echo '**Initializing virtual environment.'
	#running activate
	. env/bin/activate
	#phyton version with venv
	show_python_version
}

show_python_version() {
	pythonVersion=$(python3 --version)
	echo 'Virtual environment Python version: ' "$pythonVersion"
}

#! Installing required dependencies
install_requirements() {
	if [ ! -f "lib-requirements.txt" ]; then
		echo 'Project does not contain the requirements file.'
	else
		echo '**Downloading project dependencies.'
		#python3 -m pip install --upgrade pip setuptools wheel
		python3 -m pip install -r lib-requirements.txt
	fi
}

exist_venv
install_requirements
