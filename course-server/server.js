const express = require('express'); // import express package

const server = express(); // init server obj. with express
server.use(express.json()); // middleware for parsing JSON objects to js objects when receiving requests

// routes
const courseController = require('./controllers/courseController');
const router = express.Router();
router.get('/', courseController.getCourses); // route for fetching courses ( ex: http://localhost:3000/courses/)
router.get('/:courseId', courseController.getCourse); // route for fetching course by id (ex: http://localhost:3000/courses/3)
server.use('/courses', router);

server.listen(3000); // starting the server on port 3000 
