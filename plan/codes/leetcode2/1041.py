# coding = utf-8
"""
困于环中的机器人
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 90
        x, y = 0, 0
        for i in instructions:
            if i == 'L':
                direction += 90
            elif i == 'R':
                direction -= 90
            else:
                if direction % 360 == 90:
                    y += 1
                elif direction % 360 == 180:
                    x -= 1
                elif direction % 360 == 270:
                    y -= 1
                else:
                    x += 1
        return x == y == 0 or direction % 360 != 90