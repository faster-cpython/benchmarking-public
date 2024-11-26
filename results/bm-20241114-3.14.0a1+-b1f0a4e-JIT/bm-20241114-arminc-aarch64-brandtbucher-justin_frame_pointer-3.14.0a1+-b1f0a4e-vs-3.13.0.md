# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.138x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 413 ms: 1.36x slower                                                           |
| docutils       | 2.89 sec                                                 | 3.83 sec: 1.32x slower                                                         |
| html5lib       | 66.4 ms                                                  | 76.4 ms: 1.15x slower                                                          |
| sphinx         | 1.17 sec                                                 | 1.58 sec: 1.35x slower                                                         |
| Geometric mean | (ref)                                                    | 1.29x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 568 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 809 ms: 1.06x slower                                                           |
| async_tree_io             | 1.11 sec                                                 | 1.22 sec: 1.10x slower                                                         |
| async_generators          | 489 ms                                                   | 552 ms: 1.13x slower                                                           |
| async_tree_io_tg          | 1.13 sec                                                 | 1.30 sec: 1.15x slower                                                         |
| Geometric mean            | (ref)                                                    | 1.03x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 243 ms: 1.04x slower                                                           |
| float          | 93.3 ms                                                  | 108 ms: 1.16x slower                                                           |
| nbody          | 114 ms                                                   | 133 ms: 1.17x slower                                                           |
| Geometric mean | (ref)                                                    | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 33.4 ms: 1.05x slower                                                          |
| regex_dna      | 253 ms                                                   | 277 ms: 1.09x slower                                                           |
| regex_effbot   | 4.89 ms                                                  | 5.38 ms: 1.10x slower                                                          |
| regex_compile  | 127 ms                                                   | 186 ms: 1.47x slower                                                           |
| Geometric mean | (ref)                                                    | 1.17x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                   | 155 ms: 1.04x slower                                                           |
| xml_etree_generate   | 113 ms                                                   | 119 ms: 1.05x slower                                                           |
| xml_etree_process    | 80.5 ms                                                  | 86.1 ms: 1.07x slower                                                          |
| json_dumps           | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                          |
| tomli_loads          | 2.54 sec                                                 | 2.82 sec: 1.11x slower                                                         |
| unpickle_pure_python | 251 us                                                   | 292 us: 1.17x slower                                                           |
| pickle_pure_python   | 357 us                                                   | 432 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                    | 1.08x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.16 ms: 1.05x slower                                                          |
| python_startup         | 15.4 ms                                                  | 16.4 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                    | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 14.2 ms: 1.06x slower                                                          |
| django_template | 41.6 ms                                                  | 49.8 ms: 1.20x slower                                                          |
| genshi_text     | 27.7 ms                                                  | 36.6 ms: 1.32x slower                                                          |
| genshi_xml      | 60.3 ms                                                  | 84.5 ms: 1.40x slower                                                          |
| Geometric mean  | (ref)                                                    | 1.24x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 568 ms: 1.14x faster                                                           |
| deepcopy_memo             | 50.4 us                                                  | 46.4 us: 1.09x faster                                                          |
| deepcopy_reduce           | 4.07 us                                                  | 4.21 us: 1.03x slower                                                          |
| xml_etree_iterparse       | 149 ms                                                   | 155 ms: 1.04x slower                                                           |
| pidigits                  | 234 ms                                                   | 243 ms: 1.04x slower                                                           |
| xml_etree_generate        | 113 ms                                                   | 119 ms: 1.05x slower                                                           |
| telco                     | 9.74 ms                                                  | 10.2 ms: 1.05x slower                                                          |
| python_startup_no_site    | 8.73 ms                                                  | 9.16 ms: 1.05x slower                                                          |
| regex_v8                  | 31.8 ms                                                  | 33.4 ms: 1.05x slower                                                          |
| shortest_path             | 565 ms                                                   | 594 ms: 1.05x slower                                                           |
| bpe_tokeniser             | 5.87 sec                                                 | 6.20 sec: 1.06x slower                                                         |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 809 ms: 1.06x slower                                                           |
| thrift                    | 968 us                                                   | 1.03 ms: 1.06x slower                                                          |
| python_startup            | 15.4 ms                                                  | 16.4 ms: 1.06x slower                                                          |
| mako                      | 13.4 ms                                                  | 14.2 ms: 1.06x slower                                                          |
| xml_etree_process         | 80.5 ms                                                  | 86.1 ms: 1.07x slower                                                          |
| connected_components      | 533 ms                                                   | 571 ms: 1.07x slower                                                           |
| scimark_fft               | 447 ms                                                   | 483 ms: 1.08x slower                                                           |
| bench_thread_pool         | 1.27 ms                                                  | 1.39 ms: 1.09x slower                                                          |
| json_dumps                | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                          |
| regex_dna                 | 253 ms                                                   | 277 ms: 1.09x slower                                                           |
| async_tree_io             | 1.11 sec                                                 | 1.22 sec: 1.10x slower                                                         |
| scimark_sor               | 160 ms                                                   | 176 ms: 1.10x slower                                                           |
| regex_effbot              | 4.89 ms                                                  | 5.38 ms: 1.10x slower                                                          |
| logging_format            | 7.82 us                                                  | 8.67 us: 1.11x slower                                                          |
| tomli_loads               | 2.54 sec                                                 | 2.82 sec: 1.11x slower                                                         |
| mdp                       | 3.34 sec                                                 | 3.71 sec: 1.11x slower                                                         |
| create_gc_cycles          | 3.35 ms                                                  | 3.75 ms: 1.12x slower                                                          |
| gc_traversal              | 5.77 ms                                                  | 6.50 ms: 1.13x slower                                                          |
| async_generators          | 489 ms                                                   | 552 ms: 1.13x slower                                                           |
| crypto_pyaes              | 83.7 ms                                                  | 95.3 ms: 1.14x slower                                                          |
| fannkuch                  | 461 ms                                                   | 528 ms: 1.15x slower                                                           |
| logging_simple            | 7.07 us                                                  | 8.11 us: 1.15x slower                                                          |
| async_tree_io_tg          | 1.13 sec                                                 | 1.30 sec: 1.15x slower                                                         |
| html5lib                  | 66.4 ms                                                  | 76.4 ms: 1.15x slower                                                          |
| float                     | 93.3 ms                                                  | 108 ms: 1.16x slower                                                           |
| scimark_lu                | 139 ms                                                   | 161 ms: 1.16x slower                                                           |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.54 ms: 1.16x slower                                                          |
| nbody                     | 114 ms                                                   | 133 ms: 1.17x slower                                                           |
| unpickle_pure_python      | 251 us                                                   | 292 us: 1.17x slower                                                           |
| meteor_contest            | 114 ms                                                   | 133 ms: 1.17x slower                                                           |
| scimark_monte_carlo       | 83.6 ms                                                  | 98.2 ms: 1.18x slower                                                          |
| spectral_norm             | 143 ms                                                   | 169 ms: 1.19x slower                                                           |
| django_template           | 41.6 ms                                                  | 49.8 ms: 1.20x slower                                                          |
| typing_runtime_protocols  | 193 us                                                   | 233 us: 1.21x slower                                                           |
| pickle_pure_python        | 357 us                                                   | 432 us: 1.21x slower                                                           |
| pyflate                   | 556 ms                                                   | 678 ms: 1.22x slower                                                           |
| sqlalchemy_imperative     | 15.1 ms                                                  | 18.5 ms: 1.22x slower                                                          |
| go                        | 160 ms                                                   | 197 ms: 1.23x slower                                                           |
| pycparser                 | 1.27 sec                                                 | 1.60 sec: 1.26x slower                                                         |
| logging_silent            | 133 ns                                                   | 169 ns: 1.27x slower                                                           |
| sqlglot_parse             | 1.38 ms                                                  | 1.80 ms: 1.30x slower                                                          |
| pylint                    | 342 ms                                                   | 451 ms: 1.32x slower                                                           |
| genshi_text               | 27.7 ms                                                  | 36.6 ms: 1.32x slower                                                          |
| docutils                  | 2.89 sec                                                 | 3.83 sec: 1.32x slower                                                         |
| chaos                     | 68.0 ms                                                  | 90.0 ms: 1.32x slower                                                          |
| sqlalchemy_declarative    | 150 ms                                                   | 200 ms: 1.33x slower                                                           |
| raytrace                  | 300 ms                                                   | 402 ms: 1.34x slower                                                           |
| pprint_safe_repr          | 926 ms                                                   | 1.25 sec: 1.35x slower                                                         |
| sqlglot_normalize         | 127 ms                                                   | 171 ms: 1.35x slower                                                           |
| sphinx                    | 1.17 sec                                                 | 1.58 sec: 1.35x slower                                                         |
| sympy_expand              | 457 ms                                                   | 619 ms: 1.36x slower                                                           |
| sqlglot_transpile         | 1.73 ms                                                  | 2.35 ms: 1.36x slower                                                          |
| 2to3                      | 304 ms                                                   | 413 ms: 1.36x slower                                                           |
| richards                  | 53.6 ms                                                  | 73.5 ms: 1.37x slower                                                          |
| comprehensions            | 20.4 us                                                  | 28.2 us: 1.38x slower                                                          |
| richards_super            | 60.1 ms                                                  | 83.2 ms: 1.38x slower                                                          |
| deltablue                 | 3.82 ms                                                  | 5.31 ms: 1.39x slower                                                          |
| nqueens                   | 100 ms                                                   | 139 ms: 1.39x slower                                                           |
| pprint_pformat            | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                         |
| genshi_xml                | 60.3 ms                                                  | 84.5 ms: 1.40x slower                                                          |
| sympy_str                 | 264 ms                                                   | 370 ms: 1.40x slower                                                           |
| sqlglot_optimize          | 62.2 ms                                                  | 88.4 ms: 1.42x slower                                                          |
| sympy_integrate           | 20.8 ms                                                  | 30.0 ms: 1.44x slower                                                          |
| regex_compile             | 127 ms                                                   | 186 ms: 1.47x slower                                                           |
| sympy_sum                 | 144 ms                                                   | 216 ms: 1.51x slower                                                           |
| hexiom                    | 7.11 ms                                                  | 11.1 ms: 1.57x slower                                                          |
| k_core                    | 2.96 sec                                                 | 4.65 sec: 1.57x slower                                                         |
| generators                | 37.6 ms                                                  | 59.5 ms: 1.58x slower                                                          |
| bench_mp_pool             | 7.68 ms                                                  | 1.60 sec: 207.68x slower                                                       |
| Geometric mean            | (ref)                                                    | 1.24x slower                                                                   |

Benchmark hidden because not significant (12): deepcopy, async_tree_memoization, async_tree_none, xml_etree_parse, async_tree_none_tg, coverage, async_tree_cpu_io_mixed_tg, asyncio_websockets, pathlib, json_loads, json, coroutines
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.138x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.08x