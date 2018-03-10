import pset10; reload(pset10)
from pset10 import *

def isClose(float1, float2):
    """
    Helper function - are two floating point values close?
    """
    return abs(float1 - float2) < .01

def testResult(boolean):
    """
    Helper function - print 'Test Failed' if boolean is false, 'Test
    Succeeded' otherwise.
    """
    if boolean:
        print 'Test Succeeded'
    else:
        print 'Test Failed'

def testHand():
    """
    Test the hand class. Add your own test cases
    """
    h = Hand(8, {'a':3, 'b':2, 'd':3})
    h.update('bad')
    testResult(h.containsLetters('aabdd') and not h.isEmpty())
    h.update('dad')
    testResult(h.containsLetters('ab') or not h.isEmpty())
    h.update('ab')
    testResult(h.isEmpty())

def testPlayer():
    """
    Test the Player class. Add your own test cases.
    """
    p = Player(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(type(p.getHand()) == Hand)
    p.addPoints(5.)
    p.addPoints(12.)
    testResult(isClose(p.getPoints(), 17))
    testResult(p.getIdNum() == 1)

def testComputerPlayer():
    """
    Test the ComputerPlayer class. Add your own test cases.
    """
    wordlist = Wordlist()
    p = ComputerPlayer(1, Hand(6, {'c':1, 'a':1, 'b':1 ,'d':1, 'o':1, 'e':1}))
    testResult(getWordScore(p.pickBestWord(wordlist)) == getWordScore('abode'))
    p2 = ComputerPlayer(2, Hand(3, {'c':1, 'a':1, 't':1}))
    testResult(getWordScore(p2.pickBestWord(wordlist)) == getWordScore('cat'))

def testAll():
    """
    Run all Tests
    """

    print "Uncomment the tests in this file as you complete each problem."

    print '-'*10,' PROBLEM 2 ','-'*10
    testHand()

    print '-'*10,' PROBLEM 3 ','-'*10
    testPlayer()

    print '-'*10,' PROBLEM 4 ','-'*10
    testComputerPlayer()

testAll()
