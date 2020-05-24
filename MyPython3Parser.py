from Python3Lexer import Python3Lexer
from Python3Listener import Python3Listener
from Python3Parser import Python3Parser
from antlr4 import *
import sys

class MyPython3Parser(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
def __init__(self): # this method creates the class object.
    pass
        
        
#function used to parse an input file
def parse(argv):
    if len(sys.argv) > 1:
        input = FileStream(argv[1]) #read the first argument as a filestream
        lexer = Python3Lexer(input) #call your lexer
        stream = CommonTokenStream(lexer)
        parser = Python3Parser(stream)
        tree = parser.file_input() #start from the parser rule, however should be changed to your entry rule for your specific grammar.
        printer = Python3Listener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
    else:
        print('Error : Expected a valid file')
