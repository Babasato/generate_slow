const fs = require('fs');
const path = require('path');

// Simple frontmatter parser
function parseFrontmatter(content) {
  const frontmatterRegex = /^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/;
  const match = content.match(frontmatterRegex);
  
  if (!match) {
    return { data: {}, content: content };
  }
  
  const frontmatter = match[1];
  const body = match[2];
  
  const data = {};
  const lines = frontmatter.split('\n');
  
  lines.forEach(line => {
    const colonIndex = line.indexOf(':');
    if (colonIndex > 0) {
      const key = line.substring(0, colonIndex).trim();
      let value = line.substring(colonIndex + 1).trim();
      
      // Remove quotes
      if (value.startsWith('"') && value.endsWith('"')) {
        value = value.slice(1, -1);
      }
      
      // Handle boolean
      if (value === 'true') value = true;
      if (value === 'false') value = false;
      
      // Handle arrays
      if (value.startsWith('[') && value.endsWith(']')) {
        value = value.slice(1, -1).split(',').map(item => item.trim().replace(/"/g, ''));
      }
      
      data[key] = value;
    }
  });
  
  return { data, content: body };
}

exports.handler = async (event, context) => {
  try {
    // Try different possible paths
    const possiblePaths = [
      path.join(process.cwd(), 'content', 'blog'),
      path.join(process.cwd(), 'content/blog'),
      path.join('/opt/build/repo/content/blog'),
      path.join('/opt/build/repo/content', 'blog')
    ];
    
    let postsDirectory = null;
    for (const tryPath of possiblePaths) {
      if (fs.existsSync(tryPath)) {
        postsDirectory = tryPath;
        break;
      }
    }
    
    if (!postsDirectory) {
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({ 
          posts: [],
          debug: `Tried paths: ${possiblePaths.join(', ')}`
        })
      };
    }
    
    const fileNames = fs.readdirSync(postsDirectory);
    const posts = fileNames
      .filter(name => name.endsWith('.md'))
      .map(name => {
        const fullPath = path.join(postsDirectory, name);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const { data, content } = parseFrontmatter(fileContents);
        
        const slug = name.replace(/\.md$/, '').replace(/^\d{4}-\d{2}-\d{2}-/, '');
        
        return {
          slug,
          title: data.title || 'Untitled',
          date: data.date || new Date().toISOString(),
          description: data.description || '',
          image: data.image || null,
          tags: Array.isArray(data.tags) ? data.tags : (data.tags ? [data.tags] : []),
          draft: data.draft === true,
          content: content.trim(),
          read_time: `${Math.ceil(content.split(' ').length / 200)} min read`
        };
      })
      .filter(post => !post.draft)
      .sort((a, b) => new Date(b.date) - new Date(a.date));

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ posts })
    };
  } catch (error) {
    return {
      statusCode: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ 
        error: error.message,
        stack: error.stack
      })
    };
  }
};
