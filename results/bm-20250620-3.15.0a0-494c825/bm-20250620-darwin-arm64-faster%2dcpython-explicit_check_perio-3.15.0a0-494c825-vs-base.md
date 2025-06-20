# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.007x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 188 ms: 1.01x slower                                                            |
| docutils       | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 432 ms                                                                | 434 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg | 422 ms                                                                | 424 ms: 1.00x slower                                                            |
| async_generators           | 273 ms                                                                | 275 ms: 1.00x slower                                                            |
| coroutines                 | 18.8 ms                                                               | 18.9 ms: 1.01x slower                                                           |
| async_tree_eager           | 72.8 ms                                                               | 73.4 ms: 1.01x slower                                                           |
| async_tree_none_tg         | 171 ms                                                                | 172 ms: 1.01x slower                                                            |
| async_tree_memoization     | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| async_tree_io              | 413 ms                                                                | 418 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 405 ms                                                                | 414 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (10): async_tree_eager_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_none, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| regex_compile  | 80.9 ms                                                               | 82.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 16.5 us                                                               | 16.6 us: 1.00x slower                                                           |
| json_dumps           | 6.82 ms                                                               | 6.87 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 73.7 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| xml_etree_generate   | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| pickle_pure_python   | 241 us                                                                | 244 us: 1.01x slower                                                            |
| unpickle_pure_python | 178 us                                                                | 180 us: 1.01x slower                                                            |
| tomli_loads          | 1.44 sec                                                              | 1.47 sec: 1.02x slower                                                          |
| xml_etree_process    | 43.1 ms                                                               | 43.9 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| genshi_xml      | 36.1 ms                                                               | 36.4 ms: 1.01x slower                                                           |
| django_template | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                           |
| mako            | 9.03 ms                                                               | 9.21 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles           | 1.36 ms                                                               | 1.35 ms: 1.00x faster                                                           |
| generators                 | 31.6 ms                                                               | 31.5 ms: 1.00x faster                                                           |
| nqueens                    | 70.1 ms                                                               | 69.9 ms: 1.00x faster                                                           |
| regex_dna                  | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| crypto_pyaes               | 61.0 ms                                                               | 61.1 ms: 1.00x slower                                                           |
| connected_components       | 303 ms                                                                | 304 ms: 1.00x slower                                                            |
| genshi_text                | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed    | 432 ms                                                                | 434 ms: 1.00x slower                                                            |
| scimark_fft                | 202 ms                                                                | 202 ms: 1.00x slower                                                            |
| async_tree_cpu_io_mixed_tg | 422 ms                                                                | 424 ms: 1.00x slower                                                            |
| async_generators           | 273 ms                                                                | 275 ms: 1.00x slower                                                            |
| json_loads                 | 16.5 us                                                               | 16.6 us: 1.00x slower                                                           |
| sympy_integrate            | 11.4 ms                                                               | 11.4 ms: 1.00x slower                                                           |
| raytrace                   | 212 ms                                                                | 213 ms: 1.00x slower                                                            |
| sqlite_synth               | 1.62 us                                                               | 1.62 us: 1.00x slower                                                           |
| scimark_sor                | 90.0 ms                                                               | 90.5 ms: 1.01x slower                                                           |
| chaos                      | 47.0 ms                                                               | 47.3 ms: 1.01x slower                                                           |
| coroutines                 | 18.8 ms                                                               | 18.9 ms: 1.01x slower                                                           |
| coverage                   | 49.4 ms                                                               | 49.7 ms: 1.01x slower                                                           |
| mdp                        | 824 ms                                                                | 829 ms: 1.01x slower                                                            |
| sqlglot_v2_parse           | 987 us                                                                | 993 us: 1.01x slower                                                            |
| 2to3                       | 186 ms                                                                | 188 ms: 1.01x slower                                                            |
| async_tree_eager           | 72.8 ms                                                               | 73.4 ms: 1.01x slower                                                           |
| genshi_xml                 | 36.1 ms                                                               | 36.4 ms: 1.01x slower                                                           |
| async_tree_none_tg         | 171 ms                                                                | 172 ms: 1.01x slower                                                            |
| async_tree_memoization     | 214 ms                                                                | 216 ms: 1.01x slower                                                            |
| sympy_str                  | 155 ms                                                                | 156 ms: 1.01x slower                                                            |
| docutils                   | 1.51 sec                                                              | 1.52 sec: 1.01x slower                                                          |
| json_dumps                 | 6.82 ms                                                               | 6.87 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 73.7 ms                                                               | 74.4 ms: 1.01x slower                                                           |
| dulwich_log                | 26.3 ms                                                               | 26.6 ms: 1.01x slower                                                           |
| sqlglot_v2_transpile       | 1.17 ms                                                               | 1.18 ms: 1.01x slower                                                           |
| xml_etree_generate         | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| json                       | 2.95 ms                                                               | 2.97 ms: 1.01x slower                                                           |
| scimark_monte_carlo        | 52.6 ms                                                               | 53.1 ms: 1.01x slower                                                           |
| sympy_expand               | 263 ms                                                                | 265 ms: 1.01x slower                                                            |
| django_template            | 25.1 ms                                                               | 25.3 ms: 1.01x slower                                                           |
| comprehensions             | 13.1 us                                                               | 13.3 us: 1.01x slower                                                           |
| async_tree_io              | 413 ms                                                                | 418 ms: 1.01x slower                                                            |
| scimark_sparse_mat_mult    | 3.19 ms                                                               | 3.22 ms: 1.01x slower                                                           |
| go                         | 99.2 ms                                                               | 100 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 110 us                                                                | 111 us: 1.01x slower                                                            |
| sympy_sum                  | 81.3 ms                                                               | 82.2 ms: 1.01x slower                                                           |
| pyflate                    | 331 ms                                                                | 335 ms: 1.01x slower                                                            |
| sqlglot_v2_normalize       | 76.1 ms                                                               | 77.0 ms: 1.01x slower                                                           |
| pickle_pure_python         | 241 us                                                                | 244 us: 1.01x slower                                                            |
| deepcopy                   | 175 us                                                                | 178 us: 1.01x slower                                                            |
| unpickle_pure_python       | 178 us                                                                | 180 us: 1.01x slower                                                            |
| hexiom                     | 5.10 ms                                                               | 5.17 ms: 1.02x slower                                                           |
| richards                   | 37.2 ms                                                               | 37.8 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 3.24 sec                                                              | 3.29 sec: 1.02x slower                                                          |
| deepcopy_reduce            | 1.90 us                                                               | 1.93 us: 1.02x slower                                                           |
| scimark_lu                 | 84.5 ms                                                               | 85.8 ms: 1.02x slower                                                           |
| sqlglot_v2_optimize        | 36.4 ms                                                               | 37.0 ms: 1.02x slower                                                           |
| logging_format             | 4.36 us                                                               | 4.43 us: 1.02x slower                                                           |
| pprint_pformat             | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                                          |
| regex_compile              | 80.9 ms                                                               | 82.3 ms: 1.02x slower                                                           |
| tomli_loads                | 1.44 sec                                                              | 1.47 sec: 1.02x slower                                                          |
| logging_simple             | 4.07 us                                                               | 4.14 us: 1.02x slower                                                           |
| many_optionals             | 492 us                                                                | 501 us: 1.02x slower                                                            |
| pprint_safe_repr           | 621 ms                                                                | 632 ms: 1.02x slower                                                            |
| xml_etree_process          | 43.1 ms                                                               | 43.9 ms: 1.02x slower                                                           |
| mako                       | 9.03 ms                                                               | 9.21 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 405 ms                                                                | 414 ms: 1.02x slower                                                            |
| richards_super             | 41.6 ms                                                               | 42.5 ms: 1.02x slower                                                           |
| deltablue                  | 2.80 ms                                                               | 2.87 ms: 1.02x slower                                                           |
| spectral_norm              | 72.1 ms                                                               | 74.0 ms: 1.03x slower                                                           |
| logging_silent             | 337 ns                                                                | 346 ns: 1.03x slower                                                            |
| deepcopy_memo              | 21.8 us                                                               | 22.6 us: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (32): async_tree_eager_tg, telco, k_core, nbody, fannkuch, float, asyncio_websockets, thrift, meteor_contest, async_tree_eager_cpu_io_mixed, regex_effbot, python_startup_no_site, pidigits, regex_v8, dask, shortest_path, async_tree_eager_cpu_io_mixed_tg, gc_traversal, async_tree_eager_memoization, xml_etree_parse, python_startup, pycparser, subparsers, sphinx, async_tree_eager_memoization_tg, async_tree_none, html5lib, async_tree_memoization_tg, async_tree_eager_io_tg, pathlib, async_tree_eager_io, pylint

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x