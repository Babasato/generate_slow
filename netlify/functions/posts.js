const path = require('path');  // <-- Add this line
const fs = require('fs');     // <-- This should already be there

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
      
      // Handle arrays (both formats)
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
    // More comprehensive path checking
    const possiblePaths = [
      // Current working directory variants
      path.join(process.cwd(), 'content', 'blog'),
      path.join(process.cwd(), 'content/blog'),
      
      // Netlify build variants
      path.join('/opt/build/repo/content/blog'),
      path.join('/opt/build/repo/content', 'blog'),
      
      // Alternative build locations
      path.join(__dirname, '..', '..', 'content', 'blog'),
      path.join(__dirname, '..', '..', 'content/blog'),
      
      // Function directory relative
      path.join(__dirname, 'content', 'blog'),
      path.join(__dirname, 'content/blog'),
      
      // Root relative
      path.join('/', 'var', 'task', 'content', 'blog'),
      path.join('/', 'tmp', 'content', 'blog')
    ];
    
    let postsDirectory = null;
    let foundPaths = [];
    
    // Check each path and log what we find
    for (const tryPath of possiblePaths) {
      try {
        if (fs.existsSync(tryPath)) {
          postsDirectory = tryPath;
          foundPaths.push(`Found: ${tryPath}`);
          break;
        } else {
          foundPaths.push(`Not found: ${tryPath}`);
        }
      } catch (err) {
        foundPaths.push(`Error checking ${tryPath}: ${err.message}`);
      }
    }
    
    if (!postsDirectory) {
      // Let's also try to find any content folder
      const contentSearchPaths = [
        path.join(process.cwd(), 'content'),
        path.join('/opt/build/repo/content'),
        path.join(__dirname, '..', '..', 'content')
      ];
      
      let contentFound = [];
      for (const contentPath of contentSearchPaths) {
        try {
          if (fs.existsSync(contentPath)) {
            const contents = fs.readdirSync(contentPath);
            contentFound.push(`Content dir ${contentPath}: ${contents.join(', ')}`);
          }
        } catch (err) {
          contentFound.push(`Error reading ${contentPath}: ${err.message}`);
        }
      }
      
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({ 
          posts: [],
          debug: {
            message: "No blog directory found",
            searchPaths: foundPaths,
            contentSearch: contentFound,
            cwd: process.cwd(),
            __dirname: __dirname
          }
        })
      };
    }
    
    let fileNames;
    try {
      fileNames = fs.readdirSync(postsDirectory);
    } catch (err) {
      return {
        statusCode: 200,
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({ 
          posts: [],
          debug: {
            message: `Found directory but can't read: ${postsDirectory}`,
            error: err.message
          }
        })
      };
    }
    
    const posts = fileNames
      .filter(name => name.endsWith('.md'))
      .map(name => {
        try {
          const fullPath = path.join(postsDirectory, name);
          const fileContents = fs.readFileSync(fullPath, 'utf8');
          const { data, content } = parseFrontmatter(fileContents);
          
          // Generate slug from filename (remove date prefix and .md extension)
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
        } catch (err) {
          console.error(`Error processing ${name}:`, err);
          return null;
        }
      })
      .filter(post => post !== null && !post.draft)
      .sort((a, b) => new Date(b.date) - new Date(a.date));

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({ 
        posts,
        debug: {
          directory: postsDirectory,
          filesFound: fileNames,
          postsProcessed: posts.length
        }
      })
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
