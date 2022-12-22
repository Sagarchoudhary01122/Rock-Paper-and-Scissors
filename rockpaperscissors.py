import random

def rockpaperscissors():
  
  computer_points = 0
  player_points = 0
  n=1000

  while n!=0:
    computer =['rock' , 'paper' , 'scissors']
    computer_choice = random.choice(computer)
    player = input('Your Choice:-  ')
    
    player_points = player_points
    computer_points=computer_points
    
    if computer_choice==player:
      print('Computer :- ', computer_choice)
      print(' Its Tie  Nobody Wins' )
      print(' Computer Points :- ', computer_points , 'Players Points :- ', player_points )

    elif computer_choice=='rock' and player == 'paper':
      player_points += 1
      print('Computer Choice :- ', computer_choice)
      print(' Player (Paper) Covers computer (Rock) ans Player Wins ') 
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)

    elif computer_choice=='rock' and player=='scissors':
      computer_points += 1
      print('Computer Choice :- ', computer_choice)
      print(' Computer (Rock) smashes Player (Scissors) and Computer Wins' ) 
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)

    elif computer_choice=='paper' and player=='scissors':
      player_points += 1
      print('Computer Choice :- ', computer_choice)
      print(' Player (Scissors) Cuts Computer (Paper) and Player Wins')
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)

    elif computer_choice=='paper' and player=='rock':
      computer_points += 1
      print('Computer Choice :- ', computer_choice)
      print(' Computer (Paper) Covers Player (Rock) and Computer Wins')
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)

    elif computer_choice=='scissors' and player=='rock':
      player_points += 1
      print('Computer Choice :- ', computer_choice)
      print('Player (Rock) smashes Computer (Scissors) and Player Wins')
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)  

    elif computer_choice=='scissors' and player=='paper':
      computer_points += 1
      print('Computer Choice :- ', computer_choice)
      print('Computer (Scissors) Cuts Player (Paper) and Computer Wins')
      print('Computer Points :- ', computer_points , 'Players Points :-', player_points)

    elif player=="END" or player=='End' or player=='end' :
      print('Game is End')
      break
    else:
      print(" Enter Right Value")
    n=n-1  
    
  FinalScore = (f"Final Score is :- Computer Points =  {computer_points} ,Players Points = {player_points}")
  return FinalScore

if __name__ =="__main__":
  print('Lets Play ROCK PAPER SCISSORS Game')
  print("Your Choice - rock , paper , scissors")
  print("If you want to exit this game Type :-  'END'")
  print(rockpaperscissors())
