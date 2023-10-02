def trap(self, height: List[int]) -> int:
        
    if height == 0: return 0
        
    volume = 0
    left, right = 0, len(height)-1
    leftMax, rightMax = height[left], height[right]
        
    while left < right:
        leftMax, rightMax = max(height[left], leftMax), max(height[right], rightMax)
            
        if leftMax <= rightMax:
            volume += leftMax - height[left]
            left += 1
        else:
            volume += rightMax - height[right]
            right -= 1
                
    return volume
