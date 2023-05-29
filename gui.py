import sys
from threading import Thread

import webview

import app

thread: Thread = None


def on_closed():
    sys.exit()


def main():
    global thread
    # Запуск Flask в отдельном потоке
    flask_thread = Thread(target=app.main, name="flask_thread")
    flask_thread.daemon = True
    flask_thread.start()
    thread = flask_thread

    window: webview.Window = webview.create_window(" ", "templates/index.html", width=1400, height=800)
    window.events.closed += on_closed

    webview.start(debug=True)



if __name__ == '__main__':
    main()
