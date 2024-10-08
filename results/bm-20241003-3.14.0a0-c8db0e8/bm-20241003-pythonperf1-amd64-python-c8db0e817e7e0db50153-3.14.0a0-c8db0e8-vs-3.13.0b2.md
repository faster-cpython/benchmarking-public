# Results vs. 3.13.0b2

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-amd64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 43.0 ms: 1.23x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 92.7 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 56.9 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 87.6 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 118 ms: 1.00x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 93.0 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.4 ms: 1.04x slower                                                      |
| pickle               | 7.11 us                                                         | 7.49 us: 1.05x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.5 ms: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.52 us: 1.13x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.1 ms: 1.15x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 218 us: 1.24x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                               |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.7 ms: 1.12x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.23 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                                      |
| django_template | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 527 us: 15.38x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.91 us: 1.04x faster                                                      |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.5 us: 1.03x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.01x faster                                                      |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.00x faster                                                       |
| pidigits                   | 150 ms                                                          | 151 ms: 1.00x slower                                                       |
| pickle_dict                | 18.1 us                                                         | 18.3 us: 1.01x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.64 us: 1.03x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 78.4 ms: 1.03x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 94.4 ms: 1.04x slower                                                      |
| telco                      | 4.67 ms                                                         | 4.87 ms: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 400 ms: 1.05x slower                                                       |
| pickle                     | 7.11 us                                                         | 7.49 us: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.4 ms: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 824 us: 1.07x slower                                                       |
| unpickle_list              | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| go                         | 82.1 ms                                                         | 88.9 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 110 us: 1.09x slower                                                       |
| generators                 | 19.6 ms                                                         | 21.4 ms: 1.09x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.84 us: 1.10x slower                                                      |
| 2to3                       | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| pylint                     | 205 ms                                                          | 226 ms: 1.10x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 13.5 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                          | 248 ms: 1.11x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.47 us: 1.12x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.5 ms: 1.12x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 72.5 ms: 1.12x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.7 ms: 1.12x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 50.9 ms: 1.12x slower                                                      |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 36.8 ms: 1.12x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 195 ms: 1.13x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 534 ms: 1.13x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 92.7 ms: 1.13x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.52 us: 1.13x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.84 ms: 1.14x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 79.5 ms: 1.14x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.23 ms: 1.14x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.9 ms: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 308 ms: 1.14x slower                                                       |
| float                      | 49.7 ms                                                         | 56.9 ms: 1.14x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.7 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.6 ms: 1.15x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 42.1 ms: 1.15x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.52 sec: 1.16x slower                                                     |
| nqueens                    | 56.7 ms                                                         | 65.5 ms: 1.16x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.8 ms: 1.17x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 554 ms: 1.17x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.9 ms: 1.17x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 74.9 ms: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                          | 329 ms: 1.18x slower                                                       |
| django_template            | 21.7 ms                                                         | 25.6 ms: 1.18x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.14 sec: 1.18x slower                                                     |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.19x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.3 us: 1.19x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 93.0 ms: 1.19x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 67.9 ms: 1.20x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 908 us: 1.21x slower                                                       |
| richards_super             | 30.2 ms                                                         | 36.8 ms: 1.22x slower                                                      |
| raytrace                   | 162 ms                                                          | 198 ms: 1.22x slower                                                       |
| richards                   | 26.7 ms                                                         | 32.6 ms: 1.22x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.31 ms: 1.23x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 43.0 ms: 1.23x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.63 ms: 1.24x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 218 us: 1.24x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 65.9 ns: 1.24x slower                                                      |
| scimark_fft                | 171 ms                                                          | 214 ms: 1.25x slower                                                       |
| fannkuch                   | 243 ms                                                          | 307 ms: 1.26x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 155 us: 1.27x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 96.2 ms: 1.28x slower                                                      |
| nbody                      | 67.6 ms                                                         | 87.6 ms: 1.30x slower                                                      |
| json                       | 3.19 ms                                                         | 4.15 ms: 1.30x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 51.3 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (12): regex_v8, async_tree_memoization_tg, async_tree_io, async_tree_memoization, pickle_list, create_gc_cycles, pycparser, regex_effbot, json_loads, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1-amd64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown