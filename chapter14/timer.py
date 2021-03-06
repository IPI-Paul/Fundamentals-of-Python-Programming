# Listing 14.23
# Updates Listing 13.6 to better support multiple inheritance. Teh only changes 
# are the use of super in the constructor and a print message to ensure the 
# constructor executes as expected.
# Author: Rick Halterman
# Last modified: 

from time import clock
from top import Top

class Timer(Top):
    """
    Provides stopwatch objects that programmers can use to time the execution 
    time of portions of a program.
    """
    def __init__(self, **kwargs):
        """
        Makes a new stopwatch ready for timing.
        """
        super().__init__(**kwargs)      # New code here
        print('Initializing stopwatch') # New code here
        self.reset()
    
    def start(self):
        """
        Starts the stopwatch, unless it is already running. Thismethod does not 
        affect any time that may have already accumulated on the stopwatch.
        """
        if not self._running:
            self._start_time = clock() - self._elapsed
            self._running = True # Clock now running
    
    def stop(self):
        """
        Stops the stopwatch, unless it is not running. Updates the accumulated 
        elapsed time.
        """
        if self._running:
            self._elapsed  = clock() - self._start_time
            self._running = False   # Clock stopped
    
    def reset(self):
        """
        Resets stopwatch to zero.
        """
        self._start_time = self._elapsed = 0
        self._running = False
        
    def elapsed(self):
        """
        Reveals the stopwatch running time since it was last reset.
        """
        if not self._running:
            return self._elapsed
        else:
            return clock() - self._start_time