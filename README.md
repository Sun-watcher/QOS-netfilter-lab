Ce projet vise à explorer et mettre en œuvre des mécanismes de Qualité de Service (QoS) et de filtrage réseau via NetFilter dans un environnement simulé. L'objectif principal est de contrôler et optimiser le trafic réseau en utilisant des outils comme tc (Traffic Control) pour appliquer des politiques de QoS (limitation de débit, gestion des priorités via le champ TOS) et iptables pour marquer ou rediriger le trafic. Les expérimentations incluent :

La configuration de queues disciplinaires (RED, HTB, SFQ) pour gérer la congestion et allouer des bandes passantes différenciées.

L'utilisation de l'interface IFB pour appliquer la QoS sur le trafic entrant (ingress).

La classification du trafic basée sur le champ TOS (Type of Service) pour prioriser certains flux (p. ex., VoIP vs. téléchargements).

L'automatisation via des scripts Python pour déclencher des règles de QoS dynamiquement en réponse à des paquets forgés (avec hping3).
