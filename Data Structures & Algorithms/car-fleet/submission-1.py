class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        fleet = 0
        fleet_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > fleet_time:
                fleet += 1
                fleet_time = time
        
        return fleet