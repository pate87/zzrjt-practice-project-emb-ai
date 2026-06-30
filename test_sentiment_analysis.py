# import the sentiment_analyzer function from the SentimentAnalysis package.
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
# Also import the unittest library.
import unittest

# Create the unit test class
class TestSentimentAnalyzer(unittest.TestCase):
    #  Define test_sentiment_analyzer as the function to run the unit tests.
    def test_sentiment_analyzer(self):

        # Test case for positive sentiment 
        positive_result = sentiment_analyzer("I love working with Python")
        self.assertEqual(positive_result['label'], "SENT_POSITIVE")
        # Test case for negative sentiment 
        negative_result = sentiment_analyzer("I hate working with Python")
        self.assertEqual(negative_result['label'], "SENT_NEGATIVE")
        # Test case for neutral sentiment 
        neutral_result = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(neutral_result['label'], "SENT_NEUTRAL")

# Call the unit tests
unittest.main()