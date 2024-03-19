# Results vs. base

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: windows-amd64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.00x faster
- HPT reliability: 70.80%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| chameleon      | 4.76 ms                                                                     | 4.70 ms: 1.01x faster                                                             |
| docutils       | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                            |
| html5lib       | 37.0 ms                                                                     | 35.8 ms: 1.03x faster                                                             |
| tornado_http   | 85.0 ms                                                                     | 83.7 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 446 ms                                                                      | 454 ms: 1.02x slower                                                              |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                                      |

Benchmark hidden because not significant (7): async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                      | 150 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                                     | 15.5 ms: 1.11x faster                                                             |
| regex_dna      | 126 ms                                                                      | 114 ms: 1.11x faster                                                              |
| regex_effbot   | 1.61 ms                                                                     | 1.56 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                                       | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle               | 7.55 us                                                                     | 7.28 us: 1.04x faster                                                             |
| pickle_dict          | 17.9 us                                                                     | 17.6 us: 1.02x faster                                                             |
| pickle_list          | 2.77 us                                                                     | 2.73 us: 1.02x faster                                                             |
| json_loads           | 13.8 us                                                                     | 13.7 us: 1.01x faster                                                             |
| unpickle             | 8.64 us                                                                     | 8.70 us: 1.01x slower                                                             |
| tomli_loads          | 1.18 sec                                                                    | 1.19 sec: 1.01x slower                                                            |
| unpickle_pure_python | 127 us                                                                      | 128 us: 1.01x slower                                                              |
| xml_etree_generate   | 53.2 ms                                                                     | 54.1 ms: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (6): unpickle_list, xml_etree_iterparse, xml_etree_parse, pickle_pure_python, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 24.7 ms                                                                     | 23.4 ms: 1.05x faster                                                             |
| python_startup_no_site | 22.5 ms                                                                     | 21.4 ms: 1.05x faster                                                             |
| Geometric mean         | (ref)                                                                       | 1.05x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 21.5 ms                                                                     | 21.9 ms: 1.02x slower                                                             |
| genshi_text     | 15.3 ms                                                                     | 16.1 ms: 1.05x slower                                                             |
| genshi_xml      | 34.9 ms                                                                     | 37.1 ms: 1.06x slower                                                             |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                                      |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 | bm-20240318-pythonperf1-amd64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8                 | 17.3 ms                                                                     | 15.5 ms: 1.11x faster                                                             |
| regex_dna                | 126 ms                                                                      | 114 ms: 1.11x faster                                                              |
| json                     | 3.36 ms                                                                     | 3.06 ms: 1.10x faster                                                             |
| scimark_sparse_mat_mult  | 2.39 ms                                                                     | 2.24 ms: 1.07x faster                                                             |
| python_startup           | 24.7 ms                                                                     | 23.4 ms: 1.05x faster                                                             |
| python_startup_no_site   | 22.5 ms                                                                     | 21.4 ms: 1.05x faster                                                             |
| unpack_sequence          | 48.6 ns                                                                     | 46.6 ns: 1.04x faster                                                             |
| deepcopy_memo            | 22.8 us                                                                     | 21.8 us: 1.04x faster                                                             |
| pickle                   | 7.55 us                                                                     | 7.28 us: 1.04x faster                                                             |
| html5lib                 | 37.0 ms                                                                     | 35.8 ms: 1.03x faster                                                             |
| meteor_contest           | 75.0 ms                                                                     | 72.6 ms: 1.03x faster                                                             |
| regex_effbot             | 1.61 ms                                                                     | 1.56 ms: 1.03x faster                                                             |
| sympy_sum                | 88.5 ms                                                                     | 86.3 ms: 1.03x faster                                                             |
| coverage                 | 47.1 ms                                                                     | 46.1 ms: 1.02x faster                                                             |
| scimark_sor              | 84.4 ms                                                                     | 82.7 ms: 1.02x faster                                                             |
| raytrace                 | 182 ms                                                                      | 178 ms: 1.02x faster                                                              |
| pickle_dict              | 17.9 us                                                                     | 17.6 us: 1.02x faster                                                             |
| fannkuch                 | 217 ms                                                                      | 213 ms: 1.02x faster                                                              |
| tornado_http             | 85.0 ms                                                                     | 83.7 ms: 1.02x faster                                                             |
| pickle_list              | 2.77 us                                                                     | 2.73 us: 1.02x faster                                                             |
| bench_mp_pool            | 70.3 ms                                                                     | 69.3 ms: 1.01x faster                                                             |
| logging_simple           | 5.87 us                                                                     | 5.79 us: 1.01x faster                                                             |
| typing_runtime_protocols | 71.1 us                                                                     | 70.3 us: 1.01x faster                                                             |
| chameleon                | 4.76 ms                                                                     | 4.70 ms: 1.01x faster                                                             |
| richards_super           | 31.6 ms                                                                     | 31.2 ms: 1.01x faster                                                             |
| docutils                 | 1.60 sec                                                                    | 1.58 sec: 1.01x faster                                                            |
| scimark_fft              | 172 ms                                                                      | 170 ms: 1.01x faster                                                              |
| coroutines               | 13.3 ms                                                                     | 13.1 ms: 1.01x faster                                                             |
| scimark_monte_carlo      | 41.9 ms                                                                     | 41.5 ms: 1.01x faster                                                             |
| richards                 | 28.2 ms                                                                     | 27.9 ms: 1.01x faster                                                             |
| sympy_integrate          | 13.1 ms                                                                     | 13.0 ms: 1.01x faster                                                             |
| spectral_norm            | 51.0 ms                                                                     | 50.7 ms: 1.01x faster                                                             |
| json_loads               | 13.8 us                                                                     | 13.7 us: 1.01x faster                                                             |
| sqlite_synth             | 1.58 us                                                                     | 1.57 us: 1.00x faster                                                             |
| pidigits                 | 150 ms                                                                      | 150 ms: 1.00x slower                                                              |
| nqueens                  | 60.3 ms                                                                     | 60.6 ms: 1.00x slower                                                             |
| sqlglot_normalize        | 175 ms                                                                      | 176 ms: 1.00x slower                                                              |
| pathlib                  | 76.6 ms                                                                     | 77.1 ms: 1.01x slower                                                             |
| logging_format           | 6.24 us                                                                     | 6.28 us: 1.01x slower                                                             |
| sqlglot_parse            | 772 us                                                                      | 777 us: 1.01x slower                                                              |
| unpickle                 | 8.64 us                                                                     | 8.70 us: 1.01x slower                                                             |
| sympy_str                | 164 ms                                                                      | 165 ms: 1.01x slower                                                              |
| go                       | 96.1 ms                                                                     | 96.8 ms: 1.01x slower                                                             |
| sqlglot_transpile        | 991 us                                                                      | 999 us: 1.01x slower                                                              |
| sqlglot_optimize         | 34.3 ms                                                                     | 34.5 ms: 1.01x slower                                                             |
| tomli_loads              | 1.18 sec                                                                    | 1.19 sec: 1.01x slower                                                            |
| async_generators         | 238 ms                                                                      | 240 ms: 1.01x slower                                                              |
| aiohttp                  | 889 us                                                                      | 898 us: 1.01x slower                                                              |
| hexiom                   | 4.32 ms                                                                     | 4.36 ms: 1.01x slower                                                             |
| unpickle_pure_python     | 127 us                                                                      | 128 us: 1.01x slower                                                              |
| deepcopy                 | 219 us                                                                      | 222 us: 1.01x slower                                                              |
| sympy_expand             | 281 ms                                                                      | 285 ms: 1.01x slower                                                              |
| telco                    | 4.57 ms                                                                     | 4.63 ms: 1.01x slower                                                             |
| pprint_pformat           | 954 ms                                                                      | 969 ms: 1.02x slower                                                              |
| generators               | 19.9 ms                                                                     | 20.2 ms: 1.02x slower                                                             |
| mdp                      | 1.44 sec                                                                    | 1.46 sec: 1.02x slower                                                            |
| xml_etree_generate       | 53.2 ms                                                                     | 54.1 ms: 1.02x slower                                                             |
| django_template          | 21.5 ms                                                                     | 21.9 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed  | 446 ms                                                                      | 454 ms: 1.02x slower                                                              |
| pprint_safe_repr         | 466 ms                                                                      | 475 ms: 1.02x slower                                                              |
| asyncio_tcp              | 470 ms                                                                      | 484 ms: 1.03x slower                                                              |
| dulwich_log              | 39.7 ms                                                                     | 41.0 ms: 1.03x slower                                                             |
| crypto_pyaes             | 43.3 ms                                                                     | 45.3 ms: 1.05x slower                                                             |
| genshi_text              | 15.3 ms                                                                     | 16.1 ms: 1.05x slower                                                             |
| genshi_xml               | 34.9 ms                                                                     | 37.1 ms: 1.06x slower                                                             |
| scimark_lu               | 70.7 ms                                                                     | 78.2 ms: 1.11x slower                                                             |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                      |

Benchmark hidden because not significant (32): bench_thread_pool, pycparser, mako, comprehensions, unpickle_list, thrift, xml_etree_iterparse, nbody, xml_etree_parse, pickle_pure_python, 2to3, xml_etree_process, mypy2, pyflate, regex_compile, chaos, create_gc_cycles, logging_silent, deepcopy_reduce, deltablue, async_tree_io, gc_traversal, async_tree_io_tg, json_dumps, pylint, float, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, asyncio_tcp_ssl


# HPT report

- Reliability score: 70.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown