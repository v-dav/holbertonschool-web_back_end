# :spider_web: Pagination

![Python](https://img.shields.io/badge/Python-3.7-blue?style=for-the-badge&logo=python&logoColor=white)

![1](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/bb8d9154-4c31-4941-b8d9-b40a2055cb8a)
![2](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/ec639613-963a-40b7-8412-469f84140504)
![3](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/0cc57c91-9e50-4704-bcc5-ee47d9e41eaa)


## 🧐 Project Overview

Welcome to the "Pagination" project! In this project, you'll explore advanced techniques for handling and presenting large datasets and gain insights into managing data efficiently, enhancing user experience, and ensuring resilience in the face of dataset modifications.

## ⚙️ Project Description

The "Pagination" project focuses on implementing effective pagination strategies for datasets. Here is three key learning objectives:

1. **Simple Pagination:**
   - Implement pagination using basic parameters such as `page` and `page_size`.
   - Gain the ability to navigate and display specific portions of a dataset seamlessly.

2. **Hypermedia Metadata:**
   - Explore the concept of paginating datasets with hypermedia metadata.
   - Learn how to enhance user navigation and discoverability through additional metadata.

3. **Deletion-Resilient Pagination:**
   - Implement pagination in a deletion-resilient manner.
   - Develop strategies to handle dataset modifications without compromising the integrity of pagination.

## 📖 Learning Objectives

Upon completing this project, you should be able to explain the following concepts without relying on external resources:

- How to paginate a dataset using simple parameters like `page` and `page_size`.
- How to implement pagination with hypermedia metadata for improved user interaction.
- How to create deletion-resilient pagination, ensuring consistency amid dataset modifications.

## Resources

1. **REST API Design: Pagination**
   - [Link to Resource](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)

2. **HATEOAS (Hypermedia as the Engine of Application State)**
   - [Link to Resource](https://en.wikipedia.org/wiki/HATEOAS)

##  🙇 Author

[Vladimir Davidov](https://github.com/v-dav) - Holberton School

---

# Personal Notes
![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/ac440e59-118b-42b9-8e67-2a496aeb7078)

## **Qu’est-ce que la pagination ?**

La pagination est le système qui permet de présenter un long contenu, ou des suites de produits en plusieurs pages successives.

Elle se matérialise à l’écran par la présence de petits boutons 1,2,3, 4 etc… en bas et/ou haut de l’écran pour passer d’une page à l’autre. Elle est utilisée sur les sites qui possèdent un grand volume de contenus et de pages (site e-commerce par exemple avec de nombreux produits disponibles à la vente).

## **Pourquoi paginer ?**

La pagination permet aux internautes de passer par exemple de la page 1 à la page 2 dans une même catégorie de produits, de passer de la page 8 à la page 9 pour accéder à des billets de blogs plus anciens, …..

La pagination présente deux grands intérêts :

- C’est un élément de navigation qui permet aux visiteurs d’accéder à toutes les pages de manière fluide et rapide.
- D’un point de vue [SEO](https://www.noiise.com/guide/seo/), elle permet aux robots des moteurs de recherche de visiter et d’indexer toutes les pages.

## **Les avantages de la pagination**

- Pas de temps de chargement excessif (contrairement à un système qui imposerait de devoir charger toutes les données sur une seule et même page).
- Navigation ergonomique.
- Permet de mettre en place des mécanismes de tri (tri par prix croissant, tri par catégorie de produits, par couleurs,…).
- Réduire le [taux de rebond](https://www.noiise.com/definition/taux-de-rebond/) sur les pages.
- Augmenter la durée moyenne des visites.
- Augmenter le nombre de pages vues.

## **Les limites de la pagination**

- Pour accéder aux éléments, produits, articles rédactionnels suivants, l’internaute doit cliquer. Il y a donc une action supplémentaire à réaliser. Selon les cas, ajouter un “clic” de plus peut freiner l’utilisation.
- Il faudra donc veiller à proposer un système de pagination (bouton d’action) visible et clair sur vos pages.

## **Les problèmes engendrés par la pagination**

Les systèmes de pagination peuvent entraîner plusieurs problèmes :

- Le contenu dupliqué : il y a des risques de duplication de contenu notamment au niveau des balises ([balise title](https://www.noiise.com/definition/balise-title/) et [meta description](https://www.noiise.com/definition/meta-description/)).
- L’[indexation](https://www.noiise.com/definition/indexation/) : les moteurs de recherche peuvent “oublier” de visiter certaines pages éloignées.
- La vitesse de chargement de la page.
- Risque de faire ressortir toutes les pages numérotées dans les résultats de Google, alors qu’elles concernent finalement un seul sujet.

## **Les problèmes de Google avec la pagination**

Deux difficultés principales pour Google :

- Son robot s’épuise et risque de ne pas crawler (c’est-à-dire visiter puis indexer) toutes vos pages.
- Comme il existe beaucoup de pages, il ne sait plus laquelle faire ressortir comme la plus pertinente dans ses résultats de recherche.

## Différents types de pagination

La pagination offset, la pagination par clé (keyset), et la pagination par recherche (seek) sont différentes approches de la pagination utilisées dans le développement web pour récupérer et afficher des enregistrements à partir d'une base de données ou d'une collection de données. Chacune de ces méthodes a ses avantages et ses inconvénients, et leur choix dépend des besoins spécifiques de l'application.

1. **Pagination Offset** :
    - **Fonctionnement** : La pagination offset, également appelée pagination par décalage, consiste à spécifier un nombre d'éléments à sauter (offset) depuis le début de la collection pour atteindre la page souhaitée. Par exemple, pour afficher la deuxième page avec 10 éléments par page, vous spécifiez un offset de 10 (10 éléments sont sautés).
    - **Avantages** : Facile à comprendre et à mettre en œuvre, convient bien lorsque vous avez un petit nombre de pages.
    - **Inconvénients** : Les performances peuvent se dégrader lorsque vous avez une grande quantité de données, car chaque page nécessite un saut de données coûteux.

1. **Pagination par Clé (Keyset)** :
    - **Fonctionnement** : La pagination par clé, également appelée pagination basée sur la clé, utilise une clé de tri (par exemple, une colonne de date ou d'ID unique) pour récupérer les enregistrements suivants ou précédents à partir de la dernière clé connue. Il n'y a pas d'offset, mais plutôt une référence à la dernière clé récupérée.
    - **Avantages** : Performances constantes, idéales pour les grands ensembles de données, aucun saut de données coûteux.
    - **Inconvénients** : Plus complexe à mettre en œuvre que la pagination offset, nécessite une clé de tri appropriée.
2. **Pagination par Recherche (Seek)** :
    - **Fonctionnement** : La pagination par recherche est similaire à la pagination par clé, mais elle permet aux utilisateurs de rechercher des éléments en fonction de critères de recherche spécifiques. Chaque demande inclut un marqueur de recherche (par exemple, une date ou une valeur) pour récupérer les éléments suivants ou précédents par rapport à ce marqueur.
    - **Avantages** : Flexibilité pour rechercher des éléments en fonction de critères spécifiques, performances constantes.
    - **Inconvénients** : Plus complexe à mettre en œuvre que la pagination offset, nécessite des critères de recherche appropriés.

Le choix entre ces méthodes dépend des exigences de votre application. La pagination par offset est simple mais moins adaptée aux grandes quantités de données. La pagination par clé est performante pour les grandes collections triées, tandis que la pagination par recherche est utile lorsque vous devez effectuer des recherches spécifiques dans vos données paginées. Chaque méthode a ses avantages et ses inconvénients, il est donc important de choisir celle qui convient le mieux à votre cas d'utilisation.

## How to paginate a dataset with simple page and page_size parameters

```python
def paginate(data, page, page_size):
    """
    Paginate a list of data based on page and page_size parameters.
    Args:
        data (list): The list of data to paginate.
        page (int): The page number to retrieve.
        page_size (int): The number of items per page.
    Returns:
        list: The paginated data for the specified page and page_size.
    """
    # Calculate the offset based on the page and page_size
    offset = (page - 1) * page_size
    
    # Retrieve the data for the specified page
    paginated_data = data[offset:offset + page_size]
    
    return paginated_data

# Create a list of numbers from 1 to 50
data = list(range(1, 51))

# Define the page and page_size parameters
page_number = 3  # Retrieve page 3
page_size = 10   # 10 items per page

# Paginate the data and print the result for page 3
result = paginate(data, page_number, page_size)
print(result)
```

## How to paginate a dataset with hypermedia metadata

La pagination d'un ensemble de données avec des métadonnées hypertexte (hypermedia metadata) signifie que, en plus des données paginées elles-mêmes, vous fournissez également des liens hypertexte pour faciliter la navigation entre les différentes pages de données. Cela rend votre API plus intuitive pour les clients, car ils peuvent suivre les liens pour accéder à la page suivante, à la page précédente ou à d'autres pages connexes.

Voici un exemple simple de code en Python pour illustrer la pagination avec des métadonnées hypertexte :

```python
:from flask import Flask, request, jsonify

app = Flask(__name__)

# Créez une liste de données à paginer
data = list(range(1, 101))  # Une liste de nombres de 1 à 100

@app.route('/paginate')
def paginate_data():
    page = int(request.args.get('page', 1))  # Récupérez le numéro de la page depuis les paramètres de requête
    page_size = int(request.args.get('page_size', 10))  # Récupérez le nombre d'éléments par page depuis les paramètres de requête

    # Calculez l'offset pour la pagination
    offset = (page - 1) * page_size

    # Extrait les éléments pour la page actuelle
    paginated_data = data[offset:offset + page_size]

    # Construisez des liens hypertexte pour la navigation
    links = {}
    if page > 1:
        links['prev'] = f'/paginate?page={page - 1}&page_size={page_size}'
    if offset + page_size < len(data):
        links['next'] = f'/paginate?page={page + 1}&page_size={page_size}'

    # Créez une réponse JSON avec les données paginées et les liens hypertexte
    response = {
        'data': paginated_data,
        'links': links
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

```

Dans cet exemple :

1. Nous utilisons Flask pour créer une petite application web.
2. Nous avons une liste de données `data` de 1 à 100 que nous souhaitons paginer.
3. L'URL `/paginate` est utilisée pour récupérer les données paginées. Nous utilisons les paramètres de requête `page` et `page_size` pour spécifier la page et le nombre d'éléments par page.
4. Nous calculons l'offset pour la pagination, puis extrayons les éléments de la page demandée.
5. Ensuite, nous construisons des liens hypertexte pour la navigation. Si une page précédente ou suivante est disponible, nous ajoutons les liens correspondants dans les métadonnées hypertexte.
6. Enfin, nous renvoyons une réponse JSON qui contient à la fois les données paginées et les liens hypertexte pour faciliter la navigation entre les pages.

## How to paginate in a deletion-resilient manner

La pagination de manière résiliente à la suppression signifie que vous gérez la pagination des données de manière à garantir que les éléments supprimés ne causent pas de problèmes pour les utilisateurs qui naviguent entre les pages. L'idée est de vous assurer que lorsque des éléments sont supprimés, les pages de données restent cohérentes et que les utilisateurs continuent à voir des résultats fiables.

Voici un exemple simple de code en Python pour illustrer la pagination résiliente à la suppression :

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Créez une liste de données à paginer
data = list(range(1, 101))  # Une liste de nombres de 1 à 100

@app.route('/paginate')
def paginate_data():
    page = int(request.args.get('page', 1))  # Récupérez le numéro de la page depuis les paramètres de requête
    page_size = int(request.args.get('page_size', 10))  # Récupérez le nombre d'éléments par page depuis les paramètres de requête

    # Calculez l'offset pour la pagination
    offset = (page - 1) * page_size

    # Extrait les éléments pour la page actuelle, en tenant compte des suppressions
    paginated_data = []
    for item in data[offset:]:
        if item is not None:  # Vérifiez si l'élément n'a pas été supprimé
            paginated_data.append(item)
            if len(paginated_data) == page_size:
                break

    # Construisez des liens hypertexte pour la navigation
    links = {}
    if page > 1:
        links['prev'] = f'/paginate?page={page - 1}&page_size={page_size}'
    if offset + page_size < len(data):
        links['next'] = f'/paginate?page={page + 1}&page_size={page_size}'

    # Créez une réponse JSON avec les données paginées et les liens hypertexte
    response = {
        'data': paginated_data,
        'links': links
    }

    return jsonify(response)

# Simulez la suppression d'éléments
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 1 <= item_id <= 100:
        data[item_id - 1] = None  # Marquez l'élément comme supprimé (None)
        return jsonify({'message': f'Élément {item_id} supprimé avec succès.'})
    else:
        return jsonify({'error': 'ID d\\'élément invalide.'}), 400

if __name__ == '__main__':
    app.run(debug=True)

```

Dans cet exemple :

1. Nous utilisons Flask pour créer une petite application web.
2. Nous avons une liste de données `data` de 1 à 100 que nous souhaitons paginer. Lorsque nous supprimons un élément, nous le marquons comme `None` pour indiquer qu'il a été supprimé.
3. L'URL `/paginate` est utilisée pour récupérer les données paginées, tandis que l'URL `/delete/<item_id>` permet de simuler la suppression d'éléments en marquant l'élément correspondant comme supprimé.
4. Lorsque nous paginons les données, nous vérifions si un élément est marqué comme supprimé (c'est-à-dire égal à `None`) avant de l'inclure dans la page paginée. Cela garantit que les éléments supprimés ne sont pas affichés.
5. Le reste du code est similaire à l'exemple précédent, avec la construction de liens hypertexte pour la navigation et la création d'une réponse JSON contenant à la fois les données paginées et les liens hypertexte.

Ainsi, ce code permet de gérer la pagination de manière résiliente à la suppression en excluant les éléments supprimés des pages paginées tout en maintenant la cohérence des données.
