from flask import Flask, jsonify, abort, request
from vote_characters import votesCharacters

# A simple votting app to see who is the most popular Diablo 4 class

app = Flask(__name__, static_url_path='', static_folder='html')

chars = [
         {'name':'Necromancer'},
         {'name':'Sorcerer'},
         {'name':'Barbarian'},
         {'name':'Rogue'},
         {'name':'Druid'},
         ]

# Request to get all characters names
@app.route('/characters', methods=['GET'])
def getAllCharnames():
    return jsonify(chars)


# Votting on a character and getting the ip address from where the vote came from
# https://stackoverflow.com/questions/3759981/get-ip-address-of-visitors-using-flask-for-python
@app.route('/vote/<charactername>', methods=['POST'])
def voteCharnames(charactername):
    
    ip_address = request.remote_addr
    data = (charactername, ip_address)
    vote_id = votesCharacters.createVote(data)

    return jsonify({'id':vote_id})


#################################################################
# Getting the amount of votes for a specific character
@app.route('/vote/<charactername>', methods=['GET'])
def getVotesChar(charactername):
    count = votesCharacters.countCharactersVotes(charactername)
    return jsonify({charactername:count})



# Getting the a list of names and votes of all characters
@app.route('/vote', methods=['GET'])
def geAllChar():
    allCharCounts = []

    # Looping thru all the characters and their votes and appending it to the empty array created above and printing the result
    for character in chars:
        charactername = character['name']
        count = votesCharacters.countCharactersVotes(charactername)
        allCharCounts.append({charactername:count})
    
    return jsonify(allCharCounts)



##### Do the delete all votes function

@app.route('/vote/all', methods=['delete'])
def deleteALLVotes():
    return jsonify({'done':True})



# Running the server
if __name__ == "__main__":
    app.run(debug=True)
