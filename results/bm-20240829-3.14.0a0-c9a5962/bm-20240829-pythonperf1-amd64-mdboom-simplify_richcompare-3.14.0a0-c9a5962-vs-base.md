# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.001x slower
- HPT reliability: 60.48%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib       | 40.1 ms                                                                    | 39.7 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 247 ms                                                                     | 251 ms: 1.02x slower                                                       |
| coroutines       | 14.3 ms                                                                    | 14.6 ms: 1.02x slower                                                      |
| Geometric mean   | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (10): async_tree_none, async_tree_memoization_tg, async_tree_io_tg, asyncio_tcp, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.2 ms                                                                    | 87.8 ms: 1.02x faster                                                      |
| pidigits       | 150 ms                                                                     | 151 ms: 1.01x slower                                                       |
| float          | 57.0 ms                                                                    | 58.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                     | 120 ms: 1.04x faster                                                       |
| regex_effbot   | 1.64 ms                                                                    | 1.59 ms: 1.03x faster                                                      |
| regex_compile  | 91.2 ms                                                                    | 92.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                                   | 1.62 sec: 1.02x faster                                                     |
| pickle_pure_python   | 217 us                                                                     | 214 us: 1.01x faster                                                       |
| unpickle_pure_python | 155 us                                                                     | 155 us: 1.00x slower                                                       |
| xml_etree_parse      | 94.4 ms                                                                    | 95.0 ms: 1.01x slower                                                      |
| json_loads           | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| xml_etree_process    | 41.9 ms                                                                    | 42.3 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_generate, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                                    | 22.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                                      |
| django_template | 25.0 ms                                                                    | 25.5 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                | 124 ms                                                                     | 120 ms: 1.04x faster                                                       |
| regex_effbot             | 1.64 ms                                                                    | 1.59 ms: 1.03x faster                                                      |
| deepcopy                 | 192 us                                                                     | 188 us: 1.02x faster                                                       |
| scimark_sor              | 95.7 ms                                                                    | 93.8 ms: 1.02x faster                                                      |
| sympy_expand             | 311 ms                                                                     | 305 ms: 1.02x faster                                                       |
| nqueens                  | 65.8 ms                                                                    | 64.7 ms: 1.02x faster                                                      |
| tomli_loads              | 1.65 sec                                                                   | 1.62 sec: 1.02x faster                                                     |
| scimark_monte_carlo      | 52.4 ms                                                                    | 51.6 ms: 1.02x faster                                                      |
| nbody                    | 89.2 ms                                                                    | 87.8 ms: 1.02x faster                                                      |
| dulwich_log              | 43.5 ms                                                                    | 42.9 ms: 1.01x faster                                                      |
| pickle_pure_python       | 217 us                                                                     | 214 us: 1.01x faster                                                       |
| sqlglot_optimize         | 37.0 ms                                                                    | 36.6 ms: 1.01x faster                                                      |
| html5lib                 | 40.1 ms                                                                    | 39.7 ms: 1.01x faster                                                      |
| generators               | 20.7 ms                                                                    | 20.5 ms: 1.01x faster                                                      |
| fannkuch                 | 303 ms                                                                     | 300 ms: 1.01x faster                                                       |
| comprehensions           | 12.2 us                                                                    | 12.1 us: 1.01x faster                                                      |
| crypto_pyaes             | 49.6 ms                                                                    | 49.3 ms: 1.01x faster                                                      |
| deltablue                | 2.30 ms                                                                    | 2.28 ms: 1.01x faster                                                      |
| deepcopy_memo            | 21.3 us                                                                    | 21.2 us: 1.01x faster                                                      |
| sqlglot_normalize        | 195 ms                                                                     | 194 ms: 1.01x faster                                                       |
| pyflate                  | 329 ms                                                                     | 327 ms: 1.00x faster                                                       |
| pprint_pformat           | 1.15 sec                                                                   | 1.15 sec: 1.00x faster                                                     |
| unpickle_pure_python     | 155 us                                                                     | 155 us: 1.00x slower                                                       |
| mdp                      | 1.50 sec                                                                   | 1.50 sec: 1.00x slower                                                     |
| sympy_integrate          | 13.3 ms                                                                    | 13.3 ms: 1.01x slower                                                      |
| go                       | 87.6 ms                                                                    | 88.1 ms: 1.01x slower                                                      |
| xml_etree_parse          | 94.4 ms                                                                    | 95.0 ms: 1.01x slower                                                      |
| logging_silent           | 64.4 ns                                                                    | 64.8 ns: 1.01x slower                                                      |
| chaos                    | 44.2 ms                                                                    | 44.4 ms: 1.01x slower                                                      |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.01x slower                                                       |
| json_loads               | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| richards_super           | 36.9 ms                                                                    | 37.2 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult  | 2.89 ms                                                                    | 2.92 ms: 1.01x slower                                                      |
| xml_etree_process        | 41.9 ms                                                                    | 42.3 ms: 1.01x slower                                                      |
| scimark_lu               | 64.6 ms                                                                    | 65.3 ms: 1.01x slower                                                      |
| telco                    | 5.14 ms                                                                    | 5.20 ms: 1.01x slower                                                      |
| logging_format           | 6.77 us                                                                    | 6.85 us: 1.01x slower                                                      |
| coverage                 | 49.4 ms                                                                    | 49.9 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 562 ms                                                                     | 569 ms: 1.01x slower                                                       |
| python_startup           | 22.2 ms                                                                    | 22.4 ms: 1.01x slower                                                      |
| regex_compile            | 91.2 ms                                                                    | 92.4 ms: 1.01x slower                                                      |
| async_generators         | 247 ms                                                                     | 251 ms: 1.02x slower                                                       |
| meteor_contest           | 78.3 ms                                                                    | 79.5 ms: 1.02x slower                                                      |
| genshi_text              | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 110 us                                                                     | 112 us: 1.02x slower                                                       |
| django_template          | 25.0 ms                                                                    | 25.5 ms: 1.02x slower                                                      |
| logging_simple           | 6.34 us                                                                    | 6.48 us: 1.02x slower                                                      |
| coroutines               | 14.3 ms                                                                    | 14.6 ms: 1.02x slower                                                      |
| float                    | 57.0 ms                                                                    | 58.6 ms: 1.03x slower                                                      |
| spectral_norm            | 69.9 ms                                                                    | 72.2 ms: 1.03x slower                                                      |
| raytrace                 | 189 ms                                                                     | 198 ms: 1.05x slower                                                       |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (37): genshi_xml, async_tree_none, mako, bench_mp_pool, sqlglot_parse, async_tree_memoization_tg, async_tree_io_tg, thrift, asyncio_tcp, sympy_str, pylint, 2to3, gc_traversal, bench_thread_pool, richards, async_tree_io, deepcopy_reduce, async_tree_memoization, sqlglot_transpile, xml_etree_generate, hexiom, tornado_http, sympy_sum, scimark_fft, async_tree_cpu_io_mixed_tg, async_tree_none_tg, docutils, json, pathlib, json_dumps, create_gc_cycles, python_startup_no_site, xml_etree_iterparse, async_tree_cpu_io_mixed, asyncio_tcp_ssl, regex_v8, pycparser

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 60.48% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown