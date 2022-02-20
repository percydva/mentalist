import React, {useState} from "react";
import axios from 'axios';

export const SpeechForm = (props) => {
    const [speech, setSpeech] = useState('');

    const handleChange = (event: any) => {
        setSpeech(event.target.value);
    }

    const handleSubmit = (event: any) => {
        event.preventDefault();

        axios.post("./api/speech", {speech: speech})
            .catch((error) => {console.log("Cannot post speech!")});
    }

    return(
        <>
            <form onSubmit={handleSubmit}>
                <label htmlFor='userSpeech'>Speech</label>
                <input id='userSpeech'
                       type='text'
                       name='speech'
                       value={speech}
                       onChange={handleChange}
                />

                <input type='submit' value='Analyze speech'/>
            </form>
        </>
    );
}