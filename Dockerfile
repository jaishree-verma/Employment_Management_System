# Build Stage (Using official Maven image so local wrapper scripts are not needed)
FROM maven:3.9.9-eclipse-temurin-17-alpine AS build
WORKDIR /app

# Copy POM file and pre-fetch dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy source code and compile project
COPY src src
RUN mvn clean package -DskipTests

# Production Run Stage
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Copy built Spring Boot executable JAR
COPY --from=build /app/target/employee-management-0.0.1-SNAPSHOT.jar app.jar

# Expose HTTP port
EXPOSE 8080

# Execute Application
ENTRYPOINT ["java", "-jar", "app.jar", "--spring.profiles.active=h2"]
