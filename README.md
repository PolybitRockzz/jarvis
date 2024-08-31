# Jarvis AI Assistant

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

AI assistant that can answer questions, and perform appropriate tasks in the system.

## Table of Contents

- [Features](#features)
  - [Routine Features](#routine-features)
- [Installation](#installation)

## Features

- Offline AI assistance using Ollama models
- Modular framework, i.e., any updates can simply be added by adding new python programs into the modules folder
- Tested support for Windows 10, and Ubuntu

### Routine Features

- Tell date and time ✅
- Schedule reminders on PC ✅
- Schedule alarms on PC (can be snoozed and dismissed) ⏱️

### Operating System Features

- Open installed apps ✅
- Close installed apps ✅

## Installation

Here are the starting dependencies required for running this program:
- [Python](https://www.python.org/) > 3.10
- [Ollama](https://ollama.com/) > 0.3
- [Git](https://git-scm.com) > 2.40

Next, in order to download the source code of this program:
```
git clone https://github.com/PolybitRockzz/jarvis.git
cd jarvis
```

Next in order to run the program, you can either start right away or (as better practice) use a virtual environment using:
```
pip install --upgrade virtualenv
python -m venv env
```
If in CMD, type: `env/Scripts/activate.bat`
If in PowerShell, type: `env/Scripts/Activate.ps1`

Finally, in order to run the program:

```
pip install -r requirements.txt
python app.py
```