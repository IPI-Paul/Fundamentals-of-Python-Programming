# Listing 14.6
# Provides the RestrictedStopwatch class definition that leverages the 
# capabilities of the CountingStopwatch object via inheritance
# Author: Rick Halterman
# Last modified: 

from countingstopwatch import CountingStopwatch

class RestrictedStopwatch(CountingStopwatch):
    def __init__(self, n):
        """
        Restrict the number of stopwatch starts to n times
        """
        # Allow superclass to do its initialisation of the inherited instance 
        # variables
        super().__init__()
        self._limit = n
    
    def start(self):
        """
        If the count exceeds the limit, terminate the program's execution
        """
        if self._count < self._limit:
            super().start() # Let superclass do its start code
        else:
            import sys
            print('Limit exceeded')
            sys.exit(1) # Limit exceeded, terminate program