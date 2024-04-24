import unittest
from demographic_data_analyzer import race_counts, average_age_men, percentage_bachelors, percentage_high_earners, \
    percentage_low_earners, min_work_hours, rich_percentage, highest_earning_country, \
    highest_earning_country_percentage, top_IN_occupation

class TestDemographicDataAnalyzer(unittest.TestCase):
    def test_race_counts(self):
        print(race_counts)
        self.assertIn(' White', race_counts.index)
        self.assertEqual(race_counts[' White'], 27816)
        self.assertEqual(race_counts[' Black'], 3124)
        self.assertEqual(race_counts[' Asian-Pac-Islander'], 1039)
        self.assertEqual(race_counts[' Amer-Indian-Eskimo'], 311)
        self.assertEqual(race_counts[' Other'], 271)
        
    def test_average_age_men(self):
        self.assertAlmostEqual(average_age_men, 39.4, places=1)
        
    def test_percentage_bachelors(self):
        self.assertAlmostEqual(percentage_bachelors, 16.4, places=1)
        
    def test_percentage_high_earners(self):
        self.assertAlmostEqual(percentage_high_earners, 46.5, places=1)
        
    def test_percentage_low_earners(self):
        self.assertAlmostEqual(percentage_low_earners, 17.4, places=1)
        
    def test_min_work_hours(self):
        self.assertEqual(min_work_hours, 1)
        
    def test_rich_percentage(self):
        self.assertAlmostEqual(rich_percentage, 10.0, places=1)
        
    def test_highest_earning_country(self):
        self.assertEqual(highest_earning_country, ' Iran')
        
    def test_highest_earning_country_percentage(self):
        self.assertAlmostEqual(highest_earning_country_percentage, 41.9, places=1)
        
    def test_top_IN_occupation(self):
        self.assertEqual(top_IN_occupation, ' Prof-specialty')
        
if __name__ == '__main__':
    unittest.main()
