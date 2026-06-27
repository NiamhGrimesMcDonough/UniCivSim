
phi = 0
from tkinter import * 

root = Tk()  
root.geometry("600x600") 

StarsThatHavePlanets = 1
PlanetsThatSupportLife = 0.3
PlanetsThatDevelopLife = 0.9
PlanetsThatDevelopIntelligentLife = 0.5
CivlizationsThatReleaseSignals = 0.6
LifetimeOfCivilizations = 0.2
MinStar = 1000
MaxStar = 5000
CivProbability = StarsThatHavePlanets*PlanetsThatSupportLife*PlanetsThatDevelopLife*PlanetsThatDevelopIntelligentLife*CivlizationsThatReleaseSignals*LifetimeOfCivilizations

#Section 1 (StarsThatHavePlanets)
slider1 = Scale( root, variable = StarsThatHavePlanets, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider1.set(100) 
label1 = Label(root, text = "Percentage Of Stars That have planets") 
slider1.pack(anchor = W) 
label1.pack(anchor= W)

#Section 2 (PlanetsThatSupportLife)
slider2 = Scale( root, variable = PlanetsThatSupportLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider2.set(30)  
label2 = Label(root, text = "Percentage Of Planets That Support Life") 
slider2.pack(anchor = W) 
label2.pack(anchor= W)

#Section 3 (PlanetsThatDevelopLife)
slider3 = Scale( root, variable = PlanetsThatDevelopLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider3.set(100)  
label3 = Label(root, text = "Percentage Of Planets That Develop Life") 
slider3.pack(anchor = W) 
label3.pack(anchor= W)

#Section 4 (PlanetsThatDevelopIntelligentLife)
slider4 = Scale( root, variable = PlanetsThatDevelopIntelligentLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider4.set(50)  
label4 = Label(root, text = "Percentage Of Planets That Develop Intelligent Life") 
slider4.pack(anchor = W) 
label4.pack(anchor= W)

#Section 5 (CivilizationsThatReleaseSignals)
slider5 = Scale( root, variable = CivlizationsThatReleaseSignals, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider5.set(20) 
label5 = Label(root, text = "Percentage Of Civilization") 
slider5.pack(anchor = W) 
label5.pack(anchor= W)

#Section 6 (CivilizationsLifetime)
slider6 = Scale( root, variable = LifetimeOfCivilizations, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider6.set(20) 
label6 = Label(root, text = "Length Of Time For Which The Civilization produces signals as a portion of the lifetime of the planet") 
slider6.pack(anchor = W) 
label6.pack(anchor= W)

#Section 6 (MinStars)
slider7 = Scale( root, variable = MinStar, 
           from_ = 0, to = 99999, 
           orient = HORIZONTAL, length=200)  
slider7.set(5000) 
label7 = Label(root, text = "Minimum Number Of Stars") 
slider7.pack(anchor = W) 
label7.pack(anchor= W)

#Section 7 (MaxStars)
slider8 = Scale( root, variable = MaxStar, 
           from_ = 0, to = 100000, 
           orient = HORIZONTAL, length=200) 
slider8.set(10000)  
label8 = Label(root, text = "Maximum Number Of Stars") 
slider8.pack(anchor = W) 
label8.pack(anchor= W)

def SaveSetting(v1, v2, v3,v4,v5,v6,v7,v8,v9):
    File = open("settings.txt", "w")
    Lines = ["Percentage stars that have planets#"+str(v1) + "\n",
              "Percentage of planets that support life#"+str(v2)+ "\n",
              "Percentage of those planets that develop life#"+str(v3)+ "\n",
              "Percentage of those planets that develop intelligent life#"+str(v4)+ "\n",
              "Percentage of that intelligent life that produce signals#"+str(v5)+ "\n",
              "Portion of the lifetime of their planet for which they produce these signals#"+str(v6)+ "\n",
              "Likelihood of a technological civilization forming in a given star#"+str(v7)+ "\n"
              "Minimum number of stars#"+str(v8)+ "\n",
              "Maximum number of stars#"+str(v9)]
    File.writelines(Lines)

def ReadSetting(LineNumber):
    File = open("settings.txt", "r")
    text=File.readlines()
    print(text[LineNumber])
    split=text[LineNumber].split("#")
    if LineNumber <= 5:
        return(float(int(split[1])//100))
    return(int(split[1]))

def save():
    StarsThatHavePlanets: float = slider1.get()
    PlanetsThatSupportLife = slider2.get()
    PlanetsThatDevelopLife = slider3.get()
    PlanetsThatDevelopIntelligentLife = slider4.get()
    CivlizationsThatReleaseSignals = slider5.get()
    LifetimeOfCivilizations = slider6.get()
    MinStar = slider7.get()
    MaxStar = slider8.get()
    CivProbability = StarsThatHavePlanets*PlanetsThatSupportLife*PlanetsThatDevelopLife*PlanetsThatDevelopIntelligentLife*CivlizationsThatReleaseSignals*LifetimeOfCivilizations
    SaveSetting(StarsThatHavePlanets,
                PlanetsThatSupportLife,
                PlanetsThatDevelopLife,
                PlanetsThatDevelopIntelligentLife,
                CivlizationsThatReleaseSignals,
                LifetimeOfCivilizations,
                CivProbability,
                MinStar,
                MaxStar
                )
    
save()

button1 = Button(root, command=save, text="save")
button1.pack(anchor=SE)

root.mainloop()



