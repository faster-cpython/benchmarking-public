# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x faster
- HPT reliability: 78.21%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 274 ms: 1.01x slower                                                     |
| html5lib       | 64.2 ms                                                               | 65.7 ms: 1.02x slower                                                    |
| tornado_http   | 92.5 ms                                                               | 92.2 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none           | 327 ms                                                                | 312 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed   | 567 ms                                                                | 555 ms: 1.02x faster                                                     |
| async_tree_memoization_tg | 379 ms                                                                | 397 ms: 1.05x slower                                                     |
| Geometric mean            | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                               | 79.7 ms: 1.02x faster                                                    |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                     |
| float          | 70.1 ms                                                               | 70.7 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.93 ms                                                               | 3.68 ms: 1.07x faster                                                    |
| regex_dna      | 229 ms                                                                | 226 ms: 1.02x faster                                                     |
| regex_compile  | 135 ms                                                                | 134 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 201 us: 1.08x faster                                                     |
| tomli_loads          | 1.94 sec                                                              | 1.91 sec: 1.01x faster                                                   |
| xml_etree_process    | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                    |
| xml_etree_generate   | 80.8 ms                                                               | 81.1 ms: 1.00x slower                                                    |
| json_loads           | 27.4 us                                                               | 27.6 us: 1.01x slower                                                    |
| pickle_pure_python   | 293 us                                                                | 299 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                    |
| python_startup_no_site | 7.12 ms                                                               | 7.08 ms: 1.01x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 9.76 ms                                                               | 9.53 ms: 1.02x faster                                                    |
| genshi_text    | 25.1 ms                                                               | 25.0 ms: 1.01x faster                                                    |
| genshi_xml     | 55.6 ms                                                               | 58.1 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20240701-linux-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                       | 2.76 sec                                                              | 2.53 sec: 1.09x faster                                                   |
| unpickle_pure_python      | 217 us                                                                | 201 us: 1.08x faster                                                     |
| regex_effbot              | 3.93 ms                                                               | 3.68 ms: 1.07x faster                                                    |
| async_tree_none           | 327 ms                                                                | 312 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult   | 4.48 ms                                                               | 4.30 ms: 1.04x faster                                                    |
| coroutines                | 24.0 ms                                                               | 23.3 ms: 1.03x faster                                                    |
| mako                      | 9.76 ms                                                               | 9.53 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 567 ms                                                                | 555 ms: 1.02x faster                                                     |
| nbody                     | 81.4 ms                                                               | 79.7 ms: 1.02x faster                                                    |
| pathlib                   | 16.1 ms                                                               | 15.8 ms: 1.02x faster                                                    |
| pycparser                 | 1.16 sec                                                              | 1.14 sec: 1.02x faster                                                   |
| regex_dna                 | 229 ms                                                                | 226 ms: 1.02x faster                                                     |
| tomli_loads               | 1.94 sec                                                              | 1.91 sec: 1.01x faster                                                   |
| json                      | 5.16 ms                                                               | 5.10 ms: 1.01x faster                                                    |
| crypto_pyaes              | 67.7 ms                                                               | 67.0 ms: 1.01x faster                                                    |
| scimark_lu                | 126 ms                                                                | 125 ms: 1.01x faster                                                     |
| python_startup            | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                    |
| regex_compile             | 135 ms                                                                | 134 ms: 1.01x faster                                                     |
| scimark_monte_carlo       | 61.2 ms                                                               | 60.7 ms: 1.01x faster                                                    |
| xml_etree_process         | 57.5 ms                                                               | 57.1 ms: 1.01x faster                                                    |
| genshi_text               | 25.1 ms                                                               | 25.0 ms: 1.01x faster                                                    |
| scimark_sor               | 132 ms                                                                | 131 ms: 1.01x faster                                                     |
| gc_traversal              | 3.70 ms                                                               | 3.68 ms: 1.01x faster                                                    |
| dulwich_log               | 67.5 ms                                                               | 67.1 ms: 1.01x faster                                                    |
| python_startup_no_site    | 7.12 ms                                                               | 7.08 ms: 1.01x faster                                                    |
| tornado_http              | 92.5 ms                                                               | 92.2 ms: 1.00x faster                                                    |
| pidigits                  | 185 ms                                                                | 186 ms: 1.00x slower                                                     |
| asyncio_tcp_ssl           | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                   |
| xml_etree_generate        | 80.8 ms                                                               | 81.1 ms: 1.00x slower                                                    |
| meteor_contest            | 106 ms                                                                | 106 ms: 1.00x slower                                                     |
| logging_silent            | 106 ns                                                                | 107 ns: 1.00x slower                                                     |
| bench_thread_pool         | 828 us                                                                | 833 us: 1.01x slower                                                     |
| hexiom                    | 6.54 ms                                                               | 6.57 ms: 1.01x slower                                                    |
| sqlglot_normalize         | 111 ms                                                                | 112 ms: 1.01x slower                                                     |
| sympy_expand              | 496 ms                                                                | 499 ms: 1.01x slower                                                     |
| typing_runtime_protocols  | 169 us                                                                | 170 us: 1.01x slower                                                     |
| float                     | 70.1 ms                                                               | 70.7 ms: 1.01x slower                                                    |
| 2to3                      | 272 ms                                                                | 274 ms: 1.01x slower                                                     |
| json_loads                | 27.4 us                                                               | 27.6 us: 1.01x slower                                                    |
| sympy_str                 | 293 ms                                                                | 295 ms: 1.01x slower                                                     |
| logging_simple            | 5.47 us                                                               | 5.52 us: 1.01x slower                                                    |
| sympy_integrate           | 21.8 ms                                                               | 22.1 ms: 1.01x slower                                                    |
| sympy_sum                 | 166 ms                                                                | 167 ms: 1.01x slower                                                     |
| scimark_fft               | 309 ms                                                                | 313 ms: 1.01x slower                                                     |
| deepcopy                  | 268 us                                                                | 271 us: 1.01x slower                                                     |
| go                        | 141 ms                                                                | 143 ms: 1.02x slower                                                     |
| generators                | 29.6 ms                                                               | 30.1 ms: 1.02x slower                                                    |
| spectral_norm             | 103 ms                                                                | 105 ms: 1.02x slower                                                     |
| nqueens                   | 85.8 ms                                                               | 87.5 ms: 1.02x slower                                                    |
| sqlglot_optimize          | 55.2 ms                                                               | 56.3 ms: 1.02x slower                                                    |
| pickle_pure_python        | 293 us                                                                | 299 us: 1.02x slower                                                     |
| raytrace                  | 265 ms                                                                | 271 ms: 1.02x slower                                                     |
| html5lib                  | 64.2 ms                                                               | 65.7 ms: 1.02x slower                                                    |
| genshi_xml                | 55.6 ms                                                               | 58.1 ms: 1.04x slower                                                    |
| async_tree_memoization_tg | 379 ms                                                                | 397 ms: 1.05x slower                                                     |
| richards_super            | 47.0 ms                                                               | 49.3 ms: 1.05x slower                                                    |
| richards                  | 40.9 ms                                                               | 43.6 ms: 1.06x slower                                                    |
| deltablue                 | 3.51 ms                                                               | 3.81 ms: 1.09x slower                                                    |
| Geometric mean            | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (33): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, chaos, deepcopy_reduce, logging_format, fannkuch, xml_etree_parse, docutils, telco, regex_v8, dask, asyncio_tcp, pyflate, thrift, create_gc_cycles, async_generators, bpe_tokeniser, bench_mp_pool, json_dumps, sqlglot_transpile, asyncio_websockets, coverage, async_tree_cpu_io_mixed_tg, pprint_pformat, pprint_safe_repr, comprehensions, xml_etree_iterparse, django_template, sqlglot_parse, deepcopy_memo, pylint

# HPT report

- Reliability score: 78.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x