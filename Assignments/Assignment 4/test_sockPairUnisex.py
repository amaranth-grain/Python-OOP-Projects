from unittest import TestCase
import garments as g


class TestSockPairUnisex(TestCase):

    def test_sock_pr_valid(self):
        d_sock_pr = {"style_name": "modern",
                     "colour": "grey",
                     "dry_cleaning": "y",
                     "textile": "silk",
                     "size": "m"}
        sock_pr = g.SockPairUnisexPineappleRepublic(**d_sock_pr)
        self.assertEqual(g.SockPairUnisexPineappleRepublic, type(sock_pr))

    def test_sock_pr_dry_cleaning(self):
        pr = {"style_name": "modern",
              "colour": "grey",
              "dry_cleaning": "true",
              "textile": "silk",
              "size": "m"}

        self.assertRaises(ValueError,
                          g.SockPairUnisexPineappleRepublic,
                          **pr)

    def test_sock_pr_size(self):
        pr = {"style_name": "modern",
              "colour": "grey",
              "dry_cleaning": "true",
              "textile": "silk",
              "size": "xs"}

        self.assertRaises(ValueError,
                          g.SockPairUnisexPineappleRepublic,
                          **pr)

    def test_sock_ll_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "silver": "y",
             "textile": "silk",
             "size": "m"}
        sock_ll = g.SockPairUnisexLululime(**d)
        self.assertEqual(g.SockPairUnisexLululime, type(sock_ll))

    def test_sock_ll_silver(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "silver": "abc",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.SockPairUnisexLululime, **d)

    def test_sock_ll_size(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "silver": "true",
             "textile": "silk",
             "size": "xs"}

        self.assertRaises(ValueError, g.SockPairUnisexLululime, **d)

    def test_sock_n_valid(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "articulated": "Y",
             "length": "calf",
             "textile": "silk",
             "size": "m"}
        sock = g.SockPairUnisexNika(**d)
        self.assertEqual(g.SockPairUnisexNika, type(sock))

    def test_sock_n_articulated(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "articulated": ":)",
             "length": "calf",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.SockPairUnisexNika, **d)

    def test_sock_n_length(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "articulated": ":)",
             "length": "updog",
             "textile": "silk",
             "size": "m"}

        self.assertRaises(ValueError, g.SockPairUnisexNika, **d)

    def test_sock_n_size(self):
        d = {"style_name": "modern",
             "colour": "grey",
             "articulated": "y",
             "length": "calf",
             "textile": "silk",
             "size": "xxl"}

        self.assertRaises(ValueError, g.SockPairUnisexNika, **d)
