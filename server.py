from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)

recipe_data = {
    '1': {
        'name': 'Feta Salad',
        'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg',
        'supplies': {
            '1': {
                'name': 'Cutting Board',
                'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
            },
            '2': {
                'name': 'Bowl',
                'image': 'https://www.heathceramics.com/cdn/shop/products/large-serving-bowl-opaque-white-heath-ceramics_108-05.jpg'
            },
            '3': {
                'name': 'Kitchen Knife',
                'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
            },
        },
        'ingredients': {
            '1': {
                'name': 'Ready to Serve Rice',
                'image': 'https://www.goya.com/media/8420/brown-heat-serve-rice.png?width=274'
            },
            '2': {
                'name': 'Greek Vinaigrette',
                'image': 'https://images.heb.com/is/image/HEBGrocery/000081144-1'
            },
            '3': {
                'name': 'Feta Cheese',
                'image': 'https://target.scene7.com/is/image/Target/GUEST_c63a48a6-c099-4522-a0bb-8932bf34a521?wid=488&hei=488&fmt=pjpeg'
            },
            '4': {
                'name': 'Cherry Tomatoes',
                'image': 'https://target.scene7.com/is/image/Target/GUEST_95c07dd1-974a-436b-8faa-808f100e7950?wid=488&hei=488&fmt=pjpeg'
            },
            '5': {
                'name': 'Avocadoes',
                'image': 'https://cdn.britannica.com/72/170772-050-D52BF8C2/Avocado-fruits.jpg'
            },
            '6': {
                'name': 'Black Olives',
                'image': "https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/64624093c4228d2fcce84d1e_99482416843-2023-cen-ecommerce-directship-ripelargepittedolives.jpg"
            }
        },
        'instructions': {
            '1': {
                'step': 'On a plate (or cutting board), cut the avocado and cherry tomatoes.',
                'image': 'https://feelgoodfoodie.net/wp-content/uploads/2023/10/How-to-Cut-an-Avocado-TIMG.jpg'
            },
            '2': {
                'step': 'In a microwave-safe bowl, combine rice mix and 2 tablespoons vinaigrette. Cover and cook on high until heated through, about 2 minutes.',
                'image': 'https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_center,w_730,h_487/k%2FPhoto%2FLifestyle%2F2021-04-Taste-Test-Microwavable-White-Rice%20%2FKitchn-2021-Microwave-Rice-Taste-Test-1'
            },
            '3': {
                'step': 'Divide between 2 bowls. Top with avocado, tomatoes, cheese, olives, remaining dressing and, if desired, parsley.',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVU5iTKckCfI0tZS0USg_g5kO_9L6fk4fjg7sqv5gA6VtB15zG'
            },
            '4': {
                'step': 'Mix it all up and add the rest of your dressing! And Enjoy!',
                'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg'
            },
        }
    },
    '2': {
        'name': 'Glazed Squash',
        'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/01/Coconut-Acorn-Squash_exps149543_TH132767C04_25_1bC_RMS.jpg',
        'supplies': {
            '1': {
                'name': 'Aluminum Foil',
                'image': 'https://www.allrecipes.com/thmb/BoxoiPyfiLYcAc2GWY2HVIURbzA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/102368196_aluminum-foil-2000-4af779937cc9438cbe9be9d54c1f2e34.jpg'
            },
            '2': {
                'name': 'Baking Sheet',
                'image': 'https://www.nordicware.com/wp-content/uploads/2021/04/44600_The_Big_Sheet_002_780x780__55006.1648753775.1280.1280.jpg'
            },
            '3': {
                'name': 'Kitchen Knife',
                'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
            },
            '4': {
                'name': 'Cutting Board',
                'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
            },
            '5': {
                'name': 'Spoon',
                'image': 'https://i.pinimg.com/originals/70/41/50/7041508df360f4517d9dc88b178c0419.png'
            }
        },
        'ingredients': {
            '1': {
                'name': 'Vegetable Oil',
                'image': 'https://i5.peapod.com/c/YS/YS0IE.jpg'
            },
            '2': {
                'name': 'Brown Sugar',
                'image': 'https://i5.walmartimages.com/asr/0d74547e-9e21-42f4-bb95-7dc1a85f907d.713258977353ca217077f6d73d545bf7.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF'
            },
            '3': {
                'name': 'Acorn Squash',
                'image': 'https://www.kroger.com/product/images/large/back/0000000004750'
            },
            '4': {
                'name': 'Black Pepper',
                'image': 'https://badiaspices.com/wp-content/uploads/2018/01/033844012311.jpg'
            },
            '5': {
                'name': 'Salt',
                'image': 'https://www.containerstore.com/catalogimages/212810/670060SaltOrPepperShaker2ozV2_600.jpg'
            },
        },
        'instructions': {
            '1': {
                'step': 'Cut the squash in half using a knife on a cutting board and scrape the seeds out with a spoon.',
                'image': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTu8IdrA9fyUjg84kK0DaFOfZKKTCVHkW1_8v_uGTEvI-UHzUZJ'
            },
            '2': {
                'step': 'Preheat the oven to 400 and add aluminum foil to a baking sheet with some oil covering the top.',
                'image': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTaw5eCwcMS4lKvpbD0NlMUf4W0pKvc4V8zh8Ye31J2NMGCl2GT'
            },
            '3': {
                'step': 'Lay squash pieces on baking sheets. Season with salt and pepper; sprinkle squashes evenly with half the sugar.',
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwwlrOMIC_F_nVt3mPj7RRmDKLxcbjd9AtTI53RdrAuR3dfmmG'
            },
            '4': {
                'step': 'Roast until sugar has melted, about 5 minutes. Remove baking sheets from oven.',
                'image': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRqvcVdfttkj8GzBnj2KaTyj7r-05gyNiFpndIgMnQ3iYQVuK0a'
            },
            '5': {
                'step': 'Flip the pieces over with a spoon. Season with salt and pepper; sprinkle evenly with remaining sugar. Roast until tender, about 20 minutes. Enjoy',
                'image': 'https://www.foodandwine.com/thmb/Q-4ciItjPFjSSQrUnHjt_TelVAs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/brown-sugar-roasted-acorn-squash-recipe-FT-BLOG1019-f14d448c609a4c09b595baa6fe04d7ec.jpg'
            },
        }
    },
    '3': {
        'name': 'Garlic Scallion Ramen',
        'image': 'https://www.kitchentreaty.com/wp-content/uploads/2020/01/super-simple-miso-ramen-5-420x560.jpg',
        'supplies': {
            '1': {
                'name': 'Pot',
                'image': 'https://www.ikea.com/us/en/images/products/hemkomst-pot-with-lid-stainless-steel-glass__1083743_pe859078_s5.jpg'
            },
            '2': {
                'name': 'Bowl',
                'image': 'https://www.heathceramics.com/cdn/shop/products/large-serving-bowl-opaque-white-heath-ceramics_108-05.jpg'
            },
            '3': {
                'name': 'Kitchen Knife',
                'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
            },
            '4': {
                'name': 'Cutting Board',
                'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
            }
        },
        'ingredients': {
            '1': {
                'name': 'Instant Noodles',
                'image': 'https://images.heb.com/is/image/HEBGrocery/prd-medium/001616095.jpg'
            },
            '2': {
                'name': 'Soy Sauce',
                'image': 'https://www.nikankitchen.com/Images/Products/kikkoman-shoyu-soy-sauce-150ml.png'
            },
            '3': {
                'name': 'Garlic',
                'image': 'https://i5.walmartimages.com/seo/Garlic-Bulb-Fresh-Whole-Each_a4f114d9-93ab-4d39-a8d6-9170536f57a9.f9f8e58c8e3e74894050c7c2267437e3.jpeg'
            },
            '4': {
                'name': 'Scallions',
                'image': 'https://www.purveyd.com/cdn/shop/products/SCALLION.jpg'
            },
            '5': {
                'name': 'Peanut Butter',
                'image': 'https://media.cdn.kaufland.de/product-images/1024x1024/6e563e9c36fe0c6dd539e823ec38e0ad.jpg'
            },
        },
        'instructions': {
            '1': {
                'step': 'Boil water in a pot and cook the noodles according to the package instructions.',
                'image': 'https://images.saymedia-content.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:eco%2Cw_1200/MjAyMjMxNzQ3NDk5MjcxMTgw/shutterstock_1816629980.jpg'
            },
            '2': {
                'step': 'Drain the noodles and set aside.',
                'image': 'https://media.blueapron.com/recipes/40165/recipe_steps/96835/1691526712-48-0019-5460/FP_Ramen_Stockpot_Web.jpg?width=512'
            },
            '3': {
                'step': 'On a cutting board, mince the garlic and chop the scallions.',
                'image': 'https://images.cutco.com/learn/2018/slice-green-onion-l.jpg'
            },
            '4': {
                'step': 'In a bowl, add the soy sauce, peanut butter, garlic, and scallions. Mix well.',
                'image': 'https://pinchofyum.com/wp-content/uploads/Peanut-Sauce-3.jpg'
            },
            '5': {
                'step': 'Add the noodles to the bowl and mix well. Enjoy',
                'image': 'https://i0.wp.com/thefoodiediaries.co/wp-content/uploads/2022/01/img_1427.jpg'
            },
        }
    }
}

quiz_data = {
    1: {
        'name': 'Feta Salad',
        'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg',
        'problems': {
            1: {
                'q_type': 'drag',
                'prompt': 'For how long do you have to microwave the precooked rice? Drag the correct timer to the microwave!',
                'prompt_image': 'https://cdn.standardmedia.co.ke/evemedia/eveimages/friday/thumb_how_to_cook_rice_in_5a740518774e1.jpg',
                'responses': {
                    '1': 'https://png.pngtree.com/png-vector/20220912/ourmid/pngtree-vector-two-minutes-icon-minutes-single-meter-vector-png-image_14498820.png',
                    '2': 'https://png.pngtree.com/png-vector/20220524/ourmid/pngtree-five-minutes-stopwatch-symbol-illustration-isolated-vector-png-image_13637774.png',
                    '3': 'https://png.pngtree.com/png-clipart/20230804/original/pngtree-fifteen-minutes-stopwatch-alarm-background-countdown-vector-picture-image_9508599.png',
                },
                'correct_response': [1],
                'response_type': 'drag',
                'points': 1
            },
            2: {
                'q_type': 'chop',
                'prompt': 'Drag the knife to the avocado to chop! Click the button when you think you finished chopping!',
                'image': '',
                'responses': {
                    1: 'Cut avocados',
                    2: 'Cook rice',
                    3: 'Blend salad',
                },
                'correct_response': '1',
                'response_type': 'dl'
            },
            3: {
                'q_type': 'mcq',
                'prompt': 'Which of these supplies is NOT needed in creating Feta Salad?',
                'image': '',
                'responses': {
                    1: 'Kitchen knife',
                    2: 'Blender',
                    3: 'Cutting board',
                    4: 'Bowl'
                },
                'correct_response': '2',
                'response_type': 'ul',
            },
            4: {
                'q_type': 'drag',
                'prompt': 'Drag all the microwave safe items to the microwave',
                'prompt_image': 'https://pngimg.com/d/microwave_PNG15719.png',
                'responses': {
                    '1': 'https://static.vecteezy.com/system/resources/previews/032/545/950/original/front-view-a-glass-of-water-isolated-on-transparent-background-png.png',
                    '2': 'https://png.pngtree.com/png-clipart/20230930/original/pngtree-blue-ceramic-bowl-png-image_13022408.png',
                    '3': 'https://em-content.zobj.net/source/twitter/348/takeout-box_1f961.png',
                    '4': 'https://smidge.co.uk/media/catalog/product/cache/91221817c87827cfdd170d83789c1ac6/s/m/smid104-01.png',
                    '5': 'https://pak-man.com/images/detailed/1/10J10.png',
                    '6': 'https://png.pngtree.com/png-vector/20231017/ourmid/pngtree-colorful-plastic-cups-and-plates-isolated-png-image_10225358.png'
                },
                'correct_response': [1, 2, 6],
                'response_type': 'drag',
                'points': 3
            }
        },
    },
    2: {
        'name': 'Glazed Squash',
        'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/01/Coconut-Acorn-Squash_exps149543_TH132767C04_25_1bC_RMS.jpg',
        'problems': {
            1: {
                'q_type': 'drag',
                'prompt': 'What should the squash look like when putting it in the oven? Drag the correct state of squash to the oven.',
                'prompt_image': 'https://image-us.samsung.com/SamsungUS/dacor/products/cooking/built-in-oven/dob30t977ss/mobile/1-Product-DOB30T977SS-PLP-Mobile.png?$DC_290_232_PNG$',
                'responses': {
                    '1': 'https://www.pngarts.com/files/11/Acorn-Squash-PNG-Photo.png',
                    '2': 'https://png.pngtree.com/png-clipart/20210829/original/pngtree-pumpkin-crop-planting-nutritious-fruit-png-image_6673485.jpg',
                    '3': 'https://seedstosuccess.com/wp-content/uploads/2022/11/Roasted-Acorn-Squash-e1669839645107-276x300.png'
                },
                'correct_response': [3],
                'response_type': 'drag',
                'points': 1
            },
            2: {
                'q_type': 'mcq',
                'prompt': 'How many times do you flip squash over when roasting?',
                'responses': {
                    1: '2',
                    2: '4',
                    3: 'trick question, 1',
                },
                'correct_response': 3,
                'response_type': 'ul'
            },
            3: {
                'q_type': 'drag',
                'prompt': 'For how much time do you roast the squash after flipping it? Drag the correct timer to the squash',
                'prompt_image': 'https://www.foodandwine.com/thmb/Q-4ciItjPFjSSQrUnHjt_TelVAs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/brown-sugar-roasted-acorn-squash-recipe-FT-BLOG1019-f14d448c609a4c09b595baa6fe04d7ec.jpg',
                'responses': {
                    '1': 'https://png.pngtree.com/png-clipart/20230813/original/pngtree-icon-symbolizing-clock-and-timer-for-measuring-15-minutes-of-time-passage-vector-picture-image_10530824.png',
                    '2': 'https://png.pngtree.com/png-vector/20220518/ourmid/pngtree-icon-for-passage-of-time-clock-and-timer-displaying-20-minutes-vector-png-image_35564356.png',
                    '3': 'https://png.pngtree.com/png-clipart/20230813/original/pngtree-icon-of-a-clock-and-timer-representing-the-passage-of-time-for-45-seconds-vector-picture-image_10530833.png',
                },
                'correct_response': [2],
                'response_type': 'drag',
                'points': 1
            },

            4: {
                'q_type': 'drag',
                'prompt': 'Drag all the seasonings you use on the squash throughout the recipe',
                'prompt_image': 'https://freepngimg.com/save/127290-acorn-ripe-squash-hd-image-free/600x580',
                'responses': {
                    '1': 'https://pngimg.com/d/salt_PNG7.png',
                    '2': 'https://www.mccormick.com/-/media/project/oneweb/mccormick-us/mccormick/products/00052100004488_a1c1.png',
                    '3': 'https://www.gfresh.com.au/wp-content/uploads/2021/02/G-Fresh_Refillable-Grinder_Black-Pepper_No-Box_646x858.png',
                    '4': 'https://d1e3z2jco40k3v.cloudfront.net/-/media/project/oneweb/clubhouseca/products/club-house/clubhouse-garlic-powder.png',
                    '5': 'https://pngimg.com/d/sugar_PNG98785.png',
                    '6': 'https://waterbutlers.com/cdn/shop/products/Screen-Shot-2019-10-19-at-10.26.32-PM_692x.png'
                },
                'correct_response': [1, 3, 6],
                'response_type': 'drag',
                'points': 3
            }
        }
    },
    3: {
        'name': 'Garlic Scallion Ramen',
        'image': 'https://www.kitchentreaty.com/wp-content/uploads/2020/01/super-simple-miso-ramen-5-420x560.jpg',
        'problems': {
            1: {
                'q_type': 'drag',
                'prompt': 'For how long should you cook the noodles? Drag the correct instructions to the pot!',
                'prompt_image': 'https://recipes.net/wp-content/uploads/2023/12/how-to-cook-perfect-spaghetti-noodles-1701663956.jpg',
                'responses': {
                    '1': 'https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-icon-of-a-clock-and-timer-indicating-the-passage-of-30-seconds-vector-png-image_32606746.png',
                    '2': 'https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-icon-representing-the-passage-of-time-clock-and-timer-set-for-5-minutes-vector-png-image_32606752.png',
                    '3': 'https://qph.cf2.quoracdn.net/main-qimg-966ad16a2753b04f467252c85724ca0a.webp',
                },
                'correct_response': [3],
                'response_type': 'drag',
                'points': 1

            },
            2: {
                'q_type': 'mcq',
                'prompt': 'What should you do after cooking the noodles?',
                'responses': {
                    1: 'Eat the noodles',
                    2: 'Drain the noodles and set aside',
                    3: 'Add sauces to the noodles',
                },
                'correct_response': 2,
                'response_type': 'ul'
            },
            3: {
                'q_type': 'drag',
                'prompt': 'Drag the ingredients used for the sauce into the bowl',
                'prompt_image': 'https://www.heathceramics.com/cdn/shop/products/large-serving-bowl-opaque-white-heath-ceramics_108-05.jpg',
                'responses': {
                    '1': 'https://media.wegetanystock.co.uk/brandbank/images/8715035150102/1',
                    '2': 'https://cdn.gardengrocer.com/attachments/photos/high_res/395.png?9340',
                    '3': 'https://i.pinimg.com/originals/cf/95/f7/cf95f7a9a402160e883887b882107745.png',
                    '4': 'https://www.pngmart.com/files/23/Milk-Carton-PNG-Transparent.png',
                    '5': 'https://png.pngtree.com/png-clipart/20230113/ourmid/pngtree-red-fresh-tomato-with-green-leaf-png-image_6561484.png',
                    '6': 'https://png.pngtree.com/png-vector/20221123/ourmid/pngtree-fresh-fruit-cut-lemon-png-image_6153348.png'
                },
                'correct_response': [1, 2, 3],
                'response_type': 'drag',
                'points': 3
            },
            4: {
                'q_type': 'chop',
                'prompt': 'Drag the knife to the scallion to chop it. When you think its been fully chopped, click the button!',
                'responses': {
                    1: 'Fun fact: scallions are also called green onions!',
                },
                'correct_response': 1,
                'response_type': 'dl'
            }
        }
    }
}

