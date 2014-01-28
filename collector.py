import sys
import os

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    raise ImportError("Jinja2 is a friendly templating language for Python")


class CollectedDesign(object):
    def __init__(self):
        file = '%s/templates/' % os.path.abspath(os.path.dirname(__file__))
        self.environment = Environment(loader=FileSystemLoader(file))
        self.template = self.environment.get_template("base.html")

    def run(self, data, outfile):
        render = self.template.render(data)
        outfile.write(render)
        return render
