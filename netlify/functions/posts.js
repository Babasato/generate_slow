const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

exports.handler = async (event, context) => {
  try {
    // Set CORS headers
    const headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Content-Type': 'application/json'
    };

    // Handle preflight requests
    if (event.httpMethod === 'OPTIONS') {
      return {
        statusCode: 200,
        headers,
        body: ''
      };
    }

    // Only allow GET requests
    if (event.httpMethod !== 'GET') {
      return {
        statusCode: 405,
        headers,
        body: JSON.stringify({ error: 'Method not allowed' })
      };
    }

    // Path to blog posts directory
    const postsDirectory = path.join(process.cwd(), 'blog');
    
    // Check if blog directory exists
    if (!fs.existsSync(postsDirectory)) {
      return {
        statusCode: 200,
        headers,
        body: JSON.stringify({ posts: [] })
      };
    }

    // Read all files in the blog directory
    const filenames = fs.readdirSync(postsDirectory);
    
    // Filter for markdown files and parse them
    const posts = filenames
      .filter(filename => filename.endsWith('.md'))
      .map(filename => {
        const fullPath = path.join(postsDirectory, filename);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const { data, content } = matter(fileContents);
        
        return {
          slug: filename.replace('.md', ''),
          title: data.title || 'Untitled',
          date: data.date || null,
          draft: data.draft || false,
          content: content,
          excerpt: content.substring(0, 150) + '...'
        };
      })
      .filter(post => !post.draft) // Filter out drafts
      .sort((a, b) => new Date(b.date) - new Date(a.date)); // Sort by date, newest first

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ posts })
    };

  } catch (error) {
    console.error('Error in posts function:', error);
    return {
      statusCode: 500,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ error: 'Internal server error' })
    };
  }
};