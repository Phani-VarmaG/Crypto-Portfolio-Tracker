import React, { useState } from 'react';
import api from '../../services/api';

const TransactionForm = () => {
  const [formData, setFormData] = useState({
    coin_id: '',
    amount: 0,
    transaction_type: 'buy'
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/transactions', formData);
      alert('Transaction added!');
    } catch (error) {
      alert('Error adding transaction');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Coin ID (e.g., bitcoin)"
        onChange={e => setFormData({...formData, coin_id: e.target.value})}
      />
      <input
        type="number"
        step="0.00000001"
        onChange={e => setFormData({...formData, amount: parseFloat(e.target.value)})}
      />
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
