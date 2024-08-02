# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed
- machine: linux-x86_64
- commit hash: 190fbfa
- commit date: 2024-07-14
- overall geometric mean: 1.02x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 273 ms: 1.01x slower                                                      |
| docutils       | 2.87 sec                                                              | 2.98 sec: 1.04x slower                                                    |
| html5lib       | 64.7 ms                                                               | 71.6 ms: 1.11x slower                                                     |
| tornado_http   | 92.4 ms                                                               | 98.3 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 545 ms: 1.02x slower                                                      |
| async_tree_io_tg           | 845 ms                                                                | 867 ms: 1.03x slower                                                      |
| async_tree_io              | 841 ms                                                                | 910 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                               | 77.0 ms: 1.04x faster                                                     |
| float          | 70.0 ms                                                               | 70.4 ms: 1.01x slower                                                     |
| pidigits       | 186 ms                                                                | 188 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.61 ms: 1.07x faster                                                     |
| regex_v8       | 25.3 ms                                                               | 23.7 ms: 1.07x faster                                                     |
| regex_compile  | 134 ms                                                                | 132 ms: 1.01x faster                                                      |
| regex_dna      | 222 ms                                                                | 219 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 28.1 us                                                               | 27.5 us: 1.02x faster                                                     |
| xml_etree_parse      | 150 ms                                                                | 148 ms: 1.01x faster                                                      |
| unpickle_pure_python | 215 us                                                                | 215 us: 1.00x slower                                                      |
| xml_etree_process    | 57.5 ms                                                               | 58.6 ms: 1.02x slower                                                     |
| xml_etree_generate   | 81.6 ms                                                               | 84.3 ms: 1.03x slower                                                     |
| pickle_pure_python   | 293 us                                                                | 304 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 99.2 ms                                                               | 103 ms: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (2): tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.96 ms: 1.02x slower                                                     |
| genshi_xml      | 58.0 ms                                                               | 63.3 ms: 1.09x slower                                                     |
| genshi_text     | 24.9 ms                                                               | 27.7 ms: 1.11x slower                                                     |
| django_template | 35.1 ms                                                               | 40.4 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.09x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-no_progress_needed-3.14.0a0-190fbfa |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| richards                   | 41.8 ms                                                               | 39.1 ms: 1.07x faster                                                     |
| regex_effbot               | 3.86 ms                                                               | 3.61 ms: 1.07x faster                                                     |
| deepcopy_memo              | 28.4 us                                                               | 26.6 us: 1.07x faster                                                     |
| regex_v8                   | 25.3 ms                                                               | 23.7 ms: 1.07x faster                                                     |
| deepcopy                   | 273 us                                                                | 258 us: 1.05x faster                                                      |
| richards_super             | 47.5 ms                                                               | 45.3 ms: 1.05x faster                                                     |
| logging_silent             | 107 ns                                                                | 102 ns: 1.05x faster                                                      |
| pycparser                  | 1.18 sec                                                              | 1.13 sec: 1.05x faster                                                    |
| scimark_lu                 | 124 ms                                                                | 119 ms: 1.04x faster                                                      |
| nbody                      | 80.0 ms                                                               | 77.0 ms: 1.04x faster                                                     |
| chaos                      | 58.1 ms                                                               | 56.0 ms: 1.04x faster                                                     |
| deepcopy_reduce            | 2.78 us                                                               | 2.68 us: 1.03x faster                                                     |
| spectral_norm              | 104 ms                                                                | 101 ms: 1.03x faster                                                      |
| go                         | 145 ms                                                                | 140 ms: 1.03x faster                                                      |
| deltablue                  | 3.52 ms                                                               | 3.42 ms: 1.03x faster                                                     |
| json_loads                 | 28.1 us                                                               | 27.5 us: 1.02x faster                                                     |
| bpe_tokeniser              | 4.84 sec                                                              | 4.73 sec: 1.02x faster                                                    |
| json                       | 5.19 ms                                                               | 5.10 ms: 1.02x faster                                                     |
| pathlib                    | 16.2 ms                                                               | 15.9 ms: 1.02x faster                                                     |
| crypto_pyaes               | 67.8 ms                                                               | 66.7 ms: 1.02x faster                                                     |
| scimark_sor                | 129 ms                                                                | 127 ms: 1.02x faster                                                      |
| regex_compile              | 134 ms                                                                | 132 ms: 1.01x faster                                                      |
| xml_etree_parse            | 150 ms                                                                | 148 ms: 1.01x faster                                                      |
| regex_dna                  | 222 ms                                                                | 219 ms: 1.01x faster                                                      |
| telco                      | 8.08 ms                                                               | 8.00 ms: 1.01x faster                                                     |
| typing_runtime_protocols   | 172 us                                                                | 171 us: 1.01x faster                                                      |
| sympy_expand               | 492 ms                                                                | 489 ms: 1.01x faster                                                      |
| dulwich_log                | 67.1 ms                                                               | 66.7 ms: 1.01x faster                                                     |
| meteor_contest             | 107 ms                                                                | 106 ms: 1.00x faster                                                      |
| gc_traversal               | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                     |
| create_gc_cycles           | 1.76 ms                                                               | 1.76 ms: 1.00x faster                                                     |
| python_startup_no_site     | 7.10 ms                                                               | 7.13 ms: 1.00x slower                                                     |
| unpickle_pure_python       | 215 us                                                                | 215 us: 1.00x slower                                                      |
| float                      | 70.0 ms                                                               | 70.4 ms: 1.01x slower                                                     |
| hexiom                     | 6.48 ms                                                               | 6.52 ms: 1.01x slower                                                     |
| 2to3                       | 271 ms                                                                | 273 ms: 1.01x slower                                                      |
| thrift                     | 801 us                                                                | 807 us: 1.01x slower                                                      |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                                | 188 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 111 ms                                                                | 113 ms: 1.01x slower                                                      |
| pyflate                    | 444 ms                                                                | 449 ms: 1.01x slower                                                      |
| scimark_fft                | 309 ms                                                                | 313 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                                     |
| asyncio_tcp_ssl            | 1.80 sec                                                              | 1.82 sec: 1.01x slower                                                    |
| raytrace                   | 266 ms                                                                | 269 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 545 ms: 1.02x slower                                                      |
| fannkuch                   | 361 ms                                                                | 366 ms: 1.02x slower                                                      |
| sympy_sum                  | 165 ms                                                                | 168 ms: 1.02x slower                                                      |
| xml_etree_process          | 57.5 ms                                                               | 58.6 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 4.36 ms: 1.02x slower                                                     |
| mako                       | 9.76 ms                                                               | 9.96 ms: 1.02x slower                                                     |
| logging_simple             | 5.42 us                                                               | 5.54 us: 1.02x slower                                                     |
| async_tree_io_tg           | 845 ms                                                                | 867 ms: 1.03x slower                                                      |
| logging_format             | 5.94 us                                                               | 6.09 us: 1.03x slower                                                     |
| sympy_str                  | 292 ms                                                                | 300 ms: 1.03x slower                                                      |
| bench_thread_pool          | 832 us                                                                | 857 us: 1.03x slower                                                      |
| xml_etree_generate         | 81.6 ms                                                               | 84.3 ms: 1.03x slower                                                     |
| pickle_pure_python         | 293 us                                                                | 304 us: 1.03x slower                                                      |
| scimark_monte_carlo        | 61.1 ms                                                               | 63.4 ms: 1.04x slower                                                     |
| docutils                   | 2.87 sec                                                              | 2.98 sec: 1.04x slower                                                    |
| sqlglot_optimize           | 55.0 ms                                                               | 57.3 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 99.2 ms                                                               | 103 ms: 1.04x slower                                                      |
| dask                       | 362 ms                                                                | 384 ms: 1.06x slower                                                      |
| asyncio_tcp                | 488 ms                                                                | 518 ms: 1.06x slower                                                      |
| tornado_http               | 92.4 ms                                                               | 98.3 ms: 1.06x slower                                                     |
| async_tree_io              | 841 ms                                                                | 910 ms: 1.08x slower                                                      |
| mdp                        | 2.52 sec                                                              | 2.74 sec: 1.09x slower                                                    |
| genshi_xml                 | 58.0 ms                                                               | 63.3 ms: 1.09x slower                                                     |
| pylint                     | 334 ms                                                                | 368 ms: 1.10x slower                                                      |
| html5lib                   | 64.7 ms                                                               | 71.6 ms: 1.11x slower                                                     |
| genshi_text                | 24.9 ms                                                               | 27.7 ms: 1.11x slower                                                     |
| async_generators           | 452 ms                                                                | 514 ms: 1.14x slower                                                      |
| nqueens                    | 85.5 ms                                                               | 97.5 ms: 1.14x slower                                                     |
| django_template            | 35.1 ms                                                               | 40.4 ms: 1.15x slower                                                     |
| sympy_integrate            | 21.8 ms                                                               | 25.3 ms: 1.16x slower                                                     |
| coroutines                 | 23.4 ms                                                               | 27.6 ms: 1.18x slower                                                     |
| generators                 | 29.5 ms                                                               | 56.1 ms: 1.90x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (14): comprehensions, asyncio_websockets, bench_mp_pool, coverage, sqlglot_parse, tomli_loads, json_dumps, pprint_safe_repr, pprint_pformat, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x