import time
import threading
import heapq
import webbrowser


# TO DO
# - have it so we can set alarm relative to current time
class TimeCounter(threading.Thread):
    """Create threads that keep track of a timer and notify observers when the time has passed"""
    
    def __init__(self, hour, minute, second, name, url, Alarm):
        """Constructor store aruguments and calculate the hours and minutes to seconds """
        # call the super
        threading.Thread.__init__(self, daemon=1, name=name)
        
        # flag that tells whether its time to activate the alarm 
        self._reachedState = False

        # flag that tells whether this time counter should be called or not 
        self._activeState = False
        
        # contains the observers that the subject is attached to
        self._observers = set()
        self.attach(Alarm)
    
        # initialize variables that will activate alarm when reached
        self.hour = hour
        self.minute = minute
        self.second = second

        # store the url
        self.url = url

        # get the current hours and minutes to convert into seconds 
        currentHour, currentMinute, currentSecond = time.localtime()[3], time.localtime()[4], time.localtime()[5]
        
        # calculate how many seconds to wait until we activate the alarm
        self.totalSeconds = ((self.minute * 60) + (self.hour * 60 * 60) + self.second)# - ((currentHour * 60 * 60) + (currentMinute *60) + currentSecond)
        print("totalsec to wait", self.totalSeconds)

        
    def run(self):
        """put the thread to sleep for the set time, then notify observers """
        self._activeState = True
        
        # sleep until it's time to activate the alarm
        time.sleep(self.totalSeconds)

        # singal that the time has been reached
        self._reachedState = True
        
        # call notify
        if self._reachedState == True and self._activeState == True:
            webbrowser.open(self.url)
            self._notify()
            
        self._reachedState = False

        # detached the time counter form alarm

    def turnOff(self):
        """change the object so that it should be activated when time is reached """
        self._activeState = False
        
    def attach(self, Alarm):
        """ attach this time instance to an alarm"""
        Alarm._subject = None
        self._observers.add(Alarm)

    def detach(self, Alarm):
        Alarm._subject = None
        self._observers.discard(Alarm)

    def _notify(self):
        """Signal to all observers(Alarm) that the state has changed"""
        for observer in self._observers:
            observer.updateTimer(self._reachedState)

    def changeState(self, state):
        """Change the state of this time instance and call notify """
        self._reachedState = state
        self._notify()

    def __lt__(self, other):
        """less than operator used to order heaps"""
        return self.totalSeconds < other.totalSeconds
    


##tc1 = TimeCounter(0, 0, 5, 'uno', 'www.google.com')
##tc2 = TimeCounter(0, 0, 6, 'dos', 'www.google.com')
##tc3 = TimeCounter(0, 0, 7, 'tres', 'www.google.com')
##tc4 = TimeCounter(0, 0, 8, 'quatro', 'www.google.com')
##tc_list = [tc2, tc4, tc3, tc1]
##heapq.heapify(tc_list)
##print(tc_list)
##



##sec = time.localtime()[5]
##while tc._reachedState != True:
##    pass

##print("reached in: ", time.localtime()[5] - sec)
##
##print("after")




