from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams from the given list of strings.
        
        Args:
        - strs (List[str]): List of strings to be grouped.

        Returns:
        - List[List[str]]: A list containing lists of anagrams.
        """
        
        # A dictionary to store grouped anagrams.
        dicto = {}

        # Loop through each string in the given list.
        for string in strs:
            # Sort the string and join it back to a single string.
            sorted_str = ''.join(sorted(string))

            # If the sorted string is already a key in the dictionary, append the original string to its list.
            if sorted_str in dicto:
                dicto[sorted_str].append(string)
            # Otherwise, create a new list for this key and add the original string.
            else:
                dicto[sorted_str] = [string]

        # Print the original list of strings.
        print(strs)
        
        # Return the grouped anagrams.
        return list(dicto.values())
