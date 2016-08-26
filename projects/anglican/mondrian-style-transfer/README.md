# Mondrian style transfer
Chris Anderson: [GitHub](https://github.com/chrisranderson), [twitter](https://twitter.com/chrisdotio)

## Prerequisites

- [pyzmq](https://github.com/zeromq/pyzmq) (I used version 15.3.0)
- python 3 (might work with 2, not sure)
- numpy
- [leiningen](http://leiningen.org/)
- [gorilla repl](http://gorilla-repl.org/)

## Instructions


The default code will try to generate a mondrian to match `mondrian.png`.

1. Run Gorilla REPL from this directory, open a browser at the port your terminal displays, click on the hamburger menu (top left), type "load", and load the `mondrian.clj` worksheet. Don't run it yet.
2. Run `server.py` - the Clojure script sends generated image descriptions to this file, and it returns the pixel-wise difference between the target image and the generated image.
3. Run `mondrian.clj`. It takes about 12.5 seconds to run on my laptop. It created a file called `generated.json` that describes the generated image.
4. Run `draw.py` to display the generated image.

## Running with different images

Towards the top of `mondrian.clj` and `server.py` there are instructions with configuration options.

## Notes

- You may have to restart Gorilla REPL if something goes wrong. Maybe something to do with ZMQ.
