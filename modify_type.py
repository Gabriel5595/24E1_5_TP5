def modify_type(tipo_atual):
  if tipo_atual in ["Artístico/Cultural/Folclórico", "Gastronômico", "Religioso", "Moda", "Comercial ou Promocional", "Científico ou Técnico"]:
      return "Fechado"
  else:
      return "Ar Livre"