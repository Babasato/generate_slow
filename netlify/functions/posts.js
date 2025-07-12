// netlify/functions/posts.js
const fs = require('fs').promises;
const path = require('path');

let matter;
try {
  matter = require('gray-matter');
} catch (error) {
  console.error('gray-matter not found, using fallback parser');
}

// Fallback frontmatter parser if gray-matter isn't available
function parseFrontmatter(content) {
  if (matter) {
    return matter(content);
  }
  
  // Simple fallback parser
  const lines = content.split('\n');
  const data = {};
  let bodyStart = 0;
  
  if (lines[0] === '---') {
    for (let i = 1; i < lines.length; i++) {
      if (lines[i] === '---') {
        bodyStart = i + 1;
        break;
      }
      const match = lines[i].match(/^(\w+):\s*(.*)$/);
      if (match) {
        const key = match[1];
        let value = match[2];
        
        // Handle arrays
        if (value.startsWith('[') && value.endsWith(']')) {
          value = value.slice(1, -1).split(',').map(item => item.trim().replace(/['"]/g, ''));
        }
        // Handle strings
        else if (value.startsWith('"') && value.endsWith('"')) {
          value = value.slice(1, -1);
        }
        
        data[key] = value;
      }
    }
  }
  
  return {
    data,
    content: lines.slice(bodyStart).join('\n')
  };
}

exports.handler = async function (event, context) {
  try {
    console.log('Starting posts function...');
    
    // Add CORS headers
    const headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Content-Type': 'application/json'
    };

    // Handle OPTIONS request
    if (event.httpMethod === 'OPTIONS') {
      return {
        statusCode: 200,
        headers,
        body: ''
      };
    }

    const postsDirectory = path.join(__dirname, '../../blog');
    console.log('Looking for posts in:', postsDirectory);
    
    // Check if directory exists
    try {
      await fs.access(postsDirectory);
    } catch (error) {
      console.error('Blog directory not found:', postsDirectory);
      return {
        statusCode: 404,
        headers,
        body: JSON.stringify({ error: 'Blog directory not found' })
      };
    }

    const filenames = await fs.readdir(postsDirectory);
    console.log('Found files:', filenames);

    const posts = [];

    for (const filename of filenames) {
      if (filename.endsWith('.md')) {
        console.log('Processing:', filename);
        const filePath = path.join(postsDirectory, filename);
        const fileContent = await fs.readFile(filePath, 'utf8');
        const { data, content } = parseFrontmatter(fileContent);

        // Basic markdown to HTML conversion
        const htmlContent = content
          .replace(/^# (.*$)/gm, '<h1>$1</h1>')
          .replace(/^## (.*$)/gm, '<h2>$1</h2>')
          .replace(/^### (.*$)/gm, '<h3>$1</h3>')
          .replace(/^#### (.*$)/gm, '<h4>$1</h4>')
          .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
          .replace(/\*(.*?)\*/g, '<em>$1</em>')
          .replace(/^\- (.*$)/gm, '<li>$1</li>')
          .replace(/\n\n/g, '</p><p>')
          .replace(/^(?!<)/gm, '<p>')
          .replace(/$/gm, '</p>')
          .replace(/<p><\/p>/g, '');

        posts.push({
          title: data.title || filename.replace('.md', ''),
          date: data.date || new Date().toISOString().split('T')[0],
          description: data.description || '',
          featured_image: data.featured_image || data.image || '',
          tags: Array.isArray(data.tags) ? data.tags : [],
          category: data.category || '',
          grade_level: Array.isArray(data.grade_level) ? data.grade_level : [],
          difficulty: data.difficulty || '',
          read_time: data.read_time ? `${data.read_time} min read` : '5 min read',
          body: htmlContent,
          slug: filename.replace('.md', ''),
        });
      }
    }

    // Sort by date
    posts.sort((a, b) => new Date(b.date) - new Date(a.date));

    console.log(`Successfully processed ${posts.length} posts`);

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify(posts),
    };
  } catch (error) {
    console.error('Error in posts function:', error);
    return {
      statusCode: 500,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        error: 'Failed to load posts',
        details: error.message 
      }),
    };
  }
};