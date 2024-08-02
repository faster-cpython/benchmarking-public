# Results vs. base

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: ae6f199
- commit date: 2024-07-08
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 275 ms: 1.01x slower                                                      |
| docutils       | 2.87 sec                                                              | 3.00 sec: 1.05x slower                                                    |
| html5lib       | 64.7 ms                                                               | 67.4 ms: 1.04x slower                                                     |
| tornado_http   | 92.4 ms                                                               | 96.8 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 543 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 70.0 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                                | 187 ms: 1.01x slower                                                      |
| nbody          | 80.0 ms                                                               | 81.0 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.70 ms: 1.04x faster                                                     |
| regex_v8       | 25.3 ms                                                               | 24.7 ms: 1.02x faster                                                     |
| regex_compile  | 134 ms                                                                | 140 ms: 1.04x slower                                                      |
| regex_dna      | 222 ms                                                                | 232 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 215 us                                                                | 206 us: 1.04x faster                                                      |
| json_loads           | 28.1 us                                                               | 27.8 us: 1.01x faster                                                     |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| pickle_pure_python   | 293 us                                                                | 295 us: 1.00x slower                                                      |
| xml_etree_iterparse  | 99.2 ms                                                               | 99.7 ms: 1.00x slower                                                     |
| xml_etree_process    | 57.5 ms                                                               | 57.9 ms: 1.01x slower                                                     |
| xml_etree_generate   | 81.6 ms                                                               | 82.2 ms: 1.01x slower                                                     |
| tomli_loads          | 1.92 sec                                                              | 2.03 sec: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.10 ms: 1.00x faster                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| genshi_xml      | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                     |
| genshi_text     | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                                     |
| django_template | 35.1 ms                                                               | 36.9 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                | 98.1 ns: 1.09x faster                                                     |
| scimark_monte_carlo        | 61.1 ms                                                               | 57.4 ms: 1.07x faster                                                     |
| gc_traversal               | 3.74 ms                                                               | 3.55 ms: 1.05x faster                                                     |
| regex_effbot               | 3.86 ms                                                               | 3.70 ms: 1.04x faster                                                     |
| unpickle_pure_python       | 215 us                                                                | 206 us: 1.04x faster                                                      |
| pycparser                  | 1.18 sec                                                              | 1.15 sec: 1.03x faster                                                    |
| regex_v8                   | 25.3 ms                                                               | 24.7 ms: 1.02x faster                                                     |
| telco                      | 8.08 ms                                                               | 7.89 ms: 1.02x faster                                                     |
| spectral_norm              | 104 ms                                                                | 102 ms: 1.02x faster                                                      |
| pathlib                    | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                     |
| create_gc_cycles           | 1.76 ms                                                               | 1.74 ms: 1.01x faster                                                     |
| json_loads                 | 28.1 us                                                               | 27.8 us: 1.01x faster                                                     |
| bpe_tokeniser              | 4.84 sec                                                              | 4.79 sec: 1.01x faster                                                    |
| float                      | 70.0 ms                                                               | 69.5 ms: 1.01x faster                                                     |
| json_dumps                 | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.10 ms                                                               | 7.10 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                                    |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                     |
| pickle_pure_python         | 293 us                                                                | 295 us: 1.00x slower                                                      |
| xml_etree_iterparse        | 99.2 ms                                                               | 99.7 ms: 1.00x slower                                                     |
| mako                       | 9.76 ms                                                               | 9.81 ms: 1.00x slower                                                     |
| pidigits                   | 186 ms                                                                | 187 ms: 1.01x slower                                                      |
| xml_etree_process          | 57.5 ms                                                               | 57.9 ms: 1.01x slower                                                     |
| thrift                     | 801 us                                                                | 807 us: 1.01x slower                                                      |
| xml_etree_generate         | 81.6 ms                                                               | 82.2 ms: 1.01x slower                                                     |
| pyflate                    | 444 ms                                                                | 448 ms: 1.01x slower                                                      |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 55.0 ms                                                               | 55.6 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 543 ms: 1.01x slower                                                      |
| nqueens                    | 85.5 ms                                                               | 86.5 ms: 1.01x slower                                                     |
| nbody                      | 80.0 ms                                                               | 81.0 ms: 1.01x slower                                                     |
| raytrace                   | 266 ms                                                                | 269 ms: 1.01x slower                                                      |
| 2to3                       | 271 ms                                                                | 275 ms: 1.01x slower                                                      |
| genshi_xml                 | 58.0 ms                                                               | 58.7 ms: 1.01x slower                                                     |
| chaos                      | 58.1 ms                                                               | 58.8 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 4.33 ms: 1.01x slower                                                     |
| genshi_text                | 24.9 ms                                                               | 25.2 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                                     |
| deepcopy_memo              | 28.4 us                                                               | 28.8 us: 1.01x slower                                                     |
| bench_thread_pool          | 832 us                                                                | 845 us: 1.01x slower                                                      |
| generators                 | 29.5 ms                                                               | 30.0 ms: 1.02x slower                                                     |
| dulwich_log                | 67.1 ms                                                               | 68.2 ms: 1.02x slower                                                     |
| dask                       | 362 ms                                                                | 368 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                               | 1.30 ms: 1.02x slower                                                     |
| scimark_sor                | 129 ms                                                                | 131 ms: 1.02x slower                                                      |
| scimark_fft                | 309 ms                                                                | 316 ms: 1.02x slower                                                      |
| sqlglot_normalize          | 111 ms                                                                | 114 ms: 1.02x slower                                                      |
| sympy_sum                  | 165 ms                                                                | 169 ms: 1.02x slower                                                      |
| sympy_integrate            | 21.8 ms                                                               | 22.5 ms: 1.03x slower                                                     |
| richards                   | 41.8 ms                                                               | 43.1 ms: 1.03x slower                                                     |
| asyncio_tcp                | 488 ms                                                                | 504 ms: 1.03x slower                                                      |
| hexiom                     | 6.48 ms                                                               | 6.68 ms: 1.03x slower                                                     |
| logging_simple             | 5.42 us                                                               | 5.61 us: 1.03x slower                                                     |
| sympy_str                  | 292 ms                                                                | 302 ms: 1.03x slower                                                      |
| logging_format             | 5.94 us                                                               | 6.15 us: 1.04x slower                                                     |
| sympy_expand               | 492 ms                                                                | 512 ms: 1.04x slower                                                      |
| html5lib                   | 64.7 ms                                                               | 67.4 ms: 1.04x slower                                                     |
| regex_compile              | 134 ms                                                                | 140 ms: 1.04x slower                                                      |
| regex_dna                  | 222 ms                                                                | 232 ms: 1.05x slower                                                      |
| docutils                   | 2.87 sec                                                              | 3.00 sec: 1.05x slower                                                    |
| tornado_http               | 92.4 ms                                                               | 96.8 ms: 1.05x slower                                                     |
| django_template            | 35.1 ms                                                               | 36.9 ms: 1.05x slower                                                     |
| tomli_loads                | 1.92 sec                                                              | 2.03 sec: 1.06x slower                                                    |
| pylint                     | 334 ms                                                                | 358 ms: 1.07x slower                                                      |
| mdp                        | 2.52 sec                                                              | 2.74 sec: 1.09x slower                                                    |
| deltablue                  | 3.52 ms                                                               | 4.20 ms: 1.19x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (25): deepcopy_reduce, async_tree_io, deepcopy, xml_etree_parse, pprint_safe_repr, async_tree_io_tg, async_tree_none_tg, comprehensions, typing_runtime_protocols, json, go, crypto_pyaes, bench_mp_pool, async_generators, richards_super, async_tree_none, scimark_lu, async_tree_memoization_tg, asyncio_websockets, coverage, coroutines, fannkuch, pprint_pformat, async_tree_memoization, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x