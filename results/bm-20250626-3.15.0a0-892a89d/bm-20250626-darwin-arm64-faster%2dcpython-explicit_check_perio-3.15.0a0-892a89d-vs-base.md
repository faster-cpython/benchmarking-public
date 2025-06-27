# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.005x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| docutils       | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none               | 182 ms                                                                | 179 ms: 1.01x faster                                                            |
| async_tree_eager_memoization  | 151 ms                                                                | 149 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 367 ms: 1.00x faster                                                            |
| async_tree_cpu_io_mixed       | 432 ms                                                                | 433 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 424 ms: 1.00x slower                                                            |
| async_tree_memoization        | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| async_tree_memoization_tg     | 206 ms                                                                | 209 ms: 1.01x slower                                                            |
| async_tree_io_tg              | 405 ms                                                                | 413 ms: 1.02x slower                                                            |
| async_tree_eager              | 72.8 ms                                                               | 76.5 ms: 1.05x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (10): async_tree_eager_tg, async_tree_io, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, coroutines, async_generators, asyncio_websockets, async_tree_none_tg, async_tree_eager_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 58.2 ms                                                               | 57.2 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 81.0 ms                                                               | 81.4 ms: 1.00x slower                                                           |
| regex_dna      | 143 ms                                                                | 145 ms: 1.01x slower                                                            |
| regex_effbot   | 2.36 ms                                                               | 2.42 ms: 1.03x slower                                                           |
| regex_v8       | 16.1 ms                                                               | 16.6 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.45 sec                                                              | 1.43 sec: 1.01x faster                                                          |
| json_loads           | 16.5 us                                                               | 16.5 us: 1.00x slower                                                           |
| xml_etree_process    | 43.2 ms                                                               | 43.5 ms: 1.01x slower                                                           |
| xml_etree_generate   | 58.4 ms                                                               | 59.0 ms: 1.01x slower                                                           |
| unpickle_pure_python | 177 us                                                                | 180 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.5 ms                                                               | 17.7 ms: 1.08x slower                                                           |
| python_startup_no_site | 12.2 ms                                                               | 13.3 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 36.2 ms                                                               | 36.6 ms: 1.01x slower                                                           |
| django_template | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                           |
| genshi_text     | 17.7 ms                                                               | 18.2 ms: 1.03x slower                                                           |
| mako            | 9.03 ms                                                               | 9.33 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| sqlglot_v2_parse              | 986 us                                                                | 944 us: 1.04x faster                                                            |
| sqlglot_v2_transpile          | 1.16 ms                                                               | 1.12 ms: 1.04x faster                                                           |
| deltablue                     | 2.82 ms                                                               | 2.73 ms: 1.03x faster                                                           |
| typing_runtime_protocols      | 109 us                                                                | 106 us: 1.03x faster                                                            |
| fannkuch                      | 303 ms                                                                | 296 ms: 1.03x faster                                                            |
| float                         | 58.2 ms                                                               | 57.2 ms: 1.02x faster                                                           |
| chaos                         | 46.9 ms                                                               | 46.1 ms: 1.02x faster                                                           |
| async_tree_none               | 182 ms                                                                | 179 ms: 1.01x faster                                                            |
| tomli_loads                   | 1.45 sec                                                              | 1.43 sec: 1.01x faster                                                          |
| telco                         | 4.79 ms                                                               | 4.73 ms: 1.01x faster                                                           |
| generators                    | 31.8 ms                                                               | 31.5 ms: 1.01x faster                                                           |
| async_tree_eager_memoization  | 151 ms                                                                | 149 ms: 1.01x faster                                                            |
| sqlglot_v2_normalize          | 76.4 ms                                                               | 75.9 ms: 1.01x faster                                                           |
| create_gc_cycles              | 1.36 ms                                                               | 1.36 ms: 1.00x faster                                                           |
| coverage                      | 49.4 ms                                                               | 49.1 ms: 1.00x faster                                                           |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 367 ms: 1.00x faster                                                            |
| raytrace                      | 212 ms                                                                | 211 ms: 1.00x faster                                                            |
| 2to3                          | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed       | 432 ms                                                                | 433 ms: 1.00x slower                                                            |
| connected_components          | 304 ms                                                                | 305 ms: 1.00x slower                                                            |
| spectral_norm                 | 72.3 ms                                                               | 72.5 ms: 1.00x slower                                                           |
| json_loads                    | 16.5 us                                                               | 16.5 us: 1.00x slower                                                           |
| regex_compile                 | 81.0 ms                                                               | 81.4 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 424 ms: 1.00x slower                                                            |
| sympy_str                     | 154 ms                                                                | 155 ms: 1.01x slower                                                            |
| sympy_expand                  | 262 ms                                                                | 263 ms: 1.01x slower                                                            |
| go                            | 99.2 ms                                                               | 99.7 ms: 1.01x slower                                                           |
| crypto_pyaes                  | 60.9 ms                                                               | 61.3 ms: 1.01x slower                                                           |
| xml_etree_process             | 43.2 ms                                                               | 43.5 ms: 1.01x slower                                                           |
| deepcopy_reduce               | 1.90 us                                                               | 1.91 us: 1.01x slower                                                           |
| thrift                        | 469 us                                                                | 472 us: 1.01x slower                                                            |
| async_tree_memoization        | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| scimark_fft                   | 202 ms                                                                | 203 ms: 1.01x slower                                                            |
| pprint_pformat                | 1.27 sec                                                              | 1.28 sec: 1.01x slower                                                          |
| pprint_safe_repr              | 623 ms                                                                | 629 ms: 1.01x slower                                                            |
| scimark_monte_carlo           | 52.6 ms                                                               | 53.1 ms: 1.01x slower                                                           |
| xml_etree_generate            | 58.4 ms                                                               | 59.0 ms: 1.01x slower                                                           |
| scimark_sor                   | 89.6 ms                                                               | 90.4 ms: 1.01x slower                                                           |
| genshi_xml                    | 36.2 ms                                                               | 36.6 ms: 1.01x slower                                                           |
| docutils                      | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| django_template               | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                           |
| hexiom                        | 5.09 ms                                                               | 5.14 ms: 1.01x slower                                                           |
| meteor_contest                | 74.6 ms                                                               | 75.3 ms: 1.01x slower                                                           |
| deepcopy                      | 175 us                                                                | 177 us: 1.01x slower                                                            |
| bpe_tokeniser                 | 3.24 sec                                                              | 3.27 sec: 1.01x slower                                                          |
| sympy_sum                     | 81.3 ms                                                               | 82.1 ms: 1.01x slower                                                           |
| scimark_lu                    | 84.5 ms                                                               | 85.3 ms: 1.01x slower                                                           |
| deepcopy_memo                 | 21.8 us                                                               | 22.0 us: 1.01x slower                                                           |
| shortest_path                 | 328 ms                                                                | 332 ms: 1.01x slower                                                            |
| async_tree_memoization_tg     | 206 ms                                                                | 209 ms: 1.01x slower                                                            |
| regex_dna                     | 143 ms                                                                | 145 ms: 1.01x slower                                                            |
| logging_silent                | 342 ns                                                                | 346 ns: 1.01x slower                                                            |
| comprehensions                | 13.1 us                                                               | 13.3 us: 1.01x slower                                                           |
| unpickle_pure_python          | 177 us                                                                | 180 us: 1.01x slower                                                            |
| richards                      | 37.1 ms                                                               | 37.7 ms: 1.02x slower                                                           |
| nqueens                       | 70.2 ms                                                               | 71.3 ms: 1.02x slower                                                           |
| many_optionals                | 495 us                                                                | 503 us: 1.02x slower                                                            |
| subparsers                    | 14.8 ms                                                               | 15.1 ms: 1.02x slower                                                           |
| async_tree_io_tg              | 405 ms                                                                | 413 ms: 1.02x slower                                                            |
| pyflate                       | 332 ms                                                                | 339 ms: 1.02x slower                                                            |
| genshi_text                   | 17.7 ms                                                               | 18.2 ms: 1.03x slower                                                           |
| regex_effbot                  | 2.36 ms                                                               | 2.42 ms: 1.03x slower                                                           |
| regex_v8                      | 16.1 ms                                                               | 16.6 ms: 1.03x slower                                                           |
| mako                          | 9.03 ms                                                               | 9.33 ms: 1.03x slower                                                           |
| logging_simple                | 4.07 us                                                               | 4.22 us: 1.04x slower                                                           |
| logging_format                | 4.35 us                                                               | 4.53 us: 1.04x slower                                                           |
| dulwich_log                   | 26.4 ms                                                               | 27.5 ms: 1.04x slower                                                           |
| async_tree_eager              | 72.8 ms                                                               | 76.5 ms: 1.05x slower                                                           |
| python_startup                | 16.5 ms                                                               | 17.7 ms: 1.08x slower                                                           |
| python_startup_no_site        | 12.2 ms                                                               | 13.3 ms: 1.08x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (31): async_tree_eager_tg, async_tree_io, async_tree_eager_memoization_tg, scimark_sparse_mat_mult, async_tree_eager_cpu_io_mixed_tg, coroutines, nbody, async_generators, sympy_integrate, mdp, pidigits, sqlglot_v2_optimize, richards_super, dask, gc_traversal, pathlib, sqlite_synth, xml_etree_parse, asyncio_websockets, pickle_pure_python, json_dumps, xml_etree_iterparse, json, k_core, async_tree_none_tg, html5lib, pycparser, sphinx, async_tree_eager_io_tg, async_tree_eager_io, pylint

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x