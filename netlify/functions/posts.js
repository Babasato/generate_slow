exports.handler = async (event, context) => {
  const posts = [
    {
      title: "Sample Post",
      date: "2024-01-15",
      description: "This is a sample post",
      slug: "sample-post"
    }
  ];
  
  return {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(posts)
  };
};