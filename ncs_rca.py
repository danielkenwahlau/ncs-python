'''
Phyton access to the commands of the Remote Control Agent.
 
Copyright IFEN GmbH 2012
@author: uwsc
'''
import sys
import logging
import tcp_if



class NCS_RCA ():
    
    def __init__(self, ip_addr, port):
        self.agent_ip_addr = ip_addr
        self.agent_port = port
        # logging.basicConfig(level=logging.ERROR)
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
        self.agent_connect()

        
    def agent_connect(self):
        
        try:
            self.tcp_cmd = tcp_if.TCP_IF(self.agent_ip_addr, self.agent_port)

            line = "xxx"
            while (line != ""):
                line = self.tcp_cmd.read_line(2)
                logging.info(line)

        except:
            logging.error("Establish TCP connection to NCS Agent failed\n")
            raise

    
    def system_version(self):
        'Poll for the version information of the NCS-RemoteControlAgent'
        self.tcp_cmd.send_cmd("sys version;")
        
        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(2)
            if (line.startswith("NCS-RCA")):
                #self.tapreport.report(True, "Poll NCS-RCA version information", yaml = line)
                logging.info(line)
            else:
                logging.info(line)


    def system_hw_ip_set(self, ipadress):
        self.tcp_cmd.send_cmd("sc param hw_ip set " + ipadress + ";")
        
        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)
        
        
    def scenario_load(self, scenario_file):
        self.tcp_cmd.send_cmd("sc load " + scenario_file + ";")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)


    def scenario_param_start_time_set(self, start_time):
        self.tcp_cmd.send_cmd("sc param start_time set " + start_time + ";")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)        

		
    def scenario_param_end_time_set(self, end_time):
        self.tcp_cmd.send_cmd("sc param end_time set " + end_time + ";")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)
	
    def scenario_param_traj_filename_set(self, traj_filename):
        self.tcp_cmd.send_cmd("sc param traj_filename set " + traj_filename + ";")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)

      
    def simulation_run(self):
        self.tcp_cmd.send_cmd("sim run;")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                #self.tapreport.report(True, "Poll NCS RCA version information", yaml = line)
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)
    

    def simulation_stop(self):
        self.tcp_cmd.send_cmd("sim stop;")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                #self.tapreport.report(True, "Poll NCS RCA version information", yaml = line)
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)

        
    def simulation_param_powerlevel_set(self, signal, level):
        self.tcp_cmd.send_cmd("sim param powerlevel set " + signal + " " + level + ";")

    def simulation_param_powerlevel_get(self, signal):
        result = self.tcp_cmd.send_cmd("sim param powerlevel get;")
        return result
    
    def simulation_info_powerlevel(self):
        self.tcp_cmd.send_cmd("sim info powerlevel;")

        results = []
        
        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            elif (line.startswith("OK: E")):
                logging.info(line)
                line = self.tcp_cmd.read_line(5)
                results.append(line)
                
        return results
    
    def __del__(self):
        pass
        #self.tcp_cmd.send_cmd("sys abort;")


#TODO: change the listening time to 1 second or less for all functions
    #start of custom defined methods

    def help(self):
        self.tcp_cmd.send_cmd("hel;")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(1)

    def time(self):
        self.tcp_cmd.send_cmd("tim:end;")

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(1)

    #Load workspace on the control agent                
    def workspace_load(self, filename):
        self.tcp_cmd.send_cmd("work " + filename)

        line = "xxx"
        while (line != ""):
            line = self.tcp_cmd.read_line(3)
            if (line.startswith("NCS-RCA")):
                logging.info(line)
            else:
                logging.info(line)
                line = self.tcp_cmd.read_line(5)


       
#endclass
