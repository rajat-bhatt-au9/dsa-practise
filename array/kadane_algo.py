""" Question Link: https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1 """

#User function Template for python3
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        tempsum = a[0]
        finalsum = a[0]
        for i in range(1, size):
            tempsum = max(a[i], tempsum + a[i])
            finalsum = max(tempsum, finalsum)
        return finalsum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends