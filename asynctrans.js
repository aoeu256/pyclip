let API = 'AIzaSyD3w-IaISfJRO_yvac_pD0EUKcQ-dZ6lf8';

async translate(text) {
    let res = await axios.post(
    `https://translation.googleapis.com/language/translate/v2?key=${API}`,
    { q: text, target: "tr" }
    );
    let translation = res.data.data.translations[0].translatedText;
    return translation;
  }

let subsUrl = ytInitialPlayerResponse.captions.playerCaptionsTracklistRenderer.captionTracks[0].baseUrl;
let subs = await (await fetch(subsUrl)).text();
let xml = new DOMParser().parseFromString(subs,"text/xml");
let textNodes = [...xml.getElementsByTagName('text')];
let subsText = textNodes.map(x => x.textContent).join("\n").replaceAll('&#39;',"'");