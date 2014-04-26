#!/usr/bin/env python
# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

import math
import random

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = float(x)
        self.y = float(y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = float(speed * math.cos(math.radians(angle)))
        delta_x = float(speed * math.sin(math.radians(angle)))
        # Add that to the existing position
        new_x = float(old_x + delta_x)
        new_y = float(old_y + delta_y)
        return Position(new_x, new_y)
    def __str__(self):
      return "Position with x="+ str(self.x) \
          + " and y=" + str(self.y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        assert (width > 0)
        assert (height > 0)
        self.width = width
        self.height = height
        self.cleanList = []
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        assert(pos.x >= 0 and pos.x <= self.width)
        assert(pos.y >= 0 and pos.y <= self.height)
        x = int(pos.x)
        y = int(pos.y)
        if (x, y) not in self.cleanList:
          self.cleanList.append((x, y))
        return self.cleanList
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        if (m, n) not in self.cleanList:
          return False
        return True
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return self.width*self.height
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return len(self.cleanList)
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        randX = random.randrange(0, self.width + 1)
        randY = random.randrange(0, self.height + 1)
        return Position(randX, randY)
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        if((pos.x >= 0 and pos.x <= self.width) and \
           (pos.y >= 0 and pos.y <= self.height)):
          return True
        return False


'''
room = RectangularRoom(20,10)
pos = Position(3, 5)
pos1 = room.getRandomPosition()
pos2 = room.getRandomPosition()
pos3 = room.getRandomPosition()
room.cleanTileAtPosition(pos)
room.cleanTileAtPosition(pos1)
room.cleanTileAtPosition(pos2)
room.cleanTileAtPosition(pos3)
room.cleanTileAtPosition(pos)
print(room.isTileCleaned(pos1.x, pos1.y))
print(room.getNumCleanedTiles())
print(room.cleanList)
'''

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        # TODO: Your code goes here
        self.room = room
        self.speed = speed
        self.position = Position(random.randrange(0, room.width + 1), \
                                 random.randrange(0, room.height + 1))
        self.direct = random.randrange(0,360)
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.position
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.direct
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.position = position
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.direct = direction


class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        self.room.cleanTileAtPosition(self.position)
        #print(self.position)
        new_position = self.position.getNewPosition(self.direct,\
                                                     self.speed)
        while not self.room.isPositionInRoom(new_position):
          #print("outside pos")
          #print(new_position)
          if(new_position.x <= 0):
            self.direct = random.randrange(0, 180)
          elif(new_position.x >= self.room.width):
            self.direct = random.randrange(180, 360)
          if(new_position.y <= 0):
            self.direct = random.randrange(-90,90)
          elif(new_position.y >= self.room.height):
            self.direct = random.randrange(90, 270)
          if(new_position.x <= 0 and new_position.y <= 0):
            self.direct = random.randrange(0, 90)
          elif(new_position.x <= 0 and\
               new_position.y >= self.room.height):
            self.direct = random.randrange(90,180)
          elif(new_position.x >= self.room.width and\
               new_position.y >= self.room.height):
            self.direct = random.randrange(180, 270)
          elif(new_position.x >= self.room.width and\
               new_position.y <= 0):
            self.direct = random.randrange(270, 360)
          #print("angle is %d"%self.direct)
          new_position = self.position.getNewPosition(self.direct,\
                                                       self.speed)
          #print("try new pos")
          #print(new_position)
        self.position = new_position
        #print("self.position")
        #print(self.position)


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here
    sim_list_lists = []
    for l in range(num_trials):
      sim_list_lists.append([])
    #Trials:
    for i in range(num_trials):
      room = RectangularRoom(width, height)
      robots = []
      for r in range(num_robots):
        bot = robot_type(room, speed)
        robots.append(bot)
      coverage = 0.0
      while(coverage < min_coverage):
        for r in range(num_robots):
          robots[r].updatePositionAndClean()  
          #print(robots[r].position)
        coverage = float(len(room.cleanList))/room.getNumTiles()
        sim_list_lists[i].append(coverage)
      #print(coverage)
      print(room.cleanList)
      #print(sim_list_lists)
      print("The %dth trial took %d steps."%(i, len(sim_list_lists[i])))
      

runSimulation(1, 1.0, 5, 5, 1.0, 5, Robot, False)
# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        self.room.cleanTileAtPosition(self.position)
        self.direct = random.randrange(0, 360)
        if(self.position.x == 0):
          self.direct = random.randrange(0, 180)
        elif(self.position.x == self.room.width):
          self.direct = random.randrange(180, 360)
        if(self.position.y == 0):
          self.direct = random.randrange(-90,90)
        elif(self.position.y == self.room.height):
          self.direct = random.randrange(90, 270)
        if(self.position.x == 0 and self.position.y == 0):
          self.direct = random.randrange(0, 90)
        elif(self.position.x == 0 and\
             self.position.y == self.room.height):
          self.direct = random.randrange(90,180)
        elif(self.position.x == self.room.width and\
             self.position.y == self.room.height):
          self.direct = random.randrange(180, 270)
        elif(self.position.x == self.room.width and\
             self.position.y == 0):
          self.direct = random.randrange(270, 360)
        self.position = self.position.getNewPosition(self.direct, self.speed)


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here
