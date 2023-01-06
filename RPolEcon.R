library(ggplot2)

colnames(timeSeriesData)[1] <- 'Time'

# Basic line plot with points
plot(df$LeftPolicy,type = "o")
plot(df$RightPolicy,type = "o")
plot(df$LLAf,type = "o")
plot(df$LRAf,type = "o")
plot(df$RLAf,type = "o")
plot(df$RRAf,type = "o")

#y are LeftPolicy, RightPolicy, LLAf, LRAf, RLAf, RRAf
#x are 

#1.InfoA, InfoNA
#2.InfoA, InfoNA, Polarisation
#3.InfoA, InfoNA, Polarisation, CostLevelL, CostLevelR

model1 <- lm(LeftPolicy ~ InfoA + InfoNA, data = crossSectionData)
summary(model1)

model2 <- lm(RightPolicy ~ InfoA + InfoNA, data = crossSectionData)
summary(model2)

model3 <- lm(LLAf ~ InfoA + InfoNA, data = crossSectionData)
summary(model3)

model4 <- lm(LRAf ~ InfoA + InfoNA, data = crossSectionData)
summary(model4)

model5 <- lm(RLAf ~ InfoA + InfoNA, data = crossSectionData)
summary(model5)

model6 <- lm(RRAf ~ InfoA + InfoNA, data = crossSectionData)
summary(model6)

model1a <- lm(LeftPolicy ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model1a)

model2a <- lm(RightPolicy ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model2a)

model3a <- lm(LLAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model3a)

model4a <- lm(LRAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model4a)

model5a <- lm(RLAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model5a)

model6a <- lm(RRAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA, data = crossSectionData)
summary(model6a)

model1b <- lm(LeftPolicy ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model1b)

model2b <- lm(RightPolicy ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model2b)

model3b <- lm(LLAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model3b)

model4b <- lm(LRAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model4b)

model5b <- lm(RLAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model5b)

model6b <- lm(RRAf ~ InfoA + InfoNA + Polarisation + Polarisation * InfoA + Polarisation * InfoNA + CostLevelL + CostLevelR, data = crossSectionData)
summary(model6b)

library(texreg)
texreg(list(model1, model1a, model1b, model2, model2a, model2b))
texreg(list(model3, model3a, model3b, model6, model6a, model6b))
