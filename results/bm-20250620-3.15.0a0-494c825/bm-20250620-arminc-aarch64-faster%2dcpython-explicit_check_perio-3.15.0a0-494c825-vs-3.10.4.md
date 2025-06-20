# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.330x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                            |
| html5lib       | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 891 ms: 2.57x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                              |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.39x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 667 ms: 1.91x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.2 ms: 1.55x faster                                                             |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.43x faster                                                              |
| regex_dna      | 257 ms                                                                | 219 ms: 1.17x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 28.6 ms: 1.13x faster                                                             |
| regex_effbot   | 4.25 ms                                                               | 3.86 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| unpickle_pure_python | 366 us                                                                | 270 us: 1.35x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 412 us: 1.28x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                             |
| mako            | 18.9 ms                                                               | 14.4 ms: 1.31x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 63.8 ms: 1.10x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.31x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 891 ms: 2.57x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                              |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.39x faster                                                              |
| deltablue                | 8.94 ms                                                               | 4.07 ms: 2.20x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                            |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                                              |
| generators               | 68.1 ms                                                               | 35.1 ms: 1.94x faster                                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 667 ms: 1.91x faster                                                              |
| chaos                    | 121 ms                                                                | 70.9 ms: 1.71x faster                                                             |
| richards_super           | 107 ms                                                                | 62.9 ms: 1.71x faster                                                             |
| raytrace                 | 573 ms                                                                | 336 ms: 1.70x faster                                                              |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                              |
| richards                 | 91.7 ms                                                               | 54.8 ms: 1.67x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 83.3 ms: 1.61x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.99 ms: 1.56x faster                                                             |
| float                    | 135 ms                                                                | 87.2 ms: 1.55x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 40.0 us: 1.54x faster                                                             |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.53x faster                                                              |
| pylint                   | 485 ms                                                                | 318 ms: 1.52x faster                                                              |
| pyflate                  | 795 ms                                                                | 526 ms: 1.51x faster                                                              |
| deepcopy                 | 511 us                                                                | 341 us: 1.50x faster                                                              |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                              |
| regex_compile            | 177 ms                                                                | 124 ms: 1.43x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 62.2 ms: 1.39x faster                                                             |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                            |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.35x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 54.9 ms: 1.34x faster                                                             |
| django_template          | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                             |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.31x faster                                                             |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 412 us: 1.28x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                             |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                             |
| thrift                   | 1.26 ms                                                               | 1.01 ms: 1.25x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.70 us: 1.24x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.57 us: 1.24x faster                                                             |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.24x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.93 us: 1.23x faster                                                             |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 81.1 ms: 1.23x faster                                                             |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                            |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                                              |
| nqueens                  | 117 ms                                                                | 99.5 ms: 1.18x faster                                                             |
| regex_dna                | 257 ms                                                                | 219 ms: 1.17x faster                                                              |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.15x faster                                                              |
| sympy_expand             | 543 ms                                                                | 471 ms: 1.15x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 28.6 ms: 1.13x faster                                                             |
| fannkuch                 | 546 ms                                                                | 485 ms: 1.12x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 2.11 sec: 1.12x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.03 sec: 1.12x faster                                                            |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                              |
| regex_effbot             | 4.25 ms                                                               | 3.86 ms: 1.10x faster                                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                             |
| genshi_xml               | 69.8 ms                                                               | 63.8 ms: 1.10x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                              |
| json                     | 5.88 ms                                                               | 5.77 ms: 1.02x faster                                                             |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.50 ms: 1.12x slower                                                             |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                              |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.72 ms: 1.62x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.75 ms: 1.66x slower                                                             |
| logging_silent           | 222 ns                                                                | 643 ns: 2.89x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                                      |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.330x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.37x