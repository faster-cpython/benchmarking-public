# Results vs. base

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 39fa464
- commit date: 2024-07-19
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                     | 218 ms: 1.03x faster                                                       |
| docutils       | 1.67 sec                                                                   | 1.67 sec: 1.00x faster                                                     |
| html5lib       | 40.4 ms                                                                    | 39.0 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 552 ms                                                                     | 527 ms: 1.05x faster                                                       |
| async_generators           | 241 ms                                                                     | 235 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 386 ms                                                                     | 381 ms: 1.01x faster                                                       |
| coroutines                 | 13.3 ms                                                                    | 13.1 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                                   | 1.74 sec: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_tcp, async_tree_memoization, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 78.2 ms                                                                    | 68.8 ms: 1.14x faster                                                      |
| float          | 55.4 ms                                                                    | 54.0 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.05x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 85.8 ms                                                                    | 83.8 ms: 1.02x faster                                                      |
| regex_dna      | 119 ms                                                                     | 120 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 39.5 ms                                                                    | 38.0 ms: 1.04x faster                                                      |
| xml_etree_generate   | 57.2 ms                                                                    | 55.2 ms: 1.04x faster                                                      |
| unpickle_pure_python | 139 us                                                                     | 134 us: 1.03x faster                                                       |
| tomli_loads          | 1.50 sec                                                                   | 1.46 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 64.3 ms                                                                    | 63.6 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                                    | 14.1 us: 1.01x faster                                                      |
| json_dumps           | 5.90 ms                                                                    | 5.87 ms: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 21.4 ms                                                                    | 21.7 ms: 1.01x slower                                                      |
| python_startup_no_site | 17.5 ms                                                                    | 18.0 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                                      | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.08 ms                                                                    | 6.88 ms: 1.03x faster                                                      |
| genshi_text     | 15.8 ms                                                                    | 15.6 ms: 1.02x faster                                                      |
| django_template | 23.2 ms                                                                    | 23.0 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-39fa464 |
|----------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pycparser                  | 848 ms                                                                     | 738 ms: 1.15x faster                                                       |
| nbody                      | 78.2 ms                                                                    | 68.8 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.73 ms                                                                    | 2.52 ms: 1.08x faster                                                      |
| scimark_sor                | 84.4 ms                                                                    | 78.9 ms: 1.07x faster                                                      |
| scimark_fft                | 199 ms                                                                     | 187 ms: 1.07x faster                                                       |
| crypto_pyaes               | 48.6 ms                                                                    | 45.9 ms: 1.06x faster                                                      |
| nqueens                    | 60.7 ms                                                                    | 57.4 ms: 1.06x faster                                                      |
| chaos                      | 41.5 ms                                                                    | 39.3 ms: 1.05x faster                                                      |
| generators                 | 20.7 ms                                                                    | 19.6 ms: 1.05x faster                                                      |
| hexiom                     | 4.14 ms                                                                    | 3.93 ms: 1.05x faster                                                      |
| spectral_norm              | 68.9 ms                                                                    | 65.4 ms: 1.05x faster                                                      |
| mdp                        | 1.46 sec                                                                   | 1.39 sec: 1.05x faster                                                     |
| raytrace                   | 172 ms                                                                     | 164 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 46.4 ms                                                                    | 44.2 ms: 1.05x faster                                                      |
| async_tree_io              | 552 ms                                                                     | 527 ms: 1.05x faster                                                       |
| deltablue                  | 2.04 ms                                                                    | 1.95 ms: 1.05x faster                                                      |
| scimark_lu                 | 58.6 ms                                                                    | 56.0 ms: 1.05x faster                                                      |
| fannkuch                   | 280 ms                                                                     | 269 ms: 1.04x faster                                                       |
| deepcopy_memo              | 19.6 us                                                                    | 18.9 us: 1.04x faster                                                      |
| xml_etree_process          | 39.5 ms                                                                    | 38.0 ms: 1.04x faster                                                      |
| xml_etree_generate         | 57.2 ms                                                                    | 55.2 ms: 1.04x faster                                                      |
| html5lib                   | 40.4 ms                                                                    | 39.0 ms: 1.04x faster                                                      |
| thrift                     | 525 us                                                                     | 507 us: 1.03x faster                                                       |
| unpickle_pure_python       | 139 us                                                                     | 134 us: 1.03x faster                                                       |
| pyflate                    | 302 ms                                                                     | 293 ms: 1.03x faster                                                       |
| mako                       | 7.08 ms                                                                    | 6.88 ms: 1.03x faster                                                      |
| sqlglot_parse              | 854 us                                                                     | 830 us: 1.03x faster                                                       |
| float                      | 55.4 ms                                                                    | 54.0 ms: 1.03x faster                                                      |
| go                         | 91.0 ms                                                                    | 88.7 ms: 1.03x faster                                                      |
| async_generators           | 241 ms                                                                     | 235 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 34.6 ms                                                                    | 33.7 ms: 1.03x faster                                                      |
| 2to3                       | 224 ms                                                                     | 218 ms: 1.03x faster                                                       |
| regex_compile              | 85.8 ms                                                                    | 83.8 ms: 1.02x faster                                                      |
| tomli_loads                | 1.50 sec                                                                   | 1.46 sec: 1.02x faster                                                     |
| richards_super             | 32.7 ms                                                                    | 32.0 ms: 1.02x faster                                                      |
| sqlglot_transpile          | 1.06 ms                                                                    | 1.04 ms: 1.02x faster                                                      |
| coverage                   | 47.3 ms                                                                    | 46.5 ms: 1.02x faster                                                      |
| telco                      | 4.82 ms                                                                    | 4.74 ms: 1.02x faster                                                      |
| genshi_text                | 15.8 ms                                                                    | 15.6 ms: 1.02x faster                                                      |
| sympy_sum                  | 88.7 ms                                                                    | 87.5 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.8 ms                                                                    | 12.6 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 64.3 ms                                                                    | 63.6 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 386 ms                                                                     | 381 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 181 ms                                                                     | 179 ms: 1.01x faster                                                       |
| richards                   | 28.6 ms                                                                    | 28.3 ms: 1.01x faster                                                      |
| coroutines                 | 13.3 ms                                                                    | 13.1 ms: 1.01x faster                                                      |
| django_template            | 23.2 ms                                                                    | 23.0 ms: 1.01x faster                                                      |
| logging_format             | 6.46 us                                                                    | 6.40 us: 1.01x faster                                                      |
| comprehensions             | 11.1 us                                                                    | 11.0 us: 1.01x faster                                                      |
| sympy_expand               | 294 ms                                                                     | 292 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 1.80 us                                                                    | 1.78 us: 1.01x faster                                                      |
| sympy_str                  | 172 ms                                                                     | 171 ms: 1.01x faster                                                       |
| json_loads                 | 14.2 us                                                                    | 14.1 us: 1.01x faster                                                      |
| meteor_contest             | 73.8 ms                                                                    | 73.4 ms: 1.01x faster                                                      |
| json_dumps                 | 5.90 ms                                                                    | 5.87 ms: 1.01x faster                                                      |
| logging_silent             | 58.4 ns                                                                    | 58.2 ns: 1.00x faster                                                      |
| logging_simple             | 5.98 us                                                                    | 5.95 us: 1.00x faster                                                      |
| docutils                   | 1.67 sec                                                                   | 1.67 sec: 1.00x faster                                                     |
| regex_dna                  | 119 ms                                                                     | 120 ms: 1.01x slower                                                       |
| bench_mp_pool              | 67.1 ms                                                                    | 67.8 ms: 1.01x slower                                                      |
| pprint_pformat             | 1.07 sec                                                                   | 1.08 sec: 1.01x slower                                                     |
| python_startup             | 21.4 ms                                                                    | 21.7 ms: 1.01x slower                                                      |
| json                       | 2.94 ms                                                                    | 3.00 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 105 us                                                                     | 107 us: 1.02x slower                                                       |
| pprint_safe_repr           | 523 ms                                                                     | 535 ms: 1.02x slower                                                       |
| python_startup_no_site     | 17.5 ms                                                                    | 18.0 ms: 1.03x slower                                                      |
| asyncio_tcp_ssl            | 1.59 sec                                                                   | 1.74 sec: 1.10x slower                                                     |
| Geometric mean             | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (20): async_tree_io_tg, asyncio_tcp, async_tree_memoization, bench_thread_pool, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, pylint, async_tree_memoization_tg, gc_traversal, regex_effbot, pidigits, pickle_pure_python, pathlib, xml_etree_parse, deepcopy, create_gc_cycles, tornado_http, genshi_xml, regex_v8

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown