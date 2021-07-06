2021.07.06

def minion_game(S):
    # your code goes here
      stuart = 0
      kevin = 0
      vowels = ('A','E','I','O','U')

      for idx, s in enumerate(S):
          if s in vowels:
            kevin += len(S) - idx
          else:
            stuart += len(S) - idx

      if stuart > kevin:
          print('Stuart', stuart)
      elif kevin > stuart:
          print('Kevin', kevin)
      else:
          print('Draw')