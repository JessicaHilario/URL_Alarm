import time
import TimeCounter
import AlarmCounter
import webbrowser
import heapq
import os

#todo proceaa txt filw with days
class Alarm():
    # keeps track of the last index in the respective heaps

    def __init__(self):
        Alarm.timerInstanceNumber = 0
        Alarm.alarmInstanceNumber = 0
        # holds active timer threads
        self.timerInstances = []
        # holds active alarm threads
        self.alarmInstances = []

        # check text file exist
        if os.path.exists("alarm.txt"):
            self.txtFile = open("alarm.txt", "r")
	    # process the file 

            for lines in self.txtFile:
                print(lines, end= "")

                alarmDays, hour, minute, url = lines.split(";")
                print(hour, minute, url)
                self.alarmInstances.append(AlarmCounter.AlarmCounter(alarmDays.split(","),int(hour), int(minute), 0, Alarm.alarmInstanceNumber, url, self, 24))
                self.alarmInstances[Alarm.alarmInstanceNumber].start()
                Alarm.alarmInstanceNumber += 1
        else:
            # create the file 
            self.txtFile = open("alarm.txt", "a+")
            print("doesn't exist")

        self.txtFile.close()
		

    def updateAlarm(self, arg):
         # call activate alarm, 

        #self.play_alarm(self.timerInstances[0].url)
        # re heapify, move the top value down
        heapq.heappop(self.alarmInstances)
        Alarm.alarmInstanceNumber -= 1
        pass
    
    def updateTimer(self, arg):
         # call activate alarm, 

        #self.play_alarm(self.timerInstances[0].url)
        # re heapify, move the top value down
        heapq.heappop(self.timerInstances)
        Alarm.timerInstanceNumber -= 1
        pass
        
    def set_alarm(self,alarmDays ,url, hour, minute, second, time_format):
        """"Create an alarm text file if one is not created yet.
            If we have a alarm text file write that alarm to the text file"""

        # add the alarmCounter thread into the alarmInstances heap and start it 
        #CHANGE: add "day" into parameter
        self.alarmInstances.append(AlarmCounter.AlarmCounter(alarmDays, hour, minute, second, Alarm.alarmInstanceNumber, url, self, time_format))

        self.alarmInstances[Alarm.alarmInstanceNumber].start()
        heapq.heapify(self.timerInstances)
        # store the alarm in the text file 
        self.txtFile = open("alarm.txt", "a")
        index = 0 
        for day in alarmDays:
            if index < 6: 
                self.txtFile.write(str(day) + ",")
            else:
                self.txtFile.write(str(day) + ";")
            index+=1
        self.txtFile.write(str(hour) + ";" + str(minute) + ";" + str(url) + "\n")
        self.txtFile.close()
        # increment the index
        Alarm.alarmInstanceNumber += 1
                                   
    def set_timer(self, url, hour, minute, second):
        """Set a timer and activate the url when the time is reached"""
        self.timerInstances.append(TimeCounter.TimeCounter(hour, minute, second, Alarm.timerInstanceNumber, url, self))
        self.timerInstances[Alarm.timerInstanceNumber].start()
        Alarm.timerInstanceNumber += 1
        # turn off the previous off
        heapq.heapify(self.timerInstances)

        #print("time instance ", self.timeInstances)
        pass
        
    def play_alarm(self, url):
        """Open the url based on the alarm text file when a time_instance element
            Has been activated"""

        webbrowser.open(url)
        


    def deactivate_alarm(self):
        """Read the alarm text file and flip a bit denoting that that time instance should be tracked  """
        pass

    def validate_time(self):
        """Read the time the user inputted and check if it's in the correct format"""
        pass


    def validate_url(self):
        """Check that the url the user inputted is valid"""
        pass

    def modify_alarm(self):
        """Read the alarm text file and change it according to user input."""
        pass

    def delete_alarm(self):
        """Read the alarm text file and delete an alarm instace from it. Also update the time_isntance variable"""
        pass

    def activate_alarm(self):
        """Read the alarm text file and flip a bit denoting that that time instance should not be tracked"""
##            time_isntances.add(new timecounter)
        pass
