# Results vs. base

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: windows-amd64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x faster
- HPT reliability: 92.02%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chameleon      | 4.64 ms                                                                     | 4.74 ms: 1.02x slower                                                           |
| html5lib       | 35.8 ms                                                                     | 36.4 ms: 1.02x slower                                                           |
| tornado_http   | 81.8 ms                                                                     | 79.8 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 49.9 ms                                                                     | 48.7 ms: 1.02x faster                                                           |
| nbody          | 66.1 ms                                                                     | 67.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 17.6 ms                                                                     | 15.2 ms: 1.15x faster                                                           |
| regex_dna      | 124 ms                                                                      | 118 ms: 1.05x faster                                                            |
| regex_effbot   | 1.61 ms                                                                     | 1.59 ms: 1.02x faster                                                           |
| regex_compile  | 77.6 ms                                                                     | 78.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle             | 8.58 us                                                                     | 8.17 us: 1.05x faster                                                           |
| json_loads           | 14.5 us                                                                     | 14.0 us: 1.03x faster                                                           |
| xml_etree_parse      | 91.0 ms                                                                     | 88.2 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 62.1 ms                                                                     | 60.8 ms: 1.02x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                                     | 52.9 ms: 1.02x faster                                                           |
| xml_etree_process    | 36.9 ms                                                                     | 36.2 ms: 1.02x faster                                                           |
| pickle_pure_python   | 176 us                                                                      | 174 us: 1.01x faster                                                            |
| unpickle_pure_python | 125 us                                                                      | 124 us: 1.01x faster                                                            |
| json_dumps           | 5.61 ms                                                                     | 5.57 ms: 1.01x faster                                                           |
| unpickle_list        | 2.75 us                                                                     | 2.74 us: 1.01x faster                                                           |
| pickle_dict          | 18.4 us                                                                     | 18.9 us: 1.03x slower                                                           |
| pickle               | 7.22 us                                                                     | 7.47 us: 1.03x slower                                                           |
| pickle_list          | 3.05 us                                                                     | 3.28 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 21.5 ms                                                                     | 21.7 ms: 1.01x slower                                                           |
| genshi_text     | 14.5 ms                                                                     | 15.0 ms: 1.04x slower                                                           |
| genshi_xml      | 31.5 ms                                                                     | 34.0 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                                       | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark            | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-pythonperf1-amd64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8             | 17.6 ms                                                                     | 15.2 ms: 1.15x faster                                                           |
| json                 | 3.38 ms                                                                     | 3.14 ms: 1.08x faster                                                           |
| async_generators     | 244 ms                                                                      | 228 ms: 1.07x faster                                                            |
| spectral_norm        | 62.8 ms                                                                     | 59.3 ms: 1.06x faster                                                           |
| unpickle             | 8.58 us                                                                     | 8.17 us: 1.05x faster                                                           |
| regex_dna            | 124 ms                                                                      | 118 ms: 1.05x faster                                                            |
| scimark_lu           | 56.8 ms                                                                     | 54.4 ms: 1.04x faster                                                           |
| crypto_pyaes         | 48.6 ms                                                                     | 46.9 ms: 1.03x faster                                                           |
| json_loads           | 14.5 us                                                                     | 14.0 us: 1.03x faster                                                           |
| xml_etree_parse      | 91.0 ms                                                                     | 88.2 ms: 1.03x faster                                                           |
| tornado_http         | 81.8 ms                                                                     | 79.8 ms: 1.02x faster                                                           |
| dask                 | 316 ms                                                                      | 309 ms: 1.02x faster                                                            |
| float                | 49.9 ms                                                                     | 48.7 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 62.1 ms                                                                     | 60.8 ms: 1.02x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                                     | 52.9 ms: 1.02x faster                                                           |
| scimark_monte_carlo  | 40.4 ms                                                                     | 39.7 ms: 1.02x faster                                                           |
| deepcopy_memo        | 22.3 us                                                                     | 21.9 us: 1.02x faster                                                           |
| xml_etree_process    | 36.9 ms                                                                     | 36.2 ms: 1.02x faster                                                           |
| meteor_contest       | 72.1 ms                                                                     | 70.9 ms: 1.02x faster                                                           |
| nqueens              | 57.8 ms                                                                     | 56.8 ms: 1.02x faster                                                           |
| regex_effbot         | 1.61 ms                                                                     | 1.59 ms: 1.02x faster                                                           |
| pickle_pure_python   | 176 us                                                                      | 174 us: 1.01x faster                                                            |
| unpickle_pure_python | 125 us                                                                      | 124 us: 1.01x faster                                                            |
| json_dumps           | 5.61 ms                                                                     | 5.57 ms: 1.01x faster                                                           |
| mypy2                | 423 ms                                                                      | 420 ms: 1.01x faster                                                            |
| unpickle_list        | 2.75 us                                                                     | 2.74 us: 1.01x faster                                                           |
| pathlib              | 79.1 ms                                                                     | 78.7 ms: 1.01x faster                                                           |
| pyflate              | 283 ms                                                                      | 281 ms: 1.00x faster                                                            |
| hexiom               | 3.79 ms                                                                     | 3.81 ms: 1.00x slower                                                           |
| sympy_expand         | 271 ms                                                                      | 273 ms: 1.01x slower                                                            |
| regex_compile        | 77.6 ms                                                                     | 78.1 ms: 1.01x slower                                                           |
| fannkuch             | 243 ms                                                                      | 245 ms: 1.01x slower                                                            |
| sqlite_synth         | 1.62 us                                                                     | 1.63 us: 1.01x slower                                                           |
| django_template      | 21.5 ms                                                                     | 21.7 ms: 1.01x slower                                                           |
| go                   | 84.0 ms                                                                     | 84.5 ms: 1.01x slower                                                           |
| sqlglot_normalize    | 171 ms                                                                      | 172 ms: 1.01x slower                                                            |
| logging_silent       | 50.3 ns                                                                     | 50.7 ns: 1.01x slower                                                           |
| logging_format       | 6.11 us                                                                     | 6.17 us: 1.01x slower                                                           |
| pprint_safe_repr     | 473 ms                                                                      | 478 ms: 1.01x slower                                                            |
| deepcopy_reduce      | 1.95 us                                                                     | 1.97 us: 1.01x slower                                                           |
| deepcopy             | 214 us                                                                      | 217 us: 1.01x slower                                                            |
| pprint_pformat       | 964 ms                                                                      | 975 ms: 1.01x slower                                                            |
| deltablue            | 1.86 ms                                                                     | 1.89 ms: 1.01x slower                                                           |
| richards_super       | 29.3 ms                                                                     | 29.7 ms: 1.01x slower                                                           |
| nbody                | 66.1 ms                                                                     | 67.0 ms: 1.01x slower                                                           |
| html5lib             | 35.8 ms                                                                     | 36.4 ms: 1.02x slower                                                           |
| logging_simple       | 5.67 us                                                                     | 5.76 us: 1.02x slower                                                           |
| generators           | 18.6 ms                                                                     | 19.0 ms: 1.02x slower                                                           |
| richards             | 25.9 ms                                                                     | 26.4 ms: 1.02x slower                                                           |
| scimark_sor          | 74.7 ms                                                                     | 76.0 ms: 1.02x slower                                                           |
| chameleon            | 4.64 ms                                                                     | 4.74 ms: 1.02x slower                                                           |
| pickle_dict          | 18.4 us                                                                     | 18.9 us: 1.03x slower                                                           |
| coverage             | 43.2 ms                                                                     | 44.6 ms: 1.03x slower                                                           |
| pickle               | 7.22 us                                                                     | 7.47 us: 1.03x slower                                                           |
| genshi_text          | 14.5 ms                                                                     | 15.0 ms: 1.04x slower                                                           |
| pickle_list          | 3.05 us                                                                     | 3.28 us: 1.08x slower                                                           |
| genshi_xml           | 31.5 ms                                                                     | 34.0 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                    |

Benchmark hidden because not significant (42): asyncio_tcp_ssl, bench_thread_pool, async_tree_memoization_tg, asyncio_tcp, async_tree_cpu_io_mixed, create_gc_cycles, pycparser, async_tree_cpu_io_mixed_tg, comprehensions, pylint, async_tree_io_tg, async_tree_memoization, async_tree_none, scimark_sparse_mat_mult, typing_runtime_protocols, async_tree_none_tg, bench_mp_pool, aiohttp, gc_traversal, scimark_fft, coroutines, chaos, python_startup, sympy_integrate, raytrace, mdp, pidigits, sympy_str, python_startup_no_site, sqlglot_transpile, flaskblogging, sqlglot_parse, docutils, tomli_loads, sqlglot_optimize, 2to3, thrift, telco, dulwich_log, sympy_sum, async_tree_io, mako

# HPT report

- Reliability score: 92.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown