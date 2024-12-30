import pickle
import streamlit as st

st.set_page_config(
    page_title="Multiple App"
)
#baca model
pred_fruit = pickle.load(open('dataset/fruit_p.sav', 'rb'))

# judul web
st.title('Prediksi Jenis Buah metode perceptron')

# inputan

col1, col2 = st.columns(2)
with col1:
    diameter = st.number_input("Diameter", min_value=0.1, max_value=1000.0, value=4.47)
with col2:
    weight = st.number_input("Berat", min_value=0.1, max_value=1000.0, value=95.76)
with col1:
    red = st.number_input("Red", min_value=0, max_value=200, value=161)
with col2:
    green = st.number_input("Green", min_value=0, max_value=100, value=72)
with col1:
    blue = st.number_input("Blue", min_value=0, max_value=100, value=9)



#membuat tombol prediksi
if st.button('Prediksi Jenis Buah'):
    # Melakukan prediksi
    fruit_pred = pred_fruit.predict([[diameter, weight, red, green, blue]])
    
    # Mengubah hasil prediksi menjadi label
    fruit_label = "Jeruk" if fruit_pred[0] == 1 else "Anggur"
    
    # Menampilkan hasil prediksi
    st.success(f"Jenis Buah Yang Diprediksi = {fruit_label}")

    
