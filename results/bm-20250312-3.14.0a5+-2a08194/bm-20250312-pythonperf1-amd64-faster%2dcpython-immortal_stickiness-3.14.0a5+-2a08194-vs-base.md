# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.004x slower
- HPT reliability: 99.38%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.68 sec                                                                    | 1.69 sec: 1.01x slower                                                               |
| html5lib       | 39.8 ms                                                                     | 40.7 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|--------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_none_tg | 178 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| asyncio_websockets | 295 ms                                                                      | 304 ms: 1.03x slower                                                                 |
| Geometric mean     | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (9): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_generators, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                      | 152 ms: 1.01x slower                                                                 |
| nbody          | 65.7 ms                                                                     | 67.4 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                      | 111 ms: 1.06x faster                                                                 |
| regex_v8       | 13.9 ms                                                                     | 13.2 ms: 1.05x faster                                                                |
| regex_effbot   | 1.47 ms                                                                     | 1.40 ms: 1.05x faster                                                                |
| regex_compile  | 85.8 ms                                                                     | 86.5 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.04x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                                     | 90.9 ms: 1.03x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                                     | 64.0 ms: 1.01x faster                                                                |
| unpickle_pure_python | 149 us                                                                      | 150 us: 1.01x slower                                                                 |
| json_loads           | 14.7 us                                                                     | 14.8 us: 1.01x slower                                                                |
| xml_etree_generate   | 58.1 ms                                                                     | 59.2 ms: 1.02x slower                                                                |
| xml_etree_process    | 41.2 ms                                                                     | 42.4 ms: 1.03x slower                                                                |
| json_dumps           | 6.61 ms                                                                     | 7.02 ms: 1.06x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 20.4 ms                                                                     | 20.5 ms: 1.01x slower                                                                |
| python_startup         | 25.9 ms                                                                     | 26.4 ms: 1.02x slower                                                                |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text    | 17.6 ms                                                                     | 17.4 ms: 1.01x faster                                                                |
| mako           | 6.85 ms                                                                     | 6.96 ms: 1.02x slower                                                                |
| genshi_xml     | 38.0 ms                                                                     | 39.1 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20250312-pythonperf1-amd64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna               | 117 ms                                                                      | 111 ms: 1.06x faster                                                                 |
| regex_v8                | 13.9 ms                                                                     | 13.2 ms: 1.05x faster                                                                |
| regex_effbot            | 1.47 ms                                                                     | 1.40 ms: 1.05x faster                                                                |
| deepcopy_memo           | 19.8 us                                                                     | 19.3 us: 1.03x faster                                                                |
| xml_etree_parse         | 93.2 ms                                                                     | 90.9 ms: 1.03x faster                                                                |
| scimark_lu              | 59.5 ms                                                                     | 58.2 ms: 1.02x faster                                                                |
| deepcopy                | 184 us                                                                      | 180 us: 1.02x faster                                                                 |
| connected_components    | 342 ms                                                                      | 336 ms: 1.02x faster                                                                 |
| sqlglot_v2_normalize    | 75.7 ms                                                                     | 74.2 ms: 1.02x faster                                                                |
| sqlglot_v2_parse        | 914 us                                                                      | 898 us: 1.02x faster                                                                 |
| subparsers              | 16.8 ms                                                                     | 16.5 ms: 1.02x faster                                                                |
| xml_etree_iterparse     | 65.0 ms                                                                     | 64.0 ms: 1.01x faster                                                                |
| shortest_path           | 370 ms                                                                      | 365 ms: 1.01x faster                                                                 |
| logging_silent          | 59.1 ns                                                                     | 58.4 ns: 1.01x faster                                                                |
| genshi_text             | 17.6 ms                                                                     | 17.4 ms: 1.01x faster                                                                |
| async_tree_none_tg      | 178 ms                                                                      | 177 ms: 1.01x faster                                                                 |
| spectral_norm           | 57.1 ms                                                                     | 56.6 ms: 1.01x faster                                                                |
| create_gc_cycles        | 1.25 ms                                                                     | 1.24 ms: 1.01x faster                                                                |
| generators              | 19.4 ms                                                                     | 19.3 ms: 1.01x faster                                                                |
| sqlglot_v2_transpile    | 1.12 ms                                                                     | 1.11 ms: 1.01x faster                                                                |
| docutils                | 1.68 sec                                                                    | 1.69 sec: 1.01x slower                                                               |
| pidigits                | 151 ms                                                                      | 152 ms: 1.01x slower                                                                 |
| crypto_pyaes            | 50.4 ms                                                                     | 50.7 ms: 1.01x slower                                                                |
| sympy_integrate         | 13.2 ms                                                                     | 13.3 ms: 1.01x slower                                                                |
| python_startup_no_site  | 20.4 ms                                                                     | 20.5 ms: 1.01x slower                                                                |
| sympy_expand            | 300 ms                                                                      | 303 ms: 1.01x slower                                                                 |
| unpickle_pure_python    | 149 us                                                                      | 150 us: 1.01x slower                                                                 |
| thrift                  | 529 us                                                                      | 533 us: 1.01x slower                                                                 |
| hexiom                  | 4.36 ms                                                                     | 4.39 ms: 1.01x slower                                                                |
| many_optionals          | 436 us                                                                      | 440 us: 1.01x slower                                                                 |
| regex_compile           | 85.8 ms                                                                     | 86.5 ms: 1.01x slower                                                                |
| json_loads              | 14.7 us                                                                     | 14.8 us: 1.01x slower                                                                |
| scimark_fft             | 178 ms                                                                      | 180 ms: 1.01x slower                                                                 |
| sympy_str               | 175 ms                                                                      | 177 ms: 1.01x slower                                                                 |
| logging_simple          | 6.46 us                                                                     | 6.54 us: 1.01x slower                                                                |
| bpe_tokeniser           | 2.99 sec                                                                    | 3.03 sec: 1.01x slower                                                               |
| json                    | 3.01 ms                                                                     | 3.05 ms: 1.01x slower                                                                |
| nqueens                 | 64.5 ms                                                                     | 65.4 ms: 1.01x slower                                                                |
| sympy_sum               | 89.1 ms                                                                     | 90.4 ms: 1.01x slower                                                                |
| dulwich_log             | 42.2 ms                                                                     | 42.8 ms: 1.01x slower                                                                |
| scimark_monte_carlo     | 43.4 ms                                                                     | 44.0 ms: 1.02x slower                                                                |
| mako                    | 6.85 ms                                                                     | 6.96 ms: 1.02x slower                                                                |
| python_startup          | 25.9 ms                                                                     | 26.4 ms: 1.02x slower                                                                |
| richards_super          | 33.0 ms                                                                     | 33.7 ms: 1.02x slower                                                                |
| xml_etree_generate      | 58.1 ms                                                                     | 59.2 ms: 1.02x slower                                                                |
| logging_format          | 6.93 us                                                                     | 7.07 us: 1.02x slower                                                                |
| html5lib                | 39.8 ms                                                                     | 40.7 ms: 1.02x slower                                                                |
| chaos                   | 43.1 ms                                                                     | 44.1 ms: 1.02x slower                                                                |
| nbody                   | 65.7 ms                                                                     | 67.4 ms: 1.03x slower                                                                |
| scimark_sparse_mat_mult | 2.49 ms                                                                     | 2.56 ms: 1.03x slower                                                                |
| pyflate                 | 306 ms                                                                      | 314 ms: 1.03x slower                                                                 |
| genshi_xml              | 38.0 ms                                                                     | 39.1 ms: 1.03x slower                                                                |
| xml_etree_process       | 41.2 ms                                                                     | 42.4 ms: 1.03x slower                                                                |
| asyncio_websockets      | 295 ms                                                                      | 304 ms: 1.03x slower                                                                 |
| go                      | 87.8 ms                                                                     | 90.8 ms: 1.03x slower                                                                |
| richards                | 28.9 ms                                                                     | 30.2 ms: 1.05x slower                                                                |
| coverage                | 47.1 ms                                                                     | 49.4 ms: 1.05x slower                                                                |
| fannkuch                | 267 ms                                                                      | 282 ms: 1.05x slower                                                                 |
| json_dumps              | 6.61 ms                                                                     | 7.02 ms: 1.06x slower                                                                |
| mdp                     | 1.48 sec                                                                    | 1.58 sec: 1.07x slower                                                               |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (34): async_tree_io_tg, gc_traversal, raytrace, django_template, deepcopy_reduce, async_tree_cpu_io_mixed_tg, sqlglot_v2_optimize, scimark_sor, async_tree_io, bench_mp_pool, k_core, coroutines, float, pprint_pformat, tomli_loads, deltablue, telco, pprint_safe_repr, sphinx, sqlite_synth, async_tree_memoization_tg, async_tree_cpu_io_mixed, meteor_contest, async_generators, pylint, bench_thread_pool, pathlib, comprehensions, typing_runtime_protocols, async_tree_none, async_tree_memoization, pycparser, 2to3, pickle_pure_python

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown