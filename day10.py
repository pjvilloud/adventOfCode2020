"""--- Day 10: Adapter Array ---
Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can figure out whether it will impact your vacation plans, however, your device suddenly turns off!

Its battery is dead.

You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of jolts. Always prepared, you make a list of all of the joltage adapters in your bag.

Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.

In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)

Treat the charging outlet near your seat as having an effective joltage rating of 0.

Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort and realize you can't even charge your device!

If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging outlet, the adapters, and your device?

For example, suppose that in your bag, you have adapters with the following joltage ratings:

16
10
15
5
1
11
7
19
6
12
4
With these adapters, your device's built-in joltage adapter would be rated for 19 + 3 = 22 jolts, 3 higher than the highest-rated adapter.

Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this:

The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly would need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any adapters, you have to pick the adapter rated 5 jolts (difference of 1).
Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7 (with difference of 1 and 1).
The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1), then 19 (difference of 3).
Finally, your device's built-in adapter is always 3 higher than the highest adapter, so its rating is 22 jolts (always a difference of 3).
In this example, when using every adapter, there are 7 differences of 1 jolt and 5 differences of 3 jolts.

Here is a larger example:

28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
In this larger example, in a chain that uses all of the adapters, there are 22 differences of 1 jolt and 10 differences of 3 jolts.

Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count the joltage differences between the charging outlet, the adapters, and your device. What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

Your puzzle answer was 2277.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

The first example above (the one that starts with 16, 10, 15) supports the following arrangements:

(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
(The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.

The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
46, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 48, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
47, 49, (52)

(0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
48, 49, (52)
In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.

You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?"""

bag_joltages = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
# bag_joltages = [99, 104, 120, 108, 67, 136, 80, 44, 129, 113, 158, 157, 89, 60, 138, 63, 35, 57, 61, 153, 116, 54, 7, 22, 133, 130, 5, 72, 2, 28, 131, 123, 55, 145, 151, 42, 98, 34, 140, 146, 100, 79, 117, 154, 9, 83, 132, 45, 43, 107, 91, 163, 86, 115, 39, 76, 36, 82, 162, 6, 27, 101, 150, 30, 110, 139, 109, 1, 64, 56, 161, 92, 62, 69, 144, 21, 147, 12, 114, 18, 137, 75, 164, 33, 152, 23, 68, 51, 8, 95, 90, 48, 29, 26, 165, 81, 13, 126, 14, 143, 15]
bag_joltages = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


# We sort the bags by ascending joltage
bag_joltages.sort()

# The built-in adapter joltage is max + 3
max_joltage_bag = max(bag_joltages) + 3

charging_outlet_joltage = 0

# Number of joltage difference of 1, 2 and 3 joltage
joltage_diff = [0, 0, 0]

# Initialization of the first diff with the charging outlet
joltage_diff[bag_joltages[0] - 1] = 1
all_joltage_diff = [0 for i in range(len(bag_joltages))]
all_joltage_diff[0] = bag_joltages[0]
last_joltage = bag_joltages[0]

nb_deletable_adatapter = 0
deletable_adapters = []
previous_1 = 0
sequence_of_1 = []
if bag_joltages[0] == 1:
    previous_1 = 1

for bag_joltage_index in range(1, len(bag_joltages)):
    joltage_difference = bag_joltages[bag_joltage_index] - last_joltage
    if joltage_difference == 1:
        previous_1 += 1
    else:
        sequence_of_1.append(previous_1)
        previous_1 = 0
    all_joltage_diff[bag_joltage_index] = joltage_difference
    if not(joltage_difference == 3 or all_joltage_diff[bag_joltage_index - 1] == 3 or joltage_difference == 2 and all_joltage_diff[bag_joltage_index - 1] == 2):
        deletable_adapters.append(bag_joltages[bag_joltage_index])
        nb_deletable_adatapter += 1
    if joltage_difference > 3:
        print "For adapter", bag_joltages[bag_joltage_index], "next one is", last_joltage
        break
    joltage_diff[joltage_difference - 1] += 1
    last_joltage = bag_joltages[bag_joltage_index]

#
joltage_diff[2] += 1
print joltage_diff
print "The number of 1-jolt differences multiplied by the number of 3-jolt differences is", joltage_diff[0] * joltage_diff[2]
print "The number of deletable adapters is", nb_deletable_adatapter
# print "The number of sequences of three 1 is", sequence_of_1
# 13260
# print "The number of arrangements is", pow(2, nb_deletable_adatapter) - pow(2, sequence_of_1)

mybase = [1, 2, 3, 4, 5]

arr = set()

def find_arrangements(base):
    # print base
    arr.add(','.join([str(x) for x in base]))
    if len(base) > 1:
        b = list(base)
        b.pop()
        find_arrangements(b)


def find_arr(babase):
    find_arrangements(babase)
    for i in range(len(babase)):
        bas = list(babase)
        bas.pop(i)
        find_arr(bas)
        # for j in range(len(ba)-1):
        #     ba.pop(0)
        #     find_arrangements(ba)
#
# find_arr(deletable_adapters)
print len(deletable_adapters)
print len(arr)
print arr
print bag_joltages
#2^15 = 32768
#Total 19208
#A supprimer 13560