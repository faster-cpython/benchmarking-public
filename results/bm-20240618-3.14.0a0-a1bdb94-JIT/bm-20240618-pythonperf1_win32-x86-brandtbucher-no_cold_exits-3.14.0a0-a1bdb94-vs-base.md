# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                         | 249 ms: 1.01x faster                                                          |
| docutils       | 1.92 sec                                                                       | 1.92 sec: 1.00x faster                                                        |
| html5lib       | 47.7 ms                                                                        | 48.9 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 270 ms                                                                         | 263 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 218 ms                                                                         | 213 ms: 1.02x faster                                                          |
| async_tree_memoization     | 295 ms                                                                         | 289 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                         | 460 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 495 ms                                                                         | 488 ms: 1.01x faster                                                          |
| async_tree_none            | 242 ms                                                                         | 238 ms: 1.01x faster                                                          |
| Geometric mean             | (ref)                                                                          | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 53.4 ms                                                                        | 52.5 ms: 1.02x faster                                                         |
| pidigits       | 197 ms                                                                         | 197 ms: 1.00x faster                                                          |
| float          | 41.9 ms                                                                        | 43.0 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 95.8 ms                                                                        | 94.7 ms: 1.01x faster                                                         |
| regex_v8       | 15.8 ms                                                                        | 16.0 ms: 1.01x slower                                                         |
| regex_effbot   | 1.98 ms                                                                        | 2.07 ms: 1.04x slower                                                         |
| regex_dna      | 117 ms                                                                         | 132 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                                          | 1.04x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list        | 3.86 us                                                                        | 3.60 us: 1.07x faster                                                         |
| unpickle           | 10.3 us                                                                        | 10.1 us: 1.02x faster                                                         |
| json_loads         | 20.8 us                                                                        | 20.5 us: 1.01x faster                                                         |
| xml_etree_parse    | 103 ms                                                                         | 102 ms: 1.01x faster                                                          |
| json_dumps         | 6.96 ms                                                                        | 7.01 ms: 1.01x slower                                                         |
| xml_etree_generate | 57.5 ms                                                                        | 58.3 ms: 1.01x slower                                                         |
| tomli_loads        | 1.46 sec                                                                       | 1.48 sec: 1.01x slower                                                        |
| pickle             | 8.18 us                                                                        | 8.35 us: 1.02x slower                                                         |
| unpickle_list      | 2.76 us                                                                        | 2.89 us: 1.05x slower                                                         |
| Geometric mean     | (ref)                                                                          | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): pickle_dict, unpickle_pure_python, xml_etree_process, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 20.4 ms                                                                        | 18.6 ms: 1.10x faster                                                         |
| python_startup         | 24.7 ms                                                                        | 22.8 ms: 1.08x faster                                                         |
| Geometric mean         | (ref)                                                                          | 1.09x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 53.1 ms                                                                        | 51.7 ms: 1.03x faster                                                         |
| genshi_text     | 21.5 ms                                                                        | 21.1 ms: 1.02x faster                                                         |
| django_template | 33.4 ms                                                                        | 32.9 ms: 1.02x faster                                                         |
| mako            | 5.43 ms                                                                        | 5.50 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                          | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240618-pythonperf1_win32-x86-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site     | 20.4 ms                                                                        | 18.6 ms: 1.10x faster                                                         |
| python_startup             | 24.7 ms                                                                        | 22.8 ms: 1.08x faster                                                         |
| pickle_list                | 3.86 us                                                                        | 3.60 us: 1.07x faster                                                         |
| richards                   | 34.4 ms                                                                        | 32.6 ms: 1.05x faster                                                         |
| raytrace                   | 236 ms                                                                         | 227 ms: 1.04x faster                                                          |
| typing_runtime_protocols   | 148 us                                                                         | 142 us: 1.04x faster                                                          |
| pprint_safe_repr           | 572 ms                                                                         | 553 ms: 1.03x faster                                                          |
| richards_super             | 39.0 ms                                                                        | 37.8 ms: 1.03x faster                                                         |
| go                         | 114 ms                                                                         | 111 ms: 1.03x faster                                                          |
| async_tree_memoization_tg  | 270 ms                                                                         | 263 ms: 1.03x faster                                                          |
| genshi_xml                 | 53.1 ms                                                                        | 51.7 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.17 sec                                                                       | 1.14 sec: 1.03x faster                                                        |
| logging_silent             | 58.9 ns                                                                        | 57.4 ns: 1.03x faster                                                         |
| async_tree_none_tg         | 218 ms                                                                         | 213 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 2.45 ms                                                                        | 2.40 ms: 1.02x faster                                                         |
| unpickle                   | 10.3 us                                                                        | 10.1 us: 1.02x faster                                                         |
| async_tree_memoization     | 295 ms                                                                         | 289 ms: 1.02x faster                                                          |
| genshi_text                | 21.5 ms                                                                        | 21.1 ms: 1.02x faster                                                         |
| chaos                      | 54.1 ms                                                                        | 53.1 ms: 1.02x faster                                                         |
| deepcopy                   | 238 us                                                                         | 234 us: 1.02x faster                                                          |
| bench_mp_pool              | 74.8 ms                                                                        | 73.5 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 468 ms                                                                         | 460 ms: 1.02x faster                                                          |
| nbody                      | 53.4 ms                                                                        | 52.5 ms: 1.02x faster                                                         |
| sympy_expand               | 387 ms                                                                         | 381 ms: 1.02x faster                                                          |
| django_template            | 33.4 ms                                                                        | 32.9 ms: 1.02x faster                                                         |
| hexiom                     | 4.62 ms                                                                        | 4.55 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 495 ms                                                                         | 488 ms: 1.01x faster                                                          |
| async_tree_none            | 242 ms                                                                         | 238 ms: 1.01x faster                                                          |
| scimark_monte_carlo        | 40.2 ms                                                                        | 39.7 ms: 1.01x faster                                                         |
| json_loads                 | 20.8 us                                                                        | 20.5 us: 1.01x faster                                                         |
| json                       | 4.19 ms                                                                        | 4.14 ms: 1.01x faster                                                         |
| regex_compile              | 95.8 ms                                                                        | 94.7 ms: 1.01x faster                                                         |
| scimark_sor                | 97.3 ms                                                                        | 96.2 ms: 1.01x faster                                                         |
| sympy_sum                  | 109 ms                                                                         | 108 ms: 1.01x faster                                                          |
| 2to3                       | 251 ms                                                                         | 249 ms: 1.01x faster                                                          |
| sympy_str                  | 217 ms                                                                         | 214 ms: 1.01x faster                                                          |
| coverage                   | 51.4 ms                                                                        | 50.9 ms: 1.01x faster                                                         |
| fannkuch                   | 218 ms                                                                         | 215 ms: 1.01x faster                                                          |
| xml_etree_parse            | 103 ms                                                                         | 102 ms: 1.01x faster                                                          |
| logging_format             | 8.27 us                                                                        | 8.21 us: 1.01x faster                                                         |
| mdp                        | 1.69 sec                                                                       | 1.67 sec: 1.01x faster                                                        |
| deltablue                  | 2.76 ms                                                                        | 2.74 ms: 1.01x faster                                                         |
| pathlib                    | 83.3 ms                                                                        | 82.8 ms: 1.01x faster                                                         |
| scimark_lu                 | 75.2 ms                                                                        | 74.8 ms: 1.00x faster                                                         |
| sympy_integrate            | 15.9 ms                                                                        | 15.8 ms: 1.00x faster                                                         |
| docutils                   | 1.92 sec                                                                       | 1.92 sec: 1.00x faster                                                        |
| pidigits                   | 197 ms                                                                         | 197 ms: 1.00x faster                                                          |
| meteor_contest             | 72.4 ms                                                                        | 72.6 ms: 1.00x slower                                                         |
| sqlglot_optimize           | 43.1 ms                                                                        | 43.2 ms: 1.00x slower                                                         |
| thrift                     | 761 us                                                                         | 764 us: 1.00x slower                                                          |
| json_dumps                 | 6.96 ms                                                                        | 7.01 ms: 1.01x slower                                                         |
| crypto_pyaes               | 47.8 ms                                                                        | 48.1 ms: 1.01x slower                                                         |
| nqueens                    | 71.1 ms                                                                        | 71.9 ms: 1.01x slower                                                         |
| mako                       | 5.43 ms                                                                        | 5.50 ms: 1.01x slower                                                         |
| async_generators           | 298 ms                                                                         | 302 ms: 1.01x slower                                                          |
| regex_v8                   | 15.8 ms                                                                        | 16.0 ms: 1.01x slower                                                         |
| sqlglot_normalize          | 232 ms                                                                         | 236 ms: 1.01x slower                                                          |
| xml_etree_generate         | 57.5 ms                                                                        | 58.3 ms: 1.01x slower                                                         |
| tomli_loads                | 1.46 sec                                                                       | 1.48 sec: 1.01x slower                                                        |
| telco                      | 5.54 ms                                                                        | 5.64 ms: 1.02x slower                                                         |
| pickle                     | 8.18 us                                                                        | 8.35 us: 1.02x slower                                                         |
| pyflate                    | 277 ms                                                                         | 283 ms: 1.02x slower                                                          |
| html5lib                   | 47.7 ms                                                                        | 48.9 ms: 1.02x slower                                                         |
| sqlglot_parse              | 916 us                                                                         | 939 us: 1.03x slower                                                          |
| sqlglot_transpile          | 1.17 ms                                                                        | 1.20 ms: 1.03x slower                                                         |
| float                      | 41.9 ms                                                                        | 43.0 ms: 1.03x slower                                                         |
| scimark_fft                | 164 ms                                                                         | 169 ms: 1.03x slower                                                          |
| spectral_norm              | 47.3 ms                                                                        | 49.3 ms: 1.04x slower                                                         |
| regex_effbot               | 1.98 ms                                                                        | 2.07 ms: 1.04x slower                                                         |
| unpickle_list              | 2.76 us                                                                        | 2.89 us: 1.05x slower                                                         |
| regex_dna                  | 117 ms                                                                         | 132 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                                  |

Benchmark hidden because not significant (22): async_tree_io, pycparser, pickle_dict, tornado_http, generators, deepcopy_memo, unpickle_pure_python, logging_simple, comprehensions, sqlite_synth, coroutines, gc_traversal, pylint, asyncio_tcp_ssl, xml_etree_process, deepcopy_reduce, pickle_pure_python, xml_etree_iterparse, create_gc_cycles, async_tree_io_tg, bench_thread_pool, asyncio_tcp

# HPT report

- Reliability score: 99.60% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown