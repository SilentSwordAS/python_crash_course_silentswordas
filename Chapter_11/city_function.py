def get_city_country(city, country, population=None):
    if population:
        return f"{city.strip().title()}, {country.strip().title()} - population {population}"
    else:
        return f"{city.strip().title()}, {country.strip().title()}"