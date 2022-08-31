from psycopg2 import connect
from dotenv import dotenv_values as getQuery
from flask import flash

def get_db_connection():
    
    try:
        conn = connect(database='favorite_teams', user='postgres', password='1234554321')
        cur = conn.cursor()
        return [cur, conn]
        # TRATAR ERROR EN CASO QUE NO PUEDA CONECTARSE A LA BASE DE DATOS
    except Exception as err:
        print(f'ERROR ! {err}:')
        return []
    

def getFavoriteTeams():
    getCurAndConn = get_db_connection()
    if type(getCurAndConn) == list:
        cur = getCurAndConn[0]
        conn = getCurAndConn[1]
        cur.execute(getQuery().get('getFavoriteTeams'))
        records = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return records
    # probar en caso de error
        
        
def registerFavoriteTeam(data_team):
    try:
        getCurAndConn = get_db_connection()
        if type(getCurAndConn) == list:
            cur = getCurAndConn[0]
            conn = getCurAndConn[1]
            cur.execute(getQuery().get('insertFavoriteTeam'), data_team)
            conn.commit()
            cur.close()
            conn.close()
            flash('Added To Favorites')
            
    except Exception as err:
        flash('Is Already In Favorites')
        print('ERROR: ', err)
        

def deleteFavoriteTeams(id):
    try:
        getCurAndConn = get_db_connection()
        if type(getCurAndConn) == list:
            cur = getCurAndConn[0]
            conn = getCurAndConn[1]
            cur.execute(getQuery().get('deleteFavoriteTeam'), id)
            conn.commit()
            cur.close()
            conn.close()
            flash('Removed From Favorites')
            
    except Exception as err:
        flash(err)
        print('ERROR: ', err)


def descendingOrder(query):
    try:
        getCurAndConn = get_db_connection()
        if type(getCurAndConn) == list:
            cur = getCurAndConn[0]
            conn = getCurAndConn[1]
            cur.execute(query)
            records = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return records
            
    except Exception as err:
        print('ERROR: ', err)