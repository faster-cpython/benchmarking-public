# Results vs. base

- fork: brandtbucher
- ref: msvc_musttail
- machine: windows-amd64
- commit hash: 06bc3bd
- commit date: 2025-03-07
- overall geometric mean: 1.008x faster
- HPT reliability: 97.03%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                      | 229 ms: 1.01x slower                                                       |
| docutils       | 1.68 sec                                                                    | 1.71 sec: 1.02x slower                                                     |
| html5lib       | 40.8 ms                                                                     | 40.1 ms: 1.02x faster                                                      |
| sphinx         | 658 ms                                                                      | 669 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines                 | 13.5 ms                                                                     | 13.1 ms: 1.03x faster                                                      |
| async_generators           | 226 ms                                                                      | 221 ms: 1.03x faster                                                       |
| asyncio_websockets         | 318 ms                                                                      | 315 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 343 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                       |
| async_tree_io_tg           | 410 ms                                                                      | 417 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 74.1 ms                                                                     | 67.9 ms: 1.09x faster                                                      |
| float          | 47.8 ms                                                                     | 44.8 ms: 1.06x faster                                                      |
| pidigits       | 152 ms                                                                      | 151 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 13.5 ms                                                                     | 13.2 ms: 1.03x faster                                                      |
| regex_compile  | 88.2 ms                                                                     | 87.2 ms: 1.01x faster                                                      |
| regex_dna      | 112 ms                                                                      | 113 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                                    | 1.39 sec: 1.05x faster                                                     |
| xml_etree_process    | 41.5 ms                                                                     | 39.9 ms: 1.04x faster                                                      |
| xml_etree_generate   | 58.7 ms                                                                     | 56.7 ms: 1.04x faster                                                      |
| unpickle_pure_python | 155 us                                                                      | 150 us: 1.03x faster                                                       |
| pickle_pure_python   | 237 us                                                                      | 230 us: 1.03x faster                                                       |
| json_dumps           | 7.05 ms                                                                     | 6.86 ms: 1.03x faster                                                      |
| xml_etree_parse      | 91.2 ms                                                                     | 92.2 ms: 1.01x slower                                                      |
| json_loads           | 14.7 us                                                                     | 15.1 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 19.8 ms                                                                     | 19.5 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.86 ms                                                                     | 6.79 ms: 1.01x faster                                                      |
| django_template | 25.1 ms                                                                     | 25.7 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 | bm-20250307-pythonperf1-amd64-brandtbucher-msvc_musttail-3.14.0a5+-06bc3bd |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent             | 65.2 ns                                                                     | 59.0 ns: 1.11x faster                                                      |
| nbody                      | 74.1 ms                                                                     | 67.9 ms: 1.09x faster                                                      |
| scimark_sor                | 91.0 ms                                                                     | 84.2 ms: 1.08x faster                                                      |
| scimark_fft                | 192 ms                                                                      | 180 ms: 1.07x faster                                                       |
| float                      | 47.8 ms                                                                     | 44.8 ms: 1.06x faster                                                      |
| spectral_norm              | 61.5 ms                                                                     | 57.8 ms: 1.06x faster                                                      |
| chaos                      | 43.6 ms                                                                     | 41.1 ms: 1.06x faster                                                      |
| deepcopy_memo              | 21.0 us                                                                     | 19.9 us: 1.06x faster                                                      |
| tomli_loads                | 1.47 sec                                                                    | 1.39 sec: 1.05x faster                                                     |
| fannkuch                   | 296 ms                                                                      | 282 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 558 ms                                                                      | 533 ms: 1.05x faster                                                       |
| scimark_lu                 | 66.9 ms                                                                     | 64.1 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 47.1 ms                                                                     | 45.2 ms: 1.04x faster                                                      |
| xml_etree_process          | 41.5 ms                                                                     | 39.9 ms: 1.04x faster                                                      |
| pprint_pformat             | 1.13 sec                                                                    | 1.08 sec: 1.04x faster                                                     |
| xml_etree_generate         | 58.7 ms                                                                     | 56.7 ms: 1.04x faster                                                      |
| deepcopy                   | 190 us                                                                      | 183 us: 1.04x faster                                                       |
| unpickle_pure_python       | 155 us                                                                      | 150 us: 1.03x faster                                                       |
| json                       | 3.14 ms                                                                     | 3.04 ms: 1.03x faster                                                      |
| pickle_pure_python         | 237 us                                                                      | 230 us: 1.03x faster                                                       |
| coroutines                 | 13.5 ms                                                                     | 13.1 ms: 1.03x faster                                                      |
| mdp                        | 1.64 sec                                                                    | 1.59 sec: 1.03x faster                                                     |
| json_dumps                 | 7.05 ms                                                                     | 6.86 ms: 1.03x faster                                                      |
| async_generators           | 226 ms                                                                      | 221 ms: 1.03x faster                                                       |
| regex_v8                   | 13.5 ms                                                                     | 13.2 ms: 1.03x faster                                                      |
| hexiom                     | 4.38 ms                                                                     | 4.28 ms: 1.02x faster                                                      |
| go                         | 88.6 ms                                                                     | 86.6 ms: 1.02x faster                                                      |
| telco                      | 4.89 ms                                                                     | 4.78 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.72 ms                                                                     | 2.66 ms: 1.02x faster                                                      |
| bpe_tokeniser              | 2.96 sec                                                                    | 2.90 sec: 1.02x faster                                                     |
| logging_format             | 7.03 us                                                                     | 6.88 us: 1.02x faster                                                      |
| logging_simple             | 6.53 us                                                                     | 6.41 us: 1.02x faster                                                      |
| crypto_pyaes               | 50.0 ms                                                                     | 49.1 ms: 1.02x faster                                                      |
| html5lib                   | 40.8 ms                                                                     | 40.1 ms: 1.02x faster                                                      |
| python_startup_no_site     | 19.8 ms                                                                     | 19.5 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 1.94 us                                                                     | 1.91 us: 1.02x faster                                                      |
| dulwich_log                | 43.4 ms                                                                     | 42.8 ms: 1.01x faster                                                      |
| sqlglot_v2_parse           | 892 us                                                                      | 882 us: 1.01x faster                                                       |
| sympy_expand               | 302 ms                                                                      | 299 ms: 1.01x faster                                                       |
| regex_compile              | 88.2 ms                                                                     | 87.2 ms: 1.01x faster                                                      |
| pyflate                    | 315 ms                                                                      | 312 ms: 1.01x faster                                                       |
| bench_mp_pool              | 88.7 ms                                                                     | 87.8 ms: 1.01x faster                                                      |
| pidigits                   | 152 ms                                                                      | 151 ms: 1.01x faster                                                       |
| asyncio_websockets         | 318 ms                                                                      | 315 ms: 1.01x faster                                                       |
| mako                       | 6.86 ms                                                                     | 6.79 ms: 1.01x faster                                                      |
| sqlglot_v2_transpile       | 1.10 ms                                                                     | 1.09 ms: 1.01x faster                                                      |
| nqueens                    | 63.6 ms                                                                     | 63.1 ms: 1.01x faster                                                      |
| sympy_sum                  | 90.5 ms                                                                     | 90.0 ms: 1.01x faster                                                      |
| regex_dna                  | 112 ms                                                                      | 113 ms: 1.01x slower                                                       |
| 2to3                       | 227 ms                                                                      | 229 ms: 1.01x slower                                                       |
| xml_etree_parse            | 91.2 ms                                                                     | 92.2 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed    | 339 ms                                                                      | 343 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                       |
| raytrace                   | 191 ms                                                                      | 193 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 106 us                                                                      | 108 us: 1.02x slower                                                       |
| many_optionals             | 438 us                                                                      | 445 us: 1.02x slower                                                       |
| sphinx                     | 658 ms                                                                      | 669 ms: 1.02x slower                                                       |
| subparsers                 | 16.1 ms                                                                     | 16.4 ms: 1.02x slower                                                      |
| sqlglot_v2_normalize       | 73.6 ms                                                                     | 74.9 ms: 1.02x slower                                                      |
| docutils                   | 1.68 sec                                                                    | 1.71 sec: 1.02x slower                                                     |
| async_tree_io_tg           | 410 ms                                                                      | 417 ms: 1.02x slower                                                       |
| comprehensions             | 11.3 us                                                                     | 11.5 us: 1.02x slower                                                      |
| django_template            | 25.1 ms                                                                     | 25.7 ms: 1.02x slower                                                      |
| json_loads                 | 14.7 us                                                                     | 15.1 us: 1.03x slower                                                      |
| pylint                     | 201 ms                                                                      | 207 ms: 1.03x slower                                                       |
| generators                 | 19.3 ms                                                                     | 20.1 ms: 1.04x slower                                                      |
| coverage                   | 46.8 ms                                                                     | 49.1 ms: 1.05x slower                                                      |
| richards_super             | 35.1 ms                                                                     | 40.6 ms: 1.16x slower                                                      |
| richards                   | 30.7 ms                                                                     | 35.6 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (25): bench_thread_pool, k_core, gc_traversal, python_startup, thrift, xml_etree_iterparse, pathlib, sqlite_synth, regex_effbot, sympy_str, create_gc_cycles, sympy_integrate, genshi_text, meteor_contest, shortest_path, connected_components, deltablue, async_tree_none, genshi_xml, sqlglot_v2_optimize, async_tree_memoization, async_tree_io, async_tree_none_tg, pycparser, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 97.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown