# Results vs. base

- fork: faster-cpython
- ref: use_attributes_to_gu
- machine: linux-x86_64
- commit hash: 3d7e23f
- commit date: 2024-08-05
- overall geometric mean: 1.00x slower
- HPT reliability: 74.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                | 263 ms: 1.00x slower                                                            |
| docutils       | 2.72 sec                                                              | 2.74 sec: 1.01x slower                                                          |
| html5lib       | 64.9 ms                                                               | 66.0 ms: 1.02x slower                                                           |
| tornado_http   | 90.4 ms                                                               | 89.7 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_generators | 439 ms                                                                | 435 ms: 1.01x faster                                                            |
| asyncio_tcp      | 486 ms                                                                | 485 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                          |
| coroutines       | 23.0 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.6 ms                                                               | 77.8 ms: 1.01x faster                                                           |
| pidigits       | 188 ms                                                                | 187 ms: 1.00x faster                                                            |
| nbody          | 85.0 ms                                                               | 86.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 229 ms: 1.05x slower                                                            |
| regex_effbot   | 3.66 ms                                                               | 3.87 ms: 1.06x slower                                                           |
| regex_v8       | 24.2 ms                                                               | 25.8 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.0 ms                                                               | 59.4 ms: 1.01x faster                                                           |
| xml_etree_generate   | 86.2 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| unpickle_pure_python | 212 us                                                                | 211 us: 1.01x faster                                                            |
| tomli_loads          | 2.04 sec                                                              | 2.03 sec: 1.01x faster                                                          |
| pickle_pure_python   | 303 us                                                                | 302 us: 1.00x faster                                                            |
| json_dumps           | 10.4 ms                                                               | 10.7 ms: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.10 ms                                                               | 7.07 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| genshi_xml     | 51.4 ms                                                               | 52.5 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20240805-linux-x86_64-python-1422500d020bd199b263-3.14.0a0-1422500 | bm-20240805-linux-x86_64-faster%2dcpython-use_attributes_to_gu-3.14.0a0-3d7e23f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| go                     | 143 ms                                                                | 117 ms: 1.23x faster                                                            |
| telco                  | 8.32 ms                                                               | 8.12 ms: 1.02x faster                                                           |
| logging_silent         | 99.6 ns                                                               | 98.0 ns: 1.02x faster                                                           |
| bpe_tokeniser          | 4.86 sec                                                              | 4.78 sec: 1.02x faster                                                          |
| sqlglot_normalize      | 108 ms                                                                | 106 ms: 1.02x faster                                                            |
| scimark_monte_carlo    | 67.8 ms                                                               | 66.8 ms: 1.01x faster                                                           |
| pyflate                | 479 ms                                                                | 473 ms: 1.01x faster                                                            |
| float                  | 78.6 ms                                                               | 77.8 ms: 1.01x faster                                                           |
| deepcopy_memo          | 29.0 us                                                               | 28.6 us: 1.01x faster                                                           |
| xml_etree_process      | 60.0 ms                                                               | 59.4 ms: 1.01x faster                                                           |
| async_generators       | 439 ms                                                                | 435 ms: 1.01x faster                                                            |
| sympy_sum              | 151 ms                                                                | 150 ms: 1.01x faster                                                            |
| nqueens                | 80.0 ms                                                               | 79.3 ms: 1.01x faster                                                           |
| xml_etree_generate     | 86.2 ms                                                               | 85.5 ms: 1.01x faster                                                           |
| pathlib                | 15.8 ms                                                               | 15.7 ms: 1.01x faster                                                           |
| sqlglot_parse          | 1.27 ms                                                               | 1.27 ms: 1.01x faster                                                           |
| tornado_http           | 90.4 ms                                                               | 89.7 ms: 1.01x faster                                                           |
| unpickle_pure_python   | 212 us                                                                | 211 us: 1.01x faster                                                            |
| sympy_expand           | 459 ms                                                                | 456 ms: 1.01x faster                                                            |
| sqlglot_transpile      | 1.57 ms                                                               | 1.56 ms: 1.01x faster                                                           |
| sqlglot_optimize       | 53.4 ms                                                               | 53.1 ms: 1.01x faster                                                           |
| tomli_loads            | 2.04 sec                                                              | 2.03 sec: 1.01x faster                                                          |
| sympy_integrate        | 19.6 ms                                                               | 19.5 ms: 1.01x faster                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| pickle_pure_python     | 303 us                                                                | 302 us: 1.00x faster                                                            |
| python_startup_no_site | 7.10 ms                                                               | 7.07 ms: 1.00x faster                                                           |
| asyncio_tcp            | 486 ms                                                                | 485 ms: 1.00x faster                                                            |
| pidigits               | 188 ms                                                                | 187 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                          |
| bench_thread_pool      | 783 us                                                                | 785 us: 1.00x slower                                                            |
| scimark_sor            | 125 ms                                                                | 125 ms: 1.00x slower                                                            |
| 2to3                   | 261 ms                                                                | 263 ms: 1.00x slower                                                            |
| richards_super         | 51.3 ms                                                               | 51.6 ms: 1.01x slower                                                           |
| deepcopy               | 262 us                                                                | 263 us: 1.01x slower                                                            |
| comprehensions         | 16.5 us                                                               | 16.6 us: 1.01x slower                                                           |
| crypto_pyaes           | 71.7 ms                                                               | 72.2 ms: 1.01x slower                                                           |
| generators             | 27.6 ms                                                               | 27.8 ms: 1.01x slower                                                           |
| docutils               | 2.72 sec                                                              | 2.74 sec: 1.01x slower                                                          |
| richards               | 45.5 ms                                                               | 45.9 ms: 1.01x slower                                                           |
| scimark_fft            | 354 ms                                                                | 358 ms: 1.01x slower                                                            |
| deltablue              | 3.15 ms                                                               | 3.19 ms: 1.01x slower                                                           |
| logging_format         | 6.07 us                                                               | 6.14 us: 1.01x slower                                                           |
| coroutines             | 23.0 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| nbody                  | 85.0 ms                                                               | 86.2 ms: 1.01x slower                                                           |
| mako                   | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| hexiom                 | 6.08 ms                                                               | 6.18 ms: 1.02x slower                                                           |
| html5lib               | 64.9 ms                                                               | 66.0 ms: 1.02x slower                                                           |
| deepcopy_reduce        | 2.66 us                                                               | 2.71 us: 1.02x slower                                                           |
| genshi_xml             | 51.4 ms                                                               | 52.5 ms: 1.02x slower                                                           |
| fannkuch               | 399 ms                                                                | 408 ms: 1.02x slower                                                            |
| raytrace               | 251 ms                                                                | 257 ms: 1.02x slower                                                            |
| json_dumps             | 10.4 ms                                                               | 10.7 ms: 1.02x slower                                                           |
| spectral_norm          | 110 ms                                                                | 112 ms: 1.02x slower                                                            |
| gc_traversal           | 3.63 ms                                                               | 3.75 ms: 1.03x slower                                                           |
| regex_dna              | 219 ms                                                                | 229 ms: 1.05x slower                                                            |
| coverage               | 85.6 ms                                                               | 90.3 ms: 1.06x slower                                                           |
| regex_effbot           | 3.66 ms                                                               | 3.87 ms: 1.06x slower                                                           |
| regex_v8               | 24.2 ms                                                               | 25.8 ms: 1.06x slower                                                           |
| mdp                    | 2.52 sec                                                              | 2.69 sec: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (31): xml_etree_parse, regex_compile, async_tree_none, async_tree_cpu_io_mixed, genshi_text, typing_runtime_protocols, pycparser, pprint_pformat, django_template, scimark_lu, sympy_str, async_tree_io_tg, async_tree_none_tg, scimark_sparse_mat_mult, bench_mp_pool, meteor_contest, json_loads, dask, create_gc_cycles, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, pprint_safe_repr, chaos, logging_simple, asyncio_websockets, async_tree_memoization_tg, pylint, thrift, async_tree_io, json, async_tree_memoization

# HPT report

- Reliability score: 74.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x