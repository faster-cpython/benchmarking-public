# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.223x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 61.1 ms: 1.42x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 879 ms: 2.60x faster                                                              |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 464 ms: 2.44x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 660 ms: 1.93x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| nbody          | 166 ms                                                                | 120 ms: 1.39x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.45x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                             |
| regex_dna      | 257 ms                                                                | 229 ms: 1.12x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                            |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 78.6 ms: 1.27x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| json_loads           | 30.9 us                                                               | 35.3 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 202 us: 3.28x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 879 ms: 2.60x faster                                                              |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 464 ms: 2.44x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.71 sec: 2.16x faster                                                            |
| go                       | 264 ms                                                                | 129 ms: 2.05x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 660 ms: 1.93x faster                                                              |
| richards_super           | 107 ms                                                                | 57.7 ms: 1.86x faster                                                             |
| generators               | 68.1 ms                                                               | 36.7 ms: 1.85x faster                                                             |
| richards                 | 91.7 ms                                                               | 51.1 ms: 1.79x faster                                                             |
| chaos                    | 121 ms                                                                | 69.0 ms: 1.75x faster                                                             |
| raytrace                 | 573 ms                                                                | 328 ms: 1.75x faster                                                              |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 82.1 ms: 1.63x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 81.1 ms: 1.58x faster                                                             |
| pylint                   | 485 ms                                                                | 310 ms: 1.57x faster                                                              |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                              |
| hexiom                   | 10.9 ms                                                               | 7.01 ms: 1.56x faster                                                             |
| scimark_lu               | 227 ms                                                                | 147 ms: 1.54x faster                                                              |
| float                    | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| pyflate                  | 795 ms                                                                | 541 ms: 1.47x faster                                                              |
| spectral_norm            | 186 ms                                                                | 128 ms: 1.45x faster                                                              |
| regex_compile            | 177 ms                                                                | 121 ms: 1.45x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 61.1 ms: 1.42x faster                                                             |
| dulwich_log              | 73.5 ms                                                               | 52.6 ms: 1.40x faster                                                             |
| nbody                    | 166 ms                                                                | 120 ms: 1.39x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.44 sec: 1.38x faster                                                            |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                            |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                             |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                                             |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.53 us: 1.30x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.70 us: 1.27x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 78.6 ms: 1.27x faster                                                             |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                              |
| logging_format           | 10.6 us                                                               | 8.41 us: 1.26x faster                                                             |
| coroutines               | 37.2 ms                                                               | 30.0 ms: 1.24x faster                                                             |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                            |
| nqueens                  | 117 ms                                                                | 98.1 ms: 1.20x faster                                                             |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 27.4 ms: 1.18x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.02 sec: 1.17x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 985 ms: 1.16x faster                                                              |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                              |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                             |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 61.5 ms: 1.14x faster                                                             |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                              |
| regex_dna                | 257 ms                                                                | 229 ms: 1.12x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.83 ms: 1.12x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.08x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                              |
| json                     | 5.88 ms                                                               | 6.07 ms: 1.03x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.38 ms: 1.11x slower                                                             |
| json_loads               | 30.9 us                                                               | 35.3 us: 1.14x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.78 ms: 1.67x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.97 ms: 1.68x slower                                                             |
| logging_silent           | 222 ns                                                                | 628 ns: 2.83x slower                                                              |
| coverage                 | 83.6 ms                                                               | 553 ms: 6.62x slower                                                              |
| thrift                   | 1.26 ms                                                               | 193 ms: 152.96x slower                                                            |
| bench_mp_pool            | 14.5 ms                                                               | 2.26 sec: 155.45x slower                                                          |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.223x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.35x