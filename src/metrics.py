import pandas as pd
from pandas import DataFrame
from typing import Dict, Optional

class Metrics:
    def apply_filters_to_dataframe(self, df: DataFrame, dicionario: Dict[str, Optional[float]]) -> DataFrame:
        """
        Apply filters to a DataFrame based on the provided dictionary of metrics.

        Args:
            df (DataFrame): The DataFrame to filter.
            dicionario (Dict[str, Optional[float]]): A dictionary of metrics and their values for filtering.

        Returns:
            DataFrame: The filtered DataFrame.
        """
        filtered_df = df.copy()
        metrics_less_than = ['Cotacao', 'P/L', 'P/VP', 'PSR', "P/Ativo", "P/Cap.Giro", "P/EBIT", "P/ACL", "EV/EBIT", "EV/EBITDA"]
        metrics_more_than = ['DY', 'Mrg.Ebit', 'Mrg.Liq.', 'Liq.Corr.', "ROIC", "ROE", "Pat.Liq", "Div.Brut/Pat.", "Liq.2meses", "Cresc.5anos"]
        
        if self.check_dict(dicionario):
            if dicionario['Papel'] is not None:
                return df[df['Papel'] == dicionario['Papel']]
                
            conditions = []
            
            for metric in metrics_less_than:
                value = dicionario.get(metric)
                if value is not None:
                    conditions.append((filtered_df[metric] > 0) & (filtered_df[metric] < value))
            
            for metric in metrics_more_than:
                value = dicionario.get(metric)
                if value is not None:
                    conditions.append(filtered_df[metric] > value)
            
            if conditions:
                filter_condition = pd.DataFrame(conditions).all(axis=0)
                filtered_df = filtered_df.loc[filter_condition]
        
        return filtered_df

    @staticmethod
    def check_dict(d: Dict[str, Optional[float]]) -> bool:
        """
        Check if any values in the dictionary are not None.

        Args:
            d (Dict[str, Optional[float]]): The dictionary to check.

        Returns:
            bool: True if any values in the dictionary are not None, otherwise False.
        """
        for value in d.values():
            if value is not None:
                return True
        return False
