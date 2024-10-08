# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-amd64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 225 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.6 ms: 1.16x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 83.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.3 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 92.3 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 6.99 us: 1.02x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.27 us: 1.10x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.0 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.5 ms: 1.14x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 216 us: 1.23x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 157 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.82 ms: 1.07x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.8 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| django_template | 21.7 ms                                                         | 26.0 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 513 us: 15.81x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| json                       | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 21.0 us: 1.05x faster                                                      |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.93 us: 1.03x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.52 ms: 1.02x faster                                                      |
| pickle                     | 7.11 us                                                         | 6.99 us: 1.02x faster                                                      |
| pathlib                    | 75.9 ms                                                         | 74.6 ms: 1.02x faster                                                      |
| create_gc_cycles           | 888 us                                                          | 874 us: 1.02x faster                                                       |
| pidigits                   | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 83.5 ms: 1.02x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 66.2 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.63 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.2 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 393 ms: 1.03x slower                                                       |
| regex_dna                  | 119 ms                                                          | 124 ms: 1.04x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.9 ms: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 813 us: 1.06x slower                                                       |
| unpickle_list              | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 89.7 ms: 1.06x slower                                                      |
| go                         | 82.1 ms                                                         | 87.8 ms: 1.07x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.82 ms: 1.07x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.01 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.09x slower                                                      |
| 2to3                       | 207 ms                                                          | 225 ms: 1.09x slower                                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.61 sec: 1.09x slower                                                     |
| async_generators           | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.31 us: 1.09x slower                                                      |
| pycparser                  | 754 ms                                                          | 826 ms: 1.10x slower                                                       |
| pylint                     | 205 ms                                                          | 225 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.27 us: 1.10x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.90 us: 1.11x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.0 ms: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.3 ms: 1.11x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 62.9 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.79 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.5 ms: 1.12x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 78.0 ms: 1.12x slower                                                      |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| float                      | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.4 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 195 ms: 1.13x slower                                                       |
| coverage                   | 42.1 ms                                                         | 47.8 ms: 1.14x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.5 ms: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 64.5 ms: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 308 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 115 us: 1.14x slower                                                       |
| chaos                      | 38.4 ms                                                         | 44.0 ms: 1.15x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 73.6 ms: 1.15x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.6 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 551 ms: 1.16x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.53 sec: 1.17x slower                                                     |
| genshi_xml                 | 31.6 ms                                                         | 36.8 ms: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                          | 326 ms: 1.17x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.13 sec: 1.17x slower                                                     |
| comprehensions             | 10.4 us                                                         | 12.2 us: 1.17x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.18x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 92.3 ms: 1.18x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.0 ms: 1.20x slower                                                      |
| raytrace                   | 162 ms                                                          | 195 ms: 1.20x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.63 sec: 1.21x slower                                                     |
| scimark_fft                | 171 ms                                                          | 206 ms: 1.21x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 905 us: 1.21x slower                                                       |
| richards                   | 26.7 ms                                                         | 32.4 ms: 1.21x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.7 ms: 1.22x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.29 ms: 1.22x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 64.8 ns: 1.23x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.57 ms: 1.23x slower                                                      |
| nbody                      | 67.6 ms                                                         | 83.3 ms: 1.23x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 216 us: 1.23x slower                                                       |
| fannkuch                   | 243 ms                                                          | 302 ms: 1.24x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 93.9 ms: 1.25x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.2 ms: 1.28x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 157 us: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (8): regex_v8, async_tree_memoization_tg, async_tree_io, pickle_list, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_memoization, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf1-amd64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown