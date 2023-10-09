class Metrics:
    def apply_filters_to_dataframe(self, df, dicionario, valores_desejados):
        metrics_less_than = ['Cotacao', 'P/L', 'P/VP',
                             'PSR', "P/Ativo", "P/Cap.Giro",
                             "P/EBIT", "P/ACL", "EV/EBIT", "EV/EBITDA"]
        
        metrics_more_than = ['DY', 'Mrg.Ebit', 'Mrg.Liq.' ,
                            'Liq.Corr.', "ROIC", "ROE", "Pat.Liq.",
                            "Div.Brut/Pat.", "Liq.2meses", "Cresc.5anos"]

        filtered_df = df[
            df.apply(
                lambda row: all(
                    (row[col] < dicionario[col]) if col in metrics_less_than and dicionario[col] is not None
                    else (row[col] > dicionario[col]) if col in metrics_more_than and dicionario[col] is not None
                    else True
                    for col in valores_desejados if col in row
                ),
                axis=1
            )
        ]

        return filtered_df
