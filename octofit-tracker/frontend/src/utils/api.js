const getApiBaseUrl = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  return codespaceName
    ? `https://${codespaceName}-8000.app.github.dev`
    : 'http://localhost:8000';
};

export default getApiBaseUrl;
