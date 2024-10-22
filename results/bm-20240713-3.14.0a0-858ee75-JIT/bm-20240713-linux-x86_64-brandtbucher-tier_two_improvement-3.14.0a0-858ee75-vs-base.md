# Results vs. base

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 858ee75
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 97.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 273 ms: 1.00x slower                                                        |
| html5lib       | 65.4 ms                                                               | 63.6 ms: 1.03x faster                                                       |
| tornado_http   | 93.8 ms                                                               | 93.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 536 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| float          | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                | 134 ms: 1.01x faster                                                        |
| regex_v8       | 25.5 ms                                                               | 26.3 ms: 1.03x slower                                                       |
| regex_dna      | 227 ms                                                                | 238 ms: 1.05x slower                                                        |
| regex_effbot   | 3.84 ms                                                               | 4.03 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 217 us                                                                | 216 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| json_loads           | 27.5 us                                                               | 28.5 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_process, tomli_loads, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                                       |
| python_startup         | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 35.5 ms: 1.02x faster                                                       |
| mako            | 9.77 ms                                                               | 9.73 ms: 1.00x faster                                                       |
| genshi_xml      | 56.9 ms                                                               | 58.8 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.71 sec                                                              | 2.53 sec: 1.07x faster                                                      |
| bpe_tokeniser              | 4.82 sec                                                              | 4.61 sec: 1.04x faster                                                      |
| logging_simple             | 5.61 us                                                               | 5.43 us: 1.03x faster                                                       |
| html5lib                   | 65.4 ms                                                               | 63.6 ms: 1.03x faster                                                       |
| gc_traversal               | 3.64 ms                                                               | 3.55 ms: 1.03x faster                                                       |
| meteor_contest             | 108 ms                                                                | 106 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 536 ms: 1.02x faster                                                        |
| django_template            | 36.1 ms                                                               | 35.5 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 113 ms                                                                | 111 ms: 1.02x faster                                                        |
| pyflate                    | 446 ms                                                                | 439 ms: 1.02x faster                                                        |
| logging_silent             | 108 ns                                                                | 106 ns: 1.02x faster                                                        |
| go                         | 146 ms                                                                | 144 ms: 1.01x faster                                                        |
| create_gc_cycles           | 1.77 ms                                                               | 1.74 ms: 1.01x faster                                                       |
| raytrace                   | 271 ms                                                                | 268 ms: 1.01x faster                                                        |
| logging_format             | 6.16 us                                                               | 6.08 us: 1.01x faster                                                       |
| nqueens                    | 86.2 ms                                                               | 85.2 ms: 1.01x faster                                                       |
| dulwich_log                | 68.0 ms                                                               | 67.3 ms: 1.01x faster                                                       |
| regex_compile              | 135 ms                                                                | 134 ms: 1.01x faster                                                        |
| async_generators           | 455 ms                                                                | 451 ms: 1.01x faster                                                        |
| deltablue                  | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                       |
| deepcopy                   | 274 us                                                                | 272 us: 1.01x faster                                                        |
| tornado_http               | 93.8 ms                                                               | 93.0 ms: 1.01x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                               | 7.06 ms: 1.01x faster                                                       |
| thrift                     | 799 us                                                                | 793 us: 1.01x faster                                                        |
| comprehensions             | 16.7 us                                                               | 16.6 us: 1.01x faster                                                       |
| python_startup             | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 60.8 ms                                                               | 60.4 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 217 us                                                                | 216 us: 1.01x faster                                                        |
| xml_etree_iterparse        | 99.0 ms                                                               | 98.5 ms: 1.01x faster                                                       |
| mako                       | 9.77 ms                                                               | 9.73 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                      |
| pidigits                   | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| 2to3                       | 272 ms                                                                | 273 ms: 1.00x slower                                                        |
| sympy_expand               | 493 ms                                                                | 495 ms: 1.00x slower                                                        |
| coroutines                 | 23.5 ms                                                               | 23.7 ms: 1.01x slower                                                       |
| sympy_integrate            | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                       |
| float                      | 70.4 ms                                                               | 70.9 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| json_dumps                 | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                       |
| pycparser                  | 1.19 sec                                                              | 1.20 sec: 1.01x slower                                                      |
| richards                   | 41.5 ms                                                               | 42.0 ms: 1.01x slower                                                       |
| coverage                   | 92.7 ms                                                               | 93.9 ms: 1.01x slower                                                       |
| generators                 | 29.8 ms                                                               | 30.2 ms: 1.01x slower                                                       |
| telco                      | 7.92 ms                                                               | 8.08 ms: 1.02x slower                                                       |
| scimark_lu                 | 126 ms                                                                | 129 ms: 1.02x slower                                                        |
| scimark_fft                | 305 ms                                                                | 313 ms: 1.02x slower                                                        |
| spectral_norm              | 101 ms                                                                | 105 ms: 1.03x slower                                                        |
| regex_v8                   | 25.5 ms                                                               | 26.3 ms: 1.03x slower                                                       |
| genshi_xml                 | 56.9 ms                                                               | 58.8 ms: 1.03x slower                                                       |
| json_loads                 | 27.5 us                                                               | 28.5 us: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.37 ms                                                               | 4.54 ms: 1.04x slower                                                       |
| regex_dna                  | 227 ms                                                                | 238 ms: 1.05x slower                                                        |
| regex_effbot               | 3.84 ms                                                               | 4.03 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (38): xml_etree_parse, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, deepcopy_reduce, async_tree_cpu_io_mixed, async_tree_io, json, pprint_safe_repr, async_tree_memoization, scimark_sor, async_tree_none, pylint, deepcopy_memo, hexiom, xml_etree_process, asyncio_tcp, typing_runtime_protocols, sympy_sum, dask, crypto_pyaes, bench_thread_pool, sqlglot_optimize, bench_mp_pool, nbody, chaos, sqlglot_parse, richards_super, asyncio_websockets, docutils, genshi_text, tomli_loads, sympy_str, xml_etree_generate, pathlib, pickle_pure_python, fannkuch, pprint_pformat

# HPT report

- Reliability score: 97.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x