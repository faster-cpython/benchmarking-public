# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-amd64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 224 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 55.8 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 81.8 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_dna      | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.6 ms: 1.04x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.07 us: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.3 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.3 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.34 us: 1.11x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 213 us: 1.22x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.79 ms: 1.07x slower                                                      |
| django_template | 21.7 ms                                                         | 25.7 ms: 1.18x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.5 ms: 1.19x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 519 us: 15.63x faster                                                      |
| deepcopy                   | 220 us                                                          | 192 us: 1.15x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.9 us: 1.06x faster                                                      |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.55 ms: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.96 us: 1.02x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                      |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 66.3 ms: 1.02x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.64 us: 1.03x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.31 us: 1.03x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.6 us: 1.03x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 84.2 ms: 1.03x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.6 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.60 ms: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.69 sec: 1.04x slower                                                     |
| bench_thread_pool          | 768 us                                                          | 807 us: 1.05x slower                                                       |
| go                         | 82.1 ms                                                         | 86.6 ms: 1.06x slower                                                      |
| pickle_list                | 2.90 us                                                         | 3.07 us: 1.06x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.77 us: 1.06x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 48.1 ms: 1.06x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 89.9 ms: 1.07x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.79 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.1 ms: 1.07x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.3 ms: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                          | 241 ms: 1.08x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 61.3 ms: 1.08x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.05 ms: 1.08x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 69.0 ms: 1.08x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| 2to3                       | 207 ms                                                          | 224 ms: 1.09x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.43 sec: 1.09x slower                                                     |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.62 sec: 1.09x slower                                                     |
| typing_runtime_protocols   | 101 us                                                          | 110 us: 1.09x slower                                                       |
| pylint                     | 205 ms                                                          | 224 ms: 1.10x slower                                                       |
| coverage                   | 42.1 ms                                                         | 46.3 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 191 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.4 ms                                                         | 40.3 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.91 us: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                      |
| chaos                      | 38.4 ms                                                         | 42.6 ms: 1.11x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.34 us: 1.11x slower                                                      |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 42.4 ms: 1.11x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 77.8 ms: 1.11x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.46 us: 1.12x slower                                                      |
| float                      | 49.7 ms                                                         | 55.8 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 63.8 ms: 1.13x slower                                                      |
| sympy_expand               | 271 ms                                                          | 306 ms: 1.13x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.5 ms: 1.14x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.10 sec: 1.14x slower                                                     |
| html5lib                   | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 543 ms: 1.15x slower                                                       |
| pyflate                    | 279 ms                                                          | 322 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.16x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| richards_super             | 30.2 ms                                                         | 35.6 ms: 1.18x slower                                                      |
| django_template            | 21.7 ms                                                         | 25.7 ms: 1.18x slower                                                      |
| scimark_fft                | 171 ms                                                          | 203 ms: 1.19x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.60 sec: 1.19x slower                                                     |
| hexiom                     | 3.72 ms                                                         | 4.42 ms: 1.19x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 37.5 ms: 1.19x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 63.0 ns: 1.19x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 895 us: 1.20x slower                                                       |
| raytrace                   | 162 ms                                                          | 194 ms: 1.20x slower                                                       |
| richards                   | 26.7 ms                                                         | 32.0 ms: 1.20x slower                                                      |
| fannkuch                   | 243 ms                                                          | 293 ms: 1.20x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.27 ms: 1.21x slower                                                      |
| nbody                      | 67.6 ms                                                         | 81.8 ms: 1.21x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 213 us: 1.22x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 149 us: 1.22x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 92.2 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.0 ms: 1.25x slower                                                      |
| json                       | 3.19 ms                                                         | 4.39 ms: 1.38x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, async_tree_io, pycparser, async_tree_memoization_tg, create_gc_cycles, pathlib, async_tree_cpu_io_mixed, pidigits, async_tree_memoization, async_tree_none_tg, asyncio_tcp
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1-amd64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown