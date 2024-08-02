# Results vs. base

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 212 ms                                                          | 208 ms: 1.02x faster                                                        |
| chameleon      | 4.75 ms                                                         | 4.71 ms: 1.01x faster                                                       |
| docutils       | 1.64 sec                                                        | 1.61 sec: 1.02x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.2 ms: 1.01x slower                                                       |
| tornado_http   | 82.5 ms                                                         | 81.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg | 213 ms                                                          | 204 ms: 1.04x faster                                                        |
| Geometric mean     | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.1 ms                                                         | 66.2 ms: 1.01x faster                                                       |
| pidigits       | 147 ms                                                          | 150 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                         | 76.9 ms: 1.02x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| regex_dna      | 118 ms                                                          | 118 ms: 1.00x slower                                                        |
| regex_v8       | 14.3 ms                                                         | 15.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 2.77 us                                                         | 2.62 us: 1.06x faster                                                       |
| unpickle_pure_python | 127 us                                                          | 120 us: 1.05x faster                                                        |
| pickle_list          | 3.02 us                                                         | 2.94 us: 1.03x faster                                                       |
| xml_etree_process    | 36.8 ms                                                         | 35.9 ms: 1.03x faster                                                       |
| pickle_pure_python   | 177 us                                                          | 173 us: 1.02x faster                                                        |
| tomli_loads          | 1.37 sec                                                        | 1.35 sec: 1.02x faster                                                      |
| xml_etree_generate   | 53.7 ms                                                         | 52.9 ms: 1.02x faster                                                       |
| xml_etree_parse      | 90.0 ms                                                         | 91.3 ms: 1.01x slower                                                       |
| json_loads           | 13.7 us                                                         | 14.0 us: 1.02x slower                                                       |
| pickle_dict          | 18.4 us                                                         | 19.4 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (4): json_dumps, xml_etree_iterparse, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.4 ms                                                         | 20.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                         | 14.5 ms: 1.02x faster                                                       |
| django_template | 21.5 ms                                                         | 21.1 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo            | 23.1 us                                                         | 21.7 us: 1.06x faster                                                       |
| scimark_lu               | 56.8 ms                                                         | 53.7 ms: 1.06x faster                                                       |
| unpickle_list            | 2.77 us                                                         | 2.62 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult  | 2.53 ms                                                         | 2.39 ms: 1.06x faster                                                       |
| unpickle_pure_python     | 127 us                                                          | 120 us: 1.05x faster                                                        |
| crypto_pyaes             | 46.9 ms                                                         | 44.9 ms: 1.04x faster                                                       |
| coverage                 | 45.3 ms                                                         | 43.5 ms: 1.04x faster                                                       |
| async_tree_none_tg       | 213 ms                                                          | 204 ms: 1.04x faster                                                        |
| scimark_sor              | 75.9 ms                                                         | 73.1 ms: 1.04x faster                                                       |
| scimark_monte_carlo      | 40.5 ms                                                         | 39.1 ms: 1.04x faster                                                       |
| hexiom                   | 3.76 ms                                                         | 3.64 ms: 1.03x faster                                                       |
| richards                 | 26.6 ms                                                         | 25.8 ms: 1.03x faster                                                       |
| typing_runtime_protocols | 103 us                                                          | 100 us: 1.03x faster                                                        |
| telco                    | 4.72 ms                                                         | 4.59 ms: 1.03x faster                                                       |
| sympy_str                | 162 ms                                                          | 158 ms: 1.03x faster                                                        |
| pickle_list              | 3.02 us                                                         | 2.94 us: 1.03x faster                                                       |
| sympy_integrate          | 12.5 ms                                                         | 12.1 ms: 1.03x faster                                                       |
| spectral_norm            | 61.9 ms                                                         | 60.1 ms: 1.03x faster                                                       |
| pprint_safe_repr         | 481 ms                                                          | 467 ms: 1.03x faster                                                        |
| sympy_expand             | 275 ms                                                          | 267 ms: 1.03x faster                                                        |
| xml_etree_process        | 36.8 ms                                                         | 35.9 ms: 1.03x faster                                                       |
| pprint_pformat           | 982 ms                                                          | 959 ms: 1.02x faster                                                        |
| mypy2                    | 427 ms                                                          | 417 ms: 1.02x faster                                                        |
| fannkuch                 | 244 ms                                                          | 238 ms: 1.02x faster                                                        |
| pickle_pure_python       | 177 us                                                          | 173 us: 1.02x faster                                                        |
| deepcopy                 | 223 us                                                          | 218 us: 1.02x faster                                                        |
| 2to3                     | 212 ms                                                          | 208 ms: 1.02x faster                                                        |
| richards_super           | 29.9 ms                                                         | 29.3 ms: 1.02x faster                                                       |
| regex_compile            | 78.5 ms                                                         | 76.9 ms: 1.02x faster                                                       |
| thrift                   | 8.23 ms                                                         | 8.07 ms: 1.02x faster                                                       |
| genshi_text              | 14.7 ms                                                         | 14.5 ms: 1.02x faster                                                       |
| sympy_sum                | 85.2 ms                                                         | 83.8 ms: 1.02x faster                                                       |
| django_template          | 21.5 ms                                                         | 21.1 ms: 1.02x faster                                                       |
| docutils                 | 1.64 sec                                                        | 1.61 sec: 1.02x faster                                                      |
| logging_format           | 6.22 us                                                         | 6.12 us: 1.02x faster                                                       |
| tomli_loads              | 1.37 sec                                                        | 1.35 sec: 1.02x faster                                                      |
| xml_etree_generate       | 53.7 ms                                                         | 52.9 ms: 1.02x faster                                                       |
| comprehensions           | 10.2 us                                                         | 10.1 us: 1.02x faster                                                       |
| aiohttp                  | 908 us                                                          | 894 us: 1.02x faster                                                        |
| pyflate                  | 280 ms                                                          | 276 ms: 1.01x faster                                                        |
| nbody                    | 67.1 ms                                                         | 66.2 ms: 1.01x faster                                                       |
| scimark_fft              | 175 ms                                                          | 172 ms: 1.01x faster                                                        |
| dulwich_log              | 39.6 ms                                                         | 39.1 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 172 ms                                                          | 170 ms: 1.01x faster                                                        |
| nqueens                  | 56.2 ms                                                         | 55.5 ms: 1.01x faster                                                       |
| logging_simple           | 5.80 us                                                         | 5.73 us: 1.01x faster                                                       |
| tornado_http             | 82.5 ms                                                         | 81.6 ms: 1.01x faster                                                       |
| pathlib                  | 80.1 ms                                                         | 79.3 ms: 1.01x faster                                                       |
| chameleon                | 4.75 ms                                                         | 4.71 ms: 1.01x faster                                                       |
| go                       | 84.3 ms                                                         | 83.5 ms: 1.01x faster                                                       |
| sqlite_synth             | 1.62 us                                                         | 1.61 us: 1.01x faster                                                       |
| sqlglot_transpile        | 962 us                                                          | 954 us: 1.01x faster                                                        |
| python_startup           | 20.4 ms                                                         | 20.2 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 32.9 ms                                                         | 32.6 ms: 1.01x faster                                                       |
| sqlglot_parse            | 754 us                                                          | 749 us: 1.01x faster                                                        |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| meteor_contest           | 71.3 ms                                                         | 71.0 ms: 1.00x faster                                                       |
| regex_dna                | 118 ms                                                          | 118 ms: 1.00x slower                                                        |
| coroutines               | 12.6 ms                                                         | 12.7 ms: 1.01x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 35.2 ms: 1.01x slower                                                       |
| async_generators         | 225 ms                                                          | 226 ms: 1.01x slower                                                        |
| create_gc_cycles         | 893 us                                                          | 903 us: 1.01x slower                                                        |
| bench_mp_pool            | 65.3 ms                                                         | 66.2 ms: 1.01x slower                                                       |
| xml_etree_parse          | 90.0 ms                                                         | 91.3 ms: 1.01x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.33 sec: 1.02x slower                                                      |
| json_loads               | 13.7 us                                                         | 14.0 us: 1.02x slower                                                       |
| logging_silent           | 51.7 ns                                                         | 52.8 ns: 1.02x slower                                                       |
| pidigits                 | 147 ms                                                          | 150 ms: 1.02x slower                                                        |
| generators               | 18.6 ms                                                         | 19.3 ms: 1.04x slower                                                       |
| raytrace                 | 154 ms                                                          | 161 ms: 1.05x slower                                                        |
| pickle_dict              | 18.4 us                                                         | 19.4 us: 1.05x slower                                                       |
| json                     | 2.93 ms                                                         | 3.13 ms: 1.07x slower                                                       |
| regex_v8                 | 14.3 ms                                                         | 15.5 ms: 1.08x slower                                                       |
| asyncio_tcp              | 482 ms                                                          | 566 ms: 1.18x slower                                                        |
| Geometric mean           | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (24): async_tree_memoization_tg, pylint, genshi_xml, async_tree_none, python_startup_no_site, float, json_dumps, deepcopy_reduce, async_tree_memoization, deltablue, chaos, xml_etree_iterparse, mako, async_tree_cpu_io_mixed_tg, pickle, unpickle, flaskblogging, gc_traversal, async_tree_io_tg, async_tree_io, async_tree_cpu_io_mixed, bench_thread_pool, asyncio_tcp_ssl, pycparser
Ignored benchmarks (1) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf1-amd64-python-v3.13.0b1-3.13.0b1-2268289.json: dask

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown