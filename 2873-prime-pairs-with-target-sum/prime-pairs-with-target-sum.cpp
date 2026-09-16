class Solution {
public:
    vector<vector<int>> findPrimePairs(int n) {
        vector <bool> spf(n+1,true);
        spf[0] = spf[1] = false;
        for( int i = 2; i * i < n+1; i++ ){
            if( spf[i] ) {
                for( int j = i * i; j < n+1; j += i ){
                    if( spf[j] ) spf[j] = false;
                }
            }
        }
        vector<vector<int>> pairs;
        for(int i = 1; i <= n/2; i++){
            int j = n - i;
            if( spf[i] && spf[j] ) pairs.push_back({i,j});
        }
        return pairs;
    }
};