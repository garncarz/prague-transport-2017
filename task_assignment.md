## Instructions

1. Read all the information carefully.
2. Create folder "hackathon"
3. Create file "hackathon/members.txt" with email address and name of all your teammates (NAME;EMAIL;\r\n) – we will send you entry passes
4. Prepare a team logo (150x150 px) "hackathon/logo.png"
5. Prepare public accessible webserver (you can use any hosting provider you like). Your solution will need to run there.
6. Create file "hackathon/answers.txt" where the first line will be the URL on your server for Task 1 and on the second line URL on your server for Task 2
7. Put all source files for task 1 in "hackathon/task1/"
8. Put all source files for task 2 in "hackathon/task2/"
9. Compress folder "hackathon" to ZIP file named "package.zip"
10. Sign in on praguehackathon.com
11. Upload your package.zip till the timer expires - 5 days
12. Keep task URLs alive and working until the decision will be made (23.4. is a safe choice)
13. Have fun


## Task 1

The development division of Simpleway Industries has decided to create a theoretical European Hyperloop travel network which would connect selected capital cities.

We have already spoke with a couple of construction companies and asked them to propose a technical solution and estimate investment costs for single direction lines – each Hyperloop line will be constructed independently.

Our network plan considers spoke and hub model with a main transfer station and Hyperloop depo. Some cities will not be connected due to the efficiency reasons. The current state of the way is to make the final decision where to build the hub so it meets the following requirements.

From the central station / hub it must have a direct or an indirect line to all cities. The direct connection has a price offer. The indirect connection has a connection via more than one city. Total cost (the sum of the construction cost of all single direction lines) of the network must be as low as possible.

Your task is to figure out the cheapest possible solution if any. If so, what kind of connections/lines we will need to create, how much it will cost, and what the location of the central station will be.

### Input data

The prices related to each city are confidential at the moment, thus, we use numerical IDs instead (starting from 0). The data sheet consists of the total number of cities. Individual IDs have values from 0..(n-1)

Each proposal always consists of an ID of the departing city, IDs of the arriving city, and the cost of the line in MM EUR The data are in the JSON format
Will be POSTed with JSON body to:

URL `http://<your-server>/<optional-folder>/task1/input`

```json
{
  "citiesCount" : 4,
  "costOffers" : [
    {
      "from" : 0,
      "to" : 1,
      "price" : 6
    },{
      "from" : 1,
      "to" : 2,
      "price" : 10
    },{
      "from" : 2,
      "to" : 1,
      "price" : 10
    },{
      "from" : 1,
      "to" : 3,
      "price" : 12
    },{
      "from" : 3,
      "to" : 2,
      "price" : 8
    },{
      "from" : 3,
      "to" : 0,
      "price" : 1
    }
  ]
}
```

### Output Data

Response JSON which will contain the following parameters.
- The feasibility parameter will contain true/false
- The totalCost parameter contains the sum of the total cost of the network
- The depotId parameter contains position of the central station/hub
- The recommended Offers parameter consists of suggested price offers in the same format as it is Input. There is no order parameter.

```json
{
  "feasible" : true,
  "totalCost" : 15,
  "depotId" : 3,
  "recommendedOffers" : [
    {
      "from" : 0,
      "to" : 1,
      "price" : 6
    },{
      "from" : 3,
      "to" : 0,
      "price" : 1
    },{
      "from" : 3,
      "to" : 2,
      "price" : 8
    }
  ]
}
```


## Task 2

An airport wants to deploy a new advanced technology for automatic airplane recognition based on various measurements at the runway. For the past month they measured noise level, brake distance and vibrations during landing. Here is a small part of the data:

Type | Noise-level (db) | Braking distance (m) | Vibrations (rms)
---- | ---------------- | -------------------- | ---
A380 | 103	            | 2130                 | 0.81
A380 | 101              | 2070                 | 0.88
737  | 94               | 1730                 | 0.82
737  | 96               | 1820                 | 0.79

Your job is to determine the airplane type based on this measurement.

### Input

- input will provide a training set of data based on the past measurements and sample data which needs to be classified
- its formatted in JSON

Will be POSTed with JSON body to:

URL `http://<your-server>/<optional-folder>/task2/input`

```json
{
  "measurements" : [
    {
      "type" : "A380",
      "noise-level": 103,
      "brake-distance": 2130,
      "vibrations": 0.81
    },{
      "type" : "A380",
      "noise-level": 101,
      "brake-distance": 2070,
      "vibrations": 0.88
    },{
      "type" : "737",
      "noise-level": 94,
      "brake-distance": 1730,
      "vibrations": 0.82
    },{
      "type" : "737",
      "noise-level": 96,
      "brake-distance": 1820,
      "vibrations": 0.79
    }
  ],
  "samples" : [
    {
      "id" : 1,
      "noise-level": 102,
      "brake-distance": 2105,
      "vibrations": 0.80
    },{
      "id" : 2,
      "noise-level": 97,
      "brake-distance": 1830,
      "vibrations": 0.80
    }
  ]
}
```

### Output

- response JSON which will contain the ID from the sample and detected type of the aircraft

```json
{
    "result" : [
        {
            "id" : 1,
            "type" : "A380"
        },{
            "id" : 2,
            "type" : "737"
        }
    ]
}
```
