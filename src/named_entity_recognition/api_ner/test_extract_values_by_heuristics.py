from unittest import TestCase

from named_entity_recognition.api_ner.extract_values_by_heuristics import find_values_in_quota, find_ordinals, \
    find_emails


class Test(TestCase):
    def test__find_values_in_quota(self):
        # GIVEN
        question = "Find the names of the customers who have order status both 'On Road' and \"Shipped\""
        # WHEN
        values = find_values_in_quota(question)

        # THEN
        self.assertEqual(['On Road',
                          'Shipped',
                          '%On Road%',
                          '%Shipped%',
                          '%On Road',
                          '%Shipped',
                          'On Road%',
                          'Shipped%'], values)

    def test__find_values_in_quota_apostroph_in_names(self):
        # GIVEN
        question = "Which head's name has the substring 'Ha'? List the id and name."
        # WHEN
        values = find_values_in_quota(question)

        # THEN
        self.assertEqual(['Ha', '%Ha%', '%Ha', 'Ha%'], values)

    def test__find_ordinals(self):
        # GIVEN
        question = ['how', 'many', 'third', 'head', 'of', 'department', 'are', 'older', 'than', '56', '?']

        # WHEN
        ordinals = find_ordinals(question)

        # THEN
        self.assertEqual(['3'], ordinals)

    def test__find_emails(self):
        # GIVEN
        question = 'Find id of the candidate whose email is stanley.monahan@example.org?'

        # WHEN
        ordinals = find_emails(question)

        # THEN
        self.assertEqual(['stanley.monahan@example.org'], ordinals)