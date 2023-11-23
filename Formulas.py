def calculate_cycle_fleet_utilization_rate(utilization_rate):
    return utilization_rate

def calculate_minimum_cycle_revenues(total_revenues, recycling_revenue):
    return total_revenues - recycling_revenue

# def calculate_total_costs(shared_costs, fleet_size, lease_management_costs, maintenance_costs, subscription_management_costs, rental_management_costs, recycling_costs):
#     fixed_costs = shared_costs / fleet_size
#     variable_costs = lease_management_costs + maintenance_costs + subscription_management_costs + maintenance_costs + rental_management_costs + maintenance_costs
#     end_of_life_costs = recycling_costs
#     total_costs = fixed_costs + variable_costs + end_of_life_costs
#     return total_costs

def calculate_total_costs(shared_costs, fleet_size, offering_costs, end_of_life_costs):
    print("shared_costs", shared_costs, fleet_size, offering_costs, end_of_life_costs)
    # Shared Costs / Fleet Size + Offering Costs + End-of-Life Costs​
    
    return (shared_costs/fleet_size) + offering_costs + end_of_life_costs


# def calculate_minimum_cycle_price(minimum_total_offering_revenues, cycle_duration, utilization_rate):
#     return minimum_total_offering_revenues / cycle_duration / utilization_rate

def calculate_market_adjustment(competitor_price, minimum_cycle_price, price_adjustment_slicer):
    market_adjustment = (competitor_price - minimum_cycle_price) * price_adjustment_slicer
    return max(0, market_adjustment)

def calculate_suggested_cycle_price(minimum_cycle_price, market_adjustment):
    return minimum_cycle_price + market_adjustment




################################################################

def calculate_average_transportations_per_month(average_of_contract_per_month, average_of_transportations_per_contract):
    return average_of_contract_per_month * average_of_transportations_per_contract

def calculate_average_storage_time(cycle_duration, fleet_utilization_rate, fleet_transportation):
    #Cycle Duration * (1 – Fleet Utilization Rate – Fleet Transportation / Processing Time)

    if fleet_transportation != 0:
        return 24 * (1- (fleet_utilization_rate + fleet_transportation))
    else:
        return 0

def calculate_average_of_rotation_inspections_per_month(average_of_rotation_inspections_per_month_dict):
    #Logic for selecting cycle MAYBE
    return average_of_rotation_inspections_per_month_dict

def calculate_average_inspection_and_maintenance_cost(average_inspection_and_maintenance_cost):
    #Logic for selecting cycle MAYBE
    return average_inspection_and_maintenance_cost


def calculate_regular_maintenance(average_regular_maintenance_costs, average_of_maintenance_per_cycle, cycle_duration):
    average_of_regular_maintenance_per_month = average_of_maintenance_per_cycle / cycle_duration

    return average_regular_maintenance_costs * average_of_regular_maintenance_per_month
def calculate_average_queries_per_month(average_queries_per_contract, average_of_contracts_per_month):
    return (average_queries_per_contract * average_of_contracts_per_month)

def calculate_average_contracts_per_month(average_of_contracts_per_cycle, cycle_duration):
    #  0.02 	 0.03 	 0.04 	 0.04 

    return (average_of_contracts_per_cycle/cycle_duration)

def calculate_vehicle_transportation(average_transportation_costs, average_transportations_per_month):
    return (average_transportation_costs * average_transportations_per_month)

def calculate_vehicle_storage(average_storage_costs, average_storage_time):
    return average_storage_costs * average_storage_time

def calculate_customer_support(average_costs_per_query_handling, average_queries_per_month):
    return (average_costs_per_query_handling * average_queries_per_month)

def calculate_contract_management(average_cost_per_contract, average_contracts_per_month):
    return (average_cost_per_contract * average_contracts_per_month)


def calculate_management_costs(contract_management, customer_support, vehicle_storage, vehicle_transportation):
    return (contract_management + customer_support + vehicle_storage + vehicle_transportation)

def calculate_subscription_management_costs(contract_management, customer_support, vehicle_storage, vehicle_transportation):
    return (contract_management + customer_support + vehicle_storage + vehicle_transportation)

