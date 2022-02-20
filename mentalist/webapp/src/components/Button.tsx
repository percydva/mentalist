import React, {useState} from "react";
import axios from 'axios';

export const Button = (props) => {
    return(
        <button type={props.type} className='button'>{props.value}</button>
    );
}