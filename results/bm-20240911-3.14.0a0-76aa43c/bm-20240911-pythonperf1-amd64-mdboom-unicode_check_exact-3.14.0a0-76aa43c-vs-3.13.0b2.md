# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-amd64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 220 ms: 1.07x slower                                                      |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                    |
| html5lib       | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                     |
| tornado_http   | 81.8 ms                                                         | 83.5 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                           | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                      |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                              |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 54.2 ms: 1.09x slower                                                     |
| nbody          | 67.6 ms                                                         | 82.1 ms: 1.21x slower                                                     |
| Geometric mean | (ref)                                                           | 1.10x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                     |
| regex_dna      | 119 ms                                                          | 114 ms: 1.05x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                                     |
| regex_compile  | 78.0 ms                                                         | 89.2 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                           | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.15 us: 1.01x slower                                                     |
| xml_etree_parse      | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                     |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                     |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.5 ms: 1.03x slower                                                     |
| unpickle_list        | 2.62 us                                                         | 2.73 us: 1.04x slower                                                     |
| pickle_dict          | 18.1 us                                                         | 19.2 us: 1.06x slower                                                     |
| xml_etree_generate   | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                     |
| json_dumps           | 5.61 ms                                                         | 6.14 ms: 1.09x slower                                                     |
| xml_etree_process    | 36.4 ms                                                         | 40.3 ms: 1.10x slower                                                     |
| unpickle             | 8.40 us                                                         | 9.50 us: 1.13x slower                                                     |
| tomli_loads          | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                    |
| pickle_pure_python   | 175 us                                                          | 207 us: 1.18x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 147 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                              |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                     |
| python_startup_no_site | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.84 ms: 1.08x slower                                                     |
| django_template | 21.7 ms                                                         | 24.4 ms: 1.13x slower                                                     |
| genshi_xml      | 31.6 ms                                                         | 36.7 ms: 1.16x slower                                                     |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 512 us: 15.83x faster                                                     |
| deepcopy                   | 220 us                                                          | 190 us: 1.16x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 20.2 us: 1.10x faster                                                     |
| regex_v8                   | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                     |
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                      |
| json                       | 3.19 ms                                                         | 3.00 ms: 1.06x faster                                                     |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                      |
| regex_dna                  | 119 ms                                                          | 114 ms: 1.05x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.93 us: 1.04x faster                                                     |
| regex_effbot               | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                                     |
| pathlib                    | 75.9 ms                                                         | 74.2 ms: 1.02x faster                                                     |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                     |
| pickle                     | 7.11 us                                                         | 7.15 us: 1.01x slower                                                     |
| sqlite_synth               | 1.60 us                                                         | 1.62 us: 1.01x slower                                                     |
| xml_etree_parse            | 90.9 ms                                                         | 92.5 ms: 1.02x slower                                                     |
| tornado_http               | 81.8 ms                                                         | 83.5 ms: 1.02x slower                                                     |
| json_loads                 | 14.2 us                                                         | 14.5 us: 1.02x slower                                                     |
| spectral_norm              | 63.7 ms                                                         | 65.3 ms: 1.02x slower                                                     |
| go                         | 82.1 ms                                                         | 84.6 ms: 1.03x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.5 ms: 1.03x slower                                                     |
| docutils                   | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.2 ms: 1.04x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.73 us: 1.04x slower                                                     |
| bench_mp_pool              | 64.8 ms                                                         | 67.4 ms: 1.04x slower                                                     |
| python_startup             | 20.3 ms                                                         | 21.3 ms: 1.05x slower                                                     |
| bench_thread_pool          | 768 us                                                          | 807 us: 1.05x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 89.1 ms: 1.06x slower                                                     |
| pickle_dict                | 18.1 us                                                         | 19.2 us: 1.06x slower                                                     |
| scimark_lu                 | 56.6 ms                                                         | 59.9 ms: 1.06x slower                                                     |
| mdp                        | 1.31 sec                                                        | 1.40 sec: 1.06x slower                                                    |
| sympy_integrate            | 12.2 ms                                                         | 13.0 ms: 1.06x slower                                                     |
| 2to3                       | 207 ms                                                          | 220 ms: 1.07x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.58 sec: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.67 ms: 1.07x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                     |
| logging_format             | 6.22 us                                                         | 6.67 us: 1.07x slower                                                     |
| xml_etree_generate         | 53.2 ms                                                         | 57.2 ms: 1.08x slower                                                     |
| mako                       | 6.36 ms                                                         | 6.84 ms: 1.08x slower                                                     |
| async_generators           | 223 ms                                                          | 241 ms: 1.08x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.24 us: 1.08x slower                                                     |
| telco                      | 4.67 ms                                                         | 5.04 ms: 1.08x slower                                                     |
| generators                 | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                     |
| typing_runtime_protocols   | 101 us                                                          | 110 us: 1.09x slower                                                      |
| float                      | 49.7 ms                                                         | 54.2 ms: 1.09x slower                                                     |
| json_dumps                 | 5.61 ms                                                         | 6.14 ms: 1.09x slower                                                     |
| pylint                     | 205 ms                                                          | 224 ms: 1.09x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.1 ms: 1.10x slower                                                     |
| sympy_str                  | 159 ms                                                          | 175 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 191 ms: 1.10x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 40.3 ms: 1.10x slower                                                     |
| coverage                   | 42.1 ms                                                         | 46.6 ms: 1.11x slower                                                     |
| dulwich_log                | 38.0 ms                                                         | 42.1 ms: 1.11x slower                                                     |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                     |
| comprehensions             | 10.4 us                                                         | 11.5 us: 1.11x slower                                                     |
| meteor_contest             | 69.9 ms                                                         | 78.1 ms: 1.12x slower                                                     |
| chaos                      | 38.4 ms                                                         | 42.9 ms: 1.12x slower                                                     |
| nqueens                    | 56.7 ms                                                         | 63.7 ms: 1.12x slower                                                     |
| sympy_expand               | 271 ms                                                          | 304 ms: 1.12x slower                                                      |
| django_template            | 21.7 ms                                                         | 24.4 ms: 1.13x slower                                                     |
| raytrace                   | 162 ms                                                          | 184 ms: 1.13x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.50 us: 1.13x slower                                                     |
| pyflate                    | 279 ms                                                          | 316 ms: 1.13x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.09 ms: 1.14x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 541 ms: 1.14x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 86.1 ms: 1.14x slower                                                     |
| html5lib                   | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                     |
| regex_compile              | 78.0 ms                                                         | 89.2 ms: 1.14x slower                                                     |
| pprint_pformat             | 966 ms                                                          | 1.11 sec: 1.15x slower                                                    |
| tomli_loads                | 1.35 sec                                                        | 1.55 sec: 1.15x slower                                                    |
| sqlglot_parse              | 748 us                                                          | 868 us: 1.16x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.7 ms: 1.16x slower                                                     |
| scimark_fft                | 171 ms                                                          | 199 ms: 1.16x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.33 ms: 1.16x slower                                                     |
| logging_silent             | 52.9 ns                                                         | 61.7 ns: 1.17x slower                                                     |
| richards_super             | 30.2 ms                                                         | 35.5 ms: 1.18x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                     |
| pickle_pure_python         | 175 us                                                          | 207 us: 1.18x slower                                                      |
| richards                   | 26.7 ms                                                         | 31.5 ms: 1.18x slower                                                     |
| deltablue                  | 1.88 ms                                                         | 2.23 ms: 1.18x slower                                                     |
| fannkuch                   | 243 ms                                                          | 289 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 147 us: 1.21x slower                                                      |
| nbody                      | 67.6 ms                                                         | 82.1 ms: 1.21x slower                                                     |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.1 ms: 1.26x slower                                                     |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                              |

Benchmark hidden because not significant (10): async_tree_io, async_tree_memoization_tg, asyncio_tcp, async_tree_none_tg, async_tree_memoization, pycparser, create_gc_cycles, pidigits, pickle_list, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1-amd64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown