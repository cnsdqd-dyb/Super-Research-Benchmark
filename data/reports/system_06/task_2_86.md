# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 52dc8029 | **Time:** 291.89s | **Cost:** $0.20593
--------------------------------------------------------------------------------

# Data Quality and Attribution Uncertainty in Climate Agreement Verification Using Remote Sensing: A Comprehensive Analysis

## Abstract

The verification of climate agreements, including the Kyoto Protocol and subsequent frameworks under the United Nations Framework Convention on Climate Change (UNFCCC), relies fundamentally on the accurate quantification of greenhouse gas emissions and removals. Remote sensing technologies have emerged as indispensable tools for monitoring treaty compliance, offering systematic observations of land cover, carbon stocks, and anthropogenic emission sources across spatial and temporal scales that ground-based observations alone cannot achieve. However, the integration of remote sensing data into formal verification frameworks introduces significant challenges related to data quality assurance, uncertainty quantification, and the attribution of observed changes to specific emission sources or sinks. This report examines the current state of data quality management and attribution uncertainty handling in climate agreement verification, analyzing the methodological frameworks established by the Intergovernmental Panel on Climate Change (IPCC), the technical approaches employed in operational monitoring systems, and the persistent gaps that limit the reliability of remote sensing-based verification. The analysis reveals that while substantial progress has been made in developing validation protocols and uncertainty characterization methods, challenges remain in harmonizing top-down observational approaches with bottom-up inventory methods, propagating uncertainty through complex processing chains, and attributing observed atmospheric enhancements to specific emission categories consistent with international reporting frameworks.

## 1. Introduction

### 1.1 The Role of Remote Sensing in International Climate Governance

The verification of international climate agreements presents unprecedented challenges in measurement, reporting, and verification (MRV) that extend far beyond the capabilities of traditional environmental monitoring approaches. Climate treaties such as the Kyoto Protocol and subsequent agreements under the UNFCCC require Parties to demonstrate measurable reductions in greenhouse gas emissions or enhancements in carbon sequestration with sufficient confidence to support claims of compliance or non-compliance. This requirement has driven the development of sophisticated monitoring systems that integrate remote sensing observations with ground-based measurements, inventory methodologies, and atmospheric modeling approaches [1].

Remote sensing technology offers unique capabilities for climate agreement verification that address several fundamental requirements of international environmental governance. Satellite-based observations provide systematic, consistent coverage of environmental parameters across national boundaries and over extended time periods, enabling the detection of changes in land cover, vegetation biomass, and atmospheric composition that serve as indicators of emissions and removals. The historical archive of satellite observations, extending back to the early 1970s with the Landsat program, provides essential baseline data for establishing reference conditions against which changes can be measured [1]. This temporal depth proves particularly valuable for establishing 1990 baseline carbon stocks as required under the Kyoto Protocol, where ground-based inventories from that period may be unavailable for many countries.

The application of remote sensing to climate agreement verification encompasses five primary domains identified in early assessments of treaty monitoring needs: the provision of systematic observations of relevant land cover; support for establishing historical carbon stock baselines; detection and quantification of land cover changes; quantification of above-ground vegetation biomass stocks and their changes; and mapping and monitoring of anthropogenic methane sources [1]. Each of these applications presents distinct technical challenges related to data quality, uncertainty characterization, and the attribution of observed changes to specific causes or sources.

### 1.2 The Verification Challenge

The fundamental challenge in climate agreement verification lies in the need to transform raw remote sensing observations into quantified estimates of greenhouse gas fluxes with known and appropriately characterized uncertainties. This transformation involves multiple processing stages, each introducing potential errors and uncertainties that must be quantified and propagated through the analysis chain to produce reliable final estimates. The complexity of this challenge is compounded by the diverse requirements of different climate agreements, which may specify different gases, source categories, spatial and temporal scales, and uncertainty thresholds for compliance assessment [2].

The IPCC has established good practice principles for greenhouse gas inventory development that provide the foundation for understanding how remote sensing data should be handled in verification contexts. These principles emphasize transparency in documentation, completeness in covering all relevant emission categories, consistency in methodology across years and reporting periods, comparability between national inventories, and accuracy in producing estimates that are neither systematically biased high nor low [2]. The application of these principles to remote sensing data requires particular attention to consistency, given that satellite missions inevitably change over time as instruments reach end-of-life and new platforms are launched, potentially introducing systematic differences in observations that could be misinterpreted as real environmental changes.

## 2. Remote Sensing Applications in Climate Agreement Monitoring

### 2.1 Land Cover Observation and Change Detection

The systematic observation of land cover represents one of the most mature applications of remote sensing in climate agreement verification. Land cover data serve multiple purposes in greenhouse gas accounting, including the stratification of areas for emission factor application, the identification of land use change events that trigger carbon stock changes, and the mapping of carbon pools that may not be directly measurable through other means. The Kyoto Protocol specifically references land cover observations in Articles 5 and 10, recognizing their importance for both mandatory and voluntary reporting requirements [1].

Change detection from satellite imagery enables the identification of deforestation, reforestation, afforestation, and forest degradation events that drive changes in terrestrial carbon stocks. These capabilities have proven particularly important for Reducing Emissions from Deforestation and Forest Degradation (REDD+) activities under the UNFCCC, where payments are contingent upon demonstrated reductions in emissions from deforestation or enhancements in forest carbon stocks. The technical challenge in change detection lies not merely in identifying that change has occurred, but in accurately quantifying the spatial extent and timing of change, characterizing the uncertainty in these estimates, and attributing the change to specific causes or agents [2].

The integration of land cover observations into national greenhouse gas inventories requires careful attention to consistency with IPCC methodological frameworks. The IPCC guidelines provide tiered approaches for estimating emissions and removals, with higher tiers requiring more detailed activity data and emission factors that may be derived from remote sensing observations. The transition between tiers, or between different data sources within a tier, introduces potential inconsistencies that must be documented and addressed to maintain the consistency principle essential for tracking emissions over time [2].

### 2.2 Biomass and Carbon Stock Estimation

Quantification of above-ground vegetation biomass and its changes represents a more technically demanding application of remote sensing in climate agreement verification. Biomass estimation from remote sensing requires the development of relationships between remotely observable properties, such as radar backscatter, optical reflectance, or LiDAR-derived canopy structure, and ground-measured biomass values. These relationships are inherently uncertain, reflecting both the indirect nature of the remote sensing observations and the natural variability in biomass across spatial and temporal scales [1].

The establishment of 1990 carbon stock baselines, as required under Article 3 of the Kyoto Protocol, presents particular challenges for biomass estimation. Where historical ground-based inventories are unavailable, satellite data from the relevant time period must be used to reconstruct baseline conditions. The Landsat archive, extending back to 1972, provides the only long-term source of Earth observation data at spatial resolutions sufficient to evaluate human impacts on the environment, such as forest harvesting, at the landscape scales relevant for national accounting [1]. However, the technical characteristics of historical sensors differ substantially from modern instruments, introducing additional uncertainties when integrating data across the historical record.

Contemporary approaches to biomass estimation increasingly employ synthetic aperture radar (SAR) and LiDAR observations that penetrate vegetation canopies and provide structural information directly related to biomass. The European Space Agency's Biomass mission, launched in 2018, represents the first satellite specifically designed to measure forest biomass globally using P-band radar. Such missions offer the potential for improved biomass estimates with known uncertainty characteristics, but validation against ground measurements remains essential for establishing confidence in the products [3].

### 2.3 Anthropogenic Methane Source Monitoring

The mapping and monitoring of anthropogenic methane sources represents an emerging application of remote sensing that addresses a significant gap in current greenhouse gas monitoring capabilities. Methane's high global warming potential and its role as a precursor to ground-level ozone make its accurate quantification particularly important for climate agreement verification. The Kyoto Protocol references methane monitoring in Articles 3, 5, and 10, recognizing its significance for both compliance assessment and understanding the overall carbon cycle [1].

Satellite-based methane detection has advanced substantially with the launch of dedicated greenhouse gas monitoring missions. The Greenhouse gases Observing SATellite (GOSAT) and its successor GOSAT-2 provide column measurements of methane, while the TROPOspheric Monitoring Instrument (TROPOMI) on the Sentinel-5 Precursor satellite provides methane observations with improved spatial resolution. These instruments enable the detection of large point sources and the observation of regional-scale methane enhancements, supporting top-down approaches to emission estimation that complement traditional bottom-up inventory methods [4].

The attribution of satellite-observed methane enhancements to specific source types remains technically challenging. Methane has an atmospheric lifetime of approximately nine years, allowing it to mix over continental scales before detection, which complicates the attribution of observed concentrations to specific emission regions or source categories. Inverse modeling approaches can be employed to infer surface fluxes from atmospheric concentration measurements, but these approaches require accurate characterization of atmospheric transport and specification of prior emission estimates, both of which introduce additional uncertainties [4].

## 3. Data Quality Management Frameworks

### 3.1 Validation Requirements and Protocols

The credibility of remote sensing products for climate agreement verification depends fundamentally on the ability to assess and quantify their accuracy through systematic validation. A thematic product derived from remote sensing data, whether a land cover classification, carbon stock estimate, or change detection map, has no value or credibility unless its accuracy can be reliably assessed and quantified [1]. This principle, established in early assessments of remote sensing applications to the Kyoto Protocol, remains central to contemporary approaches for integrating satellite data into greenhouse gas inventories.

Validation of remote sensing products requires access to independent reference data that represent the true state of the variable being measured. For land cover products, this typically involves high-resolution satellite imagery or field observations that provide more accurate classifications than can be achieved with the coarser resolution products being validated. For biomass products, validation requires destructive sampling or allometric equations applied to field measurements, which themselves introduce uncertainties that must be propagated into validation assessments [3].

The development of community-validated approaches for remote sensing product validation has progressed across multiple domains. The Committee on Earth Observation Satellites (CEOS) has coordinated efforts to establish validation protocols for soil moisture products, land surface temperature products, and biomass products, providing frameworks that can be adapted for climate agreement applications. These protocols typically specify the number and distribution of validation samples required, the statistical metrics to be reported, and the procedures for documenting validation results [3].

### 3.2 Integration of In Situ and Remote Observations

Up-to-date, quantifiable in situ data are needed for the reliable use of remote sensing data and for thematic validation across all applications evaluated for climate agreement monitoring [1]. The collection of field data represents a painstaking, time-consuming, and expensive endeavor, yet its relevance for ensuring the quality of remote sensing products cannot be overstated. The relationship between ground-based and remotely sensed observations should be treated as complementary rather than utilitarian, with sampling designs optimized for the combined performance of both data sources rather than for each separately [3].

The integration of in situ and remote observations requires careful attention to the spatial and temporal scales at which each data source provides the most reliable information. Ground-based observations typically provide point measurements with high accuracy but limited spatial coverage, while satellite observations provide systematic coverage but with coarser resolution and potential systematic biases. The optimal integration strategy depends on the specific application, the spatial and temporal variability of the target variable, and the relative costs of different observation types [3].

National Forest Monitoring Systems (NFMS) have emerged as institutional frameworks for coordinating the collection and integration of ground-based and satellite observations for climate agreement reporting. These systems require establishment of institutional arrangements that enable long-term availability of human and logistical resources, technical capacity, and partnerships and funding mechanisms. The design of integrated monitoring systems must consider how data sources complement and inform each other, with stratification decisions and operational processes optimized for combined performance rather than for individual data streams [3].

### 3.3 Quality Assurance and Quality Control

Quality assurance (QA) and quality control (QC) procedures are essential components of any remote sensing data processing chain intended for climate agreement verification. Quality assurance encompasses the planned systematic activities implemented to ensure that data meet specified quality requirements, while quality control refers to the operational techniques and activities used to verify that data quality requirements are met. Together, these procedures provide the framework for documenting and managing data quality throughout the processing chain [5].

The application of QA/QC procedures to remote sensing data for climate agreement verification must address multiple potential sources of error and uncertainty. Pre-processing steps such as radiometric calibration, geometric correction, and atmospheric correction introduce uncertainties that propagate into subsequent analysis products. The calibration of satellite sensors is typically maintained through vicarious calibration using ground targets or cross-calibration with other sensors, but residual uncertainties remain and must be characterized [3].

The Global Climate Observation System (GCOS) and the Global Atmospheric Observation System (GAW) have established climate monitoring principles that provide guidance for QA/QC procedures applicable to climate agreement verification. These principles emphasize the need for calibration against international standards, documentation of algorithms and processing methods, metadata documentation sufficient to enable data users to assess data quality and applicability, and ongoing assessment of data quality through comparison with other measurements [5].

