This energy report format is published under Creative Commons 4.0.
https://creativecommons.org/licenses/by/4.0/

# Report the electricity consumption of your models

## 1. Goal

The goal described by this document is to setup a simple and resilient digital ecosystem, so as to gather homogeneous, well-formated measures of energy consumption of a machine learning task, from the electricty consumption of a processor during a single inference to the finetuning of a model on a large server.

The purpose thereby followed is to build a large, open, database of energy consumption of AI tasks depending on data nature, algorithms, hardware, etc., in order to improve energy efficiency approaches based on empiric knowledge. 

More concretely, this empiric knowledge may be used in applied research to improve frugal approaches in AI models grid search and avoid energy-intensive tasks.

## 2. Energy Measurement

It is assumed that the measurement of an atomic task can be achieved by one or several means among the following.

### Software-based 
CodeCarbon
Carbon AI
PyJoules
PowerGadget
EcoLogits
...

### Hardware-based 
Direct physical measure with a Watt-meter.

In the report schema, you can provide as many measure_schemas as you wish. Please note that the aim is not to mix measurements from a whole series of tasks in a single report, but to allow you to compare measurements for the same task that may be taken from different tools (several software and/or hardware tools at the same time).

## 3. What to describe ? 

The datamodel is complex and allows to describe a lot of different configurations : for example, you can provide provide the description of as many dataset or hardware components that you want. However, it is important to bear in mind that the more precise the report, the more usefull the information will be. For example, if you simply say that you performed 10000 inferences on different images of various sizes, using a supervised algorithm, that you were on the cloud and that you consumed x kWh, this will not allow you to deduce much information about the cost of an inference on a specific piece of data on a specific hardware. It is better to produce reports on a finer scale: I've run this recognition algorithm, I've measured the power consumption of the cpu and gpu of this model, I have made an inference about an image of this certain size...    

Read the schema carefully: some attributes are enumerations with detailed possible values, others are free fields. When this is the case, please describe things in a unique and unambiguous way to facilitate processing. We ask you to use the [snake_case](https://www.logilax.com/snake-case/) notation (e.g don't write "Random forest" or "RandomForest" but "random_forest" instead).

## 4. Quick preview of the fields

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

