input_test = """939
7,13,x,x,59,x,31,19"""

input = """1000495
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,521,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,523,x,x,x,x,x,37,x,x,x,x,x,x,13"""

split_input = input_test.splitlines()
earliest_departure_timestamp = int(split_input[0])

# Part 1
bus_ids = list(filter(lambda b_id: b_id != "x", split_input[1].split(",")))
earliest_departures = list()

for bus_id in bus_ids:
    earliest_departures.append( (earliest_departure_timestamp / int(bus_id) + 1) * int(bus_id))

waiting_time = min(earliest_departures) - earliest_departure_timestamp
earliest_bus = int(bus_ids[earliest_departures.index(min(earliest_departures))])

print "You need to wait", waiting_time, "for bus", earliest_bus, "so the answer is", waiting_time*earliest_bus

# Part 2
input_test = """xxx
1789,37,47,1889"""
split_input = input_test.splitlines()
bus_ids = split_input[1].split(",")
bus_ids_filtered = list(filter(lambda b_id: b_id != "x", split_input[1].split(",")))
bus_ids_filtered_int = list(map(lambda b_id: int(b_id), bus_ids_filtered))

max_timestamp = reduce(lambda x, y: x*y, bus_ids_filtered_int)
min_timestamp = max_timestamp / max(bus_ids_filtered_int)

n = 1

while n < max_timestamp:
    is_int = False
    for i in range(1, len(bus_ids_filtered_int)):
        if (bus_ids_filtered_int[0] * n + bus_ids.index(str(bus_ids_filtered_int[i]))) % bus_ids_filtered_int[i] != 0:
            is_int = False
            break
        else:
            is_int = True
    if is_int:
        break
    n += 1

print "n is", n
print "The answer is", n * bus_ids_filtered_int[0]
