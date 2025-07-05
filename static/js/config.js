const config = {
    // Replace this with your deployed backend URL
    API_URL: process.env.NODE_ENV === 'production' 
        ? 'https://your-backend-url.com'  // Replace with your actual backend URL
        : 'http://localhost:5000'
}; 