"""date_and_time."""


def date_time(time):
    """Docstring."""
    timelst = time.replace('.', ' ').replace(':', ' ').split()

    def day(d):
        months = {
                1: "January",
                2: "February",
                3: "March",
                4: "April",
                5: "May",
                6: "June",
                7: "July",
                8: "August",
                9: "September",
                10: "October",
                11: "November",
                12: "December"
            }
        return months[d]

    def hour(h):
        if h == 1 or h == 11:
            return str(h) + ' hour'
        else:
            return str(h) + ' hours'

    def minute(h):
        if h == 1 or h == 11:
            return str(h) + ' minute'
        else:
            return str(h) + ' minutes'

    # s = f"{timelst[0]} {day(int(timelst[1]))} {timelst[2]} year {hour(int(timelst[3]))} {minute(int(timelst[4]))}"
    # print(str(int(timelst[0])) + ' ' + day(int(timelst[1])) + ' ' + timelst[2] + ' year ' + hour(int(timelst[3])) + ' ' + minute(int(timelst[4])))
    return (str(int(timelst[0])) + ' ' + day(int(timelst[1])) + ' ' +
            timelst[2] + ' year ' + hour(int(timelst[3])) + ' ' +
            minute(int(timelst[4])))

if __name__ == '__main__':
    # print("Example:")
    # print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    # date_time("01.01.2000 00:00")
