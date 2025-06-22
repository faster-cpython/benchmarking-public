# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                            |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                           |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.75x faster                                                            |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 510 ms: 1.99x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 74.3 ms: 1.58x faster                                                           |
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| regex_v8       | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                           |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                           |
| mako            | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.75x faster                                                            |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                            |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                           |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.22x faster                                                           |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 510 ms: 1.99x faster                                                            |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                                           |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                           |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                            |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                                           |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                            |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                           |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 76.4 ms: 1.67x faster                                                           |
| pyflate                  | 716 ms                                                 | 431 ms: 1.66x faster                                                            |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.37 ms: 1.63x faster                                                           |
| float                    | 117 ms                                                 | 74.3 ms: 1.58x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                          |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.51x faster                                                           |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                            |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                            |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                           |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                                           |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                           |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                            |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                          |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                            |
| logging_simple           | 8.30 us                                                | 6.33 us: 1.31x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                           |
| logging_format           | 9.09 us                                                | 7.02 us: 1.30x faster                                                           |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 51.2 ms: 1.29x faster                                                           |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                            |
| fannkuch                 | 532 ms                                                 | 417 ms: 1.28x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 815 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.37 ms: 1.20x faster                                                           |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 23.5 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.33 ms: 1.09x faster                                                           |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                                           |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                           |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                            |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                            |
| coverage                 | 79.4 ms                                                | 87.7 ms: 1.10x slower                                                           |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                           |
| logging_silent           | 190 ns                                                 | 481 ns: 2.53x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x