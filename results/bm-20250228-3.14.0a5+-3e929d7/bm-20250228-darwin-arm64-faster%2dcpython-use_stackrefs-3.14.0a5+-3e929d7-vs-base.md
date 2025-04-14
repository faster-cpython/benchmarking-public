# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.024x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                                 | 173 ms: 1.03x faster                                                      |
| docutils       | 1.51 sec                                                               | 1.50 sec: 1.01x faster                                                    |
| html5lib       | 33.1 ms                                                                | 32.3 ms: 1.02x faster                                                     |
| sphinx         | 609 ms                                                                 | 599 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|---------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization          | 222 ms                                                                 | 209 ms: 1.06x faster                                                      |
| coroutines                      | 18.7 ms                                                                | 17.6 ms: 1.06x faster                                                     |
| async_tree_none_tg              | 172 ms                                                                 | 165 ms: 1.05x faster                                                      |
| async_tree_eager                | 70.2 ms                                                                | 67.3 ms: 1.04x faster                                                     |
| async_tree_io_tg                | 401 ms                                                                 | 385 ms: 1.04x faster                                                      |
| async_tree_eager_io             | 399 ms                                                                 | 384 ms: 1.04x faster                                                      |
| async_tree_io                   | 415 ms                                                                 | 400 ms: 1.04x faster                                                      |
| async_tree_none                 | 178 ms                                                                 | 172 ms: 1.03x faster                                                      |
| async_tree_memoization_tg       | 212 ms                                                                 | 206 ms: 1.03x faster                                                      |
| async_tree_eager_io_tg          | 407 ms                                                                 | 395 ms: 1.03x faster                                                      |
| async_generators                | 269 ms                                                                 | 262 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed         | 435 ms                                                                 | 426 ms: 1.02x faster                                                      |
| async_tree_eager_tg             | 143 ms                                                                 | 140 ms: 1.02x faster                                                      |
| async_tree_eager_memoization_tg | 191 ms                                                                 | 187 ms: 1.02x faster                                                      |
| async_tree_eager_memoization    | 150 ms                                                                 | 149 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg      | 428 ms                                                                 | 424 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed   | 366 ms                                                                 | 363 ms: 1.01x faster                                                      |
| Geometric mean                  | (ref)                                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 92.3 ms                                                                | 79.9 ms: 1.16x faster                                                     |
| float          | 54.5 ms                                                                | 53.0 ms: 1.03x faster                                                     |
| pidigits       | 284 ms                                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 78.1 ms                                                                | 75.5 ms: 1.04x faster                                                     |
| regex_dna      | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| regex_v8       | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| regex_effbot   | 2.26 ms                                                                | 2.29 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_process    | 42.8 ms                                                                | 40.9 ms: 1.05x faster                                                     |
| pickle_pure_python   | 231 us                                                                 | 223 us: 1.03x faster                                                      |
| xml_etree_generate   | 58.1 ms                                                                | 56.6 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 75.2 ms                                                                | 73.4 ms: 1.02x faster                                                     |
| tomli_loads          | 1.45 sec                                                               | 1.43 sec: 1.02x faster                                                    |
| xml_etree_parse      | 104 ms                                                                 | 102 ms: 1.02x faster                                                      |
| unpickle_pure_python | 170 us                                                                 | 168 us: 1.01x faster                                                      |
| json_dumps           | 7.49 ms                                                                | 7.45 ms: 1.01x faster                                                     |
| json_loads           | 17.7 us                                                                | 17.6 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 12.4 ms                                                                | 11.8 ms: 1.05x faster                                                     |
| python_startup         | 17.1 ms                                                                | 16.6 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 24.4 ms                                                                | 22.7 ms: 1.07x faster                                                     |
| genshi_text     | 16.3 ms                                                                | 15.4 ms: 1.06x faster                                                     |
| genshi_xml      | 33.8 ms                                                                | 32.0 ms: 1.06x faster                                                     |
| mako            | 8.18 ms                                                                | 7.81 ms: 1.05x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                       | bm-20250228-darwin-arm64-python-fecf8bc8f2fd09a9a4c5-3.14.0a5+-fecf8bc | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|---------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators                      | 28.8 ms                                                                | 24.9 ms: 1.16x faster                                                     |
| nbody                           | 92.3 ms                                                                | 79.9 ms: 1.16x faster                                                     |
| raytrace                        | 213 ms                                                                 | 193 ms: 1.10x faster                                                      |
| pprint_pformat                  | 1.10 sec                                                               | 1.03 sec: 1.08x faster                                                    |
| django_template                 | 24.4 ms                                                                | 22.7 ms: 1.07x faster                                                     |
| pprint_safe_repr                | 545 ms                                                                 | 509 ms: 1.07x faster                                                      |
| richards                        | 39.9 ms                                                                | 37.5 ms: 1.06x faster                                                     |
| hexiom                          | 5.28 ms                                                                | 4.96 ms: 1.06x faster                                                     |
| async_tree_memoization          | 222 ms                                                                 | 209 ms: 1.06x faster                                                      |
| coroutines                      | 18.7 ms                                                                | 17.6 ms: 1.06x faster                                                     |
| genshi_text                     | 16.3 ms                                                                | 15.4 ms: 1.06x faster                                                     |
| scimark_monte_carlo             | 50.3 ms                                                                | 47.5 ms: 1.06x faster                                                     |
| genshi_xml                      | 33.8 ms                                                                | 32.0 ms: 1.06x faster                                                     |
| python_startup_no_site          | 12.4 ms                                                                | 11.8 ms: 1.05x faster                                                     |
| mako                            | 8.18 ms                                                                | 7.81 ms: 1.05x faster                                                     |
| xml_etree_process               | 42.8 ms                                                                | 40.9 ms: 1.05x faster                                                     |
| async_tree_none_tg              | 172 ms                                                                 | 165 ms: 1.05x faster                                                      |
| scimark_sor                     | 93.1 ms                                                                | 89.1 ms: 1.05x faster                                                     |
| async_tree_eager                | 70.2 ms                                                                | 67.3 ms: 1.04x faster                                                     |
| scimark_lu                      | 85.3 ms                                                                | 81.8 ms: 1.04x faster                                                     |
| async_tree_io_tg                | 401 ms                                                                 | 385 ms: 1.04x faster                                                      |
| logging_simple                  | 3.76 us                                                                | 3.62 us: 1.04x faster                                                     |
| logging_format                  | 4.08 us                                                                | 3.92 us: 1.04x faster                                                     |
| async_tree_eager_io             | 399 ms                                                                 | 384 ms: 1.04x faster                                                      |
| dulwich_log                     | 30.1 ms                                                                | 29.0 ms: 1.04x faster                                                     |
| sqlglot_parse                   | 889 us                                                                 | 856 us: 1.04x faster                                                      |
| async_tree_io                   | 415 ms                                                                 | 400 ms: 1.04x faster                                                      |
| sqlglot_transpile               | 1.07 ms                                                                | 1.04 ms: 1.04x faster                                                     |
| deltablue                       | 2.76 ms                                                                | 2.66 ms: 1.04x faster                                                     |
| coverage                        | 48.9 ms                                                                | 47.1 ms: 1.04x faster                                                     |
| deepcopy                        | 170 us                                                                 | 164 us: 1.04x faster                                                      |
| sqlglot_normalize               | 196 ms                                                                 | 189 ms: 1.04x faster                                                      |
| regex_compile                   | 78.1 ms                                                                | 75.5 ms: 1.04x faster                                                     |
| async_tree_none                 | 178 ms                                                                 | 172 ms: 1.03x faster                                                      |
| deepcopy_reduce                 | 1.77 us                                                                | 1.71 us: 1.03x faster                                                     |
| pickle_pure_python              | 231 us                                                                 | 223 us: 1.03x faster                                                      |
| deepcopy_memo                   | 21.0 us                                                                | 20.3 us: 1.03x faster                                                     |
| sqlglot_optimize                | 35.7 ms                                                                | 34.6 ms: 1.03x faster                                                     |
| async_tree_memoization_tg       | 212 ms                                                                 | 206 ms: 1.03x faster                                                      |
| python_startup                  | 17.1 ms                                                                | 16.6 ms: 1.03x faster                                                     |
| sqlalchemy_imperative           | 7.09 ms                                                                | 6.88 ms: 1.03x faster                                                     |
| async_tree_eager_io_tg          | 407 ms                                                                 | 395 ms: 1.03x faster                                                      |
| sympy_sum                       | 79.7 ms                                                                | 77.5 ms: 1.03x faster                                                     |
| xml_etree_generate              | 58.1 ms                                                                | 56.6 ms: 1.03x faster                                                     |
| 2to3                            | 178 ms                                                                 | 173 ms: 1.03x faster                                                      |
| sympy_expand                    | 255 ms                                                                 | 249 ms: 1.03x faster                                                      |
| async_generators                | 269 ms                                                                 | 262 ms: 1.03x faster                                                      |
| float                           | 54.5 ms                                                                | 53.0 ms: 1.03x faster                                                     |
| sympy_str                       | 153 ms                                                                 | 149 ms: 1.03x faster                                                      |
| telco                           | 4.78 ms                                                                | 4.66 ms: 1.02x faster                                                     |
| html5lib                        | 33.1 ms                                                                | 32.3 ms: 1.02x faster                                                     |
| xml_etree_iterparse             | 75.2 ms                                                                | 73.4 ms: 1.02x faster                                                     |
| logging_silent                  | 73.1 ns                                                                | 71.4 ns: 1.02x faster                                                     |
| richards_super                  | 42.8 ms                                                                | 41.8 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed         | 435 ms                                                                 | 426 ms: 1.02x faster                                                      |
| async_tree_eager_tg             | 143 ms                                                                 | 140 ms: 1.02x faster                                                      |
| subparsers                      | 12.9 ms                                                                | 12.7 ms: 1.02x faster                                                     |
| go                              | 94.9 ms                                                                | 93.0 ms: 1.02x faster                                                     |
| scimark_fft                     | 204 ms                                                                 | 200 ms: 1.02x faster                                                      |
| async_tree_eager_memoization_tg | 191 ms                                                                 | 187 ms: 1.02x faster                                                      |
| tomli_loads                     | 1.45 sec                                                               | 1.43 sec: 1.02x faster                                                    |
| sqlalchemy_declarative          | 62.6 ms                                                                | 61.5 ms: 1.02x faster                                                     |
| mdp                             | 1.55 sec                                                               | 1.53 sec: 1.02x faster                                                    |
| xml_etree_parse                 | 104 ms                                                                 | 102 ms: 1.02x faster                                                      |
| sphinx                          | 609 ms                                                                 | 599 ms: 1.02x faster                                                      |
| comprehensions                  | 13.1 us                                                                | 12.9 us: 1.02x faster                                                     |
| thrift                          | 460 us                                                                 | 454 us: 1.01x faster                                                      |
| async_tree_eager_memoization    | 150 ms                                                                 | 149 ms: 1.01x faster                                                      |
| many_optionals                  | 467 us                                                                 | 462 us: 1.01x faster                                                      |
| sympy_integrate                 | 12.2 ms                                                                | 12.1 ms: 1.01x faster                                                     |
| meteor_contest                  | 78.3 ms                                                                | 77.5 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg      | 428 ms                                                                 | 424 ms: 1.01x faster                                                      |
| async_tree_eager_cpu_io_mixed   | 366 ms                                                                 | 363 ms: 1.01x faster                                                      |
| unpickle_pure_python            | 170 us                                                                 | 168 us: 1.01x faster                                                      |
| json                            | 3.03 ms                                                                | 3.00 ms: 1.01x faster                                                     |
| docutils                        | 1.51 sec                                                               | 1.50 sec: 1.01x faster                                                    |
| json_dumps                      | 7.49 ms                                                                | 7.45 ms: 1.01x faster                                                     |
| json_loads                      | 17.7 us                                                                | 17.6 us: 1.01x faster                                                     |
| scimark_sparse_mat_mult         | 3.08 ms                                                                | 3.07 ms: 1.00x faster                                                     |
| pidigits                        | 284 ms                                                                 | 283 ms: 1.00x faster                                                      |
| create_gc_cycles                | 1.27 ms                                                                | 1.27 ms: 1.00x slower                                                     |
| gc_traversal                    | 3.09 ms                                                                | 3.10 ms: 1.00x slower                                                     |
| regex_dna                       | 140 ms                                                                 | 141 ms: 1.01x slower                                                      |
| regex_v8                        | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                     |
| regex_effbot                    | 2.26 ms                                                                | 2.29 ms: 1.01x slower                                                     |
| spectral_norm                   | 78.1 ms                                                                | 79.5 ms: 1.02x slower                                                     |
| bpe_tokeniser                   | 3.24 sec                                                               | 3.32 sec: 1.03x slower                                                    |
| k_core                          | 1.54 sec                                                               | 1.58 sec: 1.03x slower                                                    |
| shortest_path                   | 339 ms                                                                 | 351 ms: 1.03x slower                                                      |
| crypto_pyaes                    | 59.1 ms                                                                | 61.5 ms: 1.04x slower                                                     |
| connected_components            | 314 ms                                                                 | 328 ms: 1.05x slower                                                      |
| fannkuch                        | 293 ms                                                                 | 309 ms: 1.05x slower                                                      |
| nqueens                         | 65.4 ms                                                                | 69.2 ms: 1.06x slower                                                     |
| Geometric mean                  | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (12): pylint, pycparser, asyncio_websockets, bench_mp_pool, typing_runtime_protocols, dask, chaos, pyflate, async_tree_eager_cpu_io_mixed_tg, sqlite_synth, pathlib, bench_thread_pool

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.00x