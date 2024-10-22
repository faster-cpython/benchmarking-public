# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 518 ms: 1.36x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| html5lib       | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| tornado_http   | 178 ms                                                                | 207 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.41 sec: 1.62x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 739 ms: 1.53x faster                                                    |
| async_tree_none         | 950 ms                                                                | 625 ms: 1.52x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 914 ms: 1.39x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.51x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 207 ms: 1.54x slower                                                    |
| nbody          | 166 ms                                                                | 281 ms: 1.69x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.38x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 261 ms: 1.01x slower                                                    |
| regex_v8       | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.48 ms: 1.06x slower                                                   |
| regex_compile  | 177 ms                                                                | 259 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                    |
| pickle               | 12.5 us                                                               | 13.3 us: 1.07x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 17.9 ms: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 21.7 us: 1.24x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.19 sec: 1.25x slower                                                  |
| json_loads           | 30.9 us                                                               | 39.3 us: 1.27x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 130 ms: 1.31x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 777 us: 1.47x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 542 us: 1.48x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x slower                                                            |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.2 ms: 1.63x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.70x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.49x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 53.3 ms: 1.52x slower                                                   |
| mako            | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| django_template | 53.3 ms                                                               | 83.4 ms: 1.56x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.52x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 7.20 ms: 2.02x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 336 us: 1.97x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.41 sec: 1.62x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 739 ms: 1.53x faster                                                    |
| async_tree_none          | 950 ms                                                                | 625 ms: 1.52x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.62 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 914 ms: 1.39x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 683 ms: 1.38x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.62 sec: 1.25x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.45 ms: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 57.7 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                    |
| regex_dna                | 257 ms                                                                | 261 ms: 1.01x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 26.8 ms: 1.02x slower                                                   |
| crypto_pyaes             | 134 ms                                                                | 137 ms: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| regex_v8                 | 32.2 ms                                                               | 33.0 ms: 1.03x slower                                                   |
| pylint                   | 485 ms                                                                | 511 ms: 1.05x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.48 ms: 1.06x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.3 us: 1.07x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 17.9 ms: 1.07x slower                                                   |
| coroutines               | 37.2 ms                                                               | 40.9 ms: 1.10x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.8 us: 1.10x slower                                                   |
| deepcopy                 | 511 us                                                                | 571 us: 1.12x slower                                                    |
| scimark_fft              | 500 ms                                                                | 573 ms: 1.14x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.82 ms: 1.16x slower                                                   |
| tornado_http             | 178 ms                                                                | 207 ms: 1.16x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| deepcopy_memo            | 61.7 us                                                               | 72.1 us: 1.17x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.32 sec: 1.17x slower                                                  |
| pycparser                | 1.69 sec                                                              | 2.02 sec: 1.19x slower                                                  |
| json                     | 5.88 ms                                                               | 7.03 ms: 1.20x slower                                                   |
| spectral_norm            | 186 ms                                                                | 226 ms: 1.21x slower                                                    |
| comprehensions           | 33.1 us                                                               | 40.9 us: 1.23x slower                                                   |
| unpickle                 | 17.5 us                                                               | 21.7 us: 1.24x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.19 sec: 1.25x slower                                                  |
| json_loads               | 30.9 us                                                               | 39.3 us: 1.27x slower                                                   |
| richards                 | 91.7 ms                                                               | 117 ms: 1.27x slower                                                    |
| logging_silent           | 222 ns                                                                | 284 ns: 1.28x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.02 sec: 1.28x slower                                                  |
| nqueens                  | 117 ms                                                                | 152 ms: 1.30x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 34.7 ms: 1.31x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 96.1 ms: 1.31x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 130 ms: 1.31x slower                                                    |
| chaos                    | 121 ms                                                                | 160 ms: 1.32x slower                                                    |
| meteor_contest           | 126 ms                                                                | 167 ms: 1.32x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 163 ms: 1.32x slower                                                    |
| richards_super           | 107 ms                                                                | 143 ms: 1.33x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 6.14 us: 1.34x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 2.13 ms: 1.34x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.69 ms: 1.34x slower                                                   |
| fannkuch                 | 546 ms                                                                | 738 ms: 1.35x slower                                                    |
| 2to3                     | 381 ms                                                                | 518 ms: 1.36x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 176 ms: 1.38x slower                                                    |
| scimark_sor              | 246 ms                                                                | 341 ms: 1.38x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| raytrace                 | 573 ms                                                                | 815 ms: 1.42x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.7 ms: 1.42x slower                                                   |
| async_generators         | 452 ms                                                                | 653 ms: 1.44x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.9 ms: 1.46x slower                                                   |
| pickle_pure_python       | 529 us                                                                | 777 us: 1.47x slower                                                    |
| regex_compile            | 177 ms                                                                | 259 ms: 1.47x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 542 us: 1.48x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.49x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.6 us: 1.49x slower                                                   |
| logging_format           | 10.6 us                                                               | 15.9 us: 1.50x slower                                                   |
| telco                    | 8.49 ms                                                               | 12.8 ms: 1.51x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 53.3 ms: 1.52x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 237 ms: 1.52x slower                                                    |
| mako                     | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 3.67 ms: 1.53x slower                                                   |
| go                       | 264 ms                                                                | 404 ms: 1.53x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.76 sec: 1.53x slower                                                  |
| float                    | 135 ms                                                                | 207 ms: 1.54x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.64 sec: 1.54x slower                                                  |
| scimark_lu               | 227 ms                                                                | 350 ms: 1.54x slower                                                    |
| django_template          | 53.3 ms                                                               | 83.4 ms: 1.56x slower                                                   |
| sympy_str                | 329 ms                                                                | 514 ms: 1.57x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.45 ms: 1.57x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 119 ms: 1.57x slower                                                    |
| coverage                 | 83.6 ms                                                               | 136 ms: 1.62x slower                                                    |
| python_startup           | 11.2 ms                                                               | 18.2 ms: 1.63x slower                                                   |
| nbody                    | 166 ms                                                                | 281 ms: 1.69x slower                                                    |
| sympy_sum                | 184 ms                                                                | 318 ms: 1.73x slower                                                    |
| sympy_expand             | 543 ms                                                                | 961 ms: 1.77x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (5): pidigits, unpickle_list, xml_etree_iterparse, sqlite_synth, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.24x
- 95% likely to have a slowdown of 1.21x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: 1.33x