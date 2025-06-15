# The updated code removes matplotlib references to fix the ModuleNotFoundError
# We skip rendering the VOCAVA Root Family Tree graph and show a textual summary instead

# (All code remains as is except this section:)

# --- VOCAVA: TREE OF TONGUES + ALT LINGUAL MODULES ---
st.markdown("---")
st.subheader("🌳 Draw the Tree of Tongues")
if root_counter:
    st.markdown("### 📊 Root Family Distribution:")
    for root, count in root_counter.items():
        st.markdown(f"- **{root}**: {count} words")
    st.info("⚠️ Graphical tree visualization disabled due to environment limitations (matplotlib not supported).")
else:
    st.info("Seed the lexicon to draw a meaningful root tree.")
