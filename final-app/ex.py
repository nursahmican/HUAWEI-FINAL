a = {
   "predicted_label":"Normal",
   "scores":[
      [
         "Normal",
         "1.000"
      ],
      [
         "Other_Abnormalities",
         "0.996"
      ],
      [
         "Age_Related_Macular_Degeneration",
         "0.685"
      ],
      [
         "Diabetes",
         "0.685"
      ],
      [
         "Hypertension",
         "0.107"
      ]
   ]
}
empty_dict = {}
for i in a["scores"]:
    empty_dict[i[0]] = i[1]

print(empty_dict)    