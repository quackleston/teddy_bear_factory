""""
notes:

finished:
- creating
- singing
- stop singing
- deteriorating
- repairing
- paw press
- spider

in progress:
- choose interaction
- you have to cook food for teddy

ideas:
- teddy bear has a level
- you can play with teddy bear
- start predetermined game
- mood change 
- + food = + mood
- overfeed = die
- you can invent food
- add into inventory of food
"""""

# A PROGRAM FOR TEDDY BEARS

class TeddyBear:

    # INITIAL
    def __init__(self, name, color, material, expression, condition):
        self.name = name
        self.color = color
        self.material = material
        self.expression = expression
        self.condition = condition
        self.level = 0

    # INTERACTIONS WITH TEDDY BEAR
    def action(self):
        interact = input("next action:\n> ")
        print("")
        if interact == "view menu" or interact == "view action menu" or interact == "action menu" or interact == "menu":
            self.actionMenu()
        elif interact == "view profile" or interact == "profile":
            self.profile()
            self.action()
        elif interact == "view condition" or interact == "get condition":
            self.getCondition()
        elif interact == "view level" or interact == "get level":
            self.getCondition()
        elif interact == "sing":
            self.sing()
        elif interact == "stop singing":
            self.stopSing()
        elif interact == "deteriorate":
            self.deteriorate()
        elif interact == "repair":
            self.repair()
        elif interact == "make food":
            self.makeFood()
        elif interact == "paw press":
            self.pawPress()
        elif interact == "spider":
            self.spider()

        # ACTIONS MENU

    def actionMenu(self):
        print("A C T I O N S :")
        print("view menu\nview profile\nview condition\nview level\nsing\nstop singing\ndeteriorate\nrepair\nmake food\npaw "
              "press\nspider\n")
        self.action()

    # TEDDY BEAR PROFILE
    def profile(self):
        print(f"T E D D Y  B E A R\nP R O F I L E")
        print(f"name: {self.name}\ncolor: {self.color}\nmaterial: {self.material}"
              f"\nexpression: {self.expression}\ncondition: {self.condition}\nlevel: {self.level}\n")

    # GETTING BEAR'S CONDITION
    def getCondition(self):
        print(f"current condition: {self.condition}\n")
        self.action()

    # GETTING BEAR'S LEVEL
    def getLevel(self):
        print(f"current condition: {self.condition}\n")
        self.action()

    # MAKE TEDDY BEAR SING
    def sing(self):
        print("♫ baby shark doo doo do-do do-doo ♫\n")
        self.action()

    # STOP TEDDY BEAR'S SINGING
    def stopSing(self):
        print("SINGING STOPPED\n")
        self.action()

    # TEDDY BEAR DETERIORATES
    def deteriorate(self):
        conditions = ["excellent", "very good", "good", "decent", "poor", "very poor", "unrecognizable"]
        if self.condition in conditions and self.condition != "unrecognizable":
            for i in range(len(conditions)):
                if conditions[i] == self.condition:
                    self.condition = conditions[i + 1]
                    break
        print(f"⚠ your teddy bear deteriorated!")
        self.getCondition()
        repairAsk = input("would you like to repair your teddy bear?(y/n)\n> ")
        if repairAsk == "y":
            print("")
            self.repair()
        else:
            print("poor teddy bear")
            self.action()

    # REPAIRING TEDDY BEAR
    def repair(self):
        conditions = ["excellent", "very good", "good", "decent", "poor", "very poor", "good"]
        self.condition = conditions[0]
        print(f"REPAIRING TEDDY BEAR...\n")
        print(f"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ teddy bear repaired!")
        self.getCondition()
        self.action()

    # TEDDY BEAR PAW PRESS
    def pawPress(self):
        print(f"my name is {self.name} and i'm {self.expression}\n")
        self.action()

    # GAME 1: SPIDER
    def spider(self):
        kill = input("へ(⚈益⚈)へ THERE IS A SPIDER!\nkill by typing in kill 3 times!\n> ")
        if kill == "killkillkill" or kill == "kill kill kill":
            self.level += 1
            print(f"\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ spider defeated! \nlevel up: {self.level - 1} -> {self.level}\n")
            self.action()
        else:
            print("\nଘ(ﾉºัᴗºั)ﾉ☆ﾟ*:. teddy bear has expired from this world\n")
            restart = input("G A M E  O V E R\nrestart?(y/n)\n> ")
            if restart == "y":
                # l = []
                print("\nN E W  T E D D Y  B E A R")
                newName = input("name: ")
                self.name = newName
                newColor = input("color: ")
                self.color = newColor
                newMat = input("material: ")
                self.material = newMat
                newEx = input("expression: ")
                self.expression = newEx
                newCon = input("condition: ")
                self.condition = newCon
                self.level = 0

                self.profile()

            else:
                pass

    # FOOD
    def makeFood(self):
        foodList = ["pancakes", "scrambled eggs", "sandwich", "ramen", "sushi", "pizza", "ice cream", "fries", "hamburger"]
        foods = "\n".join(foodList)
        print(f"F O O D  M E N U\n{foods}")
        whatFood = input("\nwhat food would you like to cook?\n> ")

    # ?
    def template(self):
        pass


# START
teddy = TeddyBear("brownie", "white", "cotton", "confused", "excellent")
teddy.profile()
teddy.actionMenu()
