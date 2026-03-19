# World Wide Web 🌐 
# Codédex

def check_url(address):

  if address.startswith('https://'):
    domain = address[8:]
  elif address.startswith('http://'):
    domain = address[7:]
  else:
    return 'invalid'
  
  if '.' not in domain:
    return 'invalid'
  for char in domain:
    if not (char.isalpha() or char.isdigit() or char == '-' or char == '.'):
      return 'invalid'
    
  return 'valid'
