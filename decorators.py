PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper


@password_required
def need_password():
    print('La contraseña es correcta')


def upper_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@upper_case
def say_my_name(name):
    return(f'Hola {name}, bienvenido')



if __name__ == '__main__':
    # need_password()
    print(say_my_name('David'))