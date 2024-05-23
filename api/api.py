
# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python


class Algorithm:

    """the case-sensitive common name of the algorithm
    """
    key:str = None

    """the common name of the software framework implementing the algorithm, if any
    """
    framework:str = None

    """the version of the software framework implementing the algorithm, if any
    """
    frameworkversion:str = None

    """the full class path of the algorithm within the framework, with elements separated by dots
    """
    classpath:str = None

    hyperparameters:any = None

    """the quality of the information you provided, 3 possibilities : high (percentage error +/-1%), medium (percentage error +/-10%), low (percentage error +/-20%)
    """
    quality:str = None

    def to_dict(self):
        return {
            'key': self.key,
            'framework': self.framework,
            'frameworkversion': self.frameworkversion,
            'classpath': self.classpath,
            'hyperparameters': self.hyperparameters,
            'quality': self.quality
        }
    # end of class Algorithm
    

class Dataset:

    """the nature of the data, purposedly limited to basic types
    """
    key:str = None

    """the file type of the dataset
    """
    filetype:str = None

    """the size of the dataset
    """
    volume:int = None

    """the unit of the size of the dataset
    """
    volumeunit:str = None

    """the kind of source of the dataset
    """
    source:str = None

    """the URI of the dataset if available
    """
    sourceuri:str = None

    """the owner of the dataset if available
    """
    owner:str = None

    """the number of items in the dataset
    """
    items:int = None

    """the shape of each dataset item (for instance, an array of size 3, for greyscale images)
    """
    shape:list[int] = None

    """the quality of the information you provided, 3 possibilities : high (percentage error +/-1%), medium (percentage error +/-10%), low (percentage error +/-20%)
    """
    quality:str = None

    def to_dict(self):
        return {
            'key': self.key,
            'filetype': self.filetype,
            'volume': self.volume,
            'volumeunit': self.volumeunit,
            'source': self.source,
            'sourceuri': self.sourceuri,
            'owner': self.owner,
            'items': self.items,
            'shape': self.shape,
            'quality': self.quality
        }
    # end of class Dataset
    

class Hardware:

    """the type of this subsystem part of your infrastructure, example: cpu, gpu
    """
    key:str = None

    """the number of this item in your infrastructure
    """
    nb_component:int = None

    """the name of the manufacturer, example: NVIDIA
    """
    manufacturer:str = None

    """the family of this component, example: GeForce
    """
    family:str = None

    """the series of this component, example: RTX 4080
    """
    series:str = None

    """the percentage of use of this component
    """
    share:float = None

    """the quality of the information you provided, 3 possibilities : high (percentage error +/-1%), medium (percentage error +/-10%), low (percentage error +/-20%)
    """
    quality:str = None

    def to_dict(self):
        return {
            'key': self.key,
            'nb_component': self.nb_component,
            'manufacturer': self.manufacturer,
            'family': self.family,
            'series': self.series,
            'share': self.share,
            'quality': self.quality
        }
    # end of class Hardware
    

class Measure:

    """the method used to perform the energy or FLOPS measure, example: CodeCarbon, CarbonAI, flops-compute, Wattmeter...
    """
    key:str = None

    """the builder of the measuring tool, noticeably used for a device (if so, $$key value should be set to $Wattmeter)
    """
    manufacturer:str = None

    """the version of the measuring tool, if any
    """
    version:str = None

    """the method used to track the consumption of the CPU, example : constant, RAPL...
    """
    cpu_tracking_mode:str = None

    """the method used to track the consumption of the GPU, example : constant, nvml...
    """
    gpu_tracking_mode:str = None

    """if you practice inference throw an API, do you estimate the consumption only of the AI server (because the AI is deployed on your own server and you have access to the measure or because you estimated it with a tool like EcoLogits), only of the testingAI_server side or from both side ?
    """
    server_side_inference:str = None

    """the unit of the power consumption measure of the computing task, example: Wh, kWh, Joule, FLOPS...
    """
    unit:str = None

    """the power consumed during your calibration measure if any (to isolate the inital consumption of your machine)
    """
    powercalibrationmeasure:float = None

    """the duration of your calibration if any (in seconds)
    """
    durationsecondscalibrationmeasure:float = None

    """the power consumption measure of the computing task
    """
    powerconsumption:float = None

    """the quality of the information you provided, 3 possibilities : high (percentage error +/-1%), medium (percentage error +/-10%), low (percentage error +/-20%)
    """
    quality:str = None

    def to_dict(self):
        return {
            'key': self.key,
            'manufacturer': self.manufacturer,
            'version': self.version,
            'cpu_tracking_mode': self.cpu_tracking_mode,
            'gpu_tracking_mode': self.gpu_tracking_mode,
            'server_side_inference': self.server_side_inference,
            'unit': self.unit,
            'powercalibrationmeasure': self.powercalibrationmeasure,
            'durationsecondscalibrationmeasure': self.durationsecondscalibrationmeasure,
            'powerconsumption': self.powerconsumption,
            'quality': self.quality
        }
    # end of class Measure
    

