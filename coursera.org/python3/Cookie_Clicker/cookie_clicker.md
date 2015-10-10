##### Cookie Clicker

Best Strategy: https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=700

    * For the cheap strategy, you need to choose the item that has the lowest cost (cheapest)
    each time.  This may change throughout the simulation because an item's cost increases
    after you buy an item.

    * For the expensive strategy, this is just the opposite.  Choose the item that has the
    highest cost (most expensive) each time.  However, you also need to factor in how much
    time is left when deciding which item you can buy.
 
Implement =Best= Strategy: https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=745

    * Obtain current cost of all items.
    * Identify the cheapest item in the list.
    * Identify the most expensive item in the list that I could afford.
    * If cookies >= most expensive item, return most expensive item.  Else return cheapest item.

Code sharing: https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=746

Strategy explained:

```
Let’s say you have two options in real life. Let’s say you want to buy chicken nuggets (let’s not worry about the quality of the chicken nuggets). McDonalds sells you chicken nuggets for 3.99$ and KFC sells them for 5.99$. However, that information alone isn’t enough to justify a decision: you need to know how many nuggets you get for that money.

Actually, you want to know how many nuggets can 1$ get you, so you have a unified metric and you can pick the most cost-effective option.

So, lets assume the following:

McDonalds -> 5 chicken nuggets for  3.99$ -> 5 / 3.99 = 1,253132832 nugget per dollar

KFC -> 8 chicken nuggets for 5.99 -> 8 / 5.99 = 1,335559265 nugget per dollar

So, even though KFC is more expensive than McDonalds, they are more cost-effective and you should buy from KFC.


Using the same principle in Cookie Clicker, you should divide the CPS each option gives you by it’s cost to find how cost-effective each option is. This alone gets you a 100% on the assignment.


But let’s think about how to make that even better. Sure, the obvious choice is to pick the most cost-effective option. But what happens if there are more than one options with EXACTLY the same cost-effectiveness?

Well, if we have not enough cookies to buy anything we should accumulate enough cookies to buy the cheapest possible upgrade. Why? Let’s think this through:

Option A: costs 10, gives +5 CPS and you need to wait 5 seconds.
Option B: costs 12, gives +6 CPS and you need to wait 6 seconds.

If you buy the upgrade B, then you wait 1 second extra. But the thing is, in this extra second you get only 2 cookies (since your current CPS is 2), whereas with option A in this spare second you’d make 7 cookies instead of 2.

So if you don’t have enough cookies, you should collect enough to buy the cheapest possible option, since that one will start making you more cookies sooner.

But what happens now if you do have enough cookies to buy an upgrade? Which one would you choose?

Well, here the answer isn’t as obvious as above. To think about that, let’s consider the following example:

Option A: costs 10, gives +5 CPS and you need to wait 5 seconds.
Option B: costs 12, gives +6 CPS and you need to wait 6 seconds.
Option C: costs 14, gives +7 CPS and you need to wait 7 seconds.
Option D: costs 16, gives +8 CPS and you need to wait 8 seconds.

Now let’s assume that when you buy an upgrade, the next one of that kind is not cost-efficient. This is assumed so that whenever we pick an upgrade, then the next time we have to pick one of the remaining.

So we have 20 cookies. If we pick option A, which is the cheapest, then the above technique (where we don’t have enough cookies) is not optimal, since the cheapest has changed:

Option A: costs 10, gives +5 CPS and you need to wait 5 seconds.
Option B: costs 12, gives +6 CPS and you need to wait 6 seconds.
Option C: costs 14, gives +7 CPS and you need to wait 7 seconds.
Option D: costs 16, gives +8 CPS and you need to wait 8 seconds.

But if he buy the most expensive we can (option D), then the algorithm for when we don’t have enough cookies works perfectly, since each time we will pick the least expensive option:

Option A: costs 10, gives +5 CPS and you need to wait 5 seconds.
Option B: costs 12, gives +6 CPS and you need to wait 6 seconds.
Option C: costs 14, gives +7 CPS and you need to wait 7 seconds.
Option D: costs 16, gives +8 CPS and you need to wait 8 seconds.

So, we understand that if we have enough for various options, we should buy the most expensive one, so our other algorithm can work optimally.
```
