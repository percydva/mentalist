import React from "react";

// function getAllHackers() {
//     const hackerData = fetch("./api/hacker")
//         .then(response => response.json())
//         .then(data => {
//             data.results.map((hacker) => {
//                 console.log(hacker.nickname);
//                 return hacker.nickname;
//             });
//         });
//         // console.log(hackerData);
//         return hackerData;
//         // .then(response => response.json())
//         // .then(data => console.log(data));
//     // console.log(hackerData);
// }

let getJson = async function(response) {
    return await response.json();
}

let getAllHackers = async function() {
    const hackerData = fetch("./api/hacker")
        .then( (response) => {
            const inJson = getJson(response);
            console.log(inJson);
        })

}
export const App = (props) => {
    const data = getAllHackers();
    return (
        <>
            <h1> Hello World 2</h1>
            <h2>This is Django REST API and React app</h2>
        </>
    );
}