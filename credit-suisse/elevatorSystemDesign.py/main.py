import time
from datetime import datetime

class Elevator:
  def __init__(self, bottom, top):
    self.bottom = bottom
    self.top = top

  def move(self, direction, current_floor):
    current_floor = current_floor
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print (str(current_floor) + " | Current Time: " + str(current_time))
    if direction == 1:
      while current_floor < self.top:
        time.sleep(1)
        current_floor += 1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print (str(current_floor) + " | Current Time: " + str(current_time))
        
    else:
      while current_floor > self.bottom:
        time.sleep(1)
        current_floor -= 1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print (str(current_floor) + " | Current Time: " + str(current_time))


  # Select floors internally method
  def select_floors(self, current_floor, destination_floors: list):
    destination_floors = list(dict.fromkeys(destination_floors)) # Remove duplicate floors from destination
    if current_floor in destination_floors:
      destination_floors.remove(current_floor) # Remove current floor from destination floor, since it wouldnt make sense for user to travel to current floor
    above_floors = []
    below_floors = []
    steps = []

    for floors in destination_floors:
      if floors > current_floor:
        above_floors.append(floors)

      else:
        below_floors.append(floors)

    above_floors.sort()
    below_floors.sort()

    # Case 1: All destination floors below current floor
    if above_floors == []:
      for floor in below_floors[::-1]:
        move_number = current_floor - floor
        current_floor = floor
        for i in move_number:
          steps.append("DOWN_1")
        steps.append("OPEN_DOOR")
        steps.append("CLOSE_DOOR")
          
    # Case 2: All destination floors above current floor
    elif below_floors == []:
      for floor in above_floors:
        move_number = floor - current_floor
        current_floor = floor
        for i in move_number:
          steps.append("UP_1")
        steps.append("OPEN_DOOR")
        steps.append("CLOSE_DOOR")

    # Case 3: Multiple floors in different directions
    else:
      top_movement = above_floors[-1] - current_floor
      bottom_movement = current_floor - below_floors[0]
      
      # Condition to check which has the bigger difference in floors (Top/Bottom)
      if top_movement < bottom_movement:
        # Clear above floors first
        for floor in above_floors:
          move_number = floor - current_floor
          current_floor = floor
          for i in range(move_number):
            steps.append("UP_1")
          steps.append("OPEN_DOOR")
          steps.append("CLOSE_DOOR")

        for floor in below_floors[::-1]:
          move_number = current_floor - floor
          current_floor = floor
          for i in range(move_number):
            steps.append("DOWN_1")
          steps.append("OPEN_DOOR")
          steps.append("CLOSE_DOOR")

      else:
        # Clear bottom floors first
        for floor in below_floors[::-1]:
          move_number = current_floor - floor
          current_floor = floor
          for i in range(move_number):
            steps.append("DOWN_1")
          steps.append("OPEN_DOOR")
          steps.append("CLOSE_DOOR")

        for floor in above_floors:
          move_number = floor - current_floor
          current_floor = floor
          for i in range(move_number):
            steps.append("UP_1")
          steps.append("OPEN_DOOR")
          steps.append("CLOSE_DOOR")
          
        return steps

  # Choose floors externally method
  def choose_floors(self, current_floor, direction, source: list):
    steps_number = abs(self.source_floor - current_floor)
    steps = []

    # Simplest case if got nobody in the lift and only one source
    for i in range(steps_number):
      if self.source_floor > current_floor:
        steps.append("DOWN_1")
      else:
        steps.append("UP_1")

    steps.append("OPEN_DOOR")
    steps.append("CLOSE_DOOR")


# Class for the monitoring of elevator motion
class MovingElevator:
  def __init__(self, elevator):
    self.elevator = elevator

  # Elevator Controller, Monitor and move according to issue_select
  def issue_select_floor(self, current_floor, destination_floors):
    steps = self.elevator.select_floors(current_floor, destination_floors)

    for index, step in enumerate(steps):
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      time.sleep(1)
      print(step + " | Current Time: " + str(current_time))
      if step == "DOWN_1":
        current_floor -= 1
        door_status = "Door Closed"
        direction = "DOWN"
        print (str(current_floor) + " " + door_status + " " + direction)

      elif step == "UP_1":
        current_floor += 1
        door_status = "Door Closed"
        direction = "UP"
        print (str(current_floor) + " " + door_status + " " + direction)

      elif step == "OPEN_DOOR":
        door_status = "Door Opened"
        if steps[index-1] == "DOWN_1":
          direction = "DOWN"
        else:
          direction = "UP"
        print (str(current_floor) + " " + door_status + " " + direction)

      # Close door situation
      else:
        door_status = "Door Closed"
        if steps[index-2] == "DOWN_1":
          direction = "DOWN"
        else:
          direction = "UP"
        print (str(current_floor) + " " + door_status + " " + direction)


# Test run the code
elevator2 = Elevator(0,10)
elevatorController = MovingElevator(elevator2)
print(elevatorController.issue_select_floor(5, [1,4,4,2,7,8,10]))

# elevatorController.try_move(-1,3)