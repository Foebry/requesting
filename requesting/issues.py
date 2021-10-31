


def reconnect(func, args):
    """
        function to check if connection to internet has been re-etablished.

        :param func: callback function
        :type func: function
        :param args: arguments for callback function
        :type args: list
    """
    return func(*args)
