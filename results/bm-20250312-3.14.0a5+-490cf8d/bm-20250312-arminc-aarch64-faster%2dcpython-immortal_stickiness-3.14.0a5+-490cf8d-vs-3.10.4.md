# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: linux-aarch64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                                              |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 466 ms: 2.43x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 652 ms: 1.95x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| nbody          | 166 ms                                                                | 128 ms: 1.30x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                                             |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                             |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.15x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 386 us: 1.37x faster                                                              |
| unpickle_pure_python | 366 us                                                                | 269 us: 1.36x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 175 ms: 1.21x faster                                                              |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                             |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| json_loads           | 30.9 us                                                               | 34.9 us: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                             |
| python_startup_no_site | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                             |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.38x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                                              |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 466 ms: 2.43x faster                                                              |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 652 ms: 1.95x faster                                                              |
| go                       | 264 ms                                                                | 139 ms: 1.90x faster                                                              |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.90x faster                                                             |
| raytrace                 | 573 ms                                                                | 320 ms: 1.79x faster                                                              |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.79x faster                                                             |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                                             |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                              |
| richards                 | 91.7 ms                                                               | 54.4 ms: 1.69x faster                                                             |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 39.1 us: 1.58x faster                                                             |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                             |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                              |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                             |
| float                    | 135 ms                                                                | 87.5 ms: 1.54x faster                                                             |
| scimark_lu               | 227 ms                                                                | 148 ms: 1.53x faster                                                              |
| spectral_norm            | 186 ms                                                                | 122 ms: 1.53x faster                                                              |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 87.8 ms: 1.53x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 7.41 ms: 1.47x faster                                                             |
| dulwich_log              | 73.5 ms                                                               | 51.5 ms: 1.43x faster                                                             |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                              |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                             |
| pyflate                  | 795 ms                                                                | 577 ms: 1.38x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 386 us: 1.37x faster                                                              |
| unpickle_pure_python     | 366 us                                                                | 269 us: 1.36x faster                                                              |
| logging_format           | 10.6 us                                                               | 7.82 us: 1.36x faster                                                             |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.35x faster                                                            |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                              |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| html5lib                 | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                                            |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.5 ms: 1.32x faster                                                             |
| thrift                   | 1.26 ms                                                               | 955 us: 1.32x faster                                                              |
| nbody                    | 166 ms                                                                | 128 ms: 1.30x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                             |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                              |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                             |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                              |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                             |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.23x faster                                                             |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 950 ms: 1.21x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 175 ms: 1.21x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.95 sec: 1.20x faster                                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.48 ms: 1.18x faster                                                             |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                              |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 60.2 ms: 1.16x faster                                                             |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                                             |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                                             |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                              |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                            |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                                              |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                             |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                              |
| json                     | 5.88 ms                                                               | 5.83 ms: 1.01x faster                                                             |
| json_loads               | 30.9 us                                                               | 34.9 us: 1.13x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.60 ms: 1.13x slower                                                             |
| coverage                 | 83.6 ms                                                               | 97.3 ms: 1.16x slower                                                             |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 10.1 ms: 1.47x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.63 ms: 1.60x slower                                                             |
| bench_mp_pool            | 14.5 ms                                                               | 4.51 sec: 310.35x slower                                                          |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                                      |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, pidigits
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-arminc-aarch64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.30x