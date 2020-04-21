from queue import PriorityQueue

class Map():

    def __init__(self):
        self.matrix = [[1,2,2,1,1],[1,2,1,1,1],[1,1,1,3,3],[2,1,1,3,3],[2,2,1,1,1]]

    def mov_val(self, pos):
        return self.matrix[pos[0]][pos[1]]

    def print_vals(self, arr):
        v = []

        for i in arr:
            v.append(self.mov_val(i))

        print("values",v)
        
    def sort(self, n):

        def rec(n):
            l = len(n)

            if l == 1:
                return n
            elif l == 2:
                if self.mov_val(n[0]) <= self.mov_val(n[1]):
                    return n
                else:
                    return [n[1], n[0]]
            else:
                n1 = rec(n[:(l//2)])
                n2 = rec(n[(l//2):])

                sorted = []

                i = 0
                j = 0

                while len(sorted) < l:
                    if i == len(n1):
                        sorted.append(n2[j])
                        j += 1
                    elif i == len(n2):
                        sorted.append(n1[i])
                        i += 1
                    elif self.mov_val(n1[i]) <= self.mov_val(n2[j]):
                        sorted.append(n1[i])
                        i += 1
                    else:
                        sorted.append(n2[j])
                        j += 1

                return sorted

        sorted = rec(n)

        return sorted

    def remove_not_movable(self, n, ap):
        pass

    def get_movable(self, tile, ap): # eka versio vaihdetaan questackkiin

        visited = []

        for h in range(len(self.matrix)):
            visited.append([])
            for w in range(len(self.matrix[h])):
                visited[h].append((False, None))

        #visited = len(self.matrix) * [len(self.matrix[]) * [False]] #matrix corresponding to map for visited

        #remove_not_movable
        #remove visited

        def DFS(tile, ap):
            n = self.neighbours_pos(tile) #get neighbours for tile
            n = self.sort(n) # sort for DFS to iterrete throught in min cost order

            visited[tile[0]][tile[1]] = (True, ap) #tile called to visited
            self.print_pretty(visited)
            print("")

            #print("\n",tile,"\n")
            #self.print_pretty(visited)

            for pos in n:
                cost = self.mov_val(pos)

                if visited[pos[0]][pos[1]][0] == False: #if called pos has not been visited we can continue
                    if ap - cost < 0:
                        pass # if ap is smaller than 0 we cannot visit the tile
                    elif ap - cost == 0:
                        visited[pos[0]][pos[1]] = (True, 0) # if ap goes to 0 we dont need to call DFS again
                    else:
                        DFS(pos, ap - cost) # calling dfs we don need returns as all information is strored to local visited

        DFS(tile, ap)

        visited[tile[0]][tile[1]] = (False, None) # set start to prevent moving to same tile

        return visited

    def get_movable2(self, start_tile, ap): # eka versio vaihdetaan questackkiin

        visited = []
        for h in range(len(self.matrix)):
            visited.append([])
            for w in range(len(self.matrix[h])):
                visited[h].append((False, None))

        call_queue = PriorityQueue()
        call_queue.put( (0, start_tile) ) #add strat to call queue
        visited[start_tile[0]][start_tile[1]] = (True, 0) # set to visited with cost mov of 0, also highest priority fo call queue

        while not call_queue.empty():
            
            data = call_queue.get()
            
            cost = data[0]
            tile = data[1]
            
            print("call", tile, cost)
            
            neighbours = self.neighbours_pos(tile)

            for pos in neighbours:
                cost_next = self.mov_val(pos)

                if visited[pos[0]][pos[1]][0] == False: #check if called pos is visited and if we can continue

                    if cost + cost_next < ap: # if we would have ap left after move we will make new call, add pos to call_queue and mark as visited with mov cos
                        print("new call adde to queue", ap, cost + cost_next)
                        call_queue.put( (cost + cost_next, pos) )
                        visited[pos[0]][pos[1]] = (True, cost + cost_next)

                    elif cost + cost_next == ap: # here we dont need to add pos to call que due to not being able to make new calls anyway
                        print("zerop cost cond met", pos, cost + cost_next, ap)
                        visited[pos[0]][pos[1]] = (True, cost + cost_next)

        print("called")

        return visited

    def neighbours_pos(self, tile):
        h = len(self.matrix)
        w = len(self.matrix[0])

        a = [(-1,-1),(-1,0),(-1,+1),(0,+1),(+1,+1),(+1,0),(+1,-1),(0,-1)] 

        positions = []

        for pos in a: 
            if ( (0 <= tile[0] + pos[0] < h) and (0 <= tile[1] + pos[1] < w) ):
                positions.append( ( tile[0] + pos[0] , tile[1] + pos[1]) ) 

        return( positions )

    def print_pretty(self, m):
        for a in m:
            print(a)

if __name__ == '__main__':
    m = Map()
    n = m.neighbours_pos((1,1))
    print("")

    mov = m.get_movable2((0,0), 4)
    m.print_pretty(mov)




