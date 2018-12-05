import time
import threading
import heapq
import webbrowser


# TO DO
# - have it so we can set alarm relative to current time
class AlarmCounter(threading.Thread):
    """Create threads that keep track of a timer and notify observers when the time has passed"""
    #CHANGE: added "alarmDays" into parameter
    def __init__(self,alarmDays, hour, minute, second, name, url, Alarm, time_format):
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
        self.index = 0
        self.noneCounter = 0
        self.alarmDays = alarmDays
        self.days = [0,24,48,72,96,120,144]
        self.hour = hour
        self.minute = minute
        self.second = second
        self.totalSeconds = 0
        #self.monday,self.tuesday
        # store the url
        self.url = url
        if time_format == 24:
            # get the current hours and minutes to convert into seconds
            #CHANGE: ADD IN currentDay and time.localtime()[2]
            currentDay, currentHour, currentMinute, currentSecond = time.localtime()[6], time.localtime()[3], time.localtime()[4], time.localtime()[5]

            # calculate how many seconds to wait until we activate the alarm ( targetTime - currentTime)
            for day in self.alarmDays:
                #if there is a repeat
                if day != "None":
                    targetTime = (self.hour * 60 * 60) + (self.minute * 60) + self.second + (self.days[self.index] * 60 * 60) #days[self.index] 

                    currentTime = (currentHour * 60 * 60) + (currentMinute * 60) + currentSecond + (self.days[currentDay]* 60 *60) #days[currentDay]      
                    self.totalSeconds = targetTime - currentTime


                    # if targetTime is before currentTime
                    if (self.totalSeconds < 0):
                        partialSeconds = ((24*7*60*60) - currentTime)
                        self.totalSeconds = partialSeconds + targetTime
                    self.index += 1
                     # calculating hours , minutes, seconds
                    n = self.totalSeconds
                    daySec = n//86400
                    n%= 86400
                    hours = n //3600
                    n %= 3600
                    minutes = n // 60 
                    n %= 60
                    seconds = n
                    print("totalsec to wait is ", self.totalSeconds)
                    print("Days:", daySec, "hours:", hours, "minutes:", minutes, "seconds:", seconds)
                # if theres no repeat on this day
                else:
                    self.index += 1
                    self.noneCounter += 1
            # if theres no repeat on any day
            print(self.noneCounter)
            if (self.noneCounter == 7):
                # check if the time is before the current time
                targetTime = (self.hour *60*60) + (self.minute *60) + self.second
                currentTime =(currentHour *60 *60) + (currentMinute * 60) + currentSecond

                self.totalSeconds = targetTime - currentTime
                if self.totalSeconds < 0:
                    # 24 hours - currentTime
                    print("neg")
                    partialSeconds = ((24 *60 * 60) - (currentTime))
                    
                    # answ += targetTime
                    self.totalSeconds = partialSeconds + targetTime
        
                 # calculating hours , minutes, seconds
                n = self.totalSeconds
                daySec = n//86400
                n%= 86400
                hours = n //3600
                n %= 3600
                minutes = n // 60 
                n %= 60
                seconds = n
                print("totalsec to wait is ", self.totalSeconds)
                print("Days:", daySec, "hours:", hours, "minutes:", minutes, "seconds:", seconds)
            
            
           
			
        

        
    def run(self):
        """put the thread to sleep for the set time, then notify observers """
        #NEW POS CHANGE: alarm gets run no matter what
        # Whether if i will actually be activated will depend on the reached
        # state and the activeState (true and true)
        
        self._activeState = True
        
        # sleep until it's time to activate the alarm
        time.sleep(self.totalSeconds)

        # singal that the time has been reached
        self._reachedState = True
        
        # call notify
        if self._reachedState == True and self._activeState == True:
            # we can open the link here
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
            observer.updateAlarm(self._reachedState)

    def changeState(self, state):
        """Change the state of this time instance and call notify """
        self._reachedState = state
        self._notify()

    def __lt__(self, other):
        """less than operator used to order heaps"""
        return self.totalSeconds < other.totalSeconds
