class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the complement and its index
        complement_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement needed to reach the target
            # Check if the complement is already in the dictionary
            if complement in complement_map:
                # If found, return the current index and the index of the complement
                return [complement_map[complement], i]
            # Otherwise, store the current number with its index
            complement_map[num] = i
