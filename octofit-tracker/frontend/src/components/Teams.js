import React, { useEffect, useState } from 'react';
import getApiBaseUrl from '../utils/api';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  useEffect(() => {
    const endpoint = `${getApiBaseUrl()}/api/teams/`;
    console.log('Fetching Teams from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Teams data:', results);
      });
  }, []);
  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Teams</h2>
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              <th>Name</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={team.id || idx}>
                <td>{team.name || '-'}</td>
                <td>{team.description || '-'}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="btn btn-primary">Create Team</button>
      </div>
    </div>
  );
};
export default Teams;
