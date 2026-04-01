const https = require('https');

https.get('https://digital.tattooprojects.com/', (res) => {
    let rawData = '';
    res.on('data', (chunk) => { rawData += chunk; });
    res.on('end', () => {
        console.log('--- SITE ANALYSIS ---');
        console.log('1. GSAP & ScrollTrigger:', rawData.toLowerCase().includes('gsap') || rawData.toLowerCase().includes('scrolltrigger') ? 'Found' : 'Not direct in HTML');
        console.log('2. Lenis Smooth Scroll:', rawData.toLowerCase().includes('lenis') ? 'Found' : 'Not direct in HTML');
        console.log('3. WebGL / Three.js:', rawData.toLowerCase().includes('three') || rawData.toLowerCase().includes('webgl') ? 'Found' : 'Not direct in HTML');
        console.log('4. WebGL Shaders (GLSL):', rawData.toLowerCase().includes('gl_fragcolor') || rawData.toLowerCase().includes('varying') ? 'Found' : 'Not direct in HTML');
        
        const videos = rawData.match(/<video[^>]*>/g);
        console.log('5. Videos embedded in HTML:', videos ? videos.length : 0);
        if (videos) {
            console.log('Video tags checking lazy loading attribute:', videos.join('\n'));
        }
        
        const scripts = rawData.match(/src="([^"]+\.js[^"]*)"/g);
        if (scripts) {
            console.log('\n--- BUNDLES TO INSPECT ---');
            scripts.slice(0, 5).forEach(s => console.log(s));
        }
    });
}).on('error', (e) => {
    console.error(e);
});
