// netlify/functions/posts.js
const fs = require('fs').promises; // Use promises for async
const path = require('path');
const matter = require('gray-matter');

exports.handler = async function (event, context) {
  try {
    const postsDirectory = path.join(__dirname, '../../blog'); // Adjust path for Netlify Functions
    const filenames = await fs.readdir(postsDirectory);

    const posts = [];

    for (const filename of filenames) {
      if (filename.endsWith('.md')) {
        const filePath = path.join(postsDirectory, filename);
        const fileContent = await fs.readFile(filePath, 'utf8');
        const { data, content } = matter(fileContent);

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
          title: data.title,
          date: data.date,
          description: data.description,
          featured_image: data.featured_image || data.image || '',
          tags: data.tags || [],
          category: data.category || '',
          grade_level: data.grade_level || [],
          difficulty: data.difficulty || '',
          read_time: data.read_time ? `${data.read_time} min read` : '5 min read',
          body: htmlContent,
          slug: filename.replace('.md', ''),
        });
      }
    }

    // Sort by date
    posts.sort((a, b) => new Date(b.date) - new Date(a.date));

    // Return success response
    return {
      statusCode: 200,
      body: JSON.stringify(posts),
    };
  } catch (error) {
    console.error('Error in posts function:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to load posts' }),
    };
  }
};