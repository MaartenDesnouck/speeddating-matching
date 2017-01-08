#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Participant():  # Deelnemer van een speeddate
    id = ""
    first_name = ""
    last_name = ""
    phoneNumber = ""

    # Constructor
    def __init__(self, id, first_name, last_name, phoneNumber):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber

    # Return full name
    def fullName(self):
        return self.first_name + " " + self.last_name
