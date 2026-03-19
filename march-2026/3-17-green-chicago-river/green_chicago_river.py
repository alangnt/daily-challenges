# Green Chicago River ☘️
# Alan

def lucky_river(river, hours):
  new_river = list(river)

  for i in range(len(river)):
    # if river is green
    if river[i] == '☘️':
      for j in range(i, min(i + hours + 1, len(river))):
        new_river[j] = '☘️'

  return new_river
