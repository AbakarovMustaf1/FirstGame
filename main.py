from random import randint
chislo_popitok = 1
ball = 1
balls = []
while chislo_popitok <=5:
  chislo_popitok += 1
  a = int(input("Введите число от 1 до 6  ? "))
  b = randint(1,6)
  difference = abs(a - b)

  if difference == 0:
    ball = 6
    balls.append(ball)
  elif difference == 1:
    ball = 5
    balls.append(ball)
  elif difference == 2:
    ball = 4
    balls.append(ball)
  elif difference == 3:
    ball = 3
    balls.append(ball)
  elif difference == 4:
    ball = 2
    balls.append(ball)
  elif difference == 5:
    ball = 1
    balls.append(ball)

    print("Ваш балл" , ball)

all_ball = sum(balls)
print("Количество очков", all_ball)

if all_ball < 25:
  print("Вы проиграли")
else:
  print("Вы выиграли ")
