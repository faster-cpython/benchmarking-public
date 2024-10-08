# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-amd64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.4 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 56.1 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.7 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.23 us: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| pickle_list          | 2.90 us                                                         | 3.00 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.9 ms: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.19 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.62 us: 1.15x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 210 us: 1.20x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 151 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.6 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.89 ms: 1.08x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| django_template | 21.7 ms                                                         | 26.0 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 523 us: 15.52x faster                                                      |
| deepcopy                   | 220 us                                                          | 189 us: 1.16x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.4 us: 1.08x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| regex_v8                   | 15.8 ms                                                         | 14.6 ms: 1.08x faster                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.38 sec: 1.07x faster                                                     |
| async_tree_none            | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.93 us: 1.03x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna                  | 119 ms                                                          | 119 ms: 1.00x slower                                                       |
| pickle                     | 7.11 us                                                         | 7.23 us: 1.02x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.64 us: 1.03x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 58.4 ms: 1.03x slower                                                      |
| pickle_list                | 2.90 us                                                         | 3.00 us: 1.03x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 84.4 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.9 ms: 1.04x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 66.4 ms: 1.04x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 67.6 ms: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| go                         | 82.1 ms                                                         | 85.8 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.8 ms: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 808 us: 1.05x slower                                                       |
| telco                      | 4.67 ms                                                         | 4.97 ms: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.0 ms: 1.07x slower                                                      |
| python_startup             | 20.3 ms                                                         | 21.7 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.69 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                      |
| unpickle_list              | 2.62 us                                                         | 2.83 us: 1.08x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.89 ms: 1.08x slower                                                      |
| 2to3                       | 207 ms                                                          | 224 ms: 1.08x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 17.6 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.9 ms: 1.09x slower                                                      |
| pylint                     | 205 ms                                                          | 224 ms: 1.10x slower                                                       |
| generators                 | 19.6 ms                                                         | 21.5 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                          | 245 ms: 1.10x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| json_dumps                 | 5.61 ms                                                         | 6.19 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.2 ms: 1.11x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.91 us: 1.11x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.43 us: 1.11x slower                                                      |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 63.1 ms: 1.11x slower                                                      |
| coverage                   | 42.1 ms                                                         | 46.9 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 193 ms: 1.12x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 113 us: 1.12x slower                                                       |
| chaos                      | 38.4 ms                                                         | 43.1 ms: 1.12x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.8 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.1 ms: 1.13x slower                                                      |
| float                      | 49.7 ms                                                         | 56.1 ms: 1.13x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 78.9 ms: 1.13x slower                                                      |
| sympy_expand               | 271 ms                                                          | 306 ms: 1.13x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 36.0 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 541 ms: 1.14x slower                                                       |
| unpickle                   | 8.40 us                                                         | 9.62 us: 1.15x slower                                                      |
| scimark_fft                | 171 ms                                                          | 196 ms: 1.15x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.11 sec: 1.15x slower                                                     |
| pyflate                    | 279 ms                                                          | 320 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.15x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| hexiom                     | 3.72 ms                                                         | 4.37 ms: 1.17x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 62.2 ns: 1.17x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.8 ms: 1.18x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| richards_super             | 30.2 ms                                                         | 35.9 ms: 1.19x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 892 us: 1.19x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 89.9 ms: 1.19x slower                                                      |
| richards                   | 26.7 ms                                                         | 31.9 ms: 1.20x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 210 us: 1.20x slower                                                       |
| django_template            | 21.7 ms                                                         | 26.0 ms: 1.20x slower                                                      |
| raytrace                   | 162 ms                                                          | 195 ms: 1.20x slower                                                       |
| fannkuch                   | 243 ms                                                          | 294 ms: 1.21x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                                      |
| nbody                      | 67.6 ms                                                         | 83.7 ms: 1.24x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 151 us: 1.24x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 48.7 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (11): async_tree_io, async_tree_memoization_tg, json, async_tree_memoization, create_gc_cycles, pathlib, async_tree_none_tg, pidigits, asyncio_tcp, async_tree_cpu_io_mixed, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown