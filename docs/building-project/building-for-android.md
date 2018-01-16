## Work for all platforms

### 1. Clone Supernova project

#### For Linux or OSX:

Execute in terminal:

```git clone https://github.com/Deslon/Supernova.git```

#### For Windows:

On GitHub, navigate to the main page of the repository.

Under your repository name, click **Clone or download**.

### 2. Download and install Android Studio

Download 2.2 (or higher) version of Android Studio (http://tools.android.com/download/studio/canary/latest).

This version is necessary for external c builders support (http://tools.android.com/tech-docs/external-c-builds). Supernova uses CMake to build for Emscripten and Android.

Install it following instructions.

### 3. Open project

Open Android Studio, click in "Open an existing Android Studio project" and select ```workspace/android/``` where Supernova was cloned.

If asked to install Android NDK and CMake, select yes.