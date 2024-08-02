# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 365 ms: 1.04x faster                                                     |
| chameleon      | 10.8 ms                                                               | 9.29 ms: 1.17x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                   |
| html5lib       | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                                    |
| tornado_http   | 178 ms                                                                | 150 ms: 1.19x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 504 ms: 1.88x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.84x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 666 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 817 ms: 1.56x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.74x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.2 ms: 1.51x faster                                                    |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| pidigits       | 235 ms                                                                | 234 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 260 ms: 1.01x slower                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 83.1 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.63 us: 1.05x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.28 us: 1.01x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.0 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 11.2 ms: 1.63x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.52x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                    |
| django_template | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.58 ms: 1.95x faster                                                    |
| async_tree_none          | 950 ms                                                                | 504 ms: 1.88x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.84x faster                                                   |
| raytrace                 | 573 ms                                                                | 318 ms: 1.80x faster                                                     |
| generators               | 68.1 ms                                                               | 39.5 ms: 1.72x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.50 ms: 1.71x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 666 ms: 1.70x faster                                                     |
| richards_super           | 107 ms                                                                | 63.0 ms: 1.70x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.5 ms: 1.62x faster                                                    |
| logging_silent           | 222 ns                                                                | 138 ns: 1.60x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 817 ms: 1.56x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 87.1 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 89.2 ms: 1.51x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                    |
| go                       | 264 ms                                                                | 180 ms: 1.46x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 645 ms: 1.46x faster                                                     |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 88.1 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.44x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                    |
| scimark_sor              | 246 ms                                                                | 173 ms: 1.42x faster                                                     |
| chaos                    | 121 ms                                                                | 86.1 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.27 us: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                     |
| pyflate                  | 795 ms                                                                | 599 ms: 1.33x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.02 us: 1.32x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                     |
| thrift                   | 1.26 ms                                                               | 971 us: 1.30x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.27x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 49.4 us: 1.25x faster                                                    |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 8.91 ms: 1.22x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.7 ms: 1.21x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.1 ms: 1.20x faster                                                    |
| tornado_http             | 178 ms                                                                | 150 ms: 1.19x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.29 ms: 1.17x faster                                                    |
| pylint                   | 485 ms                                                                | 417 ms: 1.17x faster                                                     |
| fannkuch                 | 546 ms                                                                | 469 ms: 1.16x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| dask                     | 450 ms                                                                | 403 ms: 1.12x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                    |
| scimark_fft              | 500 ms                                                                | 460 ms: 1.09x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 69.3 ms: 1.09x faster                                                    |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                                   |
| django_template          | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| gunicorn                 | 1.45 ms                                                               | 1.37 ms: 1.06x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.63 us: 1.05x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| 2to3                     | 381 ms                                                                | 365 ms: 1.04x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.35 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.3 ms: 1.03x faster                                                    |
| deepcopy                 | 511 us                                                                | 497 us: 1.03x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                   |
| nqueens                  | 117 ms                                                                | 116 ms: 1.02x faster                                                     |
| pidigits                 | 235 ms                                                                | 234 ms: 1.01x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 26.7 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.28 us: 1.01x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.64 us: 1.01x slower                                                    |
| sympy_str                | 329 ms                                                                | 332 ms: 1.01x slower                                                     |
| regex_dna                | 257 ms                                                                | 260 ms: 1.01x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.62 sec: 1.03x slower                                                   |
| sympy_expand             | 543 ms                                                                | 561 ms: 1.03x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| sympy_sum                | 184 ms                                                                | 191 ms: 1.04x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 77.4 ms: 1.05x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.42 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                    |
| flaskblogging            | 4.83 ms                                                               | 5.25 ms: 1.09x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| async_generators         | 452 ms                                                                | 509 ms: 1.13x slower                                                     |
| unpickle                 | 17.5 us                                                               | 20.0 us: 1.15x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.4 ms: 1.18x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.19 ms: 1.25x slower                                                    |
| python_startup           | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 11.2 ms: 1.63x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, mypy2
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.25x