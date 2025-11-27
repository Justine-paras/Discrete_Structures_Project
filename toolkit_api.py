import webview
import time
import threading
from backend.navigation import get_shortest_path
from backend.scholarship import ScholarshipAPI

class API:
    def __init__(self):
        # instantiate ScholarshipAPI once
        self.scholarship = ScholarshipAPI()

    def open_navigation(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/navigation.html')).start()
        return "navigation loaded"
    
    def get_shortest_path(self, start, end):
        return get_shortest_path(start, end) 
    
    def open_scholarship(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/scholarship.html')).start()
        return "scholarship loaded"

    # Delegate scholarship methods
    def get_requirements(self, scholarship_type):
        return self.scholarship.get_requirements(scholarship_type)

    def check_eligibility(self, scholarship_type, answers):
        return self.scholarship.check_eligibility(scholarship_type, answers)
    
    def open_parking(self):
        threading.Timer(0.1, lambda: webview.windows[0].load_url('frontend/parking.html')).start()
        return "parking loaded"
    
    # This is a test change


