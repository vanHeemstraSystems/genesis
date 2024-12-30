# Readme

## Installation

Follow this order of installation, otherwise numpy 2.2.0 (with issues) is installed instead of the genesis compatible numpy 1.26.4:

```
$ sudo apt-get update && sudo apt-get install ffmpeg libsm6 libxext6 -y
$ pip install trimesh[all]
$ pip install -r requirements.txt
```

## Demo

Run the example:

```
$ python hello_genesis.py
```