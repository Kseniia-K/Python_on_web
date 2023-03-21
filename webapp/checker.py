def check_logged_in(func):
    def wrapper():
        if 'logged_in' in session:
            return func()
        return 'You are NOT logged in.'
    return wrapper