/**
 * Backend Notes — Client API Helper
 * Clean client-side integration with FastAPI endpoints:
 * - GET /api/playlist
 * - GET /api/chapters
 * - GET /api/chapters/{id}
 * - GET /api/transcripts/{name}
 * - GET /api/health
 */

const BackendAPI = {
  baseUrl: window.location.origin,

  async getPlaylist() {
    try {
      const res = await fetch(`${this.baseUrl}/api/playlist`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      console.warn("API fallback: using local playlist info", err);
      return null;
    }
  },

  async getChapters(category = 'all') {
    try {
      const url = category && category !== 'all' 
        ? `${this.baseUrl}/api/chapters?category=${encodeURIComponent(category)}`
        : `${this.baseUrl}/api/chapters`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      console.warn("API fallback: using embedded chapters data", err);
      return null;
    }
  },

  async getChapterById(id) {
    try {
      const res = await fetch(`${this.baseUrl}/api/chapters/${id}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.json();
    } catch (err) {
      console.warn(`API fallback: could not fetch chapter ${id}`, err);
      return null;
    }
  },

  async getTranscript(chapterName) {
    try {
      const res = await fetch(`${this.baseUrl}/api/transcripts/${encodeURIComponent(chapterName)}`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return await res.text();
    } catch (err) {
      console.warn(`API fallback: transcript error for ${chapterName}`, err);
      return null;
    }
  },

  async checkHealth() {
    try {
      const res = await fetch(`${this.baseUrl}/api/health`);
      return res.ok;
    } catch {
      return false;
    }
  }
};

window.BackendAPI = BackendAPI;
