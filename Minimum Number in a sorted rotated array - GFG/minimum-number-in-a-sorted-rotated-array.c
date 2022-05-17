// { Driver Code Starts
//Initial Template for C

#include <stdio.h>


 // } Driver Code Ends
//User function Template for C


//Function to find the minimum element in sorted and rotated array.
static long minNumber(int arr[], long low, long high)
    {
		
		while(low<=high){
			if(low==high)
				return arr[(int)low];
			long mid=  (low+high)/2;
			if(mid<high && arr[(int)mid+1]<arr[(int)mid])
				return arr[(int)mid+1];
			if(mid>low && arr[(int)mid-1]>arr[(int)mid])
				return arr[(int)mid];
			if(arr[(int) high]>arr[(int)mid])
				high=mid-1;
			else
				low = mid+1;
		}
		return arr[0];
    }

// { Driver Code Starts.

int main()
{
	
	int t;
	scanf("%d", &t);
	while(t--)
	{
		int n;
		scanf("%d", &n);
		int a[n];
		for(int i=0;i<n;++i)
			scanf("%d", &a[i]);	
	
		printf("%d\n", minNumber(a,0,n-1) );
	}
	return 0;
}  // } Driver Code Ends