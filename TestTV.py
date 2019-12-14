#!/usr/bin/python3
# 《Python语言程序设计》程序清单７－４
# Programed List 7-4
# 示例：调用TV类

from TV import TV
def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolumeLevel())
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolumeLevel())

main()