hint_data = {
    0: {
        'name': 'Draining Options',
        'recipe_id': '3',
        'steps': {
            1: {
                'instructions': 'Empty a pot into a colander held in the sink.',
                'img': 'https://cdn.apartmenttherapy.info/image/upload/f_jpg,q_auto:eco,c_fill,g_auto,w_1500,ar_16:9/k%2FEdit%2Fshutterstock_1781025173',
                'alt': 'Person emptying a pot full of noodles into a colander placed in a sink.',
            },
            2: {
                'instructions': 'Cover the pot with a lid and open slightly as you ',
                'img': 'https://qph.cf2.quoracdn.net/main-qimg-ced01ea966c6ef0272ac200ad151b7a2-lq',
                'alt': 'Person emptying'
            },
            3: {
                'instructions': 'Pour the water out carefully, with no cover, as to not let all the noodles spill out.',
                'img': 'https://content.api.news/v3/images/bin/f255ac556d14a7ac610ad6c51f565322',
                'alt': ''
            }
        }
    },
    1: {
        'name': 'Mincing Garlic',
        'recipe_id': '3',
        'img': 'https://www.deliciousmeetshealthy.com/wp-content/uploads/2020/03/Process-Shots-how-to-mince-garlic.jpg',
        'alt': 'An image divided into four quadrants, each a visual representation of the steps to mince garlic.',
        'pre_step': 'Remove some of the outer husks by pulling them apart with your fingers:',
        'steps': {
            1: 'Lay a clove flat on your cutting board and trim away the root end with the tip of your knife. Lay the flat side of your knife over the clove while holding the handle. With the heel of your other hand, carefully give your knife a gentle whack',
            2: 'Cut each clove into 4 or 5 pieces or slices',
            3: 'Turn the garlic cloves, cutting the pieces into 4 slices again.',
            4: 'Move your knife from left to right and back again, until the garlic is first finely chopped and then minced.',
        }
    },
    2: {
        'name': 'Cutting Avocados',
        'recipe_id': '1',
        'steps': {
            1: {
                'instructions': 'Cut it in half, lengthwise',
                'img': 'https://images.wsj.net/im-148170/square',
                'alt': 'An image of somebody cutting an avocado lengthwise with a knife'

            },
            2: {
                'instructions': 'Gently twist the halves apart',
                'img': 'https://toriavey.com/images/2014/01/Avocado-3-292x219.jpg',
                'alt': 'An image of somebody twisting the halves of a cut avocado apart.'
            },
            3: {
                'instructions': 'Use a knife to firmly whack the seed. Gently turn the knife and pull– the seed should come out',
                'img': 'https://www.savorythoughts.com/wp-content/uploads/2022/07/How-To-Cut-An-Avocado-Savory-Thoughts-4.jpg',
                'alt': 'An image of somebody whacking the exposed seed of an avocado cut in half lengthwise.'

            },
            4: {
                'instructions': 'Peel off the skin and then cut as desired',
                'img': 'https://www.bhg.com/thmb/4pykRKlyKx7aPN8rTZsaD7nyhoo=/1919x0/filters:no_upscale():strip_icc()/peeling-skin-off-avocado-7jRJDOFwaEbBhISHkFlt83-e5f0be859df04996ab17365c2e326310.jpg',
                'alt': 'An image of the skin of half an avocado being peeled'

            },
        }
    },
    3: {
        'name': 'Microwave-Safe Dishes',
        'recipe_id': '1',

        'safe': ['Glass dishes', 'Ceramic dishes', 'Plastic dishes'],
        'unsafe': ['Styrofoam', 'Cardboard', 'Metals, stainless steel, foil', 'Single-use plastics, to-go containers']
    },
    4: {
        'name': 'Preheating an Oven',
        'recipe_id': '2',
        'steps': {
            1: {
                'instructions': 'If you have an electric oven, you can set the oven to the desired temperature and it will ding when ready',
                'img': 'https://www.pcrichard.com/dw/image/v2/BFXM_PRD/on/demandware.static/-/Sites-pcrichard-master-product-catalog/default/dw94bbe4aa/images/hires/Z_WFE775H0HZ.jpg?sw=800&sh=800&sm=fit',
                'alt': 'An electric oven.'
            },
            2: {
                'instructions': 'But gas ovens do not alert you when the temperature is reached. For these ovens wait 15-20 min after setting the temperature',
                'img': 'https://mobileimages.lowes.com/productimages/1c380e57-3c07-4711-a037-46f5ba183592/49870314.jpg',
                'alt': 'A gas oven.'
            }
        }
    },
}
cooking_mama = {
    1: {
        'name': 'Feta Salad',
        'images': {
            1: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWLULuW9zKSOygTLRRIQ4bdvz1COYRcIMIHE-HLDHfgyinueA-j_WljABZU9aFwsUccxlT0vbPIVlTANg3uBdVaFIeDsJjyvFXIb8ZPsrNN4gbKJhtoaYUYVzAXknrnoy-zD9iuTNHL-AhkGsDCriRlhRBbrSyqzM-6iuxpS0_hjWWoIOgpf_1VrMhXHFl/s320/Screen%20Shot%202024-05-01%20at%207.22.05%20PM.png',
            2: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOpydCEc26-BKIP6Z1Ie9B1GKOeQLtL3GehaA3zSMoBr8Q__3Oy_4FtDzHLmaHziw1BrXfOfN4xzEvXDcMmh5SikvkbnqRG6Cq8JA-Yd74_Jo4hHtxmyiWwu8kKoNbgpApnWkpbQLPLGOslAOA2_gqzLRA3JVQx-9EQNCY6jH1I3qxSQXIBJRYMd2yTPTn/s320/Screen%20Shot%202024-05-01%20at%207.22.09%20PM.png',
            3: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOhREU3r0BToIL7Ck4YsU9iOHoJPeADwrDXw0zEcL9jGBIWmgJMygXQVrYkDwU2WX0ax2dbNPozbTNKnmJzgyobT-xy1xqo0MnHfQ_jOf23zj3eKfiqUP6kwiMA1_ckVIwq2sF5E7IkVApoIsha1Hs5EaVSPH538uCm3A1XSXrrT5VE_KGtE4i3UY0I2wi/s320/Screen%20Shot%202024-05-01%20at%207.22.13%20PM.png',
            4: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbVAG0VnBX6rXbYDbyzkAjNTs62C4YqntU3RBdESw8uROZ1fkjHxlkGSdCy1YOIYrxmGGVBlzO6rKr74q8MTkfZMcYPKYw6zLu9uxBqxXcNywTY2n4-MpUJ8VKb9jbMrZ6Dkq_HFNy5Mj8H9Ner1c2X3_erNGy6lMZ5B6gcLpcoAVi5rG_fKedVGD9CagI/s320/Screen%20Shot%202024-05-01%20at%207.22.18%20PM.png',
            5: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjyAMsQ3k3LRE7GhFJn0c_afOqEP30QmzphurPeR-6JmGVnAyBTSi0NNXJhgL6tdLIN4zfCzTIbltAzsrJSKs0NLwhB39oyIJSdXRn18xcpbQcE62Z9p5qT39nw6PTNqzT7Z_uAjCkZ2JfLFsBzDLp39Rcs7rjGyrYRUSkvZbBNIAPT8u6McLooNRijTHT/s320/Screen%20Shot%202024-05-01%20at%207.22.22%20PM.png',
            6: 'https://upload.wikimedia.org/wikipedia/commons/5/59/Empty.png'
        },
        
        'choppedImages': {
            1: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_mabPApHXmgOD_xHUA_cqvx_-w9vmMh67y970BLOja0crQYie3W_2nbZ9A7XNf4J5MPZkLFFvGk4Hc5zBeP5obtUEeXWNNLuqTh4Cq0QixH7NWd6sD3X5VomfraNlvkwpI3vSmHjnfNUTmOTBAuwd2W_-9HWkxif0JyP_pPncrAzpRGcOTvJPKXSJylnW/s320/Screen%20Shot%202024-05-01%20at%207.22.27%20PM.png',
            2: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEge8q5A6E_LkSNTC-8LGSVONVZuFx0XF22iRJAkjdJVyH6OLvvninO830o3rjxSZmMH4d9awg2VKyMf31uxbJANhyyT5CbdzQ1Mwiy78ppTJm4kmoeFTpcWbv-QYxMYYSwNdLIsn90tEdv8UC0pGoNIeNlpFeaaBDyMVi79Zhjttufe2ib49ocFwVFDVt3t/s320/Screen%20Shot%202024-05-01%20at%207.22.30%20PM.png',
            3: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUyiek9SMOHNwy668vqEWkAk0QYVi0EYLnl_3ykVfygg320E_4roaHXW6Ny02viX7o_AE-1z7VrZf6nElMelPpWEcQNvhnj0MOm05NMNZIGXpUepKqH89EULuRg7N0k9NIp3eN9q96SY00ZI3sZb3mUlBu9WrrMtjzdUqv7auORWFczHi9fTU-fe1U9f3A/s320/Screen%20Shot%202024-05-01%20at%207.22.33%20PM.png',
            4: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZwhKATGFtMAhLWomITr5qcMf8qXTmTpJzWY1zphfLuh48gz48Zbyh2OgZk9vZmLJAzJ5xX88GVbBweuHbtZAZBP1ex3LfQr40re_ao5IQRU-rjNeO2aSC_o0daPDS2gvNiUgYdEfQevXPXMhUssbOGsylUqZjfQ_GxY7gEaA9vhro2qxeFRoTZjYeITvE/s320/Screen%20Shot%202024-05-01%20at%207.22.39%20PM.png',
            5: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEho4Ii21flDdETFiEL9KxhwB0AxvpRmmFKum-bxDf3W4jrzg4IBBjFP8zVbZu3sati5tgL7K78usxiQMovHNwFNkkyDhOXr3zFP8C8P2QqdeZEFDJuSUIQfe-Ot0_fAb4xF0CXPM15BZMofMNA2a_EPdCmlX671ZPJNQYPRTEbQhG-RcCULh13AdC1dtz_E/s320/Screen%20Shot%202024-05-01%20at%207.22.51%20PM.png'        }
    },
    3: {
        'name': 'Garlic Scallion Ramen',
        'images': {
            1: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSiCh7Qtqdai9pm6EbLPgVFq8yF6IVP0tQCsoNnLBcBKq2H7JhXOaKzCYBufSKgYoPaFzuowJMVQpgc4LFi8XeNsJy6rIKq-1GfhSpiasu_SBcdIeUCCPOJNRWVuBFusi46gKCGIJKht3hy6YibGNH2a-qPahaOnkeqCoWPrz7rJ0lm3R3c8df70wGwS9J/s320/Screen%20Shot%202024-04-29%20at%201.30.09%20AM.png',
            2: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEithQJCZaKY4FkbVldJGo5gtpMDkhgVpOtolmD71HqLoqoU_-KCAvAHnKQeeqwQ9bsoGllke2LIaTCbD0aWaZYco0hskm6z4z_WUAzp7fuJlkVoPbnOf3OT9-QBk6CPbbKI6CUtNQrgHygSyOtTIz9FX-s7JAlzHKSW3m0ztDN3fGpVi9vbzWNKAU4HoSwP/s320/Screen%20Shot%202024-04-29%20at%201.30.14%20AM.png',
            3: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqYXZo5bYx22Vc_nQZ8Mnj4CMHtzJMVErSn983sEY3b77d-UnQ8djKV5C34IGhcJ_FT66ynZhZc1dO8Bfn9RfeZevqpj4iMR2MsQaLz7O4RDZBl9F4mpi0IfAV_74-1MThgQp3MTroTb_Er0iAKxhT9JNr889YX2GrxooCe-ZyfTzNLOoO83D6Sg1ssxIF/s320/Screen%20Shot%202024-04-29%20at%201.30.19%20AM.png',
            4: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhICiS6iiHlGZLWn0LuqIdeHDFamA53nVk7OLoRDvObaI9g5lSRmIV5d7SSp0RBDWmSTS1ofexKhe5xuwigvoyxNeYCs0cx58ueR7WxChckygm5A4v_-15K1VFRBMaQuquRfiSSv9dNv0CEHKRDfko9xjnv8ial_XPYKY-uUHxkxYU2OJXSQaVqXQDwQubv/s320/Screen%20Shot%202024-04-29%20at%201.30.21%20AM.png',
            5: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIVzNgJPx7aCUT-l8T3zHT4cGLmeA3fZgqOTQaFNhdB1lH1zgIFLyvEs71OvbQrM-gGc-ks4SK5MW_au7uBBL7bC4pnR04A7iI6rus5UhTjz4O6SB1fXVmD0yluLxvrw3hhcU_rT2UMIYP-yO1kDQ_FaPHEow9brfLBbLaIwuXzbucwsI2P3C1bkyMb_MT/s320/Screen%20Shot%202024-04-29%20at%201.30.23%20AM.png',
            6: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie-tu73vlZdcj0AraZeSqzv5IJVY2eKyC35XmJLU9qRkeftGaO0NLTNviHWhSaltMAEGTWLC7fTP6ocZSeAeoK3qUdZyZCfqGGVFoVtjuBjaLiPaHImm_x_ingqroFiSOYb4QWm4WcGquMmJLjbWFDh8pgfv-fcUl5-gZruCmWWQBmg5f5XEhmkWr_wv4B/s1600/Screen%20Shot%202024-04-29%20at%201.30.26%20AM.png',
            7: 'https://upload.wikimedia.org/wikipedia/commons/5/59/Empty.png'
        },
        
        'choppedImages': {
            1: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMOUev3k_8GGu651GiXbfn9UKfKGRUL8G37_k9PIqZ4NK9XCtwV9dM2bqI-r2Iy1j3AIbtYSSGQp3dx0c8e5bNrkGqqWUWU0iikif-fcLXvdUpYGxCifgxyb2t5Onk1KHixtxRYa4Q-7NOe2nM0eTqFpHTJBoYHgT7yfzSwVwe3wFE4LrWxc7_7toKe8wj/s1600/Screen%20Shot%202024-04-29%20at%201.36.09%20AM.png',
            2: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQXBFyy-z-WbXgBrOZMLI4opUlEI-Lbv5e78SYKiEa8W1DlHNl4C4Aud7_NBWIsESpUa7Tmht9YwpOdv-Egn1QCdqlBlXDuet1L5xWwhD66ca58DxVlD5aw9X5gxoDzGNF-DSh420v1KPJi2Pysrbs403peO18oz4lFycwGlZQrRvakH9wbigjrwoAlduF/s1600/Screen%20Shot%202024-04-29%20at%201.36.11%20AM.png',
            3: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiGqTzegePkHBJRQ-g65J3L6iUQ_EMlMF-r1M0yWfAb_C6qMEXqCZUa2d8-gTdXpTmTuzlx5TEnfVvgQIScl9DZfslY94L950SS9Iv8NjIWhNG8oQFeu3epnCWhidoA6X9q3XywoXkTflzktyHayLNUdQRoBmxiFedEcLBgAAW5L4_uShrr1rn2_R2zpwZq/s1600/Screen%20Shot%202024-04-29%20at%201.36.12%20AM.png',
            4: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgq1-lqok5-DdO5OcO9J-mNNdT-o8kd4gGpdIMEyKXxKyEl5aoPJkjdn9OpKwvKOfpRZjNLKmgbogPIX-w7X63Cv8Zee5E6qmJD8RfMWSU4oNI4n9wY7fBCghZ4DXmUz2ctnxP3ux_PRg37YkOGSqgDxAS9kP38IDY_z-NFbSerfEp8IUkqVMU7L3TjcJA3/s1600/Screen%20Shot%202024-04-29%20at%201.36.16%20AM.png',
            5: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRFRYOJ8C5_SfPmbzxy1yammksa-4k0Spu1LSk6XeSnqUrQs_Yx3a8VoSMkqoi9ISXpIIpFP9B60Zlm5YHRNOsHNLOLYyZJlMXtl8saN-B7x89GYEyRtqJLdPhWsStfcByo8O4G9h1oQQjISSAly4xynNXeRD40-RNmQSY3Tf81YVMWTJIzI9lkLv6hHgv/s320/Screen%20Shot%202024-04-29%20at%201.36.18%20AM.png',
            6: 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid5MeE7lS9Y4BYsCKyaQyDxj6-xHGLRAzZNlNuxdYQ14_Fuv-HA6nxlfYplAXnw_G05bDlb32O2ciMULKv04imHEvdD3JoboicFTvGtY-mqCc4LVeNj-gVdgG_TuUckIW7W4RMAGSdHyVGKhR9iFJFRb1aelD-g1NlnNpBdhHzOl7Tv5VkVKleoOxs_VDT/s320/Screen%20Shot%202024-04-30%20at%2012.04.09%20AM.png'
        }
    }
}
score = 0.0


@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')


@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')


@app.route('/test_recipe/<quiz_id>')
def quiz_start(quiz_id: int):
    quiz_info = quiz_data[int(quiz_id)]
    return render_template('quiz_start.html', id=quiz_id, name=quiz_info['name'], image=quiz_info['image'])


@app.route('/test_recipe/<quiz_id>/problems/<problem_id>', methods=['GET', 'POST'])
def quiz_problem(quiz_id: int, problem_id: int):
    global score
    quiz_info = quiz_data[int(quiz_id)]
    problem = quiz_info['problems'][int(problem_id)]
    problem_type = problem['q_type']
    drag_items = None
    drop_image = None

    if problem_type == 'drag':
        drag_items = problem.get('responses')
        drop_image = problem.get('prompt_image')
    else:
        drag_items = {}
        drop_image = ""

    if request.method == 'POST':
        data = request.json
        print(data)
        if data['point']:
            score += float(data['point'])
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    return render_template('quiz_problem.html', id=quiz_id, problem_id=problem_id, problem=problem,
                           total_problems=len(quiz_info['problems']), drag_items=drag_items, drop_image=drop_image, cooking_mama=cooking_mama)


@app.route('/score', methods=['GET', 'POST'])
def update_score():
    global score
    if request.method == 'POST':
        print(request.json)
        score += float(request.json['point'])
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/test_recipe/<quiz_id>/score')
def quiz_score(quiz_id):
    global score
    quiz_info = quiz_data[int(quiz_id)]
    if score < 0:
        final_score = 0
    else:
        final_score = "{:.2f}".format(score)
    score = 0.0
    return render_template('quiz_score.html', id=quiz_id, score=final_score, total_problems=len(quiz_info['problems']))


@app.route('/hints')
def hints_start():
    return render_template('hint_start.html', hints=hint_data)


@app.route('/hints/<hint_id>')
def helpful_hint(hint_id):
    return render_template('hint.html', hint_id=int(hint_id), hint=hint_data[int(hint_id)])



@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipe_data)


