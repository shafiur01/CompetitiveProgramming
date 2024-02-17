class Solution:
    def generate(self, numRows): # List[List[int]]:
        global prev
        output = []
        for i in range(numRows):
            if i == 0:
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1

                print(prev)
                while j < i:
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j - 1] + prev[j])
                    j += 1

                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        print(output)  # Return the output list of pascal values.


if __name__ == "__main__":
    triangle = Solution()
    print(triangle.generate(5))