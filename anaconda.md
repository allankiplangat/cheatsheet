## Anaconda

#### Using Conda (package manager)

- Creating a conda environment ```conda create -n env_name python=3```
- Enter the environment ```source activate env_name```
- Deactivating the environment ```source deactivate```
- List packages installed ```conda env list```
- installing packages ```conda install package_name```
- Uninstalling packages ```conda remove package_name```
- Updating packages ```conda update package_name```
- searching packages ```conda search *search_term*``` or ```conda search '*beautifulsoup*```
- save packages into a YAML file ```conda env export > environment.yaml```
- creating sn environment from an environment file ```conda env create -f environment.yaml```
- Removing environments ```conda env remove -n env_name```
- Freezing packages versions for sharing ```pip freeze > requirements.txt```