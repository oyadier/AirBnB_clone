Below are the models that this project use:

BaseModel:
This class is a super class for all classes in the AirBnB clone project

	it has a constructor the __init__ method.
		it takes in *args and **kwargs and verifies if its
		empty or not.
		if the kwargs is empty it creates a new instance and sets a
		unique id with created_at timestamp and updated_at timestamp

	The class also return a string representaion of the instance using
	__str__ method
	Save method - this method updates the updated_at and call save method
	from storage module to save the updated instance
	
	to_dict public method. It returns a dictionary of all the attributes
	of the instance in a key-value format, including the __class__ attribute
	The created_at and updated_at attributes are converted to ISo format

User:
The class that inherit from BaseModel. 
	It has the following public class attributes:
		email,
		password,
		firt_name,
		last_name,

State:
This class also inherit from BaseModel.
	It has one attribute called name, which is an emplty string


City:
This is another class that inherit from BaseModel.
	It has two public attributes
	state_id - an empty string
	name - an empty string


Amenity:
This class also inherit from BaseModel.
	It has one pulic attribute called name which is an empty string


Place:
Another class that inherit from BaseModel
	It has the following attributes
		city_id,
		user_id
		name,
		description,
		number_rooms,
		number_bathrooms
		max_guest,
		price_by_night,
		latitude,
		longitude,
		amenity_ids,


Review:
Last class that inherit from BaseModel
	It has three attributes
		place_id
		user_id,
		text,
