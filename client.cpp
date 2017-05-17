#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/socket.h> 
#include <arpa/inet.h>
using namespace std; 

int main(int argc , char *argv[])
{
    int socket_desc;
    struct sockaddr_in server;
    char message[1024], line[1024] , server_reply[2000];
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
     
    if (socket_desc == -1)
    {
        cout<<"Could not create socket";
        exit(0);
    }
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons( 8888 );
 
    //Connect to remote server
    if (connect(socket_desc , (struct sockaddr *)&server , sizeof(server)) < 0)
    {
        cout<<"connect error";
        return 1;
    }
     
    cout<<"Connected\n";
    cout<<"Enter the file name:";
    cin>>message;
    cout<<message;
    FILE *fptr=fopen(message,"r");

    int iter = 0;
    //Send some data
    while (fscanf(fptr,"%s",line) != EOF) {
    	std::cout<<"\n "<<iter++<<" "<<line;
        if( send(socket_desc , line , strlen(line) , 0) < 0)
        {
            cout<<"Send failed";
            return 1;
        }
        sleep(1);
    }
    send(socket_desc , "*" , strlen("*"), 0);
    fclose(fptr);
    
    cout<<"\nData Sent\n";
    fptr=fopen(message,"w");

    //Receive a reply from the server
    while(1) {
	    if( recv(socket_desc, server_reply , 2000 , 0) < 0)
	    {
	        cout<<"recv failed";
	    }
	    if (server_reply=="999999999") break;
        printf("%s\n",server_reply);
	    fprintf(fptr, "%s\n",server_reply);
	}    
	cout<<"Reply received\n";
	return 0;
}