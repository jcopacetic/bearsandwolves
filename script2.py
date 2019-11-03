def main():
  pass

if __name__ == '__main__':
  main()
from random import randint



class Character:

  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
    self.race = None
    self.money = 0
    self.sack = []

  def do_damage(self, enemy):
    damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: 
      print(f"{enemy.name} dodged {self.name}'s attack!")
    else: 
      print(f"{self.name} does {damage} damage to {enemy.name}!")
    return enemy.health <= 0

class Potion(Character):

  def __init__(self):
    self.health_increase = randint(5, player.health_max - 3)

  def use(self, player):
    if (player.health + self.health_increase) > player.health_max:
      player.health = player.health_max
    else:
      player.health += self.heath_increase
  
  def describe(self):
    print(f"a potion that heals at last 5 health.")

class Wolf(Character):

  def __init__(self, player):
    Character.__init__(self)
    self.name = "a wolf"
    self.health_max = randint(1, player.health)
    self.health = self.health_max
    self.pay = randint(50, 100)


class Bear(Character):

  def __init__(self, player):
    Character.__init__(self)
    self.name = "a bear"
    self.health_max = randint(5, player.health)
    self.health = self.health_max
    self.pay = randint(100, 150)
  

class Player(Character):

  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
    self.sack = [Potion(),Potion()]

  def quit(self):
    print(f"{self.name} can't find the way back home, and dies of starvation. \nR.I.P.\n\n Made ${self.money} on your adventure!\n\n")
    self.health = 0

  def help(self): 
    print(Commands.keys())

  def status(self): 
    print(f"\n{self.name}'s stuff - \nhealth: {self.health}/{self.health_max}\nmoney: ${self.money}.\n")

  def inventory(self):
    print(self.sack())

  def tired(self):
    print(f"{self.name} feels tired.")
    self.health = max(1, self.health -1)

  def rest(self):
    if self.state != 'normal':
      print(f"{self.name} can't rest now!")
      self.enemy_attacks()
    else:
      print(f"{self.name} rests.")
      if randint(0, 1):
        if randint(0, 1):
          self.enemy = Wolf(self)
        else: 
          self.enemy = Bear(self)
        print(f"{self.name} is rudely awakened by {self.enemy.name}!")
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else:
          print(f"{self.name} slept too much.")
          self.health = self.health - 1
  
  def explore(self):
    if self.state != 'normal':
      print(f"{self.name} is too busy right now!")
      self.enemy_attacks()
    else:
      print(f"{self.name} explores a twisty passage.")
      if randint(0, 1):
        if randint(0, 1):
          self.enemy = Wolf(self)
        else: 
          self.enemy = Bear(self)
        print(f"{self.name} encounters {self.enemy.name}!")
        self.state = "fight"
      else:
        if randint(0, 1):
          self.tired()

  def flee(self):
    if self.state != 'fight':
      print(f"{self.name} runs in circles for a while.")
      self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print(f"{self.name} flees from {self.enemy.name}! {self.name} can explore the cave.")
        self.enemy = None
        self.state = 'normal'
      else:
        print(f"{self.name} couldn't escape from {self.enemy.name}!")
        self.enemy_attacks()

  def attack(self):
    if self.state != 'fight':
      print(f"{self.name} swat the air, without notable results.")
      self.tired()
    else:
      if self.do_damage(self.enemy):
        print(f"{self.name} executes {self.enemy.name}! Gained ${self.enemy.pay}.")
        self.money += self.enemy.pay
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print(f"{self.name} feels stronger!")
      else:
        self.enemy_attacks()

  def check_enemy(self):
    if self.state != 'fight':
      print(f"there's no enemy to check")
    else:
      print (f"\ntype: {self.enemy.name}\nHP: {self.enemy.health}/{self.enemy.health_max}\n")

  def enemy_attacks(self):
    if self.enemy.do_damage(self):
      print(f"{self.name} was slaughtered by {self.enemy.name}!!!\nR.I.P.\n\n Made ${self.money} on your adventure!\n\n")


Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  'check': Player.check_enemy
}

p = Player()
p.name = input("What is your character's name? ")
print(f"(type help to get a list of actions)\n")
print(f"{p.name} enters a dark cave, searching for adventure.")

while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print(f"{p.name} doesn't understand the suggestion.")