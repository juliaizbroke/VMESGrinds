class Solution:
    def bestHand(self, ranks, suits):
        rank_count = {}
        suit_count = {}

        for i in range(5):
            r = ranks[i]
            s = suits[i]

            if r in rank_count:
                rank_count[r] += 1
            else:
                rank_count[r] = 1

            if s in suit_count:
                suit_count[s] += 1
            else:
                suit_count[s] = 1

            # Early flush detection
            if suit_count[s] == 5:
                return "Flush"

            # Early three-of-a-kind detection
            if rank_count[r] == 3:
                return "Three of a Kind"

        # Check for pair
        for r in rank_count:
            if rank_count[r] == 2:
                return "Pair"

        return "High Card"
