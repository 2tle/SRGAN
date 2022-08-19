from srgan_v2 import SRGAN

EPOCHS = 300
BATCH_SIZE = 1
INTERVAL = 50
DATASETS = ''
LOW_WIDTH = 100
LOW_HEIGHT = 100

gan = SRGAN(DATASETS, low_width = LOW_WIDTH, low_height = LOW_HEIGHT)
gan.train(epochs=EPOCHS, batch_size=BATCH_SIZE, sample_interval=INTERVAL)
gan.generator.save('models/SRGAN_EP%s' % (str(EPOCHS)))
