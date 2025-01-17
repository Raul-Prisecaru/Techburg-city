class Config:
    """Class representing configuration parameters for a simulation."""

    # GUI Settings
    SIM_NAME = "Ocean Simulation"
    SIMULATION_TIMER = 1
    GRID_WIDTH = 30
    GRID_HEIGHT = 30

    SURVIVOR_BOT_COLOUR = "red"
    MALFUNCTIONING_DRONE_COLOUR = "blue"
    SCAVENGER_SWARM_COLOUR = "green"
    RECHARGE_STATION_COLOUR = "purple"
    SPARE_PART_COLOUR = "black"

    MAX_SURVIVOR_BOT = 5
    PROBABILITY_NEW_GATHERER_BOT = 0.2
    PROBABILITY_NEW_REPAIR_BOT = 0.05


    # Malfunctioning Drone Settings
    MAX_MALFUNCTIONING_DRONE = 5
    MALFUNCTIONING_DRONE_MAX_ENERGY = 100
    MALFUNCTIONING_DRONE_RECHARGE_SPEED = 20

    MAX_SPARE_PARTS = 80


