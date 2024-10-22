# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.00x faster
- HPT reliability: 66.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 277 ms: 1.02x slower                                                        |
| docutils       | 2.88 sec                                                              | 3.02 sec: 1.05x slower                                                      |
| html5lib       | 65.4 ms                                                               | 64.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 70.4 ms                                                               | 70.0 ms: 1.01x faster                                                       |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                       |
| regex_effbot   | 3.84 ms                                                               | 3.88 ms: 1.01x slower                                                       |
| regex_compile  | 135 ms                                                                | 138 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.93 sec                                                              | 1.89 sec: 1.02x faster                                                      |
| unpickle_pure_python | 217 us                                                                | 213 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 99.0 ms                                                               | 98.7 ms: 1.00x faster                                                       |
| xml_etree_generate   | 81.1 ms                                                               | 81.4 ms: 1.00x slower                                                       |
| pickle_pure_python   | 296 us                                                                | 303 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (4): json_dumps, xml_etree_process, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.11 ms: 1.00x faster                                                       |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 36.1 ms                                                               | 34.8 ms: 1.04x faster                                                       |
| mako            | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards_super           | 47.7 ms                                                               | 41.1 ms: 1.16x faster                                                       |
| richards                 | 41.5 ms                                                               | 36.3 ms: 1.14x faster                                                       |
| scimark_lu               | 126 ms                                                                | 117 ms: 1.08x faster                                                        |
| logging_silent           | 108 ns                                                                | 101 ns: 1.07x faster                                                        |
| deltablue                | 3.58 ms                                                               | 3.43 ms: 1.04x faster                                                       |
| scimark_sor              | 131 ms                                                                | 126 ms: 1.04x faster                                                        |
| deepcopy_memo            | 28.4 us                                                               | 27.3 us: 1.04x faster                                                       |
| deepcopy                 | 274 us                                                                | 264 us: 1.04x faster                                                        |
| deepcopy_reduce          | 2.76 us                                                               | 2.66 us: 1.04x faster                                                       |
| django_template          | 36.1 ms                                                               | 34.8 ms: 1.04x faster                                                       |
| logging_simple           | 5.61 us                                                               | 5.47 us: 1.03x faster                                                       |
| typing_runtime_protocols | 171 us                                                                | 167 us: 1.02x faster                                                        |
| dulwich_log              | 68.0 ms                                                               | 66.6 ms: 1.02x faster                                                       |
| tomli_loads              | 1.93 sec                                                              | 1.89 sec: 1.02x faster                                                      |
| bpe_tokeniser            | 4.82 sec                                                              | 4.73 sec: 1.02x faster                                                      |
| gc_traversal             | 3.64 ms                                                               | 3.58 ms: 1.02x faster                                                       |
| unpickle_pure_python     | 217 us                                                                | 213 us: 1.02x faster                                                        |
| sqlglot_normalize        | 113 ms                                                                | 111 ms: 1.02x faster                                                        |
| logging_format           | 6.16 us                                                               | 6.06 us: 1.02x faster                                                       |
| meteor_contest           | 108 ms                                                                | 106 ms: 1.02x faster                                                        |
| chaos                    | 57.8 ms                                                               | 57.1 ms: 1.01x faster                                                       |
| async_generators         | 455 ms                                                                | 449 ms: 1.01x faster                                                        |
| raytrace                 | 271 ms                                                                | 268 ms: 1.01x faster                                                        |
| go                       | 146 ms                                                                | 144 ms: 1.01x faster                                                        |
| sympy_str                | 293 ms                                                                | 290 ms: 1.01x faster                                                        |
| asyncio_tcp              | 504 ms                                                                | 499 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult  | 4.37 ms                                                               | 4.33 ms: 1.01x faster                                                       |
| bench_thread_pool        | 833 us                                                                | 826 us: 1.01x faster                                                        |
| create_gc_cycles         | 1.77 ms                                                               | 1.75 ms: 1.01x faster                                                       |
| html5lib                 | 65.4 ms                                                               | 64.9 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.80 sec: 1.01x faster                                                      |
| float                    | 70.4 ms                                                               | 70.0 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 99.0 ms                                                               | 98.7 ms: 1.00x faster                                                       |
| python_startup_no_site   | 7.11 ms                                                               | 7.11 ms: 1.00x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| xml_etree_generate       | 81.1 ms                                                               | 81.4 ms: 1.00x slower                                                       |
| hexiom                   | 6.56 ms                                                               | 6.58 ms: 1.00x slower                                                       |
| mdp                      | 2.71 sec                                                              | 2.72 sec: 1.00x slower                                                      |
| pidigits                 | 185 ms                                                                | 186 ms: 1.00x slower                                                        |
| sympy_sum                | 167 ms                                                                | 168 ms: 1.01x slower                                                        |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                       |
| pyflate                  | 446 ms                                                                | 449 ms: 1.01x slower                                                        |
| mako                     | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                       |
| regex_v8                 | 25.5 ms                                                               | 25.7 ms: 1.01x slower                                                       |
| thrift                   | 799 us                                                                | 807 us: 1.01x slower                                                        |
| regex_effbot             | 3.84 ms                                                               | 3.88 ms: 1.01x slower                                                       |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                       |
| telco                    | 7.92 ms                                                               | 8.01 ms: 1.01x slower                                                       |
| spectral_norm            | 101 ms                                                                | 103 ms: 1.01x slower                                                        |
| regex_compile            | 135 ms                                                                | 138 ms: 1.02x slower                                                        |
| scimark_monte_carlo      | 60.8 ms                                                               | 62.0 ms: 1.02x slower                                                       |
| 2to3                     | 272 ms                                                                | 277 ms: 1.02x slower                                                        |
| pickle_pure_python       | 296 us                                                                | 303 us: 1.03x slower                                                        |
| sqlglot_optimize         | 55.7 ms                                                               | 57.4 ms: 1.03x slower                                                       |
| pprint_pformat           | 1.46 sec                                                              | 1.51 sec: 1.03x slower                                                      |
| scimark_fft              | 305 ms                                                                | 316 ms: 1.03x slower                                                        |
| sqlglot_transpile        | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                                       |
| pprint_safe_repr         | 716 ms                                                                | 742 ms: 1.04x slower                                                        |
| generators               | 29.8 ms                                                               | 30.8 ms: 1.04x slower                                                       |
| docutils                 | 2.88 sec                                                              | 3.02 sec: 1.05x slower                                                      |
| pylint                   | 336 ms                                                                | 373 ms: 1.11x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (30): async_tree_io_tg, fannkuch, coverage, dask, genshi_xml, comprehensions, async_tree_cpu_io_mixed_tg, tornado_http, genshi_text, crypto_pyaes, pycparser, regex_dna, async_tree_none_tg, sympy_expand, json_dumps, coroutines, sympy_integrate, bench_mp_pool, asyncio_websockets, nbody, async_tree_memoization, async_tree_cpu_io_mixed, nqueens, async_tree_none, xml_etree_process, xml_etree_parse, async_tree_memoization_tg, json, json_loads, async_tree_io

# HPT report

- Reliability score: 66.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x