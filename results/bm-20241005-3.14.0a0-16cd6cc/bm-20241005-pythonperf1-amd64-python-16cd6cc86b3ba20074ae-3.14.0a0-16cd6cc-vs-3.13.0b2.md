# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-amd64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.2 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 92.2 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 82.0 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.27 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.7 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.7 ms: 1.04x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.9 us: 1.04x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.04 us: 1.08x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.6 ms: 1.08x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.19 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 213 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.03 ms: 1.11x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.7 ms: 1.13x slower                                                      |
| django_template | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 525 us: 15.44x faster                                                      |
| deepcopy                   | 220 us                                                          | 187 us: 1.18x faster                                                       |
| regex_v8                   | 15.8 ms                                                         | 14.7 ms: 1.07x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 565 ms: 1.07x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.9 us: 1.06x faster                                                      |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.91 us: 1.04x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| gc_traversal               | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                      |
| regex_dna                  | 119 ms                                                          | 119 ms: 1.00x faster                                                       |
| pidigits                   | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| sqlite_synth               | 1.60 us                                                         | 1.62 us: 1.02x slower                                                      |
| pickle                     | 7.11 us                                                         | 7.27 us: 1.02x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 94.0 ms: 1.03x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 78.4 ms: 1.03x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.7 us: 1.03x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 397 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.7 ms: 1.04x slower                                                      |
| pickle_dict                | 18.1 us                                                         | 18.9 us: 1.04x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 802 us: 1.04x slower                                                       |
| go                         | 82.1 ms                                                         | 85.9 ms: 1.05x slower                                                      |
| telco                      | 4.67 ms                                                         | 4.89 ms: 1.05x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 68.8 ms: 1.06x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.1 ms: 1.07x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.58 sec: 1.07x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| unpickle                   | 8.40 us                                                         | 9.04 us: 1.08x slower                                                      |
| 2to3                       | 207 ms                                                          | 223 ms: 1.08x slower                                                       |
| python_startup             | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.73 us: 1.08x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.6 ms: 1.08x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.29 us: 1.09x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 110 us: 1.09x slower                                                       |
| pylint                     | 205 ms                                                          | 223 ms: 1.09x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 13.4 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| coverage                   | 42.1 ms                                                         | 46.0 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                          | 244 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.75 ms: 1.10x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.44 sec: 1.10x slower                                                     |
| json_dumps                 | 5.61 ms                                                         | 6.19 ms: 1.10x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 50.2 ms: 1.10x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.03 ms: 1.11x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 77.4 ms: 1.11x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 192 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 526 ms: 1.12x slower                                                       |
| spectral_norm              | 63.7 ms                                                         | 71.5 ms: 1.12x slower                                                      |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.12x slower                                                       |
| float                      | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 63.7 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 92.2 ms: 1.13x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 35.7 ms: 1.13x slower                                                      |
| chaos                      | 38.4 ms                                                         | 43.6 ms: 1.14x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 64.7 ms: 1.14x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.5 ms: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 310 ms: 1.15x slower                                                       |
| pprint_safe_repr           | 474 ms                                                          | 546 ms: 1.15x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.10 ms: 1.15x slower                                                      |
| django_template            | 21.7 ms                                                         | 25.1 ms: 1.16x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.16x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 62.3 ns: 1.18x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| pyflate                    | 279 ms                                                          | 328 ms: 1.18x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 885 us: 1.18x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.43 ms: 1.19x slower                                                      |
| richards                   | 26.7 ms                                                         | 32.0 ms: 1.20x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.2 ms: 1.20x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.2 ms: 1.20x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 91.3 ms: 1.21x slower                                                      |
| nbody                      | 67.6 ms                                                         | 82.0 ms: 1.21x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 213 us: 1.21x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 148 us: 1.22x slower                                                       |
| scimark_fft                | 171 ms                                                          | 209 ms: 1.22x slower                                                       |
| raytrace                   | 162 ms                                                          | 201 ms: 1.24x slower                                                       |
| fannkuch                   | 243 ms                                                          | 305 ms: 1.25x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.5 ms: 1.27x slower                                                      |
| json                       | 3.19 ms                                                         | 4.33 ms: 1.36x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (8): pycparser, async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, create_gc_cycles, pickle_list
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown