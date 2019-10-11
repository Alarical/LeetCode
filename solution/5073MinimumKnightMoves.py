class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque
        x , y = abs(x) , abs(y)
        DST = (x,y)
        start = (0,0)
        to_moves = {start:0}
        queue = deque([start])
        dirs = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        MAX_X = x+4
        MAX_Y = y+4
        while queue:
            cur_cell = queue.popleft()
            moves = to_moves[cur_cell]
            if cur_cell == DST:
                return moves
            x,y = cur_cell
            for dx ,dy in dirs:
                nx = dx+x
                ny = dy+y
                if not (-4<= nx <=MAX_X and -4<= ny <=MAX_Y):
                    continue
                next_cell = (nx , ny)
                last_moves = to_moves.get(next_cell , None)
                if last_moves == None:
                    queue.append(next_cell)
                    to_moves[next_cell] = moves+1