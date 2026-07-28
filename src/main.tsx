import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import App from './App.tsx';
import './index.css';
import { inject } from '@vercel/analytics';
import CanvasBackground from './components/CanvasBackground';

// Inject Vercel Web Analytics
inject();

const canvasRootElement = document.getElementById('canvas-root');
if (canvasRootElement) {
  createRoot(canvasRootElement).render(
    <StrictMode>
      <CanvasBackground />
    </StrictMode>,
  );
}

const rootElement = document.getElementById('root');
if (rootElement) {
  createRoot(rootElement).render(
    <StrictMode>
      <App />
    </StrictMode>,
  );
}
