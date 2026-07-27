export async function handler(event, context) {
  const headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Content-Type": "application/json"
  };

  if (event.httpMethod === "OPTIONS") {
    return {
      statusCode: 200,
      headers,
      body: ""
    };
  }

  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers,
      body: JSON.stringify({ error: "Method Not Allowed" })
    };
  }

  try {
    const { message, history } = JSON.parse(event.body);

    const systemPrompt = `You are NA Assistant on Naitik Agarwal portfolio. Be casual and helpful.
Naitik is an AI Explorer, Prompt Engineer, Vibe Coder and Creator.
Motto: Skills matter more than degrees.
Skills: Color Grading, Vibe Coding, Prompt Engineering, AI Tool Scouting, No-Code Development, Photography, Canva and AI Design.
AI Tools: Claude, Gemini, ChatGPT, Lovable, Antigravity, Nano Banana, Google Veo, Google AI Studio.
Project: Bioluminescent Streetlight — vibe coded with Claude and Lovable, zero traditional code, live at https://bioluminescent-streetlights.lovable.app
Achievements: Ideathon 2025 Top 100 of 1400. Ideathon 2026 Participated. MDI Gurugram Photography 4th of 135.
Badges: 75 plus total — 25 Google Cloud Skills Boost, 50 Microsoft Learn.
Goals: Achieve big in AI, shape it not just use it, stay curious.
Contact: Naitik.270810@outlook.com
Rules: Keep answers concise. Use bullet points for lists instead of a single boring paragraph. Never make up information. End contact answers with his email.`;

    const apiKey = process.env.GAPI_KEY || process.env.GEMINI_API_KEY;
    if (!apiKey) {
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ error: "GAPI_KEY is not configured" })
      };
    }

    const modelsToTry = [
      'gemini-2.5-flash',
      'gemini-3.5-flash',
      'gemini-flash-latest'
    ];

    // Construct the contents payload for Gemini API
    const contents = [];
    
    // Using system instructions supported via system_instruction in Gemini REST API
    const system_instruction = {
      parts: [{ text: systemPrompt }]
    };

    if (history && history.length > 0) {
      for (const msg of history) {
        if (msg.role && msg.content) {
          contents.push({
            role: msg.role === 'model' ? 'model' : 'user',
            parts: [{ text: msg.content }]
          });
        }
      }
    }

    contents.push({
      role: 'user',
      parts: [{ text: message }]
    });

    const payload = {
      contents,
      systemInstruction: {
        parts: [{ text: systemPrompt }]
      },
      generationConfig: {
        temperature: 0.8,
        maxOutputTokens: 1500 // Allow enough tokens for thinking models
      }
    };

    let response;
    let data;
    let lastError = "Upstream API error";

    for (const model of modelsToTry) {
      const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
      
      try {
        response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        data = await response.json();

        if (response.ok) {
          // Success! Break out of the loop
          break;
        } else {
          lastError = (data.error && data.error.message) ? data.error.message : `API Error on ${model}`;
        }
      } catch (err) {
        lastError = err.message;
      }
    }

    if (!response || !response.ok) {
      // If all models hit quota or fail, return the error so the user can debug their API key
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ reply: `Error: ${lastError}` })
      };
    }

    let reply = "I couldn't process that request at this time.";
    if (data.candidates && data.candidates.length > 0 && data.candidates[0].content && data.candidates[0].content.parts.length > 0) {
      reply = data.candidates[0].content.parts[0].text;
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ reply })
    };
  } catch (error) {
    console.error("Function error:", error);
    return {
      statusCode: 500,
      headers,
      body: JSON.stringify({ error: "Internal Server Error" })
    };
  }
}
