import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    plugins: [
      react(), 
      tailwindcss(),
      {
        name: 'netlify-functions-mock',
        configureServer(server) {
          server.middlewares.use(async (req, res, next) => {
            if (req.url?.startsWith('/.netlify/functions/ask-naitik')) {
              try {
                let body = '';
                req.on('data', chunk => body += chunk.toString());
                req.on('end', async () => {
                  try {
                    // load dynamic import without caching if possible, but fine to just import since type="module"
                    const func = await import(path.resolve(import.meta.dirname, 'netlify/functions/ask-naitik.js') + '?t=' + Date.now());
                    const event = {
                      httpMethod: req.method,
                      headers: req.headers,
                      body: body || '{}',
                    };
                    const result = await func.handler(event, {});
                    res.statusCode = result.statusCode || 200;
                    for (const [k, v] of Object.entries(result.headers || {})) {
                      res.setHeader(k, v);
                    }
                    res.end(result.body);
                  } catch (e) {
                    res.statusCode = 500;
                    res.end(JSON.stringify({ error: String(e) }));
                  }
                });
                return;
              } catch (e) {
                console.error(e);
              }
            }
            next();
          });
        },
        configurePreviewServer(server) {
          server.middlewares.use(async (req, res, next) => {
            if (req.url?.startsWith('/.netlify/functions/ask-naitik')) {
              try {
                let body = '';
                req.on('data', chunk => body += chunk.toString());
                req.on('end', async () => {
                  try {
                    const func = await import(path.resolve(import.meta.dirname, 'netlify/functions/ask-naitik.js') + '?t=' + Date.now());
                    const event = {
                      httpMethod: req.method,
                      headers: req.headers,
                      body: body || '{}',
                    };
                    const result = await func.handler(event, {});
                    res.statusCode = result.statusCode || 200;
                    for (const [k, v] of Object.entries(result.headers || {})) {
                      res.setHeader(k, v);
                    }
                    res.end(result.body);
                  } catch (e) {
                    res.statusCode = 500;
                    res.end(JSON.stringify({ error: String(e) }));
                  }
                });
                return;
              } catch (e) {
                console.error(e);
              }
            }
            next();
          });
        }
      }
    ],
    resolve: {
      alias: {
        '@': path.resolve(import.meta.dirname, '.'),
      },
    },
    server: {
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modifyâfile watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
      // Disable file watching when DISABLE_HMR is true to save CPU during agent edits.
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
    preview: {
      port: 3000,
      host: '0.0.0.0',
    },
  };
});
