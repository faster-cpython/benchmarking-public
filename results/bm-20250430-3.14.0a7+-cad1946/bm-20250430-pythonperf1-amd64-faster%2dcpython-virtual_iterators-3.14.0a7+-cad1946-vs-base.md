# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.004x slower
- HPT reliability: 96.46%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                    | 1.65 sec: 1.01x slower                                                             |
| html5lib       | 37.4 ms                                                                     | 38.9 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets      | 160 ms                                                                      | 157 ms: 1.02x faster                                                               |
| async_tree_cpu_io_mixed | 337 ms                                                                      | 334 ms: 1.01x faster                                                               |
| async_tree_none         | 181 ms                                                                      | 180 ms: 1.01x faster                                                               |
| async_generators        | 228 ms                                                                      | 232 ms: 1.02x slower                                                               |
| Geometric mean          | (ref)                                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 43.5 ms                                                                     | 44.0 ms: 1.01x slower                                                              |
| nbody          | 62.9 ms                                                                     | 63.7 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 14.8 ms                                                                     | 14.2 ms: 1.04x faster                                                              |
| regex_compile  | 79.8 ms                                                                     | 80.4 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 89.6 ms                                                                     | 88.7 ms: 1.01x faster                                                              |
| xml_etree_process    | 39.3 ms                                                                     | 39.7 ms: 1.01x slower                                                              |
| pickle_pure_python   | 209 us                                                                      | 212 us: 1.01x slower                                                               |
| xml_etree_iterparse  | 62.7 ms                                                                     | 63.6 ms: 1.01x slower                                                              |
| json_dumps           | 6.83 ms                                                                     | 6.96 ms: 1.02x slower                                                              |
| unpickle_pure_python | 132 us                                                                      | 139 us: 1.05x slower                                                               |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (3): tomli_loads, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 26.5 ms                                                                     | 26.2 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 15.0 ms                                                                     | 14.7 ms: 1.02x faster                                                              |
| mako            | 6.49 ms                                                                     | 6.54 ms: 1.01x slower                                                              |
| django_template | 24.2 ms                                                                     | 24.4 ms: 1.01x slower                                                              |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|--------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 109 us                                                                      | 100 us: 1.09x faster                                                               |
| comprehensions           | 11.1 us                                                                     | 10.6 us: 1.05x faster                                                              |
| regex_v8                 | 14.8 ms                                                                     | 14.2 ms: 1.04x faster                                                              |
| deepcopy                 | 172 us                                                                      | 167 us: 1.03x faster                                                               |
| sqlglot_v2_normalize     | 71.0 ms                                                                     | 69.4 ms: 1.02x faster                                                              |
| subparsers               | 16.0 ms                                                                     | 15.7 ms: 1.02x faster                                                              |
| meteor_contest           | 72.2 ms                                                                     | 70.7 ms: 1.02x faster                                                              |
| asyncio_websockets       | 160 ms                                                                      | 157 ms: 1.02x faster                                                               |
| json                     | 3.14 ms                                                                     | 3.08 ms: 1.02x faster                                                              |
| sqlglot_v2_optimize      | 34.2 ms                                                                     | 33.6 ms: 1.02x faster                                                              |
| genshi_text              | 15.0 ms                                                                     | 14.7 ms: 1.02x faster                                                              |
| mdp                      | 790 ms                                                                      | 777 ms: 1.02x faster                                                               |
| pathlib                  | 32.6 ms                                                                     | 32.1 ms: 1.02x faster                                                              |
| generators               | 19.6 ms                                                                     | 19.3 ms: 1.02x faster                                                              |
| deepcopy_memo            | 18.4 us                                                                     | 18.2 us: 1.01x faster                                                              |
| raytrace                 | 178 ms                                                                      | 176 ms: 1.01x faster                                                               |
| python_startup           | 26.5 ms                                                                     | 26.2 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed  | 337 ms                                                                      | 334 ms: 1.01x faster                                                               |
| xml_etree_parse          | 89.6 ms                                                                     | 88.7 ms: 1.01x faster                                                              |
| async_tree_none          | 181 ms                                                                      | 180 ms: 1.01x faster                                                               |
| hexiom                   | 3.97 ms                                                                     | 3.95 ms: 1.01x faster                                                              |
| many_optionals           | 422 us                                                                      | 420 us: 1.01x faster                                                               |
| scimark_monte_carlo      | 40.7 ms                                                                     | 40.5 ms: 1.00x faster                                                              |
| logging_silent           | 55.1 ns                                                                     | 55.4 ns: 1.01x slower                                                              |
| sqlglot_v2_parse         | 809 us                                                                      | 814 us: 1.01x slower                                                               |
| fannkuch                 | 250 ms                                                                      | 251 ms: 1.01x slower                                                               |
| pprint_safe_repr         | 491 ms                                                                      | 494 ms: 1.01x slower                                                               |
| regex_compile            | 79.8 ms                                                                     | 80.4 ms: 1.01x slower                                                              |
| docutils                 | 1.64 sec                                                                    | 1.65 sec: 1.01x slower                                                             |
| mako                     | 6.49 ms                                                                     | 6.54 ms: 1.01x slower                                                              |
| django_template          | 24.2 ms                                                                     | 24.4 ms: 1.01x slower                                                              |
| sqlite_synth             | 1.56 us                                                                     | 1.58 us: 1.01x slower                                                              |
| float                    | 43.5 ms                                                                     | 44.0 ms: 1.01x slower                                                              |
| chaos                    | 38.7 ms                                                                     | 39.1 ms: 1.01x slower                                                              |
| xml_etree_process        | 39.3 ms                                                                     | 39.7 ms: 1.01x slower                                                              |
| go                       | 76.3 ms                                                                     | 77.3 ms: 1.01x slower                                                              |
| pickle_pure_python       | 209 us                                                                      | 212 us: 1.01x slower                                                               |
| nbody                    | 62.9 ms                                                                     | 63.7 ms: 1.01x slower                                                              |
| xml_etree_iterparse      | 62.7 ms                                                                     | 63.6 ms: 1.01x slower                                                              |
| pyflate                  | 272 ms                                                                      | 276 ms: 1.01x slower                                                               |
| deepcopy_reduce          | 1.82 us                                                                     | 1.84 us: 1.01x slower                                                              |
| richards                 | 27.0 ms                                                                     | 27.5 ms: 1.02x slower                                                              |
| scimark_sor              | 74.4 ms                                                                     | 75.7 ms: 1.02x slower                                                              |
| bpe_tokeniser            | 2.85 sec                                                                    | 2.90 sec: 1.02x slower                                                             |
| async_generators         | 228 ms                                                                      | 232 ms: 1.02x slower                                                               |
| json_dumps               | 6.83 ms                                                                     | 6.96 ms: 1.02x slower                                                              |
| logging_simple           | 6.16 us                                                                     | 6.30 us: 1.02x slower                                                              |
| richards_super           | 30.7 ms                                                                     | 31.4 ms: 1.02x slower                                                              |
| logging_format           | 6.65 us                                                                     | 6.83 us: 1.03x slower                                                              |
| coverage                 | 49.3 ms                                                                     | 51.2 ms: 1.04x slower                                                              |
| html5lib                 | 37.4 ms                                                                     | 38.9 ms: 1.04x slower                                                              |
| scimark_sparse_mat_mult  | 2.50 ms                                                                     | 2.61 ms: 1.05x slower                                                              |
| unpickle_pure_python     | 132 us                                                                      | 139 us: 1.05x slower                                                               |
| deltablue                | 2.08 ms                                                                     | 2.20 ms: 1.06x slower                                                              |
| scimark_fft              | 174 ms                                                                      | 188 ms: 1.08x slower                                                               |
| scimark_lu               | 55.7 ms                                                                     | 62.8 ms: 1.13x slower                                                              |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (32): k_core, sphinx, async_tree_io, regex_effbot, genshi_xml, python_startup_no_site, async_tree_io_tg, spectral_norm, async_tree_cpu_io_mixed_tg, pprint_pformat, gc_traversal, nqueens, regex_dna, dulwich_log, shortest_path, coroutines, create_gc_cycles, async_tree_none_tg, tomli_loads, connected_components, sqlglot_v2_transpile, bench_mp_pool, telco, pidigits, crypto_pyaes, async_tree_memoization, bench_thread_pool, 2to3, json_loads, xml_etree_generate, async_tree_memoization_tg, pycparser
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 96.46% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown