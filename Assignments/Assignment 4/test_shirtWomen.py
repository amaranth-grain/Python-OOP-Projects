from unittest import TestCase
import garments as g


class TestShirtWomen(TestCase):

    def test_shirt_women_ll_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": "m"}

        garment = g.ShirtWomenLululime(**d)
        self.assertEqual(g.ShirtWomenLululime, garment.__class__)

    def test_shirt_women_ll_sport(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running backwards",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtWomenLululime, **d)

    def test_shirt_women_ll_pockets(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": [],
             "textile": "silk",
             "size": "m"}

        self.assertRaises(TypeError, g.ShirtWomenLululime, **d)

    def test_shirt_women_ll_size(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "sport": "running",
             "hidden_zipper_pockets": 30,
             "textile": "silk",
             "size": 123}

        self.assertRaises(AttributeError, g.ShirtWomenLululime, **d)

    def test_shirt_women_n_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "indoor_or_outdoor": "indoor",
             "textile": "silk",
             "size": "m"}

        garment = g.ShirtWomenNika(**d)
        self.assertEqual(g.ShirtWomenNika, garment.__class__)

    def test_shirt_women_n_io(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "indoor_or_outdoor": "halfway",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtWomenNika, **d)

    def test_shirt_women_pr_ironing(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "requires_ironing": "maybe",
             "buttons": 9000,
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtWomenPineappleRepublic, **d)

    def test_shirt_women_pr_buttons(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "requires_ironing": "y",
             "buttons": "ao30",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.ShirtWomenPineappleRepublic, **d)