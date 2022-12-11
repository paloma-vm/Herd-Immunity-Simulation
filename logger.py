class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

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
        
        # outfile = open(self.file_name, 'w')
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

        # outfile = open(self.file_name, 'w')
        with open("self.file_name", 'w') as f:
            for key, value in metadata.items():
                f.write('%s:%s\n' % (key, value))#the format of the output is string : string new line

        # outfile.writelines(metadata)
        # outfile.close
        f.close

    

    def log_interactions(self, time_step_counter, number_of_interactions, number_of_new_infections):
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        f = open(self.file_name, "a")
        # number_of_interactions = 
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        if random_person.is_vaccinated is True:
            f.write("{infected_person._id} did not infect {random_person._id} because they were vaccinated")
        # random_person is already infected:
        #     nothing happens to random person.
        if random_person.infection == virus:#implies that they are not 
            #vaccinated because the code already looked at that above
            f.write("{infected_person._id} did not infect {random_person._id} because they were already infected.")
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0.0 and 1.0.  If that number is smaller
        #     than repro_rate, add that person to the newly infected array
        if random_person.infection is None and random_number < virus.repro_rate:
            f.write("{infected_person._id} infected {random_person._id}")
        if random_person.infection is None and random_number > virus.repro_rate:
            f.write("{infected_person._id} did not infect {random_person._id}")

        f.close

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
        results = {
            'Step number': step_number,
            'Population at start of step:': population_count,
            'Number of new fatalities': number_of_new_fatalities
        }
        
        with open(self.file_name, 'a') as f:
            for key, value in results.items():
                f.write('%s:%s\n' % (key, value))#the format of the output is string : string new line
        f.close
        
    # You should log the results of each step. This should inlcude: 
    #   The population size, the number of living, the number of dead, and the number 
    #   of vaccinated people at that step. 
    def log_time_step(self, time_step_number):
        """logs a summary of the results of the step"""

        # step_display =[
        # "----------------------------------\n",
        # "This is step number {time_step_number}"
        # ]
        step_summary = {
            "------- Step {time_step_number} ":"Results --------",
            'Initial population size': self.pop_size,
            'Living': self.did_survive,
            'Dead': self.did_not_survive,
            'Vaccinated survivors': self.num_vaccinated
        }
        # f = open("self.file_name", 'a')
        # f.writelines(step_summary)
        with open("self.file_name", 'a') as f:
            for key, value in step_summary.items():
                f.write('%s:%s\n' % (key, value))#the format of the output is string : string new line
        f.close
        

    # summary should include:
    #   The population size, the number of living, the number of dead, the number 
    #   of vaccinated, and the number of steps to reach the end of the simulation.
    def log_summary(self, pop_size, did_survive, did_not_survive, num_vaccinated, time_step_counter):
        """logs a summary of the results of the whole simulation """
        sim_summary = {
            "****** SIMULATION OVER ******":"Results ***************",
            'Initial population size': pop_size,
            'Living': did_survive,
            'Dead': did_not_survive,
            'Vaccinated survivors': num_vaccinated,
            'Number of time steps to reach the end of the simulation': time_step_counter
        }
        # outfile = open(self.file_name, 'a')
        # outfile.write(summary)
        # outfile.close
        with open("self.file_name", 'a') as f:
            for key, value in sim_summary.items():
                f.write('%s:%s\n' % (key, value))#the format of the output is string : string new line
        f.close
        