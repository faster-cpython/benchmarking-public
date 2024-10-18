# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: windows-amd64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.05x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 250 ms: 1.21x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.8 ms: 1.11x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 99.5 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.18x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 588 ms                                                          | 554 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 202 ms                                                          | 210 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 605 ms                                                          | 632 ms: 1.04x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 55.0 ms: 1.23x faster                                                      |
| float          | 49.7 ms                                                         | 46.5 ms: 1.07x faster                                                      |
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                           | 1.10x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| regex_compile  | 78.0 ms                                                         | 92.9 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 51.5 ms: 1.03x faster                                                      |
| pickle_list          | 2.90 us                                                         | 2.82 us: 1.03x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 18.0 us: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.9 ms: 1.05x slower                                                      |
| pickle               | 7.11 us                                                         | 7.52 us: 1.06x slower                                                      |
| unpickle             | 8.40 us                                                         | 8.99 us: 1.07x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.87 us: 1.10x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 198 us: 1.13x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 143 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.7 ms: 1.15x slower                                                      |
| python_startup         | 20.3 ms                                                         | 24.4 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.18x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.13 ms: 1.24x faster                                                      |
| django_template | 21.7 ms                                                         | 27.7 ms: 1.28x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 19.4 ms: 1.35x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 46.0 ms: 1.46x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 527 us: 15.38x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 16.8 us: 1.31x faster                                                      |
| mako                       | 6.36 ms                                                         | 5.13 ms: 1.24x faster                                                      |
| nbody                      | 67.6 ms                                                         | 55.0 ms: 1.23x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 53.9 ms: 1.18x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 65.1 ms: 1.16x faster                                                      |
| deepcopy                   | 220 us                                                          | 194 us: 1.13x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.23 ms: 1.12x faster                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 40.8 ms: 1.12x faster                                                      |
| scimark_fft                | 171 ms                                                          | 157 ms: 1.09x faster                                                       |
| json                       | 3.19 ms                                                         | 2.95 ms: 1.08x faster                                                      |
| float                      | 49.7 ms                                                         | 46.5 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.88 us: 1.06x faster                                                      |
| async_tree_io              | 588 ms                                                          | 554 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 37.1 ms: 1.05x faster                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| xml_etree_generate         | 53.2 ms                                                         | 51.5 ms: 1.03x faster                                                      |
| pickle_list                | 2.90 us                                                         | 2.82 us: 1.03x faster                                                      |
| scimark_lu                 | 56.6 ms                                                         | 55.2 ms: 1.02x faster                                                      |
| telco                      | 4.67 ms                                                         | 4.56 ms: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| pidigits                   | 150 ms                                                          | 147 ms: 1.02x faster                                                       |
| fannkuch                   | 243 ms                                                          | 240 ms: 1.01x faster                                                       |
| pickle_dict                | 18.1 us                                                         | 18.0 us: 1.01x faster                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.59 us: 1.01x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 480 ms: 1.01x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                                      |
| async_tree_none_tg         | 202 ms                                                          | 210 ms: 1.04x slower                                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.54 sec: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 605 ms                                                          | 632 ms: 1.04x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 95.9 ms: 1.05x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.52 us: 1.06x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 56.1 ns: 1.06x slower                                                      |
| pyflate                    | 279 ms                                                          | 296 ms: 1.06x slower                                                       |
| async_tree_memoization     | 264 ms                                                          | 281 ms: 1.06x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 80.7 ms: 1.06x slower                                                      |
| unpickle                   | 8.40 us                                                         | 8.99 us: 1.07x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.67 us: 1.07x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.25 us: 1.08x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 41.2 ms: 1.08x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 76.0 ms: 1.09x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.87 us: 1.10x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 845 us: 1.10x slower                                                       |
| chaos                      | 38.4 ms                                                         | 42.2 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 38.8 ms: 1.11x slower                                                      |
| go                         | 82.1 ms                                                         | 92.0 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 63.7 ms: 1.12x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 198 us: 1.13x slower                                                       |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.7 ms: 1.15x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 118 us: 1.17x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.53 sec: 1.17x slower                                                     |
| coverage                   | 42.1 ms                                                         | 49.2 ms: 1.17x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 143 us: 1.17x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                     |
| regex_compile              | 78.0 ms                                                         | 92.9 ms: 1.19x slower                                                      |
| async_generators           | 223 ms                                                          | 268 ms: 1.20x slower                                                       |
| python_startup             | 20.3 ms                                                         | 24.4 ms: 1.20x slower                                                      |
| 2to3                       | 207 ms                                                          | 250 ms: 1.21x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 908 us: 1.21x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 99.5 ms: 1.22x slower                                                      |
| generators                 | 19.6 ms                                                         | 23.9 ms: 1.22x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 212 ms: 1.22x slower                                                       |
| sympy_expand               | 271 ms                                                          | 332 ms: 1.23x slower                                                       |
| sympy_str                  | 159 ms                                                          | 195 ms: 1.23x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 104 ms: 1.24x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.35 ms: 1.25x slower                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.96 ms: 1.26x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.21 ms: 1.27x slower                                                      |
| django_template            | 21.7 ms                                                         | 27.7 ms: 1.28x slower                                                      |
| richards_super             | 30.2 ms                                                         | 38.6 ms: 1.28x slower                                                      |
| richards                   | 26.7 ms                                                         | 34.3 ms: 1.28x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 15.9 ms: 1.30x slower                                                      |
| raytrace                   | 162 ms                                                          | 213 ms: 1.31x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 43.4 ms: 1.33x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 19.4 ms: 1.35x slower                                                      |
| pylint                     | 205 ms                                                          | 282 ms: 1.38x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 650 ms: 1.38x slower                                                       |
| bench_mp_pool              | 64.8 ms                                                         | 89.7 ms: 1.38x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 5.25 ms: 1.41x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 46.0 ms: 1.46x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 1.41 ms: 1.59x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (7): regex_v8, pycparser, async_tree_cpu_io_mixed, xml_etree_process, pprint_pformat, async_tree_memoization_tg, async_tree_none
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (2) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1-amd64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown