from logging import root
from tkinter import *
from PIL import Image,ImageTk,ImageOps
import tensorflow.keras
import numpy as np
import pyttsx3
import speech_recognition as sr
import os
import time
dex_root = Tk()
dex_root.title("POKEDEX")
dex_root.geometry("300x530")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def gen_labels():
        labels = {}
        with open("labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels
def start():


    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    # Load the model
    model = tensorflow.keras.models.load_model('keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('images/pokemon4.jpg')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    result = np.argmax(prediction[0])
    fresult=gen_labels()[str(result)]
    music_dir='C:\\Users\\cc\\OneDrive\\Desktop\\project\\pokevoices'
    pokevoices=os.listdir(music_dir)
    # name=str(input("Enter your name:"))
    speak("hello i am your pokédex")
    speak("recognising Pokémon....")
    time.sleep(1)

    if fresult=="pikachu":
            print("pikachu,An Electric type Pokémon introduced in Generation 1 . It is known as the Mouse Pokémon.")
            speak(gen_labels()[str(result)]+"An electric type Pokémon introduced in Generation 1 . It is known as the Mouse Pokémon.")
            os.startfile(os.path.join(music_dir,pokevoices[1]))
            
    elif fresult=="bulbasaur":
                print("Bulbasaur,A Grass/Poison type Pokémon introduced in Generation 1 . It is known as the Seed Pokémon.")
                speak(gen_labels()[str(result)]+"A Grass/Poison type Pokémon introduced in Generation 1 . It is known as the Seed Pokémon.")
                os.startfile(os.path.join(music_dir,pokevoices[0]))
            
    elif fresult=="squirtle":
                print("Squirtle,A Water type Pokémon introduced in Generation 1 . It is known as the Tiny Turtle Pokémon.")
                speak(gen_labels()[str(result)]+"A Water type Pokémon introduced in Generation 1 . It is known as the Tiny Turtle Pokémon.")
                os.startfile(os.path.join(music_dir,pokevoices[2]))
            

    else:
            speak("sorry, no information about this pokemon")

print("Click on the pokéball to start!")
speak("Click on the pokéball to start!")

bg=PhotoImage(file='images/pokedexp.png')
lbl=Label(dex_root,image=bg)
lbl.place(x=0,y=0,relwidth=1,relheight=1)
strt_btn=PhotoImage(file='images/pokeball.png')
img_label=Label(image=strt_btn)
my_button=Button(dex_root,image=strt_btn,command=start,borderwidth=0)
my_button.pack(pady=230)
my_label=Label(dex_root,text='')
my_label.pack(pady=230)
dex_root.mainloop()