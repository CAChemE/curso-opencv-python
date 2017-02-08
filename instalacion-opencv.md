Comandos para instalar OpenCV con Python (Windows 7 64):

1. Instalación de [miniconda con Python 3.5 (64-bit)](https://conda.io/miniconda.html)
2. Creación de entorno en ventana de comandos:

  `conda create --name pyOCV python==3.5.1`
  
3. Activación de entorno:

  `activate pyOCV`
4. Instalación de OpenCV junto a sus dependencias (mínimas)

  `conda install -c conda-forge opencv=3.1.0`
 
5. Instalación de librerías auxiliares para el curso

`conda install jupyter matplotlib scipy`

Log de instalación:

```
C:\Users\franz>conda create --name pyOCV python==3.5.1
Fetching package metadata .............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyOCV:

The following NEW packages will be INSTALLED:

    pip:            9.0.1-py35_1
    python:         3.5.1-5
    setuptools:     27.2.0-py35_1
    vs2015_runtime: 14.0.25123-0
    wheel:          0.29.0-py35_0

Proceed ([y]/n)? y

python-3.5.1-5 100% |###############################| Time: 0:00:13   2.26 MB/s
setuptools-27. 100% |###############################| Time: 0:00:00   2.43 MB/s
pip-9.0.1-py35 100% |###############################| Time: 0:00:00   2.42 MB/s
#
# To activate this environment, use:
# > activate pyOCV
#
# To deactivate this environment, use:
# > deactivate pyOCV
#
# * for power-users using bash, you must source
#


C:\Users\franz>activate pyOCV

(pyOCV) C:\Users\franz>conda install -c conda-forge opencv=3.1.0
Fetching package metadata ...............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyOCV:

The following NEW packages will be INSTALLED:

    jpeg:    9b-vc14_0         conda-forge [vc14]
    libpng:  1.6.28-vc14_0     conda-forge [vc14]
    libtiff: 4.0.6-vc14_7      conda-forge [vc14]
    mkl:     2017.0.1-0
    numpy:   1.11.3-py35_0
    opencv:  3.1.0-np111py35_1 conda-forge
    vc:      14-0              conda-forge
    zlib:    1.2.11-vc14_0     conda-forge [vc14]

Proceed ([y]/n)? y

mkl-2017.0.1-0 100% |###############################| Time: 0:00:56   2.39 MB/s
jpeg-9b-vc14_0 100% |###############################| Time: 0:00:00 422.00 kB/s
vc-14-0.tar.bz 100% |###############################| Time: 0:00:00  59.34 kB/s
zlib-1.2.11-vc 100% |###############################| Time: 0:00:00 247.34 kB/s
libpng-1.6.28- 100% |###############################| Time: 0:00:00 824.26 kB/s
libtiff-4.0.6- 100% |###############################| Time: 0:00:00   1.47 MB/s
numpy-1.11.3-p 100% |###############################| Time: 0:00:01   2.43 MB/s
opencv-3.1.0-n 100% |###############################| Time: 0:00:42   2.10 MB/s

(pyOCV) C:\Users\franz>conda install jupyter scipy matplotlib
Fetching package metadata .............
Solving package specifications: .

Package plan for installation in environment C:\Users\franz\Miniconda3\envs\pyOCV:

The following NEW packages will be INSTALLED:

    colorama:            0.3.7-py35_0
    cycler:              0.10.0-py35_0
    decorator:           4.0.11-py35_0
    entrypoints:         0.2.2-py35_0
    icu:                 57.1-vc14_0        [vc14]
    ipykernel:           4.5.2-py35_0
    ipython:             5.1.0-py35_0
    ipython_genutils:    0.1.0-py35_0
    ipywidgets:          5.2.2-py35_1
    jinja2:              2.9.4-py35_0
    jsonschema:          2.5.1-py35_0
    jupyter:             1.0.0-py35_3
    jupyter_client:      4.4.0-py35_0
    jupyter_console:     5.0.0-py35_0
    jupyter_core:        4.2.1-py35_0
    markupsafe:          0.23-py35_2
    matplotlib:          2.0.0-np111py35_0
    mistune:             0.7.3-py35_0
    nbconvert:           4.2.0-py35_0
    nbformat:            4.2.0-py35_0
    notebook:            4.3.1-py35_1
    openssl:             1.0.2k-vc14_0      [vc14]
    path.py:             10.0-py35_0
    pickleshare:         0.7.4-py35_0
    prompt_toolkit:      1.0.9-py35_0
    pygments:            2.1.3-py35_0
    pyparsing:           2.1.4-py35_0
    pyqt:                5.6.0-py35_2
    python-dateutil:     2.6.0-py35_0
    pytz:                2016.10-py35_0
    pyzmq:               16.0.2-py35_0
    qt:                  5.6.2-vc14_3       [vc14]
    qtconsole:           4.2.1-py35_2
    scipy:               0.18.1-np111py35_1
    simplegeneric:       0.8.1-py35_1
    sip:                 4.18-py35_0
    six:                 1.10.0-py35_0
    tk:                  8.5.18-vc14_0      [vc14]
    tornado:             4.4.2-py35_0
    traitlets:           4.3.1-py35_0
    wcwidth:             0.1.7-py35_0
    widgetsnbextension:  1.2.6-py35_0
    win_unicode_console: 0.5-py35_0

Proceed ([y]/n)? y

openssl-1.0.2k 100% |###############################| Time: 0:00:02   2.35 MB/s
decorator-4.0. 100% |###############################| Time: 0:00:00 928.85 kB/s
path.py-10.0-p 100% |###############################| Time: 0:00:00   3.24 MB/s
pytz-2016.10-p 100% |###############################| Time: 0:00:00   2.29 MB/s
pyzmq-16.0.2-p 100% |###############################| Time: 0:00:00   2.44 MB/s
jinja2-2.9.4-p 100% |###############################| Time: 0:00:00   2.63 MB/s
prompt_toolkit 100% |###############################| Time: 0:00:00   2.65 MB/s
python-dateuti 100% |###############################| Time: 0:00:00   2.53 MB/s
qt-5.6.2-vc14_ 100% |###############################| Time: 0:00:24   2.39 MB/s
scipy-0.18.1-n 100% |###############################| Time: 0:00:05   2.40 MB/s
jupyter_core-4 100% |###############################| Time: 0:00:00   2.32 MB/s
pyqt-5.6.0-py3 100% |###############################| Time: 0:00:01   2.40 MB/s
matplotlib-2.0 100% |###############################| Time: 0:00:03   2.40 MB/s
nbformat-4.2.0 100% |###############################| Time: 0:00:00   2.74 MB/s
ipykernel-4.5. 100% |###############################| Time: 0:00:00   2.82 MB/s
notebook-4.3.1 100% |###############################| Time: 0:00:02   2.41 MB/s
ipywidgets-5.2 100% |###############################| Time: 0:00:00   4.25 MB/s

(pyOCV) C:\Users\franz>
```
