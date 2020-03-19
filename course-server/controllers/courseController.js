const courses = [
  {
    id: 1,
    name: 'React - The Complete Guide',
    author: 'Maximilian Schwarzmüller',
    description:
      'This course is fully up-to-date with the latest version of React and includes React Hooks! Of course it will be kept up-to-date in the future',
    publisher: 'Academind',
    image:'http://resources.mynewsdesk.com/image/upload/c_limit,dpr_2.625,f_auto,h_700,q_auto,w_360/v6nif6xd9zisawu5sdar.jpg',
    page_url:'https://www.udemy.com/course/react-the-complete-guide-incl-redux/?utm_source=adwords&utm_medium=udemyads&utm_campaign=LongTail_la.EN_cc.ROW&utm_content=deal4584&utm_term=_._ag_77879424134_._ad_406614130440_._kw__._de_c_._dm__._pl__._ti_dsa-1007766171312_._li_1011806_._pd__._&matchtype=b&gclid=CjwKCAiAjMHwBRAVEiwAzdLWGI3zu8UgHDDNscwaF1vIdaa6Rsv7eQVapT9icZGzlzIPNZEN6kRwOhoCh2sQAvD_BwE',
    has_image: true,
  },
  {
    id: 2,
    name: 'NodeJS - The Complete Guide',
    author: 'Maximilian Schwarzmüller',
    description:
      'Join the most comprehensive Node.js course on Udemy and learn Node in both a practical as well as theory-based way!',
    publisher: 'Academind',
    image: 'http://pluspng.com/img-png/nodejs-logo-png--435.png',
    has_image: true,
    page_url:'https://www.udemy.com/course/nodejs-the-complete-guide/',
  },
  {
    id: 3,
    name: 'The Complete Junior to Senior Web Developer Roadmap (2020)',
    author: 'Andrei Neagoie',
    description:
      'Join a live online community of over 140,000+ developers and a course taught by an industry expert that has actually worked both in Silicon Valley and Toronto as a senior developer. Graduates of this course are now working at Google, Amazon, Apple, IBM, JP Morgan, Facebook + other top tech companies.',
    publisher: 'Andrei Neagoie',
    image: 'https://www.pngkey.com/png/full/252-2527722_our-portfolio-includes-over-100-web-development-projects.png',
    has_image: true,
    page_url:'https://www.udemy.com/course/the-complete-junior-to-senior-web-developer-roadmap/',
  }
];


function getCourses(req, res) {
  res.status(200).json(courses);
}

function getCourse(req,res)
{
  const courseId = parseInt(req.params.courseId, 10);
  const course = courses.find((c)=> c.id === courseId);
  res.status(200).json(course);
}

module.exports = { getCourses, getCourse };
