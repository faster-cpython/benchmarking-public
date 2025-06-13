# Results vs. 3.10.4

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-aarch64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 908 ms: 2.52x faster                                                    |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.6 ms: 1.57x faster                                                   |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                    |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| regex_dna      | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 260 us: 1.40x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 383 us: 1.38x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.38x faster                                                   |
| django_template | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.36x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 908 ms: 2.52x faster                                                    |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                                  |
| go                       | 264 ms                                                                | 128 ms: 2.07x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 657 ms: 1.94x faster                                                    |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                   |
| richards_super           | 107 ms                                                                | 60.2 ms: 1.78x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                   |
| chaos                    | 121 ms                                                                | 70.9 ms: 1.71x faster                                                   |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.7 ms: 1.62x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 79.3 ms: 1.61x faster                                                   |
| float                    | 135 ms                                                                | 85.6 ms: 1.57x faster                                                   |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                    |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                    |
| pyflate                  | 795 ms                                                                | 525 ms: 1.51x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 50.3 ms: 1.46x faster                                                   |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 260 us: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 383 us: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.38x faster                                                   |
| django_template          | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                  |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.50 us: 1.30x faster                                                   |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.27 us: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.63 us: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.89 sec: 1.22x faster                                                  |
| sympy_str                | 329 ms                                                                | 274 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| sympy_expand             | 543 ms                                                                | 465 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 477 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 438 ms: 1.14x faster                                                    |
| regex_dna                | 257 ms                                                                | 225 ms: 1.14x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.07 sec: 1.14x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.02 sec: 1.13x faster                                                  |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.99 ms: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.78 us: 1.09x faster                                                   |
| json                     | 5.88 ms                                                               | 5.67 ms: 1.04x faster                                                   |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.31 ms: 1.10x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.86 ms: 1.65x slower                                                   |
| logging_silent           | 222 ns                                                                | 629 ns: 2.83x slower                                                    |
| coverage                 | 83.6 ms                                                               | 545 ms: 6.52x slower                                                    |
| thrift                   | 1.26 ms                                                               | 194 ms: 153.78x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x