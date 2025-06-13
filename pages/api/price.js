export default async function handler(req, res) {
  const { symbol = 'IBM' } = req.query;
  const apiKey = process.env.MARKET_DATA_API_KEY;
  if (!apiKey) {
    return res.status(500).json({ error: 'API key not configured' });
  }
  const url = `https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${apiKey}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    const price = data['Global Quote'] && data['Global Quote']['05. price'];
    res.status(200).json({ price });
  } catch (err) {
    res.status(500).json({ error: 'Failed to fetch price' });
  }
}
