from app import get_vehicle_details, generate_all_life_cycle_combinations, calculate_common_profit_formulas, calculate_total_offering_cost, life_cycle_based_calculations, calculate_market_adjustment
import Formulas
import constants
from constants import OFFERING_CONSTANTS, LIFE_CYCLE_CONSTANTS, LEASING_YEARS_TO_CYCLE, COMMON_CONSTANTS, INDEPENDENT_OF_OFFERING_CONSTANTS

one_combination = [{'Cycle1': 'Leasing', 'Cycle2': 'Leasing', 'Cycle3': 'Subscription', 'Cycle4': 'Rental'}]

best_offering_combination = generate_all_life_cycle_combinations()
print("best_offering_combination", best_offering_combination)
# dict1 = calculate_total_offering_cost(one_combination)
# sample = [{'Cycle1:Leasing': 1477.4399999999998, 'Cycle2:Leasing': 3793.560000000002, 'Cycle3:Subscription': 10843.960000000001, 'Cycle4:Rental': 23775.719999999998, 'total_offering_cost': 39890.68}]
# life_cycle_based_calculations_dict = life_cycle_based_calculations(sample)
# print("life_cycle_based_calculations_dict_sample", life_cycle_based_calculations_dict)
# print("dict1", dict1)
# life_cycle, type_of_offering, leasing_suggested_price = calculate_common_profit_formulas('Cycle2', 'Leasing')
# print("dict1",life_cycle, type_of_offering, leasing_suggested_price)
cycle_profit = {}
total_offering_cost_per_cycle = 0
cycle_offering_cost = {}

shared_costs =  COMMON_CONSTANTS['shared_costs']
fleet_size = COMMON_CONSTANTS['fleet_size']
recycling_costs = COMMON_CONSTANTS['recycling_costs'] 
end_of_life_costs = recycling_costs
margin_target = COMMON_CONSTANTS['margin_target'] # Assumption to be 10% 
recycling_revenue = COMMON_CONSTANTS['recycling_revenue']
end_of_life_revenues = recycling_revenue


# # Your list of dictionaries
# # Your list of dictionaries
# data = [{'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Subscription': 30963.439999999995, 'Cycle4:Rental': 33245.84, 'total_offering_cost': 52111.96000000001, 'minimum_total_offering_revenues': 131311.20500000002, 'minimum_cycle1_revenues': 38080.24945, 'minimum_cycle2_revenues': 34140.91330000001, 'minimum_cycle3_revenues': 30201.577150000005, 'minimum_cycle4_revenues': 28888.465100000005, 'minimum_cycle1_price': 1586.6770604166668, 'minimum_cycle2_price': 1497.408478070176, 'minimum_cycle3_price': 1634.284477813853, 'minimum_cycle4_price': 2006.1434097222227, 'market_adjustment_Cycle1:Leasing': 163.3229395833332, 'market_adjustment_Cycle2:Leasing': 144.9619458333328, 'market_adjustment_Cycle3:Leasing': -73.32749569805218, 'market_adjustment_Cycle4:Leasing': -444.9147277777782},
#         {'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Subscription': 37387.399999999994, 'total_offering_cost': 56253.520000000004, 'minimum_total_offering_revenues': 135866.921, 'minimum_cycle1_revenues': 39401.40709, 'minimum_cycle2_revenues': 35325.39946, 'minimum_cycle3_revenues': 31249.39183, 'minimum_cycle4_revenues': 29890.72262, 'minimum_cycle1_price': 1641.7252954166668, 'minimum_cycle2_price': 1549.3596254385966, 'minimum_cycle3_price': 1690.9844063852815, 'minimum_cycle4_price': 2075.7446263888887, 'market_adjustment_Cycle1:Leasing': 108.27470458333323, 'market_adjustment_Cycle2:Leasing': 95.60835583333323, 'market_adjustment_Cycle3:Leasing': -122.65643355519494, 'market_adjustment_Cycle4:Subscription': -420.595701111111}]

# life_cycle_based_calculations_dict =  [{'Cycle1:Leasing': 1477.4399999999998, 'Cycle2:Rental': 23739.04, 'Cycle3:Rental': 23045.679999999997, 'Cycle4:Rental': 23775.719999999998, 'total_offering_cost': 72037.87999999999, 'total_cost': 140845.672, 'minimum_total_offering_revenues': 153229.717, 'minimum_cycle1_revenues': 44436.61793, 'minimum_cycle2_revenues': 39839.72642, 'minimum_cycle3_revenues': 35242.834910000005, 'minimum_cycle4_revenues': 33710.53774, 'minimum_cycle1_price': 1851.5257470833333, 'minimum_cycle2_price': 2553.8286166666667, 'minimum_cycle3_price': 2330.8753247354502, 'minimum_cycle4_price': 2341.0095652777777}]
# list_of_offerings_and_offering_cost_with_mkt_adjustment = calculate_market_adjustment(life_cycle_based_calculations_dict)
# list_of_offerings_and_offering_cost = life_cycle_based_calculations([{'Cycle1:Leasing': 1477.4399999999998, 'Cycle2:Rental': 23739.04, 'Cycle3:Rental': 23045.679999999997, 'Cycle4:Rental': 23775.719999999998, 'total_offering_cost': 72037.87999999999}])
# cycle_offering_cost = calculate_total_offering_cost([{'Cycle1': 'Leasing', 'Cycle2': 'Rental', 'Cycle3': 'Rental', 'Cycle4': 'Rental'}])
# print("list_of_offerings_and_offering_cost_with_mkt_adjustment", list_of_offerings_and_offering_cost_with_mkt_adjustment)
# {'Cycle1': 'Leasing', 'Cycle2': 'Subscription', 'Cycle3': 'Rental', 'Cycle4': 'Subscription'}
# offering_cost = calculate_common_profit_formulas('Cycle2', 'Rental')
# print("offering_cost", offering_cost)
# # Iterate through the list of dictionaries
# for dictionary in data:
#     # Initialize variables to store market_adjustment values for each cycle
#     market_adjustment_cycle1 = 0
#     market_adjustment_cycle2 = 0
#     market_adjustment_cycle3 = 0
#     market_adjustment_cycle4 = 0
    
#     # Iterate through dictionary items and extract market_adjustment values for each cycle
#     for key, value in dictionary.items():
        
#         if key.startswith('market_adjustment_Cycle'):
#             print("key, value", key,value)
#             cycle_number = key.split(':')[0]
#             print("cycle_number", cycle_number)
#             if cycle_number == 'market_adjustment_Cycle1':
#                 market_adjustment_cycle1 = value
#                 print("market_adjustment_cycle1", market_adjustment_cycle1, value)
#             elif cycle_number == 'market_adjustment_Cycle2':
#                 market_adjustment_cycle2 = value
#             elif cycle_number == 'market_adjustment_Cycle3':
#                 market_adjustment_cycle3 = value
#             elif cycle_number == 'market_adjustment_Cycle4':
#                 market_adjustment_cycle4 = value
    
#     # Calculate suggested_cycle_price based on the given formula
#     suggested_cycle_price_1 = dictionary['minimum_cycle1_price'] - market_adjustment_cycle1
#     print("dictionary['minimum_cycle1_price']", dictionary['minimum_cycle1_price'], market_adjustment_cycle1, suggested_cycle_price_1)
#     suggested_cycle_price_2 = dictionary['minimum_cycle2_price'] - market_adjustment_cycle2
#     suggested_cycle_price_3 = dictionary['minimum_cycle3_price'] - market_adjustment_cycle3
#     suggested_cycle_price_4 = dictionary['minimum_cycle4_price'] - market_adjustment_cycle4
    
#     # Add the calculated values to the dictionary
#     dictionary['suggested_cycle_price_1'] = suggested_cycle_price_1
#     dictionary['suggested_cycle_price_2'] = suggested_cycle_price_2
#     dictionary['suggested_cycle_price_3'] = suggested_cycle_price_3
#     dictionary['suggested_cycle_price_4'] = suggested_cycle_price_4

# Now data list contains the calculated suggested_cycle_price for each dictionary in the list


# # Iterate through the list of dictionaries
# for dictionary in data:
#     for key, value in dictionary.items():
#         if key.startswith('market_adjustment_Cycle'):
#             market_adjustment_Cycle = key.split(':')[0]
#             print("market_adjustment_Cycle", market_adjustment_Cycle)
            
    
    # suggested_cycle_price_1 = dictionary['minimum_cycle1_price'] - dictionary['market_adjustment_Cycle1:Leasing']
    # suggested_cycle_price_2 = dictionary['minimum_cycle2_price'] - dictionary['market_adjustment_Cycle2:Leasing']
    # suggested_cycle_price_3 = dictionary['minimum_cycle3_price'] - dictionary['market_adjustment_Cycle3:Leasing']
    # suggested_cycle_price_4 = dictionary['minimum_cycle4_price'] - dictionary['market_adjustment_Cycle4:Leasing']
    
    # # Add the calculated values to the dictionary
    # dictionary['suggested_cycle_price_1'] = suggested_cycle_price_1
    # dictionary['suggested_cycle_price_2'] = suggested_cycle_price_2
    # dictionary['suggested_cycle_price_3'] = suggested_cycle_price_3
    # dictionary['suggested_cycle_price_4'] = suggested_cycle_price_4

# Print the updated list of dictionaries
# print(data)




# Your list of dictionaries
# Input list of dictionaries
# data = [
#     {'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Leasing': 33245.84, 'total_offering_cost': 23, 'minimum_total_offering_revenues': 74013.349},
#     {'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Subscription': 37387.399999999994, 'total_offering_cost': 43, 'minimum_total_offering_revenues': 74035.349}
# ]

# # Iterate through the list of dictionaries
# for item in data:
#     # Calculate minimum_total_offering_revenues for each cycle based on given percentages
#     total_revenues = item['minimum_total_offering_revenues']
#     cycle1_revenues = total_revenues * 0.29
#     cycle2_revenues = total_revenues * 0.26
#     cycle3_revenues = total_revenues * 0.23
#     cycle4_revenues = total_revenues * 0.22

#     # Update the dictionary with calculated values
#     item['minimum_total_offering_revenues_cycle1'] = cycle1_revenues
#     item['minimum_total_offering_revenues_cycle2'] = cycle2_revenues
#     item['minimum_total_offering_revenues_cycle3'] = cycle3_revenues
#     item['minimum_total_offering_revenues_cycle4'] = cycle4_revenues

# # Print the updated list of dictionaries
# print(data)

# Your updated list of dictionaries
# Your updated list of dictionaries
# Your updated list of dictionaries
# Your updated list of dictionaries
# Your updated list of dictionaries
# Your updated list of dictionaries
# Your updated list of dictionaries
# data = [
#     {'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Subscription': 30963.439999999995, 'Cycle4:Subscription': 37387.399999999994, 'total_offering_cost': 23, 'minimum_total_offering_revenues': 74013.349, 'minimum_cycle1_revenues': 21463.871209999998, 'minimum_cycle2_revenues': 19243.47074, 'minimum_cycle3_revenues': 17023.07027, 'minimum_cycle4_revenues': 16282.93678, 'minimum_cycle1_price': 894.3279670833332, 'minimum_cycle2_price': 844.0118745614036, 'minimum_cycle3_price': 921.1618111471862, 'minimum_cycle4_price': 1130.7594986111112},
#     {'Cycle1:Leasing': 5663.04, 'Cycle2:Rental': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Subscription': 37387.399999999994, 'total_offering_cost': 43, 'minimum_total_offering_revenues': 74035.349, 'minimum_cycle1_revenues': 21470.25121, 'minimum_cycle2_revenues': 19249.190740000002, 'minimum_cycle3_revenues': 17028.13027, 'minimum_cycle4_revenues': 16287.77678, 'minimum_cycle1_price': 894.5938004166666, 'minimum_cycle2_price': 844.262751754386, 'minimum_cycle3_price': 921.4356206709957, 'minimum_cycle4_price': 1131.0956097222222}
# ]

# # LIFE_CYCLE_CONSTANTS dictionary
# LIFE_CYCLE_CONSTANTS = {
#     'Leasing': {
#         'Cycle1': {'average_real_time_competitor_price': 1750},
#         'Cycle2': {'average_real_time_competitor_price': 1650},
#         'Cycle3': {'average_real_time_competitor_price': 1550},
#         'Cycle4': {'average_real_time_competitor_price': 1450}
#     },
#     'Subscription': {
#         'Cycle1': {'average_real_time_competitor_price': 1850},
#         'Cycle2': {'average_real_time_competitor_price': 1750},
#         'Cycle3': {'average_real_time_competitor_price': 1650},
#         'Cycle4': {'average_real_time_competitor_price': 1550}
#     },
#     'Rental': {
#         'Cycle1': {'average_real_time_competitor_price': 2800},
#         'Cycle2': {'average_real_time_competitor_price': 2600},
#         'Cycle3': {'average_real_time_competitor_price': 2350},
#         'Cycle4': {'average_real_time_competitor_price': 2100}
#     }
# }

# INDEPENDENT_OF_OFFERING_CONSTANTS = {
#     'price_adjustment_slicer': {

#         'Cycle1': 1.00,
#         'Cycle2': 0.95,
#         'Cycle3': 0.87,
#         'Cycle4': 0.80,  
# }
# }

# Create a new list to store dictionaries with market adjustments
# result_data = []

# Iterate through the list of dictionaries and calculate market adjustments
# Iterate through the list of dictionaries and calculate market adjustments
# for item in data:
#     market_adjustments = {}
#     for key, value in item.items():
#         if key.startswith('Cycle'):
#             cycle_number, offering_type = key.split(':')[0], key.split(':')[1]  # Extract cycle_number and offering_type
#             print("cycle_number", cycle_number, offering_type)
#             if offering_type in LIFE_CYCLE_CONSTANTS and cycle_number in LIFE_CYCLE_CONSTANTS[offering_type]:
#                 print("inside if")
#                 competitor_price = LIFE_CYCLE_CONSTANTS[offering_type][cycle_number]['average_real_time_competitor_price']
#                 print("competitor_price", competitor_price)
#                 market_adjustment_key = f'market_adjustment_{key}'
#                 cycle_revenues_key = f'minimum_{cycle_number.lower()}_price'
#                 print("cycle_revenues_key", cycle_revenues_key)
#                 print("item[cycle_revenues_key]", item[cycle_revenues_key])
#                 print("INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number]", INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number])
#                 market_adjustment = (competitor_price - item[cycle_revenues_key]) * INDEPENDENT_OF_OFFERING_CONSTANTS['price_adjustment_slicer'][cycle_number]

#                 market_adjustments[market_adjustment_key] = market_adjustment

#     # Merge the original dictionary with calculated market adjustments
#     updated_item = {**item, **market_adjustments}
#     result_data.append(updated_item)

# Print the updated list of dictionaries with market adjustments






# list_of_offerings_and_offering_cost = [{'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Leasing': 33245.84, 'total_offering_cost': 23},
#                                        {'Cycle1:Leasing': 5663.04, 'Cycle2:Leasing': -17760.35999999999, 'Cycle3:Leasing': 30963.439999999995, 'Cycle4:Subscription': 37387.399999999994, 'total_offering_cost': 43}]

# # Assuming shared_costs is a constant value (you need to assign its actual value)
# # shared_costs = 10000  # Replace this with the actual shared_costs value
# def calculate_minimum_total_offering_revenues(dictionary):
#     total_revenues = dictionary['minimum_total_offering_revenues']
#     cycle1_revenues = total_revenues * 0.29
#     cycle2_revenues = total_revenues * 0.26
#     cycle3_revenues = total_revenues * 0.23
#     cycle4_revenues = total_revenues * 0.22
#     dictionary['minimum_cycle1_revenues'] = cycle1_revenues
#     dictionary['minimum_cycle2_revenues'] = cycle2_revenues
#     dictionary['minimum_cycle3_revenues'] = cycle3_revenues
#     dictionary['minimum_cycle4_revenues'] = cycle4_revenues


# def calculate_minimum_cycle_prices(dictionary):
    
#     cycle_duration = COMMON_CONSTANTS['cycle_duration']
#     # fleet_utilization_rate = life_cycle_constants['fleet_utilization_rate']


#     cycle_price_1 = (dictionary['minimum_cycle1_revenues'] / cycle_duration) / 1.00
#     cycle_price_2 = (dictionary['minimum_cycle2_revenues'] / 24) / 0.95
#     cycle_price_3 = (dictionary['minimum_cycle3_revenues'] / 24) / 0.77
#     cycle_price_4 = (dictionary['minimum_cycle4_revenues'] / 24) / 0.60

#     # Update the dictionary with calculated cycle prices
#     dictionary['minimum_cycle_price_1'] = cycle_price_1
#     dictionary['minimum_cycle_price_2'] = cycle_price_2
#     dictionary['minimum_cycle_price_3'] = cycle_price_3
#     dictionary['minimum_cycle_price_4'] = cycle_price_4

# # Calculate total_cost for each dictionary and add it as a new key-value pair
# for dictionary in list_of_offerings_and_offering_cost:
#     total_offering_cost = dictionary['total_offering_cost']    
#     total_costs = Formulas.calculate_total_costs(shared_costs, fleet_size, total_offering_cost, end_of_life_costs)
#     minimum_total_revenues = Formulas.calculate_minimum_total_revenues(total_costs, margin_target)
#     minimum_total_offering_revenues = Formulas.calculate_minimum_total_offering_revenues(minimum_total_revenues, end_of_life_revenues)
#     dictionary['minimum_total_offering_revenues'] = minimum_total_offering_revenues
#     calculate_minimum_total_offering_revenues(dictionary)
#     calculate_minimum_cycle_prices(dictionary)


# # Print the updated list of dictionaries
# print(list_of_offerings_and_offering_cost)


# individual_suggested_prices = []
# print("one_combination", one_combination)
# # print("type of one_combination", type(one_combination))
# for one_combo in one_combination:
#     total_profit = 0
#     print("one_combo", one_combo, len(one_combo))
#     for key, value in one_combo.items():
#         if value == 'Leasing':
#             life_cycle, type_of_offering, leasing_offering_cost = calculate_common_profit_formulas(key, value)
#             cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': leasing_offering_cost})
#             # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
#             total_offering_cost_per_cycle += leasing_offering_cost
#             print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
#         elif value == 'Rental':
#             life_cycle, type_of_offering, rental_offering_cost = calculate_common_profit_formulas(key, value)
#             cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': rental_offering_cost})
#             # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
#             total_offering_cost_per_cycle += rental_offering_cost
#             print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
#         elif value == 'Subscription':
#             life_cycle, type_of_offering, subscription_offering_cost = calculate_common_profit_formulas(key, value)
#             cycle_offering_cost.update({f'{life_cycle}:{type_of_offering}': subscription_offering_cost})
#             # total_costs_per_cycle.update({f'{life_cycle}:{type_of_offering}': total_costs})
#             total_offering_cost_per_cycle += subscription_offering_cost
#             print("total_offering_cost_per_cycle", total_offering_cost_per_cycle)
#     cycle_offering_cost.update({'total_offering_cost_per_cycle': total_offering_cost_per_cycle})
#     print("cycle_offering_cost_update", cycle_offering_cost)



# individual_suggested_prices = []
# print("one_combination", one_combination)
# # print("type of one_combination", type(one_combination))
# for one_combo in one_combination:
#     total_profit = 0
#     print("one_combo", one_combo, len(one_combo))
#     for key, value in one_combo.items():
#         if value == 'Leasing':
#             print("key", key)
#             if key == 'Cycle2':
#                 print("key_value", key, value)
#                 life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(key, value)
#                 print("54_key", key, value)
#                 # total_profit += leasing_profit
#                 print("Rental", life_cycle, type_of_offering, suggested_price, total_costs)
#             pass
#             # life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(key, value)
#             # print("54_key", key, value)
#             # total_profit += leasing_profit
#             # print("leasing_profit", life_cycle, type_of_offering, suggested_price, total_costs)
#             # cycle_profit.update({f'{life_cycle}:{type_of_offering}': leasing_profit})
#             # print("cycle_profit", cycle_profit)
#         elif value == 'Rental':
#             pass
#             # life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(key, value)
#             # print("54_key", key, value)
#             # total_profit += leasing_profit
#             # print("Rental", life_cycle, type_of_offering, suggested_price, total_costs)
#             # life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(key, value)
#             # print("rental_profit", suggested_price)
#             # total_profit += rental_profit
#             # cycle_profit.update({f'{life_cycle}:{type_of_offering}': rental_profit})
#             # print("cycle_profit", cycle_profit)
#         elif value == 'Subscription':
#             pass
#             # life_cycle, type_of_offering, suggested_price, total_costs = calculate_common_profit_formulas(key, value)
#             # print("subscription_profit", total_profit)
#             # total_profit += subscription_profit
#             # cycle_profit.update({f'{life_cycle}:{type_of_offering}': subscription_profit})
#             # print("cycle_profit", cycle_profit)
#         # cycle_profit.update({'total': total_profit})
#         # print("total_profit", total_profit)
#         # print("cycle_profit_final", cycle_profit)

# data_list = [
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Leasing': 2454.4661332777778, 'Cycle4:Leasing': 3103.3893341176463, 'total': 9159.717476398195},
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Leasing': 2454.4661332777778, 'Cycle4:Subscription': 3498.7796879999996, 'total': 9555.107830280547},
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Leasing': 2454.4661332777778, 'Cycle4:Rental': 4756.9647700000005, 'total': 10813.292912280549},
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Subscription': 2763.357776818182, 'Cycle4:Leasing': 3103.3893341176463, 'total': 9468.6091199386},
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Subscription': 2763.357776818182, 'Cycle4:Subscription': 3498.7796879999996, 'total': 9863.999473820953},
#     {'Cycle1:Leasing': 1750.0, 'Cycle2:Leasing': 1851.8620090027703, 'Cycle3:Subscription': 2763.357776818182, 'Cycle4:Rental': 4756.9647700000005, 'total': 11122.184555820953}
# ]

# # Find the dictionary with the highest 'total' value
# best_dict = max(data_list, key=lambda x: x['total'])

# print("Best Dictionary:")
# print(best_dict)
# Example dictionary with dynamically generated keys
# Example dictionary with dynamically generated keys
# rental_dict = {
#     'Cycle1:Rental': 2800.0,
#     'Cycle2:Subscription': 2972.293053157895,
#     'Cycle3:Rental': 3829.9733980158726,
#     'Cycle4:Rental': 4756.9647700000005,
#     'total': 14359.231221173768
# }

# # Initialize an empty dictionary to store the extracted values
# suggested_vehicle_lifecycle_utilization = {}

# # Extract values for keys with the format 'CycleX:'
# for key, value in rental_dict.items():
#     if key.startswith('Cycle'):
#         cycle_number, offering_type = key.split(':')
#         if offering_type in ['Rental', 'Subscription', 'Leasing']:
#             suggested_vehicle_lifecycle_utilization[cycle_number] = offering_type

# # Print the extracted values
# print("suggested_vehicle_lifecycle_utilization:")
# print(suggested_vehicle_lifecycle_utilization)

# Input dictionary with dynamically generated keys
# Input dictionary with dynamically generated keys
# Input dictionary with dynamically generated keys
input_dict = {
    'Cycle1:Rental': 2800.0,
    'Cycle2:Rental': 2972.293053157895,
    'Cycle3:Rental': 3829.9733980158726,
    'Cycle4:Rental': 4756.9647700000005,
    'total': 14359.231221173768
}

# # Extract cycle numbers and corresponding values (rounded to 2 decimal places)
# cycle_numbers = ['cycle1', 'cycle2', 'cycle3', 'cycle4']
# values = [round(input_dict[f'Cycle{i}:Rental'], 2) for i in range(1, 5)]

# # Create suggested_price_dict as a flat dictionary with rounded values
# suggested_price_dict = {cycle_numbers[i]: values[i] for i in range(len(cycle_numbers))}

# # Print the new dictionary
# print("suggested_price_dict:")
# print(suggested_price_dict)

# input_dict =  {'Cycle1:Rental': 2800.0, 'Cycle2:Leasing': 2972.293053157895, 'Cycle3:Rental': 3829.9733980158726, 'Cycle4:Rental': 4756.9647700000005, 'total': 14359.231221173768}

# def calculate_common_profit_formulas(cycle_number, offering_type):
#     print("cycle_number", cycle_number)
#     print("offering_type", offering_type)

# for key in input_dict.keys():
#     if key.startswith('Cycle'):
#         cycle_number, offering_type = key.split(':')
#         if offering_type == 'Rental':
#             calculate_common_profit_formulas(cycle_number, offering_type)
#         elif offering_type == 'Leasing':
#             calculate_common_profit_formulas(cycle_number, offering_type)
