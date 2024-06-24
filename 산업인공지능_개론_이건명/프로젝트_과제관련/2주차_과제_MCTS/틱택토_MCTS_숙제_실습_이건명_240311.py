from abc import ABC, abstractmethod
from collections import defaultdict
import math

class MCTS:
    "Monte Carlo tree searcher. 먼저 rollout한 다음, 위치(move) 선택 "
    def _init_(self, c=1):
        self.Q = defaultdict(int)
        self.N = defaultdict(int)
        self.children = dict()
        self.c = c
        
    def choose(self, node):
        "node의 최선인 자식 노드 선택"
        if node.is_terminal():
            raise RuntimeError(f"choose called onterminal node {node}")
        if node not in self.children:
            return node.find_random_child()
        
        def score(n):
            if self.N[n]==0:
                return float("-int")
            return self.Q[n] / self.N[n]
        
        return max(self.children[node], key=score)
    
        def do_rollout(self, node):
            "게임 트리에서 한 층만 더 보기"
            path = self._select(node)
            leaf = path[-1]
            self ._expand(leaf)
            reward = self ._simulate(leaf)
            self ._backpropagate(path, reward)
            
    def _select(self, node):
        "node의 아직 시도해보지 않은 자식 노드 찾기 "
        path = []
        while True:
            path.append(node)
            if node not in self.children or not self.children[node]:
                # node의 child나 grandchild가 아닌 경우: 아직 시도해보지 않은 것 또는 단말 노드
                return path
            unexplored = self.children[node] - self.children.keys()
            if unexplored:
                n = unexplored.pop()
                path.append(n)
                return path
            node = self. _uct_select(node)
    def _expand(self, node):
        "children에 node의 자식노드 추가"
        if node in self.children:
            return
        self.children[node] = node.find_children( )
        
    def _simulate(self, node):
        "node의 무작위 시뮬레이션에 대한 결과(reward) 반환"
        invert_reward = True
        while True:
           if node.is_terminal():
               reward = node.reward()
               return 1 - reward if invert_reward else reward
           node = node.find_random_child()
           invert_reward = not invert_reward
    
    def _backpropagate(self , path, reward):
        " 단말 노드의 조상 노드들에게 보상 (reward) 전달 "
        for node in reversed (path):
            self.N[node] += 1
            self.Q[node] += reward
            reward = 1 - reward
        
    def _uct_select(self, node):
        "탐험(exploration)과 이용 (exploitation)의 균형을 맞춰 node의 자식 노드 선택 "
        # node 의 모든 자신 노드가 이미 확장되었는지 확인
        assert all(n in self .children for n in self.children[node])
        log_N_vertex = math.log (self.N[node])
        
        def uct(n):
            "UCB(Upper confidence bound) 점수 계산 "
            return self.Q[n] / self.N[n] + self.c * math.sqrt(2 * log_N_vertex / self.N[n])
        
        return max(self. children[node], key=uct )
    
class Node(ABC):
    " 게임 트리의 노드로서 보드판의 상태 표현 "
    @abstractmethod
    def find_chileren(self):
        return set()
    
    @abstractmethod
    def find_random_child(self):
        return None
    
    @abstractmethod
    def is_terminal(self):
        return True
    
    @abstractmethod
    def reward(self):
       return 0
   
    @abstractmethod
    def _hash_(self):
        return 123456789
    
    @abstractmethod
    def _eq_(node1, node2):
        return True
    
from collections import namedtuple
from random import choice
#from monte_carlo_tree_search import MCTS, Node

TTTB = namedtuple("TicTacToeBoard", "tup turn winner terminal") 

class TicTacToeBoard(TTTB,Node):
    def find_children(board):
       if board.terminal:
            return set()
       return{
            board.make_move(i) for i, value in enumerate(board.tup)
            }
    
    def find_random_child(board):
       if board.terminal:
           return None
       empty_spots = [i for i, value in enumerate(board.tup) if value is None]
       return board.make_move(choice(empty_spots))
   
    def reward(board):
       if not board.terminal:
            raise RuntimeError(f"reward called on nonterminal board {board}")
       if board.winner is board.turn:
            raise RuntimeError(f"reward called on unreachable board {board}")
       if board.turn is (not board.winner):
            return 0
       if board.winner is None:
            return 0.5
       raise RuntimeError(f"board has unknown winner type {board.winner}")
    def is_terminal(board):
       return board.terminal
    
    def make_move (board, index):
        tup = board.tup[:index] + (board.turn,)+ board.tup[index+ 1 :]
        turn = not board.turn
        winner = find_winner(tup)
        is_terminal = (winner is not None ) or not any(v is None for v in tup)
        return TicTacToeBoard(tup, turn, winner, is_terminal)
    
    def display_board(board):
       to_char = lambda v: ("X" if v is True else ("O" if v is False else ""))
       rows = [
           [to_char(board.tup[3 * row + col]) for col in range(3)] for row in range(3)
       ]
       return("\n 1 2 3\n"
              + "\n".join(str(i + 1) + " " + " ".join(row) for i, row in enumerate(rows)) + "\n")
   
def play_game():
    tree = MCTS()
    board = new_Board()
    print(board.display_board())
    while True:
        row_col = input("위치 row,col:")
        row, col = map ( int , row_col .split(","))
        index = 3 * ( row - 1) + (col - 1)
        if board.tup[index] is not None :
            raise RuntimeError ("lnvalid move" )
        board = board.make_move ( index)
        print(board.display_board())
        if board.terminal:
            break
        
        for _ in range(50):
            tree.do_rollout(board)
        board = tree.choose(board)
        print (board.display_board())
        if board.terminal:
            print('게임 종료')
            break

def winning_combos():
    for start in range(0, 9, 3):
        yield (start, start + 1, start + 2)
    for start in range(3):
        yield (start, start + 3, start + 6)
    yield (0, 4, 8)
    yield (2, 4, 6)
    
def find_winner (tup):
    for i1 , i2, i3 in winning_combos():
        v1 , v2, v3 = tup [i1], tup[i2], tup [i3]
        if False is v1 is v2 is v3 :
            return False
        if True is v1 is v2 is v3 :
            return True
    return None

def new_Board():
    return TicTacToeBoard(tup=(None,) *9, turn=True, winner=None, terminal=False)

if __name__=="__main__":
    play_game()
    
        
               
                    