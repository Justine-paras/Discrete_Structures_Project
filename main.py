import webview
from toolkit_api import API  # Your custom logic lives here

if __name__ == '__main__':
    api = API()
    webview.create_window(
        title='DLSUD Toolkit',
        url='home/home.html',
        js_api=api,
        width=800,
        height=520,
        resizable=False
    )
    webview.start(debug=True)