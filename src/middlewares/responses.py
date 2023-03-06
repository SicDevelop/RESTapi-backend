STATUS: str = 'content'

ERROR_RESPONSES: dict = {
        'something_wrong': {STATUS: 'something went front.'},
        'access_denied': {STATUS: 'access denied!'},
        'user_not_found': {STATUS: 'user not found!'}
}

OK_RESPONSES: dict = {
    'simple': {STATUS: 'done!'},
    'auth_done': {STATUS: 'access granted!'},
    'admin_created': {STATUS: 'admin created!'}
}
