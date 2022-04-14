s = {
    1981:
    {
        1995:
        {
            'MUF': {
                1973: 0,
                2009: 1,
            },
            'INI': 2,
            'STATA': {
                1973: 3,
                2009: 4
            }
        },
        1957: {
            'TCL': {
                1973: 5,
                2009: 6
            },
            'INI': 7,
            'NIM': {
                1973: 8,
                2009: 9
            }
        }
    },
    2008: 10
}


def main(path):
    s1 = s[path[0]]
    if path[0] == 1981:
        s1 = s1[path[2]]
        if path[2] == 1995:
            s1 = s1[path[3]]
            if path[3] == 'MUF' or path[3] == 'STATA':
                s1 = s1[path[1]]
        elif path[2] == 1957:
            s1 = s1[path[4]]
            if path[4] == 'TCL' or path[3] == 'NIM':
                s1 = s1[path[1]]
    return s1