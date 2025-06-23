# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.003x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines       | 18.9 ms                                                               | 18.7 ms: 1.01x faster                                                           |
| async_tree_eager | 72.7 ms                                                               | 73.1 ms: 1.01x slower                                                           |
| async_generators | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (16): async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_tg, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_eager_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| regex_v8       | 16.2 ms                                                               | 16.3 ms: 1.00x slower                                                           |
| regex_compile  | 81.1 ms                                                               | 81.5 ms: 1.01x slower                                                           |
| regex_dna      | 143 ms                                                                | 144 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 73.7 ms                                                               | 74.1 ms: 1.01x slower                                                           |
| pickle_pure_python   | 241 us                                                                | 243 us: 1.01x slower                                                            |
| xml_etree_generate   | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| unpickle_pure_python | 178 us                                                                | 180 us: 1.01x slower                                                            |
| tomli_loads          | 1.44 sec                                                              | 1.46 sec: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): json_loads, json_dumps, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                               | 13.3 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 36.2 ms                                                               | 36.3 ms: 1.00x slower                                                           |
| genshi_text     | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| mako            | 9.04 ms                                                               | 9.21 ms: 1.02x slower                                                           |
| django_template | 25.0 ms                                                               | 25.5 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20250619-darwin-arm64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| raytrace                 | 219 ms                                                                | 212 ms: 1.03x faster                                                            |
| connected_components     | 304 ms                                                                | 300 ms: 1.01x faster                                                            |
| scimark_monte_carlo      | 53.3 ms                                                               | 52.7 ms: 1.01x faster                                                           |
| telco                    | 4.79 ms                                                               | 4.74 ms: 1.01x faster                                                           |
| meteor_contest           | 74.7 ms                                                               | 74.2 ms: 1.01x faster                                                           |
| coroutines               | 18.9 ms                                                               | 18.7 ms: 1.01x faster                                                           |
| scimark_fft              | 202 ms                                                                | 201 ms: 1.01x faster                                                            |
| spectral_norm            | 72.1 ms                                                               | 71.7 ms: 1.01x faster                                                           |
| scimark_sor              | 89.8 ms                                                               | 89.7 ms: 1.00x faster                                                           |
| regex_effbot             | 2.34 ms                                                               | 2.35 ms: 1.00x slower                                                           |
| chaos                    | 47.0 ms                                                               | 47.2 ms: 1.00x slower                                                           |
| genshi_xml               | 36.2 ms                                                               | 36.3 ms: 1.00x slower                                                           |
| sqlite_synth             | 1.62 us                                                               | 1.62 us: 1.00x slower                                                           |
| 2to3                     | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| fannkuch                 | 304 ms                                                                | 305 ms: 1.00x slower                                                            |
| sqlglot_v2_transpile     | 1.17 ms                                                               | 1.17 ms: 1.00x slower                                                           |
| genshi_text              | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| deltablue                | 2.80 ms                                                               | 2.81 ms: 1.00x slower                                                           |
| python_startup_no_site   | 13.2 ms                                                               | 13.3 ms: 1.00x slower                                                           |
| regex_v8                 | 16.2 ms                                                               | 16.3 ms: 1.00x slower                                                           |
| regex_compile            | 81.1 ms                                                               | 81.5 ms: 1.01x slower                                                           |
| sqlglot_v2_parse         | 986 us                                                                | 991 us: 1.01x slower                                                            |
| xml_etree_iterparse      | 73.7 ms                                                               | 74.1 ms: 1.01x slower                                                           |
| sympy_sum                | 81.0 ms                                                               | 81.4 ms: 1.01x slower                                                           |
| logging_format           | 4.36 us                                                               | 4.38 us: 1.01x slower                                                           |
| create_gc_cycles         | 1.35 ms                                                               | 1.36 ms: 1.01x slower                                                           |
| sympy_integrate          | 11.3 ms                                                               | 11.4 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 109 us                                                                | 110 us: 1.01x slower                                                            |
| async_tree_eager         | 72.7 ms                                                               | 73.1 ms: 1.01x slower                                                           |
| regex_dna                | 143 ms                                                                | 144 ms: 1.01x slower                                                            |
| sympy_expand             | 261 ms                                                                | 263 ms: 1.01x slower                                                            |
| deepcopy_reduce          | 1.90 us                                                               | 1.91 us: 1.01x slower                                                           |
| coverage                 | 49.2 ms                                                               | 49.6 ms: 1.01x slower                                                           |
| logging_simple           | 4.07 us                                                               | 4.10 us: 1.01x slower                                                           |
| pprint_safe_repr         | 622 ms                                                                | 627 ms: 1.01x slower                                                            |
| nqueens                  | 70.3 ms                                                               | 70.9 ms: 1.01x slower                                                           |
| mdp                      | 823 ms                                                                | 830 ms: 1.01x slower                                                            |
| thrift                   | 469 us                                                                | 473 us: 1.01x slower                                                            |
| async_generators         | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| pprint_pformat           | 1.26 sec                                                              | 1.27 sec: 1.01x slower                                                          |
| dulwich_log              | 26.3 ms                                                               | 26.5 ms: 1.01x slower                                                           |
| bpe_tokeniser            | 3.23 sec                                                              | 3.26 sec: 1.01x slower                                                          |
| pickle_pure_python       | 241 us                                                                | 243 us: 1.01x slower                                                            |
| xml_etree_generate       | 58.5 ms                                                               | 59.1 ms: 1.01x slower                                                           |
| deepcopy_memo            | 21.8 us                                                               | 22.0 us: 1.01x slower                                                           |
| pyflate                  | 332 ms                                                                | 336 ms: 1.01x slower                                                            |
| sqlglot_v2_normalize     | 76.3 ms                                                               | 77.1 ms: 1.01x slower                                                           |
| comprehensions           | 13.1 us                                                               | 13.2 us: 1.01x slower                                                           |
| sqlglot_v2_optimize      | 36.5 ms                                                               | 36.9 ms: 1.01x slower                                                           |
| scimark_lu               | 84.5 ms                                                               | 85.4 ms: 1.01x slower                                                           |
| richards                 | 37.1 ms                                                               | 37.6 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 178 us                                                                | 180 us: 1.01x slower                                                            |
| tomli_loads              | 1.44 sec                                                              | 1.46 sec: 1.01x slower                                                          |
| logging_silent           | 340 ns                                                                | 345 ns: 1.02x slower                                                            |
| many_optionals           | 494 us                                                                | 502 us: 1.02x slower                                                            |
| mako                     | 9.04 ms                                                               | 9.21 ms: 1.02x slower                                                           |
| django_template          | 25.0 ms                                                               | 25.5 ms: 1.02x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (44): json_loads, json_dumps, shortest_path, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, json, async_tree_cpu_io_mixed_tg, float, pidigits, richards_super, generators, async_tree_eager_cpu_io_mixed, xml_etree_parse, scimark_sparse_mat_mult, k_core, crypto_pyaes, async_tree_cpu_io_mixed, nbody, asyncio_websockets, async_tree_eager_tg, gc_traversal, go, dask, hexiom, async_tree_memoization, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, subparsers, docutils, deepcopy, async_tree_io, async_tree_none, sympy_str, async_tree_memoization_tg, async_tree_eager_io, html5lib, xml_etree_process, sphinx, async_tree_io_tg, pycparser, pylint, pathlib, python_startup

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x