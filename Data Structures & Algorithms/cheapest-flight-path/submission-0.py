class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: prices[city]
        # = 從 src 出發，目前知道到這個 city 的最低價格
        prices = [float("inf")] * n
        prices[src] = 0

        # Step 2: 最多 k stops
        # = 最多 k + 1 段 flights (0 stop -> 最多 1 段 flights)
        for _ in range(k + 1):

            # Step 3:
            # prices = 上一輪
            # temp   = 這一輪
            # 讀 prices 寫 temp
            # 不能直接在 prices 上改，不然同一輪可能偷偷走很多段 flight
            temp = prices.copy()

            # Step 4:
            # 看每一班 flight: [from_city, to_city, cost]
            for from_city, to_city, cost in flights:
                # 如果上一輪根本還到不了 from_city，
                # 那這班 flight 現在也沒有辦法搭
                # 例如：prices[1] = inf 那就不能從 1 飛到其他地方
                if prices[from_city] == float("inf"):
                    continue

                # Step 5:
                # 嘗試用這班 flight 更新 to_city
                # 原本到 to_city 的最低價格: temp[to_city]
                # 新的可能價格：prices[from_city] + cost
                # 取比較便宜的
                temp[to_city] = min(
                    temp[to_city],
                    prices[from_city] + cost
                )

            # Step 6:
            # 這一整輪全部處理完，
            # 才把新的結果變成下一輪的 prices
            prices = temp

        # Step 7:
        # 看最後能不能到 dst
        if prices[dst] == float("inf"):
            return -1

        return prices[dst]
