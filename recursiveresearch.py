import sys
try:
    class str(sys.argv[1]):
        def __init__(self):
            i = int(sys.argv[4])
            for inn in i:
                (lambda: inn)()
                continue
        def __init_subclass__(self):
            i = int(sys.argv[4])
            for inn in i:
                (lambda: inn)()
                continue
        try:
            def kwargs():
                i = int(sys.argv[4])
                for inn in i:
                    (lambda: inn)()
        except:
            pass

    class str(sys.argv[2]):
        def __init__(self):
            super(str(sys.argv[2]), self).__init__()
    insight = str(sys.argv[2])()
    (lambda: insight.kwargs())()
except:
    print("recursion -"+sys.argv[3])