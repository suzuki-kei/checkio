#
# https://py.checkio.org/en/mission/sun-angle/
#

def sun_angle(time):
    hour = int(time[0:2])
    minute = int(time[3:5])

    x = hour * 100 + (minute / 60 * 100)
    if x < 600 or 1800 < x:
        return "I don't see the sun!"
    return (x - 600) / (1800 - 600) * 180

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("12:15") == 93.75
    print("Coding complete? Click 'Check' to earn cool rewards!")

