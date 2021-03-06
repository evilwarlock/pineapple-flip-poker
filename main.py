# main function for flip pineapple poker
from deuces import deuces

from itertools import combinations 
import scipy.special

# define points 
CLASS_POINTS ={
    1: 30,
    2: 20,
    3: 10,
    4: 6,
    5: 5,
    6: 4,
    7: 3,
    8: 2,
    9: 1
}

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
    points = {}
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
        
        lane1_points = CLASS_POINTS[lane1_class]
        lane2_points = CLASS_POINTS[lane2_class]
        lane3_points = CLASS_POINTS[lane3_class]

        # print( "lane 1 score is %d, hand is %s" % (lane1_score, evaluator.class_to_string(lane1_class)))
        # print( "lane 2 score is %d, hand is %s" % (lane2_score, evaluator.class_to_string(lane2_class)))
        # print( "lane 3 score is %d, hand is %s" % (lane3_score, evaluator.class_to_string(lane3_class)))
        # print( "lane 1 score is %s" % lane1_score)
        # print( "lane 2 score is %s" % lane2_score)
        # print( "lane 3 score is %s\n" % lane3_score)

        totalpoints  = lane1_points*5 + lane2_points*3 + lane3_points       
        points[str(s)] = totalpoints
  
        
    return points

def evaluateAllTurnRiverSolutions(flop, turnandriver, solutions):
    # iterate all soluitons
    evaluator = deuces.Evaluator()
    
    points = {}
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
        
        lane1_points = CLASS_POINTS[lane1_class]
        lane2_points = CLASS_POINTS[lane2_class]
        lane3_points = CLASS_POINTS[lane3_class]

        # print( "lane 1 score is %d, hand is %s" % (lane1_score, evaluator.class_to_string(lane1_class)))
        # print( "lane 2 score is %d, hand is %s" % (lane2_score, evaluator.class_to_string(lane2_class)))
        # print( "lane 3 score is %d, hand is %s" % (lane3_score, evaluator.class_to_string(lane3_class)))
        # print( "lane 1 score is %s" % lane1_score)
        # print( "lane 2 score is %s" % lane2_score)
        # print( "lane 3 score is %s\n" % lane3_score)

        totalpoints  = lane1_points*5 + lane2_points*3 + lane3_points       
        points[str(s)] = totalpoints
  
        
    return points    
        
# evaluate points
# def getPoints():
#     # Royal Flush      30  
#     # Straight Flush   20 
#     # Four of a Kind   10
#     # Full Houses      6
#     # Flush            5
#     # Straight         4 
#     # Three of a Kind  3
#     # Two Pair         2
#     # One Pair         1
#     # High Card        1 
#     #     1: "Straight Flush",
#     #     2: "Four of a Kind",
#     #     3: "Full House",
#     #     4: "Flush",
#     #     5: "Straight",
#     #     6: "Three of a Kind",
#     #     7: "Two Pair",
#     #     8: "Pair",
#     #     9: "High Card"
#     CLASS_POINTS ={
#         1: 30,
#         2: 20,
#         3: 10,
#         4: 6,
#         5: 5,
#         6: 4,
#         7: 3,
#         8: 2,
#         9: 1
#     }

    

# utility eval

if __name__ == "__main__":
    # one hand example
    # initialize one deck
    deck = deuces.Deck()

    # get 7 cards for hero
    holecards = deck.draw(7)

    # get 3 cards as flop
    flop = deck.draw(3)
    # print(deck.cards)
    # print(len(deck.cards))

    # check if the output are correct
    # print(flop)
    # print(holecards)

    # permutate all combination for 1st, 2nd, 3rd 
    # print(scipy.special.perm(7,2)) # total permutation number

    # get all possible soluitions
    three_lane_cards = getCombinations(holecards)
    
    # get one turn and river for test and evaluate hero points.
    # turn_and_river = deck.draw(2)

    # set board
    # board = flop + turn_and_river
    
    # # eval current test solutions
    # current_points = evaluateSolutions(board, three_lane_cards)
    # print(current_points)

    # iterate all turn and river cards
    all_turn_and_river = combinations(deck.cards, 2)

    # eval all turn and river solutions
    sum_points = evaluateAllTurnRiverSolutions(flop, all_turn_and_river, three_lane_cards)
    print(sum_points)


    # show best choice