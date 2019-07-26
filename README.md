# interface_these_rammouz
Graphical User Interface (GUI) made in python for the MATLAB simulation code of the thesis titled "Optimisation de la gestion d’énergie dans les systèmes embarqués", by RAMMOUZ Ramzy.

## dependecies

- matlab.engine  (requires python 3.6)
- scipy
- tkinter


## how set up the dependencies to run the code

To run the code, you need a machine with Windows, Python 3.6 and MATLAB version 2014b or later.
Also, you will need to have the 3 libraries used by it (_matlab.engine_, _scipy_, and _tkinter_) installed.

For instructions on how to install _matlab.engine_, see:
https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

For instructions on how to install scipy, see:
https://www.scipy.org/install.html

Personally, for scipy I would recommend installing Anaconda, a free distribution of Python with scientific packages:
https://www.anaconda.com/distribution/

There is no need to install tkinter because it is included with all standard Python distributions.

## how to run

```
python main.py
```

## features

- allows to add/remove new components to the system, saving them for future simulations
- does not allow invalid inputs for new components added to the system

### TO DO

There is still a lot to do to complete this interface:
- recover simulation results from a .mat file
- show results in a clear fashion
- allow other "puissances de transmission" to be configured in the add_MRF_window
- allow other "frequences de traitement" to be configured in the add_MSP_window
- Scenario 2
- Scenario 3
- Scenario 4
- allow the user to choose the measurement unit for each parameter chosen

### Context
In a project of improving the work done by RAMMOUZ Ramzy in his thesis "Optimisation de la gestion d’énergie dans les systèmes embarqués", I will develop an interface to simplify the execution of the simulation, thus facilitating future reuse and continuation of this work.

### description in english
This python script will, in a first moment, show an intuitive visual interface where the user will provide the parameters and other information necessary to the simulation. Then, it will save this information in .mat files. Next, it will call the MATLAB simulation code. Finally, it will recover the simulation results and show them in a clear manner.

### description en français
Ce programme en python va, dans un premier temps, montrer une interface intuitive ou on saisie les paramétrés et valeurs nécessaires pour la simulation. Alors, il les stockera dans des fichiers .mat. Ensuite, il appellera le code de simulation MATLAB. Finalement, il va récupérer les résultats de la simulation et les afficher dans une façon claire.

### keywords
Remote patient monitoring ; wearable medical sensor networks ; energy consumption ; Matlab ; model ; simulation ; optimization ; Bluetooth Low Energy ;
Python ; interface

### abstract of the thesis "Optimisation de la gestion d’énergie dans les systèmes embarqués"
"*Whether it is to monitor patients at home, or to prevent the isolation and
vulnerability of the elderly, the emerging electronic monitoring and assistance
systems offer new opportunities. The technological development we have
witnessed allows individuals, hospitals, or medical aid organizations to provide
the diagnosis, prevention, control or even treatment of patients outside of
conventional clinical settings (measurements of physiological parameters, drug
administration, fall detection, etc.).
Recent developments in connected objects made efficient remote
patient monitoring possible. In other words, we are able to use a network of
wearable or implantable sensors to remotely obtain real time measurements of a
patient’s vital signs (temperature, heart rate, blood pressure, etc.). Data is
transmitted (and / or stored) to medical personnel who are able to perform
diagnosis and define treatments accordingly. An optimal design (transmission
protocols, data storage, etc.) and energy management are the bottlenecks
involved in the implementation of such systems.
This work proposes to develop a tool to help in the design of medical
sensor networks. It aims to provide information regarding feasibility during the
early stages of the design thus ensuring that a "well-constructed" circuit is
obtained. The emphasis is on the control (or even reduction) of energy
consumption.
In this regard, an efficient energy consumption simulation at the
beginning of the design flow would enable the user to decide on system
parameters. This will ensure an optimal management of the available energy
and eventually a longer network lifetime. The proposed tool is centered on the
optimization of the energy consumption using Matlab environment. It is built
over a model of the energy consumption of wireless sensor nodes. It is intended
to be generic and accurate. In fact, it enables fast creation of new component
description based on the datasheets. These components are reusable thus
producing a growing database. In addition to energy consumption estimation,
the tool uses optimization routines to guide the user through an energy aware
design (picking energy sources, components, network configuration, etc.) that
complies with medical requirements. An application to a single Bluetooth Low
Energy body temperature sensor is first proposed. The same sensor is then
included in a physiological sensor network. A physical implementation is used
in order to compare the results obtained through simulation with practical
measurements.*"
