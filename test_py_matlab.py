# to test calling a matlab function from a python code


#addpath('C:\\Users\\pimenta\\Desktop\\Codes_these_Ramzy\\Code Matlab','-end')

import matlab.engine

eng = matlab.engine.start_matlab()
eng.start_simulation(nargout=0)
eng.quit()