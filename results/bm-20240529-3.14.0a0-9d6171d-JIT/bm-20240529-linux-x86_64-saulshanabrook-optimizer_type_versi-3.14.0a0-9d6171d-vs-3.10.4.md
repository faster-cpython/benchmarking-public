# Results vs. 3.10.4

- fork: saulshanabrook
- ref: optimizer_type_versi
- machine: linux-x86_64
- commit hash: 9d6171d
- commit date: 2024-05-29
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                          |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| html5lib       | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                         |
| tornado_http   | 136 ms                                                 | 96.5 ms: 1.41x faster                                                         |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 384 ms: 1.89x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 462 ms: 1.88x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 948 ms: 1.86x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 613 ms: 1.66x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.0 ms: 1.87x faster                                                         |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                         |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                                         |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                         |
| unpickle_list        | 5.20 us                                                | 5.60 us: 1.08x slower                                                         |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                         |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                         |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                         |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                          |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                                         |
| richards_super           | 94.7 ms                                                | 48.1 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                         |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                         |
| async_tree_none          | 728 ms                                                 | 384 ms: 1.89x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 462 ms: 1.88x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                         |
| nbody                    | 154 ms                                                 | 82.0 ms: 1.87x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 948 ms: 1.86x faster                                                          |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                          |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 523 ms: 1.76x faster                                                          |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 613 ms: 1.66x faster                                                          |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.66x faster                                                          |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                         |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                          |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                         |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                          |
| pylint                   | 551 ms                                                 | 352 ms: 1.57x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                                         |
| fannkuch                 | 532 ms                                                 | 355 ms: 1.50x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                          |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.82 us: 1.43x faster                                                         |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                          |
| tornado_http             | 136 ms                                                 | 96.5 ms: 1.41x faster                                                         |
| logging_format           | 9.09 us                                                | 6.44 us: 1.41x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.60 ms: 1.41x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                         |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                         |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                         |
| python_startup           | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                         |
| thrift                   | 1.07 ms                                                | 813 us: 1.32x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                        |
| html5lib                 | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                         |
| deepcopy                 | 479 us                                                 | 372 us: 1.29x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                          |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 69.2 ms: 1.22x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 56.9 ms: 1.22x faster                                                         |
| nqueens                  | 106 ms                                                 | 87.4 ms: 1.21x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 82.8 ms: 1.20x faster                                                         |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                                          |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                         |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                          |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                         |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                          |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                          |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                                         |
| pickle_list              | 5.08 us                                                | 5.24 us: 1.03x slower                                                         |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                          |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                         |
| unpickle_list            | 5.20 us                                                | 5.60 us: 1.08x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 3.99 ms: 1.10x slower                                                         |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                         |
| telco                    | 7.27 ms                                                | 8.10 ms: 1.11x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                                         |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                         |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240529-3.14.0a0-9d6171d-JIT/bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x