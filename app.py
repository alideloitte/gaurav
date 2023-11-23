from flask import Flask, render_template, request, jsonify, request
import numpy as np

from vin_identification import vehicle_details
import Formulas
import constants
from constants import OFFERING_CONSTANTS, LIFE_CYCLE_CONSTANTS, LEASING_YEARS_TO_CYCLE, COMMON_CONSTANTS, INDEPENDENT_OF_OFFERING_CONSTANTS
import matplotlib.pyplot as plt
import numpy as np
TOTAL_YEARS = 8
LIFE_CYCLE_YEARS = 2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def plot_traditional_user_stacked_bar(user_categories, user_costs, user_profits):
    # Calculate percentages
    total_values = np.array(user_costs) + np.array(user_profits)
    cost_percentages = np.array(user_costs) / total_values * 100
    profit_percentages = np.array(user_profits) / total_values * 100

    # Create a numpy array for the x-axis positions
    x = np.arange(len(user_categories))

    # Creating a horizontal stacked bar plot with percentages inside bars
    fig, ax = plt.subplots()
    bars1 = ax.barh(x, user_costs, color='skyblue', label='Costs', edgecolor='none')
    bars2 = ax.barh(x, user_profits, color='grey', label='Profits', edgecolor='none', left=user_costs)

    # Adding labels and title
    plt.yticks(x, user_categories)  # Set y-ticks to be custom labels
    plt.xlabel('Values')
    plt.ylabel('Cycles')
    plt.title('Projection - Traditional Utilization (Euros, in thousand)')  # Updated title

    # Adding legend
    ax.legend()

    # Annotating bars with percentages inside their respective portions
    for i, (bar, cost_percentage, profit_percentage) in enumerate(zip(bars1, cost_percentages, profit_percentages)):
        width = bar.get_width()
        # Calculate x-coordinate for profit bars (aligned with the end of the bars)
        profit_x = bar.get_x() + width + (bars2[i].get_width() / 2)
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                f'{cost_percentage:.1f}%', va='center', ha='center', color='white', fontsize=8)
        ax.text(profit_x, bar.get_y() + bar.get_height() / 2,
                f'{profit_percentage:.1f}%', va='center', ha='center', color='black', fontsize=8)


    # Remove x-axis ticks and labels
    plt.xticks([])

    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Displaying the plot
    # plt.show()
def plot_calculated_selected_stacked_bar(user_categories, user_costs, user_profits):
    # Calculate percentages
    total_values = np.array(user_costs) + np.array(user_profits)
    cost_percentages = np.array(user_costs) / total_values * 100
    profit_percentages = np.array(user_profits) / total_values * 100

    print("in_line_70", user_categories, user_costs, user_profits)

    # Create a numpy array for the x-axis positions
    x = np.arange(len(user_categories))

    # Creating a horizontal stacked bar plot with percentages inside bars
    fig, ax = plt.subplots()
    bars1 = ax.barh(x, user_costs, color='green', label='Costs', edgecolor='none')
    bars2 = ax.barh(x, user_profits, color='orange', label='Profits', edgecolor='none', left=user_costs)

    # Adding labels and title
    plt.yticks(x, user_categories)  # Set y-ticks to be custom labels
    plt.xlabel('Values')
    plt.ylabel('Cycles')
    plt.title('Projection User Selected Utilization (Euros, in thousand)')  # Updated title

    # Adding legend
    ax.legend()

    # Annotating bars with percentages inside their respective portions
    for i, (bar, cost_percentage, profit_percentage) in enumerate(zip(bars1, cost_percentages, profit_percentages)):
        width = bar.get_width()
        # Calculate x-coordinate for profit bars (aligned with the end of the bars)
        profit_x = bar.get_x() + width + (bars2[i].get_width() / 2)
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                f'{cost_percentage:.1f}%', va='center', ha='center', color='white', fontsize=8)
        ax.text(profit_x, bar.get_y() + bar.get_height() / 2,
                f'{profit_percentage:.1f}%', va='center', ha='center', color='black', fontsize=8)


    # Remove x-axis ticks and labels
    plt.xticks([])

    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Displaying the plot
    # plt.show()



def plot_user_selected_stacked_bar(user_categories, user_costs, user_profits):
    # Calculate percentages
    total_values = np.array(user_costs) + np.array(user_profits)
    cost_percentages = np.array(user_costs) / total_values * 100
    profit_percentages = np.array(user_profits) / total_values * 100

    # Create a numpy array for the x-axis positions
    x = np.arange(len(user_categories))

    # Creating a horizontal stacked bar plot with percentages inside bars
    fig, ax = plt.subplots()
    bars1 = ax.barh(x, user_costs, color='green', label='Costs', edgecolor='none')
    bars2 = ax.barh(x, user_profits, color='orange', label='Profits', edgecolor='none', left=user_costs)

    # Adding labels and title
    plt.yticks(x, user_categories)  # Set y-ticks to be custom labels
    plt.xlabel('Values')
    plt.ylabel('Cycles')
    plt.title('Projection User Selected Utilization (Euros, in thousand)')  # Updated title

    # Adding legend
    ax.legend()

    # Annotating bars with percentages inside their respective portions
    for i, (bar, cost_percentage, profit_percentage) in enumerate(zip(bars1, cost_percentages, profit_percentages)):
        width = bar.get_width()
        # Calculate x-coordinate for profit bars (aligned with the end of the bars)
        profit_x = bar.get_x() + width + (bars2[i].get_width() / 2)
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2,
                f'{cost_percentage:.1f}%', va='center', ha='center', color='white', fontsize=8)
        ax.text(profit_x, bar.get_y() + bar.get_height() / 2,
                f'{profit_percentage:.1f}%', va='center', ha='center', color='black', fontsize=8)


    # Remove x-axis ticks and labels
    plt.xticks([])

    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Displaying the plot
    # plt.show()


def plot_stacked_bar(categories, costs, profits):
    # Calculate percentages
    total_values = np.array(costs) + np.array(profits)
    cost_percentages = np.array(costs) / total_values * 100
    profit_percentages = np.array(profits) / total_values * 100

    # Create a numpy array for the x-axis positions
    x = np.arange(len(categories))

    # Creating a horizontal stacked bar plot with percentages inside bars
    fig, ax = plt.subplots()
    bars1 = ax.barh(x, costs, color='skyblue', label='Costs', edgecolor='none')
    bars2 = ax.barh(x, profits, color='orange', left=costs, label='Profits', edgecolor='none')

    # Adding labels and title
    plt.yticks(x, categories)  # Set y-ticks to be custom labels
    plt.xlabel('Values')
    plt.ylabel('Cycles')
    plt.title('Projection Suggested Utilization (Euros, in thousand)')  # Updated title

    # Adding legend
    ax.legend()

    # Annotating bars with percentages inside their respective portions
    for i, (bar, cost_percentage, profit_percentage) in enumerate(zip(bars1, cost_percentages, profit_percentages)):
        width = bar.get_width()
        ax.text(bar.get_x() + width / 2, bar.get_y() + bar.get_height() / 2, 
                f'{cost_percentage:.1f}%', va='center', ha='center', color='white', fontsize=8)
        ax.text(bar.get_x() + width + (bars2[i].get_width() / 2), bar.get_y() + bar.get_height() / 2, 
                f'{profit_percentage:.1f}%', va='center', ha='center', color='black', fontsize=8)

    # Remove x-axis ticks and labels
    plt.xticks([])

    # Remove borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Displaying the plot
    # plt.show()



