def ask():
    ask = input('Do you want to continue? '
                '(type Y / YES to repeat the task or anything else to exit): ').lower()
    if ask == 'y' or ask == 'yes':
        return True
    else:
        return False