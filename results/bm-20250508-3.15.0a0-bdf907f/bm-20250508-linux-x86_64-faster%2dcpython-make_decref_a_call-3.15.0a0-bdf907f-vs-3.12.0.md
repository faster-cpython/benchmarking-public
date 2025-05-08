# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.062x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                                          |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 644 ms: 1.84x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 322 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                          |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.72x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 505 ms: 1.44x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 520 ms: 1.40x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.68x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                         |
| pidigits       | 187 ms                                                 | 200 ms: 1.07x slower                                                          |
| nbody          | 97.0 ms                                                | 104 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                         |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                          |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads         | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                        |
| xml_etree_parse     | 159 ms                                                 | 147 ms: 1.08x faster                                                          |
| xml_etree_iterparse | 107 ms                                                 | 103 ms: 1.04x faster                                                          |
| xml_etree_generate  | 89.2 ms                                                | 90.1 ms: 1.01x slower                                                         |
| xml_etree_process   | 61.7 ms                                                | 63.7 ms: 1.03x slower                                                         |
| pickle_pure_python  | 324 us                                                 | 341 us: 1.05x slower                                                          |
| json_loads          | 28.5 us                                                | 31.4 us: 1.10x slower                                                         |
| json_dumps          | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                         |
| Geometric mean      | (ref)                                                  | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                         |
| mako            | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.29 sec: 2.05x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 644 ms: 1.84x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 322 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                          |
| async_tree_none            | 472 ms                                                 | 275 ms: 1.72x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 505 ms: 1.44x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 520 ms: 1.40x faster                                                          |
| deepcopy                   | 371 us                                                 | 276 us: 1.34x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.9 us: 1.22x faster                                                         |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                          |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.92 us: 1.14x faster                                                         |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                        |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.79 us: 1.12x faster                                                         |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                                          |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                         |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                         |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 69.8 ms: 1.08x faster                                                         |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.08x faster                                                          |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 77.2 ms: 1.06x faster                                                         |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                          |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.59 ms: 1.03x faster                                                         |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                        |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                          |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                          |
| richards                   | 45.8 ms                                                | 45.0 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 770 ms: 1.01x faster                                                          |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                          |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                          |
| django_template            | 34.6 ms                                                | 34.9 ms: 1.01x slower                                                         |
| xml_etree_generate         | 89.2 ms                                                | 90.1 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.12 ms: 1.01x slower                                                         |
| scimark_fft                | 382 ms                                                 | 388 ms: 1.01x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                        |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                         |
| xml_etree_process          | 61.7 ms                                                | 63.7 ms: 1.03x slower                                                         |
| nqueens                    | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                         |
| mako                       | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                         |
| json                       | 5.26 ms                                                | 5.53 ms: 1.05x slower                                                         |
| pickle_pure_python         | 324 us                                                 | 341 us: 1.05x slower                                                          |
| fannkuch                   | 417 ms                                                 | 441 ms: 1.06x slower                                                          |
| pidigits                   | 187 ms                                                 | 200 ms: 1.07x slower                                                          |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                          |
| nbody                      | 97.0 ms                                                | 104 ms: 1.07x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 909 us: 1.08x slower                                                          |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                         |
| json_loads                 | 28.5 us                                                | 31.4 us: 1.10x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 177 us: 1.12x slower                                                          |
| telco                      | 7.10 ms                                                | 8.45 ms: 1.19x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                         |
| coverage                   | 72.7 ms                                                | 93.1 ms: 1.28x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.4 ms: 1.30x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                         |
| dask                       | 372 ms                                                 | 774 ms: 2.08x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 95.1 ms: 3.96x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (5): meteor_contest, richards_super, unpickle_pure_python, pprint_pformat, asyncio_websockets
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (25) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x