from flask import Flask, render_template, redirect, request, session
from poker import Player, Hand_Value

player = Player("player",1000)

app = Flask(__name__)
app.secret_key = "That's not Snowflake"
            
@app.route("/")
def play_game():
    if 'player_name' not in session:
        session['player_name'] = None
        session['holdcard1'] = False
        session['holdcard2'] = False
        session['holdcard3'] = False
        session['holdcard4'] = False
        session['holdcard5'] = False
        session['card1status'] = "hold"
        session['card2status'] = "hold"
        session['card3status'] = "hold"
        session['card4status'] = "hold"
        session['card5status'] = "hold"
        session['card1val'] = None
        session['card2val'] = None
        session['card3val'] = None
        session['card4val'] = None
        session['card5val'] = None
        session['card1suit'] = None
        session['card2suit'] = None
        session['card3suit'] = None
        session['card4suit'] = None
        session['card5suit'] = None
        session['show_hand'] = None
        session['show_header'] = "header"
        session['show_game'] = "display_none"
        session['header_class'] = "flex"
        session['draw_button_status'] = "Draw"
        session['net_change'] = None
    return render_template("index.html", show_game = session['show_game'], show_header = session['show_header'], player=session['player_name'], draw_button_status = session['draw_button_status'], show_hand = session['show_hand'], header_class = session['header_class'], 
        card1val = session['card1val'], card2val = session['card2val'], card3val = session['card3val'], card4val = session['card4val'], card5val = session['card5val'], net_change = session['net_change'],
        card1suit = session['card1suit'], card2suit = session['card2suit'], card3suit = session['card3suit'], card4suit = session['card4suit'], card5suit = session['card5suit'],
        holdcard1 = session['holdcard1'], holdcard2 = session['holdcard2'], holdcard3 = session['holdcard3'], holdcard4 = session['holdcard4'], holdcard5 = session['holdcard5'],
        card1status = session['card1status'], card2status = session['card2status'], card3status = session['card3status'], card4status = session['card4status'], card5status = session['card5status'])
            
@app.route("/start_game", methods=['POST'])
def start_game():
    session['show_header'] = "display_none"
    session['show_game'] = "wrapper"
    player.shuffle()
    player.deal_cards()
    player.show_hand()
    session['header_class'] = "display_none"
    session['show_hand'] = Hand_Value(player.hand).get_value()
    session['chips'] = player.chips
    session['card1val'] = player.hand[0].string_val
    session['card2val'] = player.hand[1].string_val
    session['card3val'] = player.hand[2].string_val
    session['card4val'] = player.hand[3].string_val
    session['card5val'] = player.hand[4].string_val
    session['card1suit'] = player.hand[0].suit
    session['card2suit'] = player.hand[1].suit
    session['card3suit'] = player.hand[2].suit
    session['card4suit'] = player.hand[3].suit
    session['card5suit'] = player.hand[4].suit
    return redirect('/')

@app.route("/hold", methods=['POST'])
def hold_cards():
    if request.form['hold'] == 'card1hold':
        session['holdcard1'] = True
        if session['card1status'] == "hold":
            session['card1status'] = "held"
        else:
            session['card1status'] = "hold"
    if request.form['hold'] == 'card2hold':
        session['holdcard2'] = True
        if session['card2status'] == "hold":
            session['card2status'] = "held"
        else:
            session['card2status'] = "hold"
    if request.form['hold'] == 'card3hold':
        session['holdcard3'] = True
        if session['card3status'] == "hold":
            session['card3status'] = "held"
        else:
            session['card3status'] = "hold"
    if request.form['hold'] == 'card4hold':
        session['holdcard4'] = True
        if session['card4status'] == "hold":
            session['card4status'] = "held"
        else:
            session['card4status'] = "hold"
    if request.form['hold'] == 'card5hold':
        session['holdcard5'] = True
        if session['card5status'] == "hold":
            session['card5status'] = "held"
        else:
            session['card5status'] = "hold"
    return redirect("/")

@app.route('/draw', methods=['POST'])
def draw_new_cards():
    old_chips = player.chips
    if session['draw_button_status'] == "Draw":
        if session['card5status'] == "hold":
            player.hand.pop(4)
        if session['card4status'] == "hold":
            player.hand.pop(3)
        if session['card3status'] == "hold":
            player.hand.pop(2)
        if session['card2status'] == "hold":
            player.hand.pop(1)
        if session['card1status'] == "hold":
            player.hand.pop(0)
        start_game()
        session['card1status'] = "display_none"
        session['card2status'] = "display_none"
        session['card3status'] = "display_none"
        session['card4status'] = "display_none"
        session['card5status'] = "display_none"
        player.win_chips()
        session['net_change'] = player.chips - old_chips
        session['chips'] = player.chips
        session['draw_button_status'] = "New Hand"
        return redirect('/')
    elif session['draw_button_status'] == "New Hand":
        while len(player.hand) > 0:
            player.hand.pop(0)
        start_game()
        session['card1status'] = "hold"
        session['card2status'] = "hold"
        session['card3status'] = "hold"
        session['card4status'] = "hold"
        session['card5status'] = "hold"
        session['draw_button_status'] = "Draw"
        session['show_hand'] = Hand_Value(player.hand).get_value()
        return redirect("/")
    
@app.route('/clear')
def clear_session():
    player.chips = 1000
    player.hand = []
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)            