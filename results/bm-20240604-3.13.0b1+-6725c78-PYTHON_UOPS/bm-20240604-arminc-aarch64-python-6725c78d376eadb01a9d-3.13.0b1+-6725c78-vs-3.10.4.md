# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.10x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 357 ms: 1.07x faster                                                     |
| chameleon      | 10.8 ms                                                               | 10.3 ms: 1.06x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.60 sec: 1.02x slower                                                   |
| html5lib       | 86.5 ms                                                               | 73.8 ms: 1.17x faster                                                    |
| tornado_http   | 178 ms                                                                | 139 ms: 1.29x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 522 ms: 1.82x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.27 sec: 1.79x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 685 ms: 1.66x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 827 ms: 1.54x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.70x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 119 ms: 1.14x faster                                                     |
| nbody          | 166 ms                                                                | 152 ms: 1.09x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                    |
| regex_compile  | 177 ms                                                                | 172 ms: 1.03x faster                                                     |
| regex_dna      | 257 ms                                                                | 258 ms: 1.00x slower                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps          | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| pickle_pure_python  | 529 us                                                                | 467 us: 1.13x faster                                                     |
| xml_etree_process   | 99.5 ms                                                               | 90.9 ms: 1.10x faster                                                    |
| xml_etree_parse     | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| unpickle_list       | 6.99 us                                                               | 6.68 us: 1.05x faster                                                    |
| tomli_loads         | 3.36 sec                                                              | 3.23 sec: 1.04x faster                                                   |
| pickle_list         | 5.24 us                                                               | 5.31 us: 1.01x slower                                                    |
| xml_etree_iterparse | 156 ms                                                                | 162 ms: 1.04x slower                                                     |
| json_loads          | 30.9 us                                                               | 32.1 us: 1.04x slower                                                    |
| xml_etree_generate  | 123 ms                                                                | 130 ms: 1.06x slower                                                     |
| pickle_dict         | 35.1 us                                                               | 37.9 us: 1.08x slower                                                    |
| pickle              | 12.5 us                                                               | 13.5 us: 1.08x slower                                                    |
| unpickle            | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                    |
| django_template | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 36.8 ms: 1.05x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 227 us: 2.91x faster                                                     |
| async_tree_none          | 950 ms                                                                | 522 ms: 1.82x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.27 sec: 1.79x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 8.58 ms: 1.69x faster                                                    |
| deltablue                | 8.94 ms                                                               | 5.31 ms: 1.68x faster                                                    |
| generators               | 68.1 ms                                                               | 40.7 ms: 1.67x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 685 ms: 1.66x faster                                                     |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 602 ms: 1.57x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 827 ms: 1.54x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.27 sec: 1.45x faster                                                   |
| richards_super           | 107 ms                                                                | 75.4 ms: 1.42x faster                                                    |
| chaos                    | 121 ms                                                                | 89.3 ms: 1.36x faster                                                    |
| richards                 | 91.7 ms                                                               | 68.9 ms: 1.33x faster                                                    |
| go                       | 264 ms                                                                | 199 ms: 1.33x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.43 us: 1.32x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.83 ms: 1.31x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.16 us: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 969 us: 1.30x faster                                                     |
| tornado_http             | 178 ms                                                                | 139 ms: 1.29x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 106 ms: 1.27x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.25 ms: 1.26x faster                                                    |
| scimark_sor              | 246 ms                                                                | 200 ms: 1.23x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                                   |
| pylint                   | 485 ms                                                                | 395 ms: 1.23x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 73.8 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| dask                     | 450 ms                                                                | 392 ms: 1.15x faster                                                     |
| float                    | 135 ms                                                                | 119 ms: 1.14x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 467 us: 1.13x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.4 ms: 1.13x faster                                                    |
| logging_silent           | 222 ns                                                                | 199 ns: 1.12x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 66.7 ms: 1.10x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 90.9 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| nbody                    | 166 ms                                                                | 152 ms: 1.09x faster                                                     |
| mako                     | 18.9 ms                                                               | 17.5 ms: 1.08x faster                                                    |
| mypy2                    | 936 ms                                                                | 866 ms: 1.08x faster                                                     |
| pyflate                  | 795 ms                                                                | 738 ms: 1.08x faster                                                     |
| 2to3                     | 381 ms                                                                | 357 ms: 1.07x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 120 ms: 1.06x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.31 ms: 1.06x faster                                                    |
| gunicorn                 | 1.45 ms                                                               | 1.37 ms: 1.06x faster                                                    |
| chameleon                | 10.8 ms                                                               | 10.3 ms: 1.06x faster                                                    |
| scimark_lu               | 227 ms                                                                | 215 ms: 1.06x faster                                                     |
| comprehensions           | 33.1 us                                                               | 31.5 us: 1.05x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.68 us: 1.05x faster                                                    |
| sympy_sum                | 184 ms                                                                | 176 ms: 1.05x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.23 sec: 1.04x faster                                                   |
| sympy_expand             | 543 ms                                                                | 523 ms: 1.04x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 151 ms: 1.03x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 73.0 ms: 1.03x faster                                                    |
| sympy_str                | 329 ms                                                                | 318 ms: 1.03x faster                                                     |
| regex_compile            | 177 ms                                                                | 172 ms: 1.03x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.61 sec: 1.02x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 4.04 us: 1.02x faster                                                    |
| regex_dna                | 257 ms                                                                | 258 ms: 1.00x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.31 us: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.60 sec: 1.02x slower                                                   |
| spectral_norm            | 186 ms                                                                | 191 ms: 1.02x slower                                                     |
| hexiom                   | 10.9 ms                                                               | 11.3 ms: 1.03x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 162 ms: 1.04x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 36.8 ms: 1.05x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.47 sec: 1.05x slower                                                   |
| fannkuch                 | 546 ms                                                                | 574 ms: 1.05x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 130 ms: 1.06x slower                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.88 us: 1.06x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.41 ms: 1.07x slower                                                    |
| meteor_contest           | 126 ms                                                                | 135 ms: 1.07x slower                                                     |
| flaskblogging            | 4.83 ms                                                               | 5.17 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.9 us: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.08x slower                                                    |
| deepcopy                 | 511 us                                                                | 555 us: 1.09x slower                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.41 ms: 1.10x slower                                                    |
| scimark_fft              | 500 ms                                                                | 558 ms: 1.12x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 78.6 ms: 1.13x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.9 us: 1.14x slower                                                    |
| async_generators         | 452 ms                                                                | 517 ms: 1.14x slower                                                     |
| nqueens                  | 117 ms                                                                | 134 ms: 1.14x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.3 ms: 1.19x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 75.8 us: 1.23x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.21 ms: 1.25x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.9 ms: 1.28x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, sympy_integrate, json, pidigits, asyncio_websockets
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.15x