## 4. Uncertainty Quantification Methodologies

### 4.1 Metrological Approaches to Uncertainty

The characterization of uncertainty in remote sensing products for climate agreement verification has increasingly adopted approaches developed in the field of metrology, the science of measurement. Classic metrological practice involves firstly assessing and quantifying all known sources of error, and secondly propagating uncertainty rigorously through all steps to the end result [3]. The analogy between the problems in Earth observation-based climate science and metrology has prompted developing dialogue and joint projects between these communities, including collaborations between the World Meteorological Organization (WMO) and the Bureau International des Poids et Mesures (BIPM) [3].

The uncertainty characterization of satellite-based climate data records typically involves identifying and quantifying all significant sources of uncertainty in the processing chain from raw sensor measurements to derived geophysical products. For passive remote sensing observations, this includes uncertainties in calibration of the sensor, atmospheric correction, geolocation, and retrieval algorithms. Each source of uncertainty must be characterized in terms of its statistical distribution, spatial and temporal correlation structure, and potential systematic components [3].

The propagation of uncertainty through processing chains requires knowledge of how uncertainties in input variables combine to produce uncertainties in output products. For linear processing chains, uncertainty propagation can be accomplished through standard methods of error analysis, but many remote sensing retrieval algorithms involve nonlinear transformations that require more sophisticated approaches such as Monte Carlo simulation or analytical covariance propagation. The resulting uncertainty estimates should be provided at the pixel level to enable users to assess the reliability of individual measurements [3].

### 4.2 Uncertainty in Satellite-Derived Greenhouse Gas Estimates

The quantification of uncertainty in satellite-derived greenhouse gas estimates presents particular challenges related to the indirect nature of the measurements and the complexity of the retrieval algorithms. Satellite instruments measure radiances at specific wavelengths, from which column-averaged dry-air mole fractions of greenhouse gases are retrieved through inverse methods that require specification of atmospheric state, surface properties, and viewing geometry. Each of these inputs introduces uncertainties that propagate into the final retrieved concentrations [4].

The uncertainty characterization for satellite greenhouse gas products typically distinguishes between random uncertainties, which can be reduced through averaging, and systematic uncertainties, which persist regardless of sample size. Random uncertainties arise primarily from measurement noise and atmospheric variability within the satellite footprint, while systematic uncertainties may result from calibration errors, spectroscopic uncertainties in absorption line parameters, or errors in the treatment of scattering by aerosols and clouds [4].

The development of good practice guidelines for the validation of satellite greenhouse gas products has been identified as a priority by the atmospheric science community. These guidelines should specify protocols for comparing satellite retrievals with independent measurements from ground-based networks, aircraft campaigns, and other satellite instruments, as well as methods for aggregating validation results to characterize uncertainty at different spatial and temporal scales [4].

### 4.3 Error Propagation in Integrated Assessment

The integration of remote sensing observations with inventory data and atmospheric models for climate agreement verification requires careful attention to the propagation of uncertainties through complex analysis chains. Top-down approaches that use atmospheric observations to constrain surface fluxes must specify uncertainties in the prior emission estimates, the atmospheric observations, and the transport model, and propagate these through the inversion to produce posterior flux estimates with characterized uncertainties [4].

Atmospheric transport models introduce significant uncertainties in top-down emission estimates. The simulation of atmospheric tracer transport depends on the accuracy of meteorological fields, the parameterization of sub-grid scale processes such as convection and boundary layer mixing, and the spatial and temporal resolution of the model. These transport uncertainties can be comparable to or larger than the uncertainties in the observations themselves, particularly for short-lived species or at fine spatial scales [4].

The development of emulators for atmospheric transport models represents a promising approach for uncertainty quantification in integrated assessments. Emulators are statistical approximations of complex model outputs that can be evaluated much more rapidly than the full model, enabling comprehensive exploration of parameter uncertainty and sensitivity analysis. Recent work has demonstrated the application of emulator-based uncertainty quantification to satellite-based greenhouse gas emission estimates, providing a framework for characterizing the full range of uncertainties in top-down approaches [6].

## 5. Attribution Uncertainty and Source Identification

### 5.1 Source Attribution Techniques

The attribution of observed atmospheric enhancements or land cover changes to specific emission sources or causes represents one of the most challenging aspects of climate agreement verification. Attribution uncertainty arises from the fundamental difficulty of separating the contributions of multiple sources to an observed signal, the limited spatial and temporal resolution of observations, and the uncertainties in prior information used to constrain the attribution problem [4].

Source-receptor (influence-function) techniques offer a computationally efficient approach for source attribution that has proven well suited for near-real-time verification applications. These techniques pre-compute the sensitivity of observations at receptor locations to emissions from different source regions, enabling rapid calculation of source contributions without repeated forward model runs. However, the accuracy of these techniques depends on the quality of the transport model used to compute the influence functions and the representativeness of the source and receptor configurations assumed [4].

Inverse modeling approaches provide a more comprehensive framework for source attribution that can simultaneously estimate emissions from multiple source regions or categories. These approaches solve the inverse problem of inferring surface fluxes from atmospheric concentration measurements, typically using Bayesian inference frameworks that combine prior emission estimates with observational constraints. The resulting posterior emission estimates reflect both the prior information and the information content of the observations, with uncertainties that reflect both sources of constraint [4].

### 5.2 Challenges in Emission Category Attribution

The attribution of observed emissions to IPCC emission categories presents particular challenges for integrating satellite observations into national greenhouse gas inventories. National inventories are organized by economic sector and process, with emission factors applied to activity data to estimate emissions from each category. Satellite observations, in contrast, measure atmospheric concentrations that reflect the integrated effect of all sources within the satellite footprint, without inherent information about the source category responsible [4].

The persistent divergence between independent model estimates and official inventory data underscores the urgent need for harmonized approaches to emission attribution. For applications such as Carbon Capture, Utilization, and Storage (CCUS) monitoring, this implies that national inventories must be capable of incorporating concentration-based data from sensors, drones, and satellites into their reporting frameworks. Establishing procedures for aligning observed emissions with inventory categories, including uncertainty quantification and attribution of sources, will be critical as monitoring technologies mature [4].

The use of satellite observations of co-emitted species can aid in source attribution by providing information about emission processes or fuel types. Observations of carbon monoxide (CO), which is co-emitted with CO2 from combustion sources, can help distinguish fossil fuel emissions from biogenic sources. Similarly, observations of nitrogen dioxide (NO2) can provide information about combustion sources and high-temperature industrial processes. The synergistic use of multiple species from satellite observations offers potential for improved source attribution, but requires careful consideration of emission ratios and atmospheric chemistry [4].

### 5.3 Spatial and Temporal Attribution Scales

The spatial and temporal scales at which attribution is required for climate agreement verification may not align with the native resolution of satellite observations or the characteristic scales of emission variability. National inventories typically report emissions at annual time steps and national spatial scales, while satellite observations provide instantaneous column measurements at specific overpass times and spatial resolutions ranging from kilometers to tens of kilometers [4].

The temporal aggregation of satellite observations to annual totals requires assumptions about diurnal, seasonal, and inter-annual variability that introduce additional uncertainties. For greenhouse gases with significant diurnal cycles in boundary layer concentration, such as methane, the time of satellite overpass can significantly affect the representativeness of the observation for daily or annual means. Similarly, the spatial aggregation of point source emissions to grid scales appropriate for comparison with models requires characterization of sub-grid variability [4].

Mass balance approaches have been applied to point sources measured by satellite data, enabling estimation of emission rates from individual facilities. These approaches integrate the observed atmospheric enhancement downwind of a source, accounting for atmospheric transport, to estimate the total emission flux. However, mass balance approaches typically provide only snapshot estimates and require extrapolation to longer time scales, introducing additional uncertainties. Most mass balance approaches also have attributional limits at facility-level or higher spatial scales, limiting their utility for distinguishing between emission processes within a facility [4].

## 6. Methodological Frameworks and Standards

### 6.1 IPCC Guidelines and Good Practice Principles

The IPCC has produced and published guidance that countries have agreed to use in estimating greenhouse gas inventories for reporting to the UNFCCC and the Kyoto Protocol since 1996. These inventories cover all economic sectors, including Land Use, Land-Use Change and Forestry (LULUCF), and provide the methodological foundation for climate agreement verification. The IPCC guidelines establish tiered approaches that allow countries to select methods appropriate to their national circumstances and data availability, with higher tiers generally requiring more detailed activity data and emission factors [2].

Good practice in greenhouse gas inventory development encompasses five general principles that apply to all emission categories and estimation methods. Transparency requires documentation sufficient for reviewers to assess the extent to which good practice requirements have been met. Completeness requires that all relevant categories of emissions and removals are estimated and reported. Consistency requires that differences between years reflect differences in emissions or removals and are not artifacts of changes in methodology or data availability. Comparability requires that inventory estimates can be compared between countries. Accuracy requires the use of methods designed to produce neither systematic over- nor under-estimates [2].

The application of remote sensing data in the context of IPCC good practice principles requires particular attention to consistency. Because satellites go out of commission and new ones enter into use, and because ways of using the imagery evolve, the consistency of remote sensing-derived data products over time cannot be assumed. Changes in satellite platforms, sensors, algorithms, or processing methods may introduce systematic differences that must be documented and, where possible, corrected to maintain consistency in time series used for emission estimation [2].

### 6.2 UNFCCC Reporting Requirements and Review Processes

The UNFCCC has established well-developed processes for reviewing greenhouse gas inventories of developed country Parties, providing the basis for assessing progress towards emissions reduction targets and commitments. These review processes examine the methodological approaches used by Parties, the completeness and accuracy of reported data, and the consistency of reported inventories over time. The technical review of inventory submissions identifies areas where improvements are needed and provides recommendations for enhancing the quality of future submissions [2].

For REDD+ activities, the UNFCCC has developed specific guidance on measurement, reporting, and verification that builds upon the IPCC framework while addressing the particular characteristics of forest carbon accounting. The Warsaw Framework for REDD+ establishes requirements for national forest monitoring systems, reference emission levels, and safeguards information systems, providing the institutional context within which remote sensing data are integrated into REDD+ accounting [2].

The integration of top-down emission estimates from atmospheric observations into UNFCCC review processes represents an evolving area of methodology development. While bottom-up inventories remain the primary basis for national reporting, top-down approaches using atmospheric observations and assimilation methods offer a way to cross-check and improve the accuracy of national reporting. The establishment of formal processes for integrating top-down estimates into inventory quality assurance, especially for sectors involving large point sources or diffuse emissions, has been recommended by the scientific community [4].

### 6.3 International Coordination and Standardization

The international coordination of remote sensing activities for climate agreement verification occurs through multiple institutional mechanisms, including the Committee on Earth Observation Satellites (CEOS), the Coordination Group for Meteorological Satellites (CGMS), and the Global Climate Observation System (GCOS). These bodies work to ensure the continuity of satellite observations, the interoperability of data products, and the standardization of validation protocols across different missions and agencies [3].

The establishment of Essential Climate Variables (ECVs) by GCOS provides a framework for prioritizing satellite observations and product development efforts. ECVs are those physical, chemical, or biological variables or groups of linked variables that critically contribute to the characterization of Earth's climate. The specification of ECVs enables coordinated international efforts to ensure that observations of these variables are sustained and that products meet the quality requirements for climate monitoring and verification applications [3].

The International Organization for Standardization (ISO) has developed technical standards relevant to remote sensing data quality that provide additional frameworks for standardization. ISO standards for geographic information, remote sensing, and spatial data quality offer specifications for metadata, data quality indicators, and quality assessment procedures that can be applied to remote sensing products for climate agreement verification. The adoption of these standards facilitates data exchange and interoperability across different systems and national boundaries [3].

## 7. Persistent Challenges and Emerging Solutions

### 7.1 Technical Limitations and Data Gaps

Despite substantial progress in remote sensing technology and methodology, significant technical limitations continue to constrain the reliability of satellite-based verification of climate agreements. Detection thresholds for emission sources remain undefined for many applications, making it difficult to assess the completeness of emission estimates derived from satellite observations. The spatial resolution of current satellite greenhouse gas observations, typically several kilometers, limits the ability to detect and quantify emissions from small or dispersed sources that may be significant at national or sub-national scales [4].

