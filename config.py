
phi = 0
from tkinter import * 

root = Tk()  
root.geometry("900x650") 

StarsThatHavePlanets = 1
PlanetsThatSupportLife = 0.3
PlanetsThatDevelopLife = 0.9
PlanetsThatDevelopIntelligentLife = 0.5
CivlizationsThatReleaseSignals = 0.6
LifetimeOfCivilizations = 0.2
MinStar = 1000
MaxStar = 5000
PercentageBenevolent = 50
EquivalenceRange = 0.2
DesperationGrowthRate = 0.1
VictoryDesperationChange = -500
CivProbability = StarsThatHavePlanets*PlanetsThatSupportLife*PlanetsThatDevelopLife*PlanetsThatDevelopIntelligentLife*CivlizationsThatReleaseSignals*LifetimeOfCivilizations

#Galaxy Generation Factors

#Section 1 (StarsThatHavePlanets)
slider1 = Scale( root, variable = StarsThatHavePlanets, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider1.set(100) 
label1 = Label(root, text = "Percentage Of Stars That have planets") 
slider1.grid(column=0,row=1)
label1.grid(column=0, row=0)

#Section 2 (PlanetsThatSupportLife)
slider2 = Scale( root, variable = PlanetsThatSupportLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider2.set(30)  
label2 = Label(root, text = "Percentage Of Planets That Support Life") 
slider2.grid(column=0,row=3) 
label2.grid(column=0,row=2)

#Section 3 (PlanetsThatDevelopLife)
slider3 = Scale( root, variable = PlanetsThatDevelopLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider3.set(100)  
label3 = Label(root, text = "Percentage Of Planets That Support Life That Go \n On TO Develop Life") 
slider3.grid(column=0,row=5) 
label3.grid(column=0,row=4)

#Section 4 (PlanetsThatDevelopIntelligentLife)
slider4 = Scale( root, variable = PlanetsThatDevelopIntelligentLife, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200) 
slider4.set(50)  
label4 = Label(root, text = "Percentage Of Planets That Develop Life That Go \n On To Develop Intelligent Life") 
slider4.grid(column=0,row=7) 
label4.grid(column=0,row=6)

#Section 5 (CivilizationsThatReleaseSignals)
slider5 = Scale( root, variable = CivlizationsThatReleaseSignals, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider5.set(20) 
label5 = Label(root, text = "Percentage Of Intelligent Life That Release Observable Signals") 
slider5.grid(column=0,row=9) 
label5.grid(column=0,row=8)

#Section 6 (CivilizationsLifetime)
slider6 = Scale( root, variable = LifetimeOfCivilizations, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider6.set(20) 
label6 = Label(root, text = "Length Of Time For Which The Intelligent Life \n produces signals as a portion of the lifetime \n of the planet") 
slider6.grid(column=0,row=11) 
label6.grid(column=0,row=10)

#Galaxy Generation

#Section 6 (MinStars)
slider7 = Scale( root, variable = MinStar, 
           from_ = 0, to = 99999, 
           orient = HORIZONTAL, length=200)  
slider7.set(5000) 
label7 = Label(root, text = "Minimum Number Of Stars") 
slider7.grid(column=1,row=2) 
label7.grid(column=1,row=1)

#Section 7 (MaxStars)
slider8 = Scale( root, variable = MaxStar, 
           from_ = 0, to = 100000, 
           orient = HORIZONTAL, length=200) 
slider8.set(10000)  
label8 = Label(root, text = "Maximum Number Of Stars") 
slider8.grid(column=1,row=4) 
label8.grid(column=1,row=3)

#Civilization Behaviour

#Section 8 (PercentageBenevolent)
slider9 = Scale( root, variable = PercentageBenevolent, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider9.set(50) 
label9 = Label(root, text = "Percentage Of Intelligent Life That Behaves Benevolently Towards \n Other Intelligent Life. Those That Aren't Benevolent Are \n Automatically Malevolent") 
slider9.grid(column=2,row=2) 
label9.grid(column=2,row=1)

#Section 9 (Equivalence range)
slider10 = Scale( root, variable = EquivalenceRange, 
           from_ = 0, to = 50, 
           orient = HORIZONTAL, length=200)  
slider10.set(20) 
label10 = Label(root, text = "Range Of Technology Values For Which Two Civilizations \n Are Considered Equivalent. For Example If The Value \n Is 20 Then Civilizations Within 0.2 Technology Value \n Of Eachother Will Be Considered Equivalent") 
slider10.grid(column=2,row=4) 
label10.grid(column=2,row=3)

#Section 10 (Desperation Growth Rate)
slider11 = Scale( root, variable = DesperationGrowthRate, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL, length=200)  
slider11.set(10) 
label11 = Label(root, text = "The Rate At Which An Intelligent Civilizations Desperation \n Will Grow Passively. For Example If The Growth \n Rate Is Set To 10 And The Civilization Has A \n Tech Value Of 0.1 They Will Gain 100 \n Desperation During That Game Tick. If A Civlization \n Has A Desperation Over 1000 They Are Considered \n Desperate") 
slider11.grid(column=2,row=6) 
label11.grid(column=2,row=5)

#Section 11 (Victory Desperation Change)
slider12 = Scale( root, variable = VictoryDesperationChange, 
           from_ = -1000, to = 1000, 
           orient = HORIZONTAL, length=200) 
slider12.set(-500)  
label12 = Label(root, text = "The Amount Of Desperation A Civilization Gains Or \n Loses After Victory Over Another Civilization, This Includes \n Passive Victories Such As Combining With Another Civilization.") 
slider12.grid(column=2,row=8) 
label12.grid(column=2,row=7)

def SaveSetting(v1, v2, v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13):
    File = open("settings.txt", "w")
    Lines = ["Percentage stars that have planets#"+str(v1) + "\n",
              "Percentage of planets that support life#"+str(v2)+ "\n",
              "Percentage of those planets that develop life#"+str(v3)+ "\n",
              "Percentage of those planets that develop intelligent life#"+str(v4)+ "\n",
              "Percentage of that intelligent life that produce signals#"+str(v5)+ "\n",
              "Portion of the lifetime of their planet for which they produce these signals#"+str(v6)+ "\n",
              "Likelihood of a technological civilization forming in a given star#"+str(v7)+ "\n"
              "Minimum number of stars#"+str(v8)+ "\n",
              "Maximum number of stars#"+str(v9)+ "\n",
              "Percentage Benevolent#"+str(v10)+ "\n",
              "Equivalence range#"+str(v11)+ "\n",
              "Desperation Growth Rate#"+str(v12)+ "\n",
              "Victory Desperation Change#"+str(v13)]
    File.writelines(Lines)

def ReadSetting(LineNumber):
    File = open("settings.txt", "r")
    text=File.readlines()
    split=text[LineNumber].split("#")
    if LineNumber <= 5:
        return(float(int(split[1])//100))
    else:
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
    PercentageBenevolent = slider9.get()
    EquivalanceRange = slider10.get()
    DesperationGrowthRate = slider11.get()
    VictoryDesperationChange = slider12.get()
    CivProbability = StarsThatHavePlanets*PlanetsThatSupportLife*PlanetsThatDevelopLife*PlanetsThatDevelopIntelligentLife*CivlizationsThatReleaseSignals*LifetimeOfCivilizations
    SaveSetting(StarsThatHavePlanets,
                PlanetsThatSupportLife,
                PlanetsThatDevelopLife,
                PlanetsThatDevelopIntelligentLife,
                CivlizationsThatReleaseSignals,
                LifetimeOfCivilizations,
                CivProbability,
                MinStar,
                MaxStar,
                PercentageBenevolent,
                EquivalanceRange,
                DesperationGrowthRate,
                VictoryDesperationChange
                )
    
save()

button1 = Button(root, command=save, text="save")
button1.grid(column=2,row=11)
button2 = Button(root, command=root.destroy, text="close")
button2.grid(column=2,row=10)
root.mainloop()



