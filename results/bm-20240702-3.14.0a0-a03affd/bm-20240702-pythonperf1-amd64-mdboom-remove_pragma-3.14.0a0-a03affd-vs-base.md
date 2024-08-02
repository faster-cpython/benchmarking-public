# Results vs. base

- fork: mdboom
- ref: remove_pragma
- machine: windows-amd64
- commit hash: a03affd
- commit date: 2024-07-02
- overall geometric mean: 1.01x slower
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                   | 1.70 sec: 1.01x slower                                              |
| html5lib       | 38.5 ms                                                                    | 40.8 ms: 1.06x slower                                               |
| tornado_http   | 81.8 ms                                                                    | 82.5 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 58.6 ms                                                                    | 57.8 ms: 1.01x faster                                               |
| pidigits       | 150 ms                                                                     | 150 ms: 1.00x faster                                                |
| nbody          | 83.0 ms                                                                    | 86.1 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                     | 115 ms: 1.02x faster                                                |
| regex_compile  | 87.3 ms                                                                    | 92.2 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                        |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 14.4 us                                                                    | 14.0 us: 1.02x faster                                               |
| unpickle_pure_python | 157 us                                                                     | 154 us: 1.02x faster                                                |
| tomli_loads          | 1.63 sec                                                                   | 1.61 sec: 1.01x faster                                              |
| xml_etree_process    | 41.5 ms                                                                    | 41.8 ms: 1.01x slower                                               |
| pickle_pure_python   | 212 us                                                                     | 214 us: 1.01x slower                                                |
| xml_etree_generate   | 59.1 ms                                                                    | 60.2 ms: 1.02x slower                                               |
| json_dumps           | 5.99 ms                                                                    | 6.13 ms: 1.02x slower                                               |
| xml_etree_parse      | 93.4 ms                                                                    | 95.6 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 17.1 ms                                                                    | 16.9 ms: 1.01x faster                                               |
| django_template | 24.3 ms                                                                    | 25.1 ms: 1.03x slower                                               |
| genshi_xml      | 36.8 ms                                                                    | 38.6 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240702-pythonperf1-amd64-python-8e8d202f552c993f4091-3.14.0a0-8e8d202 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma-3.14.0a0-a03affd |
|--------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 3.17 ms                                                                    | 2.99 ms: 1.06x faster                                               |
| comprehensions           | 12.6 us                                                                    | 11.9 us: 1.06x faster                                               |
| logging_silent           | 65.0 ns                                                                    | 63.4 ns: 1.03x faster                                               |
| json_loads               | 14.4 us                                                                    | 14.0 us: 1.02x faster                                               |
| fannkuch                 | 312 ms                                                                     | 305 ms: 1.02x faster                                                |
| scimark_sor              | 92.3 ms                                                                    | 90.4 ms: 1.02x faster                                               |
| unpickle_pure_python     | 157 us                                                                     | 154 us: 1.02x faster                                                |
| generators               | 23.6 ms                                                                    | 23.1 ms: 1.02x faster                                               |
| deepcopy_memo            | 21.9 us                                                                    | 21.5 us: 1.02x faster                                               |
| regex_dna                | 117 ms                                                                     | 115 ms: 1.02x faster                                                |
| richards                 | 30.8 ms                                                                    | 30.3 ms: 1.02x faster                                               |
| crypto_pyaes             | 53.9 ms                                                                    | 53.0 ms: 1.02x faster                                               |
| richards_super           | 34.6 ms                                                                    | 34.1 ms: 1.01x faster                                               |
| spectral_norm            | 73.2 ms                                                                    | 72.2 ms: 1.01x faster                                               |
| pyflate                  | 327 ms                                                                     | 323 ms: 1.01x faster                                                |
| float                    | 58.6 ms                                                                    | 57.8 ms: 1.01x faster                                               |
| coverage                 | 47.1 ms                                                                    | 46.5 ms: 1.01x faster                                               |
| tomli_loads              | 1.63 sec                                                                   | 1.61 sec: 1.01x faster                                              |
| hexiom                   | 4.53 ms                                                                    | 4.48 ms: 1.01x faster                                               |
| genshi_text              | 17.1 ms                                                                    | 16.9 ms: 1.01x faster                                               |
| chaos                    | 44.9 ms                                                                    | 44.6 ms: 1.01x faster                                               |
| bench_mp_pool            | 66.2 ms                                                                    | 65.8 ms: 1.01x faster                                               |
| sympy_integrate          | 13.2 ms                                                                    | 13.2 ms: 1.00x faster                                               |
| scimark_fft              | 221 ms                                                                     | 220 ms: 1.00x faster                                                |
| pidigits                 | 150 ms                                                                     | 150 ms: 1.00x faster                                                |
| pprint_pformat           | 1.14 sec                                                                   | 1.15 sec: 1.00x slower                                              |
| mdp                      | 1.47 sec                                                                   | 1.47 sec: 1.00x slower                                              |
| nqueens                  | 64.6 ms                                                                    | 64.8 ms: 1.00x slower                                               |
| scimark_lu               | 67.4 ms                                                                    | 67.8 ms: 1.01x slower                                               |
| xml_etree_process        | 41.5 ms                                                                    | 41.8 ms: 1.01x slower                                               |
| pprint_safe_repr         | 561 ms                                                                     | 565 ms: 1.01x slower                                                |
| docutils                 | 1.69 sec                                                                   | 1.70 sec: 1.01x slower                                              |
| scimark_monte_carlo      | 50.8 ms                                                                    | 51.2 ms: 1.01x slower                                               |
| tornado_http             | 81.8 ms                                                                    | 82.5 ms: 1.01x slower                                               |
| pickle_pure_python       | 212 us                                                                     | 214 us: 1.01x slower                                                |
| coroutines               | 14.6 ms                                                                    | 14.8 ms: 1.01x slower                                               |
| sqlglot_optimize         | 35.4 ms                                                                    | 35.8 ms: 1.01x slower                                               |
| telco                    | 4.92 ms                                                                    | 4.97 ms: 1.01x slower                                               |
| sqlglot_normalize        | 188 ms                                                                     | 190 ms: 1.01x slower                                                |
| logging_format           | 6.74 us                                                                    | 6.83 us: 1.01x slower                                               |
| sqlglot_parse            | 907 us                                                                     | 919 us: 1.01x slower                                                |
| go                       | 96.4 ms                                                                    | 97.9 ms: 1.02x slower                                               |
| logging_simple           | 6.28 us                                                                    | 6.38 us: 1.02x slower                                               |
| thrift                   | 536 us                                                                     | 546 us: 1.02x slower                                                |
| xml_etree_generate       | 59.1 ms                                                                    | 60.2 ms: 1.02x slower                                               |
| python_startup_no_site   | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                               |
| sympy_sum                | 89.5 ms                                                                    | 91.2 ms: 1.02x slower                                               |
| typing_runtime_protocols | 110 us                                                                     | 113 us: 1.02x slower                                                |
| json_dumps               | 5.99 ms                                                                    | 6.13 ms: 1.02x slower                                               |
| xml_etree_parse          | 93.4 ms                                                                    | 95.6 ms: 1.02x slower                                               |
| async_generators         | 251 ms                                                                     | 257 ms: 1.03x slower                                                |
| django_template          | 24.3 ms                                                                    | 25.1 ms: 1.03x slower                                               |
| nbody                    | 83.0 ms                                                                    | 86.1 ms: 1.04x slower                                               |
| sympy_str                | 172 ms                                                                     | 180 ms: 1.05x slower                                                |
| genshi_xml               | 36.8 ms                                                                    | 38.6 ms: 1.05x slower                                               |
| regex_compile            | 87.3 ms                                                                    | 92.2 ms: 1.06x slower                                               |
| html5lib                 | 38.5 ms                                                                    | 40.8 ms: 1.06x slower                                               |
| sympy_expand             | 291 ms                                                                     | 308 ms: 1.06x slower                                                |
| pycparser                | 756 ms                                                                     | 839 ms: 1.11x slower                                                |
| Geometric mean           | (ref)                                                                      | 1.01x slower                                                        |

Benchmark hidden because not significant (28): asyncio_tcp_ssl, bench_thread_pool, gc_traversal, deltablue, mako, 2to3, pathlib, meteor_contest, deepcopy_reduce, raytrace, sqlglot_transpile, xml_etree_iterparse, python_startup, async_tree_cpu_io_mixed_tg, deepcopy, pylint, async_tree_memoization_tg, json, async_tree_cpu_io_mixed, create_gc_cycles, regex_effbot, asyncio_tcp, async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io, regex_v8

# HPT report

- Reliability score: 98.65% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown