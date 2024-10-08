# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 224 ms                                                                     | 226 ms: 1.01x slower                                              |
| html5lib       | 40.3 ms                                                                    | 40.9 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 394 ms                                                                     | 385 ms: 1.03x faster                                              |
| coroutines              | 14.1 ms                                                                    | 13.8 ms: 1.02x faster                                             |
| asyncio_tcp_ssl         | 1.38 sec                                                                   | 1.45 sec: 1.05x slower                                            |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                      |

Benchmark hidden because not significant (9): async_tree_none_tg, asyncio_tcp, async_tree_memoization, async_tree_memoization_tg, async_generators, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 56.1 ms                                                                    | 55.3 ms: 1.01x faster                                             |
| pidigits       | 150 ms                                                                     | 151 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                    | 1.59 ms: 1.01x slower                                             |
| regex_compile  | 91.8 ms                                                                    | 93.1 ms: 1.01x slower                                             |
| regex_dna      | 119 ms                                                                     | 121 ms: 1.02x slower                                              |
| regex_v8       | 14.6 ms                                                                    | 15.3 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list          | 3.00 us                                                                    | 2.73 us: 1.10x faster                                             |
| unpickle             | 9.62 us                                                                    | 9.12 us: 1.06x faster                                             |
| pickle_dict          | 18.5 us                                                                    | 17.6 us: 1.05x faster                                             |
| pickle               | 7.23 us                                                                    | 7.10 us: 1.02x faster                                             |
| json_loads           | 14.4 us                                                                    | 14.2 us: 1.02x faster                                             |
| unpickle_list        | 2.83 us                                                                    | 2.78 us: 1.02x faster                                             |
| xml_etree_process    | 41.1 ms                                                                    | 40.9 ms: 1.00x faster                                             |
| xml_etree_parse      | 93.5 ms                                                                    | 94.3 ms: 1.01x slower                                             |
| json_dumps           | 6.19 ms                                                                    | 6.26 ms: 1.01x slower                                             |
| xml_etree_generate   | 57.9 ms                                                                    | 58.6 ms: 1.01x slower                                             |
| unpickle_pure_python | 151 us                                                                     | 153 us: 1.01x slower                                              |
| tomli_loads          | 1.58 sec                                                                   | 1.61 sec: 1.02x slower                                            |
| pickle_pure_python   | 210 us                                                                     | 215 us: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 17.6 ms                                                                    | 17.9 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml     | 36.0 ms                                                                    | 35.6 ms: 1.01x faster                                             |
| genshi_text    | 17.1 ms                                                                    | 16.9 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                      |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list              | 3.00 us                                                                    | 2.73 us: 1.10x faster                                             |
| unpickle                 | 9.62 us                                                                    | 9.12 us: 1.06x faster                                             |
| pickle_dict              | 18.5 us                                                                    | 17.6 us: 1.05x faster                                             |
| async_tree_cpu_io_mixed  | 394 ms                                                                     | 385 ms: 1.03x faster                                              |
| coroutines               | 14.1 ms                                                                    | 13.8 ms: 1.02x faster                                             |
| thrift                   | 523 us                                                                     | 512 us: 1.02x faster                                              |
| typing_runtime_protocols | 113 us                                                                     | 111 us: 1.02x faster                                              |
| pickle                   | 7.23 us                                                                    | 7.10 us: 1.02x faster                                             |
| json_loads               | 14.4 us                                                                    | 14.2 us: 1.02x faster                                             |
| unpickle_list            | 2.83 us                                                                    | 2.78 us: 1.02x faster                                             |
| bench_mp_pool            | 67.6 ms                                                                    | 66.6 ms: 1.01x faster                                             |
| float                    | 56.1 ms                                                                    | 55.3 ms: 1.01x faster                                             |
| genshi_xml               | 36.0 ms                                                                    | 35.6 ms: 1.01x faster                                             |
| genshi_text              | 17.1 ms                                                                    | 16.9 ms: 1.01x faster                                             |
| sympy_expand             | 306 ms                                                                     | 305 ms: 1.01x faster                                              |
| sqlite_synth             | 1.64 us                                                                    | 1.64 us: 1.00x faster                                             |
| xml_etree_process        | 41.1 ms                                                                    | 40.9 ms: 1.00x faster                                             |
| sympy_str                | 177 ms                                                                     | 178 ms: 1.01x slower                                              |
| comprehensions           | 11.9 us                                                                    | 12.0 us: 1.01x slower                                             |
| sympy_sum                | 90.0 ms                                                                    | 90.6 ms: 1.01x slower                                             |
| pidigits                 | 150 ms                                                                     | 151 ms: 1.01x slower                                              |
| scimark_sor              | 89.9 ms                                                                    | 90.7 ms: 1.01x slower                                             |
| 2to3                     | 224 ms                                                                     | 226 ms: 1.01x slower                                              |
| regex_effbot             | 1.57 ms                                                                    | 1.59 ms: 1.01x slower                                             |
| xml_etree_parse          | 93.5 ms                                                                    | 94.3 ms: 1.01x slower                                             |
| deepcopy                 | 189 us                                                                     | 191 us: 1.01x slower                                              |
| json_dumps               | 6.19 ms                                                                    | 6.26 ms: 1.01x slower                                             |
| raytrace                 | 195 ms                                                                     | 197 ms: 1.01x slower                                              |
| sqlglot_transpile        | 1.11 ms                                                                    | 1.12 ms: 1.01x slower                                             |
| sqlglot_parse            | 892 us                                                                     | 902 us: 1.01x slower                                              |
| deepcopy_memo            | 20.4 us                                                                    | 20.6 us: 1.01x slower                                             |
| xml_etree_generate       | 57.9 ms                                                                    | 58.6 ms: 1.01x slower                                             |
| pyflate                  | 320 ms                                                                     | 324 ms: 1.01x slower                                              |
| unpickle_pure_python     | 151 us                                                                     | 153 us: 1.01x slower                                              |
| regex_compile            | 91.8 ms                                                                    | 93.1 ms: 1.01x slower                                             |
| dulwich_log              | 42.8 ms                                                                    | 43.4 ms: 1.02x slower                                             |
| html5lib                 | 40.3 ms                                                                    | 40.9 ms: 1.02x slower                                             |
| regex_dna                | 119 ms                                                                     | 121 ms: 1.02x slower                                              |
| sqlglot_optimize         | 36.2 ms                                                                    | 36.8 ms: 1.02x slower                                             |
| pprint_safe_repr         | 541 ms                                                                     | 551 ms: 1.02x slower                                              |
| deltablue                | 2.28 ms                                                                    | 2.32 ms: 1.02x slower                                             |
| tomli_loads              | 1.58 sec                                                                   | 1.61 sec: 1.02x slower                                            |
| pprint_pformat           | 1.11 sec                                                                   | 1.13 sec: 1.02x slower                                            |
| sqlglot_normalize        | 193 ms                                                                     | 197 ms: 1.02x slower                                              |
| python_startup_no_site   | 17.6 ms                                                                    | 17.9 ms: 1.02x slower                                             |
| pickle_pure_python       | 210 us                                                                     | 215 us: 1.02x slower                                              |
| logging_silent           | 62.2 ns                                                                    | 63.5 ns: 1.02x slower                                             |
| logging_format           | 6.91 us                                                                    | 7.08 us: 1.03x slower                                             |
| richards_super           | 35.9 ms                                                                    | 36.9 ms: 1.03x slower                                             |
| richards                 | 31.9 ms                                                                    | 33.0 ms: 1.03x slower                                             |
| coverage                 | 46.9 ms                                                                    | 48.5 ms: 1.03x slower                                             |
| go                       | 85.8 ms                                                                    | 88.9 ms: 1.04x slower                                             |
| logging_simple           | 6.43 us                                                                    | 6.68 us: 1.04x slower                                             |
| chaos                    | 43.1 ms                                                                    | 44.9 ms: 1.04x slower                                             |
| mdp                      | 1.44 sec                                                                   | 1.51 sec: 1.04x slower                                            |
| telco                    | 4.97 ms                                                                    | 5.20 ms: 1.04x slower                                             |
| regex_v8                 | 14.6 ms                                                                    | 15.3 ms: 1.05x slower                                             |
| nqueens                  | 63.1 ms                                                                    | 65.9 ms: 1.05x slower                                             |
| fannkuch                 | 294 ms                                                                     | 308 ms: 1.05x slower                                              |
| spectral_norm            | 66.4 ms                                                                    | 69.9 ms: 1.05x slower                                             |
| asyncio_tcp_ssl          | 1.38 sec                                                                   | 1.45 sec: 1.05x slower                                            |
| scimark_monte_carlo      | 48.7 ms                                                                    | 51.4 ms: 1.06x slower                                             |
| hexiom                   | 4.37 ms                                                                    | 4.62 ms: 1.06x slower                                             |
| scimark_fft              | 196 ms                                                                     | 212 ms: 1.08x slower                                              |
| scimark_sparse_mat_mult  | 2.69 ms                                                                    | 2.93 ms: 1.09x slower                                             |
| scimark_lu               | 58.4 ms                                                                    | 65.7 ms: 1.12x slower                                             |
| Geometric mean           | (ref)                                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (29): pycparser, json, async_tree_none_tg, asyncio_tcp, generators, mako, async_tree_memoization, tornado_http, bench_thread_pool, django_template, create_gc_cycles, async_tree_memoization_tg, async_generators, gc_traversal, meteor_contest, unpack_sequence, nbody, pylint, async_tree_io, crypto_pyaes, docutils, pathlib, async_tree_io_tg, async_tree_cpu_io_mixed_tg, sympy_integrate, async_tree_none, xml_etree_iterparse, deepcopy_reduce, python_startup

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown