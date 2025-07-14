const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

exports.handler = async (event, context) => {
  try {
    const postsDirectory = path.join(process.cwd(), 'content', 'blog');
    
    // Check if directory exists
    if (!fs.existsSync(postsDirectory)) {
      return {
        statusCode: 200,
        body: JSON.stringify({ posts: [] })
      };
    }
    
    const fileNames = fs.readdirSync(postsDirectory);
    const posts = fileNames
      .filter(name => name.endsWith('.md'))
      .map(name => {
        const fullPath = path.join(postsDirectory, name);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const { data, content } = matter(fileContents);
        
        // Create slug from filename
        const slug = name.replace(/\.md$/, '').replace(/^\d{4}-\d{2}-\d{2}-/, '');
        
        return {
          slug,
          title: data.title,
          date: data.date,
          description: data.description,
          image: data.image,
          tags: data.tags || [],
          draft: data.draft || false,
          content,
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
    console.error('Error loading posts:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to load posts' })
    };
  }
};
