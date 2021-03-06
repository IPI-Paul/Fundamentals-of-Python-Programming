# Listing 14.28
# Demonstrates the our new BoxAdapter class is fully cooperative
# Author: Rick Halterman
# Last modified: 

from boxadapter import BoxAdapter
from turtle import Screen, Turtle

def main():
    # Make a Box object via the adapter
    b = BoxAdapter(screen=Screen(), turtle=Turtle(), x=20, y=20, width=30)
    # Run the graphical program
    b.run()

if __name__ == '__main__':
    main()