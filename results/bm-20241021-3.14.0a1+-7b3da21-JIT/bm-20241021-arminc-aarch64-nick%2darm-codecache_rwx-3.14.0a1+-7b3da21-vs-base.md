# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.016x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 385 ms                                                                   | 363 ms: 1.06x faster                                                  |
| docutils       | 3.64 sec                                                                 | 3.48 sec: 1.04x faster                                                |
| sphinx         | 1.47 sec                                                                 | 1.38 sec: 1.06x faster                                                |
| tornado_http   | 148 ms                                                                   | 143 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                                    | 1.04x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 511 ms                                                                   | 506 ms: 1.01x faster                                                  |
| async_tree_io_tg | 1.25 sec                                                                 | 1.26 sec: 1.01x slower                                                |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                          |

Benchmark hidden because not significant (9): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, coroutines, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                   | 162 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                          |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 272 us                                                                   | 267 us: 1.02x faster                                                  |
| json_loads           | 31.8 us                                                                  | 31.3 us: 1.01x faster                                                 |
| xml_etree_parse      | 187 ms                                                                   | 188 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                          |

Benchmark hidden because not significant (6): tomli_loads, json_dumps, xml_etree_iterparse, xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 85.7 ms                                                                  | 78.6 ms: 1.09x faster                                                 |
| genshi_text     | 34.9 ms                                                                  | 32.6 ms: 1.07x faster                                                 |
| django_template | 53.3 ms                                                                  | 50.6 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                                    | 1.05x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml               | 85.7 ms                                                                  | 78.6 ms: 1.09x faster                                                 |
| regex_compile            | 177 ms                                                                   | 162 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 83.1 ms                                                                  | 77.0 ms: 1.08x faster                                                 |
| dulwich_log              | 81.5 ms                                                                  | 75.8 ms: 1.08x faster                                                 |
| genshi_text              | 34.9 ms                                                                  | 32.6 ms: 1.07x faster                                                 |
| richards_super           | 68.5 ms                                                                  | 63.9 ms: 1.07x faster                                                 |
| sympy_sum                | 219 ms                                                                   | 205 ms: 1.07x faster                                                  |
| sphinx                   | 1.47 sec                                                                 | 1.38 sec: 1.06x faster                                                |
| 2to3                     | 385 ms                                                                   | 363 ms: 1.06x faster                                                  |
| hexiom                   | 10.4 ms                                                                  | 9.81 ms: 1.06x faster                                                 |
| richards                 | 63.2 ms                                                                  | 59.7 ms: 1.06x faster                                                 |
| sympy_expand             | 595 ms                                                                   | 563 ms: 1.06x faster                                                  |
| sympy_str                | 361 ms                                                                   | 343 ms: 1.05x faster                                                  |
| django_template          | 53.3 ms                                                                  | 50.6 ms: 1.05x faster                                                 |
| deepcopy_reduce          | 4.06 us                                                                  | 3.87 us: 1.05x faster                                                 |
| sqlglot_normalize        | 157 ms                                                                   | 150 ms: 1.05x faster                                                  |
| docutils                 | 3.64 sec                                                                 | 3.48 sec: 1.04x faster                                                |
| sympy_integrate          | 30.2 ms                                                                  | 28.9 ms: 1.04x faster                                                 |
| go                       | 185 ms                                                                   | 177 ms: 1.04x faster                                                  |
| logging_simple           | 7.68 us                                                                  | 7.38 us: 1.04x faster                                                 |
| pycparser                | 1.53 sec                                                                 | 1.48 sec: 1.04x faster                                                |
| tornado_http             | 148 ms                                                                   | 143 ms: 1.03x faster                                                  |
| logging_format           | 8.22 us                                                                  | 7.99 us: 1.03x faster                                                 |
| thrift                   | 964 us                                                                   | 941 us: 1.02x faster                                                  |
| json                     | 5.78 ms                                                                  | 5.64 ms: 1.02x faster                                                 |
| unpickle_pure_python     | 272 us                                                                   | 267 us: 1.02x faster                                                  |
| scimark_sor              | 156 ms                                                                   | 153 ms: 1.02x faster                                                  |
| typing_runtime_protocols | 214 us                                                                   | 210 us: 1.02x faster                                                  |
| sqlglot_transpile        | 2.19 ms                                                                  | 2.15 ms: 1.02x faster                                                 |
| json_loads               | 31.8 us                                                                  | 31.3 us: 1.01x faster                                                 |
| telco                    | 9.63 ms                                                                  | 9.49 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.70 ms                                                                  | 1.68 ms: 1.01x faster                                                 |
| fannkuch                 | 519 ms                                                                   | 513 ms: 1.01x faster                                                  |
| deltablue                | 4.53 ms                                                                  | 4.49 ms: 1.01x faster                                                 |
| async_generators         | 511 ms                                                                   | 506 ms: 1.01x faster                                                  |
| mdp                      | 3.49 sec                                                                 | 3.47 sec: 1.01x faster                                                |
| async_tree_io_tg         | 1.25 sec                                                                 | 1.26 sec: 1.01x slower                                                |
| xml_etree_parse          | 187 ms                                                                   | 188 ms: 1.01x slower                                                  |
| scimark_monte_carlo      | 89.1 ms                                                                  | 90.0 ms: 1.01x slower                                                 |
| pprint_safe_repr         | 1.20 sec                                                                 | 1.22 sec: 1.02x slower                                                |
| spectral_norm            | 155 ms                                                                   | 159 ms: 1.02x slower                                                  |
| pprint_pformat           | 2.51 sec                                                                 | 2.58 sec: 1.03x slower                                                |
| bench_mp_pool            | 2.71 sec                                                                 | 4.29 sec: 1.58x slower                                                |
| Geometric mean           | (ref)                                                                    | 1.01x faster                                                          |

Benchmark hidden because not significant (46): pylint, comprehensions, coverage, html5lib, async_tree_memoization_tg, gc_traversal, asyncio_websockets, nqueens, async_tree_cpu_io_mixed_tg, deepcopy, regex_dna, logging_silent, async_tree_none, coroutines, async_tree_memoization, regex_effbot, pathlib, tomli_loads, pyflate, json_dumps, pidigits, raytrace, deepcopy_memo, async_tree_none_tg, bench_thread_pool, async_tree_cpu_io_mixed, xml_etree_iterparse, mako, nbody, regex_v8, generators, scimark_fft, python_startup, python_startup_no_site, float, xml_etree_process, chaos, xml_etree_generate, meteor_contest, bpe_tokeniser, crypto_pyaes, pickle_pure_python, create_gc_cycles, async_tree_io, scimark_lu, scimark_sparse_mat_mult

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x