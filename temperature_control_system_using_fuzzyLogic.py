import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#define fuzzy variables for room temperature and heater power
room_temp = ctrl.Antecedent(np.arange(0,41,1),'room_temp')  # Room temperature (0-40)
heater_power = ctrl.Antecedent(np.arange(0,11,1),'heater_power') # Heater poweer (0-10)

#define fuzzy output variable
temperature = ctrl.Consequent(np.arange(0,41,1),'temperature') # Temperature (0-40)

#Membership functions for room temperature
room_temp['cold'] = fuzz.trimf(room_temp.universe,[0,0,20])
room_temp['warm'] = fuzz.trimf(room_temp.universe,[0,20,40])
room_temp['hot'] = fuzz.trimf(room_temp.universe,[20,40,40])

#Membership functions for heater power
heater_power['low'] = fuzz.trimf(heater_power.universe,[0,0,5])
heater_power['medium'] = fuzz.trimf(heater_power.universe,[0,5,10])
heater_power['high'] = fuzz.trimf(heater_power.universe,[5,10,10])

#Mmembership functions for output temperature
temperature['low'] = fuzz.trimf(temperature.universe,[0,0,20])
temperature['medium'] = fuzz.trimf(temperature.universe,[0,20,40])
temperature['high'] = fuzz.trimf(temperature.universe,[20,40,40])

#define fuzzy rules
rule1 = ctrl.Rule(room_temp['cold'] & heater_power['low'], temperature['low'])
rule2 = ctrl.Rule(room_temp['cold'] & heater_power['medium'], temperature['medium'])
rule3 = ctrl.Rule(room_temp['cold'] & heater_power['high'], temperature['high'])
rule4 = ctrl.Rule(room_temp['warm'] & heater_power['low'], temperature['low'])
rule5 = ctrl.Rule(room_temp['warm'] & heater_power['medium'], temperature['medium'])
rule6 = ctrl.Rule(room_temp['warm'] & heater_power['high'], temperature['high'])
rule7 = ctrl.Rule(room_temp['hot'] & heater_power['low'], temperature['medium'])
rule8 = ctrl.Rule(room_temp['hot'] & heater_power['medium'], temperature['high'])
rule9 = ctrl.Rule(room_temp['hot'] & heater_power['high'], temperature['high'])


#create a control system and simulation
temperature_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
temperature_sim = ctrl.ControlSystemSimulation(temperature_ctrl)

#Input values
temperature_sim.input['room_temp'] = 18 #Room temperature
temperature_sim.input['heater_power'] = 8 # Heater power

#compute the result
temperature_sim.compute()

#output result
print(f"suggested Temperature: {temperature_sim.output['temperature']:.2f}°C")

#plot the membership functions for visualization
room_temp.view()
heater_power.view()
temperature.view()
