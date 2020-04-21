
from queue import PriorityQueue
from math import sqrt 

from tile import Tile

class Level():
    def __init__(self, game, typemap):
        self.game = game
        self.typemap = typemap
        
        height = len(typemap)
        width = len(typemap[0])

        self.map = [ [None for i in range(width)] for j in range(height)]

        # initing level also inits its tile due to not needing currently init more tiles afterwards

        for h in range(height):
            for w in range(width):
                tile_type = typemap[h][w]
                self.map[h][w] = Tile(tile_type, (h, w), self)

        # view map after generating
        #print("Map in Level:",self.map,"\n")
    
    def get_tile(self, pos):
        return self.map[pos[0]][pos[1]]

    def neighbours_pos(self, tile):
        h = len(self.map)
        w = len(self.map[0])

        tile_pos = tile.pos

        a = [(-1,-1),(-1,0),(-1,+1),(0,+1),(+1,+1),(+1,0),(+1,-1),(0,-1)] 

        neighbours = []

        for pos in a:
            if ( (0 <= tile_pos[0] + pos[0] < h) and (0 <= tile_pos[1] + pos[1] < w) ):
                neighbours.append( self.map[tile_pos[0] + pos[0]][tile_pos[1] + pos[1]] ) 

        return( neighbours )

    def get_movable(self, start_tile, ap): # eka versio vaihdetaan questackkiin
        start_pos = start_tile.pos
        visited = []

        for h in range(len(self.map)):
            visited.append([])
            for w in range(len(self.map[h])):
                visited[h].append((False, None))

        call_queue = PriorityQueue()
        call_queue.put( (0, start_pos) ) #add strat to call queue
        visited[start_pos[0]][start_pos[1]] = (True, 0) # set to visited with cost mov of 0, also highest priority fo call queue

        while not call_queue.empty():
            
            data = call_queue.get()
            
            cost = data[0]
            tile_pos = data[1]
            
            neighbours = self.neighbours_pos(self.map[tile_pos[0]][tile_pos[1]])

            for neighbour in neighbours:
                cost_next = neighbour.mov_cost
                pos_next = neighbour.pos

                if visited[pos_next[0]][pos_next[1]][0] == False and self.map[pos_next[0]][pos_next[1]].unit is None: #check if called pos is visited and is not occupied if we can continue
                    if cost + cost_next < ap: # if we would have ap left after move we will make new call, add pos to call_queue and mark as visited with mov cos
                        call_queue.put( (cost + cost_next, pos_next) )
                        visited[pos_next[0]][pos_next[1]] = (True, cost + cost_next)

                    elif cost + cost_next == ap: # here we dont need to add pos to call que due to not being able to make new calls anyway
                        visited[pos_next[0]][pos_next[1]] = (True, cost + cost_next)

        return visited

    def distance(self, tile, tile_target):
        pos = tile.pos
        pos_target = tile_target.pos

        distance = sqrt((pos[0] - pos_target[0])**2 + (pos[1] - pos_target[1])**2)
        
        return distance

    def get_attackable(self, attacker):
        # does not currently take to account visibility of tiles
        # tile = attacker.tile
        rng = attacker.rng
        
        attackable = []


        for player in self.game.players:
            if player != attacker.player:
                for unit in player.units:
                    if round(self.distance(attacker.tile, unit.tile)) <= rng:
                        attackable.append(unit)

        return attackable

