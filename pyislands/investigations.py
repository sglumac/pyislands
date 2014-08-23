
def iteration_investigate(dummy, info=None):
    if not info:
        info = {'iteration': 0}
    else:
        info = {'iteration': info['iteration'] + 1}

    return info


