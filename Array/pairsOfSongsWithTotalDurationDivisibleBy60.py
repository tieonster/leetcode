# You are given a list of songs where the ith song has a duration of time[i] seconds.

# Return the number of pairs of songs for which their
#  total duration in seconds is divisible by 60. 
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        hashmap = {}
        new_songs = []

        # Create new array which stores modulus of songs 60
        for song in time:
            new_songs.append(song % 60)

        # Create hashmap with counts
        for new_song in new_songs:
            if new_song not in hashmap:
                hashmap[new_song] = 1
            else:
                hashmap[new_song] += 1

        # Increment count of new songs (Two ways)
        # Method 1: (Goldman Sachs Hackerank method)
        for i in range(len(new_songs)):
            if 60-new_songs[i] in hashmap:
                # If song duration is 30, then minus one from count
                if (60-new_songs[i] == new_songs[i]):
                    count += hashmap[60-new_songs[i]]-1

                else:
                    count += hashmap[60-new_songs[i]]

            # If song duration is 10, then minus one from count in hashmap
            elif new_songs[i] == 0:
                count += hashmap[0]-1

        return count // 2 # Divide by 2 because we have double counted the count value when looping through

            ## My own method (Looping through hashmap instead)
            # for key, value in hashmap.items():
            #     if key == 0 or key == 30: # special case if key is 0 or 30, means the songs have to pair with itself. Find the number of such pairs using the formula: number of pairs = (n(n-1))/2
            #         add = int((value*(value-1))/2) # Formula to sum all values together
            #         count += add
                    
            #     elif key < 30: # Only increment count if key is less than 30, else there will be duplicates
            #         if key not in hashmap or (60-key) not in hashmap: # Check to make sure that key is in hashmap
            #             continue
                        
            #         else: # Increment count by multiplying current key count with 60-key count
            #             count += (hashmap[key]*hashmap[60-key])
                    
            #     else:
            #         continue
                    
            # return count