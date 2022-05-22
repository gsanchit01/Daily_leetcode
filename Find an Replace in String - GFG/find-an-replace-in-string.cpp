// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    string findAndReplace(string S ,int Q, int index[], string sources[], string targets[]) {
        for(int i=0;i<Q;i++){
            size_t found = S.find(sources[i]);
            if(found!=string::npos){
                if(found==index[i]){
                    S.replace(index[i],sources[i].length(),targets[i]);
                    for(int j=i+1;j<Q;j++){
                        index[j] += targets[i].length()-sources[i].length();
                    }
                }
                else{
                    while(found!=string::npos && found!=index[i]){
                        found = S.find(sources[i],found+1);
                    }
                    if(found==index[i]){
                        S.replace(index[i],sources[i].length(),targets[i]);
                        for(int j=i+1;j<Q;j++)
                            index[j] += targets[i].length()-sources[i].length();
                    }
                }
            }
        }
        return S;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin>>S;
        
        int Q;
        cin>>Q;
        int index[Q];
        string sources[Q], targets[Q];
        
        for(int i=0; i<Q; i++)
            cin>>index[i];
        for(int i=0; i<Q; i++)
            cin>>sources[i];
        for(int i=0; i<Q; i++)
            cin>>targets[i];

        Solution ob;
        cout<<ob.findAndReplace(S,Q,index,sources,targets)<<endl;
    }
    return 0;
}  // } Driver Code Ends