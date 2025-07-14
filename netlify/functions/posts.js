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

const fs = require('fs').promises;
const path = require('path');
const matter = require('gray-matter');

exports.handler = async function () {
  try {
    const postsDir = path.join(__dirname, '../../content/blog');
    const files = await fs.readdir(postsDir);

    const posts = await Promise.all(
      files
        .filter(file => file.endsWith('.md'))
        .map(async file => {
          const filePath = path.join(postsDir, file);
          const fileContent = await fs.readFile(filePath, 'utf8');
          const { data, content } = matter(fileContent);
          const slug = file.replace(/\.md$/, '');
          return {
            slug,
            title: data.title,
            date: data.date,
            description: data.description,
            featured_image: data.image,
            tags: data.tags || [],
            content,
            read_time: Math.ceil(content.split(' ').length / 200) + ' min read'
          };
        })
    );

    return {
      statusCode: 200,
      body: JSON.stringify({ posts })
    };
  } catch (error) {
    console.error('Error in posts function:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to load posts' })
    };
  }
};
