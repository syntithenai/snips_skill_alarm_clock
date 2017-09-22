import datetime
import threading
import sys
import itertools
import json
import pygame
import random
import time
from alarmclockskill.clock import Clock
from alarmclockskill.audioplayer import AudioPlayer

alarms = None;

"""
api to support alarm clock intents with file based persistence of alarms between requests
"""
class AlarmClockSkill:

    def __init__(self, db_file_path,tts_service=None):
        """ Initialisation.
        :param db: the json database.
        :param tts_service: A TTS service, i.e. an object which has a
                            `speak(text)` method for speaking the result.
        """
        self.tts_service = tts_service
        
        try:
            with open(db_file_path, 'r') as f:
                db = json.loads(f.read().replace('\n', ''))
                if db:
                    self.alarms = db["alarms"]
        except ValueError:
            db = []
    def speak(self,text):
        if self.tts_service is not None:
            self.tts_service.speak(text)

    def write_alarms(self):
        with open(db_file_path, 'r+') as f:
            f.write(json.dumps(self.alarms))

    def add_alarm(self,time,description='',duration=0):
        sys.stdout.write('add alarm\n')
        self.speak('add alarm\n')
        sys.stdout.write(time)
        sys.stdout.write(description)
        sys.stdout.flush()
        self.alarms.append([time,description])
        write_alarms()

    def what_is_the_time(self):
        result = "The time is {}".format(time.strftime('%X %x'))
        self.speak(result)
        return result;
    
    def cancel_alarm(self,time,description=''):
        sys.stdout.write('cancel alarm\n')
        self.speak('cancel alarm\n')
        sys.stdout.write(time)
        sys.stdout.write(description)
        sys.stdout.flush()
        write_alarms()
    
    def cancel_all_alarms(self):
        sys.stdout.write('cancel all alarm\n')
        self.speak('cancel all alarm\n')
        sys.stdout.flush()
        write_alarms()
    
    def list_alarms(self):
        sys.stdout.write('list alarms\n')
        sys.stdout.write(self.alarms);
        self.speak('list alarms\n')
        sys.stdout.flush()







