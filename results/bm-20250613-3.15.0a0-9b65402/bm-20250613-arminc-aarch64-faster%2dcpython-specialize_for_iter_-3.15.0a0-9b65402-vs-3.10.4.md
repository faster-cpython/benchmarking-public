# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.232x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 888 ms: 2.57x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                              |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 656 ms: 1.94x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 85.5 ms: 1.58x faster                                                             |
| nbody          | 166 ms                                                                | 122 ms: 1.35x faster                                                              |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.44x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                             |
| regex_dna      | 257 ms                                                                | 221 ms: 1.17x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 259 us: 1.41x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                             |
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 190 us: 3.48x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 888 ms: 2.57x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                              |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                            |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 656 ms: 1.94x faster                                                              |
| generators               | 68.1 ms                                                               | 36.0 ms: 1.89x faster                                                             |
| chaos                    | 121 ms                                                                | 65.8 ms: 1.84x faster                                                             |
| richards_super           | 107 ms                                                                | 59.1 ms: 1.81x faster                                                             |
| richards                 | 91.7 ms                                                               | 51.4 ms: 1.78x faster                                                             |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                              |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.69x faster                                                              |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.76 ms: 1.61x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 83.6 ms: 1.60x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 38.6 us: 1.60x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 80.7 ms: 1.58x faster                                                             |
| float                    | 135 ms                                                                | 85.5 ms: 1.58x faster                                                             |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                              |
| pyflate                  | 795 ms                                                                | 516 ms: 1.54x faster                                                              |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                              |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.47x faster                                                              |
| regex_compile            | 177 ms                                                                | 122 ms: 1.44x faster                                                              |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 259 us: 1.41x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 52.3 ms: 1.41x faster                                                             |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| nbody                    | 166 ms                                                                | 122 ms: 1.35x faster                                                              |
| django_template          | 53.3 ms                                                               | 39.4 ms: 1.35x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                                            |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 19.8 ms: 1.34x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 26.6 ms: 1.32x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.10 us: 1.31x faster                                                             |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                              |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                              |
| logging_simple           | 9.78 us                                                               | 7.71 us: 1.27x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                             |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                             |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                              |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.20x faster                                                            |
| nqueens                  | 117 ms                                                                | 98.1 ms: 1.20x faster                                                             |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                             |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.17x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                              |
| regex_dna                | 257 ms                                                                | 221 ms: 1.17x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.03 sec: 1.16x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 994 ms: 1.15x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                             |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                              |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                              |
| fannkuch                 | 546 ms                                                                | 481 ms: 1.13x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.92 ms: 1.10x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| regex_effbot             | 4.25 ms                                                               | 3.93 ms: 1.08x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                                             |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                             |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                                              |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.20 ms: 1.08x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.73 ms: 1.62x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.78 ms: 1.67x slower                                                             |
| logging_silent           | 222 ns                                                                | 620 ns: 2.79x slower                                                              |
| coverage                 | 83.6 ms                                                               | 556 ms: 6.65x slower                                                              |
| thrift                   | 1.26 ms                                                               | 197 ms: 156.38x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                                      |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.232x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.37x