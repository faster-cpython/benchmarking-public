# Results vs. base

- fork: faster-cpython
- ref: jit_trampoline
- machine: windows-amd64
- commit hash: 14080cb
- commit date: 2025-08-19
- overall geometric mean: 1.000x faster
- HPT reliability: 68.04%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                     | 219 ms: 1.01x faster                                                           |
| docutils       | 1.68 sec                                                                   | 1.66 sec: 1.01x faster                                                         |
| html5lib       | 39.3 ms                                                                    | 38.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 210 ms                                                                     | 207 ms: 1.01x faster                                                           |
| async_generators          | 245 ms                                                                     | 247 ms: 1.01x slower                                                           |
| coroutines                | 14.2 ms                                                                    | 14.5 ms: 1.02x slower                                                          |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                                   |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                                     | 148 ms: 1.01x slower                                                           |
| nbody          | 53.4 ms                                                                    | 58.0 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                                    | 13.9 ms: 1.11x faster                                                          |
| regex_dna      | 120 ms                                                                     | 118 ms: 1.01x faster                                                           |
| regex_compile  | 78.4 ms                                                                    | 79.2 ms: 1.01x slower                                                          |
| regex_effbot   | 1.55 ms                                                                    | 1.57 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 14.7 us                                                                    | 14.0 us: 1.05x faster                                                          |
| json_dumps           | 5.40 ms                                                                    | 5.34 ms: 1.01x faster                                                          |
| unpickle_pure_python | 106 us                                                                     | 105 us: 1.01x faster                                                           |
| xml_etree_parse      | 88.0 ms                                                                    | 88.6 ms: 1.01x slower                                                          |
| tomli_loads          | 1.11 sec                                                                   | 1.12 sec: 1.01x slower                                                         |
| xml_etree_iterparse  | 63.2 ms                                                                    | 64.5 ms: 1.02x slower                                                          |
| xml_etree_process    | 35.2 ms                                                                    | 36.2 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.4 ms                                                                    | 19.0 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                                      | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 5.41 ms                                                                    | 5.34 ms: 1.01x faster                                                          |
| genshi_text    | 15.5 ms                                                                    | 15.7 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 | bm-20250819-pythonperf1-amd64-faster%2dcpython-jit_trampoline-3.15.0a0-14080cb |
|---------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8                  | 15.5 ms                                                                    | 13.9 ms: 1.11x faster                                                          |
| json_loads                | 14.7 us                                                                    | 14.0 us: 1.05x faster                                                          |
| json                      | 3.13 ms                                                                    | 3.00 ms: 1.04x faster                                                          |
| coverage                  | 51.9 ms                                                                    | 50.0 ms: 1.04x faster                                                          |
| subparsers                | 31.2 ms                                                                    | 30.3 ms: 1.03x faster                                                          |
| pycparser                 | 727 ms                                                                     | 708 ms: 1.03x faster                                                           |
| create_gc_cycles          | 1.30 ms                                                                    | 1.27 ms: 1.02x faster                                                          |
| python_startup_no_site    | 19.4 ms                                                                    | 19.0 ms: 1.02x faster                                                          |
| fannkuch                  | 214 ms                                                                     | 210 ms: 1.02x faster                                                           |
| many_optionals            | 578 us                                                                     | 569 us: 1.02x faster                                                           |
| typing_runtime_protocols  | 104 us                                                                     | 102 us: 1.02x faster                                                           |
| async_tree_memoization_tg | 210 ms                                                                     | 207 ms: 1.01x faster                                                           |
| regex_dna                 | 120 ms                                                                     | 118 ms: 1.01x faster                                                           |
| comprehensions            | 10.7 us                                                                    | 10.5 us: 1.01x faster                                                          |
| mako                      | 5.41 ms                                                                    | 5.34 ms: 1.01x faster                                                          |
| sqlglot_v2_optimize       | 34.9 ms                                                                    | 34.5 ms: 1.01x faster                                                          |
| json_dumps                | 5.40 ms                                                                    | 5.34 ms: 1.01x faster                                                          |
| gc_traversal              | 2.12 ms                                                                    | 2.10 ms: 1.01x faster                                                          |
| mdp                       | 811 ms                                                                     | 802 ms: 1.01x faster                                                           |
| docutils                  | 1.68 sec                                                                   | 1.66 sec: 1.01x faster                                                         |
| 2to3                      | 221 ms                                                                     | 219 ms: 1.01x faster                                                           |
| unpickle_pure_python      | 106 us                                                                     | 105 us: 1.01x faster                                                           |
| html5lib                  | 39.3 ms                                                                    | 38.9 ms: 1.01x faster                                                          |
| sympy_str                 | 172 ms                                                                     | 170 ms: 1.01x faster                                                           |
| deepcopy_memo             | 18.2 us                                                                    | 18.0 us: 1.01x faster                                                          |
| sqlite_synth              | 1.55 us                                                                    | 1.54 us: 1.01x faster                                                          |
| crypto_pyaes              | 45.6 ms                                                                    | 45.5 ms: 1.00x faster                                                          |
| logging_simple            | 5.95 us                                                                    | 5.97 us: 1.00x slower                                                          |
| scimark_sor               | 76.5 ms                                                                    | 76.9 ms: 1.00x slower                                                          |
| sympy_integrate           | 12.7 ms                                                                    | 12.8 ms: 1.01x slower                                                          |
| spectral_norm             | 64.9 ms                                                                    | 65.3 ms: 1.01x slower                                                          |
| async_generators          | 245 ms                                                                     | 247 ms: 1.01x slower                                                           |
| xml_etree_parse           | 88.0 ms                                                                    | 88.6 ms: 1.01x slower                                                          |
| pidigits                  | 146 ms                                                                     | 148 ms: 1.01x slower                                                           |
| logging_silent            | 53.8 ns                                                                    | 54.3 ns: 1.01x slower                                                          |
| raytrace                  | 181 ms                                                                     | 183 ms: 1.01x slower                                                           |
| regex_compile             | 78.4 ms                                                                    | 79.2 ms: 1.01x slower                                                          |
| sympy_expand              | 295 ms                                                                     | 298 ms: 1.01x slower                                                           |
| logging_format            | 6.38 us                                                                    | 6.45 us: 1.01x slower                                                          |
| regex_effbot              | 1.55 ms                                                                    | 1.57 ms: 1.01x slower                                                          |
| scimark_monte_carlo       | 39.7 ms                                                                    | 40.2 ms: 1.01x slower                                                          |
| tomli_loads               | 1.11 sec                                                                   | 1.12 sec: 1.01x slower                                                         |
| meteor_contest            | 70.5 ms                                                                    | 71.4 ms: 1.01x slower                                                          |
| deltablue                 | 2.19 ms                                                                    | 2.22 ms: 1.01x slower                                                          |
| deepcopy                  | 169 us                                                                     | 171 us: 1.01x slower                                                           |
| deepcopy_reduce           | 1.84 us                                                                    | 1.87 us: 1.02x slower                                                          |
| scimark_lu                | 60.1 ms                                                                    | 61.1 ms: 1.02x slower                                                          |
| hexiom                    | 4.00 ms                                                                    | 4.06 ms: 1.02x slower                                                          |
| genshi_text               | 15.5 ms                                                                    | 15.7 ms: 1.02x slower                                                          |
| xml_etree_iterparse       | 63.2 ms                                                                    | 64.5 ms: 1.02x slower                                                          |
| coroutines                | 14.2 ms                                                                    | 14.5 ms: 1.02x slower                                                          |
| go                        | 76.0 ms                                                                    | 77.8 ms: 1.02x slower                                                          |
| bpe_tokeniser             | 2.52 sec                                                                   | 2.59 sec: 1.03x slower                                                         |
| richards_super            | 30.5 ms                                                                    | 31.3 ms: 1.03x slower                                                          |
| xml_etree_process         | 35.2 ms                                                                    | 36.2 ms: 1.03x slower                                                          |
| pprint_pformat            | 865 ms                                                                     | 890 ms: 1.03x slower                                                           |
| richards                  | 26.8 ms                                                                    | 27.9 ms: 1.04x slower                                                          |
| pprint_safe_repr          | 423 ms                                                                     | 440 ms: 1.04x slower                                                           |
| nbody                     | 53.4 ms                                                                    | 58.0 ms: 1.09x slower                                                          |
| Geometric mean            | (ref)                                                                      | 1.00x slower                                                                   |

Benchmark hidden because not significant (33): pyflate, sympy_sum, asyncio_websockets, nqueens, sqlglot_v2_normalize, shortest_path, generators, django_template, sphinx, connected_components, telco, k_core, dulwich_log, python_startup, thrift, async_tree_memoization, sqlglot_v2_transpile, scimark_fft, scimark_sparse_mat_mult, pickle_pure_python, float, chaos, async_tree_cpu_io_mixed, async_tree_none_tg, xml_etree_generate, sqlglot_v2_parse, pathlib, pylint, async_tree_none, async_tree_cpu_io_mixed_tg, genshi_xml, async_tree_io_tg, async_tree_io

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 68.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown