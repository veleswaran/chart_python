let names = ["eat", "tea", "tan", "ate", "nat", "bat"];
let group = [];
for (let i = 0; i < names.length; i++) {
    let first = names[i].split("").sort().join("");
    let found = [];

    for (let j = 0; j < names.length; j++) {
        let second = names[j].split("").sort().join("");
        if (first === second) {
            found.push(names[j]);

        }
    }
    group.push(found);
}

let res = []
for (let i = 0; i < group.length; i++) {
    for (let j = i+1; j < group.length; j++) {
        if (i !== j) {
            if (group[i]!= undefined&&group[j]!=undefined &&group[i].toString() == group[j].toString()) {
                delete group[j]
            }
        }
    }
   
}

console.log(group);