# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.19x faster                                                            |
| html5lib       | 86.5 ms                                                               | 62.4 ms: 1.38x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 896 ms: 2.55x faster                                                              |
| async_tree_none         | 950 ms                                                                | 389 ms: 2.44x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 467 ms: 2.43x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 656 ms: 1.94x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                                              |
| pidigits       | 235 ms                                                                | 236 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.3 ms: 1.18x faster                                                             |
| regex_dna      | 257 ms                                                                | 225 ms: 1.14x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                            |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.17x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.1 ms: 1.37x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                             |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.3 ms: 1.14x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 896 ms: 2.55x faster                                                              |
| async_tree_none          | 950 ms                                                                | 389 ms: 2.44x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 467 ms: 2.43x faster                                                              |
| mdp                      | 3.70 sec                                                              | 1.63 sec: 2.27x faster                                                            |
| deltablue                | 8.94 ms                                                               | 3.99 ms: 2.24x faster                                                             |
| go                       | 264 ms                                                                | 126 ms: 2.10x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 656 ms: 1.94x faster                                                              |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.89x faster                                                             |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                             |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                              |
| richards                 | 91.7 ms                                                               | 52.4 ms: 1.75x faster                                                             |
| chaos                    | 121 ms                                                                | 69.5 ms: 1.74x faster                                                             |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.73x faster                                                              |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 83.7 ms: 1.60x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.92 ms: 1.58x faster                                                             |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 39.2 us: 1.57x faster                                                             |
| float                    | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| pyflate                  | 795 ms                                                                | 513 ms: 1.55x faster                                                              |
| pylint                   | 485 ms                                                                | 316 ms: 1.54x faster                                                              |
| spectral_norm            | 186 ms                                                                | 124 ms: 1.50x faster                                                              |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.48x faster                                                              |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.42 sec: 1.39x faster                                                            |
| html5lib                 | 86.5 ms                                                               | 62.4 ms: 1.38x faster                                                             |
| dulwich_log              | 73.5 ms                                                               | 53.4 ms: 1.38x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                              |
| django_template          | 53.3 ms                                                               | 39.1 ms: 1.37x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                                            |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                              |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                             |
| thrift                   | 1.26 ms                                                               | 972 us: 1.30x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.59 us: 1.28x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.29 us: 1.28x faster                                                             |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                              |
| logging_simple           | 9.78 us                                                               | 7.75 us: 1.26x faster                                                             |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                             |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                             |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                             |
| nqueens                  | 117 ms                                                                | 98.0 ms: 1.20x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.19x faster                                                            |
| regex_v8                 | 32.2 ms                                                               | 27.3 ms: 1.18x faster                                                             |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.17x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.17x faster                                                            |
| scimark_fft              | 500 ms                                                                | 428 ms: 1.17x faster                                                              |
| pprint_safe_repr         | 1.15 sec                                                              | 988 ms: 1.16x faster                                                              |
| fannkuch                 | 546 ms                                                                | 474 ms: 1.15x faster                                                              |
| meteor_contest           | 126 ms                                                                | 110 ms: 1.15x faster                                                              |
| regex_dna                | 257 ms                                                                | 225 ms: 1.14x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 61.3 ms: 1.14x faster                                                             |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.13x faster                                                             |
| sqlite_synth             | 4.12 us                                                               | 3.70 us: 1.11x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.08 ms: 1.08x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                             |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                                             |
| pidigits                 | 235 ms                                                                | 236 ms: 1.00x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.40 ms: 1.11x slower                                                             |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.92 ms: 1.67x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.83 ms: 1.69x slower                                                             |
| logging_silent           | 222 ns                                                                | 614 ns: 2.77x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.37x