def calculate_common_profit_formulas(life_cycle, type_of_offering):
    # leasing_years
    # type_of_life_cycle
    print('life_cycle', life_cycle)
    print('type_of_offering', type_of_offering)

    life_cycle_constants = LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]
    offering_constants = OFFERING_CONSTANTS[type_of_offering]

    # average_of_contract_per_cycle = life_cycle_constants['average_of_contract_per_cycle']
    # cycle_duration = life_cycle_constants['cycle_duration']
    # average_cost_per_contract = offering_constants['average_cost_per_contract']
    # offering_constant_y = offering_constants['OFFERING_CONSTANT_Y']
    # independent_constant_1_value = COMMON_CONSTANTS['independent_constant_1']
    # independent_constant_2_value = COMMON_CONSTANTS['independent_constant_2']
    # maintenance_per_cycle = OFFERING_INDEPENDENT_CONSTANTS['average_of_maintenance_per_cycle_dict'][type_of_offering]

    shared_costs =  COMMON_CONSTANTS['shared_costs']
    cycle_duration = COMMON_CONSTANTS['cycle_duration']
    fleet_size = COMMON_CONSTANTS['fleet_size']
    recycling_revenue = COMMON_CONSTANTS['recycling_revenue']
    recycling_costs = COMMON_CONSTANTS['recycling_costs'] 
    average_regular_maintenance_costs = offering_constants['average_regular_maintenance_costs']
    average_of_maintenance_per_cycle_dict = life_cycle_constants['average_of_maintenance_per_cycle']
    average_inspection_and_maintenance_costs_dict = life_cycle_constants['average_inspection_and_maintenance_costs']	  	  	  
    average_of_rotation_inspections_per_month_dict = life_cycle_constants['average_of_rotation_inspections_per_month']
    average_minor_repair_cost = life_cycle_constants['average_minor_repair_cost']
    average_intermediate_repair_cost = life_cycle_constants['average_intermediate_repair_cost']
    average_major_repair_cost = life_cycle_constants['average_major_repair_cost']
    margin_target = COMMON_CONSTANTS['margin_target'] # Assumption to be 10% 
    fleet_utilization_rate = life_cycle_constants['fleet_utilization_rate']
    revenue_distribution_percentage_by_cycle =INDEPENDENT_OF_OFFERING_CONSTANTS['revenue_distribution_percentage_by_cycle'][life_cycle]# Set Assumption – 29%, 26%, 23%, 22% for 4 cycles respectively​
    
    lease_average_cost_per_contract = OFFERING_CONSTANTS['Leasing']['average_cost_per_contract']
    lease_average_queries_per_contract = OFFERING_CONSTANTS['Leasing']['average_queries_per_contract']
    lease_average_costs_per_query_handling = OFFERING_CONSTANTS['Leasing']['average_costs_per_query_handling']
    lease_average_storage_costs = OFFERING_CONSTANTS['Leasing']['average_storage_costs']
    lease_average_transportation_costs = OFFERING_CONSTANTS['Leasing']['average_transportation_costs']
    lease_average_of_transportations_per_contract = OFFERING_CONSTANTS['Leasing']['average_of_transportations_per_contract']
    lease_average_of_contract_per_cycle = LIFE_CYCLE_CONSTANTS['Leasing'][life_cycle]['average_of_contract_per_cycle']
    lease_average_of_contract_per_month =  LIFE_CYCLE_CONSTANTS['Leasing'][life_cycle]['average_of_contract_per_month']
    lease_fleet_utilization_rate = LIFE_CYCLE_CONSTANTS['Leasing'][life_cycle]['fleet_utilization_rate']
    lease_fleet_transportation = LIFE_CYCLE_CONSTANTS['Leasing'][life_cycle]['fleet_transportation']

    subscription_average_cost_per_contract = OFFERING_CONSTANTS['Subscription']['average_cost_per_contract']
    subscription_average_queries_per_contract = OFFERING_CONSTANTS['Subscription']['average_queries_per_contract']
    subscription_average_costs_per_query_handling = OFFERING_CONSTANTS['Subscription']['average_costs_per_query_handling']
    subscription_average_storage_costs = OFFERING_CONSTANTS['Subscription']['average_storage_costs']
    subscription_average_transportation_costs = OFFERING_CONSTANTS['Subscription']['average_transportation_costs']
    subscription_average_of_transportations_per_contract = OFFERING_CONSTANTS['Subscription']['average_of_transportations_per_contract']
    #can check on this value from jasmin
    subscription_average_of_contract_per_cycle = LIFE_CYCLE_CONSTANTS['Subscription'][life_cycle]['average_of_contract_per_cycle']
    subscription_fleet_utilization_rate = LIFE_CYCLE_CONSTANTS['Subscription'][life_cycle]['fleet_utilization_rate']
    subscription_fleet_transportation = LIFE_CYCLE_CONSTANTS['Subscription'][life_cycle]['fleet_transportation']
    subscription_average_of_contract_per_month = LIFE_CYCLE_CONSTANTS['Subscription'][life_cycle]['average_of_contract_per_month']


    rental_average_cost_per_contract = OFFERING_CONSTANTS['Rental']['average_cost_per_contract']
    rental_average_queries_per_contract = OFFERING_CONSTANTS['Rental']['average_queries_per_contract']
    rental_average_costs_per_query_handling = OFFERING_CONSTANTS['Rental']['average_costs_per_query_handling']
    rental_average_storage_costs = OFFERING_CONSTANTS['Rental']['average_storage_costs']
    rental_average_transportation_costs = OFFERING_CONSTANTS['Rental']['average_transportation_costs']
    rental_average_of_transportations_per_contract = OFFERING_CONSTANTS['Rental']['average_of_transportations_per_contract']
    #can check on this value from jasmin
    rental_average_of_contract_per_cycle = LIFE_CYCLE_CONSTANTS['Rental'][life_cycle]['average_of_contract_per_cycle']
    rental_fleet_utilization_rate = LIFE_CYCLE_CONSTANTS['Rental'][life_cycle]['fleet_utilization_rate']
    rental_fleet_transportation = LIFE_CYCLE_CONSTANTS['Rental'][life_cycle]['fleet_transportation']
    rental_average_of_contract_per_month =LIFE_CYCLE_CONSTANTS['Rental'][life_cycle]['average_of_contract_per_month']

    # Cycle duration in Years
    average_of_contract_per_month =LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]['average_of_contract_per_month']
    average_of_transportations_per_contract = OFFERING_CONSTANTS[type_of_offering]['average_of_transportations_per_contract']
    fleet_utilization_rate = LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]['fleet_utilization_rate']
    fleet_transportation = LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]['fleet_transportation']
    average_of_contract_per_cycle = LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]['average_of_contract_per_cycle']
    average_queries_per_contract = OFFERING_CONSTANTS[type_of_offering]['average_queries_per_contract']
    average_of_contract_per_month =LIFE_CYCLE_CONSTANTS[type_of_offering][life_cycle]['average_of_contract_per_month']
    average_transportation_costs = OFFERING_CONSTANTS[type_of_offering]['average_transportation_costs']
    average_storage_costs = OFFERING_CONSTANTS[type_of_offering]['average_storage_costs']
    average_costs_per_query_handling = OFFERING_CONSTANTS[type_of_offering]['average_costs_per_query_handling']
    average_cost_per_contract = OFFERING_CONSTANTS[type_of_offering]['average_cost_per_contract']

    #4 market_adjustment
    average_real_time_competitor_price = life_cycle_constants['average_real_time_competitor_price']
    price_adjustment_slicer = INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][life_cycle]
    # print("average_regular_maintenance_costs", average_regular_maintenance_costs, average_of_maintenance_per_cycle_dict)
    regular_maintenance = Formulas.calculate_regular_maintenance(average_regular_maintenance_costs, average_of_maintenance_per_cycle_dict, cycle_duration)
    # print("regular_maintenance_", regular_maintenance)
    average_inspection_and_maintenance_costs = Formulas.calculate_average_inspection_and_maintenance_cost(average_inspection_and_maintenance_costs_dict)
    average_of_rotation_inspections_per_month = Formulas.calculate_average_of_rotation_inspections_per_month(average_of_rotation_inspections_per_month_dict)
    average_minor_repair_probability_per_cycle = life_cycle_constants['average_minor_repair_probability_per_cycle']
    average_intermediate_repair_probability_per_cycle = life_cycle_constants['average_intermediate_repair_probability_per_cycle']
    average_major_repair_probability_per_cycle = life_cycle_constants['average_major_repair_probability_per_cycle']

    # CONSTANTS ABOVE 
    average_transportations_per_month = Formulas.calculate_average_transportations_per_month(average_of_contract_per_month, average_of_transportations_per_contract)
    average_storage_time = Formulas.calculate_average_storage_time(cycle_duration,  fleet_utilization_rate, fleet_transportation)    
    average_contracts_per_month = Formulas.calculate_average_contracts_per_month(average_of_contract_per_cycle, cycle_duration)
    average_queries_per_month = Formulas.calculate_average_queries_per_month(average_queries_per_contract, average_of_contract_per_month)    
    vehicle_transportation = Formulas.calculate_vehicle_transportation(average_transportation_costs, average_transportations_per_month)
    vehicle_storage = Formulas.calculate_vehicle_storage(average_storage_costs, average_storage_time)
    customer_support = Formulas.calculate_customer_support(average_costs_per_query_handling, average_queries_per_month)
    contract_management = Formulas.calculate_contract_management(average_cost_per_contract, average_contracts_per_month)

  
    # Need to check common values for the below three.
    management_costs = Formulas.calculate_management_costs(contract_management, customer_support, vehicle_storage, vehicle_transportation)
    maintenance_costs = Formulas.calculate_maintenance_costs(regular_maintenance, average_inspection_and_maintenance_costs, average_of_rotation_inspections_per_month, average_minor_repair_cost, average_minor_repair_probability_per_cycle, average_intermediate_repair_cost, average_intermediate_repair_probability_per_cycle, average_major_repair_cost, average_major_repair_probability_per_cycle, cycle_duration)
    costs = Formulas.calculate_costs(management_costs, maintenance_costs, cycle_duration)
    
    return life_cycle, type_of_offering, costs


def calculate_total_offering_cost(one_combination):
    print("one_combination_1", one_combination)
    individual_suggested_prices = []
    # cycle_profit = {}

    # print("one_combination", one_combination)
    for one_combo in one_combination:
        print("one_combo_353", one_combo)
        total_offering_cost_per_cycle = 0
        cycle_offering_cost = {}
        total_costs_per_cycle = {}
        leasing_suggested_price = 0
        rental_suggested_price = 0
        subscription_suggested_price = 0
        # print("one_combo", one_combo)
        for key, value in one_combo.items():
            if value == 'Leasing':
                print("key,value", key, value)
                life_cycle, type_of_offering, leasing_total_cost = calculate_common_profit_formulas(key, value)
                print("leasing_total_cost", leasing_total_cost)
                cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': leasing_total_cost})
                # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
                total_offering_cost_per_cycle += leasing_total_cost
                # print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
                # print("leasing_suggested_price", leasing_suggested_price)
                # print("total_profit_leasing_suggested_price", total_profit)
            elif value == 'Rental':
                life_cycle, type_of_offering, rental_total_cost = calculate_common_profit_formulas(key, value)
                print("rental_total_cost", rental_total_cost)
                cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': rental_total_cost})
                # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
                total_offering_cost_per_cycle += rental_total_cost
                # print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
                # print("rental_suggested_price", rental_suggested_price)
                # print("total_profit_rental_suggested_price", total_profit)
            elif value == 'Subscription':
                life_cycle, type_of_offering, subscription_total_cost = calculate_common_profit_formulas(key, value)
                print("subscription_total_cost", subscription_total_cost)
                cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': subscription_total_cost})
                # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
                total_offering_cost_per_cycle += subscription_total_cost
                # print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
            print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
        cycle_offering_cost.update({'total_offering_cost': total_offering_cost_per_cycle})
        print("cycle_offering_cost_update", cycle_offering_cost)
        # print("cycle_offering_cost", cycle_offering_cost)
        # print("cycle_offering_cost_length", len(cycle_offering_cost))
    # return cycle_profit, total_costs_per_cycle
    return cycle_offering_cost

def calculate_market_adjustment(list_of_offerings_and_offering_cost):
    result_data = []

    for dictionary in list_of_offerings_and_offering_cost:
        market_adjustments = {}
        print("dictionary_374", dictionary)
        for key, value in dictionary.items():
            if key.startswith('Cycle'):
                cycle_number, offering_type = key.split(':')[0], key.split(':')[1]  # Extract cycle_number and offering_type
                print("cycle_number", cycle_number, offering_type)
                if offering_type in LIFE_CYCLE_CONSTANTS and cycle_number in LIFE_CYCLE_CONSTANTS[offering_type]:
                    print("inside if")
                    competitor_price = LIFE_CYCLE_CONSTANTS[offering_type][cycle_number]['average_real_time_competitor_price']
                    print("competitor_price", competitor_price)
                    market_adjustment_key = f'market_adjustment_{key}'
                    cycle_revenues_key = f'minimum_{cycle_number.lower()}_price'
                    print("cycle_revenues_key", cycle_revenues_key)
                    print("item[cycle_revenues_key]", dictionary[cycle_revenues_key])
                    print("INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number]", INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number])
                    market_adjustment = (competitor_price - dictionary[cycle_revenues_key]) * INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number]
                    print("market_adjustment", market_adjustment)
                    market_adjustments[market_adjustment_key] = market_adjustment

        # Merge the original dictionary with calculated market adjustments
        updated_item = {**dictionary, **market_adjustments}
        # print("updated_item", updated_item)
        result_data.append(updated_item)
        # print("result_data", result_data)
    return result_data


