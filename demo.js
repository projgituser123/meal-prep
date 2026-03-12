let obj = {name : 'dvc', batch : 'd4', age:19, present : true, sub :["DM","COA","FSD2"], sports : { sname : "football", position : "cm", club: "psg"}}

    console.log(obj.name)
    console.log(obj.batch)
    console.log(typeof(obj.present))
    console.log(typeof(obj["age"]))
    console.log(obj["sub"])
    console.log(obj["sub"][1])
    console.log(typeof(obj["sub"][1]))
    console.log(obj.sports)
    console.log(obj.sports["sname"])

    console.log(obj.sports.position)

let infojson_obj = require ("./info.json")
console.log(infojson_obj)
console.log(infojson_obj.name)


let sub = {
        FSD : [{Topic : "HTML", course : "beginner", content : {tags : "table", form : "xyz"}} , 
    {Topic : "CSS", course : "beginner", content : ["tag", "tables","form"]}]
}
console.log(sub.FSD[0].content.tags)
console.log(sub.FSD[1].content[0])