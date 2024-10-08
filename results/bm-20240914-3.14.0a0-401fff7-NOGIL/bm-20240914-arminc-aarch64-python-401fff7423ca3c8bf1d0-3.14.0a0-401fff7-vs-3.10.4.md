# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.18x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 509 ms: 1.34x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.97 sec: 1.13x slower                                                  |
| html5lib       | 86.5 ms                                                               | 118 ms: 1.37x slower                                                    |
| tornado_http   | 178 ms                                                                | 203 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.37 sec: 1.67x faster                                                  |
| async_tree_none         | 950 ms                                                                | 600 ms: 1.58x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 723 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 901 ms: 1.41x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 205 ms: 1.52x slower                                                    |
| nbody          | 166 ms                                                                | 281 ms: 1.70x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.37x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| regex_compile  | 177 ms                                                                | 246 ms: 1.39x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 153 ms: 1.02x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.35 us: 1.02x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| pickle               | 12.5 us                                                               | 13.2 us: 1.06x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 39.0 us: 1.11x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.12 sec: 1.23x slower                                                  |
| unpickle             | 17.5 us                                                               | 21.5 us: 1.23x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.1 us: 1.23x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 125 ms: 1.25x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 155 ms: 1.26x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 749 us: 1.42x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 525 us: 1.44x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x slower                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.68x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 100 ms: 1.43x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 51.0 ms: 1.45x slower                                                   |
| django_template | 53.3 ms                                                               | 79.2 ms: 1.48x slower                                                   |
| mako            | 18.9 ms                                                               | 28.4 ms: 1.50x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.47x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.94 ms: 2.09x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 324 us: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.37 sec: 1.67x faster                                                  |
| async_tree_none          | 950 ms                                                                | 600 ms: 1.58x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 723 ms: 1.57x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 901 ms: 1.41x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.60 ms: 1.41x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 677 ms: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.61 sec: 1.26x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.46 ms: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 58.3 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.01 us: 1.03x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 153 ms: 1.02x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.35 us: 1.02x slower                                                   |
| crypto_pyaes             | 134 ms                                                                | 137 ms: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| deepcopy                 | 511 us                                                                | 530 us: 1.04x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| pylint                   | 485 ms                                                                | 506 ms: 1.04x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.47 ms: 1.05x slower                                                   |
| coroutines               | 37.2 ms                                                               | 39.2 ms: 1.06x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.2 us: 1.06x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 67.7 us: 1.10x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 39.0 us: 1.11x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.97 sec: 1.13x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.64 ms: 1.13x slower                                                   |
| tornado_http             | 178 ms                                                                | 203 ms: 1.14x slower                                                    |
| json                     | 5.88 ms                                                               | 6.75 ms: 1.15x slower                                                   |
| scimark_fft              | 500 ms                                                                | 579 ms: 1.16x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.29 sec: 1.16x slower                                                  |
| pycparser                | 1.69 sec                                                              | 1.99 sec: 1.18x slower                                                  |
| comprehensions           | 33.1 us                                                               | 40.1 us: 1.21x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.12 sec: 1.23x slower                                                  |
| unpickle                 | 17.5 us                                                               | 21.5 us: 1.23x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.1 us: 1.23x slower                                                   |
| spectral_norm            | 186 ms                                                                | 231 ms: 1.24x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 5.71 us: 1.24x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 125 ms: 1.25x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.00 sec: 1.26x slower                                                  |
| xml_etree_generate       | 123 ms                                                                | 155 ms: 1.26x slower                                                    |
| nqueens                  | 117 ms                                                                | 149 ms: 1.27x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 2.02 ms: 1.27x slower                                                   |
| logging_silent           | 222 ns                                                                | 285 ns: 1.28x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 95.1 ms: 1.29x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 34.4 ms: 1.30x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.63 ms: 1.30x slower                                                   |
| richards                 | 91.7 ms                                                               | 119 ms: 1.30x slower                                                    |
| richards_super           | 107 ms                                                                | 140 ms: 1.31x slower                                                    |
| chaos                    | 121 ms                                                                | 160 ms: 1.32x slower                                                    |
| meteor_contest           | 126 ms                                                                | 167 ms: 1.32x slower                                                    |
| 2to3                     | 381 ms                                                                | 509 ms: 1.34x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 172 ms: 1.34x slower                                                    |
| fannkuch                 | 546 ms                                                                | 741 ms: 1.36x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 118 ms: 1.37x slower                                                    |
| scimark_sor              | 246 ms                                                                | 341 ms: 1.39x slower                                                    |
| regex_compile            | 177 ms                                                                | 246 ms: 1.39x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.5 ms: 1.39x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 219 ms: 1.40x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.3 ms: 1.40x slower                                                   |
| pickle_pure_python       | 529 us                                                                | 749 us: 1.42x slower                                                    |
| raytrace                 | 573 ms                                                                | 813 ms: 1.42x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 100 ms: 1.43x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 525 us: 1.44x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.65 sec: 1.44x slower                                                  |
| logging_simple           | 9.78 us                                                               | 14.1 us: 1.44x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 3.40 sec: 1.44x slower                                                  |
| go                       | 264 ms                                                                | 382 ms: 1.45x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 109 ms: 1.45x slower                                                    |
| async_generators         | 452 ms                                                                | 656 ms: 1.45x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 51.0 ms: 1.45x slower                                                   |
| scimark_lu               | 227 ms                                                                | 329 ms: 1.45x slower                                                    |
| logging_format           | 10.6 us                                                               | 15.5 us: 1.46x slower                                                   |
| django_template          | 53.3 ms                                                               | 79.2 ms: 1.48x slower                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 4.22 ms: 1.49x slower                                                   |
| telco                    | 8.49 ms                                                               | 12.7 ms: 1.49x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.4 ms: 1.50x slower                                                   |
| float                    | 135 ms                                                                | 205 ms: 1.52x slower                                                    |
| sympy_str                | 329 ms                                                                | 507 ms: 1.54x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.71 ms: 1.54x slower                                                   |
| coverage                 | 83.6 ms                                                               | 130 ms: 1.56x slower                                                    |
| python_startup           | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| nbody                    | 166 ms                                                                | 281 ms: 1.70x slower                                                    |
| sympy_sum                | 184 ms                                                                | 317 ms: 1.72x slower                                                    |
| sympy_expand             | 543 ms                                                                | 936 ms: 1.72x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.0 ms: 1.74x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.18x slower                                                            |

Benchmark hidden because not significant (5): pathlib, pidigits, unpickle_list, regex_v8, regex_dna
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.32x