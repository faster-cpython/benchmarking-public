# Results vs. base

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: darwin-arm64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.00x slower
- HPT reliability: 98.31%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 184 ms                                                                | 158 ms: 1.16x faster                                                  |
| html5lib       | 31.2 ms                                                               | 31.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators    | 285 ms                                                                | 280 ms: 1.02x faster                                                  |
| coroutines          | 16.1 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| async_tree_io       | 592 ms                                                                | 594 ms: 1.00x slower                                                  |
| async_tree_eager    | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                                 |
| async_tree_eager_tg | 41.7 ms                                                               | 42.6 ms: 1.02x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (16): async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, asyncio_tcp, asyncio_websockets, asyncio_tcp_ssl, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.4 ms                                                               | 60.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                 |
| regex_effbot   | 2.46 ms                                                               | 2.47 ms: 1.00x slower                                                 |
| regex_compile  | 66.9 ms                                                               | 67.2 ms: 1.00x slower                                                 |
| regex_dna      | 145 ms                                                                | 146 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.48 sec                                                              | 1.43 sec: 1.04x faster                                                |
| xml_etree_parse    | 111 ms                                                                | 109 ms: 1.02x faster                                                  |
| json_loads         | 17.2 us                                                               | 17.1 us: 1.01x faster                                                 |
| pickle_pure_python | 182 us                                                                | 184 us: 1.01x slower                                                  |
| json_dumps         | 6.32 ms                                                               | 6.42 ms: 1.02x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.95 ms                                                               | 6.91 ms: 1.00x faster                                                 |
| django_template | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                                 |
| genshi_text     | 13.9 ms                                                               | 14.0 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3                    | 184 ms                                                                | 158 ms: 1.16x faster                                                  |
| tomli_loads             | 1.48 sec                                                              | 1.43 sec: 1.04x faster                                                |
| xml_etree_parse         | 111 ms                                                                | 109 ms: 1.02x faster                                                  |
| chaos                   | 35.7 ms                                                               | 34.9 ms: 1.02x faster                                                 |
| scimark_lu              | 68.1 ms                                                               | 66.8 ms: 1.02x faster                                                 |
| async_generators        | 285 ms                                                                | 280 ms: 1.02x faster                                                  |
| logging_simple          | 3.09 us                                                               | 3.06 us: 1.01x faster                                                 |
| fannkuch                | 262 ms                                                                | 260 ms: 1.01x faster                                                  |
| deltablue               | 2.14 ms                                                               | 2.12 ms: 1.01x faster                                                 |
| json                    | 2.95 ms                                                               | 2.93 ms: 1.01x faster                                                 |
| json_loads              | 17.2 us                                                               | 17.1 us: 1.01x faster                                                 |
| sympy_integrate         | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                 |
| telco                   | 4.72 ms                                                               | 4.69 ms: 1.01x faster                                                 |
| logging_format          | 3.39 us                                                               | 3.37 us: 1.01x faster                                                 |
| python_startup          | 16.0 ms                                                               | 15.9 ms: 1.01x faster                                                 |
| mako                    | 6.95 ms                                                               | 6.91 ms: 1.00x faster                                                 |
| sqlglot_transpile       | 904 us                                                                | 900 us: 1.00x faster                                                  |
| crypto_pyaes            | 51.1 ms                                                               | 50.8 ms: 1.00x faster                                                 |
| pyflate                 | 321 ms                                                                | 319 ms: 1.00x faster                                                  |
| hexiom                  | 4.07 ms                                                               | 4.06 ms: 1.00x faster                                                 |
| sqlglot_parse           | 747 us                                                                | 745 us: 1.00x faster                                                  |
| sympy_expand            | 228 ms                                                                | 227 ms: 1.00x faster                                                  |
| regex_v8                | 16.6 ms                                                               | 16.6 ms: 1.00x faster                                                 |
| coroutines              | 16.1 ms                                                               | 16.1 ms: 1.00x faster                                                 |
| nqueens                 | 53.3 ms                                                               | 53.2 ms: 1.00x faster                                                 |
| logging_silent          | 61.0 ns                                                               | 61.1 ns: 1.00x slower                                                 |
| gc_traversal            | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult | 2.78 ms                                                               | 2.78 ms: 1.00x slower                                                 |
| meteor_contest          | 71.9 ms                                                               | 72.1 ms: 1.00x slower                                                 |
| scimark_sor             | 92.8 ms                                                               | 93.0 ms: 1.00x slower                                                 |
| async_tree_io           | 592 ms                                                                | 594 ms: 1.00x slower                                                  |
| django_template         | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                                 |
| sympy_str               | 132 ms                                                                | 132 ms: 1.00x slower                                                  |
| bench_thread_pool       | 447 us                                                                | 449 us: 1.00x slower                                                  |
| pprint_pformat          | 928 ms                                                                | 931 ms: 1.00x slower                                                  |
| coverage                | 44.6 ms                                                               | 44.8 ms: 1.00x slower                                                 |
| regex_effbot            | 2.46 ms                                                               | 2.47 ms: 1.00x slower                                                 |
| regex_compile           | 66.9 ms                                                               | 67.2 ms: 1.00x slower                                                 |
| bpe_tokeniser           | 3.12 sec                                                              | 3.13 sec: 1.00x slower                                                |
| deepcopy                | 143 us                                                                | 144 us: 1.00x slower                                                  |
| regex_dna               | 145 ms                                                                | 146 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 1.50 us                                                               | 1.51 us: 1.01x slower                                                 |
| html5lib                | 31.2 ms                                                               | 31.4 ms: 1.01x slower                                                 |
| scimark_fft             | 184 ms                                                                | 185 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 451 ms                                                                | 454 ms: 1.01x slower                                                  |
| raytrace                | 149 ms                                                                | 150 ms: 1.01x slower                                                  |
| genshi_text             | 13.9 ms                                                               | 14.0 ms: 1.01x slower                                                 |
| async_tree_eager        | 60.6 ms                                                               | 61.1 ms: 1.01x slower                                                 |
| mdp                     | 1.42 sec                                                              | 1.43 sec: 1.01x slower                                                |
| pickle_pure_python      | 182 us                                                                | 184 us: 1.01x slower                                                  |
| nbody                   | 59.4 ms                                                               | 60.1 ms: 1.01x slower                                                 |
| generators              | 20.5 ms                                                               | 20.8 ms: 1.01x slower                                                 |
| json_dumps              | 6.32 ms                                                               | 6.42 ms: 1.02x slower                                                 |
| go                      | 106 ms                                                                | 108 ms: 1.02x slower                                                  |
| async_tree_eager_tg     | 41.7 ms                                                               | 42.6 ms: 1.02x slower                                                 |
| richards                | 30.4 ms                                                               | 31.1 ms: 1.02x slower                                                 |
| richards_super          | 33.3 ms                                                               | 34.3 ms: 1.03x slower                                                 |
| comprehensions          | 9.99 us                                                               | 10.3 us: 1.03x slower                                                 |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (40): async_tree_none, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, xml_etree_iterparse, asyncio_tcp, create_gc_cycles, sympy_sum, sqlglot_normalize, asyncio_websockets, genshi_xml, docutils, float, dulwich_log, xml_etree_process, sqlglot_optimize, asyncio_tcp_ssl, scimark_monte_carlo, pidigits, python_startup_no_site, xml_etree_generate, spectral_norm, thrift, async_tree_eager_cpu_io_mixed_tg, unpickle_pure_python, deepcopy_memo, async_tree_eager_io_tg, typing_runtime_protocols, pycparser, async_tree_eager_memoization_tg, async_tree_eager_memoization, pathlib, bench_mp_pool, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_io, pylint, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, tornado_http

# HPT report

- Reliability score: 98.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x