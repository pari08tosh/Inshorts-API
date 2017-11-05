# Inshorts API

Inshorts is an app which provides news from different sources and presents them under 60 words. This API Scraps content from the Inshorts website and provides it in easy to use JSON Format. 

## Categories

Supports all categories as on the Inshorts Website. These include - 

1. '' // blank to get top news from all categories
2. national //Indian National News
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke // Unconventional
12. science
13. automobile

## Usage

### 1. GET Request

Make a get request of the form 
```
http://{site_address}/news?category={category_name}
```
Example - http://www.exampleapi.com/news?category=science

### 2. POST Request

Make a post request with the category, provided as form data with name 'category' to the same route as above i.e '/news'.

## Response Format

The response JSON Object looks something like this - 

```JSON
{
    "category": "science",
    "data": [
        {
            "author": "Gaurav Shroff",
            "content": "NASA-backed Starlight program has selected tardigrades and a roundworm species as Earth's first interstellar voyagers who would exit the solar system on a laser-powered spacecraft. Tardigrades, also called water bears, are regarded as the most resilient life forms on Earth. The eight-legged micro-animal can survive for 30 years without food or water and endure temperatures from -270ºC to 150ºC.",
            "date": "04 Nov 2017,Saturday",
            "imageUrl": "http://images.newsinshorts.com.edgesuite.net/app_assets/images/2017/4nov/inshorts_image_1509767709444_984.jpg?resize=400px:*",
            "readMoreUrl": "http://www.deepspace.ucsb.edu/projects/ets?utm_source=inshorts&utm_medium=referral&utm_campaign=fullarticle ",
            "time": "12:38 pm",
            "title": "\nTardigrades selected among 1st species to leave solar system\n",
            "url": "https://www.inshorts.com/en/news/tardigrades-selected-among-1st-species-to-leave-solar-system-1509779328721"
        },
        {
            "author": "Gaurav Shroff",
            "content": "India, with the launch of ₹450-crore Mangalyaan mission on November 5, 2013, became the only country to reach the Martian orbit on its maiden voyage. Mangalyaan, also Asia's first successful Mars mission, recently completed three years in orbit despite being designed to last just six months. Notably, only 21 of the 51 previous attempts to reach Mars were successful.",
            "date": "05 Nov 2017,Sunday",
            "imageUrl": "http://images.newsinshorts.com.edgesuite.net/app_assets/images/2017/5nov/inshorts_image_1509863191507_302.jpg?resize=400px:*",
            "readMoreUrl": "https://www.theverge.com/2014/9/24/6837745/india-spacecraft-reaches-mars-orbit-less-than-gravity?utm_source=inshorts&utm_medium=referral&utm_campaign=fullarticle ",
            "time": "12:49 pm",
            "title": "\nIndia's Mangalyaan only mission to reach Mars in 1st attempt\n",
            "url": "https://www.inshorts.com/en/news/indias-mangalyaan-only-mission-to-reach-mars-in-1st-attempt-1509866348359"
        },
    ],
    "success": true
}
```

Each response object has the following keys -

1. **success** - true indicates the api ran successfully. Upon error the success value is false and the object includes an errorMessage key with the error message.

    ```JSON
    {
        "category": "sciencedfg",
        "data": [],
        "errorMessage": "Invalid Category",
        "success": false
    }
    ```

2. **category** - the category you requested for.

3. **data** - An array of objects each containing a news item for the category. Each object contains 
    * title 
    * content
    * author 
    * imageUrl 
    * readMoreUrl(link to original news article)
    * date and time of publish
    * url (link to inshorts page)

## Installation and Setup

All dependencies are listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo pip freeze -r requirements.txt
    ```

2. Start the api server

    ```bash 
    $ python app.py
    ```


