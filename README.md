# expander-proto

1. Install protoc and add it to the PATH environment variable.  
   https://github.com/protocolbuffers/protobuf/releases  

2. Install python dependencies for nanopd  
   https://github.com/nanopb/nanopb
   ``` shell
   pip install scons protobuf grpcio-tools
   ```
   
3. Run **generate_all.cmd** to generate the .h/.c and .py files
