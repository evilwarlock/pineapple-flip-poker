# main function for flip pineapple poker
from deuces import deuces

from itertools import combinations 
import scipy.special

# get all combinations for all c(7,2) in 1st, 2nd, 3rd lane
# input : cards   :list[int] 
#         the input of 7 cards, e.g.[1,2,3,4,5,6,7]
# output: solution:list[list[int]]
#         all combination of 3 lanes solution, e.g.[[[1,2],[3,4],[5,6]],[[2,3],[4,5],[6,7]],...] 
def getCombinations(cards):
    # get all combinations for c(7,2)
    # print(cards)
    
    solution = []
    seven_cards = set(cards)
    # get all c(7,2)
    comb = combinations(seven_cards, 2)
    
    for i in comb:
        # initialize strategy
        first_lane = []

        # get 2 cards
        # print 2 cards
        # print(i)

        # add 2 cards to 1st_lane

        first_lane.append(list(i))
        # print(first_lane)
        
        # get 5 cards left
        five_cards = seven_cards.difference(set(i))
        comb2 = combinations(five_cards, 2)
        for j in comb2:
            second_lane = []
            second_lane.append(list(j))
            three_cards = set(five_cards).difference(set(j))
            comb3 = combinations(three_cards, 2)
            for k in comb3:
                third_lane = []
                third_lane.append(list(k))
                solution.append(first_lane + second_lane + third_lane)

    # print(len(solution))
    return solution
        
# point eval
def evaluateSolutions(board, solutions):
    # iterate all soluitons
    evaluator = deuces.Evaluator()
    for index, s in enumerate(solutions):
        lane1_cards = s[0]
        lane1_score = evaluator.evaluate(board, lane1_cards)
        lane1_class = evaluator.get_rank_class(lane1_score)

        lane2_cards = s[1]
        lane2_score = evaluator.evaluate(board, lane2_cards)
        lane2_class = evaluator.get_rank_class(lane2_score)

        lane3_cards = s[2]
        lane3_score = evaluator.evaluate(board, lane3_cards)
        lane3_class = evaluator.get_rank_class(lane3_score)

        print('For solution %d' % index)
        print( "lane 1 is %s" % evaluator.class_to_string(lane1_class))
        print( "lane 2 is %s" % evaluator.class_to_string(lane2_class))
        print( "lane 3 is %s\n" % evaluator.class_to_string(lane3_class))
        


# utility eval

if __name__ == "__main__":
    # one hand example
    # initialize one deck
    deck = deuces.Deck()

    # get 7 cards for hero
    holecards = deck.draw(7)

    # get 3 cards as flop
    flop = deck.draw(3)

    # check if the output are correct
    # print(flop)
    # print(holecards)

    # permutate all combination for 1st, 2nd, 3rd 
    # print(scipy.special.perm(7,2)) # total permutation number

    # get all possible soluitions
    three_lane_cards = getCombinations(holecards)
    
    # get all turn and river and evaluate hero points.
    turn_and_river = deck.draw(2)

    # set board
    board = flop + turn_and_river

    # eval all solutions
    current_points = evaluateSolutions(board, three_lane_cards)

    # show best choice