# Results vs. base

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 700ea07
- commit date: 2024-07-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 270 ms: 1.00x faster                                            |
| docutils       | 2.88 sec                                                              | 2.96 sec: 1.03x slower                                          |
| html5lib       | 65.4 ms                                                               | 67.9 ms: 1.04x slower                                           |
| tornado_http   | 93.8 ms                                                               | 91.9 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io  | 842 ms                                                                | 909 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 187 ms: 1.01x slower                                            |
| float          | 70.4 ms                                                               | 78.7 ms: 1.12x slower                                           |
| nbody          | 79.5 ms                                                               | 92.2 ms: 1.16x slower                                           |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 24.1 ms: 1.06x faster                                           |
| regex_effbot   | 3.84 ms                                                               | 3.64 ms: 1.05x faster                                           |
| regex_compile  | 135 ms                                                                | 135 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                           |
| unpickle_pure_python | 217 us                                                                | 220 us: 1.01x slower                                            |
| pickle_pure_python   | 296 us                                                                | 304 us: 1.03x slower                                            |
| xml_etree_process    | 57.5 ms                                                               | 60.6 ms: 1.05x slower                                           |
| xml_etree_generate   | 81.1 ms                                                               | 86.9 ms: 1.07x slower                                           |
| xml_etree_parse      | 148 ms                                                                | 159 ms: 1.07x slower                                            |
| xml_etree_iterparse  | 99.0 ms                                                               | 108 ms: 1.09x slower                                            |
| tomli_loads          | 1.93 sec                                                              | 2.24 sec: 1.16x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.05x slower                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 34.5 ms: 1.05x faster                                           |
| genshi_text     | 25.1 ms                                                               | 25.7 ms: 1.03x slower                                           |
| mako            | 9.77 ms                                                               | 11.5 ms: 1.17x slower                                           |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240711-linux-x86_64-brandtbucher-optimize-3.14.0a0-700ea07 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| deltablue                | 3.58 ms                                                               | 3.28 ms: 1.09x faster                                           |
| scimark_lu               | 126 ms                                                                | 116 ms: 1.09x faster                                            |
| sympy_sum                | 167 ms                                                                | 157 ms: 1.06x faster                                            |
| regex_v8                 | 25.5 ms                                                               | 24.1 ms: 1.06x faster                                           |
| sympy_expand             | 493 ms                                                                | 466 ms: 1.06x faster                                            |
| sympy_integrate          | 21.9 ms                                                               | 20.8 ms: 1.05x faster                                           |
| regex_effbot             | 3.84 ms                                                               | 3.64 ms: 1.05x faster                                           |
| scimark_sor              | 131 ms                                                                | 125 ms: 1.05x faster                                            |
| sympy_str                | 293 ms                                                                | 280 ms: 1.05x faster                                            |
| dulwich_log              | 68.0 ms                                                               | 64.9 ms: 1.05x faster                                           |
| django_template          | 36.1 ms                                                               | 34.5 ms: 1.05x faster                                           |
| deepcopy_reduce          | 2.76 us                                                               | 2.65 us: 1.04x faster                                           |
| typing_runtime_protocols | 171 us                                                                | 165 us: 1.03x faster                                            |
| asyncio_tcp              | 504 ms                                                                | 490 ms: 1.03x faster                                            |
| logging_simple           | 5.61 us                                                               | 5.46 us: 1.03x faster                                           |
| sqlglot_normalize        | 113 ms                                                                | 110 ms: 1.03x faster                                            |
| raytrace                 | 271 ms                                                                | 265 ms: 1.02x faster                                            |
| logging_silent           | 108 ns                                                                | 106 ns: 1.02x faster                                            |
| deepcopy                 | 274 us                                                                | 269 us: 1.02x faster                                            |
| tornado_http             | 93.8 ms                                                               | 91.9 ms: 1.02x faster                                           |
| logging_format           | 6.16 us                                                               | 6.06 us: 1.02x faster                                           |
| bench_thread_pool        | 833 us                                                                | 821 us: 1.02x faster                                            |
| create_gc_cycles         | 1.77 ms                                                               | 1.74 ms: 1.01x faster                                           |
| thrift                   | 799 us                                                                | 791 us: 1.01x faster                                            |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                            |
| python_startup_no_site   | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                           |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                          |
| regex_compile            | 135 ms                                                                | 135 ms: 1.00x faster                                            |
| 2to3                     | 272 ms                                                                | 270 ms: 1.00x faster                                            |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                           |
| pidigits                 | 185 ms                                                                | 187 ms: 1.01x slower                                            |
| json_dumps               | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                           |
| bpe_tokeniser            | 4.82 sec                                                              | 4.87 sec: 1.01x slower                                          |
| json                     | 5.15 ms                                                               | 5.21 ms: 1.01x slower                                           |
| async_generators         | 455 ms                                                                | 461 ms: 1.01x slower                                            |
| sqlglot_transpile        | 1.60 ms                                                               | 1.62 ms: 1.01x slower                                           |
| unpickle_pure_python     | 217 us                                                                | 220 us: 1.01x slower                                            |
| coroutines               | 23.5 ms                                                               | 24.0 ms: 1.02x slower                                           |
| mdp                      | 2.71 sec                                                              | 2.77 sec: 1.02x slower                                          |
| sqlglot_parse            | 1.28 ms                                                               | 1.30 ms: 1.02x slower                                           |
| gc_traversal             | 3.64 ms                                                               | 3.73 ms: 1.02x slower                                           |
| genshi_text              | 25.1 ms                                                               | 25.7 ms: 1.03x slower                                           |
| docutils                 | 2.88 sec                                                              | 2.96 sec: 1.03x slower                                          |
| pickle_pure_python       | 296 us                                                                | 304 us: 1.03x slower                                            |
| meteor_contest           | 108 ms                                                                | 111 ms: 1.03x slower                                            |
| html5lib                 | 65.4 ms                                                               | 67.9 ms: 1.04x slower                                           |
| pprint_pformat           | 1.46 sec                                                              | 1.52 sec: 1.04x slower                                          |
| sqlglot_optimize         | 55.7 ms                                                               | 58.0 ms: 1.04x slower                                           |
| chaos                    | 57.8 ms                                                               | 60.2 ms: 1.04x slower                                           |
| pprint_safe_repr         | 716 ms                                                                | 747 ms: 1.04x slower                                            |
| telco                    | 7.92 ms                                                               | 8.30 ms: 1.05x slower                                           |
| nqueens                  | 86.2 ms                                                               | 90.6 ms: 1.05x slower                                           |
| xml_etree_process        | 57.5 ms                                                               | 60.6 ms: 1.05x slower                                           |
| xml_etree_generate       | 81.1 ms                                                               | 86.9 ms: 1.07x slower                                           |
| xml_etree_parse          | 148 ms                                                                | 159 ms: 1.07x slower                                            |
| hexiom                   | 6.56 ms                                                               | 7.05 ms: 1.07x slower                                           |
| async_tree_io            | 842 ms                                                                | 909 ms: 1.08x slower                                            |
| comprehensions           | 16.7 us                                                               | 18.0 us: 1.08x slower                                           |
| crypto_pyaes             | 67.0 ms                                                               | 72.9 ms: 1.09x slower                                           |
| pyflate                  | 446 ms                                                                | 485 ms: 1.09x slower                                            |
| xml_etree_iterparse      | 99.0 ms                                                               | 108 ms: 1.09x slower                                            |
| deepcopy_memo            | 28.4 us                                                               | 31.1 us: 1.10x slower                                           |
| spectral_norm            | 101 ms                                                                | 113 ms: 1.12x slower                                            |
| float                    | 70.4 ms                                                               | 78.7 ms: 1.12x slower                                           |
| richards_super           | 47.7 ms                                                               | 53.5 ms: 1.12x slower                                           |
| richards                 | 41.5 ms                                                               | 47.0 ms: 1.13x slower                                           |
| fannkuch                 | 364 ms                                                                | 414 ms: 1.14x slower                                            |
| scimark_monte_carlo      | 60.8 ms                                                               | 69.4 ms: 1.14x slower                                           |
| nbody                    | 79.5 ms                                                               | 92.2 ms: 1.16x slower                                           |
| tomli_loads              | 1.93 sec                                                              | 2.24 sec: 1.16x slower                                          |
| mako                     | 9.77 ms                                                               | 11.5 ms: 1.17x slower                                           |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 5.20 ms: 1.19x slower                                           |
| scimark_fft              | 305 ms                                                                | 369 ms: 1.21x slower                                            |
| generators               | 29.8 ms                                                               | 45.8 ms: 1.54x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.03x slower                                                    |

Benchmark hidden because not significant (17): dask, pycparser, bench_mp_pool, coverage, asyncio_websockets, pathlib, async_tree_cpu_io_mixed, json_loads, genshi_xml, regex_dna, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x