The fragmentation of observation platforms represents a significant barrier to effective greenhouse gas monitoring. In situ sensors, drones, and satellites are often operated in isolation, without coordinated data fusion or cross-calibration. This siloed monitoring approach prevents full exploitation of spatial and temporal synergies, undermining the effectiveness of greenhouse gas assessments across different scales. The integration of observations from multiple platforms requires development of common data standards, calibration protocols, and fusion algorithms [4].

The underutilization of certain spectral regions for greenhouse gas monitoring represents an additional technical gap. Shortwave infrared (SWIR) data for CO2 and CH4 remain underutilized in industrial contexts, and the synergistic use of multi-angle and hyperspectral sensors is still limited. The quantitative error propagation between retrievals and emission estimates is often overlooked in current operational systems, limiting the reliability of uncertainty characterization for verification applications [4].

### 7.2 Institutional and Capacity Barriers

The effective use of remote sensing for climate agreement verification requires technical capacity and institutional arrangements that may be lacking in some countries, particularly developing countries and those with limited resources. The establishment of National Forest Monitoring Systems requires long-term commitment of human and financial resources, technical expertise in remote sensing and forest inventory, and coordination across multiple government agencies and research institutions [3].

The cost-effectiveness of different monitoring approaches remains an important consideration for countries with limited resources. The IPCC guidance documents emphasize that methods should remain relevant even as technologies and methods evolve, and that countries should apply principles outlined in guidance documents using existing examples of national greenhouse gas inventories and operational systems. The development of cost-effective approaches that leverage existing data and infrastructure while meeting verification requirements represents an ongoing challenge [2].

The integration of remote sensing expertise with inventory development expertise requires institutional arrangements that bridge traditional disciplinary and organizational boundaries. Remote sensing scientists may have limited knowledge of the data needs of the treaty community, while treaty staff and national inventory compilers may be unaware of what remote sensing technologies are available or how they could provide information for implementation. Bridging this gap requires sustained dialogue and capacity building efforts [1].

### 7.3 Emerging Technologies and Methodological Advances

Emerging technologies offer potential solutions to many of the current limitations in remote sensing-based climate agreement verification. The development of satellite missions with higher spatial resolution, improved spectral coverage, and enhanced temporal revisit will enable detection and quantification of smaller emission sources and more frequent monitoring of temporal variations in emissions. Constellations of small satellites offer the potential for improved temporal coverage compared to traditional single-satellite missions [4].

Advances in inverse modeling and data assimilation offer improved frameworks for integrating multiple data streams and characterizing uncertainty in emission estimates. Ensemble Kalman filters and variational approaches (4D-Var) have proven effective for regional- to facility-scale inverse modeling, while optimal-estimation algorithms such as LIDORT and OSS remain the most robust for satellite-based column retrievals. The continued development of these methods, combined with increased computational resources, enables more sophisticated analysis of satellite observations for verification applications [4].

The development of standardized approaches for error propagation and uncertainty quantification represents an important methodological advance. The application of metrological principles to Earth observation, including rigorous characterization of error sources and propagation through processing chains, provides a foundation for more reliable uncertainty estimates. The dialogue between the climate science and metrology communities, facilitated by organizations such as WMO and BIPM, is advancing these approaches [3].

## 8. Conclusions

The verification of climate agreements using remote sensing represents a complex interdisciplinary challenge that requires integration of satellite technology, atmospheric science, inventory methodology, and institutional arrangements. Substantial progress has been made in developing the technical capabilities, methodological frameworks, and institutional mechanisms needed to support remote sensing-based verification, yet significant challenges remain in ensuring the reliability and consistency of satellite-derived estimates for compliance assessment.

Data quality management for climate agreement verification requires systematic validation of remote sensing products against independent reference data, integration of in situ and satellite observations as complementary data sources, and implementation of quality assurance and quality control procedures throughout processing chains. The metrological approach to uncertainty characterization, involving identification and quantification of all significant error sources and rigorous propagation through processing chains, provides a foundation for reliable uncertainty estimates but has not yet been fully implemented across all remote sensing applications.

Attribution uncertainty remains a fundamental challenge for integrating satellite observations into climate agreement verification. The attribution of observed atmospheric enhancements or land cover changes to specific emission sources or causes requires sophisticated inverse modeling approaches that must account for uncertainties in atmospheric transport, prior emission estimates, and observational constraints. The alignment of satellite-based emission estimates with IPCC emission categories for integration into national inventories requires methodological development that is still ongoing.

