# Results vs. 3.10.4

- fork: mdboom
- ref: pyfloat_fromdouble
- machine: linux-x86_64
- commit hash: 9487962
- commit date: 2025-05-30
- overall geometric mean: 1.318x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                              |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                               |
| nbody          | 154 ms                                                 | 95.8 ms: 1.60x faster                                               |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                               |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                              |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.3 us: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| django_template | 48.2 ms                                                | 33.0 ms: 1.46x faster                                               |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                               |
| go                       | 240 ms                                                 | 110 ms: 2.19x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                               |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                               |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                               |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| comprehensions           | 28.8 us                                                | 15.9 us: 1.81x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.04 ms: 1.72x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                               |
| pyflate                  | 716 ms                                                 | 430 ms: 1.67x faster                                                |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                               |
| nbody                    | 154 ms                                                 | 95.8 ms: 1.60x faster                                               |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                               |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| django_template          | 48.2 ms                                                | 33.0 ms: 1.46x faster                                               |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                               |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                               |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 18.8 ms: 1.37x faster                                               |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| logging_simple           | 8.30 us                                                | 6.21 us: 1.34x faster                                               |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                               |
| logging_format           | 9.09 us                                                | 6.97 us: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                               |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.65 sec: 1.27x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 810 ms: 1.26x faster                                                |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                |
| scimark_fft              | 466 ms                                                 | 371 ms: 1.25x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.20 ms: 1.24x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                               |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                               |
| json_loads               | 31.2 us                                                | 29.3 us: 1.06x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                               |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                               |
| logging_silent           | 190 ns                                                 | 470 ns: 2.48x slower                                                |
| coverage                 | 79.4 ms                                                | 418 ms: 5.26x slower                                                |
| thrift                   | 1.07 ms                                                | 148 ms: 137.98x slower                                              |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                        |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250530-3.15.0a0-9487962/bm-20250530-linux-x86_64-mdboom-pyfloat_fromdouble-3.15.0a0-9487962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.318x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x