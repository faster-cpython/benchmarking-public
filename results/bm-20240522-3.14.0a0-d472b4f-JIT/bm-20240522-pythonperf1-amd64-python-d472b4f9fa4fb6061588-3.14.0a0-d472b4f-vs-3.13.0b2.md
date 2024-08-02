# Results vs. 3.13.0b2

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-amd64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.01x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 235 ms: 1.14x slower                                                       |
| chameleon      | 4.80 ms                                                         | 5.13 ms: 1.07x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| html5lib       | 35.0 ms                                                         | 37.6 ms: 1.07x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 86.0 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg          | 605 ms                                                          | 623 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 403 ms: 1.04x slower                                                       |
| async_tree_io             | 588 ms                                                          | 610 ms: 1.04x slower                                                       |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| async_tree_none_tg        | 202 ms                                                          | 212 ms: 1.05x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.07x slower                                                       |
| Geometric mean            | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.2 ms: 1.32x faster                                                      |
| float          | 49.7 ms                                                         | 45.2 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 89.3 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                      |
| pickle_pure_python   | 175 us                                                          | 172 us: 1.02x faster                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 89.4 ms: 1.02x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.0 us: 1.01x faster                                                      |
| json_dumps           | 5.61 ms                                                         | 5.66 ms: 1.01x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.57 us: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.35 us: 1.03x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 129 us: 1.06x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.79 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.03 ms: 1.26x faster                                                      |
| django_template | 21.7 ms                                                         | 26.1 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1-amd64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                    | 8.11 ms                                                         | 516 us: 15.71x faster                                                      |
| spectral_norm             | 63.7 ms                                                         | 45.4 ms: 1.40x faster                                                      |
| nbody                     | 67.6 ms                                                         | 51.2 ms: 1.32x faster                                                      |
| mako                      | 6.36 ms                                                         | 5.03 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult   | 2.50 ms                                                         | 2.13 ms: 1.18x faster                                                      |
| scimark_fft               | 171 ms                                                          | 147 ms: 1.16x faster                                                       |
| fannkuch                  | 243 ms                                                          | 218 ms: 1.12x faster                                                       |
| crypto_pyaes              | 45.5 ms                                                         | 41.1 ms: 1.11x faster                                                      |
| float                     | 49.7 ms                                                         | 45.2 ms: 1.10x faster                                                      |
| tomli_loads               | 1.35 sec                                                        | 1.23 sec: 1.10x faster                                                     |
| json                      | 3.19 ms                                                         | 2.91 ms: 1.09x faster                                                      |
| pyflate                   | 279 ms                                                          | 259 ms: 1.08x faster                                                       |
| deepcopy_memo             | 22.1 us                                                         | 20.9 us: 1.06x faster                                                      |
| xml_etree_iterparse       | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                                      |
| pickle_list               | 2.90 us                                                         | 2.80 us: 1.04x faster                                                      |
| pprint_safe_repr          | 474 ms                                                          | 460 ms: 1.03x faster                                                       |
| xml_etree_generate        | 53.2 ms                                                         | 51.7 ms: 1.03x faster                                                      |
| scimark_monte_carlo       | 39.1 ms                                                         | 38.1 ms: 1.03x faster                                                      |
| pprint_pformat            | 966 ms                                                          | 941 ms: 1.03x faster                                                       |
| telco                     | 4.67 ms                                                         | 4.56 ms: 1.02x faster                                                      |
| sqlite_synth              | 1.60 us                                                         | 1.57 us: 1.02x faster                                                      |
| pickle_pure_python        | 175 us                                                          | 172 us: 1.02x faster                                                       |
| xml_etree_parse           | 90.9 ms                                                         | 89.4 ms: 1.02x faster                                                      |
| comprehensions            | 10.4 us                                                         | 10.2 us: 1.01x faster                                                      |
| pickle_dict               | 18.1 us                                                         | 18.0 us: 1.01x faster                                                      |
| pidigits                  | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| flaskblogging             | 2.03 sec                                                        | 2.03 sec: 1.00x faster                                                     |
| logging_simple            | 5.78 us                                                         | 5.80 us: 1.00x slower                                                      |
| regex_effbot              | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| json_dumps                | 5.61 ms                                                         | 5.66 ms: 1.01x slower                                                      |
| unpickle                  | 8.40 us                                                         | 8.57 us: 1.02x slower                                                      |
| regex_dna                 | 119 ms                                                          | 122 ms: 1.03x slower                                                       |
| async_tree_io_tg          | 605 ms                                                          | 623 ms: 1.03x slower                                                       |
| meteor_contest            | 69.9 ms                                                         | 72.0 ms: 1.03x slower                                                      |
| deepcopy_reduce           | 1.99 us                                                         | 2.06 us: 1.03x slower                                                      |
| pickle                    | 7.11 us                                                         | 7.35 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed   | 389 ms                                                          | 403 ms: 1.04x slower                                                       |
| async_tree_io             | 588 ms                                                          | 610 ms: 1.04x slower                                                       |
| chaos                     | 38.4 ms                                                         | 39.8 ms: 1.04x slower                                                      |
| async_tree_memoization_tg | 258 ms                                                          | 270 ms: 1.05x slower                                                       |
| pathlib                   | 75.9 ms                                                         | 79.5 ms: 1.05x slower                                                      |
| tornado_http              | 81.8 ms                                                         | 86.0 ms: 1.05x slower                                                      |
| async_tree_none_tg        | 202 ms                                                          | 212 ms: 1.05x slower                                                       |
| coverage                  | 42.1 ms                                                         | 44.4 ms: 1.06x slower                                                      |
| unpickle_pure_python      | 122 us                                                          | 129 us: 1.06x slower                                                       |
| async_tree_memoization    | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| unpickle_list             | 2.62 us                                                         | 2.79 us: 1.06x slower                                                      |
| async_tree_none           | 218 ms                                                          | 232 ms: 1.07x slower                                                       |
| coroutines                | 12.8 ms                                                         | 13.6 ms: 1.07x slower                                                      |
| mdp                       | 1.31 sec                                                        | 1.40 sec: 1.07x slower                                                     |
| chameleon                 | 4.80 ms                                                         | 5.13 ms: 1.07x slower                                                      |
| logging_silent            | 52.9 ns                                                         | 56.8 ns: 1.07x slower                                                      |
| html5lib                  | 35.0 ms                                                         | 37.6 ms: 1.07x slower                                                      |
| deepcopy                  | 220 us                                                          | 237 us: 1.08x slower                                                       |
| python_startup            | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| bench_mp_pool             | 64.8 ms                                                         | 70.4 ms: 1.09x slower                                                      |
| sqlglot_parse             | 748 us                                                          | 813 us: 1.09x slower                                                       |
| raytrace                  | 162 ms                                                          | 177 ms: 1.09x slower                                                       |
| scimark_sor               | 75.3 ms                                                         | 82.4 ms: 1.09x slower                                                      |
| docutils                  | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| sqlglot_transpile         | 955 us                                                          | 1.05 ms: 1.10x slower                                                      |
| bench_thread_pool         | 768 us                                                          | 849 us: 1.11x slower                                                       |
| nqueens                   | 56.7 ms                                                         | 62.7 ms: 1.11x slower                                                      |
| generators                | 19.6 ms                                                         | 21.8 ms: 1.12x slower                                                      |
| python_startup_no_site    | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| richards                  | 26.7 ms                                                         | 29.9 ms: 1.12x slower                                                      |
| sympy_sum                 | 84.4 ms                                                         | 94.9 ms: 1.12x slower                                                      |
| typing_runtime_protocols  | 101 us                                                          | 114 us: 1.13x slower                                                       |
| async_generators          | 223 ms                                                          | 252 ms: 1.13x slower                                                       |
| sympy_str                 | 159 ms                                                          | 179 ms: 1.13x slower                                                       |
| richards_super            | 30.2 ms                                                         | 34.1 ms: 1.13x slower                                                      |
| 2to3                      | 207 ms                                                          | 235 ms: 1.14x slower                                                       |
| sqlglot_optimize          | 32.7 ms                                                         | 37.3 ms: 1.14x slower                                                      |
| go                        | 82.1 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| regex_compile             | 78.0 ms                                                         | 89.3 ms: 1.15x slower                                                      |
| sympy_integrate           | 12.2 ms                                                         | 14.1 ms: 1.15x slower                                                      |
| pylint                    | 205 ms                                                          | 238 ms: 1.16x slower                                                       |
| sympy_expand              | 271 ms                                                          | 315 ms: 1.17x slower                                                       |
| django_template           | 21.7 ms                                                         | 26.1 ms: 1.21x slower                                                      |
| hexiom                    | 3.72 ms                                                         | 4.71 ms: 1.26x slower                                                      |
| deltablue                 | 1.88 ms                                                         | 2.38 ms: 1.27x slower                                                      |
| genshi_text               | 14.4 ms                                                         | 18.3 ms: 1.27x slower                                                      |
| scimark_lu                | 56.6 ms                                                         | 73.1 ms: 1.29x slower                                                      |
| genshi_xml                | 31.6 ms                                                         | 45.6 ms: 1.44x slower                                                      |
| Geometric mean            | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, pycparser, gc_traversal, logging_format, json_loads, xml_etree_process, create_gc_cycles, asyncio_tcp, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, dulwich_log, mypy2, sqlglot_normalize

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown