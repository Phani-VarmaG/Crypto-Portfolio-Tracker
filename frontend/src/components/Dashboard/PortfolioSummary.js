import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import api from '../../services/api';

const PortfolioSummary = () => {
  const [portfolioData, setPortfolioData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get('/portfolio');
        setPortfolioData(response.data);
      } catch (error) {
        console.error('Error fetching portfolio:', error);
      }
    };
    fetchData();
  }, []);

  const chartData = {
    labels: portfolioData.map(coin => coin.name),
    datasets: [{
      label: 'Portfolio Allocation',
      data: portfolioData.map(coin => coin.value),
      backgroundColor: portfolioData.map(coin => `#${Math.floor(Math.random()*16777215).toString(16)}`)
    }]
  };

  return (
    <div className="dashboard-section">
      <h2>Portfolio Overview</h2>
      <div className="chart-container">
        <Line data={chartData} options={{ responsive: true }} />
      </div>
    </div>
  );
};
