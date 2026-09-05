# Build Stage
FROM eclipse-temurin:17-jdk-alpine AS build
WORKDIR /app

# Copy Maven wrapper & POM
COPY mvnw .
COPY mvnw.cmd .
COPY .mvn .mvn
COPY pom.xml .

# Grant execution permission to mvnw
RUN chmod +x mvnw

# Download dependencies
RUN ./mvnw dependency:go-offline -B

# Copy source code and build package
COPY src src
RUN ./mvnw clean package -DskipTests

# Production Stage
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Copy built JAR from build stage
COPY --from=build /app/target/employee-management-0.0.1-SNAPSHOT.jar app.jar

# Expose server port
EXPOSE 8080

# Run Spring Boot Application
ENTRYPOINT ["java", "-jar", "app.jar", "--spring.profiles.active=h2"]
