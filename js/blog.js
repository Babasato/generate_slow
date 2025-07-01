// Wait until page loads
document.addEventListener('DOMContentLoaded', function() {
  const blogContainer = document.getElementById('blog-posts');
  
  // Sample posts data (replace with real fetch later)
  const posts = [
    {
      title: "Complete Setup Guide",
      excerpt: "Transform math time from chaos to calm.",
      image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80",
      url: "/blog/example-post"
    }
  ];

  // Add posts to page
  posts.forEach(post => {
    blogContainer.innerHTML += `
      <article class="glass-card rounded-xl overflow-hidden blog-card">
        <img src="${post.image}" alt="${post.title}" class="w-full h-48 object-cover">
        <div class="p-6">
          <h3 class="text-xl font-bold mb-2">${post.title}</h3>
          <p class="text-gray-600 mb-4">${post.excerpt}</p>
          <a href="${post.url}" class="text-purple-600 font-medium">Read More →</a>
        </div>
      </article>
    `;
  });
});