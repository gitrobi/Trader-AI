# Start evaluation rnn_trader:
# Compare its performance over the testing period (2012-2017) against a buy-and-hold trader.
from utils import read_stock_market_data_conveniently
from evaluating.portfolio_evaluator import PortfolioEvaluator
from model.CompanyEnum import CompanyEnum
from model.Portfolio import Portfolio
from predicting.predictor.perfect_predictor import PerfectPredictor
from trading.trader.buy_and_hold_trader import BuyAndHoldTrader
from trading.trader.rnn_trader import RnnTrader

if __name__ == "__main__":
    period1 = '1962-2011'
    period2 = '2012-2017'

    stock_market_data = read_stock_market_data_conveniently([CompanyEnum.COMPANY_A, CompanyEnum.COMPANY_B],
                                                            [period1, period2])

    # TODO @Jonas Kann man dieses Benchmark hier eleganter machen, z.B. dependency injection?
    benchmark = BuyAndHoldTrader()
    trader_under_test = RnnTrader(PerfectPredictor(CompanyEnum.COMPANY_A),
                                  PerfectPredictor(CompanyEnum.COMPANY_B))  # TODO implement PerfectStockBPredictor
    benchmark_portfolio = Portfolio(10000, [], 'Benchmark')
    trader_under_test_portfolio = Portfolio(10000, [], 'RNN Trader')
    evaluator = PortfolioEvaluator([benchmark, trader_under_test], True)
    evaluator.inspect_over_time(stock_market_data, [benchmark_portfolio, trader_under_test_portfolio], 1000)