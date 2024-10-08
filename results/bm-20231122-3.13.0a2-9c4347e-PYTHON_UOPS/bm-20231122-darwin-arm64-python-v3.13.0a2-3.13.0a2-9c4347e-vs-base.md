# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x slower
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.46x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                                                               | 176 ms: 1.09x faster                                                                                             |
| chameleon      | 4.73 ms                                                                                              | 4.75 ms: 1.01x slower                                                                                            |
| docutils       | 1.46 sec                                                                                             | 1.45 sec: 1.00x faster                                                                                           |
| Geometric mean | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_io                    | 706 ms                                                                                               | 710 ms: 1.00x slower                                                                                             |
| async_tree_eager_cpu_io_mixed_tg | 344 ms                                                                                               | 346 ms: 1.01x slower                                                                                             |
| async_tree_io_tg                 | 690 ms                                                                                               | 695 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization     | 172 ms                                                                                               | 174 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                                                               | 143 ms: 1.01x slower                                                                                             |
| async_tree_none_tg               | 267 ms                                                                                               | 270 ms: 1.01x slower                                                                                             |
| Geometric mean                   | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (10): async_tree_eager, async_tree_eager_tg, async_tree_cpu_io_mixed, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_eager_io_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| nbody          | 70.8 ms                                                                                              | 71.5 ms: 1.01x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 74.9 ms                                                                                              | 74.6 ms: 1.00x faster                                                                                            |
| regex_v8       | 17.1 ms                                                                                              | 17.3 ms: 1.01x slower                                                                                            |
| regex_effbot   | 2.57 ms                                                                                              | 2.63 ms: 1.02x slower                                                                                            |
| regex_dna      | 152 ms                                                                                               | 158 ms: 1.04x slower                                                                                             |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| json_loads           | 17.2 us                                                                                              | 16.8 us: 1.03x faster                                                                                            |
| pickle_list          | 2.98 us                                                                                              | 2.94 us: 1.01x faster                                                                                            |
| json_dumps           | 6.61 ms                                                                                              | 6.54 ms: 1.01x faster                                                                                            |
| xml_etree_process    | 39.5 ms                                                                                              | 39.3 ms: 1.01x faster                                                                                            |
| pickle               | 7.39 us                                                                                              | 7.34 us: 1.01x faster                                                                                            |
| xml_etree_generate   | 56.2 ms                                                                                              | 56.0 ms: 1.00x faster                                                                                            |
| unpickle_pure_python | 155 us                                                                                               | 155 us: 1.00x slower                                                                                             |
| unpickle_list        | 2.98 us                                                                                              | 2.99 us: 1.01x slower                                                                                            |
| pickle_pure_python   | 198 us                                                                                               | 200 us: 1.01x slower                                                                                             |
| xml_etree_iterparse  | 71.3 ms                                                                                              | 76.3 ms: 1.07x slower                                                                                            |
| xml_etree_parse      | 99.9 ms                                                                                              | 109 ms: 1.09x slower                                                                                             |
| Geometric mean       | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (3): unpickle, pickle_dict, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                                                              | 16.6 ms: 1.19x slower                                                                                            |
| python_startup_no_site | 12.4 ms                                                                                              | 14.7 ms: 1.19x slower                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.19x slower                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mako           | 7.39 ms                                                                                              | 7.35 ms: 1.00x faster                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.00x faster                                                                                                     |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                        | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3                             | 192 ms                                                                                               | 176 ms: 1.09x faster                                                                                             |
| coroutines                       | 18.8 ms                                                                                              | 18.2 ms: 1.03x faster                                                                                            |
| json_loads                       | 17.2 us                                                                                              | 16.8 us: 1.03x faster                                                                                            |
| telco                            | 4.54 ms                                                                                              | 4.47 ms: 1.02x faster                                                                                            |
| pickle_list                      | 2.98 us                                                                                              | 2.94 us: 1.01x faster                                                                                            |
| json_dumps                       | 6.61 ms                                                                                              | 6.54 ms: 1.01x faster                                                                                            |
| bench_thread_pool                | 493 us                                                                                               | 488 us: 1.01x faster                                                                                             |
| comprehensions                   | 11.4 us                                                                                              | 11.3 us: 1.01x faster                                                                                            |
| sympy_integrate                  | 10.6 ms                                                                                              | 10.5 ms: 1.01x faster                                                                                            |
| logging_format                   | 3.84 us                                                                                              | 3.82 us: 1.01x faster                                                                                            |
| xml_etree_process                | 39.5 ms                                                                                              | 39.3 ms: 1.01x faster                                                                                            |
| nqueens                          | 58.4 ms                                                                                              | 58.1 ms: 1.01x faster                                                                                            |
| pickle                           | 7.39 us                                                                                              | 7.34 us: 1.01x faster                                                                                            |
| sympy_expand                     | 234 ms                                                                                               | 232 ms: 1.01x faster                                                                                             |
| pprint_pformat                   | 1.01 sec                                                                                             | 1.00 sec: 1.01x faster                                                                                           |
| mako                             | 7.39 ms                                                                                              | 7.35 ms: 1.00x faster                                                                                            |
| regex_compile                    | 74.9 ms                                                                                              | 74.6 ms: 1.00x faster                                                                                            |
| pprint_safe_repr                 | 496 ms                                                                                               | 495 ms: 1.00x faster                                                                                             |
| logging_simple                   | 3.54 us                                                                                              | 3.53 us: 1.00x faster                                                                                            |
| xml_etree_generate               | 56.2 ms                                                                                              | 56.0 ms: 1.00x faster                                                                                            |
| docutils                         | 1.46 sec                                                                                             | 1.45 sec: 1.00x faster                                                                                           |
| scimark_sor                      | 104 ms                                                                                               | 104 ms: 1.00x faster                                                                                             |
| sqlglot_optimize                 | 33.3 ms                                                                                              | 33.3 ms: 1.00x faster                                                                                            |
| chaos                            | 41.2 ms                                                                                              | 41.2 ms: 1.00x faster                                                                                            |
| meteor_contest                   | 73.0 ms                                                                                              | 72.9 ms: 1.00x faster                                                                                            |
| unpickle_pure_python             | 155 us                                                                                               | 155 us: 1.00x slower                                                                                             |
| create_gc_cycles                 | 703 us                                                                                               | 705 us: 1.00x slower                                                                                             |
| deltablue                        | 2.44 ms                                                                                              | 2.44 ms: 1.00x slower                                                                                            |
| fannkuch                         | 270 ms                                                                                               | 271 ms: 1.00x slower                                                                                             |
| richards_super                   | 38.0 ms                                                                                              | 38.2 ms: 1.00x slower                                                                                            |
| scimark_fft                      | 200 ms                                                                                               | 201 ms: 1.00x slower                                                                                             |
| async_tree_io                    | 706 ms                                                                                               | 710 ms: 1.00x slower                                                                                             |
| gc_traversal                     | 2.40 ms                                                                                              | 2.41 ms: 1.01x slower                                                                                            |
| raytrace                         | 178 ms                                                                                               | 179 ms: 1.01x slower                                                                                             |
| chameleon                        | 4.73 ms                                                                                              | 4.75 ms: 1.01x slower                                                                                            |
| async_tree_eager_cpu_io_mixed_tg | 344 ms                                                                                               | 346 ms: 1.01x slower                                                                                             |
| scimark_sparse_mat_mult          | 3.08 ms                                                                                              | 3.10 ms: 1.01x slower                                                                                            |
| unpickle_list                    | 2.98 us                                                                                              | 2.99 us: 1.01x slower                                                                                            |
| async_tree_io_tg                 | 690 ms                                                                                               | 695 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization     | 172 ms                                                                                               | 174 ms: 1.01x slower                                                                                             |
| async_tree_eager_memoization_tg  | 142 ms                                                                                               | 143 ms: 1.01x slower                                                                                             |
| logging_silent                   | 69.9 ns                                                                                              | 70.6 ns: 1.01x slower                                                                                            |
| pickle_pure_python               | 198 us                                                                                               | 200 us: 1.01x slower                                                                                             |
| nbody                            | 70.8 ms                                                                                              | 71.5 ms: 1.01x slower                                                                                            |
| richards                         | 33.9 ms                                                                                              | 34.3 ms: 1.01x slower                                                                                            |
| regex_v8                         | 17.1 ms                                                                                              | 17.3 ms: 1.01x slower                                                                                            |
| async_tree_none_tg               | 267 ms                                                                                               | 270 ms: 1.01x slower                                                                                             |
| sqlite_synth                     | 1.58 us                                                                                              | 1.60 us: 1.01x slower                                                                                            |
| deepcopy                         | 218 us                                                                                               | 221 us: 1.01x slower                                                                                             |
| async_generators                 | 294 ms                                                                                               | 299 ms: 1.01x slower                                                                                             |
| deepcopy_memo                    | 24.8 us                                                                                              | 25.3 us: 1.02x slower                                                                                            |
| regex_effbot                     | 2.57 ms                                                                                              | 2.63 ms: 1.02x slower                                                                                            |
| regex_dna                        | 152 ms                                                                                               | 158 ms: 1.04x slower                                                                                             |
| flaskblogging                    | 3.89 ms                                                                                              | 4.11 ms: 1.06x slower                                                                                            |
| pathlib                          | 24.4 ms                                                                                              | 26.0 ms: 1.07x slower                                                                                            |
| xml_etree_iterparse              | 71.3 ms                                                                                              | 76.3 ms: 1.07x slower                                                                                            |
| bench_mp_pool                    | 44.7 ms                                                                                              | 48.1 ms: 1.08x slower                                                                                            |
| xml_etree_parse                  | 99.9 ms                                                                                              | 109 ms: 1.09x slower                                                                                             |
| python_startup                   | 13.9 ms                                                                                              | 16.6 ms: 1.19x slower                                                                                            |
| python_startup_no_site           | 12.4 ms                                                                                              | 14.7 ms: 1.19x slower                                                                                            |
| Geometric mean                   | (ref)                                                                                                | 1.01x slower                                                                                                     |

Benchmark hidden because not significant (48): asyncio_tcp, unpickle, typing_runtime_protocols, pycparser, sympy_str, asyncio_tcp_ssl, pickle_dict, json, sqlglot_parse, go, async_tree_eager, crypto_pyaes, hexiom, pidigits, genshi_xml, generators, async_tree_eager_tg, dulwich_log, asyncio_websockets, django_template, scimark_monte_carlo, tomli_loads, sqlglot_transpile, genshi_text, deepcopy_reduce, coverage, sympy_sum, pyflate, thrift, spectral_norm, scimark_lu, mdp, float, sqlglot_normalize, async_tree_cpu_io_mixed, html5lib, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_eager_io_tg, async_tree_memoization_tg, aiohttp, mypy2, pylint, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.46x