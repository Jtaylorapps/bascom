# Contains data-grabbing functionality for the webapp

import pandas as pd
import requests

# Constant variables - likely would want to make these configurable
start_date = 1900
end_date = 2022

def scrape_api(country):
    """
    Simple API request getting full population data for a given country string.

    :return: pd.DataFrame containing full population data
             dict containing year -> value population mapping
    """
    # Construct an API call for the worldbank population data
    url = f"http://api.worldbank.org/v2/country/{country}/" \
          f"indicator/SP.POP.TOTL?date={start_date}:{end_date}&format=json&per_page=100"
    response = requests.get(url)

    # Get the response in JSON
    header, population_data = response.json()

    # Convert data into year:population format
    population = list()
    population_map = dict()
    for item in population_data:
        population.append({"year": item["date"], "total_pop": item["value"]})
        population_map[item["date"]] = item["value"]

    # Create DataFrame for sorting and filtering
    population = pd.DataFrame.from_dict(population)
    population = population.dropna().sort_values("year")
    return population_map, population
