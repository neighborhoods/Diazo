# [Diazo](https://en.wikipedia.org/wiki/Whiteprint#The_diazo_printing_process)
A simple Docker-run Python CLI utility to use Graphviz to convert a .dot file to a .png or .svg.

## Requirements
- Docker (tested on 17.06)

## Usage
- Place your [Graphviz-formatted dot files](http://www.graphviz.org/content/dot-language) in the `/data` directory.
- Run the command `docker-compose run --rm diazo --input_file=yourfilename.dot --output_format=png|svg`
  - The `--output_format` is optional. It will default to png if nothing is provided.
  - Make sure your `--input_format` is the exact file name in the correct case. Do not need to prepend the `/data` directory.
- Your output file will be in `/output`