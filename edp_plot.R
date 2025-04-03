ggplot()+
  geom_line(data =avg_edp, mapping = aes(x=z,y=Ser),, color = "red")+
  geom_line(data =avg_edp, mapping = aes(x=z,y=Phos),, color = "green4")+
  geom_line(data =avg_edp, mapping = aes(x=z,y=Gly),, color = "green")+
  geom_line(data =avg_edp, mapping = aes(x=z,y=Carb),, color = "orange")+
  geom_line(data =avg_edp, mapping = aes(x=z,y=CH2),, color = "purple")+
  #geom_line(data =avg_edp, mapping = aes(x=z,y=CH2E),, color = "purple4")+
  geom_line(data =avg_edp, mapping = aes(x=z,y=CH3),, color = "cyan4")+
  #geom_line(data =avg_edp, mapping = aes(x=z,y=CH1E),, color = "orange4")+
  geom_line(data =avg_wat_edp, mapping = aes(x=z,y=Wat),, color = "blue2")+
  geom_line(data =total_edp, mapping = aes(x=avg_wat_edp.z,y=total),, color = "grey4")+
    # Add labels for each line
  geom_text(data = avg_edp, aes(x = 45, y = 0.05, label = "Ser"), color = "red", vjust = -0.5) +
  geom_text(data = avg_edp, aes(x = 45, y = 0.08, label = "Phos"), color = "green4", vjust = -0.5) +
  geom_text(data = avg_edp, aes(x = 45, y = 0.1, label = "Gly"), color = "green", vjust = -0.5) +
  geom_text(data = avg_edp, aes(x = 45, y = 0.15, label = "Carb"), color = "orange", vjust = -0.5) +
  geom_text(data = avg_edp, aes(x = 45, y = 0.18, label = "CH2"), color = "purple", vjust = -0.5) +
  #geom_text(data = avg_edp, aes(x = 45, y = 0.38, label = "CH1E"), color = "orange4", vjust = -0.5) +
  #geom_text(data = avg_edp, aes(x = 45, y = 0.35, label = "CH2E"), color = "purple4", vjust = -0.5) +
  geom_text(data = avg_edp, aes(x = 45, y = 0.21, label = "CH3"), color = "cyan4", vjust = -0.5) +
  #geom_text(data = avg_edp, aes(x = 45, y = 0.3, label = "CH3E"), color = "cyan4", vjust = -0.5) +
  geom_text(data = avg_wat_edp, aes(x = 45, y = 0.27, label = "Wat"), color = "blue2", vjust = -0.5) +
  geom_text(data = total_edp, aes(x = 45, y = 0.45, label = "Total"), color = "grey4", vjust = -0.5) +
  labs(title = "DPPS All-Atom Electron Density Profiles (EDP)", y = "EDP") +
  theme_minimal()