@app.route('/get_quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)


@app.route('/learn_recipe/<recipe_id>')
def recipe(recipe_id):
    return render_template('recipe.html', recipe_id=recipe_id, name=recipe_data[recipe_id]['name'],
                           image=recipe_data[recipe_id]['image'])
    # return render_template('supplies_ingredients.html', recipe_id = recipe_id)


@app.route('/learn_recipe/<recipe_id>/supplies')
def supplies(recipe_id):
    return render_template('supplies_ingredients.html', recipe_id=recipe_id,
                           supplies=recipe_data[recipe_id]['supplies'], key='Supplies')


@app.route('/learn_recipe/<recipe_id>/ingredients')
def ingredients(recipe_id):
    return render_template('supplies_ingredients.html', recipe_id=recipe_id,
                           ingredients=recipe_data[recipe_id]['ingredients'], key='Ingredients')


@app.route('/get_supplies_ingredients/<recipe_id>', methods=['GET'])
def get_supplies_ingredients(recipe_id):
    return jsonify(recipe_data[recipe_id])


@app.route('/learn_recipe/<recipe_id>/instructions')
def instructions(recipe_id):
    return render_template('instructions.html', recipe_id=recipe_id,
                           instructions=recipe_data[recipe_id]['instructions'])


@app.route('/get_instructions/<recipe_id>', methods=['GET'])
def get_instructions(recipe_id):
    return jsonify(recipe_data[recipe_id]['instructions'])


if __name__ == '__main__':
    app.run(debug=True)
