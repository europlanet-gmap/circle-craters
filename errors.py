# -*- coding: utf-8 -*-


class CircleCraterError(Exception):
   # def __init__(self):
    #    self.message =

    def __init__(self, message=None):
        # Call the base class constructor with the parameters it needs
        if message is None:
            message = "Generic Circle Crater Error, no more info available, inspect stack trace"
        super().__init__(message)

        self.message = message # seems python2 was using this (?) \todo remove this usage of messages
