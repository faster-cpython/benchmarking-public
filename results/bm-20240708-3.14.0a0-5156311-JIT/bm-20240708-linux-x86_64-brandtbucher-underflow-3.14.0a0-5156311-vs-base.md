# Results vs. base

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 5156311
- commit date: 2024-07-08
- overall geometric mean: 1.02x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 282 ms: 1.04x slower                                             |
| docutils       | 2.87 sec                                                              | 3.02 sec: 1.05x slower                                           |
| html5lib       | 64.7 ms                                                               | 69.9 ms: 1.08x slower                                            |
| tornado_http   | 92.4 ms                                                               | 97.6 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 547 ms: 1.02x slower                                             |
| async_tree_io              | 841 ms                                                                | 887 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 80.0 ms                                                               | 78.9 ms: 1.01x faster                                            |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                             |
| float          | 70.0 ms                                                               | 70.6 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.61 ms: 1.07x faster                                            |
| regex_v8       | 25.3 ms                                                               | 24.1 ms: 1.05x faster                                            |
| regex_dna      | 222 ms                                                                | 225 ms: 1.01x slower                                             |
| regex_compile  | 134 ms                                                                | 138 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 199 us: 1.08x faster                                             |
| json_loads           | 28.1 us                                                               | 27.5 us: 1.02x faster                                            |
| xml_etree_generate   | 81.6 ms                                                               | 82.5 ms: 1.01x slower                                            |
| pickle_pure_python   | 293 us                                                                | 297 us: 1.01x slower                                             |
| json_dumps           | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                            |
| tomli_loads          | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                     |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                            |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 24.9 ms                                                               | 23.5 ms: 1.06x faster                                            |
| mako            | 9.76 ms                                                               | 9.72 ms: 1.00x faster                                            |
| genshi_xml      | 58.0 ms                                                               | 59.5 ms: 1.03x slower                                            |
| django_template | 35.1 ms                                                               | 36.7 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python       | 215 us                                                                | 199 us: 1.08x faster                                             |
| regex_effbot               | 3.86 ms                                                               | 3.61 ms: 1.07x faster                                            |
| genshi_text                | 24.9 ms                                                               | 23.5 ms: 1.06x faster                                            |
| scimark_monte_carlo        | 61.1 ms                                                               | 58.1 ms: 1.05x faster                                            |
| regex_v8                   | 25.3 ms                                                               | 24.1 ms: 1.05x faster                                            |
| spectral_norm              | 104 ms                                                                | 100 ms: 1.04x faster                                             |
| nqueens                    | 85.5 ms                                                               | 83.0 ms: 1.03x faster                                            |
| telco                      | 8.08 ms                                                               | 7.87 ms: 1.03x faster                                            |
| fannkuch                   | 361 ms                                                                | 352 ms: 1.02x faster                                             |
| json_loads                 | 28.1 us                                                               | 27.5 us: 1.02x faster                                            |
| json                       | 5.19 ms                                                               | 5.09 ms: 1.02x faster                                            |
| comprehensions             | 16.7 us                                                               | 16.3 us: 1.02x faster                                            |
| crypto_pyaes               | 67.8 ms                                                               | 66.7 ms: 1.02x faster                                            |
| nbody                      | 80.0 ms                                                               | 78.9 ms: 1.01x faster                                            |
| meteor_contest             | 107 ms                                                                | 106 ms: 1.01x faster                                             |
| pyflate                    | 444 ms                                                                | 439 ms: 1.01x faster                                             |
| bpe_tokeniser              | 4.84 sec                                                              | 4.80 sec: 1.01x faster                                           |
| bench_thread_pool          | 832 us                                                                | 827 us: 1.01x faster                                             |
| coroutines                 | 23.4 ms                                                               | 23.3 ms: 1.01x faster                                            |
| mako                       | 9.76 ms                                                               | 9.72 ms: 1.00x faster                                            |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x faster                                             |
| gc_traversal               | 3.74 ms                                                               | 3.75 ms: 1.00x slower                                            |
| python_startup_no_site     | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                            |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                            |
| typing_runtime_protocols   | 172 us                                                                | 173 us: 1.01x slower                                             |
| float                      | 70.0 ms                                                               | 70.6 ms: 1.01x slower                                            |
| hexiom                     | 6.48 ms                                                               | 6.55 ms: 1.01x slower                                            |
| xml_etree_generate         | 81.6 ms                                                               | 82.5 ms: 1.01x slower                                            |
| richards_super             | 47.5 ms                                                               | 48.1 ms: 1.01x slower                                            |
| pickle_pure_python         | 293 us                                                                | 297 us: 1.01x slower                                             |
| async_generators           | 452 ms                                                                | 458 ms: 1.01x slower                                             |
| regex_dna                  | 222 ms                                                                | 225 ms: 1.01x slower                                             |
| json_dumps                 | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                            |
| sqlglot_parse              | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                            |
| coverage                   | 92.4 ms                                                               | 94.1 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 547 ms: 1.02x slower                                             |
| sqlglot_optimize           | 55.0 ms                                                               | 56.1 ms: 1.02x slower                                            |
| dask                       | 362 ms                                                                | 370 ms: 1.02x slower                                             |
| raytrace                   | 266 ms                                                                | 272 ms: 1.02x slower                                             |
| genshi_xml                 | 58.0 ms                                                               | 59.5 ms: 1.03x slower                                            |
| richards                   | 41.8 ms                                                               | 43.0 ms: 1.03x slower                                            |
| asyncio_tcp                | 488 ms                                                                | 503 ms: 1.03x slower                                             |
| regex_compile              | 134 ms                                                                | 138 ms: 1.03x slower                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 4.43 ms: 1.04x slower                                            |
| sqlglot_normalize          | 111 ms                                                                | 116 ms: 1.04x slower                                             |
| 2to3                       | 271 ms                                                                | 282 ms: 1.04x slower                                             |
| sqlglot_transpile          | 1.60 ms                                                               | 1.67 ms: 1.04x slower                                            |
| django_template            | 35.1 ms                                                               | 36.7 ms: 1.05x slower                                            |
| pprint_safe_repr           | 710 ms                                                                | 745 ms: 1.05x slower                                             |
| logging_simple             | 5.42 us                                                               | 5.69 us: 1.05x slower                                            |
| docutils                   | 2.87 sec                                                              | 3.02 sec: 1.05x slower                                           |
| sympy_str                  | 292 ms                                                                | 307 ms: 1.05x slower                                             |
| sympy_expand               | 492 ms                                                                | 518 ms: 1.05x slower                                             |
| pprint_pformat             | 1.45 sec                                                              | 1.53 sec: 1.05x slower                                           |
| async_tree_io              | 841 ms                                                                | 887 ms: 1.05x slower                                             |
| tornado_http               | 92.4 ms                                                               | 97.6 ms: 1.06x slower                                            |
| sympy_integrate            | 21.8 ms                                                               | 23.1 ms: 1.06x slower                                            |
| logging_format             | 5.94 us                                                               | 6.30 us: 1.06x slower                                            |
| tomli_loads                | 1.92 sec                                                              | 2.06 sec: 1.07x slower                                           |
| logging_silent             | 107 ns                                                                | 115 ns: 1.07x slower                                             |
| html5lib                   | 64.7 ms                                                               | 69.9 ms: 1.08x slower                                            |
| dulwich_log                | 67.1 ms                                                               | 72.6 ms: 1.08x slower                                            |
| sympy_sum                  | 165 ms                                                                | 179 ms: 1.08x slower                                             |
| mdp                        | 2.52 sec                                                              | 2.75 sec: 1.09x slower                                           |
| pylint                     | 334 ms                                                                | 392 ms: 1.17x slower                                             |
| deltablue                  | 3.52 ms                                                               | 4.14 ms: 1.18x slower                                            |
| generators                 | 29.5 ms                                                               | 43.2 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                     |

Benchmark hidden because not significant (24): chaos, xml_etree_parse, deepcopy, scimark_lu, xml_etree_iterparse, deepcopy_memo, asyncio_tcp_ssl, go, pycparser, pathlib, create_gc_cycles, bench_mp_pool, scimark_fft, asyncio_websockets, xml_etree_process, scimark_sor, thrift, async_tree_io_tg, async_tree_none, deepcopy_reduce, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x