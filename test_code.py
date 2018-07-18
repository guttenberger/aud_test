import unittest
from io import StringIO
import sys
import difflib


def test_code(globals):
    """Test the result of the code execution."""
    loader = unittest.TestLoader()
    #TestQuicksort.globals = globals
    #suite = loader.loadTestsFromTestCase(TestQuicksort)
    TestDynProg.globals = globals
    suite = loader.loadTestsFromTestCase(TestDynProg)
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
class TestQuicksort(unittest.TestCase):
    """Test the quicksort algorithm according to its specification.
    
    For writing more tests, please see
    """
    
    globals = None # will be set by test_code
    
    # set up & tear down
    
    def setUp(self):
        """Initialize the test case."""
        self.sort = self.globals.get("quicksort", None)
        self.old_stdout = sys.stdout
        self.stdout = sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.old_stdout

    # helpers
    
    def assert_is_sorted(self, input, output, message):
        input = input[:]
        self.test_01_quicksort_function_exists()
        self.sort(input)
        self.assertEqual(input, output, message + "\n{} ist erwartet aber\n{} wurde geliefert.".format(input, output))

    def assertSwap(self, input, swap, message):
        self.test_01_quicksort_function_exists()
        self.sort(input)

        sort_swap = self.stdout.getvalue().split()
        excpected_swap = swap.split()
        diff = difflib.ndiff(sort_swap, excpected_swap)
        self.assertEqual(sort_swap, excpected_swap, message + "\n for list {}\n{}".format(input, "\n".join(diff)))

    # test cases for setup
    
    def test_01_quicksort_function_exists(self):
        self.assertIsNotNone(self.sort, "Ich erwarte eine Funktion namens \"quicksort\".")
    
    # test cases for sorting
    
    def test_02_can_sort_no_elements(self):
        self.assert_is_sorted([], [], "Eine leere Liste kann sortiert werden.")

    def test_03_can_sort_one_element(self):
        self.assert_is_sorted([1], [1], "Eine Liste mit einem Element ist sortiert.")
        self.assert_is_sorted([131], [131], "Eine Liste mit einem Element ist sortiert.")

    def test_04_can_sort_two_equal_elements(self):
        self.assert_is_sorted([1, 1], [1, 1], "Zwei gleiche Elemente.")
        
    def test_05_can_sort_two_unequal_sorted_elements(self):
        self.assert_is_sorted([1, 2], [1, 2], "Zwei vertauschte Elemente werden in der selben Liste sortiert.")
        
    def test_06_can_sort_two_equal_elements(self):
        self.assert_is_sorted([2000000000000, 1], [1, 2000000000000], "Zwei falsch sortierte Elemente.")
    
    def test_07_can_sort_negative_and_positive_numbers(self):
        self.assert_is_sorted(
            [9, -81, 94, 43, 97, 40, -6, 70, -15, -88],
            [-88, -81, -15, -6, 9, 40, 43, 70, 94, 97],
            "Negative und positive Zahlen erhalten die richtige Reihenfolge.")
    
    def test_08_can_sort_big_numbers_with_duplicates(self):
        self.assert_is_sorted(
            [10000004, 10000006, 10000005, 10000004, 10000005, 10000004, 10000008, 10000007, 10000008, 10000004],
            [10000004, 10000004, 10000004, 10000004, 10000005, 10000005, 10000006, 10000007, 10000008, 10000008],
            "Grosse Zahlen mit duplikaten erhalten die richtige Reihenfolge.")
    
    def test_09_can_sort_huge_list_elements(self):
        sorted_list = list(range(100))
        unsorted_list = sorted_list[::-1]
        self.assert_is_sorted(
            unsorted_list,
            sorted_list,
            "{} Elemente koennen sortiert werden.".format(len(sorted_list)))
        
    
    # test cases for element swapping
    
    def test_50_swap_no_elements(self):
        self.assertSwap([], "", "No elements are swapped if the list is empty.")
        
    def test_51_swap_one_element_list(self):
        self.assertSwap([123], "", "No elements are swapped if the list has one element.")
        
    def test_52_swap_two_elements(self):
        self.assertSwap([2,1], "0,1", "The two elements are swapped. The indices are printed in order without spaces.")
        
    def test_53_do_not_swap_elements_if_in_order(self):
        self.assertSwap([1,2], "", "No elements are swapped if the two elements are in order.")
        self.assertSwap(list(range(10)), "", "No elements are swapped if the two elements are in order.")
        
    def test_54_swap_last_and_first(self):
        self.assertSwap([10,2,3,4,5,6,1], "0,6", "The first and last element get swapped.")

    def test_55_swap_many_elements(self):
        self.assertSwap(
            [9, -81, 94, 43, 97, 40, -6, 70, -15, -88], 
            "0,9 2,8 3,6 4,9", 
            "Elements get swapped around.")

    def test_55_swap_all_elements_if_reversed(self):
        self.assertSwap(
            list(range(5)) + list(range(5, 0, -1)), 
            "1,9 2,9 3,8 4,9 5,8 6,7 5,6 7,9 8,9", 
            "Many Elements get swapped around in a reversed list.")


