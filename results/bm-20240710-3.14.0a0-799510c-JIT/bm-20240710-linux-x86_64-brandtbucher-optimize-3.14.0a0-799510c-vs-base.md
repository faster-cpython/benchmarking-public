# Results vs. base

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.87 sec                                                              | 6.74 sec: 2.35x slower                                          |
| html5lib       | 64.7 ms                                                               | 77.0 ms: 1.19x slower                                           |
| tornado_http   | 92.4 ms                                                               | 97.9 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                                 | 1.31x slower                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 845 ms                                                                | 863 ms: 1.02x slower                                            |
| async_tree_cpu_io_mixed    | 559 ms                                                                | 573 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 552 ms: 1.03x slower                                            |
| async_tree_io              | 841 ms                                                                | 896 ms: 1.07x slower                                            |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 80.0 ms                                                               | 77.4 ms: 1.03x faster                                           |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                            |
| float          | 70.0 ms                                                               | 70.9 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 130 ms: 1.03x faster                                            |
| regex_effbot   | 3.86 ms                                                               | 3.88 ms: 1.01x slower                                           |
| regex_dna      | 222 ms                                                                | 223 ms: 1.01x slower                                            |
| regex_v8       | 25.3 ms                                                               | 25.6 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 28.1 us                                                               | 27.4 us: 1.03x faster                                           |
| xml_etree_parse      | 150 ms                                                                | 148 ms: 1.01x faster                                            |
| tomli_loads          | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                          |
| xml_etree_process    | 57.5 ms                                                               | 58.1 ms: 1.01x slower                                           |
| unpickle_pure_python | 215 us                                                                | 218 us: 1.01x slower                                            |
| xml_etree_iterparse  | 99.2 ms                                                               | 102 ms: 1.03x slower                                            |
| pickle_pure_python   | 293 us                                                                | 303 us: 1.03x slower                                            |
| xml_etree_generate   | 81.6 ms                                                               | 84.8 ms: 1.04x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                           |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.87 ms: 1.01x slower                                           |
| genshi_xml      | 58.0 ms                                                               | 62.2 ms: 1.07x slower                                           |
| genshi_text     | 24.9 ms                                                               | 27.0 ms: 1.08x slower                                           |
| django_template | 35.1 ms                                                               | 40.3 ms: 1.15x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.08x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| richards                   | 41.8 ms                                                               | 38.5 ms: 1.09x faster                                           |
| richards_super             | 47.5 ms                                                               | 44.6 ms: 1.07x faster                                           |
| spectral_norm              | 104 ms                                                                | 98.0 ms: 1.06x faster                                           |
| deepcopy_reduce            | 2.78 us                                                               | 2.64 us: 1.05x faster                                           |
| logging_silent             | 107 ns                                                                | 102 ns: 1.05x faster                                            |
| deepcopy                   | 273 us                                                                | 261 us: 1.05x faster                                            |
| deepcopy_memo              | 28.4 us                                                               | 27.2 us: 1.04x faster                                           |
| chaos                      | 58.1 ms                                                               | 56.0 ms: 1.04x faster                                           |
| nbody                      | 80.0 ms                                                               | 77.4 ms: 1.03x faster                                           |
| go                         | 145 ms                                                                | 140 ms: 1.03x faster                                            |
| typing_runtime_protocols   | 172 us                                                                | 167 us: 1.03x faster                                            |
| regex_compile              | 134 ms                                                                | 130 ms: 1.03x faster                                            |
| deltablue                  | 3.52 ms                                                               | 3.43 ms: 1.03x faster                                           |
| scimark_lu                 | 124 ms                                                                | 121 ms: 1.03x faster                                            |
| json_loads                 | 28.1 us                                                               | 27.4 us: 1.03x faster                                           |
| dulwich_log                | 67.1 ms                                                               | 65.4 ms: 1.03x faster                                           |
| telco                      | 8.08 ms                                                               | 7.90 ms: 1.02x faster                                           |
| json                       | 5.19 ms                                                               | 5.08 ms: 1.02x faster                                           |
| scimark_sor                | 129 ms                                                                | 126 ms: 1.02x faster                                            |
| crypto_pyaes               | 67.8 ms                                                               | 66.6 ms: 1.02x faster                                           |
| bpe_tokeniser              | 4.84 sec                                                              | 4.76 sec: 1.02x faster                                          |
| xml_etree_parse            | 150 ms                                                                | 148 ms: 1.01x faster                                            |
| pycparser                  | 1.18 sec                                                              | 1.16 sec: 1.01x faster                                          |
| pathlib                    | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                           |
| create_gc_cycles           | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                           |
| comprehensions             | 16.7 us                                                               | 16.6 us: 1.01x faster                                           |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x faster                                            |
| python_startup_no_site     | 7.10 ms                                                               | 7.12 ms: 1.00x slower                                           |
| sympy_expand               | 492 ms                                                                | 493 ms: 1.00x slower                                            |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                           |
| regex_effbot               | 3.86 ms                                                               | 3.88 ms: 1.01x slower                                           |
| hexiom                     | 6.48 ms                                                               | 6.52 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.81 sec: 1.01x slower                                          |
| regex_dna                  | 222 ms                                                                | 223 ms: 1.01x slower                                            |
| sqlglot_parse              | 1.27 ms                                                               | 1.28 ms: 1.01x slower                                           |
| tomli_loads                | 1.92 sec                                                              | 1.94 sec: 1.01x slower                                          |
| coverage                   | 92.4 ms                                                               | 93.3 ms: 1.01x slower                                           |
| xml_etree_process          | 57.5 ms                                                               | 58.1 ms: 1.01x slower                                           |
| mako                       | 9.76 ms                                                               | 9.87 ms: 1.01x slower                                           |
| float                      | 70.0 ms                                                               | 70.9 ms: 1.01x slower                                           |
| unpickle_pure_python       | 215 us                                                                | 218 us: 1.01x slower                                            |
| regex_v8                   | 25.3 ms                                                               | 25.6 ms: 1.01x slower                                           |
| gc_traversal               | 3.74 ms                                                               | 3.80 ms: 1.02x slower                                           |
| sympy_sum                  | 165 ms                                                                | 168 ms: 1.02x slower                                            |
| logging_simple             | 5.42 us                                                               | 5.54 us: 1.02x slower                                           |
| async_tree_io_tg           | 845 ms                                                                | 863 ms: 1.02x slower                                            |
| sqlglot_normalize          | 111 ms                                                                | 114 ms: 1.02x slower                                            |
| scimark_fft                | 309 ms                                                                | 316 ms: 1.02x slower                                            |
| bench_thread_pool          | 832 us                                                                | 853 us: 1.03x slower                                            |
| async_tree_cpu_io_mixed    | 559 ms                                                                | 573 ms: 1.03x slower                                            |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 552 ms: 1.03x slower                                            |
| logging_format             | 5.94 us                                                               | 6.11 us: 1.03x slower                                           |
| sqlglot_transpile          | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                           |
| xml_etree_iterparse        | 99.2 ms                                                               | 102 ms: 1.03x slower                                            |
| pickle_pure_python         | 293 us                                                                | 303 us: 1.03x slower                                            |
| sympy_str                  | 292 ms                                                                | 302 ms: 1.03x slower                                            |
| xml_etree_generate         | 81.6 ms                                                               | 84.8 ms: 1.04x slower                                           |
| pyflate                    | 444 ms                                                                | 463 ms: 1.04x slower                                            |
| fannkuch                   | 361 ms                                                                | 377 ms: 1.05x slower                                            |
| scimark_monte_carlo        | 61.1 ms                                                               | 64.1 ms: 1.05x slower                                           |
| asyncio_tcp                | 488 ms                                                                | 516 ms: 1.06x slower                                            |
| dask                       | 362 ms                                                                | 383 ms: 1.06x slower                                            |
| tornado_http               | 92.4 ms                                                               | 97.9 ms: 1.06x slower                                           |
| async_tree_io              | 841 ms                                                                | 896 ms: 1.07x slower                                            |
| mdp                        | 2.52 sec                                                              | 2.70 sec: 1.07x slower                                          |
| genshi_xml                 | 58.0 ms                                                               | 62.2 ms: 1.07x slower                                           |
| genshi_text                | 24.9 ms                                                               | 27.0 ms: 1.08x slower                                           |
| sqlglot_optimize           | 55.0 ms                                                               | 60.0 ms: 1.09x slower                                           |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 4.67 ms: 1.09x slower                                           |
| nqueens                    | 85.5 ms                                                               | 94.1 ms: 1.10x slower                                           |
| async_generators           | 452 ms                                                                | 514 ms: 1.14x slower                                            |
| django_template            | 35.1 ms                                                               | 40.3 ms: 1.15x slower                                           |
| sympy_integrate            | 21.8 ms                                                               | 25.3 ms: 1.16x slower                                           |
| coroutines                 | 23.4 ms                                                               | 27.5 ms: 1.18x slower                                           |
| html5lib                   | 64.7 ms                                                               | 77.0 ms: 1.19x slower                                           |
| pylint                     | 334 ms                                                                | 425 ms: 1.27x slower                                            |
| generators                 | 29.5 ms                                                               | 47.6 ms: 1.61x slower                                           |
| docutils                   | 2.87 sec                                                              | 6.74 sec: 2.35x slower                                          |
| raytrace                   | 266 ms                                                                | 4.85 sec: 18.25x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                    |

Benchmark hidden because not significant (12): asyncio_websockets, json_dumps, 2to3, bench_mp_pool, meteor_contest, thrift, pprint_safe_repr, pprint_pformat, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x