The continued advancement of remote sensing capabilities for climate agreement verification will require sustained investment in satellite missions, algorithm development, validation infrastructure, and capacity building. The coordination of international efforts through bodies such as CEOS, GCOS, and the UNFCCC will be essential for ensuring the continuity and interoperability of observations across national boundaries and over time. As monitoring technologies mature, particularly those capable of identifying emissions from specific industrial processes or geological storage, validation approaches must become integral components of national reporting systems to ensure the credibility and transparency of climate agreement implementation.

## References

[1] JAXA. Remote Sensing and the Kyoto Protocol: A Review of Available and Future Technology for Monitoring Treaty Compliance. International Society for Photogrammetry and Remote Sensing (ISPRS), WG VII/5 and VII/6; 1999.

[2] UNFCCC. Methods and Guidance Document for REDD+ Reference Emission Levels and Reference Levels. REDD+ Technical Expert Panel; 2014.

[3] European Space Agency. Uncertainty characterization for essential climate variables from satellite remote sensing. Earth System Science Data; 2017.

[4] MDPI Remote Sensing. Monitoring and Verification for Carbon Capture, Utilization, and Storage: A Review of Technologies and Practices. Remote Sensing; 2024.

[5] Bureau International des Poids et Mesures. Measurement challenges in climate science: Ensuring traceability and uncertainty characterization. BIPM; 2020.

[6] Clark JN, et al. Uncertainty assessment in satellite-based greenhouse gas emissions estimates using emulated atmospheric transport. School of Engineering Mathematics and Technology, University of Bristol; 2025.

## Annotations


## Sources
[1] https://arxiv.org/pdf/2510.05751?
[2] https://bmva-archive.org.uk/bmvc/2025/assets/workshops/MVCC/Paper_5/paper.pdf
[3] https://dialnet.unirioja.es/descarga/articulo/10085301.pdf
[4] https://essd.copernicus.org/articles/9/511/2017/essd-9-511-2017.pdf
[5] https://harvardforest.fas.harvard.edu/publications/pdfs/Campbell_BioSci_2013.pdf
[6] https://journals.ametsoc.org/view/journals/bams/94/3/bams-d-12-00042.1.pdf
[7] https://juser.fz-juelich.de/record/850698/files/J%C3%BCl_2824_Lanchbery.pdf
[8] https://ntrs.nasa.gov/api/citations/20040171274/downloads/20040171274.pdf
[9] https://ntrs.nasa.gov/citations/20090040011
[10] https://redd.unfccc.int/uploads/2_77_redd_20140218_mgd_report_gfoi.pdf
[11] https://scispace.com/pdf/providing-data-quality-information-for-remote-sensing-1q5isy058m.pdf
[12] https://unfccc.int/sites/default/files/resource/terr1.2024_CANa01.pdf
[13] https://wiki.esipfed.org/Sensor_Data_Quality
[14] https://www.bipm.org/documents/20126/28127073/bipm%20publication-ID-2169/99b88250-e7ae-0231-6243-0a90a7aeb8fa
[15] https://www.eorc.jaxa.jp/ALOS/en/kyoto/ref/KP-RS_WS-Report_ISPRS_VII56.pdf
[16] https://www.fs.usda.gov/rm/pubs_journals/2020/rmrs_2020_espejo_a001.pdf
[17] https://www.ipcc.ch/report/2019-refinement-to-the-2006-ipcc-guidelines-for-national-greenhouse-gas-inventories/
[18] https://www.math.sissa.it/content/spatial-statistics-and-uncertainty-quantification-remote-sensing-and-climate-science-dr-0
[19] https://www.mdpi.com/2072-4292/16/20/3818
[20] https://www.mdpi.com/2072-4292/17/22/3707
[21] https://www.nationalacademies.org/publications/12677
[22] https://www.nationalacademies.org/read/26641/chapter/4
[23] https://www.nies.go.jp/soc/doc/GHG_Satellite_Guidebook_1st_12d.pdf
[24] https://www.sciencedirect.com/science/article/pii/S0013935125010187
[25] https://www.sciencedirect.com/science/article/pii/S0034425720301760
[26] https://www.sciencedirect.com/science/article/pii/S0168169922001612