
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

    def neighbours(self, tile):
        # returns array of tile objects wich are neighbours of tile

        h = len(self.map)
        w = len(self.map[0])

        tile_pos = tile.pos

        a = [(-1,-1),(-1,0),(-1,+1),(0,+1),(+1,+1),(+1,0),(+1,-1),(0,-1)] 

        neighbours = []

        for pos in a:
            if ( (0 <= tile_pos[0] + pos[0] < h) and (0 <= tile_pos[1] + pos[1] < w) ):
                neighbours.append( self.map[tile_pos[0] + pos[0]][tile_pos[1] + pos[1]] ) 

        return( neighbours )

    def find_closest_movable(self, start_tile, end_tile, ap):
        movable = self.get_movable(start_tile, ap)
        self.game.movable = movable

        closest_movable = end_tile

        print("finding from", start_tile.pos, "to (castle pos)", end_tile.pos)

        while not movable[closest_movable.pos[0]][closest_movable.pos[1]][0]:
            print("closest_moveble.pos:", closest_movable.pos)

            neighbours = self.neighbours(closest_movable)
            for n in movable:
                print(n)

            print("")

            lowest_n = neighbours[0]

            for n in neighbours:
                if movable[n.pos[0]][n.pos[1]][1] != None and movable[lowest_n.pos[0]][lowest_n.pos[1]][1] != None:
                    if movable[n.pos[0]][n.pos[1]][1] < movable[lowest_n.pos[0]][lowest_n.pos[1]][1]:
                        lowest_n = n

            closest_movable = lowest_n

            if closest_movable == start_tile:
                break
        
        print("new closest:",closest_movable.pos,"\n")
        return(closest_movable)

    def get_movable(self, start_tile, ap):
        start_pos = start_tile.pos
        visited = []

        for h in range(len(self.map)):
            visited.append([])
            for w in range(len(self.map[h])):
                visited[h].append((None, None))

        call_queue = PriorityQueue()
        call_queue.put( (0, start_pos) ) #add start to call queue
        visited[start_pos[0]][start_pos[1]] = (True, 0) # set to visited with cost mov of 0, also highest priority fo call queue

        while not call_queue.empty():
            
            data = call_queue.get()
            
            cost = data[0]
            tile_pos = data[1]
            
            neighbours = self.neighbours(self.map[tile_pos[0]][tile_pos[1]])

            for neighbour in neighbours:
                cost_next = neighbour.mov_cost
                pos_next = neighbour.pos

                if visited[pos_next[0]][pos_next[1]][0] == None and self.map[pos_next[0]][pos_next[1]].unit is None: #check if called pos is visited and is not occupied if we can continue
                    if cost + cost_next < ap: # if we would have ap left after move we will make new call, add pos to call_queue and mark as visited with mov cos
                        call_queue.put( (cost + cost_next, pos_next) )
                        visited[pos_next[0]][pos_next[1]] = (True, cost + cost_next)

                    elif cost + cost_next == ap: # border of movement
                        call_queue.put( (cost + cost_next, pos_next) )
                        visited[pos_next[0]][pos_next[1]] = (True, cost + cost_next)

                    else:
                        call_queue.put( (cost + cost_next, pos_next) )
                        visited[pos_next[0]][pos_next[1]] = (False, cost + cost_next)

                elif visited[pos_next[0]][pos_next[1]][0] == None:
                    call_queue.put( (cost + cost_next, pos_next) )
                    visited[pos_next[0]][pos_next[1]] = (False, cost + cost_next)

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

    

