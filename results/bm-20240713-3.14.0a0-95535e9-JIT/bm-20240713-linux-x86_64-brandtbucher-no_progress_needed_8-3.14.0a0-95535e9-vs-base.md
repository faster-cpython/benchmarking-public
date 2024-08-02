# Results vs. base

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.00x slower
- HPT reliability: 97.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 277 ms: 1.02x slower                                                        |
| docutils       | 2.87 sec                                                              | 3.02 sec: 1.05x slower                                                      |
| tornado_http   | 92.4 ms                                                               | 93.6 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 544 ms: 1.01x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.88 ms: 1.01x slower                                                       |
| regex_v8       | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                       |
| regex_dna      | 222 ms                                                                | 227 ms: 1.02x slower                                                        |
| regex_compile  | 134 ms                                                                | 138 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.92 sec                                                              | 1.89 sec: 1.02x faster                                                      |
| json_dumps           | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 99.2 ms                                                               | 98.7 ms: 1.01x faster                                                       |
| pickle_pure_python   | 293 us                                                                | 303 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                       |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                               | 56.6 ms: 1.02x faster                                                       |
| django_template | 35.1 ms                                                               | 34.8 ms: 1.01x faster                                                       |
| mako            | 9.76 ms                                                               | 9.85 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240708-linux-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| richards_super             | 47.5 ms                                                               | 41.1 ms: 1.16x faster                                                       |
| richards                   | 41.8 ms                                                               | 36.3 ms: 1.15x faster                                                       |
| scimark_lu                 | 124 ms                                                                | 117 ms: 1.06x faster                                                        |
| logging_silent             | 107 ns                                                                | 101 ns: 1.06x faster                                                        |
| gc_traversal               | 3.74 ms                                                               | 3.58 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 2.78 us                                                               | 2.66 us: 1.04x faster                                                       |
| deepcopy_memo              | 28.4 us                                                               | 27.3 us: 1.04x faster                                                       |
| typing_runtime_protocols   | 172 us                                                                | 167 us: 1.03x faster                                                        |
| deepcopy                   | 273 us                                                                | 264 us: 1.03x faster                                                        |
| deltablue                  | 3.52 ms                                                               | 3.43 ms: 1.03x faster                                                       |
| genshi_xml                 | 58.0 ms                                                               | 56.6 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 4.84 sec                                                              | 4.73 sec: 1.02x faster                                                      |
| scimark_sor                | 129 ms                                                                | 126 ms: 1.02x faster                                                        |
| chaos                      | 58.1 ms                                                               | 57.1 ms: 1.02x faster                                                       |
| tomli_loads                | 1.92 sec                                                              | 1.89 sec: 1.02x faster                                                      |
| crypto_pyaes               | 67.8 ms                                                               | 66.9 ms: 1.01x faster                                                       |
| spectral_norm              | 104 ms                                                                | 103 ms: 1.01x faster                                                        |
| pathlib                    | 16.2 ms                                                               | 16.1 ms: 1.01x faster                                                       |
| telco                      | 8.08 ms                                                               | 8.01 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                       |
| django_template            | 35.1 ms                                                               | 34.8 ms: 1.01x faster                                                       |
| dulwich_log                | 67.1 ms                                                               | 66.6 ms: 1.01x faster                                                       |
| bench_thread_pool          | 832 us                                                                | 826 us: 1.01x faster                                                        |
| sympy_str                  | 292 ms                                                                | 290 ms: 1.01x faster                                                        |
| meteor_contest             | 107 ms                                                                | 106 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 215 us                                                                | 213 us: 1.01x faster                                                        |
| async_generators           | 452 ms                                                                | 449 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 99.2 ms                                                               | 98.7 ms: 1.01x faster                                                       |
| create_gc_cycles           | 1.76 ms                                                               | 1.75 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                       |
| python_startup             | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                       |
| sympy_integrate            | 21.8 ms                                                               | 21.9 ms: 1.00x slower                                                       |
| regex_effbot               | 3.86 ms                                                               | 3.88 ms: 1.01x slower                                                       |
| thrift                     | 801 us                                                                | 807 us: 1.01x slower                                                        |
| raytrace                   | 266 ms                                                                | 268 ms: 1.01x slower                                                        |
| mako                       | 9.76 ms                                                               | 9.85 ms: 1.01x slower                                                       |
| logging_simple             | 5.42 us                                                               | 5.47 us: 1.01x slower                                                       |
| pyflate                    | 444 ms                                                                | 449 ms: 1.01x slower                                                        |
| tornado_http               | 92.4 ms                                                               | 93.6 ms: 1.01x slower                                                       |
| nqueens                    | 85.5 ms                                                               | 86.6 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 537 ms                                                                | 544 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                               | 4.33 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 61.1 ms                                                               | 62.0 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                       |
| hexiom                     | 6.48 ms                                                               | 6.58 ms: 1.02x slower                                                       |
| regex_v8                   | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                                       |
| sympy_sum                  | 165 ms                                                                | 168 ms: 1.02x slower                                                        |
| logging_format             | 5.94 us                                                               | 6.06 us: 1.02x slower                                                       |
| scimark_fft                | 309 ms                                                                | 316 ms: 1.02x slower                                                        |
| asyncio_tcp                | 488 ms                                                                | 499 ms: 1.02x slower                                                        |
| 2to3                       | 271 ms                                                                | 277 ms: 1.02x slower                                                        |
| regex_dna                  | 222 ms                                                                | 227 ms: 1.02x slower                                                        |
| regex_compile              | 134 ms                                                                | 138 ms: 1.03x slower                                                        |
| pickle_pure_python         | 293 us                                                                | 303 us: 1.03x slower                                                        |
| sqlglot_transpile          | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.45 sec                                                              | 1.51 sec: 1.04x slower                                                      |
| sqlglot_optimize           | 55.0 ms                                                               | 57.4 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 710 ms                                                                | 742 ms: 1.04x slower                                                        |
| generators                 | 29.5 ms                                                               | 30.8 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                              | 3.02 sec: 1.05x slower                                                      |
| mdp                        | 2.52 sec                                                              | 2.72 sec: 1.08x slower                                                      |
| pylint                     | 334 ms                                                                | 373 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (28): async_tree_io_tg, json_loads, xml_etree_parse, nbody, go, xml_etree_generate, dask, coverage, float, comprehensions, asyncio_tcp_ssl, sqlglot_normalize, json, fannkuch, bench_mp_pool, sympy_expand, asyncio_websockets, html5lib, pycparser, coroutines, xml_etree_process, async_tree_none_tg, genshi_text, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io

# HPT report

- Reliability score: 97.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x