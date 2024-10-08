# Results vs. base

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: ade1f65
- commit date: 2024-08-15
- overall geometric mean: 1.01x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                        |
| tornado_http   | 89.9 ms                                                               | 90.1 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| asyncio_tcp            | 484 ms                                                                | 479 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl        | 1.78 sec                                                              | 1.78 sec: 1.00x slower                                                        |
| asyncio_websockets     | 558 ms                                                                | 561 ms: 1.01x slower                                                          |
| async_tree_none        | 323 ms                                                                | 327 ms: 1.01x slower                                                          |
| async_generators       | 438 ms                                                                | 444 ms: 1.01x slower                                                          |
| async_tree_memoization | 407 ms                                                                | 425 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (7): coroutines, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                          |
| nbody          | 85.7 ms                                                               | 86.9 ms: 1.01x slower                                                         |
| float          | 77.9 ms                                                               | 79.8 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.66 ms                                                               | 3.61 ms: 1.02x faster                                                         |
| regex_dna      | 225 ms                                                                | 222 ms: 1.01x faster                                                          |
| regex_compile  | 130 ms                                                                | 131 ms: 1.01x slower                                                          |
| regex_v8       | 24.3 ms                                                               | 26.1 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                                        |
| pickle_pure_python   | 302 us                                                                | 306 us: 1.01x slower                                                          |
| unpickle_pure_python | 213 us                                                                | 217 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (6): xml_etree_parse, json_loads, xml_etree_process, xml_etree_iterparse, json_dumps, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                               | 7.03 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text    | 23.1 ms                                                               | 23.2 ms: 1.01x slower                                                         |
| mako           | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                         |
| genshi_xml     | 49.8 ms                                                               | 50.5 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240815-linux-x86_64-python-b106cf8d978b32b04a43-3.14.0a0-b106cf8 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| spectral_norm           | 113 ms                                                                | 109 ms: 1.03x faster                                                          |
| telco                   | 8.34 ms                                                               | 8.16 ms: 1.02x faster                                                         |
| fannkuch                | 405 ms                                                                | 396 ms: 1.02x faster                                                          |
| regex_effbot            | 3.66 ms                                                               | 3.61 ms: 1.02x faster                                                         |
| regex_dna               | 225 ms                                                                | 222 ms: 1.01x faster                                                          |
| coverage                | 85.8 ms                                                               | 84.7 ms: 1.01x faster                                                         |
| asyncio_tcp             | 484 ms                                                                | 479 ms: 1.01x faster                                                          |
| json                    | 5.32 ms                                                               | 5.27 ms: 1.01x faster                                                         |
| pathlib                 | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                         |
| pidigits                | 187 ms                                                                | 187 ms: 1.00x faster                                                          |
| mdp                     | 2.54 sec                                                              | 2.54 sec: 1.00x faster                                                        |
| richards                | 46.6 ms                                                               | 46.4 ms: 1.00x faster                                                         |
| bench_thread_pool       | 787 us                                                                | 785 us: 1.00x faster                                                          |
| sympy_integrate         | 19.8 ms                                                               | 19.8 ms: 1.00x faster                                                         |
| python_startup_no_site  | 7.03 ms                                                               | 7.03 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl         | 1.78 sec                                                              | 1.78 sec: 1.00x slower                                                        |
| tornado_http            | 89.9 ms                                                               | 90.1 ms: 1.00x slower                                                         |
| sqlglot_normalize       | 107 ms                                                                | 108 ms: 1.00x slower                                                          |
| sympy_sum               | 150 ms                                                                | 151 ms: 1.00x slower                                                          |
| richards_super          | 52.6 ms                                                               | 52.8 ms: 1.00x slower                                                         |
| asyncio_websockets      | 558 ms                                                                | 561 ms: 1.01x slower                                                          |
| genshi_text             | 23.1 ms                                                               | 23.2 ms: 1.01x slower                                                         |
| sqlglot_optimize        | 53.5 ms                                                               | 53.8 ms: 1.01x slower                                                         |
| docutils                | 2.70 sec                                                              | 2.72 sec: 1.01x slower                                                        |
| nqueens                 | 78.6 ms                                                               | 79.2 ms: 1.01x slower                                                         |
| mako                    | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                         |
| crypto_pyaes            | 72.5 ms                                                               | 73.1 ms: 1.01x slower                                                         |
| meteor_contest          | 106 ms                                                                | 107 ms: 1.01x slower                                                          |
| sqlglot_transpile       | 1.57 ms                                                               | 1.58 ms: 1.01x slower                                                         |
| sqlglot_parse           | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                         |
| thrift                  | 775 us                                                                | 783 us: 1.01x slower                                                          |
| create_gc_cycles        | 1.73 ms                                                               | 1.75 ms: 1.01x slower                                                         |
| regex_compile           | 130 ms                                                                | 131 ms: 1.01x slower                                                          |
| raytrace                | 257 ms                                                                | 259 ms: 1.01x slower                                                          |
| tomli_loads             | 2.07 sec                                                              | 2.09 sec: 1.01x slower                                                        |
| go                      | 140 ms                                                                | 142 ms: 1.01x slower                                                          |
| scimark_lu              | 113 ms                                                                | 114 ms: 1.01x slower                                                          |
| hexiom                  | 6.10 ms                                                               | 6.17 ms: 1.01x slower                                                         |
| pickle_pure_python      | 302 us                                                                | 306 us: 1.01x slower                                                          |
| sympy_str               | 271 ms                                                                | 274 ms: 1.01x slower                                                          |
| async_tree_none         | 323 ms                                                                | 327 ms: 1.01x slower                                                          |
| async_generators        | 438 ms                                                                | 444 ms: 1.01x slower                                                          |
| nbody                   | 85.7 ms                                                               | 86.9 ms: 1.01x slower                                                         |
| comprehensions          | 16.5 us                                                               | 16.7 us: 1.01x slower                                                         |
| genshi_xml              | 49.8 ms                                                               | 50.5 ms: 1.02x slower                                                         |
| deltablue               | 3.20 ms                                                               | 3.25 ms: 1.02x slower                                                         |
| scimark_monte_carlo     | 67.4 ms                                                               | 68.6 ms: 1.02x slower                                                         |
| unpickle_pure_python    | 213 us                                                                | 217 us: 1.02x slower                                                          |
| generators              | 28.0 ms                                                               | 28.6 ms: 1.02x slower                                                         |
| pprint_safe_repr        | 738 ms                                                                | 754 ms: 1.02x slower                                                          |
| pprint_pformat          | 1.51 sec                                                              | 1.54 sec: 1.02x slower                                                        |
| deepcopy                | 261 us                                                                | 267 us: 1.02x slower                                                          |
| float                   | 77.9 ms                                                               | 79.8 ms: 1.02x slower                                                         |
| scimark_sor             | 125 ms                                                                | 129 ms: 1.03x slower                                                          |
| deepcopy_memo           | 29.7 us                                                               | 30.9 us: 1.04x slower                                                         |
| async_tree_memoization  | 407 ms                                                                | 425 ms: 1.05x slower                                                          |
| pycparser               | 1.13 sec                                                              | 1.19 sec: 1.05x slower                                                        |
| scimark_fft             | 354 ms                                                                | 374 ms: 1.06x slower                                                          |
| regex_v8                | 24.3 ms                                                               | 26.1 ms: 1.07x slower                                                         |
| logging_silent          | 97.6 ns                                                               | 105 ns: 1.08x slower                                                          |
| gc_traversal            | 3.53 ms                                                               | 3.82 ms: 1.08x slower                                                         |
| scimark_sparse_mat_mult | 4.54 ms                                                               | 5.07 ms: 1.12x slower                                                         |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (27): xml_etree_parse, logging_format, json_loads, xml_etree_process, logging_simple, coroutines, xml_etree_iterparse, chaos, pylint, deepcopy_reduce, django_template, pyflate, bpe_tokeniser, 2to3, bench_mp_pool, python_startup, json_dumps, xml_etree_generate, html5lib, typing_runtime_protocols, sympy_expand, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x