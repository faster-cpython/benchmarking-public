# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-x86_64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                             |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                             |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| nbody          | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                            |
| regex_dna      | 212 ms                                                 | 224 ms: 1.05x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 100.0 ms: 1.07x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.07x faster                                                             |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                             |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                            |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                            |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                            |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 632 ms: 1.87x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                             |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.74x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.48x faster                                                             |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                                            |
| go                         | 139 ms                                                 | 114 ms: 1.23x faster                                                             |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                                            |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                            |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                            |
| async_generators           | 463 ms                                                 | 396 ms: 1.17x faster                                                             |
| spectral_norm              | 115 ms                                                 | 98.8 ms: 1.16x faster                                                            |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.14x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                             |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                            |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                             |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                            |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                            |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                                             |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                             |
| scimark_fft                | 382 ms                                                 | 347 ms: 1.10x faster                                                             |
| logging_silent             | 104 ns                                                 | 95.0 ns: 1.10x faster                                                            |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                            |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 100.0 ms: 1.07x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.07x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                            |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                             |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.3 ms: 1.05x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                             |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                                            |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                             |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                            |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                             |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                             |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                           |
| nbody                      | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.04x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.19 ms: 1.04x slower                                                            |
| coroutines                 | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                            |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                            |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.05x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                            |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                            |
| coverage                   | 72.7 ms                                                | 92.5 ms: 1.27x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.87 ms: 1.28x slower                                                            |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x