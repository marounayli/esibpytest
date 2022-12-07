import unittest
import argparse
import json
import importlib.util
import sys
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("--ex", help="exercice you want to test; leave empty if you want to run all tests" , type=str)
args = parser.parse_args()
tp=None
sys.tracebacklimit = 0
class App:
    def __init__(self,  ex_number, content) -> None:
        self.content = content
        self.ex_number=ex_number
        filename="source_code_{}.py".format(self.ex_number)
        with open(filename,"w") as source_code:
            source_code.write(self.content)
        spec = importlib.util.spec_from_file_location("tp", filename)
        global tp
        tp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(tp)

def swap_tuples(tuples_list):
    res = []
    for t in tuples_list:
        if 0 not in t:
            (x,y) = t[1],t[0]
            res.append((x,y))
    return res

def canBeTypedWords(text, brokenLetters):
    text = text.split()
    length = len(text)
    brokenLetters = set(brokenLetters)

    for word in text:
        for char in word:
            if char in brokenLetters:
                length -= 1
                break
				
    return length

def freq_counter_1(text):
    ### implement here
    text=text.replace("\n"," ").strip()
    d = {}
    for token in text.split(" "):
        if token in d:
            d[token]+=1
        else:
            d[token]=1
    return d

def freq_counter_2(l):
    ints = defaultdict(int)
    strs = defaultdict(int)
    for elt in l:
        if type(elt) is str:
            strs[elt]+=1
        else:
            ints[elt]+=1
    return dict(ints),dict(strs)

test_scores = {"ex1":0 , "ex2":0, "ex3":0, "ex4":0}
class Ex1(unittest.TestCase):
    
    def genTestCase(self, t1, t2, testCaseName):
        try:
            self.assertListEqual(swap_tuples(t1),tp.swap_tuples(t2))
            print(testCaseName , " success \u2714")
            test_scores["ex1"] = test_scores["ex1"] +1
        except AssertionError:
            print("Test case failed in ", testCaseName,"\u274C")
                
    def test1ex1(self):
        self.genTestCase([(1,1),(1,1)] ,[(1,1),(1,1)], "ex1-test1")
    def test2ex1(self):
        self.genTestCase([(1,1),(1,2),(2,0)], [(1,1),(1,2),(2,0)], "ex1-test2")
    def test3ex1(self):
        self.genTestCase([(1,1),(1,2),(2,0)] , [(1,1),(1,2),(2,0)], "ex1-test3")
    def test4ex1(self):
        self.genTestCase([(1,1),(1,2),(2,0)] , [(1,1),(1,2),(2,0)], "ex1-test4")
    def test5ex1(self):
        self.genTestCase([(1,1),(1,2),(2,0)] , [(1,1),(1,2),(2,0)], "ex1-test5")

class Ex2(unittest.TestCase):

    
    def genTestCase(self, text1, text2,testCaseName):
        try:
            self.assertDictEqual(freq_counter_1(text1),tp.freq_counter_1(text2))
            print(testCaseName , " success \u2714")
            test_scores["ex2"] = test_scores["ex2"]+1 
        except AssertionError:
            print("Test case failed in ", testCaseName,"\u274C")

    def test1ex2(self):
        self.genTestCase("test1 test1 test2 hello","test1 test1 test2 hello","ex2-test1")               
    def test2ex2(self):
        self.genTestCase("test1 test1 test2 hello","test1 test1 test2 hello","ex2-test2") 
    def test3ex2(self):
        self.genTestCase("test1 test1 test2 hello","test1 test1 test2 hello","ex2-test3")
    def test4ex2(self):
        self.genTestCase("Maximus", "Maximus","ex2-test4")
    def test5ex2(self):
        self.genTestCase("a", "a" , "ex2-test5")
        
class Ex3(unittest.TestCase):
    def genTestCase(self, text1, text2,testCaseName):
        try:
            self.assertTupleEqual(freq_counter_2(text1),tp.freq_counter_2(text2))
            print(testCaseName , " success \u2714")
            test_scores["ex3"] = test_scores["ex3"]+1 
        except AssertionError:
            print("Test case failed in ", testCaseName,"\u274C")

    def test1ex2(self):
        self.genTestCase([1,2,1,1,2,"test","test","alpha"],[1,2,1,1,2,"test","test","alpha"],"ex3-test1")               
    def test2ex2(self):
        self.genTestCase([1,2,1,1,2,"test","test","alpha"],[1,2,1,1,2,"test","test","alpha"],"ex3-test2") 
    def test3ex2(self):
        self.genTestCase([1,2,1,1,2,"test","test","alpha"], [1,2,1,1,2,"test","test","alpha"],"ex3-test3")
    def test4ex2(self):
        self.genTestCase([1,2,1,1,2,"test","test","alpha"], [1,2,1,1,2,"test","test","alpha"],"ex3-test4")
    def test5ex2(self):
        self.genTestCase([1,2,1,1,2,"test","test","alpha"],[1,2,1,1,2,"test","test","alpha"], "ex3-test5")

class Ex4(unittest.TestCase):
    def genTestCase(self,t1,l1,t2,l2,testCaseName):
        try:
            self.assertEqual(canBeTypedWords(t1,l1),tp.canBeTypedWords(t2,l2))
            print(testCaseName , " success \u2714")
            test_scores["ex4"] = test_scores["ex4"]+1 
        except AssertionError:
            print("Test case failed in ", testCaseName,"\u274C")

    def test1ex2(self):
        self.genTestCase("leet code","lt","leet code","lt","ex4-test1")
    def test2ex2(self):
        self.genTestCase("Let there be light","e","Let there be light","e","ex4-test2")
    def test3ex2(self):
        self.genTestCase("in war gods favor the sharper blade","ao","in war gods favor the sharper blade","ao","ex4-test3")
    def test4ex2(self):
        self.genTestCase("artouro","lop","artouro","lop","ex4-test4")
    def test5ex2(self):
        self.genTestCase("","","","","ex4-test5")

exs = {"ex1":Ex1 , "ex2":Ex2 , "ex3":Ex3, "ex4" :Ex4}



def runTest(ex_number,source_code):
    #reset the current ex
    test_scores[ex_number]=0
    
    app = App(ex_number,source_code)
    print(app.content)
    print(app.ex_number)
    unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(exs[ex_number]))
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    print("Your grade for this exercice : " ,str(test_scores[ex_number])+"/5")
    return str(test_scores[ex_number]) 


# if __name__ == '__main__':  
#     if args.ex is not None:
#         if args.ex not in exs.keys():
#             print("Provided value for argument ex is invalid, choose one of the following : ", exs.keys() , " or nothing")
#         unittest.TextTestRunner()
#         suite = unittest.TestSuite()
#         suite.addTests(unittest.makeSuite(exs[args.ex]))
#         result = unittest.TextTestRunner(verbosity=1).run(suite)
#         print("Your grade for this exercice : " ,str(test_scores[args.ex])+"/5")
#     else:
#         unittest.main(exit=False)
#         print(test_scores)
#         # print("Your final grade : " ,getFinalGrade(test_scores))
    
