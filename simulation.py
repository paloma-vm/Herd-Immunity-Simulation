import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger(self)
        # TODO: Store the virus in an attribute
        self.virus = virus
        # TODO: Store pop_size in an attributes
        self.pop_size = pop_size
        # TODO: Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        # TODO: Store initial_infected in a variable
        self.initial_infected = initial_infected
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        # TODO: Call self._create_population() and pass in the correct parameters.
        # self.population = self._create_population(pop_size, vacc_percentage, initial_infected) 
        self.population = self._create_population() 

        self.newly_infected = []
        
        

    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the the initial_infected
        list_of_people = []
        
        for i in range(len(pop_size)):
            person = Person(i,is_vaccinated=False, infection=None)
            list_of_people.append(person)
        #  Make  vaccinated people
        starting_people_vaccinated = self.vacc_percentage * self.pop_size
        
        vaccinated_people = random.choices(list_of_people, weights=None, cum_weights=None, k=starting_people_vaccinated)
        for i in range(len(vaccinated_people)):
            person.is_vaccinated = True

        #  Make infected people
        infected_people = random.choices(list_of_people, weights=None, cum_weights=None, k=initial_infected)
        for i in range(len(infected_people)):
            person.infection = virus

        return list_of_people


    def _simulation_should_continue(self):
        # This method will return a booleanb indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 

        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        
        did_not_survive = 0
        did_survive = 0
        did_survive_is_vacc = 0
        
        for person in self.population:
            if person.is_alive is False:
                did_not_survive += 1
            if person.is_alive is True:
                did_survive += 1
            if person.is_alive is True and person.is_vaccinated is True:
                did_survive_is_vacc += 1
                

        if did_not_survive == self.pop_size and did_survive_is_vacc == did_survive:
            return False
        else:
            return True

    

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True
        

        while should_continue:
            # TODO: Increment the time_step_counter
            time_step_counter += 1
            
            # TODO: for every iteration of this loop, call self.time_step() 
            self.time_step()
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            should_continue = self._simulation_should_continue()

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
        self.logger.write_metadata(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num=virus.repro_rate)
       
       
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for person in self.population:
            if person.infection == virus:
                people_interacted_with = random.choices(self.population, weights=None, cum_weights=None, k=100)
                people_interacted_with.interaction()

        pass

    def interaction(self, infected_person, random_person):
    # TODO: Finish this method.
        # newly_infected = []
    # The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        if random_person.is_vaccinated == True:
            return random_person
        # random_person is already infected:
        #     nothing happens to random person.
        if random_person.infection == virus:#implies that they are not 
            #vaccinated because the code already looked at that above
            return random_person
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0.0 and 1.0.  If that number is smaller
        #     than repro_rate, add that person to the newly infected array
        if random_person.infection == None:
            random_number = random.random()
            if random_number < virus.repro_rate:
                self.newly_infected.append(random_person)
            
        #     Simulation object's newly_infected array, so that their infected
        #     attribute can be changed to True at the end of the time step.

        # TODO: Call logger method during this method.
        return self.newly_infected

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in self.newly_infected:
            person.infection = virus

        self.newly_infected.clear()
    


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
