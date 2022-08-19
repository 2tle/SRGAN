from srgan_v2 import SRGAN

EPOCHS = 300
BATCH_SIZE = 1
INTERVAL = 50

gan = SRGAN()
gan.train(epochs=EPOCHS, batch_size=BATCH_SIZE, sample_interval=INTERVAL)
gan.generator.save('models/SRGAN_EP%s' % (str(EPOCHS)))
