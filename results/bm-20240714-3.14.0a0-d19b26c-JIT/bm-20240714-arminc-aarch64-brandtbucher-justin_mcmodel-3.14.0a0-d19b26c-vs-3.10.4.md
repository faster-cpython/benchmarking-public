# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-aarch64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 361 ms: 1.06x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.55 sec: 1.01x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.2 ms: 1.21x faster                                                   |
| tornado_http   | 178 ms                                                                | 144 ms: 1.24x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none         | 950 ms                                                                | 447 ms: 2.12x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 587 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 737 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.2 ms: 1.51x faster                                                   |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_compile  | 177 ms                                                                | 175 ms: 1.01x faster                                                    |
| regex_dna      | 257 ms                                                                | 259 ms: 1.01x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.95 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 279 us: 1.31x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 411 us: 1.29x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| django_template | 53.3 ms                                                               | 50.3 ms: 1.06x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 84.9 ms: 1.22x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.19x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none          | 950 ms                                                                | 447 ms: 2.12x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 587 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 38.3 ms: 1.78x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.77x faster                                                    |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 737 ms: 1.73x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.8 ms: 1.67x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.8 us: 1.59x faster                                                   |
| logging_silent           | 222 ns                                                                | 142 ns: 1.56x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 625 ms: 1.51x faster                                                    |
| float                    | 135 ms                                                                | 89.2 ms: 1.51x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 90.0 ms: 1.49x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.61 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.7 us: 1.40x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 91.5 ms: 1.40x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.04 ms: 1.39x faster                                                   |
| scimark_sor              | 246 ms                                                                | 177 ms: 1.39x faster                                                    |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.28 us: 1.34x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.90 us: 1.34x faster                                                   |
| deepcopy                 | 511 us                                                                | 382 us: 1.34x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 279 us: 1.31x faster                                                    |
| chaos                    | 121 ms                                                                | 93.3 ms: 1.30x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 411 us: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 978 us: 1.29x faster                                                    |
| pyflate                  | 795 ms                                                                | 621 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.67 sec: 1.26x faster                                                  |
| coroutines               | 37.2 ms                                                               | 29.6 ms: 1.26x faster                                                   |
| spectral_norm            | 186 ms                                                                | 149 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 8.81 ms: 1.24x faster                                                   |
| tornado_http             | 178 ms                                                                | 144 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.24x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 71.2 ms: 1.21x faster                                                   |
| pylint                   | 485 ms                                                                | 408 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                   |
| dask                     | 450 ms                                                                | 390 ms: 1.15x faster                                                    |
| fannkuch                 | 546 ms                                                                | 474 ms: 1.15x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 68.5 ms: 1.10x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.21 us: 1.09x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.00 ms: 1.09x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                  |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| scimark_fft              | 500 ms                                                                | 472 ms: 1.06x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.3 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 361 ms: 1.06x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.6 ms: 1.02x faster                                                   |
| sympy_str                | 329 ms                                                                | 323 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 26.3 ms: 1.01x faster                                                   |
| regex_compile            | 177 ms                                                                | 175 ms: 1.01x faster                                                    |
| sympy_sum                | 184 ms                                                                | 183 ms: 1.01x faster                                                    |
| regex_dna                | 257 ms                                                                | 259 ms: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.55 sec: 1.01x slower                                                  |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.16 sec: 1.01x slower                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.42 sec: 1.02x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 511 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.95 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.7 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.04 ms: 1.21x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 84.9 ms: 1.22x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                            |

Benchmark hidden because not significant (5): bench_mp_pool, dulwich_log, pidigits, sympy_expand, nqueens
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.22x