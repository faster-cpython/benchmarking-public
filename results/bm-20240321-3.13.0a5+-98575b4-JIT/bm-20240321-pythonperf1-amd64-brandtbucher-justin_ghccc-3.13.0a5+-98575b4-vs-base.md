# Results vs. base

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-amd64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.00x faster
- HPT reliability: 91.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| chameleon      | 4.67 ms                                                                     | 4.73 ms: 1.01x slower                                                     |
| docutils       | 2.43 sec                                                                    | 2.45 sec: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                              |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io              | 7.30 sec                                                                    | 7.14 sec: 1.02x faster                                                    |
| async_tree_io_tg           | 7.85 sec                                                                    | 7.69 sec: 1.02x faster                                                    |
| async_tree_none            | 1.81 sec                                                                    | 1.78 sec: 1.02x faster                                                    |
| async_tree_none_tg         | 1.99 sec                                                                    | 1.96 sec: 1.02x faster                                                    |
| async_tree_memoization     | 2.32 sec                                                                    | 2.29 sec: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 2.46 sec                                                                    | 2.43 sec: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 2.25 sec                                                                    | 2.23 sec: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 58.4 ms                                                                     | 54.9 ms: 1.06x faster                                                     |
| float          | 81.6 ms                                                                     | 80.3 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.57 ms                                                                     | 1.57 ms: 1.00x slower                                                     |
| regex_compile  | 82.8 ms                                                                     | 83.6 ms: 1.01x slower                                                     |
| regex_v8       | 14.6 ms                                                                     | 14.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_dict          | 19.2 us                                                                     | 18.2 us: 1.05x faster                                                     |
| pickle               | 7.42 us                                                                     | 7.13 us: 1.04x faster                                                     |
| pickle_list          | 3.00 us                                                                     | 2.90 us: 1.04x faster                                                     |
| unpickle             | 8.59 us                                                                     | 8.38 us: 1.03x faster                                                     |
| unpickle_pure_python | 128 us                                                                      | 126 us: 1.02x faster                                                      |
| xml_etree_iterparse  | 94.3 ms                                                                     | 93.1 ms: 1.01x faster                                                     |
| json_dumps           | 5.59 ms                                                                     | 5.56 ms: 1.01x faster                                                     |
| json_loads           | 13.6 us                                                                     | 13.8 us: 1.01x slower                                                     |
| xml_etree_process    | 40.6 ms                                                                     | 41.2 ms: 1.01x slower                                                     |
| pickle_pure_python   | 177 us                                                                      | 180 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (4): tomli_loads, unpickle_list, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 21.6 ms                                                                     | 20.9 ms: 1.04x faster                                                     |
| python_startup         | 23.9 ms                                                                     | 23.4 ms: 1.02x faster                                                     |
| Geometric mean         | (ref)                                                                       | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 5.58 ms                                                                     | 5.23 ms: 1.07x faster                                                     |
| genshi_xml      | 37.3 ms                                                                     | 38.0 ms: 1.02x slower                                                     |
| django_template | 21.9 ms                                                                     | 22.5 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240320-pythonperf1-amd64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| spectral_norm              | 51.3 ms                                                                     | 45.5 ms: 1.13x faster                                                     |
| fannkuch                   | 228 ms                                                                      | 205 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 41.2 ms                                                                     | 38.0 ms: 1.08x faster                                                     |
| scimark_fft                | 168 ms                                                                      | 157 ms: 1.07x faster                                                      |
| mako                       | 5.58 ms                                                                     | 5.23 ms: 1.07x faster                                                     |
| nbody                      | 58.4 ms                                                                     | 54.9 ms: 1.06x faster                                                     |
| pickle_dict                | 19.2 us                                                                     | 18.2 us: 1.05x faster                                                     |
| pyflate                    | 280 ms                                                                      | 266 ms: 1.05x faster                                                      |
| pprint_pformat             | 983 ms                                                                      | 944 ms: 1.04x faster                                                      |
| pickle                     | 7.42 us                                                                     | 7.13 us: 1.04x faster                                                     |
| pprint_safe_repr           | 479 ms                                                                      | 462 ms: 1.04x faster                                                      |
| pickle_list                | 3.00 us                                                                     | 2.90 us: 1.04x faster                                                     |
| python_startup_no_site     | 21.6 ms                                                                     | 20.9 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 2.23 ms                                                                     | 2.16 ms: 1.03x faster                                                     |
| crypto_pyaes               | 43.3 ms                                                                     | 42.0 ms: 1.03x faster                                                     |
| unpickle                   | 8.59 us                                                                     | 8.38 us: 1.03x faster                                                     |
| python_startup             | 23.9 ms                                                                     | 23.4 ms: 1.02x faster                                                     |
| async_tree_io              | 7.30 sec                                                                    | 7.14 sec: 1.02x faster                                                    |
| unpickle_pure_python       | 128 us                                                                      | 126 us: 1.02x faster                                                      |
| async_tree_io_tg           | 7.85 sec                                                                    | 7.69 sec: 1.02x faster                                                    |
| chaos                      | 39.9 ms                                                                     | 39.2 ms: 1.02x faster                                                     |
| sqlite_synth               | 1.58 us                                                                     | 1.56 us: 1.02x faster                                                     |
| async_tree_none            | 1.81 sec                                                                    | 1.78 sec: 1.02x faster                                                    |
| meteor_contest             | 74.5 ms                                                                     | 73.3 ms: 1.02x faster                                                     |
| hexiom                     | 4.35 ms                                                                     | 4.28 ms: 1.02x faster                                                     |
| float                      | 81.6 ms                                                                     | 80.3 ms: 1.02x faster                                                     |
| async_tree_none_tg         | 1.99 sec                                                                    | 1.96 sec: 1.02x faster                                                    |
| coverage                   | 47.2 ms                                                                     | 46.6 ms: 1.01x faster                                                     |
| async_tree_memoization     | 2.32 sec                                                                    | 2.29 sec: 1.01x faster                                                    |
| mdp                        | 1.47 sec                                                                    | 1.45 sec: 1.01x faster                                                    |
| xml_etree_iterparse        | 94.3 ms                                                                     | 93.1 ms: 1.01x faster                                                     |
| dulwich_log                | 41.5 ms                                                                     | 41.0 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 2.46 sec                                                                    | 2.43 sec: 1.01x faster                                                    |
| async_tree_cpu_io_mixed    | 2.25 sec                                                                    | 2.23 sec: 1.01x faster                                                    |
| aiohttp                    | 941 us                                                                      | 932 us: 1.01x faster                                                      |
| logging_simple             | 5.88 us                                                                     | 5.84 us: 1.01x faster                                                     |
| json_dumps                 | 5.59 ms                                                                     | 5.56 ms: 1.01x faster                                                     |
| logging_format             | 6.37 us                                                                     | 6.34 us: 1.01x faster                                                     |
| scimark_lu                 | 69.5 ms                                                                     | 69.2 ms: 1.00x faster                                                     |
| nqueens                    | 60.3 ms                                                                     | 60.6 ms: 1.00x slower                                                     |
| regex_effbot               | 1.57 ms                                                                     | 1.57 ms: 1.00x slower                                                     |
| sqlglot_optimize           | 36.2 ms                                                                     | 36.4 ms: 1.01x slower                                                     |
| docutils                   | 2.43 sec                                                                    | 2.45 sec: 1.01x slower                                                    |
| sqlglot_parse              | 840 us                                                                      | 846 us: 1.01x slower                                                      |
| deltablue                  | 2.14 ms                                                                     | 2.16 ms: 1.01x slower                                                     |
| thrift                     | 8.90 ms                                                                     | 8.98 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 71.2 us                                                                     | 71.9 us: 1.01x slower                                                     |
| sympy_integrate            | 13.0 ms                                                                     | 13.1 ms: 1.01x slower                                                     |
| regex_compile              | 82.8 ms                                                                     | 83.6 ms: 1.01x slower                                                     |
| sympy_str                  | 165 ms                                                                      | 167 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.06 ms                                                                     | 1.07 ms: 1.01x slower                                                     |
| json_loads                 | 13.6 us                                                                     | 13.8 us: 1.01x slower                                                     |
| coroutines                 | 13.3 ms                                                                     | 13.5 ms: 1.01x slower                                                     |
| regex_v8                   | 14.6 ms                                                                     | 14.8 ms: 1.01x slower                                                     |
| xml_etree_process          | 40.6 ms                                                                     | 41.2 ms: 1.01x slower                                                     |
| chameleon                  | 4.67 ms                                                                     | 4.73 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 181 ms                                                                      | 184 ms: 1.02x slower                                                      |
| logging_silent             | 54.8 ns                                                                     | 55.7 ns: 1.02x slower                                                     |
| sympy_sum                  | 86.7 ms                                                                     | 88.1 ms: 1.02x slower                                                     |
| pickle_pure_python         | 177 us                                                                      | 180 us: 1.02x slower                                                      |
| raytrace                   | 181 ms                                                                      | 184 ms: 1.02x slower                                                      |
| genshi_xml                 | 37.3 ms                                                                     | 38.0 ms: 1.02x slower                                                     |
| deepcopy_reduce            | 1.94 us                                                                     | 1.98 us: 1.02x slower                                                     |
| sympy_expand               | 285 ms                                                                      | 291 ms: 1.02x slower                                                      |
| scimark_sor                | 81.4 ms                                                                     | 83.2 ms: 1.02x slower                                                     |
| go                         | 96.6 ms                                                                     | 99.1 ms: 1.03x slower                                                     |
| django_template            | 21.9 ms                                                                     | 22.5 ms: 1.03x slower                                                     |
| async_generators           | 281 ms                                                                      | 291 ms: 1.03x slower                                                      |
| deepcopy                   | 221 us                                                                      | 228 us: 1.03x slower                                                      |
| json                       | 2.86 ms                                                                     | 2.99 ms: 1.05x slower                                                     |
| deepcopy_memo              | 21.2 us                                                                     | 22.5 us: 1.06x slower                                                     |
| richards                   | 27.2 ms                                                                     | 29.1 ms: 1.07x slower                                                     |
| richards_super             | 30.5 ms                                                                     | 32.5 ms: 1.07x slower                                                     |
| unpack_sequence            | 46.7 ns                                                                     | 66.6 ns: 1.42x slower                                                     |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (24): asyncio_tcp, create_gc_cycles, async_tree_memoization_tg, comprehensions, tornado_http, bench_thread_pool, bench_mp_pool, 2to3, genshi_text, pidigits, regex_dna, pathlib, gc_traversal, pycparser, telco, generators, asyncio_tcp_ssl, tomli_loads, unpickle_list, xml_etree_generate, pylint, xml_etree_parse, html5lib, mypy2


# HPT report

- Reliability score: 91.18% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown