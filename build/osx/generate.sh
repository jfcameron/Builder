#find . ! -name 'generate.sh' -type f -exec rm -f {} +
#find . ! -name '.*' -type d -exec rm -r -f {} +

cmake ../../cmake/ -G "Xcode" -DPLATFORM="PLATFORM_OSX"