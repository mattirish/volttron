
import logging

from volttron.platform.agent.base import (AbstractDrivenAgent, Results)


class LogDevice(AbstractDrivenAgent):

    def __init__(self, **kwargs):
        self.results = Results()
        self.results.log(__name__)
        for key, value in kwargs.iteritems():
            self.results.log("{}->{}".format(key, value))

    def run(self, time, points):
        self.results.log(time)
        for key, value in points.iteritems():
            self.results.log("{}->{}".format(key, value))
        return self.results