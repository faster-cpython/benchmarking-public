# Results vs. 3.10.4

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.07x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                     |
| chameleon      | 10.8 ms                                                               | 10.3 ms: 1.05x faster                                                    |
| html5lib       | 86.5 ms                                                               | 75.0 ms: 1.15x faster                                                    |
| tornado_http   | 178 ms                                                                | 136 ms: 1.31x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 507 ms: 1.87x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 673 ms: 1.68x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 813 ms: 1.56x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.73x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 116 ms: 1.16x faster                                                     |
| nbody          | 166 ms                                                                | 150 ms: 1.10x faster                                                     |
| pidigits       | 235 ms                                                                | 237 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                    |
| regex_compile  | 177 ms                                                                | 173 ms: 1.02x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps          | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| pickle_pure_python  | 529 us                                                                | 470 us: 1.13x faster                                                     |
| xml_etree_process   | 99.5 ms                                                               | 89.8 ms: 1.11x faster                                                    |
| xml_etree_parse     | 212 ms                                                                | 193 ms: 1.10x faster                                                     |
| unpickle_list       | 6.99 us                                                               | 6.73 us: 1.04x faster                                                    |
| tomli_loads         | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                   |
| xml_etree_iterparse | 156 ms                                                                | 161 ms: 1.03x slower                                                     |
| xml_etree_generate  | 123 ms                                                                | 128 ms: 1.04x slower                                                     |
| json_loads          | 30.9 us                                                               | 32.3 us: 1.05x slower                                                    |
| pickle_dict         | 35.1 us                                                               | 37.6 us: 1.07x slower                                                    |
| pickle              | 12.5 us                                                               | 13.8 us: 1.11x slower                                                    |
| unpickle            | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.51 ms: 1.23x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                    |
| django_template | 53.3 ms                                                               | 51.0 ms: 1.04x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 37.0 ms: 1.05x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 77.7 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 227 us: 2.91x faster                                                     |
| async_tree_none          | 950 ms                                                                | 507 ms: 1.87x faster                                                     |
| bench_mp_pool            | 14.5 ms                                                               | 7.77 ms: 1.87x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                   |
| generators               | 68.1 ms                                                               | 39.5 ms: 1.72x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 673 ms: 1.68x faster                                                     |
| deltablue                | 8.94 ms                                                               | 5.32 ms: 1.68x faster                                                    |
| raytrace                 | 573 ms                                                                | 348 ms: 1.65x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 581 ms: 1.63x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 813 ms: 1.56x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.51x faster                                                   |
| richards_super           | 107 ms                                                                | 76.9 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 89.5 ms: 1.35x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.80 ms: 1.34x faster                                                    |
| go                       | 264 ms                                                                | 201 ms: 1.32x faster                                                     |
| richards                 | 91.7 ms                                                               | 69.6 ms: 1.32x faster                                                    |
| tornado_http             | 178 ms                                                                | 136 ms: 1.31x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.49 us: 1.30x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.28 us: 1.28x faster                                                    |
| thrift                   | 1.26 ms                                                               | 986 us: 1.28x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 106 ms: 1.27x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.25 ms: 1.27x faster                                                    |
| pylint                   | 485 ms                                                                | 393 ms: 1.24x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.22x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                    |
| scimark_sor              | 246 ms                                                                | 202 ms: 1.22x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.7 ms: 1.21x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| dask                     | 450 ms                                                                | 385 ms: 1.17x faster                                                     |
| float                    | 135 ms                                                                | 116 ms: 1.16x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 75.0 ms: 1.15x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 470 us: 1.13x faster                                                     |
| logging_silent           | 222 ns                                                                | 199 ns: 1.12x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 89.8 ms: 1.11x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 66.4 ms: 1.11x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.9 ms: 1.10x faster                                                    |
| nbody                    | 166 ms                                                                | 150 ms: 1.10x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.33 ms: 1.09x faster                                                    |
| mako                     | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 119 ms: 1.07x faster                                                     |
| mypy2                    | 936 ms                                                                | 873 ms: 1.07x faster                                                     |
| scimark_lu               | 227 ms                                                                | 213 ms: 1.07x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.31 ms: 1.06x faster                                                    |
| sympy_sum                | 184 ms                                                                | 173 ms: 1.06x faster                                                     |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                     |
| chameleon                | 10.8 ms                                                               | 10.3 ms: 1.05x faster                                                    |
| pyflate                  | 795 ms                                                                | 759 ms: 1.05x faster                                                     |
| django_template          | 53.3 ms                                                               | 51.0 ms: 1.04x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.73 us: 1.04x faster                                                    |
| comprehensions           | 33.1 us                                                               | 32.0 us: 1.04x faster                                                    |
| sympy_expand             | 543 ms                                                                | 525 ms: 1.03x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.2 ms: 1.03x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 152 ms: 1.03x faster                                                     |
| sympy_str                | 329 ms                                                                | 320 ms: 1.03x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.61 sec: 1.03x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 73.7 ms: 1.02x faster                                                    |
| regex_compile            | 177 ms                                                                | 173 ms: 1.02x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 4.06 us: 1.01x faster                                                    |
| pidigits                 | 235 ms                                                                | 237 ms: 1.01x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 161 ms: 1.03x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.45 sec: 1.04x slower                                                   |
| spectral_norm            | 186 ms                                                                | 194 ms: 1.04x slower                                                     |
| xml_etree_generate       | 123 ms                                                                | 128 ms: 1.04x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.20 sec: 1.04x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.05x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 11.4 ms: 1.05x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.07 ms: 1.05x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 37.0 ms: 1.05x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.83 us: 1.05x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.39 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                    |
| meteor_contest           | 126 ms                                                                | 136 ms: 1.08x slower                                                     |
| deepcopy                 | 511 us                                                                | 558 us: 1.09x slower                                                     |
| fannkuch                 | 546 ms                                                                | 599 ms: 1.10x slower                                                     |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.11x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.47 ms: 1.11x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 77.7 ms: 1.11x slower                                                    |
| scimark_fft              | 500 ms                                                                | 561 ms: 1.12x slower                                                     |
| python_startup           | 11.2 ms                                                               | 12.5 ms: 1.12x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| nqueens                  | 117 ms                                                                | 134 ms: 1.14x slower                                                     |
| async_generators         | 452 ms                                                                | 524 ms: 1.16x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| deepcopy_memo            | 61.7 us                                                               | 75.9 us: 1.23x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.51 ms: 1.23x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.32 ms: 1.28x slower                                                    |
| telco                    | 8.49 ms                                                               | 165 ms: 19.47x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (6): regex_dna, sympy_integrate, json, unpickle_pure_python, docutils, pickle_list
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.15x