# Results vs. base

- fork: brandtbucher
- ref: for_iter_tier_two_ex
- machine: linux-x86_64
- commit hash: e627230
- commit date: 2024-07-12
- overall geometric mean: 1.00x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.88 sec                                                              | 2.87 sec: 1.00x faster                                                      |
| html5lib       | 65.4 ms                                                               | 64.2 ms: 1.02x faster                                                       |
| tornado_http   | 93.8 ms                                                               | 92.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 69.7 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| nbody          | 79.5 ms                                                               | 80.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                | 221 ms: 1.03x faster                                                        |
| regex_v8       | 25.5 ms                                                               | 25.1 ms: 1.01x faster                                                       |
| regex_compile  | 135 ms                                                                | 134 ms: 1.01x faster                                                        |
| regex_effbot   | 3.84 ms                                                               | 3.81 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads        | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                      |
| xml_etree_process  | 57.5 ms                                                               | 56.9 ms: 1.01x faster                                                       |
| xml_etree_generate | 81.1 ms                                                               | 80.6 ms: 1.01x faster                                                       |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (6): pickle_pure_python, json_dumps, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 56.9 ms                                                               | 56.1 ms: 1.01x faster                                                       |
| django_template | 36.1 ms                                                               | 35.6 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240712-linux-x86_64-brandtbucher-for_iter_tier_two_ex-3.14.0a0-e627230 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| meteor_contest          | 108 ms                                                                | 104 ms: 1.03x faster                                                        |
| regex_dna               | 227 ms                                                                | 221 ms: 1.03x faster                                                        |
| logging_simple          | 5.61 us                                                               | 5.46 us: 1.03x faster                                                       |
| logging_silent          | 108 ns                                                                | 106 ns: 1.02x faster                                                        |
| html5lib                | 65.4 ms                                                               | 64.2 ms: 1.02x faster                                                       |
| logging_format          | 6.16 us                                                               | 6.05 us: 1.02x faster                                                       |
| go                      | 146 ms                                                                | 143 ms: 1.02x faster                                                        |
| deepcopy_reduce         | 2.76 us                                                               | 2.72 us: 1.01x faster                                                       |
| genshi_xml              | 56.9 ms                                                               | 56.1 ms: 1.01x faster                                                       |
| scimark_lu              | 126 ms                                                                | 124 ms: 1.01x faster                                                        |
| django_template         | 36.1 ms                                                               | 35.6 ms: 1.01x faster                                                       |
| regex_v8                | 25.5 ms                                                               | 25.1 ms: 1.01x faster                                                       |
| tomli_loads             | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                      |
| mdp                     | 2.71 sec                                                              | 2.68 sec: 1.01x faster                                                      |
| scimark_sor             | 131 ms                                                                | 130 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult | 4.37 ms                                                               | 4.33 ms: 1.01x faster                                                       |
| tornado_http            | 93.8 ms                                                               | 92.8 ms: 1.01x faster                                                       |
| pyflate                 | 446 ms                                                                | 441 ms: 1.01x faster                                                        |
| dulwich_log             | 68.0 ms                                                               | 67.3 ms: 1.01x faster                                                       |
| sqlglot_normalize       | 113 ms                                                                | 112 ms: 1.01x faster                                                        |
| xml_etree_process       | 57.5 ms                                                               | 56.9 ms: 1.01x faster                                                       |
| float                   | 70.4 ms                                                               | 69.7 ms: 1.01x faster                                                       |
| pathlib                 | 15.9 ms                                                               | 15.8 ms: 1.01x faster                                                       |
| hexiom                  | 6.56 ms                                                               | 6.50 ms: 1.01x faster                                                       |
| regex_compile           | 135 ms                                                                | 134 ms: 1.01x faster                                                        |
| asyncio_tcp             | 504 ms                                                                | 501 ms: 1.01x faster                                                        |
| richards                | 41.5 ms                                                               | 41.2 ms: 1.01x faster                                                       |
| coverage                | 92.7 ms                                                               | 92.0 ms: 1.01x faster                                                       |
| regex_effbot            | 3.84 ms                                                               | 3.81 ms: 1.01x faster                                                       |
| raytrace                | 271 ms                                                                | 269 ms: 1.01x faster                                                        |
| xml_etree_generate      | 81.1 ms                                                               | 80.6 ms: 1.01x faster                                                       |
| deltablue               | 3.58 ms                                                               | 3.56 ms: 1.00x faster                                                       |
| docutils                | 2.88 sec                                                              | 2.87 sec: 1.00x faster                                                      |
| bench_thread_pool       | 833 us                                                                | 830 us: 1.00x faster                                                        |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.80 sec: 1.00x faster                                                      |
| sqlglot_optimize        | 55.7 ms                                                               | 55.5 ms: 1.00x faster                                                       |
| pidigits                | 185 ms                                                                | 185 ms: 1.00x faster                                                        |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| python_startup_no_site  | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                                       |
| sympy_str               | 293 ms                                                                | 294 ms: 1.00x slower                                                        |
| sympy_expand            | 493 ms                                                                | 496 ms: 1.01x slower                                                        |
| generators              | 29.8 ms                                                               | 30.0 ms: 1.01x slower                                                       |
| async_generators        | 455 ms                                                                | 459 ms: 1.01x slower                                                        |
| sympy_integrate         | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| nbody                   | 79.5 ms                                                               | 80.3 ms: 1.01x slower                                                       |
| richards_super          | 47.7 ms                                                               | 48.3 ms: 1.01x slower                                                       |
| gc_traversal            | 3.64 ms                                                               | 3.71 ms: 1.02x slower                                                       |
| scimark_fft             | 305 ms                                                                | 316 ms: 1.03x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (42): mako, pprint_safe_repr, async_tree_cpu_io_mixed_tg, json, deepcopy, telco, typing_runtime_protocols, scimark_monte_carlo, coroutines, pycparser, pickle_pure_python, sympy_sum, thrift, crypto_pyaes, dask, async_tree_memoization_tg, async_tree_io_tg, json_dumps, async_tree_none_tg, genshi_text, pylint, unpickle_pure_python, sqlglot_parse, pprint_pformat, spectral_norm, xml_etree_parse, bench_mp_pool, create_gc_cycles, xml_etree_iterparse, 2to3, async_tree_memoization, async_tree_cpu_io_mixed, json_loads, asyncio_websockets, chaos, bpe_tokeniser, async_tree_none, deepcopy_memo, fannkuch, async_tree_io, nqueens, comprehensions

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x