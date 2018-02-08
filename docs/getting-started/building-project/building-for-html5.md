## Work for all platforms


### 1. Clone Supernova project

#### For Linux or OSX:

Execute in terminal:

```git clone https://github.com/Deslon/Supernova.git```

#### For Windows:

On GitHub, navigate to the main page of the repository.

Under your repository name, click **Clone or download**.

### 2. Download and install Emscripten

Download from:

https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html

Follow instructions depending of your platform:

https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html#installation-instructions

We recommend to use version 1.35.0, because latest version (1.36.x) has a issue that can create wrong warnings (https://github.com/kripken/emscripten/issues/4234).

For Linux and OSX you can do:
```
./emsdk update

./emsdk install sdk-1.35.0-64bit

./emsdk activate sdk-1.35.0-64bit
```
For Windows, there is a simple installer.

### 3. Compile Supernova

#### For Linux and OSX:

Add Emscripten root to a system environment variable:

```export $EMSCRIPTEN=<path_to_emscripten>```

#### For Windows:

Install MinGW: https://sourceforge.net/projects/mingw-w64/

Note that MinGW must be in PATH environment variable of Windows. To test it, try to run ```mingw32-make``` in Prompt.

Install CMake: https://cmake.org/download/

During installation, choose to add to PATH. To test it, try to run ```cmake``` in Prompt.

#### All platforms

The directory where you clone Supernova go to: ```workspaces/emscripten/```

Execute in terminal:

```python build.py```

When finished you can see generated **.js** and **.html** files in **build/** folder. Open with any browser. 