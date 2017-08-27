#include <iostream>

#include "Platform.h"

int main (int argc, char *argv[])
{
    std::cout << "Hello there, " << Platform::name() << "!" << std::endl;
    
    return 0;
}
