// Serves the static site and sends the old workers.dev and www addresses to the main domain.
const MAIN = 'crewwearcustom.com';
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname;
    if (host.endsWith('.workers.dev') || host === 'www.' + MAIN) {
      url.protocol = 'https:';
      url.hostname = MAIN;
      url.port = '';
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
