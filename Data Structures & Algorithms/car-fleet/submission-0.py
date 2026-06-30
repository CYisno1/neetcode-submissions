class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort position in descending order, bc the car can only form fleet with the car ahead of it

        # time = (target - position) / speed
        # two cars will form a fleet
        # if and only if the car ahead has a time that is greater than or equal to the time of the car behind it
        # 重點是：因為我們已經按照 position 從大到小排序，所以我們是從離 target 最近的車開始看。

        cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)

        fleets = 0
        fleet_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            # 這台車比前面的 fleet 還慢，所以它追不上，必須自己形成一個新的 fleet。
            if time > fleet_time:
                fleets += 1
                fleet_time = time # 更後面的車要拿它當新的前方 fleet 來比較
            
        return fleets