def calculate_minimum_cycle_prices(dictionary):
    data1 = []
    print("dictionary_413", dictionary)
    minimum_cycle_price_dict = {}
    cycle_duration = COMMON_CONSTANTS['cycle_duration']
    for key in dictionary:
        # print("key", key)
        if key.startswith('Cycle'):
            cycle_number, offering_type = key.split(':')[0], key.split(':')[1]  # Extract cycle_number and offering_type
            # print("dictionary_sample", dictionary['minimum_cycle1_revenues'])
            # print("cycle_number", cycle_number, offering_type)
            if offering_type in LIFE_CYCLE_CONSTANTS:
                fleet_utilization_rate = LIFE_CYCLE_CONSTANTS[offering_type][cycle_number]['fleet_utilization_rate']
                fleet_utilization_rate_key = f'{cycle_number.lower()}_fleet_utilization_rate'
                minimum_cycle_price_key = f'minimum_{cycle_number.lower()}_price'
                minimum_cycle_revenues_key = f'minimum_{cycle_number.lower()}_revenues'
                # print("minimum_cycle_price_key", minimum_cycle_price_key, minimum_cycle_revenues_key, fleet_utilization_rate)
                minimum_cycle_price = dictionary[minimum_cycle_revenues_key] / cycle_duration / fleet_utilization_rate
                # print("minimum_cycle_price", minimum_cycle_price)
                minimum_cycle_price_dict[minimum_cycle_price_key] = minimum_cycle_price
                minimum_cycle_price_dict[fleet_utilization_rate_key] = fleet_utilization_rate

    # print("dictionary_41999", minimum_cycle_price_dict)
    # Merge the original dictionary with calculated market adjustments
    updated_item = {**dictionary, **minimum_cycle_price_dict}
    # print("updated_item", updated_item)
    data1.append(updated_item)
    # print("data1", data1)
    return data1

def calculate_minimum_cycle_revenues(dictionary):
    total_revenues = dictionary['minimum_total_offering_revenues']
    cycle1_revenues = total_revenues * 0.29
    cycle2_revenues = total_revenues * 0.26
    cycle3_revenues = total_revenues * 0.23
    cycle4_revenues = total_revenues * 0.22
    dictionary['minimum_cycle1_revenues'] = cycle1_revenues
    dictionary['minimum_cycle2_revenues'] = cycle2_revenues
    dictionary['minimum_cycle3_revenues'] = cycle3_revenues
    dictionary['minimum_cycle4_revenues'] = cycle4_revenues


def life_cycle_based_calculations(list_of_offerings_and_offering_cost):
    shared_costs =  COMMON_CONSTANTS['shared_costs']
    fleet_size = COMMON_CONSTANTS['fleet_size']
    recycling_costs = COMMON_CONSTANTS['recycling_costs'] 
    end_of_life_costs = recycling_costs
    margin_target = COMMON_CONSTANTS['margin_target'] # Assumption to be 10% 
    recycling_revenue = COMMON_CONSTANTS['recycling_revenue']
    end_of_life_revenues = recycling_revenue
    life_cycle_dict = []
    # single_dict = {list_of_dicts[0]}

    for dictionary in list_of_offerings_and_offering_cost:
        print("dictionary", dictionary)        
        total_offering_cost = dictionary['total_offering_cost']
        print("total_offering_cost", total_offering_cost)
        total_costs = Formulas.calculate_total_costs(shared_costs, fleet_size, total_offering_cost, end_of_life_costs)
        print("total_costs", total_costs)
        minimum_total_revenues = Formulas.calculate_minimum_total_revenues(total_costs, margin_target)
        print("minimum_total_revenues", minimum_total_revenues)
        minimum_total_offering_revenues = Formulas.calculate_minimum_total_offering_revenues(minimum_total_revenues, end_of_life_revenues)
        print("minimum_total_offering_revenues_426", minimum_total_offering_revenues)
        dictionary['total_cost'] = total_costs
        # dictionary['minimum_total_revenues'] = minimum_total_revenues
        dictionary['minimum_total_offering_revenues'] = minimum_total_offering_revenues
        calculate_minimum_cycle_revenues(dictionary)
        minimum_cycle_price_dict = calculate_minimum_cycle_prices(dictionary)
        print("465 ki minimum_cycle_price_dict", minimum_cycle_price_dict)
        life_cycle_dict.append(minimum_cycle_price_dict[0])
        # list_of_offerings_and_offering_cost.update(minimum_cycle_price_dict)
    print("467 minimum_cycle_price_dict", len(life_cycle_dict))
    return life_cycle_dict


def calculate_suggested_cycle_price(list_of_offerings_and_offering_cost_with_mkt_adjustment):
    # Suggested_Cycle_Price = {}
    for dictionary in list_of_offerings_and_offering_cost_with_mkt_adjustment:
        # print("dictionary", dictionary)
        # Initialize variables to store market_adjustment values for each cycle
        market_adjustment_cycle1 = 0
        market_adjustment_cycle2 = 0
        market_adjustment_cycle3 = 0
        market_adjustment_cycle4 = 0
        
        # Iterate through dictionary items and extract market_adjustment values for each cycle
        for key, value in dictionary.items():
        
            if key.startswith('market_adjustment_Cycle'):
                # print("key, value", key,value)
                cycle_number = key.split(':')[0]
                # print("cycle_number", cycle_number)
                if cycle_number == 'market_adjustment_Cycle1':
                    market_adjustment_cycle1 = value
                    # print("market_adjustment_cycle1", market_adjustment_cycle1, value)
                elif cycle_number == 'market_adjustment_Cycle2':
                    market_adjustment_cycle2 = value
                elif cycle_number == 'market_adjustment_Cycle3':
                    market_adjustment_cycle3 = value
                elif cycle_number == 'market_adjustment_Cycle4':
                    market_adjustment_cycle4 = value
        
    # Calculate suggested_cycle_price based on the given formula
        suggested_cycle_price_1 = dictionary['minimum_cycle1_price'] + market_adjustment_cycle1
        # print("dictionary['minimum_cycle1_price']", dictionary['minimum_cycle1_price'], market_adjustment_cycle1, suggested_cycle_price_1)
        suggested_cycle_price_2 = dictionary['minimum_cycle2_price'] + market_adjustment_cycle2
        suggested_cycle_price_3 = dictionary['minimum_cycle3_price'] + market_adjustment_cycle3
        suggested_cycle_price_4 = dictionary['minimum_cycle4_price'] + market_adjustment_cycle4
    
        # Add the calculated values to the dictionary
        dictionary['suggested_cycle1_price'] = suggested_cycle_price_1
        dictionary['suggested_cycle2_price'] = suggested_cycle_price_2
        dictionary['suggested_cycle3_price'] = suggested_cycle_price_3
        dictionary['suggested_cycle4_price'] = suggested_cycle_price_4

    # print("list_of_offerings_and_offering_cost_with_mkt_adjustment", list_of_offerings_and_offering_cost_with_mkt_adjustment)
    # print("Suggested_Cycle_Price_dictionary", Suggested_Cycle_Price)
    return list_of_offerings_and_offering_cost_with_mkt_adjustment

# Function to calculate the total value for a dictionary
def calculate_total_value(dictionary):
    return dictionary['suggested_cycle1_price'] + dictionary['suggested_cycle2_price'] + dictionary['suggested_cycle3_price'] + dictionary['suggested_cycle4_price']

