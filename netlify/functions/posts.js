// Create this file at: scripts/build-posts.js

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

function buildPosts() {
  const postsDirectory = path.join(__dirname, '../blog');
  const outputPath = path.join(__dirname, '../posts.json');
  
  if (!fs.existsSync(postsDirectory)) {
    console.log('Creating blog directory...');
    fs.mkdirSync(postsDirectory, { recursive: true });
    return;
  }

  const filenames = fs.readdirSync(postsDirectory);
  const posts = [];

  filenames.forEach(filename => {
    if (filename.endsWith('.md')) {
      const filePath = path.join(postsDirectory, filename);
      const fileContent = fs.readFileSync(filePath, 'utf8');
      
      const { data, content } = matter(fileContent);
      
      // Convert markdown to HTML (basic)
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
        featured_image: data.featured_image || data.image,
        tags: data.tags || [],
        category: data.category,
        grade_level: data.grade_level,
        difficulty: data.difficulty,
        read_time: data.read_time ? `${data.read_time} min read` : '5 min read',
        body: htmlContent,
        slug: filename.replace('.md', '')
      });
    }
  });

  // Sort by date
  posts.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Write to JSON file
  fs.writeFileSync(outputPath, JSON.stringify(posts, null, 2));
  console.log(`Generated ${posts.length} posts to posts.json`);
}

buildPosts();