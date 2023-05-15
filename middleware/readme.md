# Middleware  

> Basically, it's the stuff that is between the front-end and the Ecowitt database and hides to the users the token key.

To start developing your Worker, run `npx wrangler dev`
To publish your Worker to the Internet, run `npx wrangler publish`

Environment variables should be put for local dev in a `.dev.vars` file using _dotenv_ format, and then pushed using `npx wrangler secret`.