def calculate_revenue(suggested_cycle_price_dict):
    for entry in suggested_cycle_price_dict:
        print("one_item", entry)
        print("entry_suggested_cycle1_price", entry['suggested_cycle1_price'], entry['cycle1_fleet_utilization_rate'])
        entry['revenue_cycle1'] = entry['suggested_cycle1_price'] * 24 * entry['cycle1_fleet_utilization_rate']
        print("entry_revenue_cycle1", entry['revenue_cycle1'])
        entry['revenue_cycle2'] = entry['suggested_cycle2_price'] * 24 * entry['cycle2_fleet_utilization_rate']
        entry['revenue_cycle3'] = entry['suggested_cycle3_price'] * 24 * entry['cycle3_fleet_utilization_rate']
        entry['revenue_cycle4'] = entry['suggested_cycle4_price'] * 24 * entry['cycle4_fleet_utilization_rate']
        entry ['life_cycle_total_revenue'] = entry['revenue_cycle1'] + entry['revenue_cycle2'] + entry['revenue_cycle3'] + entry['revenue_cycle4'] + 1701   
        entry['cost_per_cycle1'] = entry['total_cost'] /4
        entry['cost_per_cycle2'] = entry['total_cost'] /4
        entry['cost_per_cycle3'] = entry['total_cost'] /4
        entry['cost_per_cycle4'] = entry['total_cost'] /4

        entry['profit_per_cycle1'] = entry['revenue_cycle1'] - entry['cost_per_cycle1']
        entry['profit_per_cycle2'] = entry['revenue_cycle2'] - entry['cost_per_cycle2']
        entry['profit_per_cycle3'] = entry['revenue_cycle3'] - entry['cost_per_cycle3']
        entry['profit_per_cycle4'] = entry['revenue_cycle4'] - entry['cost_per_cycle4']
        entry['life_cycle_total_profit'] = entry['profit_per_cycle1'] + entry['profit_per_cycle2'] + entry['profit_per_cycle3'] + entry['profit_per_cycle4']

        entry['profit_margin_cycle1'] = round((entry['profit_per_cycle1']/entry['revenue_cycle1'])*100,2)
        entry['profit_margin_cycle2'] = round((entry['profit_per_cycle2']/entry['revenue_cycle2'])*100,2)
        entry['profit_margin_cycle3'] = round((entry['profit_per_cycle3']/entry['revenue_cycle3'])*100,2)
        entry['profit_margin_cycle4'] = round((entry['profit_per_cycle4']/entry['revenue_cycle4'])*100,2)

        entry['life_cycle_total_profit_margin'] = round((entry['life_cycle_total_profit']/ entry['life_cycle_total_revenue'])*100,2)
    print("532_suggested_cycle_price_dict", suggested_cycle_price_dict)
    return suggested_cycle_price_dict

def generate_all_life_cycle_combinations():
    offerings = ['Leasing', 'Subscription', 'Rental']
    all_combinations = []
    list_of_offerings_and_offering_cost = []
    total_cost_per_cycle =[]
    for a in offerings:
        for b in offerings:
            for c in offerings:
                for d in offerings:
                    combination = [
                        {'Cycle1': a, 'Cycle2': b, 'Cycle3': c, 'Cycle4': d}
                    ]
                    all_combinations.append(combination)
    for one_combination in all_combinations:
        # dict1, dict2 = calculate_total_profit(one_combination)

        dict1 = calculate_total_offering_cost(one_combination)
        list_of_offerings_and_offering_cost.append(dict1)
    life_cycle_based_calculations_dict = life_cycle_based_calculations(list_of_offerings_and_offering_cost)

    # print("list_of_offerings_and_offering_cost_497", life_cycle_based_calculations_dict, len(life_cycle_based_calculations_dict))
    
    list_of_offerings_and_offering_cost_with_mkt_adjustment = calculate_market_adjustment(life_cycle_based_calculations_dict)
    print("result_data_492", list_of_offerings_and_offering_cost_with_mkt_adjustment, len(list_of_offerings_and_offering_cost_with_mkt_adjustment))

    suggested_cycle_price_dict = calculate_suggested_cycle_price(list_of_offerings_and_offering_cost_with_mkt_adjustment)
    print("suggested_cycle_price_dict", suggested_cycle_price_dict, len(suggested_cycle_price_dict))
    print("len_len", len(suggested_cycle_price_dict))
    
    dict_with_revenue = calculate_revenue(suggested_cycle_price_dict)
    print("len_len_2", len(dict_with_revenue))

    best_dict = max(suggested_cycle_price_dict, key=lambda x: x['life_cycle_total_profit_margin'])

    # key_function = lambda d: d['suggested_cycle1_price'] + d['suggested_cycle2_price'] + d['suggested_cycle3_price'] + d['suggested_cycle4_price']
    # best_dict = max(suggested_cycle_price_dict, key=key_function)
    print("best_dictionary_new", best_dict)

    # Find the best dictionary based on total value
    best_dictionary = max(suggested_cycle_price_dict, key=calculate_total_value)
    print("best_dictionary_old", best_dictionary)
    # print("total_cost_per_cycle", total_cost_per_cycle)
    # Find the dictionary with the highest 'total' value
    # best_offering_combination = max(list_of_offerings_and_offering_cost, key=lambda x: x['total'])
    # print("best_offering_combination", best_offering_combination)
    return best_dict


@app.route('/fetchComparisionData')
def generate_fetch_comparision_chart():
    profit_dict = {'profit_amount': '+€600/mo', 'profit_percentage': '(+2.5%)'}
    revenue_dict = {'revenue_amount': '+€600/mo', 'revenue_percentage': '(+2.5%)'}
    price_by_cycle_dict = {'cycle1' : {'price_difference': '+€600/mo', 'revenue_percentage': '(+2.5%)'}, 'cycle2:': {'revenue_amount': '+€600/mo', 'revenue_percentage': '(+2.5%)'}}

    response = {
            "profit_dict": profit_dict,
            "revenue_dict": revenue_dict,
            "price_by_cycle_dict": price_by_cycle_dict
        }
    return jsonify(response)


    # categories = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
    # costs = [80, 120, 160, 180]  # Example costs data
    # profits = [50, 80, 60, 90]  # Example profits data
    # plot_user_selected_stacked_bar(categories, costs, profits)
    # plt.savefig('static/user_suggested_utilisation_bar_chart.png')  # Save the chart as an image file
    # print("inside generate fetch comparision_chart")
    # return jsonify(success=True)


