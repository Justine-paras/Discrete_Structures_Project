import webview
from feature1.app import get_shortest_path

class API:
    def open_navigation(self):
        webview.create_window('Campus Navigation', 'frontend/navigation.html', js_api=self)

    def get_shortest_path(self, start, end):
        return get_shortest_path(start, end)

    # You can add scholarship and parking methods here too

    

    