# Results vs. base

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.01x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.06 sec                                                                | 3.09 sec: 1.01x slower                                                  |
| tornado_http   | 129 ms                                                                  | 125 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io  | 1.13 sec                                                                | 1.14 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (12): asyncio_tcp, async_tree_memoization, async_tree_none, async_tree_io_tg, coroutines, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, async_generators, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 109 ms                                                                  | 108 ms: 1.01x faster                                                    |
| float          | 91.9 ms                                                                 | 91.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                  | 123 ms: 1.03x faster                                                    |
| regex_v8       | 30.6 ms                                                                 | 30.5 ms: 1.00x faster                                                   |
| regex_effbot   | 4.83 ms                                                                 | 4.88 ms: 1.01x slower                                                   |
| regex_dna      | 247 ms                                                                  | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.3 ms                                                                 | 78.3 ms: 1.02x faster                                                   |
| pickle_pure_python   | 363 us                                                                  | 356 us: 1.02x faster                                                    |
| unpickle_pure_python | 255 us                                                                  | 252 us: 1.01x faster                                                    |
| tomli_loads          | 2.64 sec                                                                | 2.62 sec: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_parse, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.68 ms                                                                 | 8.77 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pprint_pformat         | 1.93 sec                                                                | 1.87 sec: 1.03x faster                                                  |
| pprint_safe_repr       | 936 ms                                                                  | 909 ms: 1.03x faster                                                    |
| regex_compile          | 127 ms                                                                  | 123 ms: 1.03x faster                                                    |
| tornado_http           | 129 ms                                                                  | 125 ms: 1.03x faster                                                    |
| xml_etree_process      | 80.3 ms                                                                 | 78.3 ms: 1.02x faster                                                   |
| pickle_pure_python     | 363 us                                                                  | 356 us: 1.02x faster                                                    |
| pycparser              | 1.24 sec                                                                | 1.22 sec: 1.02x faster                                                  |
| sqlglot_transpile      | 1.75 ms                                                                 | 1.71 ms: 1.02x faster                                                   |
| nqueens                | 100 ms                                                                  | 98.3 ms: 1.02x faster                                                   |
| scimark_lu             | 136 ms                                                                  | 134 ms: 1.02x faster                                                    |
| pyflate                | 562 ms                                                                  | 554 ms: 1.01x faster                                                    |
| nbody                  | 109 ms                                                                  | 108 ms: 1.01x faster                                                    |
| crypto_pyaes           | 83.1 ms                                                                 | 82.1 ms: 1.01x faster                                                   |
| unpickle_pure_python   | 255 us                                                                  | 252 us: 1.01x faster                                                    |
| hexiom                 | 7.10 ms                                                                 | 7.02 ms: 1.01x faster                                                   |
| deepcopy_reduce        | 3.54 us                                                                 | 3.50 us: 1.01x faster                                                   |
| tomli_loads            | 2.64 sec                                                                | 2.62 sec: 1.01x faster                                                  |
| mako                   | 13.4 ms                                                                 | 13.3 ms: 1.01x faster                                                   |
| float                  | 91.9 ms                                                                 | 91.2 ms: 1.01x faster                                                   |
| richards_super         | 59.4 ms                                                                 | 59.0 ms: 1.01x faster                                                   |
| regex_v8               | 30.6 ms                                                                 | 30.5 ms: 1.00x faster                                                   |
| scimark_sor            | 156 ms                                                                  | 158 ms: 1.01x slower                                                    |
| mdp                    | 3.34 sec                                                                | 3.37 sec: 1.01x slower                                                  |
| python_startup_no_site | 8.68 ms                                                                 | 8.77 ms: 1.01x slower                                                   |
| docutils               | 3.06 sec                                                                | 3.09 sec: 1.01x slower                                                  |
| regex_effbot           | 4.83 ms                                                                 | 4.88 ms: 1.01x slower                                                   |
| async_tree_io          | 1.13 sec                                                                | 1.14 sec: 1.01x slower                                                  |
| comprehensions         | 20.4 us                                                                 | 20.7 us: 1.02x slower                                                   |
| regex_dna              | 247 ms                                                                  | 252 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (60): bench_mp_pool, logging_format, asyncio_tcp, genshi_xml, json_dumps, json, thrift, async_tree_memoization, async_tree_none, scimark_monte_carlo, logging_simple, sympy_integrate, json_loads, pylint, typing_runtime_protocols, async_tree_io_tg, sympy_sum, telco, coroutines, genshi_text, richards, deepcopy, fannkuch, deltablue, pathlib, coverage, sympy_expand, async_tree_none_tg, xml_etree_parse, generators, meteor_contest, spectral_norm, bench_thread_pool, chaos, async_tree_cpu_io_mixed, sqlglot_parse, asyncio_websockets, scimark_fft, sqlglot_optimize, bpe_tokeniser, pidigits, raytrace, async_tree_memoization_tg, async_generators, python_startup, deepcopy_memo, async_tree_cpu_io_mixed_tg, create_gc_cycles, sqlglot_normalize, asyncio_tcp_ssl, gc_traversal, sympy_str, go, logging_silent, django_template, xml_etree_generate, scimark_sparse_mat_mult, 2to3, html5lib, xml_etree_iterparse

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x