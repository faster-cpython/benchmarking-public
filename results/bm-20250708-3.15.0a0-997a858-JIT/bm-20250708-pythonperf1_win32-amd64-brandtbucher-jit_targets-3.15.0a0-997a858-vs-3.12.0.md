# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.497x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 216 ms: 1.30x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                        |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 202 ms: 1.80x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 382 ms: 1.77x faster                                                          |
| async_tree_io              | 693 ms                                                          | 392 ms: 1.77x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.68x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.73x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 55.4 ms: 2.29x faster                                                         |
| float          | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                         |
| pidigits       | 199 ms                                                          | 149 ms: 1.34x faster                                                          |
| Geometric mean | (ref)                                                           | 1.76x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 80.2 ms: 1.61x faster                                                         |
| regex_effbot   | 2.04 ms                                                         | 1.66 ms: 1.22x faster                                                         |
| regex_v8       | 15.0 ms                                                         | 14.4 ms: 1.05x faster                                                         |
| regex_dna      | 127 ms                                                          | 122 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.12 sec: 1.96x faster                                                        |
| unpickle_pure_python | 210 us                                                          | 112 us: 1.87x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 36.2 ms: 1.47x faster                                                         |
| xml_etree_generate   | 72.1 ms                                                         | 51.1 ms: 1.41x faster                                                         |
| json_loads           | 20.4 us                                                         | 14.4 us: 1.41x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 207 us: 1.38x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 88.5 ms: 1.28x faster                                                         |
| json_dumps           | 7.40 ms                                                         | 6.17 ms: 1.20x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.4 ms: 1.19x faster                                                         |
| Geometric mean       | (ref)                                                           | 1.44x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                         |
| python_startup         | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.49 ms: 1.81x faster                                                         |
| django_template | 36.9 ms                                                         | 23.7 ms: 1.56x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.68x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pathlib                    | 91.4 ms                                                         | 30.2 ms: 3.03x faster                                                         |
| mdp                        | 1.91 sec                                                        | 794 ms: 2.41x faster                                                          |
| nbody                      | 127 ms                                                          | 55.4 ms: 2.29x faster                                                         |
| deepcopy_memo              | 38.4 us                                                         | 17.3 us: 2.22x faster                                                         |
| deepcopy                   | 360 us                                                          | 168 us: 2.15x faster                                                          |
| generators                 | 38.5 ms                                                         | 19.6 ms: 1.97x faster                                                         |
| tomli_loads                | 2.20 sec                                                        | 1.12 sec: 1.96x faster                                                        |
| unpickle_pure_python       | 210 us                                                          | 112 us: 1.87x faster                                                          |
| comprehensions             | 19.2 us                                                         | 10.3 us: 1.85x faster                                                         |
| logging_silent             | 101 ns                                                          | 54.9 ns: 1.84x faster                                                         |
| go                         | 137 ms                                                          | 75.3 ms: 1.82x faster                                                         |
| mako                       | 9.96 ms                                                         | 5.49 ms: 1.81x faster                                                         |
| async_tree_none            | 298 ms                                                          | 165 ms: 1.80x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 202 ms: 1.80x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 382 ms: 1.77x faster                                                          |
| float                      | 76.7 ms                                                         | 43.3 ms: 1.77x faster                                                         |
| async_tree_io              | 693 ms                                                          | 392 ms: 1.77x faster                                                          |
| chaos                      | 69.4 ms                                                         | 39.9 ms: 1.74x faster                                                         |
| deepcopy_reduce            | 3.23 us                                                         | 1.86 us: 1.73x faster                                                         |
| scimark_fft                | 271 ms                                                          | 157 ms: 1.72x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 328 ms: 1.72x faster                                                          |
| scimark_sor                | 130 ms                                                          | 76.0 ms: 1.71x faster                                                         |
| async_tree_memoization_tg  | 350 ms                                                          | 206 ms: 1.70x faster                                                          |
| raytrace                   | 308 ms                                                          | 182 ms: 1.69x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 4.04 ms: 1.69x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 166 ms: 1.68x faster                                                          |
| pyflate                    | 424 ms                                                          | 253 ms: 1.67x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.16 ms: 1.66x faster                                                         |
| pprint_pformat             | 1.50 sec                                                        | 908 ms: 1.65x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 333 ms: 1.64x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.37 ms: 1.63x faster                                                         |
| logging_format             | 10.4 us                                                         | 6.42 us: 1.62x faster                                                         |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.1 ms: 1.62x faster                                                         |
| logging_simple             | 9.75 us                                                         | 6.04 us: 1.61x faster                                                         |
| regex_compile              | 129 ms                                                          | 80.2 ms: 1.61x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 454 ms: 1.59x faster                                                          |
| fannkuch                   | 354 ms                                                          | 223 ms: 1.58x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 59.2 ms: 1.58x faster                                                         |
| spectral_norm              | 104 ms                                                          | 66.1 ms: 1.57x faster                                                         |
| django_template            | 36.9 ms                                                         | 23.7 ms: 1.56x faster                                                         |
| richards                   | 41.3 ms                                                         | 27.1 ms: 1.53x faster                                                         |
| crypto_pyaes               | 69.2 ms                                                         | 45.4 ms: 1.52x faster                                                         |
| scimark_lu                 | 93.2 ms                                                         | 61.7 ms: 1.51x faster                                                         |
| richards_super             | 46.5 ms                                                         | 31.0 ms: 1.50x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 36.2 ms: 1.47x faster                                                         |
| dulwich_log                | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 14.7 ms: 1.42x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 51.1 ms: 1.41x faster                                                         |
| json_loads                 | 20.4 us                                                         | 14.4 us: 1.41x faster                                                         |
| json                       | 4.15 ms                                                         | 2.96 ms: 1.40x faster                                                         |
| sympy_str                  | 240 ms                                                          | 173 ms: 1.39x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 88.8 ms: 1.38x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 207 us: 1.38x faster                                                          |
| pycparser                  | 978 ms                                                          | 711 ms: 1.37x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 12.8 ms: 1.37x faster                                                         |
| sympy_expand               | 398 ms                                                          | 297 ms: 1.34x faster                                                          |
| pidigits                   | 199 ms                                                          | 149 ms: 1.34x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.57 us: 1.32x faster                                                         |
| 2to3                       | 280 ms                                                          | 216 ms: 1.30x faster                                                          |
| async_generators           | 313 ms                                                          | 243 ms: 1.29x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 88.5 ms: 1.28x faster                                                         |
| telco                      | 5.51 ms                                                         | 4.38 ms: 1.26x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.66 ms: 1.22x faster                                                         |
| meteor_contest             | 86.9 ms                                                         | 71.2 ms: 1.22x faster                                                         |
| typing_runtime_protocols   | 126 us                                                          | 104 us: 1.22x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.64 sec: 1.21x faster                                                        |
| json_dumps                 | 7.40 ms                                                         | 6.17 ms: 1.20x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.4 ms: 1.19x faster                                                         |
| regex_v8                   | 15.0 ms                                                         | 14.4 ms: 1.05x faster                                                         |
| regex_dna                  | 127 ms                                                          | 122 ms: 1.04x faster                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.6 ms: 1.03x slower                                                         |
| coverage                   | 48.4 ms                                                         | 49.8 ms: 1.03x slower                                                         |
| python_startup             | 22.4 ms                                                         | 25.7 ms: 1.15x slower                                                         |
| gc_traversal               | 1.44 ms                                                         | 2.14 ms: 1.49x slower                                                         |
| create_gc_cycles           | 652 us                                                          | 1.34 ms: 2.05x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.50x faster                                                                  |
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.497x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.51x
- 95% likely to have a speedup of 1.49x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown