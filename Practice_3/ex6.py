import traceback


def trouble_1():
    return 1 / 0


def trouble_2():
    file = open('local.html', 'r')


class Logger(object):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback_):
        if exc_type:
            with open('file.log', 'w') as file:
                file.write('Class name: {}\n'.format(exc_type))
                file.write('Error message: {}\n'.format(exc_value))
                file.write('Traceback:\n')
                for element in traceback.format_tb(traceback_):
                    file.write(element)


def run_with_log(func):
    with Logger():
        func()


#run_with_log(trouble_1)
run_with_log(trouble_2)
