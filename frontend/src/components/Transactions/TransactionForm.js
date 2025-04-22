import React, { useState } from 'react';
// Import the configured Axios instance to communicate with the backend.
import api from '../../services/api';

const TransactionForm = () => {
  // Initialize form state with default values.
  const [formData, setFormData] = useState({
    coin_id: '',
    amount: 0,
    transaction_type: 'buy'
  });

  // Function to handle form submission.
  const handleSubmit = async (e) => {
    // Prevent default form submission behavior.
    e.preventDefault();
    try {
      // Send a POST request to the /transactions endpoint with form data.
      await api.post('/transactions', formData);
      alert('Transaction added!');
    } catch (error) {
      alert('Error adding transaction');
    }
  };

  // Render the transaction form.
  return (
    <form onSubmit={handleSubmit}>
      {/* Input for entering the coin ID */}
      <input
        type="text"
        placeholder="Coin ID (e.g., bitcoin)"
        onChange={e => setFormData({...formData, coin_id: e.target.value})}
      />
      {/* Input for entering the amount with a step for precision */}
      <input
        type="number"
        step="0.00000001"
        onChange={e => setFormData({...formData, amount: parseFloat(e.target.value)})}
      />
      {/* Dropdown for choosing transaction type (buy or sell) */}
      <select
        onChange={e => setFormData({...formData, transaction_type: e.target.value})}
      >
        <option value="buy">Buy</option>
        <option value="sell">Sell</option>
      </select>
      <button type="submit">Add Transaction</button>
    </form>
  );
};

export default TransactionForm;
