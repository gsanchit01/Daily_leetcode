// { Driver Code Starts
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    int transform (string A, string B){
        int l1=A.size(), l2=B.size(), hash[256]={0};
        if(l1!=l2)
            return -1;
        for(int i=0; i<l1; i++)
            hash[A[i]]++;
        for(int i=0; i<l2; i++)
            hash[B[i]]--;
        for(int i=0; i<256; i++){
            if(hash[i]!=0)
                return -1;
        }
        int i=l1-1, j=l2-1, cnt=0;
        while(i>=0 && j>=0){
            if(A[i]==B[j])
                j--;
            else
                cnt++;
            i--;
        }
        return cnt;
    }};


// { Driver Code Starts.

int main () 
{
    int t; cin >> t;
    while (t--)
    {
        string A, B; 
        cin >> A >> B;
        Solution ob;
        cout <<ob.transform (A, B) << endl;
    }
}  // } Driver Code Ends