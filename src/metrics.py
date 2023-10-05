

class Metrics:
    def apply_filters_to_dataframe(self, df, filters):
            """
            Aplica filtros ao DataFrame.

            Parameters:
            df (pd.DataFrame): DataFrame original.
            filters (list): Lista de filtros no formato [(métrica, valor), ...].

            Returns:
            pd.DataFrame: DataFrame filtrado.
            """
            filtered_df = df.copy()

            for metric, value in filters:
                
                value = float(value)  
                filtered_df = filtered_df[filtered_df[metric] >= value]
                    

            return filtered_df