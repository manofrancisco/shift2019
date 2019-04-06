#include <iostream>
#include "install.cpp"
#include "string_utils.cpp"

char* txt = new char[10000];

int main() {

    check_install();

    FILE *f = fopen("digits.pi", "rb");
    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);
    //char txt[] = "34523012323712575514058317135740048030481764261272684473550571772";
    fread(txt, 10000, 1, f);


    return 0;
}


int search(char pattern[]){
    patsearch(txt,pattern);
}