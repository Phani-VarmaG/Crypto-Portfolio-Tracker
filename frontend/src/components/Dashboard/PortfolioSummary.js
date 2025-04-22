import React, { useState, useEffect } from 'react';
// Import the Line chart from react-chartjs-2 to visualize data.
import { Line } from 'react-chartjs-2';
// Import Axios instance for API calls.
import api from '../../services/api';

const PortfolioSummary = () => {
  // State to hold portfolio data received from the backend.
  const [portfolioData, setPortfolioData] = useState([]);

  // Fetch portfolio data when the component mounts.
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Call the backend portfolio endpoint.
        const response = await api.get('/portfolio');
        setPortfolioData(response.data);
      } catch (error) {
        console.error('Error fetching portfolio:', error);
      }
    };
    fetchData();
  }, []);

  // Prepare data for the chart.
  const chartData = {
    // x-axis labels extracted from coin names.
    labels: portfolioData.map(coin => coin.name),
    datasets: [{
      label: 'Portfolio Allocation',
      // y-axis data calculated from coin values.
      data: portfolioData.map(coin => coin.value),
      // Random background colors for visual differentiation.
      backgroundColor: portfolioData.map(coin => `#${Math.floor(Math.random()*16777215).toString(16)}`)
    }]
  };

  // Render the portfolio summary with a line chart.
  return (
    <div className="dashboard-section">
      <h2>Portfolio Overview</h2>
      <div className="chart-container">
        <Line data={chartData} options={{ responsive: true }} />
      </div>
    </div>
  );
};

export default PortfolioSummary;