def calculate_traditional_utilisation():
    # print("calculate_traditional_utilisation inside")
    remarketing_costs = 4015
    end_of_life_costs = remarketing_costs
    end_of_life_revenue = 20000
    cycle_count = 2 

    traditiona_utilisation_data = {'Cycle1:Leasing': 1750, 'Cycle2:Leasing': 1615,'total_offering_cost': 81059.68, 'total_cost': 76919, 'minimum_total_offering_revenues': 54611,
    'minimum_cycle1_revenues': 32767, 'minimum_cycle2_revenues': 21845, 'minimum_cycle1_price': 1365,
    'minimum_cycle2_price': 958, 'market_adjustment_Cycle1:Leasing': 385,
    'market_adjustment_Cycle2:Leasing': 657,'suggested_cycle_price_1': 1750, 'suggested_cycle_price_2': 1615}
    suggested_cycle_price = {'suggested_cycle_price_1': 1750, 'suggested_cycle_price_2': 1615}
    traditional_utilisation_dict = {'total_cost_per_cycle': 40529.84, 'revenue_per_cycle_1':42000, 'revenue_per_cycle_2': 36822, 'profit_per_cycle_1': 1470.16, 'profit_per_cycle_2': -3707.84, 'profit_per_cycle_3': 0, 'profit_per_cycle_4': 0}
    #End-of-Life Costs = Remarketing Costs [Demo can quote Excel dummy data directly]
    #End-of-Life Revenues = Remarketing Revenue [Demo can quote Excel dummy data directly]
    #Cycle Count = 2 [The traditional business model is assumed to be only 2 cycles (Cycle 1: Leasing; Cycle 2: Leasing) and then End-of-Life (Remarketing), so there are only 2 cycles counted; The Excel has a counting logic to determine how many cycles the vehicle was deployed; The python demo may keep the logic or simply hard reference the number “2” as Cycle Count input for calculating the traditional business model]
    return traditional_utilisation_dict, suggested_cycle_price

@app.route('/fetchTraditionalUtilisationBarChart', methods=['POST'])
def generate_traditional_utilisation_bar_chart():
    try:
        profit_per_cycle = []
        total_cost_per_cycle = []
        costs = []
        traditional_utilisation_dict, suggested_cycle_price = calculate_traditional_utilisation()
        print("traditional_utilisation_dict_594444", traditional_utilisation_dict)
        # data = request.get_json()  # Get JSON data from the request body
        user_selected_graph_data = traditional_utilisation_dict

        if user_selected_graph_data is not None:
            # print("inside if 579")
            profit_per_cycle = [
                user_selected_graph_data['profit_per_cycle_1'],
                user_selected_graph_data['profit_per_cycle_2'],
                user_selected_graph_data['profit_per_cycle_3'],
                user_selected_graph_data['profit_per_cycle_4']
            ]
            # print("5628_profit_per_cycle", profit_per_cycle)
            total_cost_per_cycle = user_selected_graph_data['total_cost_per_cycle']
            costs = [total_cost_per_cycle] * 4  # Repeat total_cost_per_cycle 4 times
            print("total_cost_per_cycle_traditional", total_cost_per_cycle, costs)
            categories = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
            # print("total_cost_per_cycle_583", costs, categories )
            # costs = [100, 150, 120, 180]  # Example costs data
            # profits = [50, 80, 60, 90]  # Example profits data
            # Generate the bar chart using your plot_stacked_bar function
            plot_traditional_user_stacked_bar(categories, costs, profit_per_cycle)
            # print("plot_traditional_user_stacked_bar")
            plt.savefig('static/traditional_utilisation_bar_chart.png')  # Save the chart as an image file
            response = {
            "potential_price_dict": suggested_cycle_price,
        }
            # print("response", response)
            # return jsonify(response)
            return jsonify(True, message='Chart Displayed properly')
        else:
            return jsonify(success=False, message='Invalid or missing graph_data parameter')

    except Exception as e:
        return jsonify(success=False, message='Error: {}'.format(str(e)))

@app.route('/fetchCalculateUserSelectedUtilisationBarChart', methods=['POST'])
def calculate_user_selected_utilisation_bar_chart():
    try:
        profit_per_cycle = []
        total_cost_per_cycle = []
        costs = []
        data = request.get_json()  # Get JSON data from the request body
        print("data_at_576", data)
        user_selected_graph_data = data.get('user_selected_graph_dict', None)  # Extract 'graph_data' from the JSON data
        # print("graph_data_576", user_selected_graph_data)
        if user_selected_graph_data is not None:
            # print("inside if 579")
            profit_per_cycle = [
                user_selected_graph_data['profit_per_cycle1'],
                user_selected_graph_data['profit_per_cycle2'],
                user_selected_graph_data['profit_per_cycle3'],
                user_selected_graph_data['profit_per_cycle4']
            ]
            # print("5788_profit_per_cycle", profit_per_cycle)
            total_cost_per_cycle = user_selected_graph_data['total_cost']
            costs = user_selected_graph_data['total_cost'] # Repeat total_cost_per_cycle 4 times

            categories = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
            # print("total_cost_per_cycle_583", total_cost_per_cycle,costs, categories )
            # costs = [100, 150, 120, 180]  # Example costs data
            # profits = [50, 80, 60, 90]  # Example profits data
            # Generate the bar chart using your plot_stacked_bar function
            plot_calculated_selected_stacked_bar(categories, costs, profit_per_cycle)
            # print("plot_user_selected_stacked_bar")
            plt.savefig('static/calculated_suggested_utilisation_bar_chart.png')  # Save the chart as an image file
            return jsonify(True, message='Chart Displayed properly')
        else:
            return jsonify(success=False, message='Invalid or missing graph_data parameter')

    except Exception as e:
        return jsonify(success=False, message='Error: {}'.format(str(e)))


@app.route('/fetchUserSelectedUtilisationBarChart', methods=['POST'])
def generate_user_selected_utilisation_bar_chart():
    try:
        profit_per_cycle = []
        total_cost_per_cycle = []
        costs = []
        data = request.get_json()  # Get JSON data from the request body
        print("data_at 576", data)
        user_selected_graph_data = data.get('user_selected_graph_dict', None)  # Extract 'graph_data' from the JSON data
        # print("graph_data_576", user_selected_graph_data)
        if user_selected_graph_data is not None:
            # print("inside if 579")
            profit_per_cycle = [
                user_selected_graph_data['profit_per_cycle1'],
                user_selected_graph_data['profit_per_cycle2'],
                user_selected_graph_data['profit_per_cycle3'],
                user_selected_graph_data['profit_per_cycle4']
            ]
            # print("5788_profit_per_cycle", profit_per_cycle)
            total_cost_per_cycle = user_selected_graph_data['total_cost']
            costs = user_selected_graph_data['total_cost']  # Repeat total_cost_per_cycle 4 times

            categories = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
            # print("total_cost_per_cycle_583", total_cost_per_cycle,costs, categories )
            # costs = [100, 150, 120, 180]  # Example costs data
            # profits = [50, 80, 60, 90]  # Example profits data
            # Generate the bar chart using your plot_stacked_bar function
            plot_user_selected_stacked_bar(categories, costs, profit_per_cycle)
            # print("plot_user_selected_stacked_bar")
            plt.savefig('static/user_suggested_utilisation_bar_chart.png')  # Save the chart as an image file
            return jsonify(True, message='Chart Displayed properly')
        else:
            return jsonify(success=False, message='Invalid or missing graph_data parameter')

    except Exception as e:
        return jsonify(success=False, message='Error: {}'.format(str(e)))

