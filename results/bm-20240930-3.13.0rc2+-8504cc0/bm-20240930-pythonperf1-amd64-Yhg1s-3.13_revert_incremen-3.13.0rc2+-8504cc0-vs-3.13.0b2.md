# Results vs. 3.13.0b2

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-amd64
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 215 ms: 1.04x slower                                                        |
| docutils       | 1.63 sec                                                        | 1.56 sec: 1.04x faster                                                      |
| html5lib       | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                       |
| tornado_http   | 81.8 ms                                                         | 92.5 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 505 ms: 1.20x faster                                                        |
| async_tree_io              | 588 ms                                                          | 516 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 377 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 370 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 258 ms                                                          | 286 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| nbody          | 67.6 ms                                                         | 68.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 117 ms: 1.01x faster                                                        |
| regex_compile  | 78.0 ms                                                         | 81.6 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 62.3 ms                                                         | 61.4 ms: 1.01x faster                                                       |
| unpickle_list        | 2.62 us                                                         | 2.64 us: 1.01x slower                                                       |
| xml_etree_process    | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                       |
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                       |
| xml_etree_parse      | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                       |
| json_dumps           | 5.61 ms                                                         | 5.71 ms: 1.02x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 180 us: 1.02x slower                                                        |
| tomli_loads          | 1.35 sec                                                        | 1.40 sec: 1.03x slower                                                      |
| unpickle_pure_python | 122 us                                                          | 127 us: 1.04x slower                                                        |
| unpickle             | 8.40 us                                                         | 8.86 us: 1.05x slower                                                       |
| pickle_list          | 2.90 us                                                         | 3.08 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                       |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.23 ms: 1.02x faster                                                       |
| django_template | 21.7 ms                                                         | 22.2 ms: 1.03x slower                                                       |
| genshi_xml      | 31.6 ms                                                         | 32.9 ms: 1.04x slower                                                       |
| genshi_text     | 14.4 ms                                                         | 15.0 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 505 ms: 1.20x faster                                                        |
| async_tree_io              | 588 ms                                                          | 516 ms: 1.14x faster                                                        |
| create_gc_cycles           | 888 us                                                          | 813 us: 1.09x faster                                                        |
| spectral_norm              | 63.7 ms                                                         | 59.4 ms: 1.07x faster                                                       |
| scimark_lu                 | 56.6 ms                                                         | 54.0 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.40 ms: 1.04x faster                                                       |
| docutils                   | 1.63 sec                                                        | 1.56 sec: 1.04x faster                                                      |
| async_tree_cpu_io_mixed    | 389 ms                                                          | 377 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 370 ms: 1.03x faster                                                        |
| comprehensions             | 10.4 us                                                         | 10.1 us: 1.02x faster                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 44.4 ms: 1.02x faster                                                       |
| mako                       | 6.36 ms                                                         | 6.23 ms: 1.02x faster                                                       |
| async_generators           | 223 ms                                                          | 219 ms: 1.02x faster                                                        |
| logging_format             | 6.22 us                                                         | 6.12 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 61.4 ms: 1.01x faster                                                       |
| regex_dna                  | 119 ms                                                          | 117 ms: 1.01x faster                                                        |
| richards_super             | 30.2 ms                                                         | 29.8 ms: 1.01x faster                                                       |
| logging_simple             | 5.78 us                                                         | 5.72 us: 1.01x faster                                                       |
| pyflate                    | 279 ms                                                          | 277 ms: 1.01x faster                                                        |
| coroutines                 | 12.8 ms                                                         | 12.7 ms: 1.01x faster                                                       |
| deltablue                  | 1.88 ms                                                         | 1.88 ms: 1.00x faster                                                       |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                                        |
| sqlite_synth               | 1.60 us                                                         | 1.60 us: 1.00x slower                                                       |
| chaos                      | 38.4 ms                                                         | 38.5 ms: 1.00x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 53.2 ns: 1.01x slower                                                       |
| richards                   | 26.7 ms                                                         | 26.9 ms: 1.01x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 75.8 ms: 1.01x slower                                                       |
| unpickle_list              | 2.62 us                                                         | 2.64 us: 1.01x slower                                                       |
| fannkuch                   | 243 ms                                                          | 245 ms: 1.01x slower                                                        |
| xml_etree_process          | 36.4 ms                                                         | 36.7 ms: 1.01x slower                                                       |
| pickle_dict                | 18.1 us                                                         | 18.3 us: 1.01x slower                                                       |
| sqlglot_normalize          | 173 ms                                                          | 175 ms: 1.01x slower                                                        |
| generators                 | 19.6 ms                                                         | 19.8 ms: 1.01x slower                                                       |
| xml_etree_generate         | 53.2 ms                                                         | 53.7 ms: 1.01x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                       |
| nbody                      | 67.6 ms                                                         | 68.5 ms: 1.01x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 57.4 ms: 1.01x slower                                                       |
| scimark_fft                | 171 ms                                                          | 173 ms: 1.01x slower                                                        |
| deepcopy_reduce            | 1.99 us                                                         | 2.02 us: 1.01x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 12.4 ms: 1.01x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 92.3 ms: 1.02x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 5.71 ms: 1.02x slower                                                       |
| telco                      | 4.67 ms                                                         | 4.78 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 978 us: 1.02x slower                                                        |
| pickle_pure_python         | 175 us                                                          | 180 us: 1.02x slower                                                        |
| scimark_monte_carlo        | 39.1 ms                                                         | 40.1 ms: 1.03x slower                                                       |
| django_template            | 21.7 ms                                                         | 22.2 ms: 1.03x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 86.6 ms: 1.03x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 769 us: 1.03x slower                                                        |
| mypy2                      | 418 ms                                                          | 430 ms: 1.03x slower                                                        |
| deepcopy_memo              | 22.1 us                                                         | 22.8 us: 1.03x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.40 sec: 1.03x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 33.9 ms: 1.03x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 72.5 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 127 us: 1.04x slower                                                        |
| 2to3                       | 207 ms                                                          | 215 ms: 1.04x slower                                                        |
| deepcopy                   | 220 us                                                          | 228 us: 1.04x slower                                                        |
| mdp                        | 1.31 sec                                                        | 1.36 sec: 1.04x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 32.9 ms: 1.04x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 15.0 ms: 1.04x slower                                                       |
| pprint_safe_repr           | 474 ms                                                          | 494 ms: 1.04x slower                                                        |
| regex_compile              | 78.0 ms                                                         | 81.6 ms: 1.05x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.01 sec: 1.05x slower                                                      |
| aiohttp                    | 889 us                                                          | 933 us: 1.05x slower                                                        |
| sympy_str                  | 159 ms                                                          | 167 ms: 1.05x slower                                                        |
| thrift                     | 8.11 ms                                                         | 8.53 ms: 1.05x slower                                                       |
| unpickle                   | 8.40 us                                                         | 8.86 us: 1.05x slower                                                       |
| pickle_list                | 2.90 us                                                         | 3.08 us: 1.06x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 80.5 ms: 1.06x slower                                                       |
| sympy_expand               | 271 ms                                                          | 288 ms: 1.06x slower                                                        |
| bench_thread_pool          | 768 us                                                          | 816 us: 1.06x slower                                                        |
| bench_mp_pool              | 64.8 ms                                                         | 69.3 ms: 1.07x slower                                                       |
| dulwich_log                | 38.0 ms                                                         | 41.0 ms: 1.08x slower                                                       |
| go                         | 82.1 ms                                                         | 88.7 ms: 1.08x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                       |
| coverage                   | 42.1 ms                                                         | 46.4 ms: 1.10x slower                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 286 ms: 1.11x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 92.5 ms: 1.13x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 40.0 ms: 1.14x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 579 ms: 1.23x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (17): json, async_tree_none_tg, chameleon, hexiom, pickle, flaskblogging, gc_traversal, regex_effbot, typing_runtime_protocols, pycparser, float, raytrace, regex_v8, async_tree_none, async_tree_memoization, pylint, asyncio_tcp_ssl
Ignored benchmarks (1) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown