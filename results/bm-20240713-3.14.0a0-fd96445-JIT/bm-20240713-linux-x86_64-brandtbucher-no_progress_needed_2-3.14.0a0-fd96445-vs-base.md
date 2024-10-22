# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 78.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 276 ms: 1.02x slower                                                        |
| html5lib       | 65.4 ms                                                               | 65.1 ms: 1.00x faster                                                       |
| tornado_http   | 93.8 ms                                                               | 93.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io  | 842 ms                                                                | 893 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                                | 222 ms: 1.02x faster                                                        |
| regex_effbot   | 3.84 ms                                                               | 3.77 ms: 1.02x faster                                                       |
| regex_compile  | 135 ms                                                                | 137 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 148 ms                                                                | 146 ms: 1.01x faster                                                        |
| unpickle_pure_python | 217 us                                                                | 215 us: 1.01x faster                                                        |
| tomli_loads          | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| xml_etree_iterparse  | 99.0 ms                                                               | 99.5 ms: 1.00x slower                                                       |
| json_dumps           | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| xml_etree_process    | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                       |
| xml_etree_generate   | 81.1 ms                                                               | 83.1 ms: 1.02x slower                                                       |
| json_loads           | 27.5 us                                                               | 28.3 us: 1.03x slower                                                       |
| pickle_pure_python   | 296 us                                                                | 304 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.15 ms: 1.01x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 9.77 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| genshi_text    | 25.1 ms                                                               | 25.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                 | 41.5 ms                                                               | 37.7 ms: 1.10x faster                                                       |
| richards_super           | 47.7 ms                                                               | 43.9 ms: 1.08x faster                                                       |
| mdp                      | 2.71 sec                                                              | 2.56 sec: 1.06x faster                                                      |
| deltablue                | 3.58 ms                                                               | 3.42 ms: 1.05x faster                                                       |
| logging_silent           | 108 ns                                                                | 103 ns: 1.04x faster                                                        |
| deepcopy_memo            | 28.4 us                                                               | 27.3 us: 1.04x faster                                                       |
| pyflate                  | 446 ms                                                                | 433 ms: 1.03x faster                                                        |
| dulwich_log              | 68.0 ms                                                               | 66.1 ms: 1.03x faster                                                       |
| regex_dna                | 227 ms                                                                | 222 ms: 1.02x faster                                                        |
| regex_effbot             | 3.84 ms                                                               | 3.77 ms: 1.02x faster                                                       |
| mako                     | 9.77 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| sqlglot_normalize        | 113 ms                                                                | 111 ms: 1.02x faster                                                        |
| logging_simple           | 5.61 us                                                               | 5.52 us: 1.02x faster                                                       |
| typing_runtime_protocols | 171 us                                                                | 168 us: 1.01x faster                                                        |
| logging_format           | 6.16 us                                                               | 6.08 us: 1.01x faster                                                       |
| raytrace                 | 271 ms                                                                | 268 ms: 1.01x faster                                                        |
| meteor_contest           | 108 ms                                                                | 106 ms: 1.01x faster                                                        |
| xml_etree_parse          | 148 ms                                                                | 146 ms: 1.01x faster                                                        |
| bpe_tokeniser            | 4.82 sec                                                              | 4.77 sec: 1.01x faster                                                      |
| chaos                    | 57.8 ms                                                               | 57.3 ms: 1.01x faster                                                       |
| sympy_str                | 293 ms                                                                | 291 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 217 us                                                                | 215 us: 1.01x faster                                                        |
| tomli_loads              | 1.93 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                      |
| bench_thread_pool        | 833 us                                                                | 828 us: 1.01x faster                                                        |
| sqlglot_parse            | 1.28 ms                                                               | 1.27 ms: 1.01x faster                                                       |
| tornado_http             | 93.8 ms                                                               | 93.2 ms: 1.01x faster                                                       |
| go                       | 146 ms                                                                | 145 ms: 1.00x faster                                                        |
| html5lib                 | 65.4 ms                                                               | 65.1 ms: 1.00x faster                                                       |
| create_gc_cycles         | 1.77 ms                                                               | 1.76 ms: 1.00x faster                                                       |
| async_generators         | 455 ms                                                                | 456 ms: 1.00x slower                                                        |
| gc_traversal             | 3.64 ms                                                               | 3.65 ms: 1.00x slower                                                       |
| xml_etree_iterparse      | 99.0 ms                                                               | 99.5 ms: 1.00x slower                                                       |
| python_startup_no_site   | 7.11 ms                                                               | 7.15 ms: 1.01x slower                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| pidigits                 | 185 ms                                                                | 186 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| pathlib                  | 15.9 ms                                                               | 16.0 ms: 1.01x slower                                                       |
| sympy_expand             | 493 ms                                                                | 497 ms: 1.01x slower                                                        |
| thrift                   | 799 us                                                                | 805 us: 1.01x slower                                                        |
| genshi_text              | 25.1 ms                                                               | 25.4 ms: 1.01x slower                                                       |
| json_dumps               | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| regex_compile            | 135 ms                                                                | 137 ms: 1.02x slower                                                        |
| 2to3                     | 272 ms                                                                | 276 ms: 1.02x slower                                                        |
| scimark_fft              | 305 ms                                                                | 310 ms: 1.02x slower                                                        |
| crypto_pyaes             | 67.0 ms                                                               | 68.1 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.45 ms: 1.02x slower                                                       |
| xml_etree_process        | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                       |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.02x slower                                                        |
| hexiom                   | 6.56 ms                                                               | 6.69 ms: 1.02x slower                                                       |
| pprint_safe_repr         | 716 ms                                                                | 733 ms: 1.02x slower                                                        |
| xml_etree_generate       | 81.1 ms                                                               | 83.1 ms: 1.02x slower                                                       |
| json_loads               | 27.5 us                                                               | 28.3 us: 1.03x slower                                                       |
| pickle_pure_python       | 296 us                                                                | 304 us: 1.03x slower                                                        |
| pprint_pformat           | 1.46 sec                                                              | 1.51 sec: 1.03x slower                                                      |
| async_tree_io            | 842 ms                                                                | 893 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (35): fannkuch, django_template, coverage, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, sympy_sum, docutils, generators, dask, coroutines, sqlglot_optimize, sympy_integrate, nbody, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_websockets, asyncio_tcp, regex_v8, genshi_xml, scimark_lu, deepcopy_reduce, comprehensions, pycparser, scimark_sor, float, async_tree_io_tg, telco, nqueens, json, async_tree_memoization_tg, deepcopy, async_tree_memoization, async_tree_none, pylint, async_tree_none_tg

# HPT report

- Reliability score: 78.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x