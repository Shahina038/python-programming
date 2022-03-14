from postfix import *
def emptypostfix():
    ret = post_eval("")
    assert ret == []

def postfix():
    ret = post_eval("123*+")
    assert ret == 7  
