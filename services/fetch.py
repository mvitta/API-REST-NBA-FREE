import requests as req
from flask import flash
from dotenv import dotenv_values

def fetchData (page:int, per_page:int, url_option:str) -> list:
    try:
        
        URL = f"https://{dotenv_values().get('URL_BASE')}/{url_option}"
        params = {"page":page,"per_page":per_page}
        headers = {
        "X-RapidAPI-Key": dotenv_values().get('X-RapidAPI-Key'),
        "X-RapidAPI-Host": dotenv_values().get('free-nba.p.rapidapi.com')
        }

        response = req.request(method='GET', url=URL, headers=headers, params=params)
        data = list(response.json()['data'])
        
        return data
    
    except Exception as err:
        flash(error['messages'])
        error = response.json()
        print('Error: ', err)
        print(error['messages'])
        print(error['info'], '\n')
        return[]