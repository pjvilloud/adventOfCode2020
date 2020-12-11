"""--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 980499.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 200637446."""

list_numbers = [1706, 1466, 1427, 1744, 1684, 1386, 2001, 1750, 1753, 1770, 1559, 1616, 1408, 1860, 1940, 2002, 1862,
                1918, 1456, 1209, 1840, 1462, 1783, 1644, 1901, 1791, 1506, 2005, 1338, 1383, 1420, 1631, 1784, 1897,
                1771, 1588, 1955, 1937, 1392, 1396, 1803, 1429, 1407, 1698, 1562, 1913, 1678, 1198, 1398, 1703, 1831,
                1489, 1782, 1864, 1708, 1397, 1915, 1953, 1395, 1610, 1549, 1564, 1973, 1931, 2009, 1980, 1800, 1443,
                1993, 1900, 1964, 1581, 1904, 1665, 1567, 1057, 1805, 1402, 1878, 1729, 1825, 1682, 1719, 1469, 1004,
                1591, 1594, 811, 1523, 1424, 1756, 373, 1442, 1718, 1411, 1892, 1820, 1977, 1871, 1890, 1653, 1372, 1475,
                1476, 1422, 2004, 1755, 1676, 639, 1425, 1853, 1712, 1525, 1514, 1455, 1658, 1963, 1579, 1861, 1458,
                1474, 1613, 1681, 1586, 1441, 1499, 1865, 1735, 1989, 1952, 792, 1669, 1509, 1481, 1893, 1445, 1834,
                1779, 1732, 1826, 1595, 1829, 449, 1920, 1707, 1780, 1935, 1867, 1769, 1107, 919, 1382, 1604, 1875, 1453,
                1496, 1946, 1659, 1570, 1692, 1630, 1638, 1922, 1691, 1580, 1880, 1482, 1762, 1775, 1376, 1434, 1856,
                1971, 1646, 1951, 1416, 1889, 1773, 1814, 1471, 1488, 1736, 1743, 1459, 1389, 1498, 1663, 1611, 1727,
                1699, 1624, 1511, 1767, 1754, 1785, 1491, 1235, 1510, 1500, 1485]

for i1 in range(len(list_numbers) - 1, 0, -1):
    for i2 in range(len(list_numbers)):
        if i1 < i2 and list_numbers[i1] + list_numbers[i2] == 2020:
            print "Winner is: ", list_numbers[i1], " * ", list_numbers[i2], " = ", list_numbers[i1] * list_numbers[i2]
        i2 += 1
    i1 -= 1

for i1 in range(len(list_numbers) - 1, 0, -1):
    for i2 in range(len(list_numbers)):
        for i3 in range(1, len(list_numbers)):
            if i2 < i3 and list_numbers[i1] + list_numbers[i2] + list_numbers[i3] == 2020:
                print "Winner is: ", list_numbers[i1], " * ", list_numbers[i2], " * ", list_numbers[i3], " = ", \
                    list_numbers[i1] * list_numbers[i2] * list_numbers[i3]
                break
            i3 += 1
        else:
            i2 += 1
            continue
        break
    else:
        i1 -= 1
        continue
    break
