#
1) find all items that fit my budget - empirically found out that using time_left/2 gave better results;
2) come up with some score that separated the best items; tried several approaches until it came to me i should maximize delta cps/cost, which gave the best results i had so far; messing around a bit with the score, the best results i had were with: delta cps * additional cps / cost

def item_score(curr_cps,cost,add_cps):
    """
    Aux score for best strategy; score is in a separate function because there were several attempts some of them quite complex.
    """
    return (curr_cps*add_cps)/(curr_cps+add_cps)/cost 

def strategy_best(cookies, cps, history, time_left, build_info):
    #build a list of items with cost <= max_price
    max_price = cookies+time_left/2*cps  #found empiricaly that time_left/2 gives best results
    items = []
    for item in build_info.build_items():
        if build_info.get_cost(item) <= max_price:
            items += [item]
    # if list is empty, return None
    if items == []:
        return None
    else:
        # for each item on the list, calculate a score based on current cps, additional cps and cost; return item with best score
        item_max_score = None
        max_score = -float('inf')
        for item in items:
            iscore = item_score(cps,build_info.get_cost(item),build_info.get_cps(item))
            if iscore > max_score:
                item_max_score = item
                max_score = iscore
        return item_max_score
