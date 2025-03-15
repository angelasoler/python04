import unittest
import statistics
import numpy as np

from ft_statistics import mean, median, quartile, std, var


class TestStatisticsFunctions(unittest.TestCase):
    def setUp(self):
        """Test datasets"""
        self.data1 = (2, 4, 6, 8, 10)
        self.data2 = (1, 2, 3, 4, 5, 6, 7, 8)
        self.data3 = (3, 5, 7, 9)

    def test_mean(self):
        """Compare mean function"""
        self.assertAlmostEqual(mean(self.data1), statistics.mean(self.data1))
        self.assertAlmostEqual(mean(self.data2), statistics.mean(self.data2))

    def test_median(self):
        """Compare median function"""
        self.assertAlmostEqual(
            median(self.data1), statistics.median(self.data1)
        )
        self.assertAlmostEqual(
            median(self.data2), statistics.median(self.data2)
        )

    def test_quartile(self):
        """Compare quartile function"""
        self.assertAlmostEqual(
            quartile(self.data1)[0], np.percentile(self.data1, 25)
        )
        self.assertAlmostEqual(
            quartile(self.data1)[1], np.percentile(self.data1, 75)
        )
        self.assertAlmostEqual(
            quartile(self.data2)[0], np.percentile(self.data2, 25)
        )
        self.assertAlmostEqual(
            quartile(self.data2)[1], np.percentile(self.data2, 75)
        )

    def test_std(self):
        """Compare standard deviation function"""
        self.assertAlmostEqual(
            std(self.data1),
            statistics.stdev(self.data1, xbar=mean(self.data1))
        )
        self.assertAlmostEqual(
            std(self.data2),
            statistics.stdev(self.data2, xbar=mean(self.data2))
        )

    def test_var(self):
        """Compare variance function"""
        self.assertAlmostEqual(
            var(self.data1),
            statistics.variance(self.data1, xbar=mean(self.data1))
        )
        self.assertAlmostEqual(
            var(self.data2),
            statistics.variance(self.data2, xbar=mean(self.data2))
        )


if __name__ == '__main__':
    unittest.main()
