




const axios = require('axios');

const prompt = 'Hello, how are you?';
const max_tokens = 50;
const temperature = 0.5;
const apiKey = process.env.OPENAIKEY;


axios({
  method: 'post',
  url: 'https://api.openai.com/v1/engines/davinci-codex/completions',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+apiKey,
  },
  data: {
    prompt,
    max_tokens,
    temperature,
  },
})
  .then((response) => {
    console.log(response.data.choices[0].text);
  })
  .catch((error) => {
    console.error(error);
  });



  function includejQuery(callback) {
    if(window.jQuery)
    {
        // jQuery is already loaded, set up an asynchronous call
        // to the callback if any
        if (callback)
        {
            setTimeout(function() {
                callback(jQuery);
            }, 0);
        }
    }
    else
    {
        // jQuery not loaded, load it and when it loads call
        // noConflict and the callback (if any).
        var script = document.createElement('script');
        script.onload = function() {
            jQuery.noConflict();
            if (callback) {
                callback(jQuery);
            }
        };
        script.src = "http://code.jquery.com/jquery-2.1.1.min.js";
        document.getElementsByTagName('head')[0].appendChild(script);
    }
}