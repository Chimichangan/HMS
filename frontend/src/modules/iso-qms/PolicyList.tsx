import { useEffect, useState } from 'react';
import axios from 'axios';
import { useTranslation } from 'react-i18next';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
});

export default function PolicyList() {
  const [items, setItems] = useState<any[]>([]);
  const { t } = useTranslation();

  useEffect(() => {
    const token = localStorage.getItem('token');
    api
      .get('/iso-qms/policies/', {
        headers: {
          Authorization: token ? `Bearer ${token}` : '',
          'X-Org-Id': '1',
        },
      })
      .then((r) => setItems(r.data))
      .catch((e) => console.error(e));
  }, []);

  return (
    <div className="p-4">
      <h1>{t('policies') || 'Policies'}</h1>
      <ul>{items.map((p) => <li key={p.id}>{p.title}</li>)}</ul>
    </div>
  );
}
