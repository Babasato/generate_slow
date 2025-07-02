exports.handler = async (event, context) => {
  try {
    const response = await fetch(
      'https://cdn.contentful.com/spaces/gt8n4z9u155i/entries?access_token=5pJ150DbrMTkua2vEatsNYRmcMmCC5t2CkcN6OmCfFM&content_type=blogPost&order=-sys.createdAt&include=2'
    );
    
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    
    const data = await response.json();
    
    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify(data),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({
        error: 'Failed to fetch blog posts'
      }),
    };
  }
};
