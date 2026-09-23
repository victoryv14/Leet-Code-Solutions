class Solution {
public:
    int climbStairs(int n) {
        int base_1 = 1;
        int base_2 = 2;
        if( n == 1 || n == 2 ) return ( n == 1 ) ? base_1 : base_2;
        else {
            for(int i = 3; i <= n; i++ ){
                int temp = base_1 + base_2;
                base_1 = base_2;
                base_2 = temp;
            }
            return base_2;
        }
    }
};