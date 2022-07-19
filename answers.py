from capitals import states
import random

def game():
  play = ""
  while play != 'q' or play != 'Q':
    play = input('states and capitals game! Guess the right capital of a state and Press the A key to continue or Q to quit: ')
    if play == 'a' or play == 'A':
      win_counter = 0
      wrong_counter = 0
      random.shuffle(states)
      for state in states:
        print('')
        print(f'State: {state["name"]}')
        guess = input('Capital: ')
        if guess == state["capital"] or guess == state["capital"].lower():
          win_counter += 1
          print('')
          print('You were correct!')
          print(f'Correct: {win_counter}')
          print(f'Wrong: {wrong_counter}')
        else:
          wrong_counter = wrong_counter+1
          print('')
          print(f'The correct answer is {state["capital"]}')
          print('')
          print(f'Correct: {win_counter}')
          print(f'Wrong: {wrong_counter}')
          print('')
      print(f'Your score is {win_counter} out of {len(states)}')
      print('')
      play_again = input('Do you want to play again? Enter Y or N: ')
      if play_again == 'Y' or play_again == 'y':
        print('')
        game()
      else:
        print('')
        print(f'Thank you for playing!')
        break
    else:
      break


game() 

