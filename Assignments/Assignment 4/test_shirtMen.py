from unittest import TestCase
import garments as g


class TestShirtMen(TestCase):
    def test_shirt_men_ll_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": "m"}

        garment = g.ShirtMenLululime(**d)
        self.assertEqual(g.ShirtMenLululime, garment.__class__)

    def test_shirt_men_ll_sport(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running backwards",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtMenLululime, **d)

    def test_shirt_men_ll_pockets(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": [],
             "textile": "silk",
             "size": "m"}

        self.assertRaises(TypeError, g.ShirtMenLululime, **d)

    def test_shirt_men_ll_size(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": 123}

        self.assertRaises(AttributeError, g.ShirtMenLululime, **d)

    def test_shirt_men_n_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "requires_ironing": "y",
             "buttons": 9000,
             "textile": "silk",
             "size": "m"}

        garment = g.ShirtMenPineappleRepublic(**d)
        self.assertEqual(g.ShirtMenPineappleRepublic, garment.__class__)

    def test_shirt_men_pr_ironing(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "requires_ironing": "maybe",
             "buttons": 9000,
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtMenPineappleRepublic, **d)

    def test_shirt_men_pr_buttons(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "requires_ironing": "y",
             "buttons": "ao30",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtMenPineappleRepublic, **d)

