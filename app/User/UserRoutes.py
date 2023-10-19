from app.User import bp

@bp.route('/')
def base():
    return 'This is the base user route'