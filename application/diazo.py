import argparse
import pygraphviz as pgv
import sys
import os

class Architect():

    def __init__(self):
        self.input_file = None
        self.output_format = "png"
        self.allowed_formats = ["png", "svg"]

    def main(self):
        try:
            self.parse_args()
            self.draw_graph()
            sys.exit(0)
        except Exception as (strerror):
            print "Error: {}".format(strerror)
            sys.exit(1)


    def parse_args(self):
        parser = argparse.ArgumentParser(description='Generate a Graphviz image from a .dot file.')
        parser.add_argument('--input_file', help='Name of your input file')
        parser.add_argument('--output_format', help='Output format. May be .svg or .png. Optional. Defaults to .png.')
        args = parser.parse_args()
        input_file = args.input_file
        if not args.output_format:
            output_format = "png"
        else:
            output_format = args.output_format.lower()

        self.validate_input(input_file)
        self.validate_output(output_format)

        self.input_file = args.input_file
        self.output_format = output_format

    def validate_input(self, input):
        file_path = "data/{}".format(input)

        if not input:
            raise ValueError("No value provided for input file")

        ext = os.path.splitext(file_path)[-1].lower()
        if ext != ".dot":
            raise TypeError("Invalid input file specified. Only .dot files may be used.")
        if not os.path.isfile(file_path):
            raise TypeError("The input file specified does not exist")

        return True

    def validate_output(self, output):
        if output not in self.allowed_formats:
            raise TypeError("Invalid output format requested. Valid types are .svg and .png")

        return True

    def draw_graph(self):
        try:
            grapher = pgv.AGraph("data/{}".format(self.input_file))
        except pgv.agraph.DotError:
            raise TypeError("The dot file provided is not valid.")
        grapher.layout(prog='dot')
        output_file_name = "{}.{}".format(os.path.splitext(self.input_file)[0], self.output_format)
        grapher.draw("output/{}".format(output_file_name))

a = Architect()
a.main()