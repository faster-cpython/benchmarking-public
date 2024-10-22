# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 268 ms: 1.01x faster                                                  |
| docutils       | 2.88 sec                                                              | 2.83 sec: 1.02x faster                                                |
| tornado_http   | 93.8 ms                                                               | 92.1 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 538 ms: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 79.5 ms                                                               | 75.6 ms: 1.05x faster                                                 |
| float          | 70.4 ms                                                               | 69.7 ms: 1.01x faster                                                 |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.84 ms                                                               | 3.64 ms: 1.05x faster                                                 |
| regex_v8       | 25.5 ms                                                               | 24.5 ms: 1.04x faster                                                 |
| regex_compile  | 135 ms                                                                | 132 ms: 1.02x faster                                                  |
| regex_dna      | 227 ms                                                                | 230 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                |
| unpickle_pure_python | 217 us                                                                | 217 us: 1.00x slower                                                  |
| xml_etree_generate   | 81.1 ms                                                               | 81.7 ms: 1.01x slower                                                 |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                                 |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 25.1 ms                                                               | 23.8 ms: 1.05x faster                                                 |
| genshi_xml     | 56.9 ms                                                               | 55.6 ms: 1.02x faster                                                 |
| mako           | 9.77 ms                                                               | 9.73 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pycparser                  | 1.19 sec                                                              | 1.12 sec: 1.06x faster                                                |
| mdp                        | 2.71 sec                                                              | 2.56 sec: 1.06x faster                                                |
| regex_effbot               | 3.84 ms                                                               | 3.64 ms: 1.05x faster                                                 |
| genshi_text                | 25.1 ms                                                               | 23.8 ms: 1.05x faster                                                 |
| nbody                      | 79.5 ms                                                               | 75.6 ms: 1.05x faster                                                 |
| richards_super             | 47.7 ms                                                               | 45.8 ms: 1.04x faster                                                 |
| pyflate                    | 446 ms                                                                | 429 ms: 1.04x faster                                                  |
| regex_v8                   | 25.5 ms                                                               | 24.5 ms: 1.04x faster                                                 |
| go                         | 146 ms                                                                | 141 ms: 1.04x faster                                                  |
| logging_simple             | 5.61 us                                                               | 5.42 us: 1.03x faster                                                 |
| logging_format             | 6.16 us                                                               | 5.99 us: 1.03x faster                                                 |
| sympy_sum                  | 167 ms                                                                | 163 ms: 1.03x faster                                                  |
| richards                   | 41.5 ms                                                               | 40.5 ms: 1.02x faster                                                 |
| genshi_xml                 | 56.9 ms                                                               | 55.6 ms: 1.02x faster                                                 |
| regex_compile              | 135 ms                                                                | 132 ms: 1.02x faster                                                  |
| docutils                   | 2.88 sec                                                              | 2.83 sec: 1.02x faster                                                |
| tornado_http               | 93.8 ms                                                               | 92.1 ms: 1.02x faster                                                 |
| hexiom                     | 6.56 ms                                                               | 6.45 ms: 1.02x faster                                                 |
| deepcopy                   | 274 us                                                                | 269 us: 1.02x faster                                                  |
| sqlglot_parse              | 1.28 ms                                                               | 1.26 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.60 ms                                                               | 1.57 ms: 1.02x faster                                                 |
| deepcopy_memo              | 28.4 us                                                               | 27.9 us: 1.02x faster                                                 |
| sqlglot_normalize          | 113 ms                                                                | 111 ms: 1.02x faster                                                  |
| sympy_str                  | 293 ms                                                                | 289 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 55.7 ms                                                               | 54.9 ms: 1.02x faster                                                 |
| raytrace                   | 271 ms                                                                | 268 ms: 1.01x faster                                                  |
| comprehensions             | 16.7 us                                                               | 16.5 us: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 545 ms                                                                | 538 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                                | 106 ms: 1.01x faster                                                  |
| 2to3                       | 272 ms                                                                | 268 ms: 1.01x faster                                                  |
| json                       | 5.15 ms                                                               | 5.09 ms: 1.01x faster                                                 |
| sympy_integrate            | 21.9 ms                                                               | 21.7 ms: 1.01x faster                                                 |
| coroutines                 | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                                 |
| typing_runtime_protocols   | 171 us                                                                | 169 us: 1.01x faster                                                  |
| dulwich_log                | 68.0 ms                                                               | 67.3 ms: 1.01x faster                                                 |
| float                      | 70.4 ms                                                               | 69.7 ms: 1.01x faster                                                 |
| sympy_expand               | 493 ms                                                                | 488 ms: 1.01x faster                                                  |
| tomli_loads                | 1.93 sec                                                              | 1.92 sec: 1.01x faster                                                |
| deltablue                  | 3.58 ms                                                               | 3.55 ms: 1.01x faster                                                 |
| asyncio_tcp                | 504 ms                                                                | 501 ms: 1.01x faster                                                  |
| mako                       | 9.77 ms                                                               | 9.73 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                |
| python_startup_no_site     | 7.11 ms                                                               | 7.12 ms: 1.00x slower                                                 |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                 |
| unpickle_pure_python       | 217 us                                                                | 217 us: 1.00x slower                                                  |
| pidigits                   | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| bpe_tokeniser              | 4.82 sec                                                              | 4.84 sec: 1.01x slower                                                |
| pathlib                    | 15.9 ms                                                               | 16.0 ms: 1.01x slower                                                 |
| thrift                     | 799 us                                                                | 804 us: 1.01x slower                                                  |
| xml_etree_generate         | 81.1 ms                                                               | 81.7 ms: 1.01x slower                                                 |
| create_gc_cycles           | 1.77 ms                                                               | 1.78 ms: 1.01x slower                                                 |
| regex_dna                  | 227 ms                                                                | 230 ms: 1.01x slower                                                  |
| json_dumps                 | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                 |
| spectral_norm              | 101 ms                                                                | 104 ms: 1.03x slower                                                  |
| scimark_fft                | 305 ms                                                                | 316 ms: 1.03x slower                                                  |
| telco                      | 7.92 ms                                                               | 8.23 ms: 1.04x slower                                                 |
| fannkuch                   | 364 ms                                                                | 380 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 4.37 ms                                                               | 4.57 ms: 1.05x slower                                                 |
| gc_traversal               | 3.64 ms                                                               | 3.88 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (32): pylint, pprint_safe_repr, async_tree_cpu_io_mixed, logging_silent, async_tree_memoization_tg, django_template, async_tree_none, pprint_pformat, async_tree_memoization, pickle_pure_python, deepcopy_reduce, async_tree_io_tg, dask, crypto_pyaes, async_tree_none_tg, coverage, xml_etree_parse, scimark_monte_carlo, generators, async_generators, scimark_sor, xml_etree_iterparse, bench_mp_pool, bench_thread_pool, nqueens, html5lib, asyncio_websockets, async_tree_io, scimark_lu, xml_etree_process, json_loads, chaos

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x