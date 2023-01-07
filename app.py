from flask import Flask, request, jsonify, abort
from models.hangman_db import HangmanDB
from models.player import Player
from models.room import Room
from models.room_code_gen import room_code_generator

app = Flask('hangman')
db = HangmanDB({},{})
room_code_gen = room_code_generator()

# @app.errorhandler(400)
# def bad_request(e):
    # return jsonify(error=str(e)), 400

@app.route('/status', methods=['GET'])
def status():
    return 'Running!'

@app.route('/login/<name>', methods=['get'])
def login(name: str):
    player = Player(name, '', [])
    db.create_player(player)
    player: Player = db.get_player(name) # type: ignore    
    if player is None:
        abort(404, 'player not found')
    return jsonify(player)
    

@app.route('/room', methods=['GET'])  # type: ignore
def create_room():
    args = request.args
    word = args.get('word', '')
    tries = args.get('tries', '')
    creator = args.get('uid', '')
    #TODO: validate stuff
    room = Room(next(room_code_gen), creator, word, int(tries))
    db.create_room(room)
    return jsonify({
        'room code': room.code
    })

@app.route('/join', methods=['GET'])  # type: ignore
def join_room():
    args = request.args
    room_code = args.get('code', '')
    player_id = args.get('player', '')
    #TODO: validate stuff
    db.move_player(player_id, room_code)
    room: Room = db.get_room(room_code)
    return {
        'word': ['_']*len(room.word),
        'tries': room.tries
    }

@app.route('/guess', methods=['GET'])  # type: ignore
def guess():
    args = request.args
    player_id = args.get('player', '')
    guess = args.get('char', '')
    #TODO: validate stuff
    player = db.get_player(player_id)
    room = db.get_room(player.room)
    if len(player.attempted) >= room.tries:
        abort(400, 'No tries left')
    db.update_attempted(player.uid, guess)
    guessed_word = "".join([char if char in player.attempted else '_' for char in room.word])
    if guessed_word == room.word:
        return f'Congratulations! you guessed the word: {guessed_word}'
    return {
        'word': guessed_word,
        'remaining_tries': room.tries-len(player.attempted)
    }

if __name__ == '__main__':
    app.run(debug=True)
