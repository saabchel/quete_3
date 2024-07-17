import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate


st.sidebar.title("Menu")
onglet = st.sidebar.radio("Aller à", ["Accueil", "Photos"])


if onglet=="Accueil":

    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
# Appliquer la classe big-font au texte que vous souhaitez agrandir
    st.markdown('<p class="big-font">Bienvenue sur la page d accueil.</p>', unsafe_allow_html=True)
    st.image("https://th.bing.com/th/id/OIP.R_W0nztsGVhz90yLr-SeDwHaE8?w=280&h=187&c=7&r=0&o=5&pid=1.7",width=600)
elif onglet=='Photos':
# Nos données utilisateurs doivent respecter ce format

        lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
        'password': 'utilisateurMDP',
        'email': 'utilisateur@gmail.com',
        'failed_login_attemps': 0, # Sera géré automatiquement
        'logged_in': False, # Sera géré automatiquement
        'role': 'utilisateur'},
        'root': {'name': 'root',
        'password': 'rootMDP',
        'email': 'admin@gmail.com',
        'failed_login_attemps': 0, # Sera géré automatiquement
        'logged_in': False, # Sera géré automatiquement
        'role': 'administrateur'}}}

        authenticator = Authenticate(
            lesDonneesDesComptes, # Les données des comptes
            "cookie name", # Le nom du cookie, un str quelconque
            "cookie key", # La clé du cookie, un str quelconque
            30, # Le nombre de jours avant que le cookie expire 
        )

        authenticator.login()

        def accueil():
            st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")


        if st.session_state["authentication_status"]:

            st.markdown("""
                <style>
                .big-font {
                    font-size:30px !important;
                }
                </style>
                """, unsafe_allow_html=True)
                # Appliquer la classe big-font au texte que vous souhaitez agrandir
            st.markdown('<p class="big-font">Bienvenue sur mon album photo.</p>', unsafe_allow_html=True)
            col1,col2,col3=st.columns(3)
            with col1:
                st.header("Axelle")
                st.image("https://th.bing.com/th?q=Beau+Cheval+Marron&w=120&h=120&c=1&rs=1&qlt=90&cb=1&pid=InlineBlock&mkt=fr-FR&cc=FR&setlang=fr&adlt=moderate&t=1&mw=247",width=300)
            with col2:
                st.header("Samuel")
                st.image("https://th.bing.com/th/id/OIP.b6ieKa_B2QZsTItrkhGznwHaFp?w=233&h=180&c=7&r=0&o=5&pid=1.7",width=300)
            with col3:
                st.header("Coco")
                st.image("https://th.bing.com/th/id/OIP.Snyn6X2b-A4gyoxMAtT2GQHaE6?w=273&h=181&c=7&r=0&o=5&pid=1.7",width=300)




            accueil()
            # Le bouton de déconnexion
            authenticator.logout("Déconnexion")

        elif st.session_state["authentication_status"] is False:
            st.error("L'username ou le password est/sont incorrect")
        elif st.session_state["authentication_status"] is None:
            st.warning('Les champs username et mot de passe doivent être remplie')

       