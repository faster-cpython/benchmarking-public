# Results vs. 3.13.0b2

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 229 ms: 1.11x slower                                                        |
| chameleon      | 4.80 ms                                                         | 4.95 ms: 1.03x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                      |
| html5lib       | 35.0 ms                                                         | 37.8 ms: 1.08x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 85.7 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed   | 389 ms                                                          | 397 ms: 1.02x slower                                                        |
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                        |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.04x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| async_tree_none_tg        | 202 ms                                                          | 214 ms: 1.06x slower                                                        |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.4 ms: 1.32x faster                                                       |
| float          | 49.7 ms                                                         | 43.5 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 88.9 ms: 1.14x slower                                                       |
| regex_v8       | 15.8 ms                                                         | 22.7 ms: 1.44x slower                                                       |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.21 sec: 1.12x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.5 us: 1.04x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                                       |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                        |
| json_loads           | 14.2 us                                                         | 13.9 us: 1.02x faster                                                       |
| xml_etree_process    | 36.4 ms                                                         | 36.6 ms: 1.00x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 91.7 ms: 1.01x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.69 ms: 1.01x slower                                                       |
| pickle               | 7.11 us                                                         | 7.28 us: 1.02x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                        |
| unpickle             | 8.40 us                                                         | 8.98 us: 1.07x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.85 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.18 ms: 1.23x faster                                                       |
| django_template | 21.7 ms                                                         | 25.4 ms: 1.17x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|---------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm             | 63.7 ms                                                         | 45.1 ms: 1.41x faster                                                       |
| nbody                     | 67.6 ms                                                         | 51.4 ms: 1.32x faster                                                       |
| mako                      | 6.36 ms                                                         | 5.18 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.14 ms: 1.17x faster                                                       |
| float                     | 49.7 ms                                                         | 43.5 ms: 1.14x faster                                                       |
| scimark_fft               | 171 ms                                                          | 152 ms: 1.13x faster                                                        |
| tomli_loads               | 1.35 sec                                                        | 1.21 sec: 1.12x faster                                                      |
| crypto_pyaes              | 45.5 ms                                                         | 41.0 ms: 1.11x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.1 us: 1.10x faster                                                       |
| json                      | 3.19 ms                                                         | 2.90 ms: 1.10x faster                                                       |
| pyflate                   | 279 ms                                                          | 259 ms: 1.08x faster                                                        |
| fannkuch                  | 243 ms                                                          | 226 ms: 1.08x faster                                                        |
| pprint_safe_repr          | 474 ms                                                          | 452 ms: 1.05x faster                                                        |
| pprint_pformat            | 966 ms                                                          | 929 ms: 1.04x faster                                                        |
| pickle_dict               | 18.1 us                                                         | 17.5 us: 1.04x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 51.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse       | 62.3 ms                                                         | 60.6 ms: 1.03x faster                                                       |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.2 ms: 1.02x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.56 ms: 1.02x faster                                                       |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.02x faster                                                       |
| pickle_pure_python        | 175 us                                                          | 172 us: 1.02x faster                                                        |
| json_loads                | 14.2 us                                                         | 13.9 us: 1.02x faster                                                       |
| sqlite_synth              | 1.60 us                                                         | 1.58 us: 1.01x faster                                                       |
| regex_effbot              | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| logging_format            | 6.22 us                                                         | 6.19 us: 1.00x faster                                                       |
| xml_etree_process         | 36.4 ms                                                         | 36.6 ms: 1.00x slower                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 91.7 ms: 1.01x slower                                                       |
| gc_traversal              | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                       |
| json_dumps                | 5.61 ms                                                         | 5.69 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 397 ms: 1.02x slower                                                        |
| chaos                     | 38.4 ms                                                         | 39.2 ms: 1.02x slower                                                       |
| pickle                    | 7.11 us                                                         | 7.28 us: 1.02x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 622 ms: 1.03x slower                                                        |
| unpickle_pure_python      | 122 us                                                          | 125 us: 1.03x slower                                                        |
| chameleon                 | 4.80 ms                                                         | 4.95 ms: 1.03x slower                                                       |
| bench_thread_pool         | 768 us                                                          | 792 us: 1.03x slower                                                        |
| create_gc_cycles          | 888 us                                                          | 917 us: 1.03x slower                                                        |
| mdp                       | 1.31 sec                                                        | 1.36 sec: 1.03x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.08 us: 1.04x slower                                                       |
| async_tree_none           | 218 ms                                                          | 228 ms: 1.04x slower                                                        |
| async_tree_memoization    | 264 ms                                                          | 276 ms: 1.04x slower                                                        |
| tornado_http              | 81.8 ms                                                         | 85.7 ms: 1.05x slower                                                       |
| aiohttp                   | 889 us                                                          | 932 us: 1.05x slower                                                        |
| logging_silent            | 52.9 ns                                                         | 55.6 ns: 1.05x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 273 ms: 1.06x slower                                                        |
| coverage                  | 42.1 ms                                                         | 44.5 ms: 1.06x slower                                                       |
| coroutines                | 12.8 ms                                                         | 13.5 ms: 1.06x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 74.1 ms: 1.06x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 214 ms: 1.06x slower                                                        |
| bench_mp_pool             | 64.8 ms                                                         | 68.9 ms: 1.06x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 60.5 ms: 1.07x slower                                                       |
| unpickle                  | 8.40 us                                                         | 8.98 us: 1.07x slower                                                       |
| dulwich_log               | 38.0 ms                                                         | 40.7 ms: 1.07x slower                                                       |
| deepcopy                  | 220 us                                                          | 237 us: 1.08x slower                                                        |
| raytrace                  | 162 ms                                                          | 175 ms: 1.08x slower                                                        |
| html5lib                  | 35.0 ms                                                         | 37.8 ms: 1.08x slower                                                       |
| sqlglot_parse             | 748 us                                                          | 809 us: 1.08x slower                                                        |
| python_startup            | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                       |
| richards                  | 26.7 ms                                                         | 29.1 ms: 1.09x slower                                                       |
| sqlglot_transpile         | 955 us                                                          | 1.04 ms: 1.09x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.85 us: 1.09x slower                                                       |
| typing_runtime_protocols  | 101 us                                                          | 110 us: 1.09x slower                                                        |
| docutils                  | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                      |
| richards_super            | 30.2 ms                                                         | 33.0 ms: 1.09x slower                                                       |
| python_startup_no_site    | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 82.7 ms: 1.10x slower                                                       |
| thrift                    | 8.11 ms                                                         | 8.96 ms: 1.11x slower                                                       |
| 2to3                      | 207 ms                                                          | 229 ms: 1.11x slower                                                        |
| sympy_sum                 | 84.4 ms                                                         | 93.6 ms: 1.11x slower                                                       |
| async_generators          | 223 ms                                                          | 250 ms: 1.12x slower                                                        |
| sqlglot_optimize          | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                       |
| sympy_str                 | 159 ms                                                          | 180 ms: 1.13x slower                                                        |
| go                        | 82.1 ms                                                         | 93.2 ms: 1.14x slower                                                       |
| regex_compile             | 78.0 ms                                                         | 88.9 ms: 1.14x slower                                                       |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                                       |
| generators                | 19.6 ms                                                         | 22.5 ms: 1.15x slower                                                       |
| pylint                    | 205 ms                                                          | 236 ms: 1.15x slower                                                        |
| sympy_expand              | 271 ms                                                          | 316 ms: 1.17x slower                                                        |
| django_template           | 21.7 ms                                                         | 25.4 ms: 1.17x slower                                                       |
| scimark_lu                | 56.6 ms                                                         | 69.6 ms: 1.23x slower                                                       |
| genshi_text               | 14.4 ms                                                         | 18.0 ms: 1.25x slower                                                       |
| deltablue                 | 1.88 ms                                                         | 2.36 ms: 1.25x slower                                                       |
| hexiom                    | 3.72 ms                                                         | 4.68 ms: 1.26x slower                                                       |
| genshi_xml                | 31.6 ms                                                         | 44.6 ms: 1.41x slower                                                       |
| regex_v8                  | 15.8 ms                                                         | 22.7 ms: 1.44x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (11): asyncio_tcp_ssl, pickle_list, pidigits, logging_simple, asyncio_tcp, regex_dna, flaskblogging, pathlib, async_tree_cpu_io_mixed_tg, pycparser, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: mypy2, sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown