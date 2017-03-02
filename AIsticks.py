import random


def start():
    while True:
        try:
            stick_count = int(input("How many sticks would you like to play with? "))
            if stick_count > 0:
                return stick_count
        except ValueError:
            print("Pick a number.")


def pick_up(stick_count, dic):
    while True:
        if stick_count > 2:
            try:
                picked_up = int(input("Pick up some sticks: (1-3) "))
                if picked_up <= stick_count and picked_up <= 3 and picked_up > 0:
                    return picked_up
                elif picked_up == 0:
                    print(dic)
            except ValueError:
                pass
        elif stick_count == 2:
            try:
                picked_up = int(input("Pick up some sticks: (1-2) "))
                if picked_up == 1 or picked_up == 2:
                    return picked_up
                else:
                    print("Please pick a valid number")
            except ValueError:
                pass
        else:
            return 1


def show_board(stick_count):
    print('There are {} sticks on the board'.format(stick_count))


def switch_player(is_player_turn):
    return not is_player_turn


def main():
    dic = {}
    while True: #game loop
        turns_made = []
        stick_count = start()
        is_player_turn = True
        while stick_count > 0: #turn loop
            show_board(stick_count)
            stick_count -= pick_up(stick_count, dic)
            is_player_turn = switch_player(is_player_turn)
            if stick_count == 0:
                break
            turns_made = AI_turn(turns_made, stick_count, dic)
            stick_count -= turns_made[-1][1]
            is_player_turn = switch_player(is_player_turn)
        if is_player_turn:
            print("Player wins!")
            for item in turns_made:
                sub_from_entry(item[0], dic, item[1])
        else:
            print("AI wins!")
            for item in turns_made:
                add_to_entry(item[0], dic, item[1])


def create_entry(stick_count, dic):
    if stick_count >= 3:
        dic[stick_count] = [1, 2, 3]
        return dic
    if stick_count == 2:
        dic[stick_count] = [1, 2]
        return dic
    dic[stick_count] = [1]
    return dic


def add_to_entry(stick_count, dic, new_ball):
    dic[stick_count].append(new_ball)


def sub_from_entry(stick_count, dic, ball):
    if dic[stick_count].count(ball) > 1:
        dic[stick_count].remove(ball)


def AI_turn(turns_made, stick_count, dic):
    if stick_count not in dic:
        dic = create_entry(stick_count, dic)
    choice = random.choice(dic[stick_count])
    turns_made.append((stick_count, choice))
    print("AI picks up", choice)
    return turns_made


if __name__ == '__main__':
    main()
