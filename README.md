# Computer_Vision_Domain_Adaptation
MNIST to SVHN Domain Adaptation for Computer Vision

## Getting Started

### Dependencies

Refer to `requirements.txt` for a full list of dependencies.

### Installing

#### For Users:

* To install our project: 

```
git clone https://github.com/olivier-lapabe/Computer_Vision_Domain_Adaptation
cd Computer_Vision_Domain_Adaptation
pip install .
```

#### For Developers/Contributors:

If you're planning to contribute or test the latest changes, you should first set up a virtual environment and then install the package in "editable" mode. This allows any changes you make to the source files to immediately affect the installed package without requiring a reinstall.

* Clone the repository:

```
git clone https://github.com/olivier-lapabe/Computer_Vision_Domain_Adaptation
cd Computer_Vision_Domain_Adaptation
```

* Set up a virtual environment:

```
python3 -m venv dadapt_env
source dadapt_env/bin/activate   # On Windows, use: dadapt_env\Scripts\activate
```

* Install the required dependencies:

```
pip install -r requirements.txt   # For mac users, use: pip install -r requirements_mac.txt
```

* Install the project in editable mode:

```
pip install -e . 
```

### Executing program

Launch the different model Runners:  
```
python3 bin/CyCADARunner.py
python3 bin/DiscrepancyClassifierRunner.py
python3 bin/PseudoLabellingRunner.py
```


## Version History

* **1.0.0** - Initial release