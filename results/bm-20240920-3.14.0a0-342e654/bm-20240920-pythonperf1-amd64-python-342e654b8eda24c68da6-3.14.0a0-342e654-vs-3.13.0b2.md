# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 225 ms: 1.09x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 84.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 566 ms: 1.07x faster                                                       |
| async_tree_none            | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| float          | 49.7 ms                                                         | 55.8 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 85.0 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 117 ms: 1.01x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 92.6 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.75 us: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.51 us: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 218 us: 1.24x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.11 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.4 ms: 1.12x slower                                                      |
| django_template | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 525 us: 15.44x faster                                                      |
| deepcopy                   | 220 us                                                          | 193 us: 1.14x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 566 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.94 us: 1.03x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 21.5 us: 1.03x faster                                                      |
| async_tree_none            | 218 ms                                                          | 213 ms: 1.02x faster                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.01x faster                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pidigits                   | 150 ms                                                          | 150 ms: 1.00x slower                                                       |
| pickle                     | 7.11 us                                                         | 7.19 us: 1.01x slower                                                      |
| sqlite_synth               | 1.60 us                                                         | 1.62 us: 1.01x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| pickle_dict                | 18.1 us                                                         | 18.5 us: 1.02x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 66.4 ms: 1.03x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 64.3 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 84.6 ms: 1.03x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                     |
| unpickle_list              | 2.62 us                                                         | 2.75 us: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 811 us: 1.06x slower                                                       |
| go                         | 82.1 ms                                                         | 87.6 ms: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 90.7 ms: 1.07x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 49.2 ms: 1.08x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.09x slower                                                      |
| 2to3                       | 207 ms                                                          | 225 ms: 1.09x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 61.7 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                          | 245 ms: 1.10x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.16 ms: 1.10x slower                                                      |
| pylint                     | 205 ms                                                          | 225 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| spectral_norm              | 63.7 ms                                                         | 70.5 ms: 1.11x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.45 sec: 1.11x slower                                                     |
| logging_simple             | 5.78 us                                                         | 6.42 us: 1.11x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.91 us: 1.11x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 192 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 36.4 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.11x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.11 ms: 1.12x slower                                                      |
| float                      | 49.7 ms                                                         | 55.8 ms: 1.12x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 35.4 ms: 1.12x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 78.4 ms: 1.12x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.3 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.0 ms: 1.13x slower                                                      |
| sympy_str                  | 159 ms                                                          | 179 ms: 1.13x slower                                                       |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.68 sec: 1.13x slower                                                     |
| unpickle                   | 8.40 us                                                         | 9.51 us: 1.13x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.2 ms: 1.13x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 64.4 ms: 1.14x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.5 ms: 1.14x slower                                                      |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.14x slower                                                      |
| sympy_expand               | 271 ms                                                          | 310 ms: 1.15x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.2 ms: 1.15x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.39 ms: 1.15x slower                                                      |
| pyflate                    | 279 ms                                                          | 322 ms: 1.16x slower                                                       |
| pprint_safe_repr           | 474 ms                                                          | 548 ms: 1.16x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| sqlglot_transpile          | 955 us                                                          | 1.12 ms: 1.17x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.93 ms: 1.17x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 92.6 ms: 1.19x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.1 ms: 1.20x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.46 ms: 1.20x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 896 us: 1.20x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 63.4 ns: 1.20x slower                                                      |
| richards                   | 26.7 ms                                                         | 32.1 ms: 1.20x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.30 ms: 1.22x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 92.5 ms: 1.23x slower                                                      |
| fannkuch                   | 243 ms                                                          | 300 ms: 1.23x slower                                                       |
| raytrace                   | 162 ms                                                          | 201 ms: 1.24x slower                                                       |
| scimark_fft                | 171 ms                                                          | 212 ms: 1.24x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 218 us: 1.24x slower                                                       |
| nbody                      | 67.6 ms                                                         | 85.0 ms: 1.26x slower                                                      |
| json                       | 3.19 ms                                                         | 4.04 ms: 1.27x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 155 us: 1.27x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.6 ms: 1.29x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, async_tree_memoization_tg, async_tree_io, pycparser, asyncio_tcp, create_gc_cycles, pathlib, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, pickle_list
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown