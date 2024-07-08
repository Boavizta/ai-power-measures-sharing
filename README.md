This energy report format is published under Creative Commons 4.0.
https://creativecommons.org/licenses/by/4.0/

# CO2 Reporting

## 1. Goal

The goal described by this document is to setup a simple and resilient digital ecosystem, so as to gather homogeneous, well-formated measures of energy consumption from an atomic software task in general and Machine Learning / Deep Learning / AI / GenAI tasks in particular.

The purpose thereby followed is to build a large, open, database of energy consumption of IT / AI tasks depending on data nature, algorithms, hardware, etc., in order to improve energy efficiency approaches based on empiric knowledge. 

More concretely, this empiric knowledge may be used in applied research to improve frugal approaches in AI models grid search and avoid energy-intensive tasks.

## 2. Energy Measurement

It is assumed that the measurement of an atomic task can be achieved by one or several means among the following.

### Software-based 
CodeCarbon
Carbon AI
PyJoules
PowerGadget
...

### Hardware-based 
Direct physical measure with a Watt-meter.


## 3. Knowledge Elements

Elements that are likely to take place as pieces of context in each knowledge item, must be at the same time meaningful and minimal. Meaningful, in order to learn valuable patterns from data gathered. Minimal, in order to keep the monitoring task as light as possible.
- Data type (mandatory): basically, the nature of the data (text/csv, audio, image, etc.)
- Data dimensions (mandatory): the shape of the dataset, the first figure being the number of items
- Task type (mandatory): noticeably in machine learning, the nature of the process being achieved (clustering, classification, reinforcement, etc.)
- Measurement method (mandatory): software-based or hardware-based 
- Measurement solution (mandatory): for software versions, the library used ; for hardware, the watt-meter manufacturer
- Measurement unit (mandatory)
- The measure itself (mandatory)!
- Algorithm(s) (conditional): if the task is a learning task, what kind of algorithm is used
- Hyperparameters (conditional and optional): if the task is a learning task, what hyperparameters were used, with which values
- Hardware environment (recommended): What kind of host (container, VM, dedicated server), and electronic chips (GPU, CPU, RAM) are used for the measure
- System environment (recommended): What OS, version kernel, etc.
- Energy source (recommended): depending on the location or the private energy plants, permits to extrapolate the carbon emissions induced by the energy consumption
- Publisher (recommended) : information about the identity of the publisher with various levels of anonymization


## 4. State-of-the-art 

### On ML tasks categorization

- https://www.researchgate.net/publication/320609700_A_Review_on_Machine_Learning_Algorithms_Tasks_and_Applications
- https://vitalflux.com/7-common-machine-learning-tasks-related-methods/
- https://pythonprogramminglanguage.com/machine-learning-tasks/
- https://accessibleai.dev/post/coremltasks/
- https://www.c-sharpcorner.com/article/a-quick-overview-of-machine-learning-tasks/

### On ML description frameworks

These could typically inspire the ground for a format of reporting.
- https://hdsr.mitpress.mit.edu/pub/zkib7xth/release/2
- https://www.iso.org/standard/74438.html
- https://standards.ieee.org/ieee/3123/10744/


## 5. Format principles

The JSON structure is proposed for the sake of clarity for human users, and fields extensibility.
Since flattening an object containing arrays leads to a naming issues (array items have no label, and array index is not guaranteed between instances), a specific flattening scheme is proposed for arrays, thanks to the reserved property label "$$key".
*If* an array is present, then all array items *must* contain a property "$$key". Otherwise, a flattening exception is raised.


## 6. Architecture Scenarii

The differences among possible architecture scenarii are bound to several considerations.
- Simplicity: The architecture must be compatible with the way measures are produced. For instance, in the case of software libraries such as CodeCarbon, some contextual information can be added in the output produced. Should such field be used for arbitrarily long payload ? Probably not.
- Integrity: To expect large public datasets of energy monitoring figures in-the-field, individual data of corporations / projects / teams must describe things in a unique, non-ambiguous, terminology. For instance, the ‘Random Forest’ algorithm should not be described ‘randomforest’ in one case, ‘Random_Forest’ in another, ‘rf’ in a third one. Homogeneity of descriptors must be enforced.
- Privacy: Energy monitoring data publishers must be in the conditions to keep the desired level of privacy concerning the data they publish
- Trust: The data published, especially on a public database, must own the appropriate level of trust


## 7. Tests

Run tests as follows:
```
python test.py
```


## 8. API generation from JSON schemas

The file api/api.py is generated from the JSON schemas within folder /model. When they come to evolve, please refresh the API with the following command:
```
python generate_api.py
```

## 9. Examples and schema json validator

The validate-schema.py script allows you to validate that the json you have created correctly follows the schema we have defined (in the folder /model). 