//
// Created by Alaric on 2019-10-11.
//
class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size(); //n=4 , s = abcba 0 1 2 3 s[0] = a  i =1 j =3
        if (n < 2)
            return true;
        int i = 0,j = n-1; // i = 0, j=3
        while(i < j) {
            while (i < j && !isalnum(s[i]))
                i++;
            while (i < j && !isalnum(s[j]))
                j--;
            if (tolower(s[i++]) != tolower(s[j--]))
                return false; //i=2,j =1
        }
        return true;
    }
};
