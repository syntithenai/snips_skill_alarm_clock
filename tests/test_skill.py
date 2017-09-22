from unittest import TestCase

from alarmclockskill.alarmclockskill import  AlarmClockSkill
from alarmclockskill.clock import Clock
from alarmclockskill.audioplayer import AudioPlayer


class BaseTest(TestCase):

    def setUp(self):
        self.skill = AlarmClockSkill('/tmp/testalarmclock.db')


class AlarmClockSkillTest(BaseTest):
    def test_what_is_the_time(self):
        results = self.skill.what_is_the_time()
        self.assertIsNotNone(results)
