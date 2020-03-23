"""
Cookie Clicker Simulator
"""
# import simpleplot

# Used to increase the timeout, if necessary
# import codeskulptor
import math
import provided

# codeskulptor.set_timeout(20)

# import poc_clicker_provided as provided

# Constants
# SIM_TIME = 10000000000.0
SIM_TIME = 100.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self.total_number_of_cookies = 0.0
        self.current_number_of_cookies = 0.0
        self.current_time_sec = 0.0
        self.item_name = None
        self.item_cost = 0.0
        self.current_cps = 1.0
        self.history_list = [(self.current_time_sec, self.item_name, self.item_cost, self.total_number_of_cookies)]

    def __str__(self):
        """
        Return human readable state
        """
        return "\n"  + "current time in sec: " + str(self.current_time_sec) + "\n" \
                     + "current number of cookies: " + str(self.current_number_of_cookies) + "\n" \
                     + "total number of cookies made: " + str(self.total_number_of_cookies) + "\n" \
                     + "current cookie per second: " + str(self.current_cps) + "\n"\
                     + "history list : " + str(self.history_list) + "\n"



    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return str(self.current_number_of_cookies)

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time_sec

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.history_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if cookies > self.current_number_of_cookies and cookies > 0:
            return math.ceil((cookies - self.current_number_of_cookies) / self.current_cps)
        else:
            return 0.0

    def wait(self, time):
        """
        Wait for given amount of time and update state
        appropriately increase the time, the current number of cookies, and the total number of cookies.

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self.current_time_sec += time
            wait_time_cookies = self.current_cps * time
            self.current_number_of_cookies += wait_time_cookies
            self.total_number_of_cookies += wait_time_cookies

        else:
            pass

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        adjust the current number of cookies, the CPS, and add an entry into the history

        Should do nothing if you cannot afford the item
        """
        if self.current_number_of_cookies >= cost:
            self.current_number_of_cookies -= cost
            self.current_cps += additional_cps
            print(self.current_number_of_cookies)
            print(cost)
            tup = (self.current_time_sec, item_name, cost, self.total_number_of_cookies)
            self.history_list.append(tup)
        else:
            pass


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    items_info = build_info.clone()
    game_state = ClickerState()

    t_left = duration - game_state.get_time()
    # why should i use get time instead of calling the instance attributes?׳
    while t_left > 0:
        item_name = strategy(game_state.get_cookies(), game_state.get_cps(), game_state.get_history, t_left, items_info)
        if item_name is None:
            break

        item_cost = items_info.get_cost(item_name)
        additional_cps = items_info.get_cps(item_name)
        # calculate the next time its possible to buy an item and break if you don't have enough time
        time_until_purchase = game_state.time_until(item_cost)
        # if you don't have enough time to wait till the next purchase buy cookies till the end of the simulation
        if time_until_purchase > t_left:
            game_state.current_number_of_cookies += t_left * game_state.get_cps()
            game_state.total_number_of_cookies += t_left * game_state.get_cps()
            break
        # wait until that time and buy the item
        game_state.wait(time_until_purchase)
        # notice you can buy more the one item at once
        game_state.buy_item(item_name, item_cost, additional_cps)
        # update the build info
        items_info.update_item(item_name)
        t_left = duration - game_state.get_time()
    else:
        if item_cost < float(game_state.get_cookies()):
            game_state.buy_item(item_name, item_cost, additional_cps)
            items_info.update_item(item_name)

    return game_state.__str__()

# if you have enough cookies, it is possible to purchase multiple items at the same time step.
# current_salary += int(profit/current_bribe_cost)*SALARY_INCREMENT


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


# def strategy_none(cookies, cps, history, time_left, build_info):
#     """
#     Always return None
#
#     This is a pointless strategy that will never buy anything, but
#     that you can use to help debug your simulate_clicker function.
#     """
#     return None
#
#
def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    strategies_list = build_info.build_items()
    strategy_dict = {}
    for strategy in strategies_list:
        strategy_dict[strategy] = build_info.get_cost(strategy)
    key_min = min(strategy_dict.keys(), key=(lambda k: strategy_dict[k]))
    if (cps*time_left + float(cookies)) < strategy_dict[key_min]:
        return None
    else:
        return key_min


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    strategies_list = build_info.build_items()
    strategy_dict = {}
    for strategy in strategies_list:
        strategy_dict[strategy] = build_info.get_cost(strategy)

    sorted_l = sorted(strategy_dict.items(), key=lambda item: item[1], reverse=True)
    for strategy, cost in sorted_l:
        if (cps * time_left + float(cookies)) >= cost:
            return strategy
    return None


#
#
def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    strategies_list = build_info.build_items()
    info_list = []
    # aims to minimize item_cost/cps
    for strategy in strategies_list:
        # strategy_dict[strategy] = {build_info.get_cost(strategy): build_info.get_cost(strategy)/cps}
        strategy_dict = {"name": strategy, "cost": build_info.get_cost(strategy), "ratio": build_info.get_cost(strategy) / cps}
        info_list.append(strategy_dict)

    # print(info_list)
    ratios_list = [strategy['ratio'] for strategy in info_list]
    min_ratio = None
    while min_ratio is None and len(ratios_list) > 0:
        min_ratio = min(ratios_list)
        for strategy_item in info_list:
            if strategy_item['ratio'] == min_ratio :
                if (cps * time_left + float(cookies)) >= strategy_item['cost']:
                    return strategy_item["name"]
                else:
                    ratios_list.remove(min_ratio)
    else:
        return None


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print(strategy_name, ":", state)

    # Plot total cookies over time
#
#     # Uncomment out the lines below to see a plot of total cookies vs. time
#     # Be sure to allow popups, if you do want to see it
#
#     # history = state.get_history()
#     # history = [(item[0], item[3]) for item in history]
#     # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)
#
#
# def run():
#     """
#     Run the simulator.
#     """
#     run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
#
#     # Add calls to run_strategy to run additional strategies
#     # run_strategy("Cheap", SIM_TIME, strategy_cheap)
#     # run_strategy("Expensive", SIM_TIME, strategy_expensive)
#     # run_strategy("Best", SIM_TIME, strategy_best)
#
#
# # run()

# print("this is the strategy expensive {}" . format(simulate_clicker(provided.BuildInfo(), SIM_TIME,strategy_expensive)))
# print("this is the strategy cheap {}" . format(simulate_clicker(provided.BuildInfo(), SIM_TIME,strategy_cheap)))
# print("this is the strategy broken {}" . format(simulate_clicker(provided.BuildInfo(), SIM_TIME,strategy_cursor_broken)))
# print("this is the strategy broken {}" . format(simulate_clicker(provided.BuildInfo(), SIM_TIME,strategy_best)))


obj = ClickerState()
print("this is the initial object: {}".format(obj))
obj.wait(45.0)
obj.buy_item('item', 1.0, 3.5)

print("this is the final object: {}".format(obj))
# expected
# obj:
# Time: 45.0
# Current Cookies: 44.0
# CPS: 4.5
# Total Cookies: 45.0
# History(length: 2): [(0.0, None, 0.0, 0.0), (45.0, 'item', 1.0, 45.0)]



