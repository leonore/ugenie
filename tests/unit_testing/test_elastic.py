import unittest
import sys

sys.path.append('../../chat-service/model')
import elastic

class TestElastic(unittest.TestCase):

    maxDiff = None

    # test the getting data from a specific field in the short coerces data when the feild and the name is both gevin
    def test_get_sc_field(self):
        self.assertEqual('This course is suitable for' in elastic.get_sc_field(
            "Botanical painting and illustration", "Course description")[0], True)
        self.assertEqual('Impressionism is perhaps' in elastic.get_sc_field(
            "Impressionism 1860-1900", "Course description")[0], True)
        self.assertEqual('For students who have completed Stage 1' in elastic.get_sc_field(
            "SPANISH STAGE 2", "Course description")[0], True)

    # test the getting course link  from coerces data when  the course name is  gevin
    def test_get_sc_course_link(self):
        self.assertEqual(elastic.get_sc_course_link('Writing Fiction'),
                         'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11423E')
        self.assertEqual(elastic.get_sc_course_link('Northern Renaissance Art'),
                         'http://www.gla.ac.uk/coursecatalogue/course/?code=ADED11469E')
        self.assertEqual(elastic.get_sc_course_link(
            'Painting landscapes'), False)

    # test the getting sources link  from coerces data when  the course name is  gevin
    # waiting for TODO

    """def test_get_sc_resource_link(self):
        self.assertEqual(elastic.get_sc_resource_link('FT'))
        self.assertEqual(elastic.get_sc_resource_link('PT'))"""

    def test_get_admissions_field(self):
        self.assertEqual('Grade: 2.1 Borderline' in elastic.get_admissions_field(
            'EARLY MODERN HISTORY', 'Ent Req')[0], True)
        self.assertEqual(elastic.get_admissions_field(
            'CHINESE STUDIES', 'RIO')[0], 1)
        self.assertEqual(elastic.get_admissions_field(
            'Film Curation', 'Plan Code')[0], 'W621-5000')
        self.assertEqual(elastic.get_admissions_field(
            'Food Security', 'Apply Centre Description')[0], 'Life Sciences PGT')

    # test the getting sources link  from admission's data when  the course name is  gevin
    def test_get_ad_times(self):
        self.assertEqual(elastic.get_ad_times('CHINESE STUDIES'), [
                         'Chinese Studies', 2018, None])
        self.assertEqual(elastic.get_ad_times('Film Curation'), [
                         'Film Curation', 2018, None])
        self.assertEqual('Environment, Culture And Communication'in elastic.get_ad_times(
            'ENVIRONMENT, CULTURE AND COMMUNICATION'), True)
        self.assertEqual(elastic.get_ad_times('CHILDHOOD PRACTICE'), [
                         'Childhood Practice', 2018, None])

    # test the getting sources link  from admission's data when  the course name is  gevin
    # waiting for TODO
    """def test_get_admission_requirements(self):
        self.assertEqual(elastic.get_admission_requirements('BIOINFORMATICS', "IELTS requirements"),False)
        self.assertEqual(elastic.get_admission_requirements('CLINICAL NUTRITION', 'Ent Req'), False)
        self.assertEqual(elastic.get_admission_requirements("EDUCATION (CHILDREN'S LITERATURE AND LITERACIES)", 'Ent Req'),False)
        self.assertEqual(elastic.get_admission_requirements('EDUCATIONAL STUDIES', "IELTS requirements"), False)"""

    # test  getting the cost of a short course when the course's  name is both gevin
    def test_lastic_get_ad_fees(self):
        self.assertEqual(elastic.get_ad_fees(
            'CHINESE STUDIES')[1] == '8000', True)
        self.assertEqual(elastic.get_ad_fees(
            'Film Curation')[1] == '8000', True)
        self.assertEqual(elastic.get_ad_fees(
            'Food Security')[2] == '21020', True)

    # test  getting the cost of a admission  course when the course's  name is both gevin
    def test_get_ad_description(self):
        self.assertEqual('Chinese' in elastic.get_ad_description(
            'CHINESE STUDIES')[0], True)
        self.assertEqual('Childhood Practice' in elastic.get_ad_description(
            'CHILDHOOD PRACTICE')[0], True)
        self.assertEqual('Film Curation' in elastic.get_ad_description(
            'Film Curation')[0], True)
        self.assertEqual('Food Security' in elastic.get_ad_description(
            'Food Security')[0], True)

