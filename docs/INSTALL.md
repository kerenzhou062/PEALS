# PEALS: Peak-based Enhancement Analysis PipeLine for MeRIP-Seq

Latest Release:
* Github: [![Github Release](https://img.shields.io/github/v/release/peals-project/MACS)](https://github.com/kerenzhou062/PEALS/releases)
* PyPI: [![PyPI Release](https://img.shields.io/pypi/v/peals.svg) ![PyPI Python Version](https://img.shields.io/pypi/pyversions/peals) ![PyPI Format](https://img.shields.io/pypi/format/peals)](https://pypi.org/project/peals/)

## Introduction

MeRIP-seq stands for methylated RNA immunoprecipitation sequencing, which is the most popular method for detection of post-transcriptional RNA modifications. Here, we presented
the **P**-based **E**nhancement **A**nalysis Pipe**L**ine for MeRIP-**S**eq (PEALS), for
identifying enriched methylation regions. PEALS 

## Install

The common way to install MACS is through
[PYPI](https://pypi.org/project/peals/)) or
[INSTALL](./docs/INSTALL.md) document for detail.

peals has been tested in CI for every push and PR in the following
architectures:

 * x86_64
 * aarch64
 * armv7
 * ppc64le
 * s390x 

## Usage

Example for regular peak calling on TF ChIP-seq:

`peals callpeak -t ChIP.bam -c Control.bam -f BAM -g hs -n test -B -q 0.01`

Example for broad peak calling on Histone Mark ChIP-seq:

`peals callpeak -t ChIP.bam -c Control.bam --broad -g hs --broad-cutoff 0.1`

Example for peak calling on ATAC-seq (paired-end mode):

`peals callpeak -f BAMPE -t ATAC.bam -g hs -n test -B -q 0.01`

There are currently twelve functions available in MAC3 serving as
sub-commands. Please click on the link to see the detail description
of the subcommands.

Subcommand | Description
-----------|----------
[`callpeak`](./docs/callpeak.md) | Main peals Function to call peaks from alignment results.
[`diffpeak`](./docs/diff.md) | Call peaks from bedGraph output.

For advanced usage, for example, to run `peals` in a modular way,
please read the [advanced usage](./docs/advanced_usage.md). There is a
[Q&A](./docs/qa.md) document where we collected some common questions
from users.

## Contribute

Please read our [CODE OF CONDUCT](./CODE_OF_CONDUCT.md) and
[How to contribute](./CONTRIBUTING.md) documents. If you have any
questions, suggestion/ideas, or just want to have conversions with
developers and other users in the community, we recommand you use the
[MACS Discussions](https://github.com/peals-project/MACS/discussions)
instead of posting to our
[Issues](https://github.com/peals-project/MACS/issues) page.

## Ackowledgement

peals project is sponsored by
[CZI EOSS](https://chanzuckerberg.com/eoss/). And we particularly want
to thank the user community for their supports, feedbacks and
contributions over the years.

## Other useful links

 * [Cistrome](http://cistrome.org/)
 * [bedTools](http://code.google.com/p/bedtools/)
 * [UCSC toolkits](http://hgdownload.cse.ucsc.edu/admin/exe/)
 * [deepTools](https://github.com/deeptools/deepTools/)


