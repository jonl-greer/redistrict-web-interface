from rapidfuzz import process

def validate_data(precints,election):
  precinct_names = precincts.iloc[:,0].astype(str).tolist()
  election_names = election.iloc[:,0].astype(str).tolist()

  statuses = []
  matches = []

  for name in precinct_names:
    match,score,_= process.extractOne(name, election_names)
    matches.append(match)

    if score < 70:
      statuses.append("bad")
    elif score < 90:
      statuses.append("warning")
    else:
      statuses.append("good")

  precints["matched_name"] = matches
  precints["status"] = statuses 
  return precincts
