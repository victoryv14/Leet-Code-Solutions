class Solution {
public:
    long long splitArray(vector<int>& nums) {
        int N = nums.size();
        vector <bool> spf(N+1,true);
        spf[0] = spf[1] = false;
        for( int i = 2; i * i < N+1; i++ ){
            if( spf[i] ) {
                for( int j = i * i; j < N+1; j += i ){
                    if ( spf[j] ) spf[j] = false;
                }
            }
        }
        long long sumA = 0, sumB = 0;
        for( int i = 0; i < N; i++ ){
            if(spf[i]) sumA += nums[i];
            else sumB += nums[i];
        }
        return abs(sumA - sumB);
    }
};