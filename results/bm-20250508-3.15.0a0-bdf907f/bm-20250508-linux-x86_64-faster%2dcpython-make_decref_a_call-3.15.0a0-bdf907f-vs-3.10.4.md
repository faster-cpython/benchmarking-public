# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.379x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                          |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                        |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 631 ms: 2.80x faster                                                          |
| async_tree_none         | 728 ms                                                 | 275 ms: 2.65x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.63x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 520 ms: 1.95x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.49x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.5 ms: 1.62x faster                                                         |
| nbody          | 154 ms                                                 | 104 ms: 1.48x faster                                                          |
| pidigits       | 191 ms                                                 | 200 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.41x faster                                                          |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                         |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 230 us: 1.44x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 341 us: 1.42x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 63.7 ms: 1.24x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                          |
| json_dumps           | 14.2 ms                                                | 12.5 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.13x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 90.1 ms: 1.10x faster                                                         |
| json_loads           | 31.2 us                                                | 31.4 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                         |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                         |
| mako            | 16.3 ms                                                | 12.4 ms: 1.31x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 53.0 ms: 1.25x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 177 us: 3.08x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 631 ms: 2.80x faster                                                          |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                         |
| async_tree_none          | 728 ms                                                 | 275 ms: 2.65x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.63x faster                                                          |
| mdp                      | 2.85 sec                                               | 1.29 sec: 2.21x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.59 ms: 2.20x faster                                                         |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 520 ms: 1.95x faster                                                          |
| pylint                   | 551 ms                                                 | 288 ms: 1.91x faster                                                          |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                         |
| richards_super           | 94.7 ms                                                | 51.4 ms: 1.84x faster                                                         |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                          |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                          |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                          |
| richards                 | 79.3 ms                                                | 45.0 ms: 1.76x faster                                                         |
| deepcopy                 | 479 us                                                 | 276 us: 1.73x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 77.2 ms: 1.65x faster                                                         |
| djangocms                | 38.4 us                                                | 23.4 us: 1.64x faster                                                         |
| float                    | 117 ms                                                 | 72.5 ms: 1.62x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.9 us: 1.61x faster                                                         |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.58x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                         |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                        |
| nbody                    | 154 ms                                                 | 104 ms: 1.48x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 230 us: 1.44x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.79 us: 1.44x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.92 us: 1.43x faster                                                         |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 341 us: 1.42x faster                                                          |
| regex_compile            | 188 ms                                                 | 133 ms: 1.41x faster                                                          |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                         |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                          |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                                         |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 770 ms: 1.32x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                         |
| mako                     | 16.3 ms                                                | 12.4 ms: 1.31x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                        |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                          |
| thrift                   | 1.07 ms                                                | 832 us: 1.29x faster                                                          |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.12 ms: 1.26x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 53.0 ms: 1.25x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 63.7 ms: 1.24x faster                                                         |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                        |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                         |
| fannkuch                 | 532 ms                                                 | 441 ms: 1.21x faster                                                          |
| scimark_fft              | 466 ms                                                 | 388 ms: 1.20x faster                                                          |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                          |
| json_dumps               | 14.2 ms                                                | 12.5 ms: 1.14x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.13x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 90.1 ms: 1.10x faster                                                         |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 909 us: 1.09x faster                                                          |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                          |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                                         |
| json                     | 5.69 ms                                                | 5.53 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| json_loads               | 31.2 us                                                | 31.4 us: 1.01x slower                                                         |
| pidigits                 | 191 ms                                                 | 200 ms: 1.05x slower                                                          |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                                         |
| coverage                 | 79.4 ms                                                | 93.1 ms: 1.17x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                         |
| dask                     | 441 ms                                                 | 774 ms: 1.76x slower                                                          |
| bench_mp_pool            | 24.0 ms                                                | 95.1 ms: 3.96x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                  |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.379x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.30x