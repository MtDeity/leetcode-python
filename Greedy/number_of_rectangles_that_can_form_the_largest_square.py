class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = largest_square = 0
        for rectangle in rectangles:
            min_length = min(rectangle)
            if min_length > largest_square:
                largest_square = min_length
                count = 1
            elif min_length == largest_square:
                count += 1
        return count
