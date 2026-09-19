class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(xCenter,x2))
        closestY = max(y1, min(yCenter,y2))
        closestX_distance = xCenter - closestX
        closestY_distance = yCenter - closestY
        distanceSquared = (closestX_distance**2) + (closestY_distance**2)
        return distanceSquared <= (radius**2)