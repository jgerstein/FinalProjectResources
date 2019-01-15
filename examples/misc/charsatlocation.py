destinations = {
    'magnet': ['Mr. Rafalowski', 'Maggie'],
    'bookstore': ['Neil Gaiman', 'Terry Pratchett'],
    'house': ['mom', 'dad']
}

available_locs = list(destinations.keys())

def choose_location(all_locs):
    global available_locs
    chosen_loc = ""
    while chosen_loc not in all_locs:
        chosen_loc = input(f"Choose one of the valid locations: {available_locs}")
    available_locs.remove(chosen_loc)
    return chosen_loc

def choose_allies(loc):
    print(f"Choose an ally from {loc}: {destinations[loc][0]} or {destinations[loc][1]}")


choose_allies(choose_location(available_locs))
choose_allies(choose_location(available_locs))