# Results vs. base

- fork: faster-cpython
- ref: jit_trampoline
- machine: linux-x86_64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.006x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                                      | 286 ms: 1.01x faster                                                            |
| html5lib       | 67.1 ms                                                                     | 68.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines             | 23.1 ms                                                                     | 22.4 ms: 1.03x faster                                                           |
| async_generators       | 447 ms                                                                      | 443 ms: 1.01x faster                                                            |
| async_tree_none        | 272 ms                                                                      | 270 ms: 1.01x faster                                                            |
| async_tree_memoization | 329 ms                                                                      | 327 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 65.8 ms                                                                     | 64.0 ms: 1.03x faster                                                           |
| pidigits       | 256 ms                                                                      | 255 ms: 1.00x faster                                                            |
| nbody          | 103 ms                                                                      | 106 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.6 ms                                                                     | 23.3 ms: 1.01x faster                                                           |
| regex_effbot   | 3.62 ms                                                                     | 3.58 ms: 1.01x faster                                                           |
| regex_compile  | 134 ms                                                                      | 133 ms: 1.01x faster                                                            |
| regex_dna      | 224 ms                                                                      | 228 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 149 ms                                                                      | 143 ms: 1.04x faster                                                            |
| xml_etree_generate   | 80.9 ms                                                                     | 78.4 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 100 ms                                                                      | 98.0 ms: 1.02x faster                                                           |
| pickle_pure_python   | 334 us                                                                      | 328 us: 1.02x faster                                                            |
| json_dumps           | 10.2 ms                                                                     | 10.0 ms: 1.02x faster                                                           |
| json_loads           | 25.4 us                                                                     | 25.1 us: 1.01x faster                                                           |
| unpickle_pure_python | 194 us                                                                      | 191 us: 1.01x faster                                                            |
| xml_etree_process    | 55.8 ms                                                                     | 55.0 ms: 1.01x faster                                                           |
| tomli_loads          | 1.93 sec                                                                    | 1.92 sec: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.3 ms                                                                     | 35.0 ms: 1.01x faster                                                           |
| mako            | 9.85 ms                                                                     | 9.79 ms: 1.01x faster                                                           |
| genshi_text     | 23.1 ms                                                                     | 23.4 ms: 1.02x slower                                                           |
| genshi_xml      | 55.0 ms                                                                     | 56.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20250819-pythonperf2-x86_64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf2-x86_64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|-------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 5.02 ms                                                                     | 4.79 ms: 1.05x faster                                                           |
| xml_etree_parse         | 149 ms                                                                      | 143 ms: 1.04x faster                                                            |
| spectral_norm           | 80.9 ms                                                                     | 77.6 ms: 1.04x faster                                                           |
| pprint_pformat          | 1.53 sec                                                                    | 1.48 sec: 1.04x faster                                                          |
| meteor_contest          | 125 ms                                                                      | 120 ms: 1.03x faster                                                            |
| fannkuch                | 380 ms                                                                      | 367 ms: 1.03x faster                                                            |
| xml_etree_generate      | 80.9 ms                                                                     | 78.4 ms: 1.03x faster                                                           |
| hexiom                  | 6.25 ms                                                                     | 6.06 ms: 1.03x faster                                                           |
| coroutines              | 23.1 ms                                                                     | 22.4 ms: 1.03x faster                                                           |
| float                   | 65.8 ms                                                                     | 64.0 ms: 1.03x faster                                                           |
| xml_etree_iterparse     | 100 ms                                                                      | 98.0 ms: 1.02x faster                                                           |
| go                      | 127 ms                                                                      | 124 ms: 1.02x faster                                                            |
| pprint_safe_repr        | 753 ms                                                                      | 737 ms: 1.02x faster                                                            |
| nqueens                 | 93.7 ms                                                                     | 91.8 ms: 1.02x faster                                                           |
| scimark_sor             | 103 ms                                                                      | 101 ms: 1.02x faster                                                            |
| comprehensions          | 17.4 us                                                                     | 17.1 us: 1.02x faster                                                           |
| pickle_pure_python      | 334 us                                                                      | 328 us: 1.02x faster                                                            |
| json_dumps              | 10.2 ms                                                                     | 10.0 ms: 1.02x faster                                                           |
| scimark_monte_carlo     | 63.2 ms                                                                     | 62.2 ms: 1.02x faster                                                           |
| sqlglot_v2_transpile    | 1.72 ms                                                                     | 1.69 ms: 1.02x faster                                                           |
| json_loads              | 25.4 us                                                                     | 25.1 us: 1.01x faster                                                           |
| unpickle_pure_python    | 194 us                                                                      | 191 us: 1.01x faster                                                            |
| xml_etree_process       | 55.8 ms                                                                     | 55.0 ms: 1.01x faster                                                           |
| chaos                   | 59.9 ms                                                                     | 59.1 ms: 1.01x faster                                                           |
| subparsers              | 43.0 ms                                                                     | 42.5 ms: 1.01x faster                                                           |
| regex_v8                | 23.6 ms                                                                     | 23.3 ms: 1.01x faster                                                           |
| regex_effbot            | 3.62 ms                                                                     | 3.58 ms: 1.01x faster                                                           |
| crypto_pyaes            | 77.9 ms                                                                     | 77.0 ms: 1.01x faster                                                           |
| async_generators        | 447 ms                                                                      | 443 ms: 1.01x faster                                                            |
| deltablue               | 2.89 ms                                                                     | 2.86 ms: 1.01x faster                                                           |
| django_template         | 35.3 ms                                                                     | 35.0 ms: 1.01x faster                                                           |
| sqlglot_v2_parse        | 1.32 ms                                                                     | 1.31 ms: 1.01x faster                                                           |
| async_tree_none         | 272 ms                                                                      | 270 ms: 1.01x faster                                                            |
| many_optionals          | 1.24 ms                                                                     | 1.23 ms: 1.01x faster                                                           |
| async_tree_memoization  | 329 ms                                                                      | 327 ms: 1.01x faster                                                            |
| tomli_loads             | 1.93 sec                                                                    | 1.92 sec: 1.01x faster                                                          |
| 2to3                    | 288 ms                                                                      | 286 ms: 1.01x faster                                                            |
| mako                    | 9.85 ms                                                                     | 9.79 ms: 1.01x faster                                                           |
| bpe_tokeniser           | 4.54 sec                                                                    | 4.51 sec: 1.01x faster                                                          |
| regex_compile           | 134 ms                                                                      | 133 ms: 1.01x faster                                                            |
| sympy_expand            | 505 ms                                                                      | 502 ms: 1.01x faster                                                            |
| deepcopy_memo           | 28.1 us                                                                     | 27.9 us: 1.01x faster                                                           |
| deepcopy                | 282 us                                                                      | 280 us: 1.01x faster                                                            |
| sqlglot_v2_optimize     | 58.0 ms                                                                     | 57.8 ms: 1.00x faster                                                           |
| pidigits                | 256 ms                                                                      | 255 ms: 1.00x faster                                                            |
| sympy_integrate         | 22.5 ms                                                                     | 22.4 ms: 1.00x faster                                                           |
| gc_traversal            | 6.67 ms                                                                     | 6.65 ms: 1.00x faster                                                           |
| scimark_fft             | 299 ms                                                                      | 299 ms: 1.00x faster                                                            |
| pathlib                 | 16.8 ms                                                                     | 16.8 ms: 1.00x faster                                                           |
| connected_components    | 407 ms                                                                      | 407 ms: 1.00x faster                                                            |
| thrift                  | 835 us                                                                      | 842 us: 1.01x slower                                                            |
| json                    | 5.40 ms                                                                     | 5.47 ms: 1.01x slower                                                           |
| html5lib                | 67.1 ms                                                                     | 68.1 ms: 1.01x slower                                                           |
| shortest_path           | 435 ms                                                                      | 441 ms: 1.01x slower                                                            |
| genshi_text             | 23.1 ms                                                                     | 23.4 ms: 1.02x slower                                                           |
| logging_format          | 6.42 us                                                                     | 6.52 us: 1.02x slower                                                           |
| mdp                     | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                          |
| regex_dna               | 224 ms                                                                      | 228 ms: 1.02x slower                                                            |
| coverage                | 84.8 ms                                                                     | 86.3 ms: 1.02x slower                                                           |
| raytrace                | 276 ms                                                                      | 281 ms: 1.02x slower                                                            |
| logging_simple          | 5.78 us                                                                     | 5.92 us: 1.02x slower                                                           |
| pyflate                 | 404 ms                                                                      | 414 ms: 1.03x slower                                                            |
| nbody                   | 103 ms                                                                      | 106 ms: 1.03x slower                                                            |
| genshi_xml              | 55.0 ms                                                                     | 56.6 ms: 1.03x slower                                                           |
| scimark_lu              | 94.1 ms                                                                     | 97.7 ms: 1.04x slower                                                           |
| Geometric mean          | (ref)                                                                       | 1.01x faster                                                                    |

Benchmark hidden because not significant (28): sphinx, richards_super, telco, async_tree_cpu_io_mixed, docutils, sympy_sum, sympy_str, logging_silent, deepcopy_reduce, sqlglot_v2_normalize, pycparser, async_tree_memoization_tg, djangocms, dulwich_log, python_startup_no_site, python_startup, richards, async_tree_io, create_gc_cycles, pylint, sqlite_synth, async_tree_none_tg, k_core, async_tree_cpu_io_mixed_tg, asyncio_websockets, typing_runtime_protocols, async_tree_io_tg, generators

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x