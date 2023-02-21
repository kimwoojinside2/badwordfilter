#include <stdio.h>
#include <Windows.h>

BYTE pressedList[1024] = {0,}; 
BYTE keyBuffer[1024] = {0,};
int keyBufferCount = 0;

void getGlobalKeyStatus() {
    memset(pressedList, 0, sizeof(pressedList));
    int pressedListCount = 0;

    for(BYTE i = 0; i != 0xFE + 0x1; i += 1) {
        if(isalpha(i) == TRUE) {
            if(GetAsyncKeyState(i) & 0x8000) {
                BYTE currentKey = i;

                BOOL listAppendFlag = TRUE;

                for(int j = 0; j != sizeof(pressedList); j += 1) {
                    if(pressedList[j] == currentKey) {
                        printf("duplicated value is detected\n");
                        listAppendFlag = FALSE;
                        break;
                    }
                } 

                if(listAppendFlag == TRUE) {
                    pressedList[pressedListCount] = currentKey;
                    pressedListCount += 1;
                }
            }
        }
    }

    while(TRUE) {
        Sleep(0);

        for(int i = 0; i != 0xFE + 0x1; i += 1) {
            if(isalpha(i) == TRUE) {
                if(GetAsyncKeyState(i) & 0x0001) {

                    printf("%c ", i);
    
                    keyBuffer[keyBufferCount] = i;
                    keyBufferCount += 1;

                    if(keyBufferCount == sizeof(keyBuffer)) {
                        keyBufferCount = 0;
                    }
                    
                    pressedList[i] = 0;
                }
            }
        }

        BOOL compareFlag = TRUE;
        for(int j = 0; j != sizeof(pressedList); j += 1) {
            if(pressedList[j] != 0) {
                compareFlag = FALSE;
                break;
            }
        }

        if(compareFlag == TRUE) {
            break;
        }
    }

    keyBufferCount = 0;

    return;
}


int main() {

    while(TRUE) {
        Sleep(0);
        getGlobalKeyStatus();
    }

    return 0;
}