const fs = require('fs');
const path = require('path');

// Simple frontmatter parser since gray-matter might not be available
function parseFrontmatter(content) {
  const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/;
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
      
      // Remove quotes if present
      if (value.startsWith('"') && value.endsWith('"')) {
        value = value.slice(1, -1);
      }
      
      // Handle boolean values
      if (value === 'true') value = true;
      if (value === 'false') value = false;
      
      // Handle arrays (tags)
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
    const postsDirectory = path.join(process.cwd(), 'content', 'blog');
    
    // Check if directory exists
    if (!fs.existsSync(postsDirectory)) {
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({ posts: [] })
      };
    }
    
    const fileNames = fs.readdirSync(postsDirectory);
    const posts = fileNames
      .filter(name => name.endsWith('.md'))
      .map(name => {
        const fullPath = path.join(postsDirectory, name);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const { data, content } = parseFrontmatter(fileContents);
        
        // Create slug from filename
        const slug = name.replace(/\.md$/, '').replace(/^\d{4}-\d{2}-\d{2}-/, '');
        
        // Calculate read time
        const wordCount = content.split(' ').length;
        const readTime = Math.ceil(wordCount / 200);
        
        return {
          slug,
          title: data.title || 'Untitled',
          date: data.date || new Date().toISOString(),
          description: data.description || '',
          image: data.image || null,
          tags: Array.isArray(data.tags) ? data.tags : (data.tags ? [data.tags] : []),
          draft: data.draft === true,
          content: content.trim(),
          read_time: `${readTime} min read`,
          featured_image: data.image || null
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
    console.error('Error loading posts:', error);
    return {
      statusCode: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ 
        error: 'Failed to load posts',
        details: error.message 
      })
    };
  }
};
