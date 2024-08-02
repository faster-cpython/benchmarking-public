# Results vs. base

- fork: mdboom
- ref: no_additional_schedu
- machine: windows-amd64
- commit hash: 43a18d0
- commit date: 2024-07-19
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                     | 226 ms: 1.01x slower                                                       |
| docutils       | 1.67 sec                                                                   | 1.70 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp      | 534 ms                                                                     | 517 ms: 1.03x faster                                                       |
| async_generators | 241 ms                                                                     | 244 ms: 1.01x slower                                                       |
| coroutines       | 13.3 ms                                                                    | 13.5 ms: 1.02x slower                                                      |
| async_tree_none  | 210 ms                                                                     | 217 ms: 1.04x slower                                                       |
| Geometric mean   | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                     | 150 ms: 1.01x faster                                                       |
| nbody          | 78.2 ms                                                                    | 77.8 ms: 1.00x faster                                                      |
| float          | 55.4 ms                                                                    | 56.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                     | 116 ms: 1.02x faster                                                       |
| regex_v8       | 14.6 ms                                                                    | 14.7 ms: 1.01x slower                                                      |
| regex_compile  | 85.8 ms                                                                    | 89.7 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                                    | 94.2 ms: 1.01x slower                                                      |
| xml_etree_generate   | 57.2 ms                                                                    | 58.3 ms: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                                    | 14.6 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 64.3 ms                                                                    | 65.9 ms: 1.03x slower                                                      |
| json_dumps           | 5.90 ms                                                                    | 6.13 ms: 1.04x slower                                                      |
| xml_etree_process    | 39.5 ms                                                                    | 41.3 ms: 1.04x slower                                                      |
| tomli_loads          | 1.50 sec                                                                   | 1.57 sec: 1.05x slower                                                     |
| pickle_pure_python   | 199 us                                                                     | 213 us: 1.07x slower                                                       |
| unpickle_pure_python | 139 us                                                                     | 152 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                                      | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 17.5 ms                                                                    | 17.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 23.2 ms                                                                    | 24.1 ms: 1.04x slower                                                      |
| genshi_text     | 15.8 ms                                                                    | 16.6 ms: 1.05x slower                                                      |
| mako            | 7.08 ms                                                                    | 7.52 ms: 1.06x slower                                                      |
| genshi_xml      | 33.8 ms                                                                    | 35.9 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240719-pythonperf1-amd64-python-d66b06107b0104af513f-3.14.0a0-d66b061 | bm-20240719-pythonperf1-amd64-mdboom-no_additional_schedu-3.14.0a0-43a18d0 |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coverage                 | 47.3 ms                                                                    | 44.9 ms: 1.05x faster                                                      |
| asyncio_tcp              | 534 ms                                                                     | 517 ms: 1.03x faster                                                       |
| mdp                      | 1.46 sec                                                                   | 1.41 sec: 1.03x faster                                                     |
| regex_dna                | 119 ms                                                                     | 116 ms: 1.02x faster                                                       |
| scimark_sor              | 84.4 ms                                                                    | 83.2 ms: 1.01x faster                                                      |
| generators               | 20.7 ms                                                                    | 20.4 ms: 1.01x faster                                                      |
| pidigits                 | 151 ms                                                                     | 150 ms: 1.01x faster                                                       |
| gc_traversal             | 1.56 ms                                                                    | 1.55 ms: 1.01x faster                                                      |
| sympy_sum                | 88.7 ms                                                                    | 88.2 ms: 1.01x faster                                                      |
| nbody                    | 78.2 ms                                                                    | 77.8 ms: 1.00x faster                                                      |
| bench_mp_pool            | 67.1 ms                                                                    | 67.6 ms: 1.01x slower                                                      |
| regex_v8                 | 14.6 ms                                                                    | 14.7 ms: 1.01x slower                                                      |
| sympy_str                | 172 ms                                                                     | 173 ms: 1.01x slower                                                       |
| 2to3                     | 224 ms                                                                     | 226 ms: 1.01x slower                                                       |
| telco                    | 4.82 ms                                                                    | 4.86 ms: 1.01x slower                                                      |
| nqueens                  | 60.7 ms                                                                    | 61.2 ms: 1.01x slower                                                      |
| sympy_expand             | 294 ms                                                                     | 298 ms: 1.01x slower                                                       |
| xml_etree_parse          | 93.0 ms                                                                    | 94.2 ms: 1.01x slower                                                      |
| async_generators         | 241 ms                                                                     | 244 ms: 1.01x slower                                                       |
| python_startup_no_site   | 17.5 ms                                                                    | 17.8 ms: 1.01x slower                                                      |
| sqlglot_optimize         | 34.6 ms                                                                    | 35.1 ms: 1.02x slower                                                      |
| docutils                 | 1.67 sec                                                                   | 1.70 sec: 1.02x slower                                                     |
| thrift                   | 525 us                                                                     | 533 us: 1.02x slower                                                       |
| coroutines               | 13.3 ms                                                                    | 13.5 ms: 1.02x slower                                                      |
| xml_etree_generate       | 57.2 ms                                                                    | 58.3 ms: 1.02x slower                                                      |
| raytrace                 | 172 ms                                                                     | 176 ms: 1.02x slower                                                       |
| go                       | 91.0 ms                                                                    | 93.0 ms: 1.02x slower                                                      |
| meteor_contest           | 73.8 ms                                                                    | 75.5 ms: 1.02x slower                                                      |
| float                    | 55.4 ms                                                                    | 56.7 ms: 1.02x slower                                                      |
| json_loads               | 14.2 us                                                                    | 14.6 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 64.3 ms                                                                    | 65.9 ms: 1.03x slower                                                      |
| logging_format           | 6.46 us                                                                    | 6.67 us: 1.03x slower                                                      |
| sqlglot_normalize        | 181 ms                                                                     | 187 ms: 1.03x slower                                                       |
| fannkuch                 | 280 ms                                                                     | 290 ms: 1.03x slower                                                       |
| pyflate                  | 302 ms                                                                     | 313 ms: 1.03x slower                                                       |
| async_tree_none          | 210 ms                                                                     | 217 ms: 1.04x slower                                                       |
| scimark_fft              | 199 ms                                                                     | 207 ms: 1.04x slower                                                       |
| django_template          | 23.2 ms                                                                    | 24.1 ms: 1.04x slower                                                      |
| json_dumps               | 5.90 ms                                                                    | 6.13 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult  | 2.73 ms                                                                    | 2.84 ms: 1.04x slower                                                      |
| sqlglot_transpile        | 1.06 ms                                                                    | 1.10 ms: 1.04x slower                                                      |
| logging_simple           | 5.98 us                                                                    | 6.23 us: 1.04x slower                                                      |
| sqlglot_parse            | 854 us                                                                     | 891 us: 1.04x slower                                                       |
| chaos                    | 41.5 ms                                                                    | 43.3 ms: 1.04x slower                                                      |
| regex_compile            | 85.8 ms                                                                    | 89.7 ms: 1.04x slower                                                      |
| xml_etree_process        | 39.5 ms                                                                    | 41.3 ms: 1.04x slower                                                      |
| spectral_norm            | 68.9 ms                                                                    | 72.0 ms: 1.05x slower                                                      |
| scimark_monte_carlo      | 46.4 ms                                                                    | 48.6 ms: 1.05x slower                                                      |
| deltablue                | 2.04 ms                                                                    | 2.14 ms: 1.05x slower                                                      |
| genshi_text              | 15.8 ms                                                                    | 16.6 ms: 1.05x slower                                                      |
| hexiom                   | 4.14 ms                                                                    | 4.34 ms: 1.05x slower                                                      |
| tomli_loads              | 1.50 sec                                                                   | 1.57 sec: 1.05x slower                                                     |
| typing_runtime_protocols | 105 us                                                                     | 111 us: 1.05x slower                                                       |
| crypto_pyaes             | 48.6 ms                                                                    | 51.2 ms: 1.05x slower                                                      |
| pprint_pformat           | 1.07 sec                                                                   | 1.12 sec: 1.05x slower                                                     |
| deepcopy_reduce          | 1.80 us                                                                    | 1.90 us: 1.06x slower                                                      |
| comprehensions           | 11.1 us                                                                    | 11.8 us: 1.06x slower                                                      |
| json                     | 2.94 ms                                                                    | 3.11 ms: 1.06x slower                                                      |
| mako                     | 7.08 ms                                                                    | 7.52 ms: 1.06x slower                                                      |
| richards_super           | 32.7 ms                                                                    | 34.8 ms: 1.06x slower                                                      |
| genshi_xml               | 33.8 ms                                                                    | 35.9 ms: 1.06x slower                                                      |
| pprint_safe_repr         | 523 ms                                                                     | 557 ms: 1.07x slower                                                       |
| logging_silent           | 58.4 ns                                                                    | 62.7 ns: 1.07x slower                                                      |
| pickle_pure_python       | 199 us                                                                     | 213 us: 1.07x slower                                                       |
| deepcopy                 | 174 us                                                                     | 187 us: 1.08x slower                                                       |
| richards                 | 28.6 ms                                                                    | 30.8 ms: 1.08x slower                                                      |
| unpickle_pure_python     | 139 us                                                                     | 152 us: 1.10x slower                                                       |
| deepcopy_memo            | 19.6 us                                                                    | 21.7 us: 1.11x slower                                                      |
| scimark_lu               | 58.6 ms                                                                    | 67.2 ms: 1.15x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.03x slower                                                               |

Benchmark hidden because not significant (18): pycparser, async_tree_io, html5lib, create_gc_cycles, regex_effbot, bench_thread_pool, sympy_integrate, python_startup, async_tree_cpu_io_mixed_tg, pylint, async_tree_cpu_io_mixed, pathlib, tornado_http, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown