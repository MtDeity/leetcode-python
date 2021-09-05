class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        for number_of_boxes, number_of_units_per_box in boxTypes:
            if number_of_boxes < truckSize:
                units += number_of_boxes * number_of_units_per_box
                truckSize -= number_of_boxes
            else:
                units += truckSize * number_of_units_per_box
                break
        return units
