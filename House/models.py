from turtle import position
from django.db import models
from customers.models import Customer



'''
FONCTINALITER 
Client
    I => Hotel et residance
    
    Un service pour la recherche des hotels les plus proche de sa position
    Un service de reservation d'une chanbre d'hotel 
    Payer sa reservation 
    Demander un remboursement (en gros un system de payement et de remboursement de sa reservation)
    Trouver une residance meublé 
    
    II => Maison en location
    
    Voir la lite des maison en location 
    Voir les detail d'une maison en location 
    Contacter l'agent 
    Enregistre une recherche
    
    NB : Reflechir pour voir entre l'agent et le client qui peux bien payer 
    
    

Hotel/Residance:

    1 . Enregistre Son Hotel (Nom,Description,lat ,long,...,mainImage,contact)
    2 . Enregistre une chanbre (Type,Nombre place ,clim ,ventiler,television ,douche ,prix_pour_une nuit, prix pour une heure,main_image,other image,movies )
    3 . Accepter/Refuser une reservation (si refus : Specifier le motif) 
    4 . Marque la disponibliter d'une chambre 
    5 . Demander une vercement de font 
    6 . Ajouter / Supprimer un gerant 
    6 . ...

Agent:

    1 . Ajouter une maison 
    2 . Manager les maison ajouter 
    
    

MODELS 

    Customer 
        phone(required)
        name(required),
        lastName(required),
        email (!required),
        immage (!required),
        userType (ad,ag,ag_h) ad = Admin ,af = agent,ag_h = ag_hotel
        

    hotel
        agent:Customer (required)
        title,
        description,
        star_count(!required),
        room_number(!required),
        lat (required)
        long (required)
        main_phone (required)
        other_phone (!required)
        main_image (required)
        room_status: (available,no_availble)
        hotel_service:HotelService ManytoMany
        
    NB : Envisager les parking picine bar sale de sport ,sale de reception ,sale de conferance 
            (Pour les grand hotels et autres)
    HotelService
        name,
        icon,
        for : (Hotel|Room) 
        
    Room
        hotle: Hotel (required)
        title (Ex Chambre 2D)
        description 
        room_size (Ex 40 m ) (!required)
        main_image (required)
        bed_place (required)
        room_widget :HotelService
        nithe_price 
        hour_price 
        tree_days_price 
        curency (Default XOF)
        nigth_start_hour (La nuit commence a partir de ...)
        night_end_hour (La nuit prend fin a partir de ....)

    RoomImage
        room:Room,
        image_link,
        ... other image property
        
    ReservationComment    
        title,
        description

    RoomReservation:
        room:Room,
        client:Customer,
        status
        client_note : 0 a 5 etoile 
        client_comment_select : ReservationComment
        client_comment_description
        
        NB trouver commen la reservation d'hotel se fait sur les app d'hotelerie 
        
        
     
    


    
    
    
    
    
    


    
    
    
    
    



'''

class HouseType(models.Model):
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    description = models.TextField(null= True)
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.name

class HousePayementPeriod(models.Model):
    name = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    sympbole = models.CharField(max_length=3)
    description = models.TextField(null= True)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.name
    

   
class House(models.Model):
    agent = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer_house")
    
    main_image = models.URLField()
    garage_number = models.IntegerField()
    
    house_type = models.ForeignKey(HouseType,related_name="house_type_house",on_delete=models.CASCADE)
    toilLet_number = models.IntegerField()
    address_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    price_payment_period = models.ForeignKey(HousePayementPeriod,on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=12,decimal_places=10,)
    lon = models.DecimalField(max_digits=12,decimal_places=10)
    
    created_at = models.DateTimeField(auto_now=True)
    updeted_at = models.DateTimeField(auto_now_add=True,)
    detedt_at = models.DateTimeField(null= True)
    
    def __str__(self) -> str:
        return self.address_name
    
    
    

 
