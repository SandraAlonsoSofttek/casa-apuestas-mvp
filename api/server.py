users = load_json("users.json")
events = load_json("events.json")
bets = load_json("bets.json")
@app.get("/api/users")    # Devuelve todos los usuarios
@app.get("/api/events")   # Devuelve todos los eventos
@app.get("/api/bets")     # Devuelve todas las apuestas
@app.get("/api/users/<int:user_id>/bets")      # Apuestas de un usuario
@app.get("/api/events/<int:event_id>/bets")    # Apuestas de un evento
@app.get("/api/events/open")                   # Eventos pendientes
@app.get("/api/users/<int:user_id>/bets")      # Apuestas de un usuario
@app.get("/api/events/<int:event_id>/bets")    # Apuestas de un evento
@app.get("/api/events/open")                   # Eventos pendientes
if __name__ == "__main__":
    app.run(debug=True, port=3000)
