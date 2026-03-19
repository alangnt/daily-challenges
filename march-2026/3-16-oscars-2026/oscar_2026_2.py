# Oscars 2026 🏆
# Valérie

def oscar_pool(predictions):
  # Write code below 💖
  winners = ['One Battle After Another', 'Michael B. Jordan', 'Jessie Buckley', 'Paul Thomas Anderson']
  max_score = -1
  winner_name = ''
    
  for friend in predictions:
    name = friend[0]
    preds = friend[1:]
    score = 0
        
  for i in range(len(winners)):
    if preds[i] == winners[i]:
      score += 1
                
    if score > max_score:
      max_score = score
      winner_name = name
    elif score == max_score:
      winner_name = 'Tie'
            
  return winner_name
