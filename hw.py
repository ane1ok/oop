from collections import deque

def can_visit_all_rooms(rooms):
    n = len(rooms)
    visited_rooms = set()
    keys = deque([0])
    
    while keys:
        room = keys.popleft()
        visited_rooms.add(room)
        for key in rooms[room]:
            if key not in visited_rooms:
                keys.append(key)
    
    return len(visited_rooms) == n
