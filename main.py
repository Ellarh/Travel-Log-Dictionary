travel_log = [
  {"Country": "United Arab Emirates", 
   "times_visited": 2, 
   "cities_visited": ["Dubai"],
   "Memories": "I had an amazing time with my parents spending christmas in Dubai. We went to the Desert too",
  },
  {
    "Country": "Spain", 
    "times_visited": 3, 
    "cities_visited": ["Madrid", "Seville", "Barcelona"],
    "Memories": "Enjoyes the spanish food including churros con chocolate.",
  },
  {
    "Country": "Turkey",
    "times_visited": 2,
    "cities_visited": ["Ankara", "Istanbul"],
    "Memories": "Visited lots of museums and also saw the rod of Moses, although I wasn't allowed to take pictures",
  },
]

def add_new_log(country, times, cities, travel_memories):
  add_new_country = {}
  add_new_country["Country"] = country
  add_new_country["times_visited"] = times
  add_new_country["cities_visited"] = cities
  add_new_country["Memories"] = travel_memories
  travel_log.append(add_new_country)

add_new_log(country = "France", times = 1, cities = "Paris", travel_memories = "Had a blast and visited the eiffel tower too",)
print(travel_log)
  
  