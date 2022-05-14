// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
public:
int solve(int i,int j,int n,int m,vector<vector<int>>&matrix,vector<vector<int>> &dp)
{
    if(i<0 || i>=n || j<0 || j>=m || matrix[i][j]==-1)
    return 0;
    if(dp[i][j]!=-1) return dp[i][j];
    int l=solve(i+1,j-1,n,m,matrix,dp);
    int r=solve(i+1,j+1,n,m,matrix,dp);
    int d=solve(i+1,j,n,m,matrix,dp);
    return dp[i][j]=matrix[i][j]+max(l,max(r,d));
}
int MaxGold(vector<vector<int>>&matrix){
    // Code here
    int n=matrix.size();
    int m=matrix[0].size();
    vector<vector<int>> dp(n,vector<int> (m,-1));
    int ans=INT_MIN;
    for(int i=0;i<m;i++)
    {
        ans=max(ans,solve(0,i,n,m,matrix,dp));
    }
    return ans;
}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int m, n;
		cin >> m >> n;
		vector<vector<int>>matrix(m, vector<int>(n, 0));
		for(int i = 0; i < m; i++){
			for(int j = 0; j < n; j++)
				cin >> matrix[i][j];
		}
		Solution obj;
		int ans = obj.MaxGold(matrix);
		cout << ans <<'\n';
	}
	return 0;
}  // } Driver Code Ends