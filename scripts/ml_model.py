import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv('data/nba_teams.csv')
    df['wins'] = df['record'].apply(lambda x: int(x.split('-')[0]))  # Extract wins from record
    df['losses'] = df['record'].apply(lambda x: int(x.split('-')[1]))  # Extract losses from record
    return df

def train_models(X, y):
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor()
    }
    
    results = {}
    
    for name, model in models.items():
        # Hyperparameter tuning for Random Forest
        if name == 'Random Forest':
            param_grid = {
                'n_estimators': [50, 100],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5]
            }
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2')
            grid_search.fit(X, y)
            best_model = grid_search.best_estimator_
            results[name] = {
                'model': best_model,
                'score': grid_search.best_score_,
                'params': grid_search.best_params_
            }
        else:
            model.fit(X, y)
            score = cross_val_score(model, X, y, cv=5, scoring='r2').mean()
            results[name] = {
                'model': model,
                'score': score
            }
    
    return results

def evaluate_models(results, X, y):
    for name, result in results.items():
        model = result['model']
        predictions = model.predict(X)
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)
        print(f"{name} - MSE: {mse:.2f}, R²: {r2:.2f}")

        # Visualization of predictions vs actual
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=y, y=predictions)
        plt.xlabel('Actual Wins')
        plt.ylabel('Predicted Wins')
        plt.title(f'{name} Predictions vs Actual Wins')
        plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
        plt.show()

def main():
    df = load_data()
    X = df[['wins', 'losses']]  # Features
    y = df['wins']  # Target variable: number of wins

    results = train_models(X, y)
    evaluate_models(results, X, y)

if __name__ == '__main__':
    main() 