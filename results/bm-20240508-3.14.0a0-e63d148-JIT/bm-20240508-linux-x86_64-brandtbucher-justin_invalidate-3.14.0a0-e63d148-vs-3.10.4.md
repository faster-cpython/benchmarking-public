# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_invalidate
- machine: linux-x86_64
- commit hash: e63d148
- commit date: 2024-05-08
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 302 ms: 1.15x faster                                                     |
| chameleon      | 9.68 ms                                                | 7.17 ms: 1.35x faster                                                    |
| docutils       | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                   |
| html5lib       | 88.9 ms                                                | 72.1 ms: 1.23x faster                                                    |
| tornado_http   | 136 ms                                                 | 103 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 379 ms: 1.92x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 962 ms: 1.84x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 494 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 635 ms: 1.60x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                    |
| float          | 117 ms                                                 | 72.8 ms: 1.61x faster                                                    |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.46x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.84 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 60.9 ms: 1.30x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 88.2 ms: 1.13x faster                                                    |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                     |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.03x slower                                                    |
| unpickle_list        | 5.20 us                                                | 5.39 us: 1.04x slower                                                    |
| unpickle             | 14.4 us                                                | 15.6 us: 1.08x slower                                                    |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                    |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.67 ms: 1.29x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.50 ms: 1.72x faster                                                    |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 61.6 ms: 1.07x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 179 us: 3.03x faster                                                     |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.67 ms: 2.15x faster                                                    |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                    |
| async_tree_none          | 728 ms                                                 | 379 ms: 1.92x faster                                                     |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                    |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 63.7 ms: 1.86x faster                                                    |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 962 ms: 1.84x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 69.6 ms: 1.84x faster                                                    |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                    |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 520 ms: 1.77x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 494 ms: 1.76x faster                                                     |
| mako                     | 16.3 ms                                                | 9.50 ms: 1.72x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                    |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                                     |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                     |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                     |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                     |
| float                    | 117 ms                                                 | 72.8 ms: 1.61x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 635 ms: 1.60x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.39 ms: 1.57x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 37.8 us: 1.55x faster                                                    |
| pylint                   | 551 ms                                                 | 366 ms: 1.51x faster                                                     |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                    |
| fannkuch                 | 532 ms                                                 | 364 ms: 1.46x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.77 ms: 1.45x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                                    |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                     |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                    |
| chameleon                | 9.68 ms                                                | 7.17 ms: 1.35x faster                                                    |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                                     |
| tornado_http             | 136 ms                                                 | 103 ms: 1.33x faster                                                     |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                                    |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 60.9 ms: 1.30x faster                                                    |
| deepcopy                 | 479 us                                                 | 372 us: 1.29x faster                                                     |
| thrift                   | 1.07 ms                                                | 840 us: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.24x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                    |
| html5lib                 | 88.9 ms                                                | 72.1 ms: 1.23x faster                                                    |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 3.43 us: 1.21x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 69.6 ms: 1.21x faster                                                    |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 59.9 ms: 1.16x faster                                                    |
| 2to3                     | 348 ms                                                 | 302 ms: 1.15x faster                                                     |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.15x faster                                                    |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 88.2 ms: 1.13x faster                                                    |
| gunicorn                 | 1.53 ms                                                | 1.36 ms: 1.12x faster                                                    |
| sympy_expand             | 566 ms                                                 | 513 ms: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                    |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                   |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                     |
| dask                     | 441 ms                                                 | 410 ms: 1.08x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 61.6 ms: 1.07x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                     |
| docutils                 | 3.30 sec                                               | 3.34 sec: 1.01x slower                                                   |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                     |
| pickle_list              | 5.08 us                                                | 5.21 us: 1.03x slower                                                    |
| unpickle_list            | 5.20 us                                                | 5.39 us: 1.04x slower                                                    |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.84 ms: 1.06x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.06x slower                                                    |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                    |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.08x slower                                                    |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                    |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.87 ms: 1.15x slower                                                    |
| flaskblogging            | 8.58 ms                                                | 10.0 ms: 1.17x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.67 ms: 1.29x slower                                                    |
| telco                    | 7.27 ms                                                | 174 ms: 23.97x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.14.0a0-e63d148-JIT/bm-20240508-linux-x86_64-brandtbucher-justin_invalidate-3.14.0a0-e63d148.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.23x