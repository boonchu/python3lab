###### Strategy for cc3

1. Cost per cookies-per-second. For example:

Cursor costs 15 cookies and produces 0.1 cookies per second. The cost per cookies-per-second is 15/0.1 = 150
Grandma costs 100 cookies, and produces 0.5 cookies per second. The cost per cookies-per-second is 100/0.5 = 200

Thus item A costs me less on a cookies-per-second basis, so I pick item A.

Another way to look at it: the Grandma costs 6.66666... times as much as the Cursor, but produces only 5 times as many cookies per second.

2. Another consideration was whether I could afford the item. For example, if my current CPS is 100, and I an thinking of buying a Cursor for 15 cookies that yields 0.1 CPS, but there is only 1 second left, then there is no point in buying the Cursor because it will cost me more than I will recoup before time runs out.

3. It occurred to me that I might want *some* cookies left over to purchase new items before time runs out, so maybe buying an item that exhausts my entire inventory is not a good idea.

I combined considerations 1, 2 and 3 in the body of the "for" loop. The 0.8 multiplier is for consideration 3. I cannot say for sure why it works, but in the end, it does yield more cookies than if I just compared the cost to "cookies + cps * time_left". I also considered factoring in the extra CPS that the new item would give me, and comparing the item cost to "cookies + (cps + item_cps) * time_left", but again, for reasons I am not certain, it made no difference. All of the above considerations gave me a yield of 1.31434353807e+18 cookies produced. Note that without consideration #3, my yield was 1.314018865e+18; so the multiplier made a rather significant improvement.

4. How did I arrive at always going with the cheapest item early in the simulation, while time_left > 9999993673.0? Well, I found that the "cheapest" strategy was actually more productive than the "expensive" strategy, so it occurred to me that maybe going the "cheapest" route early on, before moving on to more expensive items, might be viable.

For reasons I do not recall, I started looking at the number of more expensive items I already had before I bought more expensive items. My thinking was, "well, I just bought this really expensive item, so before I have to wait a while before buying another expensive item, I'll go the cheap route first." Ultimately I found a "sweet spot": that until I owned 2 Shipments, the "cheapest" strategy gave me an incremental bump in final cookie production. So that "if" statement used to be in the form of, "if my number of Shipments is less than 2, go the cheapest route". I experimented with other minimal numbers of pieces of equipment, but nothing I could try made any improvement. By that time, my total cookie production was up to 1.31434630618e+18.

I noticed by examining purchase history that it was still early in the simulation by the time I had acquired the second Shipment. It then occurred to me that maybe it wasn't a matter of the number of a given item I owned, but time in the simulation. So I starting with the time where that second Shipment was purchased, I started experimenting with buying the cheapest item when the time left in the simulation was greater than that time. Tweaking time a little bit, I found another "sweet spot" that yielded cookie production of 1.3143463088e+18, a marginal improvement over my prior score.
