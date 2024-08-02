# Results vs. base

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 270 ms: 1.00x faster                                            |
| docutils       | 2.87 sec                                                              | 2.96 sec: 1.03x slower                                          |
| html5lib       | 64.7 ms                                                               | 67.9 ms: 1.05x slower                                           |
| tornado_http   | 92.4 ms                                                               | 91.9 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 549 ms: 1.02x slower                                            |
| async_tree_io              | 841 ms                                                                | 909 ms: 1.08x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 187 ms: 1.00x slower                                            |
| float          | 70.0 ms                                                               | 78.7 ms: 1.12x slower                                           |
| nbody          | 80.0 ms                                                               | 92.2 ms: 1.15x slower                                           |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.64 ms: 1.06x faster                                           |
| regex_v8       | 25.3 ms                                                               | 24.1 ms: 1.05x faster                                           |
| regex_compile  | 134 ms                                                                | 135 ms: 1.01x slower                                            |
| regex_dna      | 222 ms                                                                | 228 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 28.1 us                                                               | 27.6 us: 1.02x faster                                           |
| unpickle_pure_python | 215 us                                                                | 220 us: 1.02x slower                                            |
| pickle_pure_python   | 293 us                                                                | 304 us: 1.04x slower                                            |
| xml_etree_process    | 57.5 ms                                                               | 60.6 ms: 1.05x slower                                           |
| xml_etree_parse      | 150 ms                                                                | 159 ms: 1.06x slower                                            |
| xml_etree_generate   | 81.6 ms                                                               | 86.9 ms: 1.06x slower                                           |
| xml_etree_iterparse  | 99.2 ms                                                               | 108 ms: 1.09x slower                                            |
| tomli_loads          | 1.92 sec                                                              | 2.24 sec: 1.16x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.06 ms: 1.01x faster                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 35.1 ms                                                               | 34.5 ms: 1.02x faster                                           |
| genshi_xml      | 58.0 ms                                                               | 57.1 ms: 1.02x faster                                           |
| genshi_text     | 24.9 ms                                                               | 25.7 ms: 1.03x slower                                           |
| mako            | 9.76 ms                                                               | 11.5 ms: 1.17x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| scimark_lu                 | 124 ms                                                                | 116 ms: 1.07x faster                                            |
| deltablue                  | 3.52 ms                                                               | 3.28 ms: 1.07x faster                                           |
| regex_effbot               | 3.86 ms                                                               | 3.64 ms: 1.06x faster                                           |
| sympy_expand               | 492 ms                                                                | 466 ms: 1.05x faster                                            |
| sympy_integrate            | 21.8 ms                                                               | 20.8 ms: 1.05x faster                                           |
| sympy_sum                  | 165 ms                                                                | 157 ms: 1.05x faster                                            |
| regex_v8                   | 25.3 ms                                                               | 24.1 ms: 1.05x faster                                           |
| deepcopy_reduce            | 2.78 us                                                               | 2.65 us: 1.05x faster                                           |
| sympy_str                  | 292 ms                                                                | 280 ms: 1.04x faster                                            |
| typing_runtime_protocols   | 172 us                                                                | 165 us: 1.04x faster                                            |
| dulwich_log                | 67.1 ms                                                               | 64.9 ms: 1.03x faster                                           |
| scimark_sor                | 129 ms                                                                | 125 ms: 1.03x faster                                            |
| django_template            | 35.1 ms                                                               | 34.5 ms: 1.02x faster                                           |
| json_loads                 | 28.1 us                                                               | 27.6 us: 1.02x faster                                           |
| pathlib                    | 16.2 ms                                                               | 16.0 ms: 1.02x faster                                           |
| genshi_xml                 | 58.0 ms                                                               | 57.1 ms: 1.02x faster                                           |
| deepcopy                   | 273 us                                                                | 269 us: 1.01x faster                                            |
| logging_silent             | 107 ns                                                                | 106 ns: 1.01x faster                                            |
| bench_thread_pool          | 832 us                                                                | 821 us: 1.01x faster                                            |
| thrift                     | 801 us                                                                | 791 us: 1.01x faster                                            |
| create_gc_cycles           | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                           |
| sqlglot_normalize          | 111 ms                                                                | 110 ms: 1.01x faster                                            |
| python_startup_no_site     | 7.10 ms                                                               | 7.06 ms: 1.01x faster                                           |
| tornado_http               | 92.4 ms                                                               | 91.9 ms: 1.01x faster                                           |
| gc_traversal               | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                           |
| 2to3                       | 271 ms                                                                | 270 ms: 1.00x faster                                            |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                          |
| pidigits                   | 186 ms                                                                | 187 ms: 1.00x slower                                            |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                           |
| coverage                   | 92.4 ms                                                               | 92.7 ms: 1.00x slower                                           |
| asyncio_tcp                | 488 ms                                                                | 490 ms: 1.00x slower                                            |
| regex_compile              | 134 ms                                                                | 135 ms: 1.01x slower                                            |
| logging_simple             | 5.42 us                                                               | 5.46 us: 1.01x slower                                           |
| bpe_tokeniser              | 4.84 sec                                                              | 4.87 sec: 1.01x slower                                          |
| sqlglot_transpile          | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                           |
| logging_format             | 5.94 us                                                               | 6.06 us: 1.02x slower                                           |
| async_generators           | 452 ms                                                                | 461 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 549 ms: 1.02x slower                                            |
| coroutines                 | 23.4 ms                                                               | 24.0 ms: 1.02x slower                                           |
| sqlglot_parse              | 1.27 ms                                                               | 1.30 ms: 1.02x slower                                           |
| unpickle_pure_python       | 215 us                                                                | 220 us: 1.02x slower                                            |
| telco                      | 8.08 ms                                                               | 8.30 ms: 1.03x slower                                           |
| regex_dna                  | 222 ms                                                                | 228 ms: 1.03x slower                                            |
| docutils                   | 2.87 sec                                                              | 2.96 sec: 1.03x slower                                          |
| genshi_text                | 24.9 ms                                                               | 25.7 ms: 1.03x slower                                           |
| pickle_pure_python         | 293 us                                                                | 304 us: 1.04x slower                                            |
| chaos                      | 58.1 ms                                                               | 60.2 ms: 1.04x slower                                           |
| meteor_contest             | 107 ms                                                                | 111 ms: 1.04x slower                                            |
| pprint_pformat             | 1.45 sec                                                              | 1.52 sec: 1.05x slower                                          |
| html5lib                   | 64.7 ms                                                               | 67.9 ms: 1.05x slower                                           |
| pprint_safe_repr           | 710 ms                                                                | 747 ms: 1.05x slower                                            |
| xml_etree_process          | 57.5 ms                                                               | 60.6 ms: 1.05x slower                                           |
| sqlglot_optimize           | 55.0 ms                                                               | 58.0 ms: 1.05x slower                                           |
| nqueens                    | 85.5 ms                                                               | 90.6 ms: 1.06x slower                                           |
| xml_etree_parse            | 150 ms                                                                | 159 ms: 1.06x slower                                            |
| xml_etree_generate         | 81.6 ms                                                               | 86.9 ms: 1.06x slower                                           |
| crypto_pyaes               | 67.8 ms                                                               | 72.9 ms: 1.07x slower                                           |
| async_tree_io              | 841 ms                                                                | 909 ms: 1.08x slower                                            |
| comprehensions             | 16.7 us                                                               | 18.0 us: 1.08x slower                                           |
| hexiom                     | 6.48 ms                                                               | 7.05 ms: 1.09x slower                                           |
| spectral_norm              | 104 ms                                                                | 113 ms: 1.09x slower                                            |
| xml_etree_iterparse        | 99.2 ms                                                               | 108 ms: 1.09x slower                                            |
| pyflate                    | 444 ms                                                                | 485 ms: 1.09x slower                                            |
| deepcopy_memo              | 28.4 us                                                               | 31.1 us: 1.10x slower                                           |
| mdp                        | 2.52 sec                                                              | 2.77 sec: 1.10x slower                                          |
| float                      | 70.0 ms                                                               | 78.7 ms: 1.12x slower                                           |
| richards                   | 41.8 ms                                                               | 47.0 ms: 1.13x slower                                           |
| richards_super             | 47.5 ms                                                               | 53.5 ms: 1.13x slower                                           |
| scimark_monte_carlo        | 61.1 ms                                                               | 69.4 ms: 1.14x slower                                           |
| fannkuch                   | 361 ms                                                                | 414 ms: 1.15x slower                                            |
| nbody                      | 80.0 ms                                                               | 92.2 ms: 1.15x slower                                           |
| tomli_loads                | 1.92 sec                                                              | 2.24 sec: 1.16x slower                                          |
| mako                       | 9.76 ms                                                               | 11.5 ms: 1.17x slower                                           |
| scimark_fft                | 309 ms                                                                | 369 ms: 1.20x slower                                            |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 5.20 ms: 1.22x slower                                           |
| generators                 | 29.5 ms                                                               | 45.8 ms: 1.55x slower                                           |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (15): dask, raytrace, json_dumps, bench_mp_pool, pycparser, go, asyncio_websockets, json, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_none_tg, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.97x