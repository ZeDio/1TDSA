import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import Comp from './Comp.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
    <Comp></Comp>
  </StrictMode>,
)
