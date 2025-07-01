// /js/blog.js - Complete working version
document.addEventListener('DOMContentLoaded', function() {
  const blogContainer = document.getElementById('blog-posts');
  
  // Show loading state
  blogContainer.innerHTML = `
    <div class="col-span-3 text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-600"></div>
      <p class="mt-4 text-white">Loading math resources...</p>
    </div>
  `;

  // Fetch posts from Netlify-generated index
  fetch('/blog/index.json')
    .then(response => {
      if (!response.ok) throw new Error('Failed to load posts');
      return response.json();
    })
    .then(posts => {
      // Clear loading state
      blogContainer.innerHTML = '';
      
      // Display first 3 posts
      posts.slice(0, 3).forEach(post => {
        blogContainer.innerHTML += `
          <article class="glass-card rounded-xl overflow-hidden blog-card">
            <img src="${post.image}" alt="${post.title}" 
                 class="w-full h-48 object-cover" 
                 loading="lazy">
            <div class="p-6">
              <h3 class="text-xl font-bold mb-2">${post.title}</h3>
              <p class="text-gray-600 mb-4">${post.excerpt || post.description}</p>
              <a href="/blog/${post.slug}" 
                 class="text-purple-600 font-medium hover:text-purple-800 transition-colors">
                Read More →
              </a>
            </div>
          </article>
        `;
      });
    })
    .catch(error => {
      console.error('Blog loading error:', error);
      blogContainer.innerHTML = `
        <div class="col-span-3 text-center py-12 text-white">
          <p class="text-lg mb-2">We're having trouble loading our math resources.</p>
          <p class="text-sm">Please refresh the page or check back later.</p>
        </div>
      `;
    });
});
