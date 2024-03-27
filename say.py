import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.horse("hello, " + sys.argv[1])
