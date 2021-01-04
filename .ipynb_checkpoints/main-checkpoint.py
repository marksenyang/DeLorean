{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import libraries\n",
    "from panel.interact import interact\n",
    "\n",
    "# Import self-made modules\n",
    "from get_data import get_data_stock, get_data_market\n",
    "from process_data import process_data\n",
    "from visualize_data import make_plot1, make_plot2\n",
    "from make_interface import make_interface"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to generate the app\n",
    "def create_app(ticker1, weight1, ticker2, weight2):\n",
    "    # Check if the sum of all weights = 1\n",
    "    if weight1 + weight2 != 1:\n",
    "        return 'Make sure the sum of your weights is 1'\n",
    "    \n",
    "    # --------------------- Get the data from APIs ---------------------\n",
    "    # Get data for given stocks\n",
    "    tickers = [ticker1, ticker2]\n",
    "    raw_data_stock = get_data_stock(tickers)\n",
    "    \n",
    "    # Get data of the market (i.e. S&P 500 index)\n",
    "    raw_data_market = get_data_market()\n",
    "     \n",
    "        \n",
    "    # --------------------- Process the data ---------------------\n",
    "    tickers = [ticker1, ticker2]\n",
    "    weights = [weight1, weight2]\n",
    "    processed_data_stock = process_data(raw_data_stock, tickers, weights)\n",
    "    \n",
    "    \n",
    "    # --------------------- Visualize the data ---------------------\n",
    "    plot1 = make_plot1(processed_data_stock)\n",
    "    plot2 = make_plot2(processed_data_stock)\n",
    "\n",
    "    \n",
    "    # --------------------- Make the interface of the app ---------------------\n",
    "    app = make_interface(plot1, plot2)\n",
    "    \n",
    "    return app"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run the app\n",
    "interact(create_app, ticker1='MSFT', ticker2='DIS', weight1=0.5, weight2=0.5)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
