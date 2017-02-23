Comandos para instalar OpenCV con miniconda ([DOC](https://conda.io/docs/using/envs.html)) y Python 3 para Windows, Mac o Linux.

Testeado en Windows 7 x64:


0. Si aún no tienes Anaconda o miniconda instalado en tu ordenador: descarga e instala [miniconda con Python 3.5 (64-bit)](https://conda.io/miniconda.html)
  
1. Actualiza conda a la última versión disponible y crea un entorno desde la ventana de comandos o terminal:

  `conda update conda`
  
  `conda create --name pyOCV python==3.5.0`
  
2. Activación de entorno:

  Windows: `activate pyOCV` 
  
  Linux/Mac: `$source activate pyOCV`
  
  **Comprueba que la ventana de comandos se ha activado el entorno correctamente (aparece junto a la ruta).**
  
3. Instalación de OpenCV junto a sus dependencias (mínimas)

  `conda install -c menpo opencv3=3.1`
 
4. Instalación de librerías auxiliares para el curso

  `conda install jupyter matplotlib`
  
5. [Descarga este repositorio](https://github.com/CAChemE/curso-opencv-python/archive/master.zip) y comprueba que eres capaz de ejecutar el script `test_playvideo.py`

  `python test_playvideo.py`

---

Log de instalación:

```
C:\Users\franz\Desktop\OpenCV-intro>conda update conda
Fetching package metadata .............
Solving package specifications: .

# All requested packages already installed.
# packages in environment at C:\Users\franz\Miniconda3:
#
conda                     4.3.11                   py35_0

C:\Users\franz\Desktop\OpenCV-intro>conda create --name pyOCV python==3.5.0
Fetching package metadata .............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyO

The following NEW packages will be INSTALLED:

    msvc_runtime: 1.0.1-vc14_0  [vc14]
    pip:          9.0.1-py35_1
    python:       3.5.0-4
    setuptools:   27.2.0-py35_1
    wheel:        0.29.0-py35_0

Proceed ([y]/n)? y

msvc_runtime-1 100% |###############################| Time: 0:00:01   1.75 MB/s
python-3.5.0-4 100% |###############################| Time: 0:00:09   2.86 MB/s
#
# To activate this environment, use:
# > activate pyOCV
#
# To deactivate this environment, use:
# > deactivate pyOCV
#
# * for power-users using bash, you must source
#


C:\Users\franz\Desktop\OpenCV-intro>activate pyOCV

(pyOCV) C:\Users\franz\Desktop\OpenCV-intro>conda install -c menpo opencv3=3.1
Fetching package metadata ...............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyOCV:

The following NEW packages will be INSTALLED:

    mkl:     2017.0.1-0
    numpy:   1.12.0-py35_0
    opencv3: 3.1.0-py35_0  menpo

Proceed ([y]/n)? y

numpy-1.12.0-p 100% |###############################| Time: 0:00:01   2.90 MB/s
opencv3-3.1.0- 100% |###############################| Time: 0:00:26   1.67 MB/s

(pyOCV) C:\Users\franz\Desktop\OpenCV-intro>conda install jupyter matplotlib scipy
Fetching package metadata ...............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyOCV:

The following NEW packages will be INSTALLED:

    bleach:              1.5.0-py35_0
    colorama:            0.3.7-py35_0
    cycler:              0.10.0-py35_0
    decorator:           4.0.11-py35_0
    entrypoints:         0.2.2-py35_1
    html5lib:            0.999-py35_0
    icu:                 57.1-vc14_0              [vc14]
    ipykernel:           4.5.2-py35_0
    ipython:             5.1.0-py35_0
    ipython_genutils:    0.1.0-py35_0
    ipywidgets:          5.1.5-py35_0       menpo
    jinja2:              2.9.4-py35_0
    jpeg:                9b-vc14_0                [vc14]
    jsonschema:          2.5.1-py35_0
    jupyter:             1.0.0-py35_3
    jupyter_client:      4.4.0-py35_0
    jupyter_console:     5.0.0-py35_0
    jupyter_core:        4.2.1-py35_0
    libpng:              1.6.27-vc14_0            [vc14]
    markupsafe:          0.23-py35_2
    matplotlib:          2.0.0-np112py35_0
    mistune:             0.7.3-py35_0
    nbconvert:           5.1.1-py35_0
    nbformat:            4.2.0-py35_0
    notebook:            4.3.1-py35_1
    openssl:             1.0.2k-vc14_0            [vc14]
    pandocfilters:       1.4.1-py35_0
    path.py:             10.0-py35_0
    pickleshare:         0.7.4-py35_0
    prompt_toolkit:      1.0.9-py35_0
    pygments:            2.1.3-py35_0
    pyparsing:           2.1.4-py35_0
    pyqt:                5.6.0-py35_2
    python-dateutil:     2.6.0-py35_0
    pytz:                2016.10-py35_0
    pyzmq:               16.0.2-py35_0
    qt:                  5.6.2-vc14_3             [vc14]
    qtconsole:           4.2.1-py35_2
    scipy:               0.18.1-np112py35_1
    simplegeneric:       0.8.1-py35_1
    sip:                 4.18-py35_0
    six:                 1.10.0-py35_0
    testpath:            0.3-py35_0
    tk:                  8.5.18-vc14_0            [vc14]
    tornado:             4.4.2-py35_0
    traitlets:           4.3.1-py35_0
    vs2015_runtime:      14.0.25123-0
    wcwidth:             0.1.7-py35_0
    widgetsnbextension:  1.2.3-py35_1       menpo
    win_unicode_console: 0.5-py35_0
    zlib:                1.2.8-vc14_3             [vc14]

Proceed ([y]/n)? y

entrypoints-0. 100% |###############################| Time: 0:00:00   1.04 MB/s
pandocfilters- 100% |###############################| Time: 0:00:00   1.15 MB/s
testpath-0.3-p 100% |###############################| Time: 0:00:00   1.72 MB/s
html5lib-0.999 100% |###############################| Time: 0:00:00   1.90 MB/s
scipy-0.18.1-n 100% |###############################| Time: 0:00:03   3.09 MB/s
bleach-1.5.0-p 100% |###############################| Time: 0:00:00   1.86 MB/s
matplotlib-2.0 100% |###############################| Time: 0:00:02   3.14 MB/s
nbconvert-5.1. 100% |###############################| Time: 0:00:00   3.55 MB/s
widgetsnbexten 100% |###############################| Time: 0:00:03 388.75 kB/s
ipywidgets-5.1 100% |###############################| Time: 0:00:00 381.78 kB/s

(pyOCV) C:\Users\franz\Desktop\OpenCV-intro>
```
