# SOEN6611 - Team E(Summer'19) 
# Software Measurement Project

**The purpose of this project is to calculate the metrics for selected open source projects and find correlation between them.**

## Professor : Jinqiu Yang

## Team Members

|Student ID  | Name |
| :---:  | :---:  |
| 40059347  | Alekya karicherla  |
| 40069746  | Sai Krishna Alla  |
| 40071067  | Ezhilmani Aakaash  |
| 40057918  | Vigneswar Mourouguessin |
| 40042347  | Kasyap Vedantam |
****

## Software Metrics selected for project
> 1. Statement Coverage [Definition](https://en.wikipedia.org/wiki/Code_coverage)

> 2. Branch Coverage [Definition](https://en.wikipedia.org/wiki/Code_coverage)

> 3. Mutation Score [Definition](https://en.wikipedia.org/wiki/Mutation_testing)

> 4. McCabe Complexity [Definition](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

> 5. Code Churn [Definition](https://codescene.io/docs/guides/technical/code-churn.html)

> 6. Defect Density [Definition](https://maisqual.squoring.com/wiki/index.php/Defect_Density)
****

## Open Source projects selected
> 1. [Apache Commons – Configurations](https://commons.apache.org/proper/commons-configuration/) 

> 2. [Apache Commons – Codec](https://commons.apache.org/proper/commons-codec/)

> 3. [Apache Commons – Collections](https://commons.apache.org/proper/commons-collections/)

> 4. [Apache Commons – Math](https://commons.apache.org/proper/commons-math/)

> 5. [Apache Commons – Pool](https://commons.apache.org/proper/commons-pool/)
****

## How to Build Project
- Download [JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) and ensure JAVA_HOME environment variable is set and points to your JDK installation path
- Download [Apache Maven](https://maven.apache.org/download.cgi) and add the bin directory of the created directory apache-maven-3.6.1 to the PATH environment variable
- Execute the command ``` mvn clean install```
- These stackoverflow links helped in fixing maven build errors [link1](https://stackoverflow.com/questions/12533885/could-not-calculate-build-plan-plugin-org-apache-maven-pluginsmaven-resources) [link2](https://stackoverflow.com/questions/22481931/how-to-fix-maven-maven-configuration-and-maven-dependency-problems-in-eclipse)
****

## Coverage & Complexity Metrics Calculation( Metrics 1, 2 & 4)
- [x] How we implemented in our project?

We made use of **Jacoco**, a free code coverage library for Java, which has been created by the EclEmma team based on the lessons learned from using and integration existing libraries for many years.

Simply, we need to add the below dependency plugin to pom.xml 

```
<plugin>
   <groupId>org.jacoco</groupId>
   <artifactId>jacoco-maven-plugin</artifactId>
   <version>0.7.7.201606060606</version>
   <executions>
      <execution>
         <goals>
            <goal>prepare-agent</goal>
         </goals>
      </execution>
      <execution>
         <id>report</id>
         <phase>prepare-package</phase>
         <goals>
            <goal>report</goal>
         </goals>
      </execution>
   </executions>
</plugin>
```

After adding the code, execute ``` mvn clean install```

Report will be generated at target/site/jacoco/*.
****

## Mutation Score Calculation( Metric 3)
- [x] How we implemented in our project?

We perfomed the calculation of this metric using [PIT](http://pitest.org/).It is fast, easy to use, actively developed and supported.The reports produced by PIT are in an easy to read format combining line coverage and mutation coverage information.

To perform pit, we should add the below dependency plugin to pom.xml 
```
<plugin>
        <groupId>org.pitest</groupId>
        <artifactId>pitest-maven</artifactId>
        <version>1.4.2</version>
        <configuration>
            <outputFormats>
                <param>HTML</param>
                <param>CSV</param>
            </outputFormats>
        </configuration>
</plugin>
```
After adding the code, execute ``` mvn clean install``` and ```mvn org.pitest:pitest-maven:mutationCoverage```

Report will be generated at target/pit-reports/*.
****

## Code Churn Calculation( Metric 5)
- [x] How we implemented in our project?

Two versions of project need to be considered along with all the commits in between the versions. We used [cloc](http://cloc.sourceforge.net/#Overview) to count the lines of code and performed the below calculations sequentialy to obtain results


 - Firstly, execute command ``` cloc-1.64.exe proj_V1 ``` , this will provide loc of V1(Version 1)
 - Perform the same action for the next commit(if any) For eg: ``` cloc-1.64.exe proj_V1_Commit1 ```
 - Now execute command ``` cloc-1.64.exe -diff proj_V1 proj_V1_Commit1``` [Output](Metrics%20Calculations/cloc.png)
 - Calcualte LOC(Modified+Added) for all commits between versions and for version2 as well.
 - Relative Churned Code = Summate all calculated LOC's(Modified+Added)/ version2 LOC
 
 **Please refer the documentation with screen shots attached** [Click Here](Metrics%20Calculations/Metric%205%20Calculation%20with%20Screenshots.docx)
 
_Note_: We have only considered added & modified lines during calculation of churned LOC(Deleted lines generally have less impact on the evolution of the system).May be taking deleted lines of code into account seperately provides a better view of the actual change that took place.

****

## Post Defect Density Calculation( Metric 6)
- [x] How we implemented in our project?

Inorder to calculate this metric, defects after project release need to be counted from issue tracker. In our case JIRA is the issue tracker
 - Firstly, should navigate to issue tracker page. (Project main page --> Issue tracking --> All Apache Bugs)
 - Click on Advanced link, enter query ``` porject =xxx and afectedVersion = xx ORDER BY key desc ```
 - Take count of bugs [Refer to this image](Metrics%20Calculations/Metric%206%20Screenshot.JPG)
 - Defect Density = No.of Bugs/ Size of release 
 
 Size of release = LOC --> Calculated using cloc
 
****

## Correlation

****
