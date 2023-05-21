def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    # initializing a count the keep track of the flowerbed planted
    count = 0
    # simulating the padding where we can plant our flowerbed
    flowerbed = [0] + flowerbed + [0]

    # we use a loop to iterate from 1 to the last but one index -> stay in the actual list
    for i in range(1, len(flowerbed) - 1):
        # checking if we are obeying the on adjacent rule
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1

            # we check if the count is less then or equal the n to help break out early
            if count >= n:
                return True
    # this helping us plant more then there is.
    return count >= n
