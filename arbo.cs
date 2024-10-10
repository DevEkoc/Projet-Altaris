Projet_Altaris/
├── Altaris/                            # Répertoire du projet Django
│   ├── __init__.py                     
│   ├── asgi.py                         
│   ├── settings.py                     
│   ├── urls.py                         
│   ├── wsgi.py                         
│   └── static/                         
│       ├── images/                     
│       ├── js/                         
│       └── css/                        
├── manage.py                           
├── static/                             
│   ├── images/                         
│   ├── js/                             
│   └── css/                            
├── templates/                          
│   └── base.html                       
└── apps/                               
    ├── core/                           # Application de base, transversale
    │   ├── migrations/                 
    │   ├── static/                     
    │   │   └── core/                   
    │   │       ├── images/             
    │   │       ├── js/                 
    │   │       └── css/                
    │   ├── templates/                  
    │   │   └── core/                   
    │   │       └── index.html          
    │   ├── admin.py                    
    │   ├── apps.py                     
    │   ├── models.py                   
    │   ├── tests.py                    
    │   └── views.py                    
    ├── servants/                       
    │   ├── migrations/                 
    │   ├── static/                     
    │   │   └── servants/               
    │   │       ├── images/             
    │   │       ├── js/                 
    │   │       └── css/                
    │   ├── templates/                  
    │   │   └── servants/               
    │   │       └── list.html           
    │   ├── admin.py                    
    │   ├── apps.py                     
    │   ├── models.py                   
    │   ├── tests.py                    
    │   └── views.py                    
    ├── bureaux/                        
    │   ├── migrations/                 
    │   ├── static/                     
    │   │   └── bureaux/                
    │   │       ├── images/             
    │   │       ├── js/                 
    │   │       └── css/                
    │   ├── templates/                  
    │   │   └── bureaux/                
    │   │       └── detail.html         
    │   ├── admin.py                    
    │   ├── apps.py                     
    │   ├── models.py                   
    │   ├── tests.py                    
    │   └── views.py                    
    ├── some_other_app/                 # Autre application
    │   ├── migrations/                 
    │   ├── static/                     
    │   │   └── some_other_app/         
    │   │       ├── images/             
    │   │       ├── js/                 
    │   │       └── css/                
    │   ├── templates/                  
    │   │   └── some_other_app/         
    │   │       └── page.html           
    │   ├── admin.py                    
    │   ├── apps.py                     
    │   ├── models.py                   
    │   ├── tests.py                    
    │   └── views.py                    
    └── another_app/                    # Encore une autre application
        ├── migrations/                 
        ├── static/                     
        │   └── another_app/            
        │       ├── images/             
        │       ├── js/                 
        │       └── css/                
        ├── templates/                  
        │   └── another_app/            
        │       └── another_page.html   
        ├── admin.py                    
        ├── apps.py                     
        ├── models.py                   
        ├── tests.py                    
        └── views.py                    
