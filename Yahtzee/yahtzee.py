"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor



# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    hand = tuple(sorted(hand))
    scores_dict = {}
    for num in hand:
        if num not in scores_dict:
            scores_dict[num] = num
        else:
            scores_dict[num] += num
    # print(scores_dict)
    maximum_key = max(scores_dict, key=scores_dict.get)
    max_value = scores_dict[maximum_key]

    return max_value


def expected_value(held_dice, num_die_sides, num_free_dice):
    """                                                                    
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    outcomes = [num for num in range(1,num_die_sides+1)]
    length = num_free_dice
    combinations = gen_all_sequences(outcomes,length)
    scores = 0
    for tup in combinations:
        new_hand = list(held_dice[:])
        for num in tup:
            new_hand.append(num)

        # print(new_hand)
        # print(score(new_hand))
        scores += score(new_hand)
    expected_value = scores/len(combinations)

    return expected_value


def gen_all_holds(hand):
    '''
    generate all possible choices of dice from hand to hold
    hand (a tuple): full yahtzee hand
    returns a set of tuples, where each tuple is dice to hold
    '''
    # just generate a power set from 'hand' (without following recipe with itertools)
    from_hand = [()]
    for item in hand:
        for subset in from_hand:
            from_hand = from_hand + [subset + (item,)]

    return set(from_hand)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_possible_hands_set = gen_all_holds(hand)
    # print(all_possible_hands_set)
    exp_val_dict = {}
    for tup in all_possible_hands_set:
        exp_val = expected_value(tup,num_die_sides,len(hand) - len(tup))
        exp_val_dict[tup] = exp_val
    print(exp_val_dict)
    max_ev_hand = max(exp_val_dict, key=exp_val_dict.get)

    return exp_val_dict[max_ev_hand],max_ev_hand


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)






# run_example()
print(strategy((1,),6))
# print(expected_value((1,5),6,1))
#
# outcomes = [1,2,3,4,5,6]
# print(gen_all_sequences(outcomes,1))