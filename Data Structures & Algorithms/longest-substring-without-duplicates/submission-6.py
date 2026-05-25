class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window problem, left and right pointer
        # Variable to keep track of longest substring w/o repeating characters
        # Have a set of unique characters that are in substring s[left:right + 1]
        # Move right until s[right] is found in our set
        # Move our left until we found the corresponding character
        # Record each time our pointers move the size of our sliding window, compare it with our variable
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        # Initialize pointers
        left, right = 0, 0

        # Initialize set and tracker
        set_ = set()
        
        tracker = 0

        # While right less than length of s
        while right < len(s) - 1:
            # Increment right pointer
            set_.add(s[right])
            right += 1
            # If s[right] is in set
            print(f"left: {left}")
            print(f"right: {right}")
            print(f"list: {s[left:right + 1]}")
            if s[right] in set_:
                print(f"s[right]: {s[right]} was found in set_")
                # Move left until the first instance of character is off our sliding window
                while s[left] != s[right]:
                    set_.remove(s[left])
                    left += 1
                left += 1
            print(set_)
            # Max size between our tracker and current sliding window
            tracker = max(tracker, right - left + 1)
        return tracker