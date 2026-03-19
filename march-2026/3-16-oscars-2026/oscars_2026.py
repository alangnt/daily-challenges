# Oscars 2026 🏆
# Alan

def oscar_pool(predictions):
  oscar_winners = ['One Battle After Another', 'Michael B. Jordan', 'Jessie Buckley', 'Paul Thomas Anderson']
  
  highest_score_friend_name = ''
  highest_score = -1
  tie = False

  for prediction in predictions:
    score = 0
    friend_name = prediction[0]
    prediction = prediction[1:]

    for i in range(len(prediction)):
      if prediction[i] == oscar_winners[i]:
        score += 1
    
    if score > highest_score:
      highest_score = score
      highest_score_friend_name = friend_name
      tie = False
    elif score == highest_score:
      tie = True

  return 'Tie' if tie else highest_score_friend_name