def calculate_maintenance_costs(regular_maintenance, average_inspection_and_maintenance_costs, average_of_rotation_inspections_per_month, average_minor_repair_cost, average_minor_repair_probability_per_cycle, average_intermediate_repair_cost, average_intermediate_repair_probability_per_cycle, average_major_repair_cost, average_major_repair_probability_per_cycle, cycle_duration):

    vehicle_rotation_inspection_and_maintenance = average_inspection_and_maintenance_costs * average_of_rotation_inspections_per_month

    minor_repair_costs = average_minor_repair_cost * average_minor_repair_probability_per_cycle / cycle_duration
    intermediate_repair_costs = average_intermediate_repair_cost * average_intermediate_repair_probability_per_cycle / cycle_duration
    major_repair_costs = average_major_repair_cost * average_major_repair_probability_per_cycle / cycle_duration

    wear_and_tear_repairs = minor_repair_costs + intermediate_repair_costs + major_repair_costs

    return (regular_maintenance + vehicle_rotation_inspection_and_maintenance + wear_and_tear_repairs)

def calculate_lease_management_costs(contract_management,customer_support, vehicle_storage, vehicle_transportation):

    return (contract_management + customer_support + vehicle_storage + vehicle_transportation)

def calculate_rental_costs(rental_management_costs, maintenance_costs, cycle_duration):
    return (rental_management_costs + maintenance_costs)*cycle_duration

def calculate_subscription_costs(subscription_management_costs, maintenance_costs, cycle_duration):
    return (subscription_management_costs + maintenance_costs)*cycle_duration

def calculate_costs(management_costs, maintenance_costs, cycle_duration):
    return (management_costs + maintenance_costs)*cycle_duration


def calculate_fixed_costs(vehicle_acquisition, general_administrative, marketing, technology_infrastructure):
    # Vehicle Acquisition + General Administrative + Marketing (fixed) + Technology Infrastructure
    return (vehicle_acquisition + general_administrative + marketing + technology_infrastructure)


def calculate_variable_costs(marketing_variable, insurance):
    return marketing_variable + insurance
def calculate_offering_costs(leasing_costs, subscription_costs, rental_costs):
    #  Leasing Costs + Subscription Costs + Rental Costs​
    return (leasing_costs + subscription_costs + rental_costs)
def calculate_shared_costs(fixed_costs, variable_costs):
    return (fixed_costs + variable_costs) 


def calculate_minimum_total_revenues(total_costs, margin_target):
    return total_costs * (1 + margin_target)

def calculate_minimum_total_offering_revenues(minimum_total_revenues, end_of_life_revenues):
    return minimum_total_revenues - end_of_life_revenues
    
def calculate_minimum_cycle_revenues(minimum_total_offering_revenues, revenue_distribution_percentage_by_cycle):
    # Minimum Total Offering Revenues * Revenue Distribution % by Cycle​
    return minimum_total_offering_revenues*revenue_distribution_percentage_by_cycle

def calculate_minimum_cycle_price(minimum_cycle_revenues, cycle_duration, cycle_fleet_utilization_rate):
    return (minimum_cycle_revenues / cycle_duration) / cycle_fleet_utilization_rate

def calculate_market_adjustment(average_competitor_price, minimum_cycle_price, market_adjustment_slicer):
    # 2.	Market Adjustment = (Average Competitor Price – Minimum Price) / Market Adjustment Slicer

    return (average_competitor_price - minimum_cycle_price) * market_adjustment_slicer

def calculate_suggested_price(minimum_cycle_price, market_adjustment):
    # 3.	Suggested Price [Leasing/Subscription/Rental] =  Minimum Price + Market Adjustment

    return minimum_cycle_price + market_adjustment

def calculate_recycling_residual_value(recycling_material_value, spot_price_correction):
    # 4.	Remarketing Price/Residual Value = Obtained from external websites (e.g., used car valuation sites)

    return recycling_material_value * spot_price_correction

def calculate_remarketing_costs(remarketing_management_costs, refurbishment_costs):
    return remarketing_management_costs + refurbishment_costs

def calculate_recycling_costs(logistics_costs, process_costs):
    return logistics_costs + process_costs
