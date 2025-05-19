# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.066x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                          |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 324 ms: 1.77x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                          |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| nbody          | 97.0 ms                                                | 100 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.13x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                         |
| regex_dna      | 212 ms                                                 | 217 ms: 1.03x slower                                                          |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.05 sec: 1.13x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 225 us: 1.02x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 91.2 ms: 1.02x slower                                                         |
| xml_etree_process    | 61.7 ms                                                | 64.1 ms: 1.04x slower                                                         |
| pickle_pure_python   | 324 us                                                 | 337 us: 1.04x slower                                                          |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                         |
| json_loads           | 28.5 us                                                | 31.5 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| mako            | 11.9 ms                                                | 12.0 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.29 sec: 2.04x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 324 ms: 1.77x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                          |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                          |
| deepcopy                   | 371 us                                                 | 270 us: 1.38x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                                         |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                          |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.89 us: 1.16x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.05 sec: 1.13x faster                                                        |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                          |
| regex_compile              | 148 ms                                                 | 132 ms: 1.13x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                          |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.10x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                         |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                                         |
| async_generators           | 463 ms                                                 | 424 ms: 1.09x faster                                                          |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 70.0 ms: 1.07x faster                                                         |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 77.3 ms: 1.06x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.53 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                          |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                          |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                        |
| richards                   | 45.8 ms                                                | 44.4 ms: 1.03x faster                                                         |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 225 us: 1.02x faster                                                          |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                          |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 769 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                                        |
| richards_super             | 51.5 ms                                                | 51.1 ms: 1.01x faster                                                         |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.00x faster                                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                          |
| scimark_fft                | 382 ms                                                 | 385 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                         |
| mako                       | 11.9 ms                                                | 12.0 ms: 1.01x slower                                                         |
| generators                 | 31.2 ms                                                | 31.8 ms: 1.02x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 121 ms: 1.02x slower                                                          |
| xml_etree_generate         | 89.2 ms                                                | 91.2 ms: 1.02x slower                                                         |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.03x slower                                                          |
| sqlite_synth               | 2.83 us                                                | 2.91 us: 1.03x slower                                                         |
| nbody                      | 97.0 ms                                                | 100 ms: 1.04x slower                                                          |
| xml_etree_process          | 61.7 ms                                                | 64.1 ms: 1.04x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 337 us: 1.04x slower                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.27 ms: 1.04x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.0 ms: 1.05x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                         |
| fannkuch                   | 417 ms                                                 | 440 ms: 1.06x slower                                                          |
| json                       | 5.26 ms                                                | 5.56 ms: 1.06x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 913 us: 1.08x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                         |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                                         |
| json_loads                 | 28.5 us                                                | 31.5 us: 1.10x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 175 us: 1.11x slower                                                          |
| telco                      | 7.10 ms                                                | 8.43 ms: 1.19x slower                                                         |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                         |
| dask                       | 372 ms                                                 | 779 ms: 2.09x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 94.8 ms: 3.95x slower                                                         |
| logging_silent             | 104 ns                                                 | 495 ns: 4.74x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (5): pycparser, logging_format, asyncio_websockets, hexiom, logging_simple
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x