# Results vs. base

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.007x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| html5lib       | 39.1 ms                                                                     | 39.5 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 314 ms                                                                      | 302 ms: 1.04x faster                                                             |
| coroutines                 | 14.8 ms                                                                     | 14.7 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 345 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 345 ms                                                                      | 347 ms: 1.01x slower                                                             |
| async_tree_none            | 192 ms                                                                      | 195 ms: 1.02x slower                                                             |
| async_tree_none_tg         | 180 ms                                                                      | 187 ms: 1.04x slower                                                             |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                     |

Benchmark hidden because not significant (5): async_generators, async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 148 ms: 1.01x slower                                                             |
| float          | 50.1 ms                                                                     | 51.9 ms: 1.04x slower                                                            |
| nbody          | 74.9 ms                                                                     | 78.2 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.51 ms                                                                     | 1.48 ms: 1.02x faster                                                            |
| regex_dna      | 117 ms                                                                      | 116 ms: 1.01x faster                                                             |
| regex_compile  | 88.2 ms                                                                     | 89.3 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 16.0 us                                                                     | 15.4 us: 1.04x faster                                                            |
| json_dumps           | 6.82 ms                                                                     | 6.77 ms: 1.01x faster                                                            |
| xml_etree_parse      | 87.5 ms                                                                     | 88.0 ms: 1.01x slower                                                            |
| xml_etree_process    | 41.1 ms                                                                     | 41.4 ms: 1.01x slower                                                            |
| unpickle_pure_python | 153 us                                                                      | 155 us: 1.01x slower                                                             |
| xml_etree_generate   | 57.7 ms                                                                     | 58.5 ms: 1.01x slower                                                            |
| pickle_pure_python   | 229 us                                                                      | 236 us: 1.03x slower                                                             |
| tomli_loads          | 1.40 sec                                                                    | 1.45 sec: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 24.7 ms                                                                     | 24.3 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 35.4 ms                                                                     | 34.7 ms: 1.02x faster                                                            |
| mako            | 6.88 ms                                                                     | 6.77 ms: 1.02x faster                                                            |
| genshi_text     | 16.5 ms                                                                     | 16.3 ms: 1.01x faster                                                            |
| django_template | 25.7 ms                                                                     | 25.9 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 1.63 sec                                                                    | 1.51 sec: 1.08x faster                                                           |
| json                       | 3.20 ms                                                                     | 3.04 ms: 1.05x faster                                                            |
| asyncio_websockets         | 314 ms                                                                      | 302 ms: 1.04x faster                                                             |
| json_loads                 | 16.0 us                                                                     | 15.4 us: 1.04x faster                                                            |
| sympy_sum                  | 90.9 ms                                                                     | 88.0 ms: 1.03x faster                                                            |
| sqlite_synth               | 1.62 us                                                                     | 1.57 us: 1.03x faster                                                            |
| generators                 | 21.5 ms                                                                     | 21.0 ms: 1.03x faster                                                            |
| sympy_integrate            | 13.6 ms                                                                     | 13.3 ms: 1.02x faster                                                            |
| regex_effbot               | 1.51 ms                                                                     | 1.48 ms: 1.02x faster                                                            |
| genshi_xml                 | 35.4 ms                                                                     | 34.7 ms: 1.02x faster                                                            |
| scimark_fft                | 195 ms                                                                      | 191 ms: 1.02x faster                                                             |
| sympy_expand               | 304 ms                                                                      | 299 ms: 1.02x faster                                                             |
| telco                      | 4.87 ms                                                                     | 4.79 ms: 1.02x faster                                                            |
| mako                       | 6.88 ms                                                                     | 6.77 ms: 1.02x faster                                                            |
| python_startup             | 24.7 ms                                                                     | 24.3 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.10 ms                                                                     | 1.09 ms: 1.01x faster                                                            |
| crypto_pyaes               | 49.2 ms                                                                     | 48.6 ms: 1.01x faster                                                            |
| genshi_text                | 16.5 ms                                                                     | 16.3 ms: 1.01x faster                                                            |
| coroutines                 | 14.8 ms                                                                     | 14.7 ms: 1.01x faster                                                            |
| sympy_str                  | 178 ms                                                                      | 177 ms: 1.01x faster                                                             |
| sqlglot_parse              | 888 us                                                                      | 882 us: 1.01x faster                                                             |
| json_dumps                 | 6.82 ms                                                                     | 6.77 ms: 1.01x faster                                                            |
| meteor_contest             | 75.8 ms                                                                     | 75.4 ms: 1.01x faster                                                            |
| regex_dna                  | 117 ms                                                                      | 116 ms: 1.01x faster                                                             |
| dulwich_log                | 42.5 ms                                                                     | 42.7 ms: 1.00x slower                                                            |
| xml_etree_parse            | 87.5 ms                                                                     | 88.0 ms: 1.01x slower                                                            |
| pidigits                   | 147 ms                                                                      | 148 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 345 ms: 1.01x slower                                                             |
| connected_components       | 318 ms                                                                      | 319 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 345 ms                                                                      | 347 ms: 1.01x slower                                                             |
| xml_etree_process          | 41.1 ms                                                                     | 41.4 ms: 1.01x slower                                                            |
| coverage                   | 48.9 ms                                                                     | 49.3 ms: 1.01x slower                                                            |
| pathlib                    | 77.4 ms                                                                     | 78.0 ms: 1.01x slower                                                            |
| nqueens                    | 65.5 ms                                                                     | 66.1 ms: 1.01x slower                                                            |
| django_template            | 25.7 ms                                                                     | 25.9 ms: 1.01x slower                                                            |
| deepcopy_reduce            | 1.84 us                                                                     | 1.86 us: 1.01x slower                                                            |
| pprint_pformat             | 1.08 sec                                                                    | 1.09 sec: 1.01x slower                                                           |
| sqlglot_optimize           | 36.2 ms                                                                     | 36.6 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 153 us                                                                      | 155 us: 1.01x slower                                                             |
| regex_compile              | 88.2 ms                                                                     | 89.3 ms: 1.01x slower                                                            |
| deepcopy                   | 183 us                                                                      | 185 us: 1.01x slower                                                             |
| html5lib                   | 39.1 ms                                                                     | 39.5 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 197 ms                                                                      | 200 ms: 1.01x slower                                                             |
| xml_etree_generate         | 57.7 ms                                                                     | 58.5 ms: 1.01x slower                                                            |
| shortest_path              | 351 ms                                                                      | 356 ms: 1.01x slower                                                             |
| scimark_monte_carlo        | 48.0 ms                                                                     | 48.8 ms: 1.02x slower                                                            |
| async_tree_none            | 192 ms                                                                      | 195 ms: 1.02x slower                                                             |
| bpe_tokeniser              | 3.00 sec                                                                    | 3.05 sec: 1.02x slower                                                           |
| raytrace                   | 202 ms                                                                      | 206 ms: 1.02x slower                                                             |
| deepcopy_memo              | 20.3 us                                                                     | 20.8 us: 1.02x slower                                                            |
| pprint_safe_repr           | 538 ms                                                                      | 551 ms: 1.02x slower                                                             |
| chaos                      | 42.5 ms                                                                     | 43.5 ms: 1.02x slower                                                            |
| pyflate                    | 308 ms                                                                      | 316 ms: 1.02x slower                                                             |
| logging_simple             | 6.25 us                                                                     | 6.41 us: 1.02x slower                                                            |
| logging_format             | 6.66 us                                                                     | 6.82 us: 1.03x slower                                                            |
| logging_silent             | 68.1 ns                                                                     | 69.9 ns: 1.03x slower                                                            |
| pickle_pure_python         | 229 us                                                                      | 236 us: 1.03x slower                                                             |
| comprehensions             | 12.6 us                                                                     | 13.0 us: 1.03x slower                                                            |
| float                      | 50.1 ms                                                                     | 51.9 ms: 1.04x slower                                                            |
| tomli_loads                | 1.40 sec                                                                    | 1.45 sec: 1.04x slower                                                           |
| async_tree_none_tg         | 180 ms                                                                      | 187 ms: 1.04x slower                                                             |
| scimark_sor                | 90.8 ms                                                                     | 94.7 ms: 1.04x slower                                                            |
| nbody                      | 74.9 ms                                                                     | 78.2 ms: 1.04x slower                                                            |
| richards_super             | 35.7 ms                                                                     | 37.4 ms: 1.05x slower                                                            |
| deltablue                  | 2.36 ms                                                                     | 2.48 ms: 1.05x slower                                                            |
| go                         | 89.2 ms                                                                     | 93.6 ms: 1.05x slower                                                            |
| richards                   | 31.5 ms                                                                     | 33.1 ms: 1.05x slower                                                            |
| hexiom                     | 4.54 ms                                                                     | 4.79 ms: 1.05x slower                                                            |
| fannkuch                   | 272 ms                                                                      | 289 ms: 1.06x slower                                                             |
| scimark_lu                 | 67.1 ms                                                                     | 71.5 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 2.58 ms                                                                     | 2.76 ms: 1.07x slower                                                            |
| spectral_norm              | 60.5 ms                                                                     | 66.2 ms: 1.09x slower                                                            |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (22): bench_thread_pool, async_generators, xml_etree_iterparse, typing_runtime_protocols, thrift, create_gc_cycles, async_tree_memoization_tg, docutils, sphinx, many_optionals, gc_traversal, 2to3, async_tree_memoization, bench_mp_pool, async_tree_io, pylint, subparsers, pycparser, k_core, async_tree_io_tg, python_startup_no_site, regex_v8

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown