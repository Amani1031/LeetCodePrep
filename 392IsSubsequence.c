bool isSubsequence(char * s, char * t){
    int length = strlen(t);
    if (length == 0 && strlen(s) == 0){
        return true;
    }
    for (int i = 0 ; i < length ; i++){
        if (*s == *t){
            s++;
        }
        if (*s == '\0'){
            return true;
        }
        t++;
    }
    return false;
}
