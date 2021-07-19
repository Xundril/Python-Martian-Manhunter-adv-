SELECT * FROM articles
    LEFT JOIN article_categories ac ON articles.id = ac.articles.id
    LEFT JOIN category c ON  ac.category_id = c.id;