# SRGAN
Super Resoultion GAN with Keras on macos

This project is based on [eriklindernoren/Keras-GAN](https://github.com/eriklindernoren/Keras-GAN)

## Datasets
1. create directory named `datasets`
2. create directory `YOUR_DATASETS_NAME` in `datasets` directory
3. put your images in `YOUR_DATASETS_NAME`
4. edit `train.py`
```
DATASETS = 'YOUR_DATASETS_NAME'
```

## How to run
1. `pip install -r requirements.txt`
2. `python train.py`
model will be saved in models directory

## If you wanna use this model on windows..
1. open `requirements.txt`
2. remove 2 lines:
```
tensorflow-macos==2.9.2
tensorflow-metal==0.5.1
```
3. run!
