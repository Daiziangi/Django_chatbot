import { pipeline } from '@xenova/transformers';

// Create a translation pipeline
const translator = await pipeline('translation', 'Xenova/nllb-200-distilled-600M');

// Translate text from Hindi to French
const output = await translator('जीवन एक चॉकलेट बॉक्स की तरह है।', {
    src_lang:'eng_Latn', tgt_lang:'zho_Hans'
});
console.log(output);
// [{ translation_text: 'La vie est comme une boîte à chocolat.' }]
