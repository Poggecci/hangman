from dataclasses import dataclass
from .player import Player
from .room import Room
from typing import Dict

@dataclass
class HangmanDB:
    rooms: Dict[str, Room]
    players: Dict[str, Player]

    def create_room(self, room: Room):
        if room.code not in self.rooms:
            self.rooms[room.code] = room

    def get_room(self, room_code: str):
        if room_code not in self.rooms:
            raise KeyError('Room not found in db')
        return self.rooms[room_code]

    def create_player(self, player: Player):
        self.players[player.uid] = player
    
    def move_player(self, player_id: str, room_id: str):
        if room_id not in self.rooms:
            raise KeyError(f'{room_id} not found in db')
        if player_id not in self.players:
            raise KeyError(f'{player_id} not found in db')
        
        self.players[player_id].room = room_id
    
    def update_attempted(self, player_id: str, guess: str):
        if player_id not in self.players:
            raise KeyError(f'{player_id} not found in db')
        player = self.players[player_id]
        if guess not in player.attempted:
            player.attempted.append(guess)
    
    def get_player(self, player_id: str):
        return self.players[player_id]