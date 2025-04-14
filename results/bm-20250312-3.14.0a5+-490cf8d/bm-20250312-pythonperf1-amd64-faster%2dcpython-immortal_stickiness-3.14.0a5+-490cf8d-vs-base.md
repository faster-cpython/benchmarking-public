# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.009x faster
- HPT reliability: 98.74%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines                 | 13.6 ms                                                                     | 13.4 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 179 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| async_tree_memoization     | 222 ms                                                                      | 220 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 343 ms: 1.01x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                      | 347 ms: 1.02x slower                                                                 |
| asyncio_websockets         | 306 ms                                                                      | 313 ms: 1.02x slower                                                                 |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (5): async_generators, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 46.1 ms                                                                     | 45.3 ms: 1.02x faster                                                                |
| pidigits       | 151 ms                                                                      | 152 ms: 1.01x slower                                                                 |
| nbody          | 67.8 ms                                                                     | 69.2 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.54 ms                                                                     | 1.40 ms: 1.10x faster                                                                |
| regex_v8       | 14.2 ms                                                                     | 13.1 ms: 1.08x faster                                                                |
| regex_dna      | 119 ms                                                                      | 112 ms: 1.06x faster                                                                 |
| regex_compile  | 86.4 ms                                                                     | 85.9 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 150 us                                                                      | 146 us: 1.03x faster                                                                 |
| xml_etree_generate   | 60.0 ms                                                                     | 58.9 ms: 1.02x faster                                                                |
| pickle_pure_python   | 227 us                                                                      | 224 us: 1.02x faster                                                                 |
| xml_etree_process    | 42.6 ms                                                                     | 42.1 ms: 1.01x faster                                                                |
| json_loads           | 14.8 us                                                                     | 14.7 us: 1.01x faster                                                                |
| xml_etree_parse      | 90.8 ms                                                                     | 91.7 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (3): json_dumps, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 25.7 ms                                                                     | 26.0 ms: 1.01x slower                                                                |
| genshi_text     | 17.0 ms                                                                     | 17.3 ms: 1.01x slower                                                                |
| genshi_xml      | 37.3 ms                                                                     | 38.3 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot               | 1.54 ms                                                                     | 1.40 ms: 1.10x faster                                                                |
| regex_v8                   | 14.2 ms                                                                     | 13.1 ms: 1.08x faster                                                                |
| pprint_safe_repr           | 558 ms                                                                      | 518 ms: 1.08x faster                                                                 |
| scimark_sor                | 83.3 ms                                                                     | 77.7 ms: 1.07x faster                                                                |
| regex_dna                  | 119 ms                                                                      | 112 ms: 1.06x faster                                                                 |
| spectral_norm              | 59.3 ms                                                                     | 56.0 ms: 1.06x faster                                                                |
| pprint_pformat             | 1.09 sec                                                                    | 1.06 sec: 1.03x faster                                                               |
| richards_super             | 33.8 ms                                                                     | 32.8 ms: 1.03x faster                                                                |
| richards                   | 29.8 ms                                                                     | 28.9 ms: 1.03x faster                                                                |
| logging_format             | 7.16 us                                                                     | 6.97 us: 1.03x faster                                                                |
| connected_components       | 341 ms                                                                      | 332 ms: 1.03x faster                                                                 |
| bpe_tokeniser              | 3.04 sec                                                                    | 2.96 sec: 1.03x faster                                                               |
| unpickle_pure_python       | 150 us                                                                      | 146 us: 1.03x faster                                                                 |
| fannkuch                   | 283 ms                                                                      | 276 ms: 1.02x faster                                                                 |
| logging_simple             | 6.62 us                                                                     | 6.47 us: 1.02x faster                                                                |
| crypto_pyaes               | 51.3 ms                                                                     | 50.2 ms: 1.02x faster                                                                |
| sqlite_synth               | 1.62 us                                                                     | 1.58 us: 1.02x faster                                                                |
| scimark_fft                | 181 ms                                                                      | 178 ms: 1.02x faster                                                                 |
| xml_etree_generate         | 60.0 ms                                                                     | 58.9 ms: 1.02x faster                                                                |
| scimark_monte_carlo        | 44.1 ms                                                                     | 43.3 ms: 1.02x faster                                                                |
| float                      | 46.1 ms                                                                     | 45.3 ms: 1.02x faster                                                                |
| create_gc_cycles           | 1.26 ms                                                                     | 1.24 ms: 1.02x faster                                                                |
| thrift                     | 520 us                                                                      | 512 us: 1.02x faster                                                                 |
| pickle_pure_python         | 227 us                                                                      | 224 us: 1.02x faster                                                                 |
| pyflate                    | 314 ms                                                                      | 310 ms: 1.01x faster                                                                 |
| sympy_expand               | 303 ms                                                                      | 299 ms: 1.01x faster                                                                 |
| nqueens                    | 64.8 ms                                                                     | 63.9 ms: 1.01x faster                                                                |
| coroutines                 | 13.6 ms                                                                     | 13.4 ms: 1.01x faster                                                                |
| telco                      | 4.91 ms                                                                     | 4.85 ms: 1.01x faster                                                                |
| chaos                      | 43.9 ms                                                                     | 43.4 ms: 1.01x faster                                                                |
| xml_etree_process          | 42.6 ms                                                                     | 42.1 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 179 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| async_tree_memoization     | 222 ms                                                                      | 220 ms: 1.01x faster                                                                 |
| subparsers                 | 16.6 ms                                                                     | 16.5 ms: 1.01x faster                                                                |
| deepcopy_reduce            | 1.92 us                                                                     | 1.91 us: 1.01x faster                                                                |
| hexiom                     | 4.34 ms                                                                     | 4.31 ms: 1.01x faster                                                                |
| json_loads                 | 14.8 us                                                                     | 14.7 us: 1.01x faster                                                                |
| sqlglot_v2_normalize       | 74.7 ms                                                                     | 74.2 ms: 1.01x faster                                                                |
| sympy_sum                  | 89.4 ms                                                                     | 88.7 ms: 1.01x faster                                                                |
| regex_compile              | 86.4 ms                                                                     | 85.9 ms: 1.01x faster                                                                |
| comprehensions             | 11.8 us                                                                     | 11.8 us: 1.01x faster                                                                |
| sympy_integrate            | 13.3 ms                                                                     | 13.3 ms: 1.01x faster                                                                |
| sqlglot_v2_optimize        | 35.8 ms                                                                     | 35.6 ms: 1.00x faster                                                                |
| deltablue                  | 2.25 ms                                                                     | 2.24 ms: 1.00x faster                                                                |
| mdp                        | 1.59 sec                                                                    | 1.60 sec: 1.00x slower                                                               |
| scimark_lu                 | 60.0 ms                                                                     | 60.4 ms: 1.01x slower                                                                |
| sqlglot_v2_transpile       | 1.11 ms                                                                     | 1.12 ms: 1.01x slower                                                                |
| pidigits                   | 151 ms                                                                      | 152 ms: 1.01x slower                                                                 |
| xml_etree_parse            | 90.8 ms                                                                     | 91.7 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 343 ms: 1.01x slower                                                                 |
| django_template            | 25.7 ms                                                                     | 26.0 ms: 1.01x slower                                                                |
| genshi_text                | 17.0 ms                                                                     | 17.3 ms: 1.01x slower                                                                |
| generators                 | 19.2 ms                                                                     | 19.4 ms: 1.01x slower                                                                |
| json                       | 3.01 ms                                                                     | 3.06 ms: 1.02x slower                                                                |
| coverage                   | 48.7 ms                                                                     | 49.5 ms: 1.02x slower                                                                |
| typing_runtime_protocols   | 111 us                                                                      | 113 us: 1.02x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                      | 347 ms: 1.02x slower                                                                 |
| nbody                      | 67.8 ms                                                                     | 69.2 ms: 1.02x slower                                                                |
| deepcopy_memo              | 19.4 us                                                                     | 19.8 us: 1.02x slower                                                                |
| asyncio_websockets         | 306 ms                                                                      | 313 ms: 1.02x slower                                                                 |
| genshi_xml                 | 37.3 ms                                                                     | 38.3 ms: 1.03x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (33): python_startup_no_site, python_startup, mako, logging_silent, sympy_str, pathlib, bench_mp_pool, json_dumps, docutils, shortest_path, tomli_loads, pylint, async_generators, meteor_contest, 2to3, async_tree_none, sqlglot_v2_parse, many_optionals, async_tree_io_tg, bench_thread_pool, deepcopy, gc_traversal, scimark_sparse_mat_mult, pycparser, k_core, sphinx, raytrace, async_tree_memoization_tg, xml_etree_iterparse, dulwich_log, html5lib, async_tree_io, go

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 98.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown