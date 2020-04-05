import pytest
import app
def test_bmi_case1(): 
    assert app.bmi(125, 6, 5)==15.18
def test_bmi_case2(): 
    assert app.bmi(130, 4, 5)==33.32
def test_bmi_case3(): 
    assert app.bmi(165, 6, 4)==20.57
def test_bmi_case4(): 
    assert app.bmi(200, 5, 11)==28.57
def test_bmi_case5(): 
    assert app.bmi(141, 6, 1)==19.05
def test_retirement_case1():
    assert app.retirement__(12, 1000, 10, 10000)==74.07
def test_retirement_case2():
    assert app.retirement__(22, 10000000, 10, 500000)==0.37
def test_retirement_case3():
    assert app.retirement__(14, 50000, 10, 10000)==1.48
def test_retirement_case4():
    assert app.retirement__(17, 100000, 10, 500000)==37.04

