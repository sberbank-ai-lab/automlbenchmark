OpenML AutoML Benchmark (https://github.com/openml/automlbenchmark)

Full benchmark process was executed in docker mode on cloud server under OS Ubuntu 18.04 with HDD and Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz. 
Docker provides ways to control how much memory, or CPU a container can use, so each container was executed with resources limits specified in OpenML Benchmark configuration. 

<p align="center">
    <img src="https://github.com/sberbank-ai-lab/automlbenchmark/blob/lightautoml/reports_with_lightautoml/results.jpg"  width=1000>
    <br>
</p>

<p align="center">
    <img src="https://github.com/sberbank-ai-lab/automlbenchmark/blob/lightautoml/reports_with_lightautoml/AutoML_results_on_OpenML_datasets.png"  width=1000>
    <br>
</p>


Results: `./reports_with_lightautoml/reports.ipynb`

All docker images used in benchmark is available here:
https://hub.docker.com/u/sberailab/

