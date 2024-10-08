# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: windows-amd64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                                |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                              |
| html5lib       | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                               |
| tornado_http   | 81.8 ms                                                         | 92.9 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                           | 1.10x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 566 ms: 1.07x faster                                                |
| async_tree_none  | 218 ms                                                          | 207 ms: 1.05x faster                                                |
| Geometric mean   | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                |
| float          | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                               |
| nbody          | 67.6 ms                                                         | 81.0 ms: 1.20x slower                                               |
| Geometric mean | (ref)                                                           | 1.11x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                               |
| regex_dna      | 119 ms                                                          | 114 ms: 1.04x faster                                                |
| regex_effbot   | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                               |
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                               |
| Geometric mean | (ref)                                                           | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                               |
| xml_etree_parse      | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                               |
| xml_etree_iterparse  | 62.3 ms                                                         | 64.4 ms: 1.03x slower                                               |
| unpickle_list        | 2.62 us                                                         | 2.74 us: 1.05x slower                                               |
| xml_etree_generate   | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                               |
| unpickle             | 8.40 us                                                         | 9.30 us: 1.11x slower                                               |
| xml_etree_process    | 36.4 ms                                                         | 40.7 ms: 1.12x slower                                               |
| json_dumps           | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                               |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                              |
| pickle_pure_python   | 175 us                                                          | 215 us: 1.22x slower                                                |
| unpickle_pure_python | 122 us                                                          | 150 us: 1.23x slower                                                |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                        |

