

def isRole(identity, role='user'):
    return identity['role'] == role


def hasAccess(identity, role='user'):
    has = convertRoleToNumber(identity['role'])
    required = convertRoleToNumber(role)
    if(has >= required):
        return True
    return False


def convertRoleToNumber(role):
    if(role == 'user'):
        return 1
    if(role == 'developer'):
        return 2
    if(role == 'admin'):
        return 3
    return 0
