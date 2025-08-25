# Results vs. base

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                                                                               | 214 ms: 1.01x faster                                                                                                     |
| docutils       | 1.63 sec                                                                                                             | 1.61 sec: 1.01x faster                                                                                                   |
| html5lib       | 37.7 ms                                                                                                              | 37.3 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg          | 392 ms                                                                                                               | 377 ms: 1.04x faster                                                                                                     |
| async_tree_none           | 173 ms                                                                                                               | 168 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg        | 168 ms                                                                                                               | 164 ms: 1.02x faster                                                                                                     |
| async_tree_memoization    | 201 ms                                                                                                               | 197 ms: 1.02x faster                                                                                                     |
| coroutines                | 14.3 ms                                                                                                              | 14.5 ms: 1.02x slower                                                                                                    |
| async_tree_memoization_tg | 204 ms                                                                                                               | 208 ms: 1.02x slower                                                                                                     |
| async_generators          | 224 ms                                                                                                               | 237 ms: 1.06x slower                                                                                                     |
| Geometric mean            | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (6): asyncio_websockets, async_tree_io, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 62.8 ms                                                                                                              | 60.0 ms: 1.05x faster                                                                                                    |
| float          | 43.5 ms                                                                                                              | 42.9 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                                                               | 116 ms: 1.04x faster                                                                                                     |
| regex_v8       | 13.7 ms                                                                                                              | 13.5 ms: 1.01x faster                                                                                                    |
| regex_compile  | 78.1 ms                                                                                                              | 77.4 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.52 ms                                                                                                              | 1.55 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                                                                               | 104 us: 1.28x faster                                                                                                     |
| tomli_loads          | 1.36 sec                                                                                                             | 1.08 sec: 1.27x faster                                                                                                   |
| xml_etree_generate   | 55.6 ms                                                                                                              | 49.8 ms: 1.12x faster                                                                                                    |
| xml_etree_process    | 38.4 ms                                                                                                              | 34.7 ms: 1.11x faster                                                                                                    |
| pickle               | 8.21 us                                                                                                              | 7.46 us: 1.10x faster                                                                                                    |
| pickle_pure_python   | 209 us                                                                                                               | 197 us: 1.06x faster                                                                                                     |
| unpickle_list        | 2.80 us                                                                                                              | 2.70 us: 1.04x faster                                                                                                    |
| pickle_dict          | 20.0 us                                                                                                              | 19.3 us: 1.03x faster                                                                                                    |
| xml_etree_parse      | 87.6 ms                                                                                                              | 85.5 ms: 1.02x faster                                                                                                    |
| xml_etree_iterparse  | 63.1 ms                                                                                                              | 61.6 ms: 1.02x faster                                                                                                    |
| pickle_list          | 3.35 us                                                                                                              | 3.30 us: 1.02x faster                                                                                                    |
| json_loads           | 14.3 us                                                                                                              | 14.1 us: 1.01x faster                                                                                                    |
| json_dumps           | 5.36 ms                                                                                                              | 5.31 ms: 1.01x faster                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.5 ms                                                                                                              | 25.2 ms: 1.01x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.59 ms                                                                                                              | 5.21 ms: 1.26x faster                                                                                                    |
| django_template | 24.4 ms                                                                                                              | 23.9 ms: 1.02x faster                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | results/bm-20250823-3.15.0a0-6fcac09/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json | results/bm-20250823-3.15.0a0-6fcac09-JIT/bm-20250823-pythonperf1-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python      | 133 us                                                                                                               | 104 us: 1.28x faster                                                                                                     |
| tomli_loads               | 1.36 sec                                                                                                             | 1.08 sec: 1.27x faster                                                                                                   |
| mako                      | 6.59 ms                                                                                                              | 5.21 ms: 1.26x faster                                                                                                    |
| fannkuch                  | 256 ms                                                                                                               | 210 ms: 1.22x faster                                                                                                     |
| bpe_tokeniser             | 2.93 sec                                                                                                             | 2.46 sec: 1.19x faster                                                                                                   |
| scimark_fft               | 176 ms                                                                                                               | 148 ms: 1.19x faster                                                                                                     |
| pprint_safe_repr          | 485 ms                                                                                                               | 414 ms: 1.17x faster                                                                                                     |
| pprint_pformat            | 991 ms                                                                                                               | 849 ms: 1.17x faster                                                                                                     |
| xml_etree_generate        | 55.6 ms                                                                                                              | 49.8 ms: 1.12x faster                                                                                                    |
| xml_etree_process         | 38.4 ms                                                                                                              | 34.7 ms: 1.11x faster                                                                                                    |
| pyflate                   | 282 ms                                                                                                               | 256 ms: 1.10x faster                                                                                                     |
| pickle                    | 8.21 us                                                                                                              | 7.46 us: 1.10x faster                                                                                                    |
| scimark_sparse_mat_mult   | 2.48 ms                                                                                                              | 2.28 ms: 1.09x faster                                                                                                    |
| telco                     | 4.14 ms                                                                                                              | 3.82 ms: 1.09x faster                                                                                                    |
| connected_components      | 344 ms                                                                                                               | 319 ms: 1.08x faster                                                                                                     |
| comprehensions            | 11.0 us                                                                                                              | 10.3 us: 1.07x faster                                                                                                    |
| k_core                    | 1.70 sec                                                                                                             | 1.59 sec: 1.07x faster                                                                                                   |
| crypto_pyaes              | 47.1 ms                                                                                                              | 44.2 ms: 1.07x faster                                                                                                    |
| coverage                  | 50.5 ms                                                                                                              | 47.4 ms: 1.07x faster                                                                                                    |
| pickle_pure_python        | 209 us                                                                                                               | 197 us: 1.06x faster                                                                                                     |
| sqlglot_v2_parse          | 801 us                                                                                                               | 762 us: 1.05x faster                                                                                                     |
| nbody                     | 62.8 ms                                                                                                              | 60.0 ms: 1.05x faster                                                                                                    |
| unpack_sequence           | 34.5 ns                                                                                                              | 33.0 ns: 1.05x faster                                                                                                    |
| regex_dna                 | 120 ms                                                                                                               | 116 ms: 1.04x faster                                                                                                     |
| shortest_path             | 361 ms                                                                                                               | 348 ms: 1.04x faster                                                                                                     |
| async_tree_io_tg          | 392 ms                                                                                                               | 377 ms: 1.04x faster                                                                                                     |
| unpickle_list             | 2.80 us                                                                                                              | 2.70 us: 1.04x faster                                                                                                    |
| hexiom                    | 4.04 ms                                                                                                              | 3.91 ms: 1.03x faster                                                                                                    |
| pickle_dict               | 20.0 us                                                                                                              | 19.3 us: 1.03x faster                                                                                                    |
| sympy_sum                 | 87.2 ms                                                                                                              | 84.5 ms: 1.03x faster                                                                                                    |
| typing_runtime_protocols  | 104 us                                                                                                               | 100 us: 1.03x faster                                                                                                     |
| nqueens                   | 61.0 ms                                                                                                              | 59.2 ms: 1.03x faster                                                                                                    |
| sqlglot_v2_transpile      | 999 us                                                                                                               | 969 us: 1.03x faster                                                                                                     |
| logging_silent            | 55.2 ns                                                                                                              | 53.5 ns: 1.03x faster                                                                                                    |
| mdp                       | 800 ms                                                                                                               | 777 ms: 1.03x faster                                                                                                     |
| logging_simple            | 6.06 us                                                                                                              | 5.89 us: 1.03x faster                                                                                                    |
| async_tree_none           | 173 ms                                                                                                               | 168 ms: 1.03x faster                                                                                                     |
| logging_format            | 6.53 us                                                                                                              | 6.35 us: 1.03x faster                                                                                                    |
| chaos                     | 40.6 ms                                                                                                              | 39.6 ms: 1.03x faster                                                                                                    |
| async_tree_none_tg        | 168 ms                                                                                                               | 164 ms: 1.02x faster                                                                                                     |
| xml_etree_parse           | 87.6 ms                                                                                                              | 85.5 ms: 1.02x faster                                                                                                    |
| xml_etree_iterparse       | 63.1 ms                                                                                                              | 61.6 ms: 1.02x faster                                                                                                    |
| bench_mp_pool             | 94.3 ms                                                                                                              | 92.2 ms: 1.02x faster                                                                                                    |
| async_tree_memoization    | 201 ms                                                                                                               | 197 ms: 1.02x faster                                                                                                     |
| go                        | 76.5 ms                                                                                                              | 74.9 ms: 1.02x faster                                                                                                    |
| dulwich_log               | 40.0 ms                                                                                                              | 39.1 ms: 1.02x faster                                                                                                    |
| deepcopy_reduce           | 1.86 us                                                                                                              | 1.82 us: 1.02x faster                                                                                                    |
| meteor_contest            | 71.9 ms                                                                                                              | 70.5 ms: 1.02x faster                                                                                                    |
| django_template           | 24.4 ms                                                                                                              | 23.9 ms: 1.02x faster                                                                                                    |
| thrift                    | 493 us                                                                                                               | 484 us: 1.02x faster                                                                                                     |
| pycparser                 | 706 ms                                                                                                               | 694 ms: 1.02x faster                                                                                                     |
| pickle_list               | 3.35 us                                                                                                              | 3.30 us: 1.02x faster                                                                                                    |
| deepcopy                  | 171 us                                                                                                               | 168 us: 1.02x faster                                                                                                     |
| deltablue                 | 2.18 ms                                                                                                              | 2.15 ms: 1.02x faster                                                                                                    |
| float                     | 43.5 ms                                                                                                              | 42.9 ms: 1.01x faster                                                                                                    |
| docutils                  | 1.63 sec                                                                                                             | 1.61 sec: 1.01x faster                                                                                                   |
| json_loads                | 14.3 us                                                                                                              | 14.1 us: 1.01x faster                                                                                                    |
| 2to3                      | 217 ms                                                                                                               | 214 ms: 1.01x faster                                                                                                     |
| create_gc_cycles          | 1.29 ms                                                                                                              | 1.28 ms: 1.01x faster                                                                                                    |
| sqlite_synth              | 1.54 us                                                                                                              | 1.52 us: 1.01x faster                                                                                                    |
| regex_v8                  | 13.7 ms                                                                                                              | 13.5 ms: 1.01x faster                                                                                                    |
| html5lib                  | 37.7 ms                                                                                                              | 37.3 ms: 1.01x faster                                                                                                    |
| python_startup            | 25.5 ms                                                                                                              | 25.2 ms: 1.01x faster                                                                                                    |
| subparsers                | 29.6 ms                                                                                                              | 29.4 ms: 1.01x faster                                                                                                    |
| regex_compile             | 78.1 ms                                                                                                              | 77.4 ms: 1.01x faster                                                                                                    |
| spectral_norm             | 62.7 ms                                                                                                              | 62.1 ms: 1.01x faster                                                                                                    |
| json_dumps                | 5.36 ms                                                                                                              | 5.31 ms: 1.01x faster                                                                                                    |
| generators                | 19.2 ms                                                                                                              | 19.1 ms: 1.01x faster                                                                                                    |
| many_optionals            | 553 us                                                                                                               | 558 us: 1.01x slower                                                                                                     |
| deepcopy_memo             | 17.9 us                                                                                                              | 18.2 us: 1.01x slower                                                                                                    |
| scimark_sor               | 73.5 ms                                                                                                              | 74.7 ms: 1.02x slower                                                                                                    |
| coroutines                | 14.3 ms                                                                                                              | 14.5 ms: 1.02x slower                                                                                                    |
| sqlglot_v2_optimize       | 33.5 ms                                                                                                              | 34.1 ms: 1.02x slower                                                                                                    |
| async_tree_memoization_tg | 204 ms                                                                                                               | 208 ms: 1.02x slower                                                                                                     |
| regex_effbot              | 1.52 ms                                                                                                              | 1.55 ms: 1.02x slower                                                                                                    |
| sqlglot_v2_normalize      | 68.7 ms                                                                                                              | 70.3 ms: 1.02x slower                                                                                                    |
| raytrace                  | 172 ms                                                                                                               | 176 ms: 1.03x slower                                                                                                     |
| sympy_expand              | 278 ms                                                                                                               | 288 ms: 1.03x slower                                                                                                     |
| json                      | 2.91 ms                                                                                                              | 3.02 ms: 1.04x slower                                                                                                    |
| async_generators          | 224 ms                                                                                                               | 237 ms: 1.06x slower                                                                                                     |
| scimark_lu                | 53.6 ms                                                                                                              | 57.8 ms: 1.08x slower                                                                                                    |
| Geometric mean            | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (21): asyncio_websockets, pathlib, genshi_xml, python_startup_no_site, sphinx, async_tree_io, richards, sympy_integrate, asyncio_tcp_ssl, pidigits, sympy_str, scimark_monte_carlo, richards_super, bench_thread_pool, genshi_text, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, pylint, unpickle, gc_traversal, asyncio_tcp

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown