# Results vs. base

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                     | 233 ms: 1.03x slower                                               |
| docutils       | 1.72 sec                                                                   | 1.75 sec: 1.02x slower                                             |
| tornado_http   | 83.4 ms                                                                    | 93.5 ms: 1.12x slower                                              |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 14.3 ms                                                                    | 14.4 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 388 ms                                                                     | 394 ms: 1.02x slower                                               |
| async_generators           | 247 ms                                                                     | 253 ms: 1.02x slower                                               |
| async_tree_io              | 560 ms                                                                     | 581 ms: 1.04x slower                                               |
| asyncio_tcp                | 467 ms                                                                     | 539 ms: 1.15x slower                                               |
| asyncio_tcp_ssl            | 1.44 sec                                                                   | 1.68 sec: 1.16x slower                                             |
| Geometric mean             | (ref)                                                                      | 1.04x slower                                                       |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 83.5 ms                                                                    | 85.1 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 16.5 ms                                                                    | 15.0 ms: 1.10x faster                                              |
| regex_compile  | 90.7 ms                                                                    | 90.4 ms: 1.00x faster                                              |
| regex_dna      | 118 ms                                                                     | 119 ms: 1.01x slower                                               |
| regex_effbot   | 1.56 ms                                                                    | 1.58 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|--------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python | 212 us                                                                     | 210 us: 1.01x faster                                               |
| json_dumps         | 6.13 ms                                                                    | 6.08 ms: 1.01x faster                                              |
| xml_etree_generate | 57.1 ms                                                                    | 57.7 ms: 1.01x slower                                              |
| json_loads         | 14.4 us                                                                    | 14.8 us: 1.02x slower                                              |
| xml_etree_parse    | 92.3 ms                                                                    | 96.0 ms: 1.04x slower                                              |
| Geometric mean     | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (4): tomli_loads, unpickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 17.5 ms                                                                    | 18.0 ms: 1.03x slower                                              |
| python_startup         | 21.2 ms                                                                    | 22.2 ms: 1.05x slower                                              |
| Geometric mean         | (ref)                                                                      | 1.04x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 36.3 ms                                                                    | 37.1 ms: 1.02x slower                                              |
| django_template | 24.4 ms                                                                    | 25.0 ms: 1.02x slower                                              |
| genshi_text     | 17.1 ms                                                                    | 17.5 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240817-pythonperf1-amd64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8                   | 16.5 ms                                                                    | 15.0 ms: 1.10x faster                                              |
| mdp                        | 1.54 sec                                                                   | 1.42 sec: 1.09x faster                                             |
| generators                 | 20.9 ms                                                                    | 20.6 ms: 1.01x faster                                              |
| thrift                     | 527 us                                                                     | 520 us: 1.01x faster                                               |
| pickle_pure_python         | 212 us                                                                     | 210 us: 1.01x faster                                               |
| telco                      | 5.04 ms                                                                    | 4.99 ms: 1.01x faster                                              |
| json_dumps                 | 6.13 ms                                                                    | 6.08 ms: 1.01x faster                                              |
| crypto_pyaes               | 48.3 ms                                                                    | 48.1 ms: 1.00x faster                                              |
| hexiom                     | 4.38 ms                                                                    | 4.36 ms: 1.00x faster                                              |
| regex_compile              | 90.7 ms                                                                    | 90.4 ms: 1.00x faster                                              |
| deepcopy_memo              | 20.2 us                                                                    | 20.3 us: 1.00x slower                                              |
| sqlglot_transpile          | 1.10 ms                                                                    | 1.10 ms: 1.01x slower                                              |
| go                         | 97.1 ms                                                                    | 97.6 ms: 1.01x slower                                              |
| coroutines                 | 14.3 ms                                                                    | 14.4 ms: 1.01x slower                                              |
| deepcopy                   | 188 us                                                                     | 189 us: 1.01x slower                                               |
| sympy_str                  | 177 ms                                                                     | 178 ms: 1.01x slower                                               |
| sqlglot_parse              | 883 us                                                                     | 889 us: 1.01x slower                                               |
| regex_dna                  | 118 ms                                                                     | 119 ms: 1.01x slower                                               |
| sympy_sum                  | 90.0 ms                                                                    | 90.8 ms: 1.01x slower                                              |
| sqlglot_optimize           | 35.7 ms                                                                    | 36.0 ms: 1.01x slower                                              |
| sympy_integrate            | 13.2 ms                                                                    | 13.3 ms: 1.01x slower                                              |
| xml_etree_generate         | 57.1 ms                                                                    | 57.7 ms: 1.01x slower                                              |
| regex_effbot               | 1.56 ms                                                                    | 1.58 ms: 1.01x slower                                              |
| logging_silent             | 62.1 ns                                                                    | 62.9 ns: 1.01x slower                                              |
| pprint_pformat             | 1.13 sec                                                                   | 1.14 sec: 1.01x slower                                             |
| pprint_safe_repr           | 548 ms                                                                     | 555 ms: 1.01x slower                                               |
| comprehensions             | 11.8 us                                                                    | 11.9 us: 1.01x slower                                              |
| logging_format             | 6.69 us                                                                    | 6.78 us: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 388 ms                                                                     | 394 ms: 1.02x slower                                               |
| sqlglot_normalize          | 190 ms                                                                     | 193 ms: 1.02x slower                                               |
| json                       | 3.04 ms                                                                    | 3.09 ms: 1.02x slower                                              |
| sympy_expand               | 303 ms                                                                     | 308 ms: 1.02x slower                                               |
| docutils                   | 1.72 sec                                                                   | 1.75 sec: 1.02x slower                                             |
| chaos                      | 43.2 ms                                                                    | 44.0 ms: 1.02x slower                                              |
| gc_traversal               | 1.55 ms                                                                    | 1.58 ms: 1.02x slower                                              |
| nbody                      | 83.5 ms                                                                    | 85.1 ms: 1.02x slower                                              |
| fannkuch                   | 291 ms                                                                     | 297 ms: 1.02x slower                                               |
| nqueens                    | 63.4 ms                                                                    | 64.7 ms: 1.02x slower                                              |
| genshi_xml                 | 36.3 ms                                                                    | 37.1 ms: 1.02x slower                                              |
| pyflate                    | 318 ms                                                                     | 325 ms: 1.02x slower                                               |
| async_generators           | 247 ms                                                                     | 253 ms: 1.02x slower                                               |
| django_template            | 24.4 ms                                                                    | 25.0 ms: 1.02x slower                                              |
| genshi_text                | 17.1 ms                                                                    | 17.5 ms: 1.02x slower                                              |
| json_loads                 | 14.4 us                                                                    | 14.8 us: 1.02x slower                                              |
| coverage                   | 48.9 ms                                                                    | 50.1 ms: 1.02x slower                                              |
| bench_mp_pool              | 66.7 ms                                                                    | 68.4 ms: 1.03x slower                                              |
| scimark_sor                | 90.5 ms                                                                    | 93.0 ms: 1.03x slower                                              |
| python_startup_no_site     | 17.5 ms                                                                    | 18.0 ms: 1.03x slower                                              |
| dulwich_log                | 41.8 ms                                                                    | 43.0 ms: 1.03x slower                                              |
| 2to3                       | 226 ms                                                                     | 233 ms: 1.03x slower                                               |
| spectral_norm              | 68.9 ms                                                                    | 71.3 ms: 1.04x slower                                              |
| scimark_fft                | 200 ms                                                                     | 207 ms: 1.04x slower                                               |
| async_tree_io              | 560 ms                                                                     | 581 ms: 1.04x slower                                               |
| scimark_lu                 | 60.9 ms                                                                    | 63.3 ms: 1.04x slower                                              |
| xml_etree_parse            | 92.3 ms                                                                    | 96.0 ms: 1.04x slower                                              |
| python_startup             | 21.2 ms                                                                    | 22.2 ms: 1.05x slower                                              |
| scimark_sparse_mat_mult    | 2.72 ms                                                                    | 2.86 ms: 1.05x slower                                              |
| pathlib                    | 73.8 ms                                                                    | 77.9 ms: 1.06x slower                                              |
| richards_super             | 35.4 ms                                                                    | 37.7 ms: 1.07x slower                                              |
| richards                   | 31.2 ms                                                                    | 33.3 ms: 1.07x slower                                              |
| pycparser                  | 782 ms                                                                     | 871 ms: 1.11x slower                                               |
| tornado_http               | 83.4 ms                                                                    | 93.5 ms: 1.12x slower                                              |
| asyncio_tcp                | 467 ms                                                                     | 539 ms: 1.15x slower                                               |
| asyncio_tcp_ssl            | 1.44 sec                                                                   | 1.68 sec: 1.16x slower                                             |
| Geometric mean             | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (24): tomli_loads, unpickle_pure_python, meteor_contest, typing_runtime_protocols, float, scimark_monte_carlo, pidigits, xml_etree_process, deltablue, logging_simple, deepcopy_reduce, html5lib, raytrace, create_gc_cycles, mako, xml_etree_iterparse, pylint, async_tree_cpu_io_mixed, bench_thread_pool, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown