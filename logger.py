class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name
        

        pass

    # The methods below are just suggestions. You can rearrange these or 
    # rewrite them to better suit your code style. 
    # What is important is that you log the following information from the simulation:
    # Meta data: This shows the starting situtation including:
    #   population, initial infected, the virus, and the initial vaccinated.
    # Log interactions. At each step there will be a number of interaction
    # You should log:
    #   The number of interactions, the number of new infections that occured
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    # When the simulation concludes you should log the results of the simulation. 
    # This should include: 
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation. 

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        self.file_name = 'output.txt'
        outfile = open('output.txt', 'w')
        starting_people_vaccinated = vacc_percentage * pop_size
        # metadata = "Herd-Immunity Simulation\nInitial population size: {self.pop_size}\n
        # Virus: {virus_name}\n
        # Initial infected: {self.initial_infected}\n
        # Initial vaccinated: {starting_people_vaccinated}"
        # "Herd-Immunity Simulation\n
        metadata = {
            'Initial population size': pop_size,
            'Virus': virus_name,
            'Initial infected': self.initial_infected,
            'Initial vaccinated': starting_people_vaccinated,
            'Mortality rate': mortality_rate,
            'Reproduction rate': basic_repro_num
        }

    
        outfile.write(metadata)
        outfile.close

    

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        number_of_interactions = 
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        pass

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        
        if person.is_alive == True:
            did_die_from_infection = False
        if person.is_alive == False:
            number_of_new_fatalities += 1
            did_die_from_infection = True

        population_count -= number_of_new_fatalities
        step_number += 1


        # Append the results of the infection to the logfile
        pass

    def log_time_step(self, time_step_number):
        # 
        pass

    # summary should include:
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation.
    def log_summary(self, pop_size, did_survive, did_not_survive, num_vaccinated, time_step_counter):
        summary = {
            'Initial population size': pop_size,
            'Living': did_survive,
            'Dead': did_not_survive,
            'Vaccinated survivors': num_vaccinated,
            'Number of time steps': time_step_counter
        }
        outfile.write(summary)
        outfile.close
        
        pass

    
    
if __name__ == "__main__":

