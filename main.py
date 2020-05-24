import MyPython3Parser
import sys

#main method and entry point of application

def main(argv):
    """Main method calling a single debugger for an input script"""
    parser = MyPython3Parser
    parser.parse(argv)

if __name__ == '__main__':
    main(sys.argv) 
