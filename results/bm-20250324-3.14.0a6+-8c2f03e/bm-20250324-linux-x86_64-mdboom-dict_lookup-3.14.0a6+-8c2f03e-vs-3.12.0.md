# Results vs. 3.12.0

- fork: mdboom
- ref: dict_lookup
- machine: linux-x86_64
- commit hash: 8c2f03e
- commit date: 2025-03-24
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                          |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                          |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                          |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                         |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                         |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                         |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                          |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                          |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                         |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                         |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                          |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                          |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                         |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                         |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                          |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                         |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                          |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                         |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                        |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                         |
| dulwich_log                | 68.5 ms                                                | 59.0 ms: 1.16x faster                                         |
| spectral_norm              | 115 ms                                                 | 99.4 ms: 1.15x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                         |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                         |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                          |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                         |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                         |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                         |
| scimark_fft                | 382 ms                                                 | 354 ms: 1.08x faster                                          |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                          |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 76.7 ms: 1.07x faster                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                          |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                          |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                        |
| logging_silent             | 104 ns                                                 | 98.4 ns: 1.06x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                          |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                         |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                        |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                          |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                         |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                         |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                          |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                          |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                         |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                          |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                         |
| nqueens                    | 83.3 ms                                                | 85.3 ms: 1.02x slower                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                         |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                          |
| fannkuch                   | 417 ms                                                 | 434 ms: 1.04x slower                                          |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                          |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                         |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                         |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                         |
| coverage                   | 72.7 ms                                                | 93.5 ms: 1.29x slower                                         |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                         |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (1): scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250324-3.14.0a6+-8c2f03e/bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x