# test  getting the cost of a admission  course when the course's  name is both gevin
    def test_get_type_courses(self):
        self.assertEqual('Introduction to Ancient Egypt 1B' in elastic.get_type_courses(
            'Festivals in Ancient Egypt', "short")[0], True)
        self.assertEqual(len(elastic.get_type_courses(
            'Festivals in Ancient Egypt', "short")[0]) < 4, False)
        self.assertEqual('Introducing Geology' in elastic.get_type_courses(
            'Introducing Geology', "short")[0], True)
        self.assertEqual(len(elastic.get_type_courses(
            'Festivals in Ancient Egypt', "short")[0]) < 4, False)

    # test  get_acronym_descd in elastic
    # test  wait for work
    """
    def test_get_acronym_descd(self):
        self.assertEqual('IELTS requirements is the English' in elastic.get_acronym_desc('IELTS requirements')[1], True)
        self.assertEqual(elastic.get_acronym_desc('FT')[1], 'FT means full-time.')
        self.assertEqual('Plan Code is the unique code given to a' in elastic.get_acronym_desc('Plan Code')[1], True)
        self.assertEqual(elastic.get_acronym_desc('PT')[1], 'PT means part-time.')
"""
 # test  get_sc_times in elastic

    def test_get_sc_times(self):
        self.assertEqual('10.00' in elastic.get_sc_times(
            "Ancient Medicine: Theory")[0], True)
        self.assertEqual(
            '12/03/2019' in elastic.get_sc_times("SPANISH STAGE 2")[0], True)
        self.assertEqual('French Stage 1' in elastic.get_sc_times(
            "French stage 1")[0], True)

 # test  get_course_title in elastic

    def test_get_course_title(self):
        self.assertEqual(elastic.get_course_title(
            "Brain Sciences"), ('Brain Sciences', 'AD', 9.722658))
        self.assertEqual(elastic.get_course_title("ANIMAL WELFARE SCIENCE"),
                         ('Animal Welfare Science, Ethics And Law', 'AD', 8.870279))
        self.assertEqual(elastic.get_course_title("Orkney"),
                         ('Orkney In Scotland', 'SC', 4.4347043))
        self.assertEqual(elastic.get_course_title("Film"),
                         ('Film Curation', 'AD', 5.484622))
        self.assertEqual(elastic.get_course_title(
            "Film Studies"), ('Film Studies 1', 'SC', 9.140733))
        self.assertEqual(elastic.get_course_title(
            "szdfedg"), (None, None, None))

 # test  getting the cost of a admission  course when the course's  name is both gevin
    # wait for implementation
    """def test_get_description(self):
        self.assertEqual('French Stage 1 is: A course for' in elastic.get_description("french study 1")[1], True)
        self.assertEqual(elastic.get_description("brain science")[0], ('BRAIN SCIENCES'))
        self.assertEqual(elastic.get_description("FT"), ('FT', 'FT means full-time.'))
"""

 # test  _get_tutor_courses in elastic
    def test_get_tutor_courses(self):
        self.assertEqual(elastic.get_tutor_courses(
            "Ruth Ezra")[0], 'Ruth Ezra')  # >1 class
        self.assertEqual('Painting The American Landscape,  and Art And Anatomy' in elastic.get_tutor_courses(
            "Ruth Ezra")[1], True)
        self.assertEqual(elastic.get_tutor_courses(
            "Sarah Wolstencroft"), ('Sarah Wolstencroft', 'Continuing Latin'))
        self.assertEqual(elastic.get_tutor_courses("Sam Cook"), (False, False))


# test  weekdayToNum in elastic

    def test_monthToNum(self):
        self.assertEqual(elastic.monthToNum('July'), 7)
        self.assertEqual(elastic.monthToNum('March'), 3)
        self.assertEqual(elastic.monthToNum("November"), 11)

 # test  weekdayToNum in elastic

    def test_weekdayToNum(self):
        self.assertEqual(elastic.weekdayToNum("Monday"), 0)
        self.assertEqual(elastic.weekdayToNum("Tuesday"), 1)
        self.assertEqual(elastic.weekdayToNum("Thursday"), 3)

 # test  fullify_sc_list in elastic
    def test_fullify_list(self):
        cources_list = elastic.fullify_list(
            ['Writing Fiction', 'Writing Poetry'], "short")
        self.assertEqual(cources_list[0]['Tutor'], 'Alan McMunnigall')
        self.assertEqual(cources_list[0]['Cost'], 125)
        self.assertEqual(cources_list[1]['Class code'], 8087)
 # test  filterForMonths in elastic

    def test_filterForMonths(self):
        cources_list = elastic.filterForMonths(
            'january', ['Writing Fiction', 'Writing Poetry'])
        self.assertEqual('Writing Fiction' not in cources_list, True)
        self.assertEqual('Writing Poetry' in cources_list, True)


# test  filterForWeekday in elastic

    def test_filterForWeekday(self):
        cources_list = elastic.filterForWeekday(
            'Monday', ['Writing Fiction', 'Writing Poetry'])
        cources_list_1 = elastic.filterForWeekday(
            'Tuesday', ['Writing Fiction', 'Writing Poetry'])
        self.assertEqual('Writing Poetry' in cources_list_1, False)
        self.assertEqual(
            'Writing Fiction: One week course' in cources_list_1, True)
        self.assertEqual('Writing Fiction: The Novel' in cources_list_1, True)

# test  elastic getMultiTutors
    def test_getMultiTutors(self):
        self.assertEqual('Alan Mcmunnigall' in elastic.getMultiTutors(
            'Writing Fiction')[1], True)
        self.assertEqual('Pamela  Ross' in elastic.getMultiTutors(
            'Writing Fiction')[1], True)

# test  elastic check_pt_ft_course
    def test_check_pt_ft_course(self):
        self.assertEqual(elastic.check_pt_ft_course(
            'BIOINFORMATICS'), ('running', ['Bioinformatics', ['full-time']]))
        self.assertEqual(elastic.check_pt_ft_course(
            'Academic Practice'), ('running', ['Academic Practice', ['part-time']]))
        self.assertEqual(elastic.check_pt_ft_course('ADVANCED PRACTICE IN HEALTH CARE'), ('running', [
                         'Advanced Practice In Health Care', ['part-time']]))
        self.assertEqual(elastic.check_pt_ft_course(
            'Cancer Sciences'), ('not_running', []))


if __name__ == '__main__':
    unittest.main()
