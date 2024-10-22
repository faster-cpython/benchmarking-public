# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6125ff0
- commit date: 2024-07-13
- overall geometric mean: 1.01x slower
- HPT reliability: 97.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 275 ms: 1.01x slower                                                        |
| tornado_http   | 93.8 ms                                                               | 93.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                | 219 ms: 1.04x faster                                                        |
| regex_effbot   | 3.84 ms                                                               | 3.80 ms: 1.01x faster                                                       |
| regex_v8       | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| tomli_loads       | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                      |
| json_loads        | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| json_dumps        | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                       |
| Geometric mean    | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_iterparse, unpickle_pure_python, xml_etree_parse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.11 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 9.77 ms                                                               | 9.79 ms: 1.00x slower                                                       |
| genshi_xml     | 56.9 ms                                                               | 59.3 ms: 1.04x slower                                                       |
| genshi_text    | 25.1 ms                                                               | 26.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| bpe_tokeniser           | 4.82 sec                                                              | 4.60 sec: 1.05x faster                                                      |
| regex_dna               | 227 ms                                                                | 219 ms: 1.04x faster                                                        |
| meteor_contest          | 108 ms                                                                | 105 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 716 ms                                                                | 701 ms: 1.02x faster                                                        |
| scimark_sor             | 131 ms                                                                | 129 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.76 us                                                               | 2.72 us: 1.01x faster                                                       |
| mdp                     | 2.71 sec                                                              | 2.68 sec: 1.01x faster                                                      |
| regex_effbot            | 3.84 ms                                                               | 3.80 ms: 1.01x faster                                                       |
| pyflate                 | 446 ms                                                                | 442 ms: 1.01x faster                                                        |
| logging_simple          | 5.61 us                                                               | 5.56 us: 1.01x faster                                                       |
| xml_etree_process       | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                       |
| dulwich_log             | 68.0 ms                                                               | 67.5 ms: 1.01x faster                                                       |
| coroutines              | 23.5 ms                                                               | 23.4 ms: 1.01x faster                                                       |
| logging_format          | 6.16 us                                                               | 6.12 us: 1.01x faster                                                       |
| asyncio_websockets      | 558 ms                                                                | 554 ms: 1.01x faster                                                        |
| crypto_pyaes            | 67.0 ms                                                               | 66.6 ms: 1.01x faster                                                       |
| tornado_http            | 93.8 ms                                                               | 93.3 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.77 ms                                                               | 1.76 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                      |
| asyncio_tcp             | 504 ms                                                                | 503 ms: 1.00x faster                                                        |
| python_startup_no_site  | 7.11 ms                                                               | 7.11 ms: 1.00x faster                                                       |
| mako                    | 9.77 ms                                                               | 9.79 ms: 1.00x slower                                                       |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| go                      | 146 ms                                                                | 147 ms: 1.00x slower                                                        |
| deepcopy_memo           | 28.4 us                                                               | 28.5 us: 1.00x slower                                                       |
| sympy_sum               | 167 ms                                                                | 168 ms: 1.01x slower                                                        |
| sqlglot_parse           | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                       |
| regex_v8                | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                       |
| sympy_str               | 293 ms                                                                | 296 ms: 1.01x slower                                                        |
| tomli_loads             | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                      |
| async_generators        | 455 ms                                                                | 459 ms: 1.01x slower                                                        |
| sqlglot_optimize        | 55.7 ms                                                               | 56.3 ms: 1.01x slower                                                       |
| scimark_lu              | 126 ms                                                                | 127 ms: 1.01x slower                                                        |
| telco                   | 7.92 ms                                                               | 8.01 ms: 1.01x slower                                                       |
| 2to3                    | 272 ms                                                                | 275 ms: 1.01x slower                                                        |
| chaos                   | 57.8 ms                                                               | 58.6 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 60.8 ms                                                               | 61.6 ms: 1.01x slower                                                       |
| json_loads              | 27.5 us                                                               | 27.9 us: 1.01x slower                                                       |
| sqlglot_transpile       | 1.60 ms                                                               | 1.62 ms: 1.02x slower                                                       |
| sqlglot_normalize       | 113 ms                                                                | 115 ms: 1.02x slower                                                        |
| sympy_expand            | 493 ms                                                                | 502 ms: 1.02x slower                                                        |
| sympy_integrate         | 21.9 ms                                                               | 22.4 ms: 1.02x slower                                                       |
| json_dumps              | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                       |
| gc_traversal            | 3.64 ms                                                               | 3.73 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult | 4.37 ms                                                               | 4.49 ms: 1.03x slower                                                       |
| pathlib                 | 15.9 ms                                                               | 16.4 ms: 1.03x slower                                                       |
| spectral_norm           | 101 ms                                                                | 105 ms: 1.04x slower                                                        |
| genshi_xml              | 56.9 ms                                                               | 59.3 ms: 1.04x slower                                                       |
| genshi_text             | 25.1 ms                                                               | 26.2 ms: 1.04x slower                                                       |
| scimark_fft             | 305 ms                                                                | 319 ms: 1.05x slower                                                        |
| richards_super          | 47.7 ms                                                               | 50.2 ms: 1.05x slower                                                       |
| richards                | 41.5 ms                                                               | 43.9 ms: 1.06x slower                                                       |
| generators              | 29.8 ms                                                               | 38.6 ms: 1.30x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (38): django_template, logging_silent, pprint_pformat, async_tree_cpu_io_mixed_tg, nqueens, json, async_tree_cpu_io_mixed, async_tree_none, html5lib, float, comprehensions, bench_thread_pool, async_tree_none_tg, hexiom, thrift, python_startup, dask, bench_mp_pool, raytrace, xml_etree_iterparse, async_tree_io_tg, regex_compile, unpickle_pure_python, docutils, xml_etree_parse, deltablue, coverage, deepcopy, pycparser, xml_etree_generate, async_tree_io, async_tree_memoization_tg, nbody, typing_runtime_protocols, pickle_pure_python, async_tree_memoization, fannkuch, pylint

# HPT report

- Reliability score: 97.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x