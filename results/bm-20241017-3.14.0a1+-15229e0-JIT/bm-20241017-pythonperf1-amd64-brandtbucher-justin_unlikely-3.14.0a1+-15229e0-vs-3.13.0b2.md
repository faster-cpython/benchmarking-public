# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.05x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 251 ms: 1.22x slower                                                         |
| docutils       | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                       |
| html5lib       | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                        |
| tornado_http   | 81.8 ms                                                         | 101 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                           | 1.19x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 588 ms                                                          | 557 ms: 1.06x faster                                                         |
| async_tree_none_tg         | 202 ms                                                          | 211 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 605 ms                                                          | 637 ms: 1.05x slower                                                         |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 406 ms: 1.06x slower                                                         |
| async_tree_memoization     | 264 ms                                                          | 283 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 51.8 ms: 1.31x faster                                                        |
| float          | 49.7 ms                                                         | 46.7 ms: 1.06x faster                                                        |
| pidigits       | 150 ms                                                          | 148 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                        |
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                         |
| regex_effbot   | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                        |
| regex_compile  | 78.0 ms                                                         | 92.5 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.74 us: 1.06x faster                                                        |
| xml_etree_generate   | 53.2 ms                                                         | 51.0 ms: 1.04x faster                                                        |
| tomli_loads          | 1.35 sec                                                        | 1.32 sec: 1.03x faster                                                       |
| pickle_dict          | 18.1 us                                                         | 17.9 us: 1.02x faster                                                        |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                                        |
| pickle               | 7.11 us                                                         | 7.38 us: 1.04x slower                                                        |
| xml_etree_parse      | 90.9 ms                                                         | 95.3 ms: 1.05x slower                                                        |
| unpickle             | 8.40 us                                                         | 9.08 us: 1.08x slower                                                        |
| unpickle_list        | 2.62 us                                                         | 2.86 us: 1.09x slower                                                        |
| json_dumps           | 5.61 ms                                                         | 6.24 ms: 1.11x slower                                                        |
| pickle_pure_python   | 175 us                                                          | 202 us: 1.15x slower                                                         |
| unpickle_pure_python | 122 us                                                          | 147 us: 1.21x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                        |
| python_startup         | 20.3 ms                                                         | 24.3 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.02 ms: 1.27x faster                                                        |
| django_template | 21.7 ms                                                         | 27.0 ms: 1.25x slower                                                        |
| genshi_text     | 14.4 ms                                                         | 19.5 ms: 1.35x slower                                                        |
| genshi_xml      | 31.6 ms                                                         | 46.9 ms: 1.48x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 526 us: 15.41x faster                                                        |
| nbody                      | 67.6 ms                                                         | 51.8 ms: 1.31x faster                                                        |
| deepcopy_memo              | 22.1 us                                                         | 17.1 us: 1.30x faster                                                        |
| mako                       | 6.36 ms                                                         | 5.02 ms: 1.27x faster                                                        |
| scimark_sor                | 75.3 ms                                                         | 62.8 ms: 1.20x faster                                                        |
| spectral_norm              | 63.7 ms                                                         | 53.2 ms: 1.20x faster                                                        |
| deepcopy                   | 220 us                                                          | 192 us: 1.14x faster                                                         |
| crypto_pyaes               | 45.5 ms                                                         | 39.9 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.26 ms: 1.11x faster                                                        |
| scimark_fft                | 171 ms                                                          | 157 ms: 1.09x faster                                                         |
| regex_v8                   | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                        |
| float                      | 49.7 ms                                                         | 46.7 ms: 1.06x faster                                                        |
| json                       | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                        |
| pickle_list                | 2.90 us                                                         | 2.74 us: 1.06x faster                                                        |
| telco                      | 4.67 ms                                                         | 4.42 ms: 1.06x faster                                                        |
| async_tree_io              | 588 ms                                                          | 557 ms: 1.06x faster                                                         |
| pprint_safe_repr           | 474 ms                                                          | 449 ms: 1.05x faster                                                         |
| deepcopy_reduce            | 1.99 us                                                         | 1.90 us: 1.05x faster                                                        |
| pprint_pformat             | 966 ms                                                          | 924 ms: 1.05x faster                                                         |
| xml_etree_generate         | 53.2 ms                                                         | 51.0 ms: 1.04x faster                                                        |
| fannkuch                   | 243 ms                                                          | 234 ms: 1.04x faster                                                         |
| regex_dna                  | 119 ms                                                          | 114 ms: 1.04x faster                                                         |
| scimark_monte_carlo        | 39.1 ms                                                         | 37.8 ms: 1.04x faster                                                        |
| scimark_lu                 | 56.6 ms                                                         | 55.0 ms: 1.03x faster                                                        |
| tomli_loads                | 1.35 sec                                                        | 1.32 sec: 1.03x faster                                                       |
| pickle_dict                | 18.1 us                                                         | 17.9 us: 1.02x faster                                                        |
| pidigits                   | 150 ms                                                          | 148 ms: 1.02x faster                                                         |
| sqlite_synth               | 1.60 us                                                         | 1.59 us: 1.01x faster                                                        |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.01x slower                                                        |
| regex_effbot               | 1.58 ms                                                         | 1.60 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 62.3 ms                                                         | 63.5 ms: 1.02x slower                                                        |
| pickle                     | 7.11 us                                                         | 7.38 us: 1.04x slower                                                        |
| pyflate                    | 279 ms                                                          | 289 ms: 1.04x slower                                                         |
| async_tree_none_tg         | 202 ms                                                          | 211 ms: 1.04x slower                                                         |
| xml_etree_parse            | 90.9 ms                                                         | 95.3 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 605 ms                                                          | 637 ms: 1.05x slower                                                         |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 406 ms: 1.06x slower                                                         |
| logging_simple             | 5.78 us                                                         | 6.18 us: 1.07x slower                                                        |
| logging_format             | 6.22 us                                                         | 6.66 us: 1.07x slower                                                        |
| async_tree_memoization     | 264 ms                                                          | 283 ms: 1.07x slower                                                         |
| pathlib                    | 75.9 ms                                                         | 81.3 ms: 1.07x slower                                                        |
| bench_thread_pool          | 768 us                                                          | 825 us: 1.07x slower                                                         |
| meteor_contest             | 69.9 ms                                                         | 75.2 ms: 1.08x slower                                                        |
| unpickle                   | 8.40 us                                                         | 9.08 us: 1.08x slower                                                        |
| chaos                      | 38.4 ms                                                         | 41.5 ms: 1.08x slower                                                        |
| logging_silent             | 52.9 ns                                                         | 57.4 ns: 1.08x slower                                                        |
| dulwich_log                | 38.0 ms                                                         | 41.5 ms: 1.09x slower                                                        |
| unpickle_list              | 2.62 us                                                         | 2.86 us: 1.09x slower                                                        |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.10x slower                                                        |
| json_dumps                 | 5.61 ms                                                         | 6.24 ms: 1.11x slower                                                        |
| comprehensions             | 10.4 us                                                         | 11.6 us: 1.11x slower                                                        |
| coverage                   | 42.1 ms                                                         | 47.1 ms: 1.12x slower                                                        |
| nqueens                    | 56.7 ms                                                         | 63.5 ms: 1.12x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                        |
| html5lib                   | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 101 us                                                          | 116 us: 1.15x slower                                                         |
| pickle_pure_python         | 175 us                                                          | 202 us: 1.15x slower                                                         |
| go                         | 82.1 ms                                                         | 95.4 ms: 1.16x slower                                                        |
| generators                 | 19.6 ms                                                         | 22.9 ms: 1.17x slower                                                        |
| mdp                        | 1.31 sec                                                        | 1.55 sec: 1.18x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 92.5 ms: 1.19x slower                                                        |
| docutils                   | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                                       |
| python_startup             | 20.3 ms                                                         | 24.3 ms: 1.20x slower                                                        |
| async_generators           | 223 ms                                                          | 269 ms: 1.20x slower                                                         |
| sqlglot_normalize          | 173 ms                                                          | 209 ms: 1.21x slower                                                         |
| unpickle_pure_python       | 122 us                                                          | 147 us: 1.21x slower                                                         |
| sympy_sum                  | 84.4 ms                                                         | 102 ms: 1.21x slower                                                         |
| 2to3                       | 207 ms                                                          | 251 ms: 1.22x slower                                                         |
| sympy_expand               | 271 ms                                                          | 331 ms: 1.22x slower                                                         |
| sqlglot_parse              | 748 us                                                          | 915 us: 1.22x slower                                                         |
| tornado_http               | 81.8 ms                                                         | 101 ms: 1.23x slower                                                         |
| sympy_str                  | 159 ms                                                          | 196 ms: 1.23x slower                                                         |
| django_template            | 21.7 ms                                                         | 27.0 ms: 1.25x slower                                                        |
| deltablue                  | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                        |
| gc_traversal               | 1.55 ms                                                         | 1.96 ms: 1.26x slower                                                        |
| sqlglot_transpile          | 955 us                                                          | 1.21 ms: 1.27x slower                                                        |
| richards                   | 26.7 ms                                                         | 34.5 ms: 1.29x slower                                                        |
| richards_super             | 30.2 ms                                                         | 39.1 ms: 1.30x slower                                                        |
| sympy_integrate            | 12.2 ms                                                         | 15.9 ms: 1.30x slower                                                        |
| raytrace                   | 162 ms                                                          | 214 ms: 1.32x slower                                                         |
| sqlglot_optimize           | 32.7 ms                                                         | 43.2 ms: 1.32x slower                                                        |
| genshi_text                | 14.4 ms                                                         | 19.5 ms: 1.35x slower                                                        |
| bench_mp_pool              | 64.8 ms                                                         | 89.3 ms: 1.38x slower                                                        |
| pylint                     | 205 ms                                                          | 283 ms: 1.38x slower                                                         |
| hexiom                     | 3.72 ms                                                         | 5.25 ms: 1.41x slower                                                        |
| asyncio_tcp                | 471 ms                                                          | 666 ms: 1.41x slower                                                         |
| genshi_xml                 | 31.6 ms                                                         | 46.9 ms: 1.48x slower                                                        |
| create_gc_cycles           | 888 us                                                          | 1.42 ms: 1.59x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                 |

Benchmark hidden because not significant (6): pycparser, async_tree_cpu_io_mixed, xml_etree_process, async_tree_none, async_tree_memoization_tg, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown