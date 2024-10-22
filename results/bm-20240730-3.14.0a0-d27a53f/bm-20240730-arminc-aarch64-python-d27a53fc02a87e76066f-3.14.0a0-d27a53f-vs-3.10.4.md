# Results vs. 3.10.4

- fork: python
- ref: d27a53fc02a87e76066f
- machine: linux-aarch64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.8 ms: 1.28x faster                                                   |
| tornado_http   | 178 ms                                                                | 124 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 438 ms: 2.17x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.09 sec: 2.09x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                   |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 365 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.80 ms: 2.35x faster                                                   |
| async_tree_none          | 950 ms                                                                | 438 ms: 2.17x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.09 sec: 2.09x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.01 ms: 2.07x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.95x faster                                                   |
| raytrace                 | 573 ms                                                                | 294 ms: 1.95x faster                                                    |
| richards_super           | 107 ms                                                                | 58.7 ms: 1.83x faster                                                   |
| chaos                    | 121 ms                                                                | 67.0 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.73x faster                                                   |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 558 ms: 1.69x faster                                                    |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.65x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.4 ms: 1.59x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                    |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.19 sec: 1.50x faster                                                  |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 365 us: 1.45x faster                                                    |
| tornado_http             | 178 ms                                                                | 124 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                   |
| pyflate                  | 795 ms                                                                | 562 ms: 1.41x faster                                                    |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.04 us: 1.39x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 3.34 us: 1.37x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                   |
| pylint                   | 485 ms                                                                | 357 ms: 1.36x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.52 sec: 1.33x faster                                                  |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.1 ms: 1.32x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| thrift                   | 1.26 ms                                                               | 974 us: 1.29x faster                                                    |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 67.8 ms: 1.28x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.9 ms: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                    |
| dask                     | 450 ms                                                                | 365 ms: 1.23x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.94 sec: 1.22x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 948 ms: 1.21x faster                                                    |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.44 ms: 1.18x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.8 ms: 1.18x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 185 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                                  |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                                   |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.04x slower                                                   |
| async_generators         | 452 ms                                                                | 484 ms: 1.07x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.84 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.18x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.06 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.80 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-arminc-aarch64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.15x