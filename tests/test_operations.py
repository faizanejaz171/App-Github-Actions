from src.maths_operations import add, sub


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(5,4)==1
    assert sub(8,7)==1
    assert sub(9,8)==1   

