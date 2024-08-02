# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| chameleon      | 10.8 ms                                                               | 8.99 ms: 1.21x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                    |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 487 ms: 1.95x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 647 ms: 1.75x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 781 ms: 1.63x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.81x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.1 ms: 1.48x faster                                                    |
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.45x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.48 us: 1.08x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                                    |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| django_template | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.04 ms: 2.07x faster                                                    |
| async_tree_none          | 950 ms                                                                | 487 ms: 1.95x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                   |
| raytrace                 | 573 ms                                                                | 298 ms: 1.92x faster                                                     |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.83x faster                                                    |
| chaos                    | 121 ms                                                                | 68.7 ms: 1.76x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 647 ms: 1.75x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.73x faster                                                    |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                    |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                     |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 574 ms: 1.65x faster                                                     |
| richards                 | 91.7 ms                                                               | 55.9 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 781 ms: 1.63x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                    |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.61x faster                                                     |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 82.5 ms: 1.55x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                   |
| float                    | 135 ms                                                                | 91.1 ms: 1.48x faster                                                    |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.45x faster                                                     |
| pylint                   | 485 ms                                                                | 338 ms: 1.44x faster                                                     |
| pyflate                  | 795 ms                                                                | 559 ms: 1.42x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.01 us: 1.39x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.73 us: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| thrift                   | 1.26 ms                                                               | 951 us: 1.32x faster                                                     |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.8 ms: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.26x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                                     |
| sympy_str                | 329 ms                                                                | 266 ms: 1.23x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 59.7 ms: 1.23x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                     |
| mypy2                    | 936 ms                                                                | 764 ms: 1.22x faster                                                     |
| dask                     | 450 ms                                                                | 369 ms: 1.22x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 50.8 us: 1.21x faster                                                    |
| fannkuch                 | 546 ms                                                                | 451 ms: 1.21x faster                                                     |
| chameleon                | 10.8 ms                                                               | 8.99 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.7 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.8 ms: 1.19x faster                                                    |
| aiohttp                  | 1.39 ms                                                               | 1.18 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.24 ms: 1.16x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.56 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                                    |
| deepcopy                 | 511 us                                                                | 448 us: 1.14x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.06 us: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.48 us: 1.08x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.60 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| pickle_list              | 5.24 us                                                               | 5.30 us: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                    |
| async_generators         | 452 ms                                                                | 493 ms: 1.09x slower                                                     |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.87 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.3 ms: 1.18x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.22 ms: 1.26x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (3): pidigits, flaskblogging, asyncio_websockets
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x