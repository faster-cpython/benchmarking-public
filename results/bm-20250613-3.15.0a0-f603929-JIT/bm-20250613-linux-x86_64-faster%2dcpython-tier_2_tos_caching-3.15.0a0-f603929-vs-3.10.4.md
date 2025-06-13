# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                          |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.94x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                          |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.9 ms: 1.78x faster                                                         |
| nbody          | 154 ms                                                 | 88.2 ms: 1.74x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                          |
| regex_v8       | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                         |
| regex_dna      | 227 ms                                                 | 196 ms: 1.16x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 203 us: 1.63x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                         |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                         |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.94x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                          |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                          |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                         |
| richards_super           | 94.7 ms                                                | 40.0 ms: 2.37x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                        |
| richards                 | 79.3 ms                                                | 35.0 ms: 2.26x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                         |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                          |
| go                       | 240 ms                                                 | 125 ms: 1.92x faster                                                          |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                          |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.85x faster                                                         |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                          |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                          |
| float                    | 117 ms                                                 | 65.9 ms: 1.78x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                         |
| nbody                    | 154 ms                                                 | 88.2 ms: 1.74x faster                                                         |
| pyflate                  | 716 ms                                                 | 425 ms: 1.68x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 76.5 ms: 1.67x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 203 us: 1.63x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                                         |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                         |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                          |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                         |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                                         |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                          |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                         |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.38x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 61.4 ms: 1.37x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                        |
| coroutines               | 35.1 ms                                                | 25.9 ms: 1.36x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.18 us: 1.34x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                                         |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                         |
| logging_format           | 9.09 us                                                | 6.88 us: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                                         |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                          |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                          |
| nqueens                  | 106 ms                                                 | 84.2 ms: 1.26x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.23 ms: 1.24x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 81.9 ms: 1.21x faster                                                         |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                          |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 850 ms: 1.20x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.78 sec: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                         |
| regex_dna                | 227 ms                                                 | 196 ms: 1.16x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                          |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                         |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                         |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                          |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.07 ms: 1.40x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                         |
| logging_silent           | 190 ns                                                 | 480 ns: 2.53x slower                                                          |
| coverage                 | 79.4 ms                                                | 424 ms: 5.34x slower                                                          |
| thrift                   | 1.07 ms                                                | 148 ms: 138.27x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                  |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.325x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.34x