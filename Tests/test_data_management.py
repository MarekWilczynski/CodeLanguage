from unittest import TestCase
import data_management as dm


class TestDataManagement(TestCase):
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

    def test_split_data(self):
        # given
        csv_loader = dm.CsvLoader("../data.csv")
        split_ratio = 0.1

        # when
        project_list = csv_loader.get_projects_list()

        training_data, test_data = dm.split_to_test_and_training(project_list, split_ratio)
        training_example = training_data[150]
        test_example = test_data[15]

        # then

        csv_loader.close()
        self.assertIsNotNone(training_example[0])
        self.assertIsNotNone(training_example[1])
        self.assertIsNotNone(test_example.language)
        self.assertIsNotNone(test_example.codes)


