# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: a4c1908
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 98.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 275 ms: 1.01x slower                                                      |
| docutils       | 2.87 sec                                                              | 2.92 sec: 1.02x slower                                                    |
| html5lib       | 64.7 ms                                                               | 63.6 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 545 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.75 ms: 1.03x faster                                                     |
| regex_v8       | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                     |
| regex_compile  | 134 ms                                                                | 137 ms: 1.03x slower                                                      |
| regex_dna      | 222 ms                                                                | 228 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.92 sec                                                              | 1.87 sec: 1.03x faster                                                    |
| json_loads           | 28.1 us                                                               | 27.6 us: 1.02x faster                                                     |
| xml_etree_parse      | 150 ms                                                                | 148 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 99.2 ms                                                               | 98.4 ms: 1.01x faster                                                     |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                      |
| pickle_pure_python   | 293 us                                                                | 308 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (3): json_dumps, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                     |
| mako           | 9.76 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| genshi_text    | 24.9 ms                                                               | 25.9 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-a4c1908 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards                   | 41.8 ms                                                               | 35.9 ms: 1.16x faster                                                     |
| richards_super             | 47.5 ms                                                               | 40.8 ms: 1.16x faster                                                     |
| logging_silent             | 107 ns                                                                | 101 ns: 1.06x faster                                                      |
| deepcopy_memo              | 28.4 us                                                               | 27.1 us: 1.05x faster                                                     |
| scimark_lu                 | 124 ms                                                                | 119 ms: 1.05x faster                                                      |
| deepcopy_reduce            | 2.78 us                                                               | 2.68 us: 1.03x faster                                                     |
| tomli_loads                | 1.92 sec                                                              | 1.87 sec: 1.03x faster                                                    |
| regex_effbot               | 3.86 ms                                                               | 3.75 ms: 1.03x faster                                                     |
| dulwich_log                | 67.1 ms                                                               | 65.2 ms: 1.03x faster                                                     |
| deepcopy                   | 273 us                                                                | 265 us: 1.03x faster                                                      |
| telco                      | 8.08 ms                                                               | 7.88 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 4.84 sec                                                              | 4.72 sec: 1.02x faster                                                    |
| json_loads                 | 28.1 us                                                               | 27.6 us: 1.02x faster                                                     |
| deltablue                  | 3.52 ms                                                               | 3.45 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 172 us                                                                | 169 us: 1.02x faster                                                      |
| crypto_pyaes               | 67.8 ms                                                               | 66.6 ms: 1.02x faster                                                     |
| pyflate                    | 444 ms                                                                | 437 ms: 1.02x faster                                                      |
| html5lib                   | 64.7 ms                                                               | 63.6 ms: 1.02x faster                                                     |
| xml_etree_parse            | 150 ms                                                                | 148 ms: 1.02x faster                                                      |
| pathlib                    | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                     |
| sympy_str                  | 292 ms                                                                | 289 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 99.2 ms                                                               | 98.4 ms: 1.01x faster                                                     |
| coroutines                 | 23.4 ms                                                               | 23.3 ms: 1.01x faster                                                     |
| float                      | 70.0 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| bench_thread_pool          | 832 us                                                                | 827 us: 1.01x faster                                                      |
| unpickle_pure_python       | 215 us                                                                | 213 us: 1.01x faster                                                      |
| spectral_norm              | 104 ms                                                                | 104 ms: 1.00x faster                                                      |
| fannkuch                   | 361 ms                                                                | 359 ms: 1.00x faster                                                      |
| sympy_integrate            | 21.8 ms                                                               | 21.7 ms: 1.00x faster                                                     |
| asyncio_websockets         | 557 ms                                                                | 555 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.10 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| comprehensions             | 16.7 us                                                               | 16.7 us: 1.00x slower                                                     |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| regex_v8                   | 25.3 ms                                                               | 25.4 ms: 1.00x slower                                                     |
| sympy_expand               | 492 ms                                                                | 494 ms: 1.00x slower                                                      |
| scimark_fft                | 309 ms                                                                | 311 ms: 1.01x slower                                                      |
| mdp                        | 2.52 sec                                                              | 2.54 sec: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                                    |
| sympy_sum                  | 165 ms                                                                | 166 ms: 1.01x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                               | 1.78 ms: 1.01x slower                                                     |
| generators                 | 29.5 ms                                                               | 29.8 ms: 1.01x slower                                                     |
| pycparser                  | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                                    |
| thrift                     | 801 us                                                                | 812 us: 1.01x slower                                                      |
| genshi_xml                 | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                     |
| 2to3                       | 271 ms                                                                | 275 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 545 ms: 1.01x slower                                                      |
| docutils                   | 2.87 sec                                                              | 2.92 sec: 1.02x slower                                                    |
| logging_format             | 5.94 us                                                               | 6.04 us: 1.02x slower                                                     |
| scimark_monte_carlo        | 61.1 ms                                                               | 62.4 ms: 1.02x slower                                                     |
| sqlglot_optimize           | 55.0 ms                                                               | 56.2 ms: 1.02x slower                                                     |
| sqlglot_transpile          | 1.60 ms                                                               | 1.64 ms: 1.02x slower                                                     |
| regex_compile              | 134 ms                                                                | 137 ms: 1.03x slower                                                      |
| raytrace                   | 266 ms                                                                | 273 ms: 1.03x slower                                                      |
| mako                       | 9.76 ms                                                               | 10.0 ms: 1.03x slower                                                     |
| gc_traversal               | 3.74 ms                                                               | 3.85 ms: 1.03x slower                                                     |
| regex_dna                  | 222 ms                                                                | 228 ms: 1.03x slower                                                      |
| asyncio_tcp                | 488 ms                                                                | 507 ms: 1.04x slower                                                      |
| hexiom                     | 6.48 ms                                                               | 6.73 ms: 1.04x slower                                                     |
| genshi_text                | 24.9 ms                                                               | 25.9 ms: 1.04x slower                                                     |
| pprint_safe_repr           | 710 ms                                                                | 740 ms: 1.04x slower                                                      |
| pickle_pure_python         | 293 us                                                                | 308 us: 1.05x slower                                                      |
| pprint_pformat             | 1.45 sec                                                              | 1.53 sec: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (27): django_template, chaos, scimark_sor, json, dask, tornado_http, coverage, meteor_contest, json_dumps, bench_mp_pool, go, async_tree_io_tg, xml_etree_process, async_generators, sqlglot_normalize, xml_etree_generate, async_tree_memoization_tg, logging_simple, async_tree_io, nbody, async_tree_none_tg, scimark_sparse_mat_mult, async_tree_memoization, nqueens, async_tree_none, async_tree_cpu_io_mixed, pylint

# HPT report

- Reliability score: 98.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x