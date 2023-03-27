# Call peaks

This is the main function in PEALS. It can be invoked by `PEALS
callpeak` . If you type this command with `-h`, you will see a full
description of command-line options. Here we only list the essentials.

## Input Options

### `-m`/`--matrix FILENAME`

The tab-separated matrix contain all information of input samples. Header format:`label,library,condition,sample,replicate,bam,binary,...`.

Please chek an example [sample matrix](https://github.com/kerenzhou062/PEALS/blob/main/example/peals.diffpeak.sample.txt) here as reference.

### `-i`/`--input DIRECTORY`

The input directory contains all `*.bam` and `*.bai` files that listed in your input `--matrix <sample matrix>`.

### `--type`

The assumed type of RNA transcripts in input MeRIP library (mature: only contain mature transcripts; primary: only contain primary transcripts; mixture: contain both mature and primay transcripts).



## Output Options

### `-o`/`--output DIRECTORY`

All output files will be written to this directory.

### `-T`/`--temp DIRECTORY`

If specified, all temporary files will be written to this directory. Default is the same with --output.

### `-P`/`--prefix STRING`

The prefix of all output files.

### `--nobwtrack BOOL`

If specified, will not output bigwig signal tracks which can be loaded in IGV. Default is gernerate bw files.

### `--keep-temp BOOL`

Keep the temporary files. Default is delete all temp files.



## Library Options

### `-l`/`--library INT`

Library protocols of input bam files. For details, 0 (unstranded), 1 (stranded or fr-secondstrand) and 2 (reversely stranded or fr-firstrand).

### `--estlib-size STRING`

How to estimate the library size when calling peaks and scaled bigwig outputs. Choises would be one of `primary`, `mapped`, or `primary_mapped` that in the output of `samtools flagstats`.

### `--extsize INT`

Extend reads in 5'->3' direction to # bp (not recommend to be set when handling the paired-end data). Would not recommend if the input is `PARIED-END` data. Default is `0`.

When `0` is set, it will directly use the input reads without any extension.

### `--pairend BOOL`

If speficied, all input bam files will be treated as `PAIRED-END` data. Default is `False`.



## Normalization Options

### `--exp-method STRING`

The method to estimate gene expression (mainly used for filter non-expressed genes). Choices would be be one of `count`, `TPM`, or `FPKM`. Default is `count`.

If the `count` is set, then the `TPM` will be used to estimate the gene expression after filtering the non-expressed genes.

### `--estpeak-sizefactor STRING`

How to normalize reads count of peak candidates for normalization before applying DESEq2 model.

### `--bw-scale STRING`

How to handle the signal track output (in bigwig format). Choices would be one of  `raw`, `rpm`, `paired`, or `whole`. Default is `rpm`.

### `--estip-eff STRING`

How estimate the IP efficiency factors of control and treated conditions. Choices would be one of  `across` or `within`. Default is `within`.

If 'within' is specified, it will estimate IP efficiency factors within each condition, repspectively. If 'across' is specified, will estimate IP efficiency factors across 2 conditions (may introduce over-estimation).



## BAM Options

### `--scale-sample STRING`

The larger dataset will be scaled towards the smaller or larger dataset. Choices would be one of `to_small`, `to_large`, or `raw`. Default is to `to_small`.

### `--sortbam BOOL`

Sort bams before passing to featureCounts. Default is `False`.

### `--no-fraction BOOL`

Do not count the multiple-aligned reads with fraction. Default is `False`.

### `--frac-overlap FLOAT`

Only overlap the fraction of reads larger than this value will count to peak. Default is `0`.

When `0` is set, it wil count the reads to the peaks with even has only 1bp overlaps.

### `--ignore-dup BOOL`

If specified, will ignore PCR duplicate reads flagged by `1024`. Default is `False`.

### `--exp-cutoff INT`

The cutoff for an expressed transcript. Only call peaks on expressed transcripts. Default is `1`.



## Genome Options

### `--gsize FILENAME`

The file contain the sizes of chromosomes. Can be downloaded from UCSC genome browser (e.g. hg38.chrom.sizes).

### `--gff FILENAME`

The gene annotation file. The chromosomes naming should be consistent with --gsize and input bam files.

### `--gff-type STRING`

The format of input --gff. Choices would be one of `GTF` or `GFF3`. Default is `GTF`.

### `--gff-source STRING`

The source of gene annotations. Choices would be one of `GENCODE`, `ENSEMBL`, or `other`. Default is `GENCODE`.

### `--identifier STRING`

The identifier used to extract transcript information from annotation file. Default is `gene_id:gene_name:gene_type:transcript_id:transcript_name:transcript_type`.



## Peak Options

### `--split INT`

Split the transcript into subgroups by #bp long (must be >= 5000). Default is `50000`.

### `--span-method STRING`

Method used to further smooth the coverage data on transcript after calling CSAPS model. Choices would be one of `move` or `none`. Default is `move`.

### `--span-loop INT`

How many times that apply the method indicated by '--span-method' after calling CSAPS model. Default is `1`.

I won't suggest you to change this parameter unless you want to perform more smoothing on the coverage data.

### `--complexity-rate FLOAT`

If the complexity of signals in a detected region is lower than this value (eg., high PCR duplicates), then this region will no be considered as a peak candidates. Default is `0.05`.

I won't suggest you to change this value if the PCR duplicates have been removed from input BAMs or the `--ignore-dup` is set.

### `--lookahead INT`

The distance to look ahead from a peak candidate to determine if it is the actual peak (passed to `findpeaks`). Default is `25`.

### `--csaps-p FLOAT`

The constant smooth parameter p (smooth) passed to `csaps()`. Smaller p means more smoothing. Default is `0.005`.

The final parameter p for each split of transcripts would be further nomalized by transcript length.

### `--peak-size INT`

The minimun peak size. Default is the maximum value between 'half of the --extsize' and '35'.

### `--ipratio FLOAT`

Define the candidate peaks within which regions have the ratio of ip/input >= --ipratio. Default is `1.25`.

### `--center FLOAT`

Center the candidate peak region by shearing points of which are less than '--center' of highest coverage. Should be the range [0, 0.5]. Default is `0.25`.

## Model Options

### `--fit-type STRING`

Type of fitting of dispersions to the mean intensity (passed to `DESeq2`). Choices would be one of `parametric`, `local`, `mean`, or `glmGamPoi`. Default is `parametric`.

### `--shrink STRING`

The method used for shrinking the fold change (lfcShrink() in `DESeq2`). Choices would be one of `none`, `apeglm`, or `ashr`. Default is `apeglm`.

### `--test STRING`

The test method for calculating p-value (passed to `DESeq2`). Choices would be one of `Wald`, or `LRT`. Default is `Wald`.

### `--formula STRING`

The design formula passed to DESeq2(). Will overwrite the default formula.



## Filter Options

### `-p/--pval FLOAT`

If specified, only peaks have p-value <= --pval will be recognized significant peaks. Default is `0.05`.

### `--padj FLOAT`

If specified, only peaks have adjusted p-value (FDR) <= --padj will be recognized significant peaks. Default is `0.05`.

### `--padj-method STRING`

The method used to calculate adjusted p-value. Default is `BH`.

### `-f/--fold FLOAT`

If specified, only peaks have fold change (IP/input) (>= fold) will be recognized significant peaks. Default is `2`.

### `-F/--diff-fold FLOAT`

If specified, only peaks have fold change (IP/input) (>= fold or <= 1/fold) will be recognized significantly changed peaks. Default is `1`.

### `--diff-pval FLOAT`

If specified, only peaks have p-value <= --pval will be recognized significanttly changed peaks. Default is `0.05`.

### `--diff-padj FLOAT`

If specified, only peaks have adjusted p-value (FDR) <= --padj will be recognized significantly changed peaks. Default is `1`.



## Output Files

### `*.bed`

The BED output is in standard `BED` format, which can be found at [UCSC genome browser
website](http://genome.ucsc.edu/FAQ/FAQformat#format1).

The value in the `4th` coulmn represents the `log10(p-value)`.

### `*.txt`

The TXT output is in `BED12` + `additional information` format.

### `*.bw`

The BW output is in `BigWig` format, which can be found at [UCSC genome browser
website](http://genome.ucsc.edu/goldenPath/help/bigWig.html).


## `*dispersion.*.pdf`

THese files were used to judge whether the data fits well with dispersion in DESeq2 model.
