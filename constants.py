# constants.py
LEASING_YEARS_TO_CYCLE = {
    0: 'Cycle1',
    1: 'Cycle2',
    2: 'Cycle3',
    3: 'Cycle4',
}

OFFERINGS = ['Leasing', 'Subscription', 'Rental']
LIFE_CYCLES = ['Cycle1', 'Cycle2', 'Cycle3', 'Cycle4']

# Constants independent of life cycle and leasing years
COMMON_CONSTANTS = {
    'shared_costs': 67652792000,
    'cycle_duration': 24,
    'fleet_size': 1000000,
    'recycling_revenue': 1700.5222,
    'recycling_costs': 1155,
    'average_regular_maintenance_costs': 500,
    'margin_target': 0.10,

    # Add other constants here
}

INDEPENDENT_OF_OFFERING_CONSTANTS = {
    'revenue_distribution_percentage_by_cycle': {
        'Cycle1': 0.29,
        'Cycle2': 0.26,
        'Cycle3': 0.23,
        'Cycle4': 0.22,
    },
    'price_adjustment_slicer': {
        'Cycle1': 1.00,
        'Cycle2': 0.95,
        'Cycle3': 0.87,
        'Cycle4': 0.80,  
    }
}
LIFE_CYCLE_CONSTANTS = {
    'Leasing': {
        'Cycle1': {
            'average_of_contract_per_cycle': 0.5,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 2,
            'average_inspection_and_maintenance_costs': 180,
            'average_of_rotation_inspections_per_month': 0.02,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 1, #100%
            'average_of_contract_per_month': 0.02,
            'fleet_transportation': 0,
            'average_real_time_competitor_price': 1750,
            'average_minor_repair_probability_per_cycle': 0.07, #7%
            'average_intermediate_repair_probability_per_cycle': 0.06, #6%
            'average_major_repair_probability_per_cycle': 0.01 #%
        },
        'Cycle2': {
            'average_of_contract_per_cycle': 0.8,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 2,
            'average_inspection_and_maintenance_costs': 220,
            'average_of_rotation_inspections_per_month': 0.03,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.95,
            'average_of_contract_per_month': 0.03,
            'fleet_transportation': 0.01,
            'average_real_time_competitor_price': 1650,
            'average_minor_repair_probability_per_cycle': 0.08, #8%
            'average_intermediate_repair_probability_per_cycle': 0.07, #%
            'average_major_repair_probability_per_cycle': 0.02 #%
        },
        'Cycle3': {
            'average_of_contract_per_cycle': 1,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 3,
            'average_inspection_and_maintenance_costs': 250,
            'average_of_rotation_inspections_per_month': 0.04,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.90,
            'average_of_contract_per_month': 0.04,
            'fleet_transportation': 0.03,
            'average_real_time_competitor_price': 1550,
            'average_minor_repair_probability_per_cycle': 0.10, #10%
            'average_intermediate_repair_probability_per_cycle': 0.09, #%
            'average_major_repair_probability_per_cycle': 0.03 #%
        },
        'Cycle4': {
            'average_of_contract_per_cycle': 1,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 4,
            'average_inspection_and_maintenance_costs': 300,
            'average_of_rotation_inspections_per_month': 0.04,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.85,
            'average_of_contract_per_month': 0.04,
            'fleet_transportation': 0.05,
            'average_real_time_competitor_price': 1450,
            'average_minor_repair_probability_per_cycle': 0.12, #12%
            'average_intermediate_repair_probability_per_cycle': 0.11, #%
            'average_major_repair_probability_per_cycle': 0.03 #%
        },
    },
    'Subscription': {
        'Cycle1': {
            'average_of_contract_per_cycle': 0.8,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle':2,
            'average_inspection_and_maintenance_costs': 200,
            'average_of_rotation_inspections_per_month': 0.03,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 1, #100%
            'average_of_contract_per_month': 0.03,
            'fleet_transportation': 0,
            'average_real_time_competitor_price': 1850,
            'average_minor_repair_probability_per_cycle': 0.08, #8%
            'average_intermediate_repair_probability_per_cycle': 0.07, #%
            'average_major_repair_probability_per_cycle': 0.02 #%
        },
        'Cycle2': {
            'average_of_contract_per_cycle': 1,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 3,
            'average_inspection_and_maintenance_costs': 240,
            'average_of_rotation_inspections_per_month': 0.04,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.80,
            'average_of_contract_per_month': 0.04,
            'fleet_transportation': 0.05,
            'average_real_time_competitor_price': 1750,
            'average_minor_repair_probability_per_cycle': 0.10, #10%
            'average_intermediate_repair_probability_per_cycle': 0.09, #%
            'average_major_repair_probability_per_cycle': 0.03 #%

        },
        'Cycle3': {
            'average_of_contract_per_cycle': 1.5,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 4,
            'average_inspection_and_maintenance_costs': 270,
            'average_of_rotation_inspections_per_month': 0.06,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.77,
            'average_of_contract_per_month': 0.06,
            'fleet_transportation': 0.08,
            'average_real_time_competitor_price': 1650,
            'average_minor_repair_probability_per_cycle': 0.11, #11%
            'average_intermediate_repair_probability_per_cycle': 0.11, #%
            'average_major_repair_probability_per_cycle': 0.03 #%
        },
        'Cycle4': {
            'average_of_contract_per_cycle': 2,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 5,
            'average_inspection_and_maintenance_costs': 320,
            'average_of_rotation_inspections_per_month': 0.08,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.75,
            'average_of_contract_per_month': 0.08,
            'fleet_transportation': 0.12,
            'average_real_time_competitor_price': 1550,
            'average_minor_repair_probability_per_cycle': 0.13, #13%
            'average_intermediate_repair_probability_per_cycle': 0.12, #%
            'average_major_repair_probability_per_cycle': 0.04 #%
        },
    },
    'Rental': {
        'Cycle1': {
            'average_of_contract_per_cycle': 60,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 4,
            'average_inspection_and_maintenance_costs': 80,
            'average_of_rotation_inspections_per_month': 2.50,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 1,
            'average_of_contract_per_month': 2.50,
            'fleet_transportation': 0,
            'average_real_time_competitor_price': 2800,
            'average_minor_repair_probability_per_cycle': 0.10, #10%
            'average_intermediate_repair_probability_per_cycle': 0.09, #%
            'average_major_repair_probability_per_cycle': 0.03 #%
        },
        'Cycle2': {
            'average_of_contract_per_cycle': 55,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 6,
            'average_inspection_and_maintenance_costs': 110,
            'average_of_rotation_inspections_per_month': 2.29,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.65,
            'average_of_contract_per_month': 2.29,
            'fleet_transportation': 0.10,
            'average_real_time_competitor_price': 2600,
            'average_minor_repair_probability_per_cycle': 0.12, #12%
            'average_intermediate_repair_probability_per_cycle': 0.10, #%
            'average_major_repair_probability_per_cycle': 0.04 #%
        },
        'Cycle3': {
            'average_of_contract_per_cycle': 50,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 7,
            'average_inspection_and_maintenance_costs': 130,
            'average_of_rotation_inspections_per_month': 2.08,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.63,
            'average_of_contract_per_month': 2.08,
            'fleet_transportation': 0.15,
            'average_real_time_competitor_price': 2350,
            'average_minor_repair_probability_per_cycle': 0.14, #14%
            'average_intermediate_repair_probability_per_cycle': 0.12, #%
            'average_major_repair_probability_per_cycle': 0.04 #%
        },
        'Cycle4': {
            'average_of_contract_per_cycle': 45,
            'cycle_duration': 24,
            'average_of_maintenance_per_cycle': 8,
            'average_inspection_and_maintenance_costs': 150,
            'average_of_rotation_inspections_per_month': 1.88,
            'average_minor_repair_cost' : 652,
            'average_intermediate_repair_cost' : 1500,
            'average_major_repair_cost' : 3260,
            'fleet_utilization_rate': 0.60,
            'average_of_contract_per_month': 1.88,
            'fleet_transportation': 0.18,
            'average_real_time_competitor_price': 2100,
            'average_minor_repair_probability_per_cycle': 0.16, #16%
            'average_intermediate_repair_probability_per_cycle': 0.14, #%
            'average_major_repair_probability_per_cycle': 0.05 #%
        }
    },
}
OFFERING_CONSTANTS = {
    'Leasing': {
        'average_cost_per_contract': 100,
        'average_queries_per_contract': 4,
        'average_storage_costs': 90,
        'average_transportation_costs': 50,
        'average_of_transportations_per_contract': 6,
        'average_regular_maintenance_costs': 500,
        'average_costs_per_query_handling': 15,
        # Add other constants specific to Leasing
    },
    'Subscription': {
        'average_cost_per_contract': 80,
        'average_queries_per_contract': 3,
        'average_storage_costs': 90,
        'average_transportation_costs': 30,
        'average_of_transportations_per_contract': 4,
        'average_regular_maintenance_costs': 500,
        'average_costs_per_query_handling': 12,
        # Add other constants specific to Subscription
    },
    'Rental': {
        'average_cost_per_contract': 20,
        'average_queries_per_contract': 0.5,
        'average_storage_costs': 90,
        'average_transportation_costs': 10,
        'average_of_transportations_per_contract': 0.2,
        'average_regular_maintenance_costs': 500,
        'average_costs_per_query_handling': 6,
        # Add other constants specific to Leasing
    },
    # Repeat for other offerings
}