Benchmark hidden because not significant (3): json_loads, pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                               |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                               |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.93 ms: 1.09x slower                                               |
| genshi_xml      | 31.6 ms                                                         | 35.6 ms: 1.13x slower                                               |
| django_template | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                               |
| genshi_text     | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                               |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 513 us: 15.80x faster                                               |
| deepcopy                 | 220 us                                                          | 185 us: 1.19x faster                                                |
| deepcopy_memo            | 22.1 us                                                         | 20.1 us: 1.10x faster                                               |
| regex_v8                 | 15.8 ms                                                         | 14.7 ms: 1.08x faster                                               |
| async_tree_io_tg         | 605 ms                                                          | 566 ms: 1.07x faster                                                |
| async_tree_none          | 218 ms                                                          | 207 ms: 1.05x faster                                                |
| regex_dna                | 119 ms                                                          | 114 ms: 1.04x faster                                                |
| regex_effbot             | 1.58 ms                                                         | 1.54 ms: 1.03x faster                                               |
| deepcopy_reduce          | 1.99 us                                                         | 1.95 us: 1.03x faster                                               |
| pidigits                 | 150 ms                                                          | 151 ms: 1.00x slower                                                |
| gc_traversal             | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                               |
| pickle_dict              | 18.1 us                                                         | 18.4 us: 1.01x slower                                               |
| sqlite_synth             | 1.60 us                                                         | 1.63 us: 1.02x slower                                               |
| xml_etree_parse          | 90.9 ms                                                         | 93.5 ms: 1.03x slower                                               |
| create_gc_cycles         | 888 us                                                          | 917 us: 1.03x slower                                                |
| xml_etree_iterparse      | 62.3 ms                                                         | 64.4 ms: 1.03x slower                                               |
| telco                    | 4.67 ms                                                         | 4.84 ms: 1.04x slower                                               |
| pathlib                  | 75.9 ms                                                         | 78.8 ms: 1.04x slower                                               |
| docutils                 | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                              |
| unpickle_list            | 2.62 us                                                         | 2.74 us: 1.05x slower                                               |
| go                       | 82.1 ms                                                         | 87.1 ms: 1.06x slower                                               |
| bench_mp_pool            | 64.8 ms                                                         | 68.9 ms: 1.06x slower                                               |
| sympy_sum                | 84.4 ms                                                         | 90.0 ms: 1.07x slower                                               |
| bench_thread_pool        | 768 us                                                          | 819 us: 1.07x slower                                                |
| generators               | 19.6 ms                                                         | 20.9 ms: 1.07x slower                                               |
| mdp                      | 1.31 sec                                                        | 1.41 sec: 1.08x slower                                              |
| spectral_norm            | 63.7 ms                                                         | 68.8 ms: 1.08x slower                                               |
| crypto_pyaes             | 45.5 ms                                                         | 49.3 ms: 1.08x slower                                               |
| python_startup           | 20.3 ms                                                         | 22.1 ms: 1.09x slower                                               |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.72 ms: 1.09x slower                                               |
| coroutines               | 12.8 ms                                                         | 13.9 ms: 1.09x slower                                               |
| typing_runtime_protocols | 101 us                                                          | 110 us: 1.09x slower                                                |
| mako                     | 6.36 ms                                                         | 6.93 ms: 1.09x slower                                               |
| xml_etree_generate       | 53.2 ms                                                         | 58.0 ms: 1.09x slower                                               |
| pylint                   | 205 ms                                                          | 223 ms: 1.09x slower                                                |
| meteor_contest           | 69.9 ms                                                         | 76.3 ms: 1.09x slower                                               |
| 2to3                     | 207 ms                                                          | 226 ms: 1.09x slower                                                |
| logging_simple           | 5.78 us                                                         | 6.33 us: 1.09x slower                                               |
| sympy_integrate          | 12.2 ms                                                         | 13.4 ms: 1.10x slower                                               |
| python_startup_no_site   | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                               |
| logging_format           | 6.22 us                                                         | 6.82 us: 1.10x slower                                               |
| async_generators         | 223 ms                                                          | 246 ms: 1.10x slower                                                |
| unpickle                 | 8.40 us                                                         | 9.30 us: 1.11x slower                                               |
| sqlglot_normalize        | 173 ms                                                          | 192 ms: 1.11x slower                                                |
| sqlglot_optimize         | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                               |
| sympy_str                | 159 ms                                                          | 178 ms: 1.12x slower                                                |
| xml_etree_process        | 36.4 ms                                                         | 40.7 ms: 1.12x slower                                               |
| json_dumps               | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                               |
| float                    | 49.7 ms                                                         | 56.0 ms: 1.13x slower                                               |
| genshi_xml               | 31.6 ms                                                         | 35.6 ms: 1.13x slower                                               |
| asyncio_tcp              | 471 ms                                                          | 532 ms: 1.13x slower                                                |
| chaos                    | 38.4 ms                                                         | 43.5 ms: 1.13x slower                                               |
| sympy_expand             | 271 ms                                                          | 307 ms: 1.14x slower                                                |
| tornado_http             | 81.8 ms                                                         | 92.9 ms: 1.14x slower                                               |
| comprehensions           | 10.4 us                                                         | 11.8 us: 1.14x slower                                               |
| nqueens                  | 56.7 ms                                                         | 64.6 ms: 1.14x slower                                               |
| django_template          | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                               |
| html5lib                 | 35.0 ms                                                         | 40.1 ms: 1.14x slower                                               |
| pprint_safe_repr         | 474 ms                                                          | 542 ms: 1.14x slower                                                |
| pyflate                  | 279 ms                                                          | 319 ms: 1.15x slower                                                |
| pprint_pformat           | 966 ms                                                          | 1.11 sec: 1.15x slower                                              |
| dulwich_log              | 38.0 ms                                                         | 43.8 ms: 1.15x slower                                               |
| sqlglot_transpile        | 955 us                                                          | 1.10 ms: 1.15x slower                                               |
| regex_compile            | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                               |
| scimark_lu               | 56.6 ms                                                         | 65.8 ms: 1.16x slower                                               |
| tomli_loads              | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                              |
| coverage                 | 42.1 ms                                                         | 49.2 ms: 1.17x slower                                               |
| genshi_text              | 14.4 ms                                                         | 16.8 ms: 1.17x slower                                               |
| hexiom                   | 3.72 ms                                                         | 4.37 ms: 1.17x slower                                               |
| sqlglot_parse            | 748 us                                                          | 880 us: 1.18x slower                                                |
| fannkuch                 | 243 ms                                                          | 288 ms: 1.18x slower                                                |
| logging_silent           | 52.9 ns                                                         | 63.1 ns: 1.19x slower                                               |
| nbody                    | 67.6 ms                                                         | 81.0 ms: 1.20x slower                                               |
| scimark_sor              | 75.3 ms                                                         | 90.4 ms: 1.20x slower                                               |
| scimark_fft              | 171 ms                                                          | 205 ms: 1.20x slower                                                |
| richards_super           | 30.2 ms                                                         | 36.2 ms: 1.20x slower                                               |
| richards                 | 26.7 ms                                                         | 32.2 ms: 1.21x slower                                               |
| deltablue                | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                               |
| raytrace                 | 162 ms                                                          | 198 ms: 1.22x slower                                                |
| pickle_pure_python       | 175 us                                                          | 215 us: 1.22x slower                                                |
| unpickle_pure_python     | 122 us                                                          | 150 us: 1.23x slower                                                |
| scimark_monte_carlo      | 39.1 ms                                                         | 48.4 ms: 1.24x slower                                               |
| json                     | 3.19 ms                                                         | 4.27 ms: 1.34x slower                                               |
| Geometric mean           | (ref)                                                           | 1.05x slower                                                        |

Benchmark hidden because not significant (11): pycparser, async_tree_io, async_tree_memoization_tg, async_tree_memoization, json_loads, async_tree_none_tg, async_tree_cpu_io_mixed, pickle_list, pickle, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf1-amd64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown