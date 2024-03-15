#long method

light=input("Enter the color you are seeing on the trafic light : ")
if (light=="red"):
    print("stop")
elif (light=="green"):
    print("Go")
elif (light=="yellow"):
    print("break")
else:
    print("The light is broken")

# short method
    
light = input("Please enter the color: ").lower()
Stop_Message="Stop"if light=="red" else "You are colorblind"
Go_Message="Go"if light=="Green" else ""
Slowdown_message="Look"if light=="yellow" else ""
print(Stop_Message , Go_Message , Slowdown_message)

