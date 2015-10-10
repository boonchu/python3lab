####### cc4 improved (cc3 clone)

- use the following criteria (item_cost/item_cps + item_cost/cps)
  you need to take into consideration also the accumulation time
- remove the following from your code
        if time_left > 9999993673.0:
           return strategy_cheap(cookies, cps, history, time_left, build_info)

results yields 1314347034959928064.000000
- based on some kind of ROI (Return On Investment) calculation,
