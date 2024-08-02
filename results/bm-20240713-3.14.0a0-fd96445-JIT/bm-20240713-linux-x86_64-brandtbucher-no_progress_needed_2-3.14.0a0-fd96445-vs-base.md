# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.00x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 276 ms: 1.02x slower                                                        |
| docutils       | 2.87 sec                                                              | 2.88 sec: 1.00x slower                                                      |
| html5lib       | 64.7 ms                                                               | 65.1 ms: 1.01x slower                                                       |
| tornado_http   | 92.4 ms                                                               | 93.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io  | 841 ms                                                                | 893 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                               | 79.4 ms: 1.01x faster                                                       |
| float          | 70.0 ms                                                               | 70.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.77 ms: 1.02x faster                                                       |
| regex_v8       | 25.3 ms                                                               | 25.5 ms: 1.01x slower                                                       |
| regex_compile  | 134 ms                                                                | 137 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 150 ms                                                                | 146 ms: 1.03x faster                                                        |
| tomli_loads         | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| xml_etree_iterparse | 99.2 ms                                                               | 99.5 ms: 1.00x slower                                                       |
| json_dumps          | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| xml_etree_process   | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                       |
| xml_etree_generate  | 81.6 ms                                                               | 83.1 ms: 1.02x slower                                                       |
| pickle_pure_python  | 293 us                                                                | 304 us: 1.03x slower                                                        |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.15 ms: 1.01x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.76 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| genshi_xml      | 58.0 ms                                                               | 57.0 ms: 1.02x faster                                                       |
| django_template | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                       |
| genshi_text     | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards                 | 41.8 ms                                                               | 37.7 ms: 1.11x faster                                                       |
| richards_super           | 47.5 ms                                                               | 43.9 ms: 1.08x faster                                                       |
| deepcopy_memo            | 28.4 us                                                               | 27.3 us: 1.04x faster                                                       |
| logging_silent           | 107 ns                                                                | 103 ns: 1.04x faster                                                        |
| deltablue                | 3.52 ms                                                               | 3.42 ms: 1.03x faster                                                       |
| xml_etree_parse          | 150 ms                                                                | 146 ms: 1.03x faster                                                        |
| pyflate                  | 444 ms                                                                | 433 ms: 1.03x faster                                                        |
| gc_traversal             | 3.74 ms                                                               | 3.65 ms: 1.02x faster                                                       |
| regex_effbot             | 3.86 ms                                                               | 3.77 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 172 us                                                                | 168 us: 1.02x faster                                                        |
| mako                     | 9.76 ms                                                               | 9.60 ms: 1.02x faster                                                       |
| genshi_xml               | 58.0 ms                                                               | 57.0 ms: 1.02x faster                                                       |
| bpe_tokeniser            | 4.84 sec                                                              | 4.77 sec: 1.01x faster                                                      |
| dulwich_log              | 67.1 ms                                                               | 66.1 ms: 1.01x faster                                                       |
| telco                    | 8.08 ms                                                               | 7.97 ms: 1.01x faster                                                       |
| chaos                    | 58.1 ms                                                               | 57.3 ms: 1.01x faster                                                       |
| scimark_monte_carlo      | 61.1 ms                                                               | 60.5 ms: 1.01x faster                                                       |
| pathlib                  | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                       |
| nbody                    | 80.0 ms                                                               | 79.4 ms: 1.01x faster                                                       |
| tomli_loads              | 1.92 sec                                                              | 1.91 sec: 1.01x faster                                                      |
| bench_thread_pool        | 832 us                                                                | 828 us: 1.01x faster                                                        |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.00x faster                                                        |
| sympy_str                | 292 ms                                                                | 291 ms: 1.00x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x slower                                                       |
| xml_etree_iterparse      | 99.2 ms                                                               | 99.5 ms: 1.00x slower                                                       |
| sympy_integrate          | 21.8 ms                                                               | 21.9 ms: 1.00x slower                                                       |
| docutils                 | 2.87 sec                                                              | 2.88 sec: 1.00x slower                                                      |
| scimark_fft              | 309 ms                                                                | 310 ms: 1.00x slower                                                        |
| generators               | 29.5 ms                                                               | 29.7 ms: 1.01x slower                                                       |
| sqlglot_transpile        | 1.60 ms                                                               | 1.61 ms: 1.01x slower                                                       |
| html5lib                 | 64.7 ms                                                               | 65.1 ms: 1.01x slower                                                       |
| json_dumps               | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                       |
| python_startup_no_site   | 7.10 ms                                                               | 7.15 ms: 1.01x slower                                                       |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                       |
| comprehensions           | 16.7 us                                                               | 16.8 us: 1.01x slower                                                       |
| raytrace                 | 266 ms                                                                | 268 ms: 1.01x slower                                                        |
| pycparser                | 1.18 sec                                                              | 1.19 sec: 1.01x slower                                                      |
| tornado_http             | 92.4 ms                                                               | 93.2 ms: 1.01x slower                                                       |
| sympy_expand             | 492 ms                                                                | 497 ms: 1.01x slower                                                        |
| regex_v8                 | 25.3 ms                                                               | 25.5 ms: 1.01x slower                                                       |
| async_generators         | 452 ms                                                                | 456 ms: 1.01x slower                                                        |
| float                    | 70.0 ms                                                               | 70.8 ms: 1.01x slower                                                       |
| sympy_sum                | 165 ms                                                                | 167 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 55.0 ms                                                               | 55.6 ms: 1.01x slower                                                       |
| deepcopy                 | 273 us                                                                | 276 us: 1.01x slower                                                        |
| scimark_lu               | 124 ms                                                                | 126 ms: 1.01x slower                                                        |
| nqueens                  | 85.5 ms                                                               | 86.7 ms: 1.01x slower                                                       |
| mdp                      | 2.52 sec                                                              | 2.56 sec: 1.01x slower                                                      |
| xml_etree_process        | 57.5 ms                                                               | 58.5 ms: 1.02x slower                                                       |
| django_template          | 35.1 ms                                                               | 35.8 ms: 1.02x slower                                                       |
| logging_simple           | 5.42 us                                                               | 5.52 us: 1.02x slower                                                       |
| xml_etree_generate       | 81.6 ms                                                               | 83.1 ms: 1.02x slower                                                       |
| 2to3                     | 271 ms                                                                | 276 ms: 1.02x slower                                                        |
| genshi_text              | 24.9 ms                                                               | 25.4 ms: 1.02x slower                                                       |
| logging_format           | 5.94 us                                                               | 6.08 us: 1.02x slower                                                       |
| scimark_sor              | 129 ms                                                                | 132 ms: 1.02x slower                                                        |
| regex_compile            | 134 ms                                                                | 137 ms: 1.03x slower                                                        |
| pprint_safe_repr         | 710 ms                                                                | 733 ms: 1.03x slower                                                        |
| hexiom                   | 6.48 ms                                                               | 6.69 ms: 1.03x slower                                                       |
| asyncio_tcp              | 488 ms                                                                | 505 ms: 1.03x slower                                                        |
| pickle_pure_python       | 293 us                                                                | 304 us: 1.03x slower                                                        |
| pprint_pformat           | 1.45 sec                                                              | 1.51 sec: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 4.28 ms                                                               | 4.45 ms: 1.04x slower                                                       |
| async_tree_io            | 841 ms                                                                | 893 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (27): spectral_norm, deepcopy_reduce, fannkuch, sqlglot_parse, coverage, json, sqlglot_normalize, regex_dna, asyncio_tcp_ssl, bench_mp_pool, pidigits, dask, asyncio_websockets, unpickle_pure_python, coroutines, go, thrift, crypto_pyaes, json_loads, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, pylint, async_tree_none, async_tree_none_tg

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x