# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-x86_64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 264 ms: 1.03x slower                                                          |
| docutils       | 2.60 sec                                                              | 2.67 sec: 1.03x slower                                                        |
| html5lib       | 61.8 ms                                                               | 63.0 ms: 1.02x slower                                                         |
| sphinx         | 1.02 sec                                                              | 1.05 sec: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg       | 486 ms                                                                | 497 ms: 1.02x slower                                                          |
| coroutines                       | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 457 ms                                                                | 468 ms: 1.02x slower                                                          |
| async_tree_eager_cpu_io_mixed    | 384 ms                                                                | 394 ms: 1.03x slower                                                          |
| async_tree_eager_io_tg           | 629 ms                                                                | 646 ms: 1.03x slower                                                          |
| async_tree_eager_io              | 620 ms                                                                | 639 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed          | 490 ms                                                                | 505 ms: 1.03x slower                                                          |
| async_tree_none_tg               | 248 ms                                                                | 256 ms: 1.03x slower                                                          |
| async_tree_memoization_tg        | 312 ms                                                                | 324 ms: 1.04x slower                                                          |
| async_tree_io                    | 593 ms                                                                | 615 ms: 1.04x slower                                                          |
| async_tree_eager_memoization     | 198 ms                                                                | 206 ms: 1.04x slower                                                          |
| async_tree_eager_tg              | 211 ms                                                                | 220 ms: 1.04x slower                                                          |
| async_tree_memoization           | 310 ms                                                                | 322 ms: 1.04x slower                                                          |
| async_tree_none                  | 258 ms                                                                | 269 ms: 1.04x slower                                                          |
| async_tree_eager_memoization_tg  | 274 ms                                                                | 287 ms: 1.05x slower                                                          |
| async_generators                 | 405 ms                                                                | 424 ms: 1.05x slower                                                          |
| async_tree_eager                 | 102 ms                                                                | 107 ms: 1.05x slower                                                          |
| Geometric mean                   | (ref)                                                                 | 1.03x slower                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 104 ms                                                                | 100 ms: 1.03x faster                                                          |
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                          |
| float          | 70.1 ms                                                               | 72.3 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.37 ms                                                               | 3.42 ms: 1.02x slower                                                         |
| regex_dna      | 214 ms                                                                | 217 ms: 1.02x slower                                                          |
| regex_compile  | 128 ms                                                                | 132 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.02 sec                                                              | 2.05 sec: 1.02x slower                                                        |
| json_dumps           | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                         |
| unpickle_pure_python | 218 us                                                                | 225 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 98.0 ms                                                               | 102 ms: 1.04x slower                                                          |
| xml_etree_parse      | 142 ms                                                                | 148 ms: 1.04x slower                                                          |
| json_loads           | 29.8 us                                                               | 31.5 us: 1.05x slower                                                         |
| pickle_pure_python   | 320 us                                                                | 337 us: 1.06x slower                                                          |
| xml_etree_generate   | 85.5 ms                                                               | 91.2 ms: 1.07x slower                                                         |
| xml_etree_process    | 59.3 ms                                                               | 64.1 ms: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.95 ms                                                               | 7.01 ms: 1.01x slower                                                         |
| python_startup         | 12.2 ms                                                               | 12.4 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.6 ms                                                               | 12.0 ms: 1.04x slower                                                         |
| genshi_xml      | 49.6 ms                                                               | 52.1 ms: 1.05x slower                                                         |
| django_template | 32.0 ms                                                               | 33.7 ms: 1.05x slower                                                         |
| genshi_text     | 21.2 ms                                                               | 23.1 ms: 1.09x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.06x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20250519-linux-x86_64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                           | 149 ms                                                                | 811 us: 183.80x faster                                                        |
| coverage                         | 422 ms                                                                | 93.3 ms: 4.52x faster                                                         |
| dask                             | 913 ms                                                                | 779 ms: 1.17x faster                                                          |
| nbody                            | 104 ms                                                                | 100 ms: 1.03x faster                                                          |
| shortest_path                    | 510 ms                                                                | 495 ms: 1.03x faster                                                          |
| connected_components             | 457 ms                                                                | 451 ms: 1.01x faster                                                          |
| create_gc_cycles                 | 2.58 ms                                                               | 2.58 ms: 1.00x faster                                                         |
| pidigits                         | 187 ms                                                                | 188 ms: 1.00x slower                                                          |
| dulwich_log                      | 59.4 ms                                                               | 59.8 ms: 1.01x slower                                                         |
| python_startup_no_site           | 6.95 ms                                                               | 7.01 ms: 1.01x slower                                                         |
| bench_mp_pool                    | 93.7 ms                                                               | 94.8 ms: 1.01x slower                                                         |
| python_startup                   | 12.2 ms                                                               | 12.4 ms: 1.01x slower                                                         |
| scimark_sor                      | 123 ms                                                                | 124 ms: 1.01x slower                                                          |
| raytrace                         | 272 ms                                                                | 275 ms: 1.01x slower                                                          |
| regex_effbot                     | 3.37 ms                                                               | 3.42 ms: 1.02x slower                                                         |
| tomli_loads                      | 2.02 sec                                                              | 2.05 sec: 1.02x slower                                                        |
| regex_dna                        | 214 ms                                                                | 217 ms: 1.02x slower                                                          |
| sqlite_synth                     | 2.86 us                                                               | 2.91 us: 1.02x slower                                                         |
| html5lib                         | 61.8 ms                                                               | 63.0 ms: 1.02x slower                                                         |
| sympy_integrate                  | 19.0 ms                                                               | 19.4 ms: 1.02x slower                                                         |
| json_dumps                       | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                         |
| hexiom                           | 6.28 ms                                                               | 6.42 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg       | 486 ms                                                                | 497 ms: 1.02x slower                                                          |
| coroutines                       | 24.7 ms                                                               | 25.3 ms: 1.02x slower                                                         |
| pycparser                        | 1.14 sec                                                              | 1.17 sec: 1.02x slower                                                        |
| scimark_monte_carlo              | 68.5 ms                                                               | 70.0 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 457 ms                                                                | 468 ms: 1.02x slower                                                          |
| bench_thread_pool                | 891 us                                                                | 913 us: 1.02x slower                                                          |
| gc_traversal                     | 4.96 ms                                                               | 5.08 ms: 1.02x slower                                                         |
| async_tree_eager_cpu_io_mixed    | 384 ms                                                                | 394 ms: 1.03x slower                                                          |
| go                               | 112 ms                                                                | 115 ms: 1.03x slower                                                          |
| scimark_fft                      | 375 ms                                                                | 385 ms: 1.03x slower                                                          |
| richards                         | 43.3 ms                                                               | 44.4 ms: 1.03x slower                                                         |
| many_optionals                   | 969 us                                                                | 995 us: 1.03x slower                                                          |
| deepcopy_memo                    | 29.6 us                                                               | 30.4 us: 1.03x slower                                                         |
| docutils                         | 2.60 sec                                                              | 2.67 sec: 1.03x slower                                                        |
| async_tree_eager_io_tg           | 629 ms                                                                | 646 ms: 1.03x slower                                                          |
| pathlib                          | 17.0 ms                                                               | 17.5 ms: 1.03x slower                                                         |
| sympy_sum                        | 148 ms                                                                | 152 ms: 1.03x slower                                                          |
| 2to3                             | 257 ms                                                                | 264 ms: 1.03x slower                                                          |
| sqlglot_v2_parse                 | 1.24 ms                                                               | 1.28 ms: 1.03x slower                                                         |
| typing_runtime_protocols         | 170 us                                                                | 175 us: 1.03x slower                                                          |
| sphinx                           | 1.02 sec                                                              | 1.05 sec: 1.03x slower                                                        |
| async_tree_eager_io              | 620 ms                                                                | 639 ms: 1.03x slower                                                          |
| unpickle_pure_python             | 218 us                                                                | 225 us: 1.03x slower                                                          |
| async_tree_cpu_io_mixed          | 490 ms                                                                | 505 ms: 1.03x slower                                                          |
| float                            | 70.1 ms                                                               | 72.3 ms: 1.03x slower                                                         |
| async_tree_none_tg               | 248 ms                                                                | 256 ms: 1.03x slower                                                          |
| regex_compile                    | 128 ms                                                                | 132 ms: 1.03x slower                                                          |
| sympy_str                        | 268 ms                                                                | 277 ms: 1.03x slower                                                          |
| chaos                            | 59.2 ms                                                               | 61.2 ms: 1.03x slower                                                         |
| sqlglot_v2_transpile             | 1.55 ms                                                               | 1.60 ms: 1.04x slower                                                         |
| scimark_lu                       | 116 ms                                                                | 121 ms: 1.04x slower                                                          |
| async_tree_memoization_tg        | 312 ms                                                                | 324 ms: 1.04x slower                                                          |
| meteor_contest                   | 108 ms                                                                | 112 ms: 1.04x slower                                                          |
| async_tree_io                    | 593 ms                                                                | 615 ms: 1.04x slower                                                          |
| mako                             | 11.6 ms                                                               | 12.0 ms: 1.04x slower                                                         |
| sympy_expand                     | 456 ms                                                                | 473 ms: 1.04x slower                                                          |
| async_tree_eager_memoization     | 198 ms                                                                | 206 ms: 1.04x slower                                                          |
| richards_super                   | 49.2 ms                                                               | 51.1 ms: 1.04x slower                                                         |
| async_tree_eager_tg              | 211 ms                                                                | 220 ms: 1.04x slower                                                          |
| async_tree_memoization           | 310 ms                                                                | 322 ms: 1.04x slower                                                          |
| deepcopy                         | 259 us                                                                | 270 us: 1.04x slower                                                          |
| sqlglot_v2_normalize             | 106 ms                                                                | 110 ms: 1.04x slower                                                          |
| sqlglot_v2_optimize              | 52.4 ms                                                               | 54.5 ms: 1.04x slower                                                         |
| async_tree_none                  | 258 ms                                                                | 269 ms: 1.04x slower                                                          |
| deltablue                        | 3.38 ms                                                               | 3.53 ms: 1.04x slower                                                         |
| deepcopy_reduce                  | 2.77 us                                                               | 2.89 us: 1.04x slower                                                         |
| subparsers                       | 23.7 ms                                                               | 24.8 ms: 1.04x slower                                                         |
| crypto_pyaes                     | 74.2 ms                                                               | 77.3 ms: 1.04x slower                                                         |
| xml_etree_iterparse              | 98.0 ms                                                               | 102 ms: 1.04x slower                                                          |
| mdp                              | 1.23 sec                                                              | 1.29 sec: 1.04x slower                                                        |
| xml_etree_parse                  | 142 ms                                                                | 148 ms: 1.04x slower                                                          |
| generators                       | 30.4 ms                                                               | 31.8 ms: 1.04x slower                                                         |
| telco                            | 8.07 ms                                                               | 8.43 ms: 1.05x slower                                                         |
| async_tree_eager_memoization_tg  | 274 ms                                                                | 287 ms: 1.05x slower                                                          |
| async_generators                 | 405 ms                                                                | 424 ms: 1.05x slower                                                          |
| json                             | 5.31 ms                                                               | 5.56 ms: 1.05x slower                                                         |
| genshi_xml                       | 49.6 ms                                                               | 52.1 ms: 1.05x slower                                                         |
| async_tree_eager                 | 102 ms                                                                | 107 ms: 1.05x slower                                                          |
| pprint_pformat                   | 1.48 sec                                                              | 1.56 sec: 1.05x slower                                                        |
| django_template                  | 32.0 ms                                                               | 33.7 ms: 1.05x slower                                                         |
| json_loads                       | 29.8 us                                                               | 31.5 us: 1.05x slower                                                         |
| logging_silent                   | 470 ns                                                                | 495 ns: 1.05x slower                                                          |
| pickle_pure_python               | 320 us                                                                | 337 us: 1.06x slower                                                          |
| pprint_safe_repr                 | 728 ms                                                                | 769 ms: 1.06x slower                                                          |
| bpe_tokeniser                    | 4.45 sec                                                              | 4.70 sec: 1.06x slower                                                        |
| comprehensions                   | 16.7 us                                                               | 17.7 us: 1.06x slower                                                         |
| nqueens                          | 81.8 ms                                                               | 87.0 ms: 1.06x slower                                                         |
| pyflate                          | 444 ms                                                                | 474 ms: 1.07x slower                                                          |
| xml_etree_generate               | 85.5 ms                                                               | 91.2 ms: 1.07x slower                                                         |
| logging_simple                   | 6.03 us                                                               | 6.47 us: 1.07x slower                                                         |
| logging_format                   | 6.68 us                                                               | 7.19 us: 1.08x slower                                                         |
| xml_etree_process                | 59.3 ms                                                               | 64.1 ms: 1.08x slower                                                         |
| fannkuch                         | 405 ms                                                                | 440 ms: 1.09x slower                                                          |
| genshi_text                      | 21.2 ms                                                               | 23.1 ms: 1.09x slower                                                         |
| Geometric mean                   | (ref)                                                                 | 1.04x faster                                                                  |

Benchmark hidden because not significant (7): asyncio_websockets, regex_v8, spectral_norm, k_core, scimark_sparse_mat_mult, async_tree_io_tg, pylint
Ignored benchmarks (1) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-linux-x86_64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: djangocms

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.99x