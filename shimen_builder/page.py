# coding: UTF-8
import yaml
from jinja2 import FileSystemLoader

loader = FileSystemLoader('templates')


class Page:
    template_file = None

    def __init__(self, path):
        self.path = path
        self.data = None
        self.html = None

    def load_data(self, data_file):
        with open('data_file') as f:
            data = yaml.safe_load(f)

    def render(self):
        
        self.html = self.
