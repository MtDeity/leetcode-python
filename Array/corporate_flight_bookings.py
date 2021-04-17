from typing import List


class Solution:
    def corpFlightBookings(
        self,
        bookings: List[List[int]],
        n: int
    ) -> List[int]:
        flights: List[int] = [0] * n
        for first, last, seats in bookings:
            flights[first - 1] += seats
            if last < n:
                flights[last] -= seats
        for i in range(1, n):
            flights[i] += flights[i - 1]
        return flights
