// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


vector<int> permute(vector<vector<int>> &arr, int n);


int main() {
    
    int t;cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int>> arr(n);
        
        for(int i=0;i<n;i++)
        {
            int a, b;
            cin>> a>> b;
            arr[i].push_back(a);
            arr[i].push_back(b);
        }
        
        vector<int> ans;
        ans = permute(arr, n);
        for(int i=0;i<n;i++)
            cout << ans[i] << "\n";
        
    }
    
	return 0;
}// } Driver Code Ends



vector<int> permute(vector<vector<int>> &arr, int n)
{
   vector<pair<int, int>> time;
        //total time, index
   
   for(int i=0; i<n; i++) {
       int total_time = arr[i][0] + arr[i][1];
       
       time.push_back({total_time , i });
   }
   
   sort(time.begin(), time.end());
   
   vector<int> ans;
   for(auto it : time) {
       
       ans.push_back(it.second+1);
   }
   
   return ans;
}