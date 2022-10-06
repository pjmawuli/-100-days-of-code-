travel_log = [
    {"country_visited": "France", 
    "total_visits": 4,
    "cities_visited": ["paris", "lille", "dijon"], 
    },
    {"country_visited": "Germany",
    "total_visits": 3,
     "cities_visited": ["berlin", "harmburg", "stuttgart"], 
    },
]

def add_new_contry(country_visited, total_visits, cities_visited):
    travel_dic = {}
    travel_dic["country_visited"] = country_visited
    travel_dic["total_visits"] = total_visits
    travel_dic["cities_visited"] = cities_visited

    travel_log.append(travel_dic)

add_new_contry("russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)