event = {'function':'foo', 'parameters': [{'name': 'bucket', 'type': 'string', 'value': 'roymark-bedrock2-us-west-2'}, {'name': 'contents', 'type': 'string', 'value': "# New York City Itinerary: November 11-15\nTraveler: 25-year-old from Boston\n\n## Flight Details:\n- Departure: Boston Logan International Airport (BOS)\n- Arrival: John F. Kennedy International Airport (JFK)\n- Arrival Time: November 11, 11:00 AM\n\n## Hotel: Times Square Area Hotel\n\n### Day 1 (Nov 11):\n- 11:00 AM: Arrive at JFK Airport\n- 12:30 PM: Check-in at hotel, freshen up\n- 2:00 PM: Explore Times Square\n- 4:00 PM: Walk to Rockefeller Center\n- 6:30 PM: Dinner at Junior's Restaurant (classic NYC cheesecake)\n- 8:30 PM: Evening Broadway show\n\n### Day 2 (Nov 12):\n- 8:00 AM: Breakfast at Ellen's Stardust Diner\n- 10:00 AM: Statue of Liberty and Ellis Island tour\n- 2:00 PM: Financial District and 9/11 Memorial\n- 6:00 PM: Dinner in Greenwich Village\n- 9:00 PM: Comedy club in East Village\n\n### Day 3 (Nov 13):\n- 9:00 AM: Central Park walking tour\n- 12:00 PM: Lunch at Chelsea Market\n- 2:00 PM: Metropolitan Museum of Art\n- 6:00 PM: Dinner in Chinatown\n- 9:00 PM: Rooftop bar in Manhattan\n\n### Day 4 (Nov 14):\n- 9:00 AM: Brooklyn Bridge walk\n- 11:00 AM: DUMBO neighborhood exploration\n- 1:00 PM: Lunch in Brooklyn\n- 3:00 PM: Shopping in SoHo\n- 7:00 PM: Farewell dinner at a Michelin-starred restaurant\n- 10:00 PM: Night city views from Top of the Rock\n\n### Day 5 (Nov 15):\n- 9:00 AM: Breakfast near hotel\n- 10:00 AM: Last-minute shopping/souvenir hunting\n- 2:00 PM: Airport transfer\n- 5:00 PM: Departure from JFK\n\n## Transportation:\n- Airport transfers via taxi/rideshare\n- Subway for most city travel\n- Walking for nearby attractions\n\n## Recommended Packing:\n- Comfortable walking shoes\n- Layers for variable November weather\n- Evening smart-casual attire for shows/dinners\n\n## Estimated Budget:\n- Accommodations: $200-300/night\n- Food: $50-100/day\n- Activities: $100-200/day\n- Transportation: $50/day\n\n## Travel Tips:\n- Purchase a MetroCard for subway\n- Book Broadway show and tours in advance\n- Carry a portable charger"}, {'name': 'file_name', 'type': 'string', 'value': 'NYC_Itinerary_Nov11-15.md'}]}
print(event)

def get_named_parameter(event, name):
    if event['parameters']:
        for item in event['parameters']:
            if item['name'] == name:
                return item['value']
    return None
    # return next(item for item in event['parameters'] if item['name'] == name)['value']

folder_name = get_named_parameter(event, 'folder_name')
print(folder_name)