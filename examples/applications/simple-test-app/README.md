# Simple Rust Test App
The Simple Rust Test App is a lightweight app written in Rust that shows a developer how to utilize the Chariott boilerplate code to connect to Chariott and interact with the Key Value Store app.

## Getting Started
To get started, one must have already built Chariott and the kv-app.  To do so follow the directions in the main [README.md](../../../README.md#build-all-binaries-and-run-tests) 

## Run Chariott, Key Value Store App and Test App
1. Now that Chariott and the other applications are built, we can run them manually

```bash
cd target/debug
./chariott &
./kv-app &
```

2. Now we can run the Simple Test App

```bash
./simple-test-app
```

3. As you could see in the last step, the simple test app wrote a pair of key/value pairs to the Key/Value store.  Now let's step through the code
    Open the explorer window in Visual Studio code or Ctrl+Shift+E
4. Open the file in examples/Applications/simple-test-app/src/main.rs
1. Now we can set a breakpoint so that you can step through the code.  For this example let's set one right where we connect to Chariott
![image.png](../media/visualstudio-debug-breakpoint.png)
6. Now that we have a breakpoint, we can click on "Debug" right above main and step through the application to learn how to interact with Chariott


