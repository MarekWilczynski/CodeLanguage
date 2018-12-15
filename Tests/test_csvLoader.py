from unittest import TestCase
import data_management as dm


class TestCsvLoader(TestCase):
    def test_next(self):
        # given
        column_count = 4
        csv_loader = dm.CsvLoader("../data.csv")
        csv = iter(csv_loader)

        # when
        row = csv.next()

        # then
        csv_loader.close()
        self.assertEqual(len(row), column_count)

    def test_can_loop_2_times(self):
        # given
        column_count = 4
        csv_loader = dm.CsvLoader("../data.csv")
        csv = iter(csv_loader)

        # when
        for row in csv:
            pass
        for row in csv:
            pass

        # then
        csv_loader.close()
        self.assertTrue(True)
