# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_conjured_degrades_twice_as_fast_before_sell_date(self):
        items = [Item("Conjured Bread", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_conjured_degrades_four_times_as_fast_after_sell_date(self):
        items = [Item("Conjured Bread", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_conjured_never_negative(self):
        items = [Item("Conjured Coffee", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()