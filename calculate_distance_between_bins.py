from trained import detection_array
# We suppose that the model only identified valid trash bins

GAP_TOLERANCE = 2

bin_groups = 0
group_starts = []
zero_gaps_between_groups = []

i = 0
last_group_end = -1

while i < len(detection_array):
    if detection_array[i] == 1:
        bin_groups += 1
        group_starts.append(i)

        gap = 0
        i += 1
        while i < len(detection_array):
            if detection_array[i] == 1:
                gap = 0
            else:
                gap += 1
                if gap > GAP_TOLERANCE:
                    break
            i += 1

        if last_group_end != -1:
            zero_gap = detection_array[last_group_end + 1:i - gap].count(0)
            zero_gaps_between_groups.append(zero_gap)

        last_group_end = i - gap - 1
    else:
        i += 1

if zero_gaps_between_groups:
    avg_zeros = sum(zero_gaps_between_groups) / len(zero_gaps_between_groups)
    print(f"Next trash can should be visible in the next 15-20 seconds: {avg_zeros:.2f}")

