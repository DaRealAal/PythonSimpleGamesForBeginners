import random
import time

# Adding repair feature to the robot

Customer_repair_response = ('Your robot is well repaired', 
                            'Your robot is fixed', 
                            'Robot Fixed', 
                            'Successfully fixed the Robot')

random_customer_response = random.choice(Customer_repair_response)

speed_delay = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random_speed_process = random.choice(speed_delay)

random_damage_int = random.randrange(1, 12)

random_batteryD_int = random.randrange(1, 3)

robot_lifecycle = True
cycle = True
charging = True
process_running = True
drilling = True
repairing = True
robot_battery = 99
robot_health = 99
robot_charger_type = 'AC Adapter'
drill_requirement_health = 50

class Engine:
    def __init__(self, spin, drive, drill, sleep_mode, charging):
        self.spin = spin
        self.drive = drive
        self.drill = drill
        self.sleep_mode = sleep_mode
        self.charging = charging
        
class Robot_Info:
    def __init__(self, battery, health, charger_type):
        self.battery = battery
        self.health = health
        self.charger_type = charger_type

    def update_health(self, amount):
        self.health -= amount

    def update_battery(self, amount):
        self.battery -= amount

Robot_action = Engine("spinning...",
                      'driving...', 'drilling...',
                      'The Robot is now in sleep mode...',
                      'Charging...')
Robot_status = Robot_Info(robot_battery, robot_health, robot_charger_type)

while process_running:

    print("What do you want to do?")
    user_choice = input("Robot Action: ")

    if user_choice == 'battery':
        print(Robot_status.battery)
        time.sleep(random_speed_process)
        

    elif user_choice == 'charge':
        charger_ask = input("What charger do you want to charge it with")

        robot_battery -= 1
        Robot_status.battery = robot_battery
        if charger_ask != robot_charger_type:
            print("Invalid charger Please plug-in the right charger!")
        else:
            print(Robot_action.charging)
            while charging:
                robot_battery += 1
                Robot_status.battery = robot_battery
                time.sleep(12)
                if robot_battery == 100:
                    print("The robot charge is full!")
                    
    elif user_choice == 'health':
        print(f"Robot Health: {Robot_status.health}")
        time.sleep(random_speed_process)   

    elif user_choice == 'drill':
        if robot_battery <= 30 and robot_health <= 50:
            print("Your robot need to be fully prepared")
        else:
            robot_health -= random_damage_int
            robot_battery -= random_batteryD_int
            Robot_status.battery = robot_battery
            Robot_status.health = robot_health
            time.sleep(random_speed_process)
            print(Robot_action.drill)
            

    if user_choice == 'quit'.lower():
        print("Have a great day!")
        time.sleep(random_speed_process)
        break
'''    
    elif user_choice == 'repair':
        if robot_health >= 50:
            print("Your robot is function well")
        else:
        print("Repairing the robot...")
             time.sleep(4)
             print(random_customer_response)
'''
    