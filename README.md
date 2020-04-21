# General Info
This repository provides small code snippets to identify challenges with various operating systems using Python's
multiprocessing and pathos library.

The goal is to identify where and when the code works and if it may work differently on different computers with the 
same OS.

Please run the codes and add your results to the discussion or if you want to give pull requests a try update the readme
and do a pull request. 

## Results Table
|                  | Windows |  Windows Linux |Linux| MAC | Repl.it |Ideone.com | [Colab](https://colab.research.google.com/drive/1kE--nW2wKvA9i13arUV5zHAcs4Ht9XTc "Colab Notebook")<sup>1</sup> | Windows<sup>2</sup> |
|:-----------------|:--------|:-------------:|:---:|:---:|:-------:|-----------|-----------|-----------|
|**Multiprocessing_1** |Hangs    |(Debian) Hangs |     |     | Works   | Fails     | Works     | Works     |
|**Multiprocessing_2** |Works    |(Debian) Works |     |     | Works   | Works     | Works     | Works     |
|**Multiprocessing_3** |Works    |(Debian) Works |     |     | Works   | Works     | Works     | Works     |
|**Multiprocessing_4** |Hangs/Fails| (Debian) Hangs|   |   |  Works   | Fails     | Works     | Works     |
|**Multiprocessing_5** |Hangs   | (Debian) Hangs|   |      | Works |  Fails | Works     | Works     |

*Notes:* Below is a list of versions for the respective OS and the required additional software  
**<sup>1</sup>**: Google Colab, Ubuntu v18.04.3 LTS, Python v3.6.9, Pathos v0.2.5  
**<sup>2</sup>**: Microsoft Windows v10.0.17763.1158, Anaconda command line client v1.7.2, Python v3.7.3, Pathos v0.2.5  

## Expected Outputs
The below table lists the expected results of each script
| Script | Output |
|:-----------------|:--------|
|**Multiprocessing_1** |`...` </br>`[1, 64, 2187, 65536]` | 
|**Multiprocessing_2** | `1`</br>` 256`</br>`19683`| 
|**Multiprocessing_3** | `[1, 256, 19683]` | 
|**Multiprocessing_4** | `[1, 256, 19683]` | 
|**Multiprocessing_5** | `start`</br>`1`</br>`256`</br>`19683`| 

## Commands you can use to determine your version info
**Python:** `python -v` (from command line interface or use as a bash command)  
**Linux:** `cat /etc/os-release` (from command line or use as a bash command)  
**Windows:** `ver` (from command line)  
**Pathos:** Run the following python code in your environment
```python
import pathos
print("pathos imported as Version: ",pathos.__version__)
```

