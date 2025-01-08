# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: windows-x86
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.174x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 244 ms: 1.15x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                        |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 409 ms: 1.66x faster                                                          |
| async_tree_io              | 693 ms                                                          | 421 ms: 1.64x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 219 ms: 1.60x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.60x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 235 ms: 1.54x faster                                                          |
| async_tree_none            | 298 ms                                                          | 193 ms: 1.54x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 434 ms: 1.30x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 422 ms: 1.30x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.52x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 84.4 ms: 1.50x faster                                                         |
| float          | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                         |
| pidigits       | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.6 ms: 1.30x faster                                                         |
| regex_effbot   | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                         |
| regex_dna      | 127 ms                                                          | 117 ms: 1.08x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 169 us: 1.25x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.5 ms: 1.19x faster                                                         |
| xml_etree_process    | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 66.2 ms: 1.09x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 268 us: 1.07x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                         |
| json_dumps           | 7.40 ms                                                         | 8.60 ms: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                         |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.55 ms: 1.32x faster                                                         |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.21x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.3 us: 1.72x faster                                                         |
| async_tree_io_tg           | 677 ms                                                          | 409 ms: 1.66x faster                                                          |
| async_tree_io              | 693 ms                                                          | 421 ms: 1.64x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 219 ms: 1.60x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 174 ms: 1.60x faster                                                          |
| deepcopy                   | 360 us                                                          | 233 us: 1.55x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 235 ms: 1.54x faster                                                          |
| generators                 | 38.5 ms                                                         | 25.0 ms: 1.54x faster                                                         |
| async_tree_none            | 298 ms                                                          | 193 ms: 1.54x faster                                                          |
| nbody                      | 127 ms                                                          | 84.4 ms: 1.50x faster                                                         |
| spectral_norm              | 104 ms                                                          | 70.1 ms: 1.48x faster                                                         |
| logging_silent             | 101 ns                                                          | 69.2 ns: 1.46x faster                                                         |
| go                         | 137 ms                                                          | 95.0 ms: 1.45x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.85 ms: 1.41x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 66.5 ms: 1.40x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                                        |
| deltablue                  | 3.58 ms                                                         | 2.57 ms: 1.39x faster                                                         |
| comprehensions             | 19.2 us                                                         | 13.9 us: 1.38x faster                                                         |
| float                      | 76.7 ms                                                         | 56.5 ms: 1.36x faster                                                         |
| scimark_sor                | 130 ms                                                          | 96.5 ms: 1.35x faster                                                         |
| mako                       | 9.96 ms                                                         | 7.55 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 434 ms: 1.30x faster                                                          |
| regex_compile              | 129 ms                                                          | 99.6 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 422 ms: 1.30x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.57 ms: 1.29x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 2.50 us: 1.29x faster                                                         |
| chaos                      | 69.4 ms                                                         | 53.8 ms: 1.29x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 16.4 ms: 1.27x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.4 ms: 1.27x faster                                                         |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.04 ms: 1.27x faster                                                         |
| pyflate                    | 424 ms                                                          | 335 ms: 1.27x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.76 us: 1.26x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 74.8 ms: 1.25x faster                                                         |
| unpickle_pure_python       | 210 us                                                          | 169 us: 1.25x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.42 us: 1.24x faster                                                         |
| raytrace                   | 308 ms                                                          | 250 ms: 1.23x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.23x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.27 ms: 1.21x faster                                                         |
| pycparser                  | 978 ms                                                          | 809 ms: 1.21x faster                                                          |
| scimark_fft                | 271 ms                                                          | 225 ms: 1.20x faster                                                          |
| fannkuch                   | 354 ms                                                          | 294 ms: 1.20x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.5 ms: 1.19x faster                                                         |
| pprint_pformat             | 1.50 sec                                                        | 1.27 sec: 1.18x faster                                                        |
| pprint_safe_repr           | 721 ms                                                          | 617 ms: 1.17x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                         |
| richards                   | 41.3 ms                                                         | 35.6 ms: 1.16x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.15x faster                                                         |
| 2to3                       | 280 ms                                                          | 244 ms: 1.15x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 60.5 ms: 1.14x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 43.4 ms: 1.12x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 47.9 ms: 1.11x faster                                                         |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.80 sec: 1.10x faster                                                        |
| richards_super             | 46.5 ms                                                         | 42.1 ms: 1.10x faster                                                         |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 66.2 ms: 1.09x faster                                                         |
| pathlib                    | 91.4 ms                                                         | 83.9 ms: 1.09x faster                                                         |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.08x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.08x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 81.1 ms: 1.07x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 268 us: 1.07x faster                                                          |
| async_generators           | 313 ms                                                          | 294 ms: 1.06x faster                                                          |
| sympy_expand               | 398 ms                                                          | 377 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                        |
| pidigits                   | 199 ms                                                          | 197 ms: 1.01x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                         |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                         |
| coverage                   | 48.4 ms                                                         | 51.1 ms: 1.05x slower                                                         |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                         |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                          |
| python_startup             | 22.4 ms                                                         | 25.5 ms: 1.14x slower                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 87.2 ms: 1.16x slower                                                         |
| json_dumps                 | 7.40 ms                                                         | 8.60 ms: 1.16x slower                                                         |
| mypy2                      | 584 ms                                                          | 686 ms: 1.17x slower                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.78 ms: 1.24x slower                                                         |
| telco                      | 5.51 ms                                                         | 6.90 ms: 1.25x slower                                                         |
| create_gc_cycles           | 652 us                                                          | 1.05 ms: 1.62x slower                                                         |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.28x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                  |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.174x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown