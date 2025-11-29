import webview
from toolkit_api import API  # Your custom logic lives here

if __name__ == '__main__':
    api = API()
    window = webview.create_window(
        title='DLSUD Toolkit',
        url='frontend/home.html',
        js_api=api,
        width=800,
        height=560,
        resizable=True
    )

    webview.start(debug=False) 



    