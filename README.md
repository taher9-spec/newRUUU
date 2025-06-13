# RUYA-C

This is a simple Next.js application that fetches market prices from the Alpha Vantage API and displays them along with the Ruyaa logo.

## Development

Install dependencies and start the development server:

```bash
npm install
npm run dev
```

The page fetches market data from `/api/price` which requires an API key.

## Environment Variables

Set the following environment variable in your local environment or Vercel project settings:

- `MARKET_DATA_API_KEY` – your Alpha Vantage API key

## Deployment

This project works on [Vercel](https://vercel.com/). After setting the environment variable above, deploy the repository to Vercel and it should build automatically using Next.js defaults.

