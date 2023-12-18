#include <stdio.h>
#include <iostream>
#include <signal.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

using namespace std;

int N;
int M;
char ***disk; //
char **frame; //RAM
short **table; //16
int **PFtoR;
int t = 0;
int freeSlot = 0;
int firstGo;

short fetch_phys_add(int i, int px) { //vraca indeks okvira u okvir[n]

    int idx = (px >> 6) & 0x0f; //6-9 bitovi, stranica tablice
    int present = (table[i][idx]>>5) & 1;
    char frameLoc; //char? lokacija dobivenog okvira u RAM-u
    
    int offset = px & 0x003f; //doljnjih 6, posmak

    if(firstGo) printf("\toffset: %d\n",offset);
    if(firstGo) printf("\tidx: %d\n",idx);

    if(!present){
        if(firstGo) printf("\tPromasaj!\n");

        if(freeSlot < M) {
            //printf("frame: %p\n",(void *)frame);
            //printf("disk: %p\n",(void *)disk);
            //printf("test frameLoc: %d\n",frameLoc);
            table[i][idx] = freeSlot << 6;
            table[i][idx] += 32 + t; 
            
            printf("\tStavljamo okvir u slobodan slot\n");

            for(int k = 0; k < 64; k++) {
                //printf("%d ",disk[i][idx][k]);
                frame[freeSlot][k] = disk[i][idx][k]; //provjeri
            }
            //printf("\n");

            PFtoR[i][idx] = freeSlot;
            frameLoc = freeSlot;
            freeSlot++;
            
        } else { //LRU
            printf("\tTrazimo najmanji LRU\n");
            int min = 31;
            int minLoc = 0;
            int process = 0;
            int minFrame = 0;

            for(int j = 0; j < N; j++) {
                for (int k = 0; k < 16; k++) {
                    int lru = table[j][k] & 0b00011111;
                    present = (table[j][k] & 0b00100000) >> 5;
                    if(present == 1 && lru < min) {
                        min = lru;
                        process = j;
                        minFrame = k;
                        minLoc = (table[j][k] & 0xffc0) >> 6;
                    }
                }
            }

            int lruToFind;
            int isPresent;
            int locToFind;
            int procToFind;
            int procFrame;
            int doBreak = 0;

            for(int j = 0; j < N; j++) {
                for (int k = 0; k < 16; k++) {
                    lruToFind = table[j][k] & 0x001f;
                    isPresent = (table[j][k] >> 5) & 1;
                    locToFind = (table[j][k] & 0xffc0) >> 6;
                    procToFind = j;
                    procFrame = k;

                    if(lruToFind == min && isPresent && locToFind == minLoc) {
                        table[j][k] &= 0x1111111111011111;
                        table[i][idx] = (minLoc<<6) + 32 + t;
                        doBreak = 1;
                        printf("\tIzbacuje se stranica 0x%x iz procesa %d\n\tLRU izbacene stranice: %d\n", k, j, lruToFind);
                        break;
                    }
                }
                if(doBreak) break;
            }

            for(int j = 0; j < 64; j++) {
                disk[procToFind][procFrame][j] = frame[minLoc][j]; 
                frame[minLoc][j] = disk[i][idx][j];
            }
            printf("\n");

            PFtoR[i][idx] = minLoc;
            frameLoc = minLoc;

        }
    } else {
        if(firstGo) printf("\tPogodak\n");
        frameLoc = PFtoR[i][idx];
        //printf("frameLoc: %d\n", frameLoc);
    }

    short physAddy = 0;
    physAddy = (frameLoc << 6) + offset;

    if(!firstGo) {
        printf("\tDani okvir: 0x%x\n", frameLoc);
        printf("fizicka adresa: 0x%x\n", frameLoc+offset);
        printf("zapis tablice: 0x%x\n", table[i][idx]);
    }
    
    
    return physAddy;
}

int fetch_data(int i, int px) {
    short y = fetch_phys_add(i,px);
    int frame1 = y >> 6;
    int offset = y & 0x003f;
    int j = frame[frame1][offset];
    return j;
}

void write_data(int i, int px, int j) {
    short y = fetch_phys_add(i,px); //int?
    int frame1 = y >> 6;
    int offset = y & 0x003f;

    frame[frame1][offset] = j;
    return;
}

int main(int argc, char **argv) {

    srand((unsigned int)time(NULL));

    N = atoi(argv[1]);
    M = atoi(argv[2]);

    disk = new char**[N];
    for (int i = 0; i < N; i++) {
        disk[i] = new char*[16];
        for (int j = 0; j < 16; j++) {
            disk[i][j] = new char[64];
            for(int k = 0; k < 64; k++) {
                disk[i][j][k] = 0;
            }
        }
    }   

    frame = new char*[M];
    for(int i = 0; i < M; i++) {
        frame[i] = new char[64];
        for(int j = 0; j < 64; j++) {
            frame[i][j] = 0;
        }
    }

    table = new short*[N];
    for(int i = 0; i < N; i++) {
        table[i] = new short[64];
        for(int j = 0; j < 64; j++) {
            table[i][j] = 0;
        }
    }

    PFtoR = new int*[N];

    for(int i = 0; i < N; i++) {
        PFtoR[i] = new int[16];
        for(int j = 0; j < 16; j++) {
            PFtoR[i][j] = 0;
        }
    }

    //int brojac = 0; //za testiranje, nije potrebno

    printf("------------------------\n");

    while(1) {
        for(int i = 0; i < N; i++) {
            printf("proces: %d\n",i);
            firstGo = 1;

            /*if(1/*p je proizv) {
                //stavi N − 1 poruka u zajednički spremnik
            } else {
                //uzmi poruku iz zs
            }*/
            int x = rand() & 0x03FE;
            
            printf("\tlog. adresa: 0x%x\n",x);
            int j = fetch_data(i,x); 

            printf("\tsadrzaj adrese: %d\n", j);

            j++;
            firstGo = 0;

            write_data(i,x,j);
            t++;
            
            if(t==31) { //ne izvodi li se ovo za LRU = 31, a ne t?
                t = 0;

                for(j = 0; j < N; j++) {
                    for(int k = 0; k < 16; k++) {
                        table[j][k] &= 0xffe0;
                    }
                }

                short idx = (x & 0b1111000000)>>6;

                table[i][idx]++;

                printf("t,LRU resetirani\n");
            }

            printf("------------------------\n");
            sleep(3);
        }
    }

    free(disk);
    free(frame);
    free(table);

    return 0;
}