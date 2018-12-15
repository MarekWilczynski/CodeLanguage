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

    def test_get_project_list(self):
        # given
        csv_loader = dm.CsvLoader("../data.csv")

        # when
        project_list = csv_loader.get_projects_list()

        project_tuple = project_list[1]
        project_language = project_tuple.language
        project_codes_length = len(project_tuple.codes)

        # then
        csv_loader.close()
        self.assertIsNotNone(project_language)
        self.assertIsNotNone(project_codes_length)

