# Results vs. base

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5287d32
- commit date: 2024-06-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| docutils       | 2.93 sec                                                              | 2.96 sec: 1.01x slower                                                      |
| html5lib       | 66.6 ms                                                               | 68.8 ms: 1.03x slower                                                       |
| tornado_http   | 96.7 ms                                                               | 98.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 80.4 ms: 1.04x faster                                                       |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                        |
| float          | 72.3 ms                                                               | 73.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                | 139 ms: 1.01x slower                                                        |
| regex_v8       | 24.5 ms                                                               | 25.9 ms: 1.06x slower                                                       |
| regex_effbot   | 3.65 ms                                                               | 4.00 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 149 ms                                                                | 148 ms: 1.01x faster                                                        |
| xml_etree_iterparse | 101 ms                                                                | 101 ms: 1.00x faster                                                        |
| pickle_dict         | 35.7 us                                                               | 35.7 us: 1.00x faster                                                       |
| xml_etree_generate  | 82.0 ms                                                               | 82.3 ms: 1.00x slower                                                       |
| unpickle            | 14.9 us                                                               | 15.1 us: 1.01x slower                                                       |
| tomli_loads         | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| json_loads          | 28.7 us                                                               | 29.0 us: 1.01x slower                                                       |
| pickle_pure_python  | 298 us                                                                | 303 us: 1.02x slower                                                        |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (6): pickle, json_dumps, xml_etree_process, pickle_list, unpickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.62 ms                                                               | 7.64 ms: 1.00x slower                                                       |
| python_startup         | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 37.0 ms                                                               | 36.6 ms: 1.01x faster                                                       |
| mako            | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5287d32 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody                   | 84.0 ms                                                               | 80.4 ms: 1.04x faster                                                       |
| pyflate                 | 452 ms                                                                | 439 ms: 1.03x faster                                                        |
| gc_traversal            | 4.04 ms                                                               | 3.94 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult | 4.49 ms                                                               | 4.39 ms: 1.02x faster                                                       |
| spectral_norm           | 102 ms                                                                | 100 ms: 1.02x faster                                                        |
| coroutines              | 22.9 ms                                                               | 22.5 ms: 1.02x faster                                                       |
| pprint_pformat          | 1.47 sec                                                              | 1.44 sec: 1.02x faster                                                      |
| logging_simple          | 5.69 us                                                               | 5.62 us: 1.01x faster                                                       |
| pprint_safe_repr        | 720 ms                                                                | 711 ms: 1.01x faster                                                        |
| scimark_fft             | 319 ms                                                                | 315 ms: 1.01x faster                                                        |
| django_template         | 37.0 ms                                                               | 36.6 ms: 1.01x faster                                                       |
| scimark_lu              | 126 ms                                                                | 125 ms: 1.01x faster                                                        |
| xml_etree_parse         | 149 ms                                                                | 148 ms: 1.01x faster                                                        |
| fannkuch                | 356 ms                                                                | 354 ms: 1.01x faster                                                        |
| telco                   | 8.10 ms                                                               | 8.04 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 101 ms                                                                | 101 ms: 1.00x faster                                                        |
| crypto_pyaes            | 67.7 ms                                                               | 67.5 ms: 1.00x faster                                                       |
| pickle_dict             | 35.7 us                                                               | 35.7 us: 1.00x faster                                                       |
| python_startup_no_site  | 7.62 ms                                                               | 7.64 ms: 1.00x slower                                                       |
| xml_etree_generate      | 82.0 ms                                                               | 82.3 ms: 1.00x slower                                                       |
| richards_super          | 47.6 ms                                                               | 47.8 ms: 1.00x slower                                                       |
| pidigits                | 188 ms                                                                | 189 ms: 1.00x slower                                                        |
| python_startup          | 11.2 ms                                                               | 11.2 ms: 1.00x slower                                                       |
| sympy_integrate         | 22.5 ms                                                               | 22.6 ms: 1.00x slower                                                       |
| asyncio_tcp_ssl         | 1.85 sec                                                              | 1.86 sec: 1.01x slower                                                      |
| sqlglot_transpile       | 1.64 ms                                                               | 1.65 ms: 1.01x slower                                                       |
| mdp                     | 2.63 sec                                                              | 2.65 sec: 1.01x slower                                                      |
| coverage                | 92.9 ms                                                               | 93.6 ms: 1.01x slower                                                       |
| regex_compile           | 138 ms                                                                | 139 ms: 1.01x slower                                                        |
| sympy_str               | 302 ms                                                                | 304 ms: 1.01x slower                                                        |
| logging_silent          | 107 ns                                                                | 108 ns: 1.01x slower                                                        |
| async_generators        | 465 ms                                                                | 468 ms: 1.01x slower                                                        |
| thrift                  | 810 us                                                                | 818 us: 1.01x slower                                                        |
| mako                    | 10.0 ms                                                               | 10.1 ms: 1.01x slower                                                       |
| hexiom                  | 6.61 ms                                                               | 6.67 ms: 1.01x slower                                                       |
| go                      | 146 ms                                                                | 148 ms: 1.01x slower                                                        |
| 2to3                    | 277 ms                                                                | 280 ms: 1.01x slower                                                        |
| unpickle                | 14.9 us                                                               | 15.1 us: 1.01x slower                                                       |
| bench_thread_pool       | 873 us                                                                | 883 us: 1.01x slower                                                        |
| sqlglot_parse           | 1.30 ms                                                               | 1.32 ms: 1.01x slower                                                       |
| tomli_loads             | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                      |
| json_loads              | 28.7 us                                                               | 29.0 us: 1.01x slower                                                       |
| docutils                | 2.93 sec                                                              | 2.96 sec: 1.01x slower                                                      |
| asyncio_tcp             | 515 ms                                                                | 522 ms: 1.01x slower                                                        |
| sympy_sum               | 171 ms                                                                | 174 ms: 1.01x slower                                                        |
| dulwich_log             | 68.5 ms                                                               | 69.5 ms: 1.01x slower                                                       |
| richards                | 41.1 ms                                                               | 41.7 ms: 1.02x slower                                                       |
| pickle_pure_python      | 298 us                                                                | 303 us: 1.02x slower                                                        |
| float                   | 72.3 ms                                                               | 73.6 ms: 1.02x slower                                                       |
| tornado_http            | 96.7 ms                                                               | 98.7 ms: 1.02x slower                                                       |
| html5lib                | 66.6 ms                                                               | 68.8 ms: 1.03x slower                                                       |
| scimark_sor             | 129 ms                                                                | 134 ms: 1.04x slower                                                        |
| pycparser               | 1.15 sec                                                              | 1.22 sec: 1.06x slower                                                      |
| regex_v8                | 24.5 ms                                                               | 25.9 ms: 1.06x slower                                                       |
| regex_effbot            | 3.65 ms                                                               | 4.00 ms: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                |

Benchmark hidden because not significant (41): chaos, nqueens, deepcopy, genshi_xml, logging_format, sqlite_synth, pickle, json_dumps, comprehensions, generators, xml_etree_process, sqlglot_optimize, regex_dna, pathlib, create_gc_cycles, asyncio_websockets, meteor_contest, pickle_list, async_tree_io_tg, bench_mp_pool, sympy_expand, unpickle_pure_python, dask, scimark_monte_carlo, deltablue, async_tree_cpu_io_mixed, unpickle_list, deepcopy_reduce, json, sqlglot_normalize, typing_runtime_protocols, async_tree_none, raytrace, genshi_text, deepcopy_memo, pylint, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x