//
// Created by Francisco Ferreira on 2019-04-05.
//
#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
#include <random>


using namespace std;
void getdigits();
void setup();
int get_server_info();
int chunk_size = 10;
int partition_size = 10000;

void getdigits(){
    random_device rd;  //Will be used to obtain a seed for the random number engine
    mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    uniform_int_distribution<> dis(0, 9);
    ofstream digits_file;
    digits_file.open ("digits.pi");
    for (int n=0; n<partition_size; ++n)
        digits_file << dis(gen) ;
    digits_file.close();
    cout << "Numbers generated\n";
}



void check_install(){
    string filename = "digits.pi";
    if (FILE *file = fopen(filename.c_str(), "r")) {
        fclose(file);
        cout << "exists";
    } else {
        cout << "Does not exist, setting up\n";
        setup();
    }
}

int get_server_info(){
    return 1;
}

void setup(){
    int info = get_server_info();
    int client_id = info;
    cout << "ClientID: "<< client_id <<"\n" ;
    ofstream client_file;
    client_file.open ("client.id");
    client_file << client_id ;
    client_file.close();
    getdigits();
}

