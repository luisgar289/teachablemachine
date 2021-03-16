import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class proyecto():

    def __init__(self):
        pass

    def proceso(self):

        respuesta = "SI"

        while respuesta == "SI":

            
            # Disable scientific notation for clarity
            np.set_printoptions(suppress=True)

            # Load the model
            model = tensorflow.keras.models.load_model('keras_model.h5')

            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Replace this with the path to your image

            image = input('Introduce el nombre de tu archivo: ')
            imagen = Image.open(image)

            #resize the image to a 224x224 with the same strategy as in TM2:
            #resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            imagen = ImageOps.fit(imagen, size, Image.ANTIALIAS)

            #turn the image into a numpy array
            image_array = np.asarray(imagen)

            # display the resized image
            imagen.show()

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = model.predict(data)

            for i in prediction:
                if i[0] > 0.5:
                    print("El Artista de tu imagen es Taylor Swift")
                elif i[1] > 0.5:
                    print("El Artista de tu imagen es Bad Bunny")
                elif i[2] > 0.5:
                    print ("El Artista de tu imagen es JeongHan")

            respuesta = input(str("¿Quieres usar otra imagen? SI/NO "))

proyecto = proyecto()
proyecto.proceso()