@app.route('/fetchSuggestedUtilisationBarChart', methods=['POST'])
def generate_suggested_utilisation_bar_chart():
    try:
        profit_per_cycle = []
        total_cost_per_cycle = []
        costs = []
        data = request.get_json()  # Get JSON data from the request body
        graph_data = data.get('graph_data', None)  # Extract 'graph_data' from the JSON data
        # print("graph_data_576", graph_data)
        if graph_data is not None:
            # print("inside if 579")
            profit_per_cycle = [
                graph_data['profit_per_cycle1'],
                graph_data['profit_per_cycle2'],
                graph_data['profit_per_cycle3'],
                graph_data['profit_per_cycle4']
            ]
            # print("profit_per_cycle_589", profit_per_cycle)
            total_cost_per_cycle = graph_data['total_cost']
            costs = graph_data['total_cost']  # Repeat total_cost_per_cycle 4 times

            categories = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"]
            # print("total_cost_per_cycle_590", total_cost_per_cycle,costs, categories )
            # costs = [100, 150, 120, 180]  # Example costs data
            # profits = [50, 80, 60, 90]  # Example profits data
            # Generate the bar chart using your plot_stacked_bar function
            plot_stacked_bar(categories, costs, profit_per_cycle)
            plt.savefig('static/suggested_utilisation_bar_chart.png')  # Save the chart as an image file
            return jsonify(True, message='Chart Displayed properly')
        else:
            return jsonify(success=False, message='Invalid or missing graph_data parameter')

    except Exception as e:
        return jsonify(success=False, message='Error: {}'.format(str(e)))


    

    return jsonify(success=True)


@app.route('/your_backend_endpoint', methods=['POST'])
def calculate():
    try:
        # Get data from the incoming JSON request
        data = request.get_json()

        # Process the data as needed (example: print and send a response)
        # print("Received data from frontend:", data)
        user_selected_combination = [data]
        print("user_selected_Combination", user_selected_combination)
        user_selected_cycle_offering_cost = calculate_total_offering_cost(user_selected_combination)
        user_selected_cycle_offering_cost_list = [user_selected_cycle_offering_cost]
        print("user_selected_cycle_offering_cost", user_selected_cycle_offering_cost_list)
        us_life_cycle_based_calculations_dict = life_cycle_based_calculations(user_selected_cycle_offering_cost_list)

        # print("us_life_cycle_based_calculations_dict", us_life_cycle_based_calculations_dict, len(us_life_cycle_based_calculations_dict))
    
        us_list_of_offerings_and_offering_cost_with_mkt_adjustment = calculate_market_adjustment(us_life_cycle_based_calculations_dict)
        # print("us_list_of_offerings_and_offering_cost_with_mkt_adjustment_629", us_list_of_offerings_and_offering_cost_with_mkt_adjustment, len(us_list_of_offerings_and_offering_cost_with_mkt_adjustment))

        us_suggested_cycle_price_dict = calculate_suggested_cycle_price(us_list_of_offerings_and_offering_cost_with_mkt_adjustment)
        # print("us_suggested_cycle_price_dict", us_suggested_cycle_price_dict)

        dict_with_revenue = calculate_revenue(us_suggested_cycle_price_dict)
        print("dict_with_revenue_us", dict_with_revenue)

        user_requested_combination = dict_with_revenue[0]
        # # print("user_requested_combination", user_requested_combination)
        # total_cost_per_cycle = user_requested_combination['total_cost'] / 4
        # user_graph_dict = {
        #     'total_cost_per_cycle': total_cost_per_cycle,
        # }
        # revenue_per_cycle = {}
        # for key in user_requested_combination.keys():
        #     if key.startswith('Cycle'):
        #         cycle_number, offering_type = key.split(':')[0], key.split(':')[1]  # Extract cycle_number and offering_type
        #         if offering_type in LIFE_CYCLE_CONSTANTS:
        #             fleet_utilization_rate = LIFE_CYCLE_CONSTANTS[offering_type][cycle_number]['fleet_utilization_rate']
        #             suggested_cycle_price = user_requested_combination[f'suggested_cycle_price_{cycle_number[-1]}']
        #             revenue_per_cycle[f'revenue_per_cycle_{cycle_number[-1]}'] = suggested_cycle_price * 24 * fleet_utilization_rate

        # # Create graph_Dict and add revenue_per_cycle values to it
        # for key, value in revenue_per_cycle.items():
        #     user_graph_dict[key] = value
        # # print("657_user_graph_dict", user_graph_dict)
        # profit_per_cycle = {}

        # for i in range(1, 5):
        #     revenue_key = f'revenue_per_cycle_{i}'
        #     profit_key = f'profit_per_cycle_{i}'
        #     profit_per_cycle[profit_key] = user_graph_dict[revenue_key] - user_graph_dict['total_cost_per_cycle']
        #     # print("revenue_key_1", revenue_key, profit_key, user_graph_dict[revenue_key], user_graph_dict['total_cost_per_cycle'])

        # # Add profit_per_cycle values to the input dictionary
        # user_graph_dict.update(profit_per_cycle)
        # print("user_graph_dict", user_graph_dict)
        vin = '1BNEK13ZX3R298984'
        user_requested_vehicle_lifecycle_utilization, user_requested_suggested_price_dict, competitor_pricing = suggested_vehicle_lifecycle_utilization_top_row(user_requested_combination, vin)
        print("671", user_requested_vehicle_lifecycle_utilization)
        sv_lifecycle_utilization = user_requested_vehicle_lifecycle_utilization.get(vin, None)
        print("sv_lifecycle_utilization", sv_lifecycle_utilization, user_requested_suggested_price_dict,competitor_pricing)
        response = {
            "suggested_price_dict": user_requested_suggested_price_dict,
            "competitor_pricing": competitor_pricing,
            "user_selected_graph_dict": user_requested_combination
        }
        # print("response", response)
        #     return jsonify(response)
        # else:
        #     return jsonify(error="Vehicle not found")

        # Here you can perform calculations or any other processing with the received data
        # ...

        # Sending a response back to the frontend

        return jsonify(response)

    except Exception as e:
        # Handle exceptions if necessary
        error_message = str(e)
        return jsonify({"error": error_message, "status": "error"}), 500

def extract_cycle_values(input_dict):
    """
    Extracts values associated with keys like 'CycleX:' and stores them in a dictionary.

    Args:
        input_dict (dict): Input dictionary with dynamically generated keys.

    Returns:
        dict: Dictionary containing extracted values with keys 'Cycle1', 'Cycle2', 'Cycle3', etc.
    """
    # Initialize an empty dictionary to store the extracted values
    suggested_vehicle_lifecycle_utilization = {}

    # Extract values for keys with the format 'CycleX:'
    for key, value in input_dict.items():
        if key.startswith('Cycle'):
            cycle_number, offering_type = key.split(':')
            if offering_type in ['Rental', 'Subscription', 'Leasing']:
                suggested_vehicle_lifecycle_utilization[cycle_number] = offering_type
    
    # Extract cycle numbers and corresponding values (rounded to 2 decimal places)
    cycle_numbers = ['cycle1', 'cycle2', 'cycle3', 'cycle4']
    values = [round(input_dict[f'Cycle{i}:Rental'], 2) for i in range(1, 5)]

    # Create suggested_price_dict as a flat dictionary with rounded values
    suggested_price_dict = {cycle_numbers[i]: values[i] for i in range(len(cycle_numbers))}

    # Print the new dictionary
    # print("suggested_price_dict:")
    # print(suggested_price_dict)

    return suggested_vehicle_lifecycle_utilization, suggested_price_dict

