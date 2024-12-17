from . import auth_blueprint


@auth_blueprint.route('/some_route')
def some_func():
    pass
