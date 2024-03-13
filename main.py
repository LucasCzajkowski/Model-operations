import customtkinter
from ConsoleManager import *
from Loader import *
from Saver import *
from Visualizer import *
from Translator import *
from Scaller import *

global meshArray

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

mainWindow = customtkinter.CTk()  # create CTk window like you do with the Tk window
mainWindow.geometry("600x370")
mainWindow.resizable(False,False)
mainWindow.title("Zajebista aplikacja")

tabview = customtkinter.CTkTabview(master=mainWindow)
tabview.pack(padx=20, pady=10, side = "top" , fill = "x")

labelConsole = customtkinter.CTkLabel(mainWindow, text="Console output", fg_color="black")
labelConsole.pack(padx=20, pady=10, side = "top" , fill = "x")
labelConsole.configure(height = 70, text_color = "green")


def LoadModel():
    global meshArray
    meshArray = LoadModelFromDisk(entryFileLoadLocation.get())
    WriteToConsole(meshArray, labelConsole)
    print(entryFileLoadLocation.get())
    print(meshArray)


def VisualizeModel():
    global meshArray
    Visualize(meshArray)
    WriteToConsole("Visualizing model", labelConsole)


def TranslateModel():
    global meshArray
    meshArray = Translate(meshArray,entryX.get(), entryY.get(), entryZ.get())
    WriteToConsole("translating array", labelConsole)
    print(meshArray)


def Scale():
    global meshArray
    meshArray = ScaleModel(meshArray, entryScaleX.get(), entryScaleY.get(), entryScaleZ.get(), entryScaleFactor.get())
    WriteToConsole("scalling array", labelConsole)
    print(meshArray)


def SaveToTxt():
    global meshArray
    SaveArrayToTxtFile(meshArray, entrySaveLocation.get())
    WriteToConsole("Saving to .txt to " + entrySaveLocation.get(), labelConsole)
    print(meshArray)


def SaveToStl():
    global meshArray
    SaveToStlFile(meshArray, entrySaveLocation.get())
    WriteToConsole("Saving to .stl to " + entrySaveLocation.get(), labelConsole)
    print(meshArray)



# TAB LOAD MODEL
tabview.add("Load Model")

entryFileLoadLocation = customtkinter.CTkEntry(master=tabview.tab("Load Model"), placeholder_text="Model path")
entryFileLoadLocation.pack(padx=20, pady=20, side = "top" , fill = "x" )

button = customtkinter.CTkButton(master=tabview.tab("Load Model"), text = "Load Model", command = LoadModel)
button.pack(padx=20, pady=20 )


# TAB VISUALIZE
tabview.add("Visualize Model")
button = customtkinter.CTkButton(master=tabview.tab("Visualize Model"), text = "Visualize", command=VisualizeModel)
button.pack(padx=20, pady=20 )


# TAB TRANSLATE
tabview.add("Translate Model")

entryX = customtkinter.CTkEntry(master=tabview.tab("Translate Model"), placeholder_text="x")
entryX.pack(padx=20, pady=3, side = "top")
entryX.configure(width = 100)
entryY = customtkinter.CTkEntry(master=tabview.tab("Translate Model"), placeholder_text="y")
entryY.pack(padx=20, pady=3, side = "top")
entryY.configure(width = 100)
entryZ = customtkinter.CTkEntry(master=tabview.tab("Translate Model"), placeholder_text="z")
entryZ.pack(padx=20, pady=3, side = "top")
entryZ.configure(width = 100)

button = customtkinter.CTkButton(master=tabview.tab("Translate Model"), text = "Translate", command=TranslateModel)
button.pack(padx=20, pady=20 )


# TAB SCALE
tabview.add("Scale Model")
entryScaleX = customtkinter.CTkEntry(master=tabview.tab("Scale Model"), placeholder_text="Scale x position")
entryScaleX.pack(padx=20, pady=3, side = "top")
entryScaleX.configure(width = 130)
entryScaleY = customtkinter.CTkEntry(master=tabview.tab("Scale Model"), placeholder_text="Scale y position")
entryScaleY.pack(padx=20, pady=3, side = "top")
entryScaleY.configure(width = 130)
entryScaleZ = customtkinter.CTkEntry(master=tabview.tab("Scale Model"), placeholder_text="Scale z position")
entryScaleZ.pack(padx=20, pady=3, side = "top")
entryScaleZ.configure(width = 130)
entryScaleFactor = customtkinter.CTkEntry(master=tabview.tab("Scale Model"), placeholder_text="Scale factor")
entryScaleFactor.pack(padx=20, pady=3, side = "top")
entryScaleFactor.configure(width = 100)

button = customtkinter.CTkButton(master=tabview.tab("Scale Model"), text = "Scale", command=Scale)
button.pack(padx=20, pady=20 )

# TAB SAVE
tabview.add("Save to file")
entrySaveLocation = customtkinter.CTkEntry(master=tabview.tab("Save to file"), placeholder_text="FileLocation")
entrySaveLocation.pack(padx=20, pady=3, side = "top" , fill = "x" )

button = customtkinter.CTkButton(master=tabview.tab("Save to file"), text = "Save to .txt", command=SaveToTxt)
button.pack(padx=20, pady=20 )

button = customtkinter.CTkButton(master=tabview.tab("Save to file"), text = "Save to .stl", command=SaveToStl)
button.pack(padx=20, pady=20 )

tabview.set("Load Model")  # set currently visible tab

# def OpenNewWindow():
#     newWindow = customtkinter.CTkToplevel(mainWindow)
#     newWindow.geometry("400x200")

mainWindow.mainloop()
