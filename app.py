from flask import Flask, render_template, request
from services import fetch
from dotenv import dotenv_values
from services import db



app = Flask(__name__)
app.secret_key = dotenv_values().get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    #request API
    #para paginacion
    _page = 0
    _per_page = 10
    
    data = fetch.fetchData(page=_page, per_page=_per_page, url_option="teams")
    
    if request.method == 'POST':
        try:
            dataPage = list(request.form.values())[:7]
            dataPage[0] = int(dataPage[0])
            # botones
            btnFavorite = request.form.get('btn-favorite')
            btnDelete = request.form.get('btn-delete')
            if btnFavorite:
                db.registerFavoriteTeam(data_team=dataPage)
            if btnDelete:
                db.deleteFavoriteTeams(btnDelete)
                pass
            return render_template(template_name_or_list='inicio.html', dataPage=dataPage, teams=data)
            
        except Exception as err:
            print('Exception: ', err)
            
    return render_template(template_name_or_list='inicio.html', teams=data)


@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    if request.method == 'POST':
        try:
            btn = request.form.get('btn').lower()
            if btn == 'desc':
                records = db.descendingOrder(dotenv_values().get('descendingOrderByID'))
                
            if btn == 'ascbycity':
                records = db.descendingOrder(dotenv_values().get('ascendingByCity'))
                
            if btn == 'byconference':
                records = db.descendingOrder(dotenv_values().get('byConference'))  
                
            if btn == 'bydivision':
                records = db.descendingOrder(dotenv_values().get('byDivision'))  
            
            return render_template('favorites.html', records=records)
            
        except Exception as err:
            print('ERROR: ', err)

    records = db.getFavoriteTeams()
    return render_template('favorites.html', records=records)


@app.route('/api', methods=['GET'])
def api():
    return render_template(template_name_or_list='infoAPi.html')
    


if __name__ == 'main':
    app.run(port=3000, debug=True)