def calculate_total_cost_for__best_offering_combination(best_offering_combination):
    for key in best_offering_combination.keys():
        if key.startswith('Cycle'):
            cycle_number, offering_type = key.split(':')
            if offering_type == 'Rental':
                # print("cycle_number", cycle_number, offering_type)
                life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(cycle_number, 'Rental')
                # print("total_costs", total_costs, suggested_price)
            elif offering_type == 'Leasing':
                # print("cycle_number",cycle_number, offering_type)
                life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(cycle_number, 'Leasing')
                # print("total_costs", total_costs, suggested_price)

            elif offering_type == 'Subscription': 
                # print("cycle_number", cycle_number, offering_type)
                life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(cycle_number, 'Subscription')
                # print("total_costs", total_costs, suggested_price)
    
    return total_costs


def suggested_vehicle_lifecycle_utilization_top_row(best_offering_combination, vin):
    suggested_vehicle_lifecycle_utilization = {}
    print("best_offering_combination_757", best_offering_combination)
    # Iterate through the input dictionary and construct the desired dictionary
    cycle_mapping = {}
    suggested_price_dict = {}
    competitor_pricing = {}
    for key, value in best_offering_combination.items():
        print("key, value", key, value)
        if key.startswith('Cycle'):
            cycle_number, offering_type = key.split(':')
            print("cycle_number", cycle_number, offering_type)
            suggested_price_value = f'suggested_{cycle_number.lower()}_price'
            print("suggested_price_value", suggested_price_value)
            print("best_offering_combination[suggested_price_value]", best_offering_combination[suggested_price_value])
            cycle_mapping[cycle_number] = offering_type
            suggested_price_dict[cycle_number] = best_offering_combination[suggested_price_value] 
            competitor_pricing[cycle_number] = LIFE_CYCLE_CONSTANTS[offering_type][cycle_number]['average_real_time_competitor_price']

            # Add the values corresponding to Cycle1, Cycle2, Cycle3, Cycle4
            if len(cycle_mapping) == 4:
                break
    # print("competitor_pricing_709", competitor_pricing)
    suggested_price_rounded_dict = {key: round(value, 2) for key, value in suggested_price_dict.items()}
    # print("suggested_price_rounded_dict", suggested_price_rounded_dict)

    # Create the final dictionary with the specified key
    suggested_vehicle_lifecycle_utilization[vin] = cycle_mapping
    
    return suggested_vehicle_lifecycle_utilization, suggested_price_rounded_dict, competitor_pricing

# def suggested_price_dict_modifications(best_offering_combination):

@app.route('/get_vehicle_details', methods=['POST'])
def get_vehicle_details():
    # print("inside vehicle details")
    data = request.get_json()  # Access JSON data from the request
    # print("data", data)
    vin = data.get('vin', '')  # Get the VIN number from the JSON data

    # print("vin", vin)
    vehicle_info = vehicle_details.get(vin, None)
    # print("vehicle_info", vehicle_info)
    if vehicle_info:
        best_offering_combination = generate_all_life_cycle_combinations()
        print("best_offering_combination", best_offering_combination)
        suggested_vehicle_lifecycle_utilization, suggested_price_dict, competitor_pricing = suggested_vehicle_lifecycle_utilization_top_row(best_offering_combination, vin)
        # print("suggested_price_dict", suggested_price_dict, suggested_vehicle_lifecycle_utilization, competitor_pricing)
        sv_lifecycle_utilization = suggested_vehicle_lifecycle_utilization.get(vin, None)
        # print("sv_lifecycle_utilization", sv_lifecycle_utilization)
        potential_price_dict = {'Cycle1': 1750, 'Cycle2': 1615, 'Cycle3': 0, 'Cycle4': 0}
        traditional_total_revenue = 108831
        traditional_total_cost = 76919
        traditional_total_profit = 31912
        price_by_cycle_dict = {}
        cycles_to_exclude = ['Cycle3', 'Cycle4']

        for cycle in suggested_price_dict:
            if cycle not in cycles_to_exclude:
                # Traditional - Suggested 
                price_difference = round(potential_price_dict[cycle] - suggested_price_dict[cycle],2)
                profit_percentage = round(((price_difference / suggested_price_dict[cycle]) * 100 if suggested_price_dict[cycle] != 0 else 0),2)

                price_by_cycle_dict[cycle] = {
                    'price_difference': f'+€{price_difference}',
                    'profit_percentage': f'(+{profit_percentage}%)'
                }
            # print("price_by_cycle_dict", price_by_cycle_dict)
        # 1701 for end of life recycling value
        total_revenue = (best_offering_combination['life_cycle_total_revenue'] /96)
        traditional_total_revenue = traditional_total_revenue/48
        # print("total_revenue", total_revenue, traditional_total_revenue)
        # revenue_dict = {'revenue_amount': '+€600/mo', 'revenue_percentage': '(+2.5%)'}
        revenue_amount = round((total_revenue - traditional_total_revenue),2)
        revenue_percentage = round((((total_revenue - traditional_total_revenue)/traditional_total_revenue)*100 ),2)

        revenue_dict = {'revenue_amount': f'€{revenue_amount}/mo.', 'revenue_percentage': f'({revenue_percentage}%)'}
        # print("revenue_dict_1054", revenue_dict)
        total_cost = best_offering_combination['total_cost']
        total_cost_per_month = total_cost/96
        traditional_total_cost_per_month = traditional_total_cost/48
        # print("total_cost_1049", total_cost, total_cost_per_month, traditional_total_cost_per_month)

        total_profit = round((total_revenue - total_cost_per_month),2)
        traditional_total_profit = round((traditional_total_revenue - traditional_total_cost_per_month),2)
        # print( "Final_lelo_sab", total_revenue, total_cost, total_profit, traditional_total_profit) 
        # profit_dict = {'profit_amount': '+€600/mo', 'profit_percentage': '(+2.5%)'}
        calculated_profit_amount_per_month = round((total_profit - traditional_total_profit),2)
        # traditional_total_profit_per_month = round(traditional_total_profit/24,2)
        calculated_profit_percentage = round((calculated_profit_amount_per_month/traditional_total_profit)*100,2)
        profit_dict = {'profit_amount' : f'€{calculated_profit_amount_per_month}/mo.', 'profit_percentage': f'({calculated_profit_percentage}%)'}
        # print("profit_dict", profit_dict)
        response = {
            "vehicle_info": vehicle_info,
            "suggested_vehicle_lifecycle_utilization": sv_lifecycle_utilization,
            "suggested_price_dict": suggested_price_dict,
            "graph_dict": best_offering_combination,
            "competitor_pricing": competitor_pricing,
            "user_selected_graph_dict": best_offering_combination,
            "potential_price_dict": potential_price_dict,
            "price_by_cycle_dict": price_by_cycle_dict,
            "revenue_dict": revenue_dict,
            "profit_dict": profit_dict
        }
        # print("response", response)
        return jsonify(response)
    else:
        return jsonify(error="Vehicle not found")


if __name__ == '__main__':
    app.run(debug=True, port=8000)