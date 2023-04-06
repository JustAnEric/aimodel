import json, re, time, datetime, random

def get_message_probability(json, msg):
  message_certainty = 0
  for word in msg:
    if word in json["keywords"]:
      message_certainty += 1

  percentage = float(message_certainty) / float(len(json["keywords"]))

  if message_certainty > 0:
    return int(percentage*100)
  else: return 0

def CheckProbabilityAndCompare(json,msg):
  highest_prob_list = {}
  def response():
    nonlocal json, highest_prob_list
    highest_prob_list[random.choice(json["responses"])] = get_message_probability(json, msg)

def GetResponse(t):
  loadResponses = json.load(open('./responses_intents.json'))
  sp = re.split(r'\s+|[,;?!.-]\s*', t.lower())
  for word in loadResponses["intents"]:
    if sp[0] in word["keywords"]:
      response = CheckProbabilityAndCompare(word, sp)

  print(f"{response}")
  if response == None:
    response = "My intelligence is unable to understand."
    print("Logged response")
  
  return response