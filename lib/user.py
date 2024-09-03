#!/usr/bin/env python

class User:
    def __init__(self,first_name=None,last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"
    
    # def set_full_name(self):
    #     self.first_name, self.last_name = self.get_full_name().split()
    