from flask import Flask, render_template

app = Flask(__name__)

@app.route('/gadgets')
def gadgets():
    gadgets = ['Spy Cam', 'Silencer', 'Pocket Knife', 'Bulletproof Vest', 'Desert Eagle', 'Pen']
    return render_template('gadgets.html', title='Gadgets', subtitle='Essential gadgets for every mission!', gadgets=gadgets)

@app.route('/missions')
def missions():
    missions = ['Politican escort In Russia', 'North Korean Intel Corps', 'Malaysian Base Infiltration', 'Russian Nuclear Bomb Code Sabatoge']
    return render_template('missions.html', title='Missions', subtitle='Pending missions' , missions=missions)

@app.route('/')
def home():    
    return render_template('home.html', title='Welcome to the hand')

if __name__ == '__main__':
    app.run(debug=True)