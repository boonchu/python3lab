def gen_all_sequences(outcomes, length):
    ans = set([()])
    for _ in range(length):
        ans = set([seq + tuple([item]) for item in outcomes for seq in ans])
    return ans

def score(hand):
    return max([hand.count(die) * die for die in set(hand)])

def expected_value(held_dice, num_die_sides, num_free_dice):
    roll_enum = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    return sum(score(held_dice + roll) for roll in roll_enum) / float(len(roll_enum))

def gen_all_holds(hand):
    return set(map(tuple, reduce(lambda r, d: r + [l + [d] for l in r], hand, [[]])))

#def gen_all_holds(hand):
#    return set(tuple(d for p, d in enumerate(hand) if i >> p & 1) for i in xrange(1 << len(hand)))

def strategy(hand, num_die_sides):
    return max([(expected_value(hold, num_die_sides, len(hand) - len(hold)), hold) for hold in gen_all_holds(hand)])

