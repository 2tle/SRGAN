# SRGAN
Super Resoultion GAN with Keras on macos

This project is based on [eriklindernoren/Keras-GAN](https://github.com/eriklindernoren/Keras-GAN)

## Datasets
1. create directory named `datasets`
2. create directory `YOUR_DATASETS_NAME` in `datasets` directory
3. put your images in `YOUR_DATASETS_NAME`
4. edit `srgan_v2.py`
```
class SRGAN():
    def __init__(self):
    ...
    self.dataset_name = 'YOUR_DATASETS_NAME'
```

## Recommend Datasets
[DIV2K datasets](https://data.vision.ee.ethz.ch/cvl/DIV2K/)

[DIV2K introductory dataset paper](https://people.ee.ethz.ch/~timofter/publications/Agustsson-CVPRW-2017.pdf)


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
