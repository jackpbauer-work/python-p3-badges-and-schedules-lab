def badge_maker(name):
    return 'Hello, my name is ' + name + '.'

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names):
        room_assignments.append('Hello, ' + name + '! You\'ll be assigned to room ' + str(i+1) + '!')
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room_assignment in assign_rooms(names):
        print(room_assignment)
