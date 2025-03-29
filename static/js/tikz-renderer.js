async function renderTikzDiagram(containerId, tikzCode, options = {}) {
    const container = document.getElementById(containerId);
    container.innerHTML = '<div class="loading">🔄 Rendering...</div>';
    
    console.log('Starting rendering process...');
    
    try {
      // Create URL parameters including options
      const params = new URLSearchParams();
      params.append('code', tikzCode);
      
      // Add any options as parameters
      if (options && options.libraries) {
        params.append('libraries', options.libraries.join(','));
      }
      
      const url = `/render-tikz?${params.toString()}`;
      console.log(`Sending request to: ${url}`);
      
      const response = await fetch(url, {
        method: 'GET',
        headers: {
          'Accept': 'text/html,application/xhtml+xml,application/xml',
        },
      });
      
      console.log(`Response status: ${response.status}`);
      
      if (!response.ok) {
        const errorText = await response.text();
        console.error('Server error:', errorText);
        throw new Error(`Server returned ${response.status}: ${errorText}`);
      }
      
      console.log('Getting response text...');
      const svg = await response.text();
      console.log(`Received response of length: ${svg.length}`);
      
      if (!svg.includes('<svg')) {
        console.error('Invalid response:', svg.substring(0, 100) + '...');
        throw new Error('Risposta non valida dal server (manca tag SVG)');
      }
      
      console.log('Setting SVG in container...');
      container.innerHTML = svg;
    } catch (error) {
      console.error('Rendering error:', error);
      container.innerHTML = `
        <div class="error">
          ❌ Errore: ${error.message}
          <details>
            <summary>Codice TikZ</summary>
            <pre>${tikzCode}</pre>
          </details>
          <details>
            <summary>Dettagli Tecnici</summary>
            <pre>${error.stack || 'No stack trace available'}</pre>
          </details>
        </div>
      `;
    }
  }