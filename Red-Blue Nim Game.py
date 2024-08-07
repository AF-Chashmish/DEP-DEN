import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('num_red', type=int, nargs='?', default=10)
    parser.add_argument('num_blue', type=int, nargs='?', default=10)
    parser.add_argument('version', choices=['standard', 'misere'], nargs='?', default='standard')
    parser.add_argument('first_player', choices=['human', 'computer'], nargs='?', default='human')
    parser.add_argument('depth', type=int, nargs='?', default=None)
    return parser.parse_args()

def game_loop(num_red, num_blue, version, first_player):
    current_player = first_player
    while num_red > 0 and num_blue > 0:
        print(f"Red marbles: {num_red}, Blue marbles: {num_blue}")
        if current_player == 'human':
            move = input("Enter your move (red/blue and number): ")
            if len(move.split()) not in [1, 2]:
                print("Invalid input. Please enter a valid move.")
                continue
            color, num = move.split()
            num = int(num)
            if color == 'red':
                if num > num_red:
                    print("Invalid move, not enough red marbles.")
                    continue
                num_red -= num
            else:
                if num > num_blue:
                    print("Invalid move, not enough blue marbles.")
                    continue
                num_blue -= num
            current_player = 'computer'
        else:
            if version == 'standard':
                # Standard version, computer tries to avoid emptying a pile
                if num_red > num_blue:
                    move = 'red'
                    num = random.randint(1, num_red)
                else:
                    move = 'blue'
                    num = random.randint(1, num_blue)
            else:
                # Misere version, computer tries to empty a pile
                if num_red < num_blue:
                    move = 'red'
                    num = random.randint(1, num_red)
                else:
                    move = 'blue'
                    num = random.randint(1, num_blue)
            print(f"Computer move: {move} {num}")
            if move == 'red':
                num_red -= num
            else:
                num_blue -= num
            current_player = 'human'
    print(f"Game over. Red marbles: {num_red}, Blue marbles: {num_blue}")
    if version == 'standard':
        if num_red > 0 and num_blue > 0:
            print("It's a draw!")
        elif current_player == 'human':
            print("Computer wins!")
        else:
            print("Human wins!")
    else:
        if num_red > 0 and num_blue > 0:
            print("It's a draw!")
        elif current_player == 'human':
            print("Human wins!")
        else:
            print("Computer wins!")

def main():
    args = parse_args()
    game_loop(args.num_red, args.num_blue, args.version, args.first_player)

if __name__ == '__main__':
    main()
