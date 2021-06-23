# Dynamic Programming - Alien Vs Salesman
A salesperson lives on the coast. They travel to various cities along the coast to work. Sometimes
they stay in a city for a day or a few days to work, and other times they simply pass
through on their way to another city.

However, an Alien association has instituted a policy of having human travellers to go to prison for some days, but only if they want to stay in the city. If they are just passing through, they can continue on their way
without going to prison. Also, each city asks visitors to stay in prison for a different amount of time.

The salesperson has an idea of how much money they can make by working in each city, for
each day. They need to decide which cities to travel to, and which cities to work in, in order
to make the most money.

Each day, the salesperson can either work for the day in their current city, or they can travel to either adjacent city. Traveling always takes 1 day,
and since the cities are along a coast, each city has two adjacent cities, except for two cities on
the ends of the coast, which only have 1.

## Input
We think of the n cities as being numbered 0...n-1. In one day, the salesperson can travel
from city i to either city i+1 or i-1. From city 0 they can only travel to city 1, and from city
n-1 they can only travel to city n-2.

**profit** is a list of lists. All interior lists are length n. Each interior list represents a different
day. profit[d][c] is the profit that the salesperson will make by working in city c on day d.

**prison_time** is a list of non-negative integers. **prison_time**[i] is the number of
days city i requires visitors to stay in prison before they can work there.

## Output
**best_itinerary** returns an integer, which is the maximum amount of money that can be
earned by the salesperson.

## Example
```
profit = [
[6, 9, 7, 5, 9]
[4, 7, 3, 10, 9]
[7, 5, 4, 2, 8]
[2, 7, 10, 9, 5]
[2, 5, 2, 6, 1]
[4, 9, 4, 10, 6]
[2, 2, 4, 8, 7]
[4, 10, 2, 7, 4]]
prison_time = [3,1,1,1,1]
best_itinerary(profit, prison_time, 0)
>>> 39
best_itinerary(profit, prison_time, 1)
>>> 54
best_itinerary(profit, prison_time, 2)
>>> 47
best_itinerary(profit, prison_time, 3)
>>> 57
best_itinerary(profit, prison_time, 4)
>>> 51
```

- h=0. The salesperson works in city 0 on the first day, then travels to city 1 on the second
day, quarantines on the third day, then works in city 1 for the remaining days.
- h=1. The salesperson works in city 1 every day.
- h = 2. The salesperson works in city 2 on the first day, then travels to city 3 on the
second day, quarantines on the third day, then works in city 3 for the remaining days.
- h=3. The salesperson works in city 3 every day.
- h=4. The salesperson works in city 4 for 3 days, then travels to city 3 on the fourth day,
quarantines for a day, then works in city 3 for 3 days.

## Complexity
best_itinerary should run in O(nd) time and space, where n is the number of cities, and d
is the number of days (i.e. the number of interior lists in profit). In the above example, n =
5, d = 8.

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

