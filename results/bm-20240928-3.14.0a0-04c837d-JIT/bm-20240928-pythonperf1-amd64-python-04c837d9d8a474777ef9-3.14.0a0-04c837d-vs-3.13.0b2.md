# Results vs. 3.13.0b2

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.02x slower
- HPT reliability: 99.64%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 248 ms: 1.20x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 98.4 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                           | 1.20x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 556 ms: 1.09x faster                                                       |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 47.9 ms: 1.41x faster                                                      |
| float          | 49.7 ms                                                         | 45.2 ms: 1.10x faster                                                      |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                           | 1.16x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                      |
| regex_dna      | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 94.1 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| pickle_list          | 2.90 us                                                         | 2.82 us: 1.03x faster                                                      |
| pickle_dict          | 18.1 us                                                         | 17.7 us: 1.03x faster                                                      |
| xml_etree_process    | 36.4 ms                                                         | 35.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.6 ms: 1.01x faster                                                      |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 5.72 ms: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.39 us: 1.04x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.6 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.79 us: 1.07x slower                                                      |
| pickle_pure_python   | 175 us                                                          | 201 us: 1.14x slower                                                       |
| unpickle             | 8.40 us                                                         | 9.77 us: 1.16x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 144 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.10 ms: 1.25x faster                                                      |
| django_template | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 19.5 ms: 1.35x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 46.4 ms: 1.47x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 519 us: 15.63x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 15.0 us: 1.48x faster                                                      |
| spectral_norm              | 63.7 ms                                                         | 44.0 ms: 1.45x faster                                                      |
| nbody                      | 67.6 ms                                                         | 47.9 ms: 1.41x faster                                                      |
| mako                       | 6.36 ms                                                         | 5.10 ms: 1.25x faster                                                      |
| scimark_sor                | 75.3 ms                                                         | 61.9 ms: 1.22x faster                                                      |
| deepcopy                   | 220 us                                                          | 185 us: 1.19x faster                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 38.7 ms: 1.17x faster                                                      |
| scimark_fft                | 171 ms                                                          | 146 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.15 ms: 1.16x faster                                                      |
| float                      | 49.7 ms                                                         | 45.2 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 556 ms: 1.09x faster                                                       |
| regex_v8                   | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                                      |
| telco                      | 4.67 ms                                                         | 4.36 ms: 1.07x faster                                                      |
| pyflate                    | 279 ms                                                          | 261 ms: 1.07x faster                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.88 us: 1.06x faster                                                      |
| async_tree_none            | 218 ms                                                          | 206 ms: 1.06x faster                                                       |
| json                       | 3.19 ms                                                         | 3.02 ms: 1.05x faster                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.29 sec: 1.05x faster                                                     |
| pickle_list                | 2.90 us                                                         | 2.82 us: 1.03x faster                                                      |
| pickle_dict                | 18.1 us                                                         | 17.7 us: 1.03x faster                                                      |
| scimark_lu                 | 56.6 ms                                                         | 55.3 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.4 ms                                                         | 35.7 ms: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                      |
| fannkuch                   | 243 ms                                                          | 239 ms: 1.02x faster                                                       |
| deltablue                  | 1.88 ms                                                         | 1.86 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 61.6 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                                       |
| sqlite_synth               | 1.60 us                                                         | 1.61 us: 1.01x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 5.72 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                         | 10.7 us: 1.03x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.39 us: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 94.6 ms: 1.04x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.48 us: 1.04x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.08 us: 1.05x slower                                                      |
| chaos                      | 38.4 ms                                                         | 40.3 ms: 1.05x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 79.9 ms: 1.05x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.79 us: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 826 us: 1.08x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 57.1 ns: 1.08x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.04 sec: 1.08x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 514 ms: 1.08x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 61.5 ms: 1.09x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 76.1 ms: 1.09x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.0 ms: 1.09x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 112 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 43.4 ms: 1.11x slower                                                      |
| coverage                   | 42.1 ms                                                         | 46.8 ms: 1.11x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 72.9 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.4 ms: 1.14x slower                                                      |
| generators                 | 19.6 ms                                                         | 22.3 ms: 1.14x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 201 us: 1.14x slower                                                       |
| go                         | 82.1 ms                                                         | 94.1 ms: 1.15x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 545 ms: 1.16x slower                                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.71 sec: 1.16x slower                                                     |
| unpickle                   | 8.40 us                                                         | 9.77 us: 1.16x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.92 sec: 1.18x slower                                                     |
| sqlglot_normalize          | 173 ms                                                          | 205 ms: 1.18x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 144 us: 1.18x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.57 sec: 1.19x slower                                                     |
| async_generators           | 223 ms                                                          | 267 ms: 1.19x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 895 us: 1.20x slower                                                       |
| 2to3                       | 207 ms                                                          | 248 ms: 1.20x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 98.4 ms: 1.20x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.1 ms: 1.20x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 94.1 ms: 1.21x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 102 ms: 1.21x slower                                                       |
| sympy_str                  | 159 ms                                                          | 195 ms: 1.23x slower                                                       |
| sympy_expand               | 271 ms                                                          | 334 ms: 1.23x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.18 ms: 1.24x slower                                                      |
| django_template            | 21.7 ms                                                         | 26.9 ms: 1.24x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 15.3 ms: 1.25x slower                                                      |
| raytrace                   | 162 ms                                                          | 210 ms: 1.29x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 43.0 ms: 1.31x slower                                                      |
| pylint                     | 205 ms                                                          | 272 ms: 1.33x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 5.03 ms: 1.35x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 19.5 ms: 1.35x slower                                                      |
| richards_super             | 30.2 ms                                                         | 41.7 ms: 1.38x slower                                                      |
| richards                   | 26.7 ms                                                         | 38.7 ms: 1.45x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 46.4 ms: 1.47x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (8): pycparser, async_tree_memoization, async_tree_none_tg, async_tree_io, create_gc_cycles, async_tree_memoization_tg, regex_effbot, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240928-3.14.0a0-04c837d-JIT/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: unpack_sequence

# HPT report

- Reliability score: 99.64% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown