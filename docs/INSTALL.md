# INSTALL Guide For PEALS
Time-stamp: <2023-03-21 16:35:26 Keren Zhou>

Please check the following instructions to complete your installation.

## Prerequisites

### Python3

PEALS requires Python3. We have tested PEALS in Python3.8. 

### NumPy

PEALS requires [Numpy](http://www.scipy.org/Download) (>=1.21.2).

### NumPy

PEALS requires [scipy](http://www.scipy.org/Download) (>=1.7.1).

### CSAPS

PEALS requires [CSAPS](https://csaps.readthedocs.io/en/latest/) (>=1.1.0).

### findpeaks

PEALS requires [findpeaks](https://erdogant.github.io/findpeaks/pages/html/Installation.html#installation) (>=2.4.6).

## Install through PyPI

The easiest way to install PEALS is through PyPI system. Get `pip` if
it's not available in your system.

```bash
pip3 install peals --user

```

## Install from source

There are 2 ways to install PEALS from source.

The 1st way is using `pip` command.

```bash
git clone https://github.com/kerenzhou062/PEALS.git

cd PEALS

pip3 install . --user

```

The 2nd way is using `setup.py`.

```bash
git clone https://github.com/kerenzhou062/PEALS.git

cd PEALS

python3 setup.py install --user

```

### PYTHONPATH

To set up your `PYTHONPATH` environment variable, you'll need to add
the value `PREFIX/lib/pythonX.Y/site-packages` to your existing
`PYTHONPATH`. In this value, X.Y stands for the major–minor version of
Python you are using (such as 3.8; you can find this with
`sys.version[:3]` from a Python command line). `PREFIX` is the install
prefix where you installed PEALS. If you did not specify a prefix on
the command line, PEALS will be installed using Python's sys.prefix
value.

On Linux, using bash, I include the new value in my `PYTHONPATH` by
adding this line to my `~/.bashrc`::

 `$ export
 PYTHONPATH=/home/kzhou/lib/python3.8/site-packages:$PYTHONPATH`

### PATH

Please be sure that the following software or R packages have been properly installed and are available in `PATH` variable.

 * [bedTools (>=2.30.0)](https://bedtools.readthedocs.io/en/latest/content/installation.html)
 * [samtools (>=1.14)](http://www.htslib.org/download/)
 * [featureCounts (>=2.0.2)](https://subread.sourceforge.net/featureCounts.html)
 * [DESeq2 (>=1.32.0)](https://bioconductor.org/packages/release/bioc/html/DESeq2.html)
 * [ggplot2 (>=3.4.1)](https://ggplot2.tidyverse.org/index.html)
 * [ashr (>=2.2.54)](https://github.com/stephens999/ashr)
 * [apeglm (>=1.14.0)](https://bioconductor.org/packages/release/bioc/html/apeglm.html)