#testeing dynprog (refactored l8r ?)            
            
class TestDynProg(unittest.TestCase):
    """Test dynanic programming task according to its specification.
    """
    
    globals = None # will be set by test_code
    
    # set up & tear down
    
    def setUp(self):
        """Initialize the test case."""        
        self.old_stdout = sys.stdout
        self.stdout = sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.old_stdout

    # helpers

    @property
    def createChart(self):
        createChart = self.globals.get("createChart", None)
        self.assertIsNotNone(createChart, "Ich benötige eine Funktion namens createChart")
        return createChart

    @property
    def bestChoice(self):
        bestChoice = self.globals.get("bestChoice", None)
        self.assertIsNotNone(bestChoice, "Ich benötige eine Funktion namens bestChoice")
        return bestChoice
         

    # test case for optimization

    def test_best_value(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        maxWeight = 8
        bestValRef = 7
        self.assertEqual(self.createChart(items, maxWeight)[-1][-1][0],bestValRef, "Der bestmögliche Wert ist ein anderer")

    def test_createChart_chart_is_equal_to_reference_chart(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        maxWeight = 8
        chartRef = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)],
                    [(0, 0), (1, 1), (1, 1), (1, 1), (3, 0), (4, 1), (4, 1), (4, 1), (4, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 1), (5, 1), (5, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 0), (5, 0), (6, 1)],
                    [(0, 0), (1, 0), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1)]]

        self.assertEqual(self.createChart(items, maxWeight),chartRef, "Die erstellte Tabelle ist falsch")

    def test_bestChoice_value_is_equal_to_reference_value(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        bestValRef = 7
        chartRef = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)],
                    [(0, 0), (1, 1), (1, 1), (1, 1), (3, 0), (4, 1), (4, 1), (4, 1), (4, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 1), (5, 1), (5, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 0), (5, 0), (6, 1)],
                    [(0, 0), (1, 0), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1)]]
        givenChoice = self.bestChoice(chartRef, items)
       
        #bestchoice meigt not be unique, so just check summed up values of given choice
        valSum = 0
        for i in range(len(items)):
            #if item packed
            if givenChoice[i]: 
                valSum += items[i][0]

        self.assertEqual(valSum,bestValRef, "der Gesamtwert der bestimmten besten Auswahl weicht von dem Vergleichswert ab")


    def test_bestCoice_weight_is_le_max_weight(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        maxWeight = 8
        chartRef = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)],
                    [(0, 0), (1, 1), (1, 1), (1, 1), (3, 0), (4, 1), (4, 1), (4, 1), (4, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 1), (5, 1), (5, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 0), (5, 0), (6, 1)],
                    [(0, 0), (1, 0), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1)]]
        givenChoice = self.bestChoice(chartRef, items)
        
        #bestchoice meigt not be unique, so check value sum of given choice
        weightSum = 0
        for i in range(len(items)):
            #if item packed
            if givenChoice[i]:
                weightSum += items[i][1]


        #max Weight should not be exeeded
        self.assertLessEqual(weightSum, maxWeight, "das Gesamtgewicht der bestimmten Auswahl sollte kleiner als das Maximalgewicht sein")
            
    def test_bestChoice_returns_list_containing_0s_or_1s(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        chartRef = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)],
                    [(0, 0), (1, 1), (1, 1), (1, 1), (3, 0), (4, 1), (4, 1), (4, 1), (4, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 1), (5, 1), (5, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 0), (5, 0), (6, 1)],
                    [(0, 0), (1, 0), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1)]]

        givenChoice = self.bestChoice(chartRef, items)
        #returned list should only contain 0 or 1
        self.assertCountEqual(list(set(givenChoice)),[0,1],"bestChoice sollte eine Liste aus 0en und 1en zurückgeben.")

    def test_bestChoice_returns_list_as_long_as_item_list(self):
        items = [(3,4),(1,1),(4,5),(3,4),(2,2)]
        chartRef = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                    [(0, 0), (0, 0), (0, 0), (0, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1)],
                    [(0, 0), (1, 1), (1, 1), (1, 1), (3, 0), (4, 1), (4, 1), (4, 1), (4, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 1), (5, 1), (5, 1)],
                    [(0, 0), (1, 0), (1, 0), (1, 0), (3, 0), (4, 0), (5, 0), (5, 0), (6, 1)],
                    [(0, 0), (1, 0), (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 1), (7, 1)]]

        givenChoice = self.bestChoice(chartRef, items)

        #items should be as long as bestChoice return value
        self.assertEqual(len(givenChoice),len(items), "Die Länge des Rückgabewertes von bestChoice sollte der Länge der Gegenstandsliste entsprechen.")
