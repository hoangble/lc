def pairwise(seq):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    if seq:
        return zip(seq, seq[1:])
    else:
        return zip()


def cmp(x, y):
    """Return an integer depending on the comparison of two values.
    Return -1 if x <  y,
            0 if x == y,
            1 if x >  y.
    """
    return (x > y) - (y > x)  # a common Python trick: bool values to int


def count_monotonic_subsequences(seq):
    """Return the number of monotonic (consecutive) subsequences of
    length at least 2 in a sequence."""
    run_length = 0
    prev_cmp = None  # no comparisons done yet
    count_so_far = 0
    inc, dec, con = [], [], []
    last_idx = 0
    # For each item, add how many monotonic sequences end with that item
    for idx, (prev_item, item) in enumerate(zip(seq, seq[1:]), 1):
        this_cmp = cmp(prev_item, item)
        if this_cmp == prev_cmp:
            run_length += 1  # this item extends the previous mono subsequence
            if run_length >= 2:
                extra = [prev_item, item]
                if item == prev_item:
                    con.append(extra)
                elif item < prev_item:
                    dec.append(extra)
                else:
                    inc.append(extra)

        else:
            run_length = 1  # this item begins a new monotonic subsequence
            last_idx = idx

        # whenever we move, we have to add every single one in btw
        curr_seq = seq[idx - run_length : idx + 1]

        print(f"{prev_item, item, last_idx, run_length, curr_seq}")
        if item == prev_item:
            con.append(curr_seq)
        elif item < prev_item:
            dec.append(curr_seq)
        else:
            inc.append(curr_seq)
        prev_cmp = this_cmp
        count_so_far += run_length  # add new mono subsequences ending here

    print(f"{inc = }")
    print(f"{con = }")
    print(f"{dec = }")

    return count_so_far


print(count_monotonic_subsequences([1, 2, 3, 3, 2, 0, 1, 2, 4, 0, 0]))
