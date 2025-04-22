// Import React to use JSX.
import React from 'react';
// Import the PortfolioSummary component to display portfolio analytics.
import PortfolioSummary from '../components/Dashboard/PortfolioSummary';
// Import the TransactionForm component to add new transactions.
import TransactionForm from '../components/Transactions/TransactionForm';

const Portfolio = () => {
  return (
    <div>
      {/* Heading for the portfolio page */}
      <h1>My Cryptocurrency Portfolio</h1>
      {/* Component showing portfolio overview and data visualization */}
      <PortfolioSummary />
      {/* Section for adding a new transaction */}
      <h2>Add New Transaction</h2>
      <TransactionForm />
    </div>
  );
};

export default Portfolio;