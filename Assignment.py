student_id = ('000124524', '524178741', '789451784', '634781222', '965874012',
              '524178357', '741258964', '963547536', '741635784', '12339955257')

student_info =
def create_login():
    student_name = input('Enter your name: ')
    student_username = input('Enter your username: ')
    student_password = input('Enter your password: ')
    password_confirmation = input('Reenter your password: ')

    if student_name is None:
        print('Student name is blank. Reenter details.')
        return False
    if student_username is None:
        print('Username is blank. Reenter details.')
        return False
    if student_password is None:
        print('Password is blank. Reenter details.')
        return False
    if password_confirmation is None:
        print('Password confirmation is blank. Reenter details.')
        return False
    if student_password != password_confirmation:
        print('Passwords do not match. Reenter details.')
        return False


student_input_id = input('Enter your Student ID: ')
if student_input_id in student_id:

    while not create_login():
        create_login()
else:
    print('You are not a student of this class.')
