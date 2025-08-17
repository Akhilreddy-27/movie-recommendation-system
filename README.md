## 📸 Demo

### ⚡ Quick Look (GIF)
> A short walkthrough of searching a title and getting 5 similar recommendations.

![Streamlit App Demo](assets/demo.gif)

> If you don’t have a GIF yet, record one with **ScreenToGif** (Windows) or **Kap** (macOS) and save it as `assets/demo.gif`.

---

### 🖼️ Screenshots
<img width="1919" height="831" alt="Screenshot 2025-08-17 194319" src="https://github.com/user-attachments/assets/2b8cc735-7ca5-43b4-b6a0-8f6060daf724" />



> Save your PNGs in `assets/` and keep file names the same as above, or update the paths.

---

### 🕹️ How It Works (in the UI)
1. **Search** for a movie in the dropdown.
2. Click **Recommend**.
3. See the **Top 5 similar movies** computed using **cosine similarity** over preprocessed features.
4. (Optional) Click a recommendation to view **poster & details** (via TMDb API integration if enabled).

---

### 🧪 Example Output

Search: **"The Dark Knight"**  
Recommendations:
1. **Batman Begins**
2. **The Dark Knight Rises**
3. **Man of Steel**
4. **V for Vendetta**
5. **Watchmen**

*(Your exact list may vary based on preprocessing and dataset version.)*

---

### 🗂️ Required Files

Ensure these files are present at project root:

