import webview


def main():
    webview.create_window("My App", "http://127.0.0.1:5000")
    webview.start()


if __name__ == '__main__':
    main()
