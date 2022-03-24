import traceback


class FunA:
    s=traceback.extract_stack()
    print('%s Invoked me!'%s[-2][2])

FunA()