# Results vs. 3.12.0

- fork: brandtbucher
- ref: jump_backoff
- machine: windows-x86
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.054x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 267 ms: 1.05x faster                                                          |
| docutils       | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                        |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                          |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 298 ms: 1.22x faster                                                          |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 561 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                                         |
| nbody          | 127 ms                                                          | 100 ms: 1.26x faster                                                          |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                         |
| regex_compile  | 129 ms                                                          | 117 ms: 1.11x faster                                                          |
| regex_dna      | 127 ms                                                          | 116 ms: 1.10x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                        |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 208 us: 1.01x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 112 ms: 1.01x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                         |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 73.3 ms: 1.02x slower                                                         |
| pickle_pure_python   | 286 us                                                          | 302 us: 1.06x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 8.79 ms: 1.19x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                         |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.37 ms: 1.35x faster                                                         |
| django_template | 36.9 ms                                                         | 36.0 ms: 1.02x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.1 us: 1.66x faster                                                         |
| float                      | 76.7 ms                                                         | 55.6 ms: 1.38x faster                                                         |
| mako                       | 9.96 ms                                                         | 7.37 ms: 1.35x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 264 ms: 1.33x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 213 ms: 1.30x faster                                                          |
| deepcopy                   | 360 us                                                          | 277 us: 1.30x faster                                                          |
| scimark_sor                | 130 ms                                                          | 101 ms: 1.28x faster                                                          |
| nbody                      | 127 ms                                                          | 100 ms: 1.26x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.7 ms: 1.25x faster                                                         |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                          |
| spectral_norm              | 104 ms                                                          | 84.3 ms: 1.23x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 75.9 ms: 1.23x faster                                                         |
| async_tree_memoization     | 364 ms                                                          | 298 ms: 1.22x faster                                                          |
| async_tree_none            | 298 ms                                                          | 244 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.19 ms: 1.21x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 561 ms: 1.21x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.85 sec: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                         |
| logging_silent             | 101 ns                                                          | 86.0 ns: 1.17x faster                                                         |
| logging_simple             | 9.75 us                                                         | 8.39 us: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                          |
| logging_format             | 10.4 us                                                         | 9.04 us: 1.15x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.82 us: 1.14x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.0 ms: 1.14x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.83 ms: 1.12x faster                                                         |
| scimark_fft                | 271 ms                                                          | 244 ms: 1.11x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 3.23 ms: 1.11x faster                                                         |
| regex_compile              | 129 ms                                                          | 117 ms: 1.11x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 82.6 ms: 1.11x faster                                                         |
| regex_dna                  | 127 ms                                                          | 116 ms: 1.10x faster                                                          |
| go                         | 137 ms                                                          | 125 ms: 1.10x faster                                                          |
| generators                 | 38.5 ms                                                         | 35.6 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.1 ms: 1.07x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                         |
| chaos                      | 69.4 ms                                                         | 65.3 ms: 1.06x faster                                                         |
| pycparser                  | 978 ms                                                          | 922 ms: 1.06x faster                                                          |
| comprehensions             | 19.2 us                                                         | 18.2 us: 1.06x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.18 ms: 1.05x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 117 ms: 1.05x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 65.9 ms: 1.05x faster                                                         |
| 2to3                       | 280 ms                                                          | 267 ms: 1.05x faster                                                          |
| pyflate                    | 424 ms                                                          | 404 ms: 1.05x faster                                                          |
| fannkuch                   | 354 ms                                                          | 338 ms: 1.05x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.47 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.07 us                                                         | 2.01 us: 1.03x faster                                                         |
| django_template            | 36.9 ms                                                         | 36.0 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 208 us: 1.01x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 112 ms: 1.01x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 17.6 ms: 1.01x slower                                                         |
| xml_etree_process          | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.50 sec                                                        | 1.52 sec: 1.01x slower                                                        |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                         |
| sympy_str                  | 240 ms                                                          | 243 ms: 1.02x slower                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 73.3 ms: 1.02x slower                                                         |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                          |
| mdp                        | 1.91 sec                                                        | 1.95 sec: 1.02x slower                                                        |
| pprint_safe_repr           | 721 ms                                                          | 740 ms: 1.03x slower                                                          |
| meteor_contest             | 86.9 ms                                                         | 89.8 ms: 1.03x slower                                                         |
| async_generators           | 313 ms                                                          | 324 ms: 1.03x slower                                                          |
| richards                   | 41.3 ms                                                         | 43.1 ms: 1.04x slower                                                         |
| nqueens                    | 93.7 ms                                                         | 97.8 ms: 1.04x slower                                                         |
| docutils                   | 1.98 sec                                                        | 2.08 sec: 1.05x slower                                                        |
| hexiom                     | 6.82 ms                                                         | 7.21 ms: 1.06x slower                                                         |
| pickle_pure_python         | 286 us                                                          | 302 us: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.39 ms: 1.06x slower                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 51.5 ms: 1.06x slower                                                         |
| richards_super             | 46.5 ms                                                         | 49.4 ms: 1.06x slower                                                         |
| sympy_expand               | 398 ms                                                          | 424 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.7 ms: 1.07x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                         |
| sqlglot_normalize          | 100 ms                                                          | 110 ms: 1.10x slower                                                          |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 86.3 ms: 1.14x slower                                                         |
| json_dumps                 | 7.40 ms                                                         | 8.79 ms: 1.19x slower                                                         |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                         |
| telco                      | 5.51 ms                                                         | 7.18 ms: 1.30x slower                                                         |
| typing_runtime_protocols   | 126 us                                                          | 168 us: 1.33x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 1.16 ms: 1.78x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (2): raytrace, python_startup_no_site
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf1_win32-x86-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.054x faster
# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown