'''
Created on 07.11.2017

Module contains interfaces for trader implementations and model classes

@author: jtymoszuk
'''
from enum import Enum

from model.CompanyEnum import CompanyEnum
from model.SharesOfCompany import SharesOfCompany


class TradingActionEnum(Enum):
    '''
    Represents possible actions on stock market
    '''
    BUY = 1
    SELL = 2


class TradingAction:
    '''
    Represents action to be taken on a portfolio of a client
    '''

    def __init__(self, action: TradingActionEnum, shares: SharesOfCompany):
        """ Constructor
    
        Args:
          action : see TradingActionEnum
          shares : see SharesOfCompany
        """
        self.action = action
        self.shares = shares


class TradingActionList:
    '''
    Represents typesafe container to hold a list of TradingAction's
    '''

    def __init__(self):
        """ 
        Constructor
        """
        self.__trading_action_list = list()

    def __add_trading_action(self, action: TradingActionEnum, shares: SharesOfCompany):
        self.add_trading_action(TradingAction(action, shares))

    def add_trading_action(self, trading_action: TradingAction):
        """
        Adds given TradingAction to list, if not Nonen
        
        Args:
            trading_action : see TradingAction
        """
        if (trading_action is not None):
            self.__trading_action_list.append(trading_action)

    def len(self) -> int:
        return len(self.__trading_action_list)

    def get(self, index: int) -> TradingAction:
        return self.__trading_action_list[index]

    def get_by_CompanyEnum(self, company_enum: CompanyEnum) -> TradingAction:
        """
        Returns TradingAction for given CompanyEnum, or None if nothing found
        """
        return next(
            (trading_action for trading_action in self.__trading_action_list if
             trading_action.shares.company_enum == company_enum),
            None)

    def is_empty(self):
        return self.len() == 0

    def iterator(self):
        return iter(self.__trading_action_list)

    def buy(self, company: CompanyEnum, amount: int):
        """
        Adds a trading action BUY to the list

        Args:
            company:
            amount:
        """
        self.__add_trading_action(TradingActionEnum.BUY, SharesOfCompany(company, amount))

    def sell(self, company: CompanyEnum, amount: int):
        """
        Adds a trading action SELL to the list

        Args:
            company:
            amount:
        """
        self.__add_trading_action(TradingActionEnum.SELL, SharesOfCompany(company, amount))