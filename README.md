# RUYA-C

This repository contains both a command line script and a lightweight web UI
for chatting with the [OpenRouter](https://openrouter.ai) API. The free Meta
**Llama 3 8B Instruct** model is used by default and requires an API key.

## Requirements

 - Python 3.11+
- `pip` for installing dependencies

Run `./setup.sh` to install everything from `requirements.txt`.

Both the CLI and web server rely on the `OPENROUTER_API_KEY` environment
variable. You can store it in a local `.env` file for convenience. Optional
`OPENROUTER_MODEL` and `OPENROUTER_SYSTEM_PROMPT` variables allow you to change
the model and system prompt without editing the code.

## Getting started

1. Obtain an API key from [OpenRouter](https://openrouter.ai).
2. Export the key in your environment or create a `.env` file. You can also
   optionally set `OPENROUTER_MODEL` or `OPENROUTER_SYSTEM_PROMPT` here if you
   want to override the defaults:

   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   export OPENROUTER_MODEL="meta-llama/llama-3-8b-instruct:free"
   export OPENROUTER_SYSTEM_PROMPT="You are Ruyaa, a professional assistant."
   ```

   or

   ```bash
   cat <<EOF > .env
   OPENROUTER_API_KEY=your_api_key_here
   OPENROUTER_MODEL=meta-llama/llama-3-8b-instruct:free
   OPENROUTER_SYSTEM_PROMPT="You are Ruyaa, a professional assistant."
   EOF
   ```

3. Run `./setup.sh` once to install dependencies.
4. Run the chat script:

   ```bash
   python openrouter_chat.py "Hello, AI!"
   ```

The script sends your message to OpenRouter and prints the model's reply.

## Web interface

To try a simple web chat UI locally, start the Flask server:

```bash
python openrouter_web.py
```

Make sure `OPENROUTER_API_KEY` is available in your environment or `.env`.

Then open [http://localhost:5000](http://localhost:5000) in your browser. Type a
message and you should see the model's reply.

## Deploying to Vercel

This repository is ready for deployment on [Vercel](https://vercel.com). The
`public` directory contains the static HTML frontend and `api/chat.py` is
deployed as a serverless function.

1. Install the Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Set the `OPENROUTER_API_KEY` environment variable in your Vercel project.
   You can do this with `vercel env add OPENROUTER_API_KEY` or via the Vercel
   dashboard. **Never commit your real API key.**

3. Vercel automatically installs Python packages from `requirements.txt`.
   The provided `vercel.json` configures the deployment to use Python 3.11.

4. Deploy:

   ```bash
   vercel --prod
   ```

Once deployed, open your Vercel URL to chat with the AI using the hosted
interface.
