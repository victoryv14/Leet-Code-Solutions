class Solution {
public:
    int reverseDegree(string s) {
        int reverse_degree = 0;
        for( int i = 0; i < s.size(); i++ ){
            reverse_degree += ('{' - s[i]) * ( i+1 );
        }
        return reverse_degree;
    }
};