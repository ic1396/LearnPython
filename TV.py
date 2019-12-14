#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－３
# Programed List 7-3
# 示例：TV类的定义

class TV:
    def __init__(self):
        self.channel = 1    # Default channel is 1
        self.volumeLevel = 1    # Default volume level is 1
        self.on = False    # Initially, TV is off

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        # 此处和书中代码不一致。书中的做法是检查当前值是否在正确范围内，
        # 此处改为检查将要设定的值是否在确定范围内，若不在则不改变当前值。
        if self.on and 1 <= channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        # 此处和书中代码不一致。书中的做法是检查当前值是否在正确范围内，
        # 此处改为检查将要设定的值是否在确定范围内，若不在则不改变当前值。
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1