class Report_Header_Publisher:

    """name of the organization
    """
    name:str = None

    """name of the publishing department within the organization
    """
    division:str = None

    """name of the publishing project within the organization
    """
    projectname:str = None

    """ the confidentiality of the report
    """
    confidentialitylevel:str = None

    """the cryptographic public key to check the identity of the publishing organization
    """
    publickey:str = None

    def to_dict(self):
        return {
            'name': self.name,
            'division': self.division,
            'projectname': self.projectname,
            'confidentialitylevel': self.confidentialitylevel,
            'publickey': self.publickey
        }
    # end of class Report_Header_Publisher
    

class Report_Header:

    """the type of licensing applicable for the sharing of the report
    """
    licensing:str = None

    """the version of the specification of this set of schemas defining the report's fields
    """
    formatversion:str = None

    """the URI of the present specification of this set of schemas
    """
    formatversionspecificationuri:str = None

    """the unique identifier of this report, preferably as a uuid4 string
    """
    reportid:str = None

    """the publishing date of this report in format YYYY-MM-DD HH:MM:SS
    """
    reportdatetime:str = None

    """
    """
    reportstatus:str = None

    """the details about the publishing organization who produced the report
    """
    publisher:Report_Header_Publisher = None

    def to_dict(self):
        return {
            'licensing': self.licensing,
            'formatversion': self.formatversion,
            'formatversionspecificationuri': self.formatversionspecificationuri,
            'reportid': self.reportid,
            'reportdatetime': self.reportdatetime,
            'reportstatus': self.reportstatus,
            'publisher': self.publisher.to_dict()
        }
    # end of class Report_Header
    

class Report_Task:

    """type of the computing task of machine learning, example : preprocessing, supervised, unsupervised, unsupervised, postprocessing, semisupervised,postprocessing ...
    """
    tasktype:str = None

    """stage of the task if any, example: training, finetuning, reinforcement, inference...
    """
    taskstage:str = None

    """the main algorithmic approaches used by the computing task
    """
    algorithms:list[Algorithm] = None

    """the measured accuracy of your model (between 0 and 1)
    """
    measuredaccuracy:float = None

    """if you didn't measure the accuracy of your model in concrete percentages, you can give an assessment of the precision between: VERY POOR, POOR, AVERAGE, GOOD, VERY GOOD
    """
    estimatedaccuracy:str = None

    def to_dict(self):
        return {
            'tasktype': self.tasktype,
            'taskstage': self.taskstage,
            'algorithms': [ elt.to_dict() for elt in self.algorithms ],
            'measuredaccuracy': self.measuredaccuracy,
            'estimatedaccuracy': self.estimatedaccuracy
        }
    # end of class Report_Task
    

class Report_System:

    """name of the operating system
    """
    os:str = None

    """distribution of the operating system
    """
    distribution:str = None

    """distribution's version of the operating system
    """
    distroversion:str = None

    def to_dict(self):
        return {
            'os': self.os,
            'distribution': self.distribution,
            'distroversion': self.distroversion
        }
    # end of class Report_System
    

class Report_Software:

    """name of the programming language used, example : C, Java, Julia, Pyhton...
    """
    language:str = None

    """version of the programming language used
    """
    version:str = None

    def to_dict(self):
        return {
            'language': self.language,
            'version': self.version
        }
    # end of class Report_Software
    

class Report_Region:

    country:str = None

    latitude:float = None

    longitude:float = None

    location:str = None

    powersuppliertype:str = None

    powersource:str = None

    powersourcecarbonintensityunit:str = None

    powersourcecarbonintensity:float = None

    def to_dict(self):
        return {
            'country': self.country,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'location': self.location,
            'powersuppliertype': self.powersuppliertype,
            'powersource': self.powersource,
            'powersourcecarbonintensityunit': self.powersourcecarbonintensityunit,
            'powersourcecarbonintensity': self.powersourcecarbonintensity
        }
    # end of class Report_Region
    

class Report_Hash:

    """the hash function to apply first to the JSON report
    """
    hashalgorithm:str = None

    """the public key function to apply to the hash
    """
    cryptographicalgorithm:str = None

    """encrypted value of the hash value of the minimized JSON instance string, using the publisher's private key and including all root properties except the $hash property itself
    """
    value:str = None

    def to_dict(self):
        return {
            'hashalgorithm': self.hashalgorithm,
            'cryptographicalgorithm': self.cryptographicalgorithm,
            'value': self.value
        }
    # end of class Report_Hash
    

class Report:

    """information about the source of the report and publishing organization's details
    """
    header:Report_Header = None

    """the list of datasets processed by the computing task
    """
    datasets:list[Dataset] = None

    """the software and/or hardware measures of the computing task
    """
    measures:list[Measure] = None

    """the nature of the task being measured
    """
    task:Report_Task = None

    """system information of the infrastructure on which is run the computing task
    """
    system:Report_System = None

    """programming language information of the computing task
    """
    software:Report_Software = None

    """the infrastructure on which is performed the computing task
    """
    infrastructure:any = None

    """geographic region of the infrastructure
    """
    region:Report_Region = None

    hash:Report_Hash = None

    def to_dict(self):
        return {
            'header': self.header.to_dict(),
            'datasets': [ elt.to_dict() for elt in self.datasets ],
            'measures': [ elt.to_dict() for elt in self.measures ],
            'task': self.task.to_dict(),
            'system': self.system.to_dict(),
            'software': self.software.to_dict(),
            'infrastructure': self.infrastructure,
            'region': self.region.to_dict(),
            'hash': self.hash.to_dict()
        }
    # end of class Report
    
