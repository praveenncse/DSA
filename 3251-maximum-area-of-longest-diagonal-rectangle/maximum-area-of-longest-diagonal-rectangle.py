class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_sum_squares = 0
        max_product = 0

        for l, w in dimensions:
            sum_squares = l*l + w*w   
            product = l * w           

            if sum_squares > max_sum_squares or (sum_squares == max_sum_squares and product > max_product):
                max_sum_squares = sum_squares
                max_product = product
        return max_product