from sprites import *

images = 'res/cat1.png','res/cat2.png'
print(type(images))

cat = Sprite(shape=images)



while True:
    cat.play('res/chimes.wav')
    cat.fd(10)
    cat.nextcostume()
    cat.wait(0.9)
   