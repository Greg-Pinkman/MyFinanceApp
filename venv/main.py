from usrsjob import User

end_flag = False

operation = {"0": User.exit,
             "1": User.add_plus_operation,
             "2": User.add_minus_operation,
             "3": User.show_operation
             }

name_user = User.greetings()


def main():
    vote = User.select_actions()
    operation[vote](name_user)
    global end_flag
    end_flag = True if vote == "0" else None


if __name__ == "__main__":
    while not end_flag:
        main()
