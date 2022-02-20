import React, {useState} from "react";
import axios from 'axios';
import {Button} from "./Button";

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
            <form method='post' onSubmit={handleSubmit}>
                <label htmlFor='userSpeech'>How are you doing, buddy?</label>
                <textarea id='userSpeech'
                          placeholder="Tell me what's on your mind, I am all ears"
                          name='speech'
                          value={speech}
                          onChange={handleChange}
                />

                <Button type='submit' value="I have finished talking" />
            </form>
        </>
    );
}