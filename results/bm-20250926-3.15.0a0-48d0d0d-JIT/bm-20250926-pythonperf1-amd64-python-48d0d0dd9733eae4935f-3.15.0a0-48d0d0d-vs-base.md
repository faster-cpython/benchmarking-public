# Results vs. base

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.029x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                                                                               | 214 ms: 1.01x faster                                                                                                     |
| docutils       | 1.58 sec                                                                                                             | 1.62 sec: 1.02x slower                                                                                                   |
| html5lib       | 37.1 ms                                                                                                              | 38.0 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| coroutines                | 14.7 ms                                                                                                              | 13.9 ms: 1.06x faster                                                                                                    |
| async_tree_io_tg          | 383 ms                                                                                                               | 377 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg        | 166 ms                                                                                                               | 164 ms: 1.01x faster                                                                                                     |
| async_tree_memoization    | 201 ms                                                                                                               | 199 ms: 1.01x faster                                                                                                     |
| async_tree_memoization_tg | 206 ms                                                                                                               | 209 ms: 1.02x slower                                                                                                     |
| asyncio_tcp_ssl           | 1.25 sec                                                                                                             | 1.30 sec: 1.04x slower                                                                                                   |
| async_generators          | 229 ms                                                                                                               | 239 ms: 1.04x slower                                                                                                     |
| asyncio_tcp               | 377 ms                                                                                                               | 418 ms: 1.11x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (5): async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.0 ms                                                                                                              | 55.8 ms: 1.13x faster                                                                                                    |
| float          | 43.7 ms                                                                                                              | 39.8 ms: 1.10x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                                                               | 115 ms: 1.03x faster                                                                                                     |
| regex_v8       | 13.8 ms                                                                                                              | 13.3 ms: 1.03x faster                                                                                                    |
| regex_compile  | 77.9 ms                                                                                                              | 77.3 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.56 ms                                                                                                              | 1.60 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 136 us                                                                                                               | 105 us: 1.29x faster                                                                                                     |
| tomli_loads          | 1.37 sec                                                                                                             | 1.08 sec: 1.27x faster                                                                                                   |
| xml_etree_generate   | 55.9 ms                                                                                                              | 50.0 ms: 1.12x faster                                                                                                    |
| xml_etree_process    | 38.1 ms                                                                                                              | 35.7 ms: 1.07x faster                                                                                                    |
| pickle               | 8.08 us                                                                                                              | 7.65 us: 1.06x faster                                                                                                    |
| pickle_pure_python   | 209 us                                                                                                               | 198 us: 1.06x faster                                                                                                     |
| unpickle_list        | 2.85 us                                                                                                              | 2.73 us: 1.04x faster                                                                                                    |
| pickle_dict          | 19.5 us                                                                                                              | 19.2 us: 1.02x faster                                                                                                    |
| json_loads           | 14.0 us                                                                                                              | 13.8 us: 1.01x faster                                                                                                    |
| json_dumps           | 5.36 ms                                                                                                              | 5.31 ms: 1.01x faster                                                                                                    |
| xml_etree_parse      | 88.5 ms                                                                                                              | 87.6 ms: 1.01x faster                                                                                                    |
| xml_etree_iterparse  | 62.0 ms                                                                                                              | 61.5 ms: 1.01x faster                                                                                                    |
| pickle_list          | 3.21 us                                                                                                              | 3.26 us: 1.02x slower                                                                                                    |
| unpickle             | 8.55 us                                                                                                              | 8.69 us: 1.02x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 24.9 ms                                                                                                              | 25.2 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.41 ms                                                                                                              | 5.34 ms: 1.20x faster                                                                                                    |
| genshi_text    | 15.4 ms                                                                                                              | 15.7 ms: 1.02x slower                                                                                                    |
| genshi_xml     | 34.1 ms                                                                                                              | 34.9 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python      | 136 us                                                                                                               | 105 us: 1.29x faster                                                                                                     |
| scimark_fft               | 170 ms                                                                                                               | 134 ms: 1.27x faster                                                                                                     |
| tomli_loads               | 1.37 sec                                                                                                             | 1.08 sec: 1.27x faster                                                                                                   |
| fannkuch                  | 259 ms                                                                                                               | 207 ms: 1.25x faster                                                                                                     |
| mako                      | 6.41 ms                                                                                                              | 5.34 ms: 1.20x faster                                                                                                    |
| bpe_tokeniser             | 2.95 sec                                                                                                             | 2.54 sec: 1.16x faster                                                                                                   |
| scimark_sparse_mat_mult   | 2.50 ms                                                                                                              | 2.21 ms: 1.13x faster                                                                                                    |
| nbody                     | 63.0 ms                                                                                                              | 55.8 ms: 1.13x faster                                                                                                    |
| xml_etree_generate        | 55.9 ms                                                                                                              | 50.0 ms: 1.12x faster                                                                                                    |
| pprint_safe_repr          | 476 ms                                                                                                               | 433 ms: 1.10x faster                                                                                                     |
| pprint_pformat            | 972 ms                                                                                                               | 886 ms: 1.10x faster                                                                                                     |
| float                     | 43.7 ms                                                                                                              | 39.8 ms: 1.10x faster                                                                                                    |
| pyflate                   | 274 ms                                                                                                               | 250 ms: 1.10x faster                                                                                                     |
| sqlglot_v2_parse          | 812 us                                                                                                               | 755 us: 1.08x faster                                                                                                     |
| xml_etree_process         | 38.1 ms                                                                                                              | 35.7 ms: 1.07x faster                                                                                                    |
| crypto_pyaes              | 47.2 ms                                                                                                              | 44.6 ms: 1.06x faster                                                                                                    |
| coroutines                | 14.7 ms                                                                                                              | 13.9 ms: 1.06x faster                                                                                                    |
| pickle                    | 8.08 us                                                                                                              | 7.65 us: 1.06x faster                                                                                                    |
| pickle_pure_python        | 209 us                                                                                                               | 198 us: 1.06x faster                                                                                                     |
| sqlglot_v2_transpile      | 1.01 ms                                                                                                              | 963 us: 1.05x faster                                                                                                     |
| k_core                    | 1.66 sec                                                                                                             | 1.59 sec: 1.05x faster                                                                                                   |
| comprehensions            | 11.0 us                                                                                                              | 10.5 us: 1.05x faster                                                                                                    |
| unpickle_list             | 2.85 us                                                                                                              | 2.73 us: 1.04x faster                                                                                                    |
| logging_silent            | 56.5 ns                                                                                                              | 54.3 ns: 1.04x faster                                                                                                    |
| telco                     | 4.13 ms                                                                                                              | 3.96 ms: 1.04x faster                                                                                                    |
| nqueens                   | 62.0 ms                                                                                                              | 59.7 ms: 1.04x faster                                                                                                    |
| raytrace                  | 180 ms                                                                                                               | 173 ms: 1.04x faster                                                                                                     |
| unpack_sequence           | 34.4 ns                                                                                                              | 33.2 ns: 1.04x faster                                                                                                    |
| regex_dna                 | 119 ms                                                                                                               | 115 ms: 1.03x faster                                                                                                     |
| regex_v8                  | 13.8 ms                                                                                                              | 13.3 ms: 1.03x faster                                                                                                    |
| json                      | 2.89 ms                                                                                                              | 2.80 ms: 1.03x faster                                                                                                    |
| spectral_norm             | 62.2 ms                                                                                                              | 60.5 ms: 1.03x faster                                                                                                    |
| connected_components      | 324 ms                                                                                                               | 317 ms: 1.02x faster                                                                                                     |
| typing_runtime_protocols  | 104 us                                                                                                               | 102 us: 1.02x faster                                                                                                     |
| shortest_path             | 355 ms                                                                                                               | 348 ms: 1.02x faster                                                                                                     |
| pycparser                 | 694 ms                                                                                                               | 682 ms: 1.02x faster                                                                                                     |
| hexiom                    | 3.99 ms                                                                                                              | 3.92 ms: 1.02x faster                                                                                                    |
| thrift                    | 497 us                                                                                                               | 489 us: 1.02x faster                                                                                                     |
| meteor_contest            | 72.6 ms                                                                                                              | 71.4 ms: 1.02x faster                                                                                                    |
| async_tree_io_tg          | 383 ms                                                                                                               | 377 ms: 1.02x faster                                                                                                     |
| pickle_dict               | 19.5 us                                                                                                              | 19.2 us: 1.02x faster                                                                                                    |
| mdp                       | 796 ms                                                                                                               | 786 ms: 1.01x faster                                                                                                     |
| json_loads                | 14.0 us                                                                                                              | 13.8 us: 1.01x faster                                                                                                    |
| json_dumps                | 5.36 ms                                                                                                              | 5.31 ms: 1.01x faster                                                                                                    |
| async_tree_none_tg        | 166 ms                                                                                                               | 164 ms: 1.01x faster                                                                                                     |
| xml_etree_parse           | 88.5 ms                                                                                                              | 87.6 ms: 1.01x faster                                                                                                    |
| sympy_sum                 | 85.1 ms                                                                                                              | 84.2 ms: 1.01x faster                                                                                                    |
| xml_etree_iterparse       | 62.0 ms                                                                                                              | 61.5 ms: 1.01x faster                                                                                                    |
| regex_compile             | 77.9 ms                                                                                                              | 77.3 ms: 1.01x faster                                                                                                    |
| async_tree_memoization    | 201 ms                                                                                                               | 199 ms: 1.01x faster                                                                                                     |
| 2to3                      | 215 ms                                                                                                               | 214 ms: 1.01x faster                                                                                                     |
| bench_mp_pool             | 89.4 ms                                                                                                              | 88.8 ms: 1.01x faster                                                                                                    |
| generators                | 19.4 ms                                                                                                              | 19.3 ms: 1.00x faster                                                                                                    |
| many_optionals            | 560 us                                                                                                               | 563 us: 1.01x slower                                                                                                     |
| deepcopy                  | 163 us                                                                                                               | 164 us: 1.01x slower                                                                                                     |
| sympy_expand              | 282 ms                                                                                                               | 284 ms: 1.01x slower                                                                                                     |
| python_startup            | 24.9 ms                                                                                                              | 25.2 ms: 1.01x slower                                                                                                    |
| richards                  | 26.5 ms                                                                                                              | 26.8 ms: 1.01x slower                                                                                                    |
| sympy_integrate           | 12.2 ms                                                                                                              | 12.4 ms: 1.02x slower                                                                                                    |
| pickle_list               | 3.21 us                                                                                                              | 3.26 us: 1.02x slower                                                                                                    |
| scimark_monte_carlo       | 40.2 ms                                                                                                              | 40.9 ms: 1.02x slower                                                                                                    |
| unpickle                  | 8.55 us                                                                                                              | 8.69 us: 1.02x slower                                                                                                    |
| async_tree_memoization_tg | 206 ms                                                                                                               | 209 ms: 1.02x slower                                                                                                     |
| go                        | 75.2 ms                                                                                                              | 76.7 ms: 1.02x slower                                                                                                    |
| richards_super            | 30.0 ms                                                                                                              | 30.6 ms: 1.02x slower                                                                                                    |
| docutils                  | 1.58 sec                                                                                                             | 1.62 sec: 1.02x slower                                                                                                   |
| genshi_text               | 15.4 ms                                                                                                              | 15.7 ms: 1.02x slower                                                                                                    |
| html5lib                  | 37.1 ms                                                                                                              | 38.0 ms: 1.02x slower                                                                                                    |
| genshi_xml                | 34.1 ms                                                                                                              | 34.9 ms: 1.03x slower                                                                                                    |
| deltablue                 | 2.13 ms                                                                                                              | 2.19 ms: 1.03x slower                                                                                                    |
| scimark_sor               | 72.9 ms                                                                                                              | 75.0 ms: 1.03x slower                                                                                                    |
| regex_effbot              | 1.56 ms                                                                                                              | 1.60 ms: 1.03x slower                                                                                                    |
| logging_format            | 6.33 us                                                                                                              | 6.57 us: 1.04x slower                                                                                                    |
| logging_simple            | 5.84 us                                                                                                              | 6.09 us: 1.04x slower                                                                                                    |
| asyncio_tcp_ssl           | 1.25 sec                                                                                                             | 1.30 sec: 1.04x slower                                                                                                   |
| async_generators          | 229 ms                                                                                                               | 239 ms: 1.04x slower                                                                                                     |
| deepcopy_memo             | 16.4 us                                                                                                              | 17.2 us: 1.05x slower                                                                                                    |
| asyncio_tcp               | 377 ms                                                                                                               | 418 ms: 1.11x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (24): chaos, async_tree_none, sqlglot_v2_normalize, scimark_lu, django_template, pathlib, dulwich_log, deepcopy_reduce, async_tree_cpu_io_mixed_tg, subparsers, asyncio_websockets, create_gc_cycles, pidigits, async_tree_cpu_io_mixed, sympy_str, coverage, sqlite_synth, async_tree_io, gc_traversal, bench_thread_pool, sqlglot_v2_optimize, python_startup_no_site, sphinx, pylint

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown