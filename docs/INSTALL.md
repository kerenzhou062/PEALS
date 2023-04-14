# INSTALL Guide For PEALS
Time-stamp: <2023-03-21 16:35:26 Keren Zhou>

Please check the following instructions to complete your installation.

## Prerequisites

PEALS is developed under `python3` environment and has been tested in `python 3.8` and `Linux` with kernel-version `#1 SMP Mon Dec 4 23:52:40 UTC 2017`.

Please be sure that the following software or R packages have been properly installed and are available in `PATH` variable or can be directly loaded by `R`.

Software:
 * [bedTools (>=2.30.0)](https://bedtools.readthedocs.io/en/latest/content/installation.html)
 * [samtools (>=1.14)](http://www.htslib.org/download/)
 * [featureCounts (>=2.0.2)](https://subread.sourceforge.net/featureCounts.html)

R packages:
 * [getopt (>=1.20.3)](https://bioconductor.org/packages/release/bioc/html/DESeq2.html)
 * [DESeq2 (>=1.32.0)](https://bioconductor.org/packages/release/bioc/html/DESeq2.html)
 * [ggplot2 (>=3.4.1)](https://ggplot2.tidyverse.org/index.html)
 * [ashr (>=2.2.54)](https://github.com/stephens999/ashr)
 * [apeglm (>=1.14.0)](https://bioconductor.org/packages/release/bioc/html/apeglm.html)
 * [glmGamPoi (>=1.4.0)](https://bioconductor.org/packages/release/bioc/html/glmGamPoi.html)

## 3 ways to install PEALS

### Install through PyPI

The easiest way to install PEALS is through PyPI system. Get `pip` if
it's not available in your system.

```bash
pip3 install peals --user

```

### Install from source using `pip`

```bash
git clone https://github.com/kerenzhou062/PEALS.git
cd PEALS
pip3 install . --user

```

### Install from source using `setup.py`

```bash
git clone https://github.com/kerenzhou062/PEALS.git
cd PEALS
python3 setup.py install --user

```

## PYTHONPATH
Usually, you don't need to care about the `PYTHONPATH` enrivonment 
unless you install PEALS to a specific path.

To set up your `PYTHONPATH` environment variable, you'll need to add
the value `PREFIX/lib/pythonX.Y/site-packages` to your existing
`PYTHONPATH`. In this value, X.Y stands for the major–minor version of
Python you are using (such as 3.8; you can find this with
`sys.version[:3]` from a Python command line). `PREFIX` is the install
prefix where you installed PEALS.

If you did not specify a prefix on
the command line, PEALS will be installed using Python's sys.prefix
value.

On Linux, using bash, I include the new value in my `PYTHONPATH` by
adding this line to my `~/.bashrc`:

 `$ export
 PYTHONPATH=/home/kzhou/lib/python3.8/site-packages:$PYTHONPATH`
