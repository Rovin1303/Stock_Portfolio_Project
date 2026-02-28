// src/pages/PortfolioDetail.jsx

import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../services/api";
import { Bar } from "react-chartjs-2";
import "chart.js/auto";
import "./PortfolioDetail.css";

function PortfolioDetail() {
  const { portfolioId } = useParams();
  const navigate = useNavigate();

  const [portfolio, setPortfolio] = useState(null);
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    if (!portfolioId) return;

    api.get(`portfolio/${portfolioId}/`)
      .then((res) => {
        setPortfolio(res.data);
        setStocks(res.data.stocks || []);
      })
      .catch((err) => console.log(err));

  }, [portfolioId]);

  if (!portfolio) return <h2>Loading...</h2>;

  // ✅ PE Chart Data
  const peChartData = {
    labels: stocks.map((stock) => stock.company_name),
    datasets: [
      {
        label: "PE Ratio",
        data: stocks.map((stock) => stock.pe_ratio || 0),
        backgroundColor: "#2962ff",
      },
    ],
  };

  return (
    <div className="portfolio-container">

      <h1>{portfolio.name}</h1>

      {/* STOCK GRID */}
      <div className="stock-grid">
        {stocks.map((stock) => (
          <div
            key={stock.id}
            className="stock-card"
            onClick={() => navigate(`/stock/${stock.id}`)}
          >
            <h3>{stock.company_name}</h3>
            <p className="ticker">{stock.ticker}</p>

            <p>
              <strong>PE:</strong> {stock.current_price ?? "N/A"}
            </p>
          </div>
        ))}
        </div>
        {/* 📊 PE Comparison Chart */}
        <div className="card chart-section">
          <h3>PE Ratio Comparison</h3>
          <Bar data={peChartData} />
        </div>

    </div>
  );
}

export default PortfolioDetail;