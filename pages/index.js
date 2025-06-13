import { useEffect, useState } from 'react';

export default function Home() {
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(true);
  const symbol = 'IBM';

  useEffect(() => {
    async function fetchPrice() {
      try {
        const res = await fetch(`/api/price?symbol=${symbol}`);
        const data = await res.json();
        setPrice(data.price);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    fetchPrice();
    const interval = setInterval(fetchPrice, 60000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <img src="/ruyaa-logo.svg" alt="Ruyaa Logo" style={{ maxWidth: '200px' }} />
      <h1>Market Price for {symbol}</h1>
      {loading ? <p>Loading...</p> : <p>{price ? `$${price}` : 'Unavailable'}</p>}
    </div>
  );
}
