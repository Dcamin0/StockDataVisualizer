import unittest
from datetime import datetime


def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def is_valid_chart_type(chart_type):
    return chart_type in ["1", "2"]

def is_valid_time_series(time_series):
    return time_series in ["1", "2", "3", "4"]

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_date_order(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return start <= end
    except ValueError:
        return False


class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("MSFT"))
        
        self.assertFalse(is_valid_symbol("GOOGLE12")) 
        self.assertFalse(is_valid_symbol("TOOLONGSYMBOL"))  
        self.assertFalse(is_valid_symbol("appl"))  

    def test_chart_type(self):
       
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        
        self.assertFalse(is_valid_chart_type("3"))  
        self.assertFalse(is_valid_chart_type("bar"))  

    def test_time_series(self):
        
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("2"))
        self.assertTrue(is_valid_time_series("3"))
        self.assertTrue(is_valid_time_series("4"))
        
        self.assertFalse(is_valid_time_series("5"))  
        self.assertFalse(is_valid_time_series("weekly"))  

    def test_date_format(self):
        
        self.assertTrue(is_valid_date("2024-01-01"))
        self.assertTrue(is_valid_date("2023-12-31"))
        
        self.assertFalse(is_valid_date("01-01-2024"))  
        self.assertFalse(is_valid_date("2024/01/01"))  

    def test_date_order(self):
        
        self.assertTrue(is_valid_date_order("2024-01-01", "2024-12-31"))
        
        self.assertFalse(is_valid_date_order("2024-12-31", "2024-01-01"))


if __name__ == '__main__':
    unittest.main()
