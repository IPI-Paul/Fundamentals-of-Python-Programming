# Listing 14.24
# Updates listing 14.8, providing a constructor
# Author: Rick Halterman
# Last modified: 

from timer import Timer

class DigitalTimer(Timer):
    def __init__(self, **kwargs):               # New code here
        super().__init__(**kwargs)              # New code here
        print('Initialising digital stopwatch') # New code here
        
    def digital_time(self):
        """
        Returns a string representation of the elapsed time in hours : minutes :
        seceonds
        """
        # Compute time in hours , minutes, and seconds
        seconds = round(self.elapsed())
        hours = seconds // 3600 # Compute total hours
        seconds %= 3600         # Update seconds remaining
        minutes = seconds // 60 # Compute minutes
        seconds %= 60           # Update seconds remiaining
        # Each digit occupies two spaces; pad wioth leading zeros, if necessary
        return '{0:0>2}:{1:0>2}:{2:0>2}'.format(hours, minutes, seconds)