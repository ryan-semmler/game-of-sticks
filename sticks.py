def start():
    stick_count = int(input("How many sticks would you like to play with?"))
    return stick_count


def pick_up(stick_count):
    while True:
        if stick_count > 2:
            picked_up = int(input("Pick up some sticks: (1-3) "))
            if picked_up <= stick_count and picked_up <= 3 and picked_up > 0:
                # stick_count -= picked_up
                return picked_up
        elif stick_count == 2:
            picked_up = int(input("Pick up some sticks: (1-2) "))
            if picked_up == 1 or picked_up == 2:
                return picked_up
            else:
                print("Please pick a valid number")
        else:
            return 1


def show_board(stick_count, is_player1_turn):
    print('There are {} sticks on the board'.format(stick_count))
    if is_player1_turn:
        print("Player 1's turn.")
    else:
        print("Player 2's turn.")


def switch_player(is_player1_turn):
    return not is_player1_turn


def main():
    stick_count = start()
    is_player1_turn = True
    while stick_count > 0:
        show_board(stick_count, is_player1_turn)
        stick_count -= pick_up(stick_count)
        is_player1_turn = switch_player(is_player1_turn)
    if is_player1_turn:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == '__main__':
    main()
