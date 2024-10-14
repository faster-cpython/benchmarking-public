# Results vs. 3.13.0b2

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-amd64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 229 ms: 1.11x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.72 sec: 1.06x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.9 ms: 1.22x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 94.9 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg       | 605 ms                                                          | 579 ms: 1.05x faster                                                       |
| async_tree_memoization | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| float          | 49.7 ms                                                         | 53.8 ms: 1.08x slower                                                      |
| nbody          | 67.6 ms                                                         | 79.3 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 91.3 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.95 us: 1.02x slower                                                      |
| pickle               | 7.11 us                                                         | 7.25 us: 1.02x slower                                                      |
| json_loads           | 14.2 us                                                         | 14.7 us: 1.04x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 19.2 us: 1.06x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 96.5 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                      |
| unpickle_list        | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                                      |
| unpickle             | 8.40 us                                                         | 9.40 us: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.75 ms: 1.20x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.64 sec: 1.21x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.22x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 220 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.78 ms: 1.07x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| django_template | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 516 us: 15.72x faster                                                      |
| deepcopy                 | 220 us                                                          | 193 us: 1.14x faster                                                       |
| deepcopy_memo            | 22.1 us                                                         | 19.7 us: 1.12x faster                                                      |
| async_tree_io_tg         | 605 ms                                                          | 579 ms: 1.05x faster                                                       |
| gc_traversal             | 1.55 ms                                                         | 1.53 ms: 1.01x faster                                                      |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| pidigits                 | 150 ms                                                          | 149 ms: 1.01x faster                                                       |
| regex_dna                | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| pickle_list              | 2.90 us                                                         | 2.95 us: 1.02x slower                                                      |
| pickle                   | 7.11 us                                                         | 7.25 us: 1.02x slower                                                      |
| async_tree_memoization   | 264 ms                                                          | 272 ms: 1.03x slower                                                       |
| scimark_lu               | 56.6 ms                                                         | 58.4 ms: 1.03x slower                                                      |
| telco                    | 4.67 ms                                                         | 4.83 ms: 1.03x slower                                                      |
| json_loads               | 14.2 us                                                         | 14.7 us: 1.04x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 923 us: 1.04x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.67 us: 1.04x slower                                                      |
| go                       | 82.1 ms                                                         | 86.4 ms: 1.05x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 48.1 ms: 1.06x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 812 us: 1.06x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 80.4 ms: 1.06x slower                                                      |
| pickle_dict              | 18.1 us                                                         | 19.2 us: 1.06x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.72 sec: 1.06x slower                                                     |
| xml_etree_parse          | 90.9 ms                                                         | 96.5 ms: 1.06x slower                                                      |
| xml_etree_iterparse      | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                      |
| mako                     | 6.36 ms                                                         | 6.78 ms: 1.07x slower                                                      |
| unpickle_list            | 2.62 us                                                         | 2.80 us: 1.07x slower                                                      |
| bench_mp_pool            | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 68.3 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.68 ms: 1.07x slower                                                      |
| sympy_sum                | 84.4 ms                                                         | 90.9 ms: 1.08x slower                                                      |
| xml_etree_generate       | 53.2 ms                                                         | 57.4 ms: 1.08x slower                                                      |
| float                    | 49.7 ms                                                         | 53.8 ms: 1.08x slower                                                      |
| coroutines               | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 76.6 ms: 1.10x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.85 us: 1.10x slower                                                      |
| generators               | 19.6 ms                                                         | 21.5 ms: 1.10x slower                                                      |
| xml_etree_process        | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 13.5 ms: 1.10x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.38 us: 1.10x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 112 us: 1.11x slower                                                       |
| 2to3                     | 207 ms                                                          | 229 ms: 1.11x slower                                                       |
| coverage                 | 42.1 ms                                                         | 46.6 ms: 1.11x slower                                                      |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.65 sec: 1.11x slower                                                     |
| async_generators         | 223 ms                                                          | 249 ms: 1.11x slower                                                       |
| unpickle                 | 8.40 us                                                         | 9.40 us: 1.12x slower                                                      |
| sympy_str                | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| python_startup_no_site   | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| pylint                   | 205 ms                                                          | 230 ms: 1.12x slower                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                                      |
| sqlglot_normalize        | 173 ms                                                          | 196 ms: 1.13x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 64.4 ms: 1.14x slower                                                      |
| comprehensions           | 10.4 us                                                         | 11.8 us: 1.14x slower                                                      |
| chaos                    | 38.4 ms                                                         | 43.7 ms: 1.14x slower                                                      |
| pyflate                  | 279 ms                                                          | 318 ms: 1.14x slower                                                       |
| sympy_expand             | 271 ms                                                          | 309 ms: 1.14x slower                                                       |
| logging_silent           | 52.9 ns                                                         | 60.7 ns: 1.15x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 547 ms: 1.15x slower                                                       |
| pprint_pformat           | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| fannkuch                 | 243 ms                                                          | 282 ms: 1.16x slower                                                       |
| tornado_http             | 81.8 ms                                                         | 94.9 ms: 1.16x slower                                                      |
| hexiom                   | 3.72 ms                                                         | 4.33 ms: 1.16x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 44.5 ms: 1.17x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 88.2 ms: 1.17x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 37.0 ms: 1.17x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 91.3 ms: 1.17x slower                                                      |
| nbody                    | 67.6 ms                                                         | 79.3 ms: 1.17x slower                                                      |
| mdp                      | 1.31 sec                                                        | 1.55 sec: 1.18x slower                                                     |
| django_template          | 21.7 ms                                                         | 25.7 ms: 1.19x slower                                                      |
| scimark_fft              | 171 ms                                                          | 203 ms: 1.19x slower                                                       |
| sqlglot_transpile        | 955 us                                                          | 1.14 ms: 1.19x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 17.1 ms: 1.19x slower                                                      |
| scimark_monte_carlo      | 39.1 ms                                                         | 46.7 ms: 1.19x slower                                                      |
| richards                 | 26.7 ms                                                         | 32.1 ms: 1.20x slower                                                      |
| deltablue                | 1.88 ms                                                         | 2.26 ms: 1.20x slower                                                      |
| richards_super           | 30.2 ms                                                         | 36.2 ms: 1.20x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 6.75 ms: 1.20x slower                                                      |
| asyncio_tcp              | 471 ms                                                          | 568 ms: 1.21x slower                                                       |
| tomli_loads              | 1.35 sec                                                        | 1.64 sec: 1.21x slower                                                     |
| sqlglot_parse            | 748 us                                                          | 908 us: 1.21x slower                                                       |
| unpickle_pure_python     | 122 us                                                          | 148 us: 1.22x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 42.9 ms: 1.22x slower                                                      |
| pickle_pure_python       | 175 us                                                          | 220 us: 1.25x slower                                                       |
| raytrace                 | 162 ms                                                          | 207 ms: 1.28x slower                                                       |
| json                     | 3.19 ms                                                         | 4.18 ms: 1.31x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, async_tree_none, pycparser, async_tree_memoization_tg, deepcopy_reduce, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown