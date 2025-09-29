# Results vs. base

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| html5lib       | 38.7 ms                                                                                                                    | 37.3 ms: 1.04x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none           | 173 ms                                                                                                                     | 170 ms: 1.02x faster                                                                                                           |
| async_tree_none_tg        | 168 ms                                                                                                                     | 166 ms: 1.02x faster                                                                                                           |
| async_tree_io_tg          | 384 ms                                                                                                                     | 378 ms: 1.02x faster                                                                                                           |
| async_tree_cpu_io_mixed   | 326 ms                                                                                                                     | 330 ms: 1.01x slower                                                                                                           |
| async_tree_memoization_tg | 206 ms                                                                                                                     | 210 ms: 1.02x slower                                                                                                           |
| coroutines                | 14.5 ms                                                                                                                    | 15.0 ms: 1.03x slower                                                                                                          |
| async_generators          | 230 ms                                                                                                                     | 238 ms: 1.04x slower                                                                                                           |
| asyncio_tcp_ssl           | 1.31 sec                                                                                                                   | 1.38 sec: 1.06x slower                                                                                                         |
| asyncio_tcp               | 435 ms                                                                                                                     | 491 ms: 1.13x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.5 ms                                                                                                                    | 53.8 ms: 1.27x faster                                                                                                          |
| float          | 44.7 ms                                                                                                                    | 39.7 ms: 1.13x faster                                                                                                          |
| pidigits       | 151 ms                                                                                                                     | 147 ms: 1.03x faster                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.14x faster                                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 81.4 ms                                                                                                                    | 76.8 ms: 1.06x faster                                                                                                          |
| regex_dna      | 121 ms                                                                                                                     | 118 ms: 1.03x faster                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 138 us                                                                                                                     | 104 us: 1.33x faster                                                                                                           |
| tomli_loads          | 1.41 sec                                                                                                                   | 1.09 sec: 1.29x faster                                                                                                         |
| xml_etree_generate   | 56.8 ms                                                                                                                    | 49.7 ms: 1.14x faster                                                                                                          |
| xml_etree_process    | 39.5 ms                                                                                                                    | 34.7 ms: 1.14x faster                                                                                                          |
| pickle_pure_python   | 218 us                                                                                                                     | 196 us: 1.11x faster                                                                                                           |
| xml_etree_iterparse  | 64.9 ms                                                                                                                    | 60.9 ms: 1.07x faster                                                                                                          |
| xml_etree_parse      | 90.2 ms                                                                                                                    | 86.0 ms: 1.05x faster                                                                                                          |
| json_loads           | 14.4 us                                                                                                                    | 14.0 us: 1.03x faster                                                                                                          |
| unpickle_list        | 2.81 us                                                                                                                    | 2.78 us: 1.01x faster                                                                                                          |
| pickle_dict          | 19.4 us                                                                                                                    | 19.8 us: 1.02x slower                                                                                                          |
| pickle               | 7.78 us                                                                                                                    | 8.01 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.07x faster                                                                                                                   |

Benchmark hidden because not significant (3): json_dumps, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                                                                                    | 25.2 ms: 1.01x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.89 ms                                                                                                                    | 5.31 ms: 1.30x faster                                                                                                          |
| django_template | 24.7 ms                                                                                                                    | 24.0 ms: 1.03x faster                                                                                                          |
| genshi_xml      | 34.5 ms                                                                                                                    | 34.2 ms: 1.01x faster                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.08x faster                                                                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | results/bm-20250926-3.15.0a0-48d0d0d/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json | results/bm-20250926-3.15.0a0-48d0d0d-JIT/bm-20250926-pythonperf1_win32-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json |
|---------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python      | 138 us                                                                                                                     | 104 us: 1.33x faster                                                                                                           |
| scimark_fft               | 177 ms                                                                                                                     | 135 ms: 1.32x faster                                                                                                           |
| mako                      | 6.89 ms                                                                                                                    | 5.31 ms: 1.30x faster                                                                                                          |
| tomli_loads               | 1.41 sec                                                                                                                   | 1.09 sec: 1.29x faster                                                                                                         |
| fannkuch                  | 268 ms                                                                                                                     | 209 ms: 1.28x faster                                                                                                           |
| nbody                     | 68.5 ms                                                                                                                    | 53.8 ms: 1.27x faster                                                                                                          |
| pprint_safe_repr          | 501 ms                                                                                                                     | 416 ms: 1.21x faster                                                                                                           |
| bpe_tokeniser             | 2.99 sec                                                                                                                   | 2.48 sec: 1.20x faster                                                                                                         |
| pprint_pformat            | 1.02 sec                                                                                                                   | 856 ms: 1.20x faster                                                                                                           |
| pyflate                   | 290 ms                                                                                                                     | 247 ms: 1.17x faster                                                                                                           |
| scimark_sparse_mat_mult   | 2.53 ms                                                                                                                    | 2.16 ms: 1.17x faster                                                                                                          |
| xml_etree_generate        | 56.8 ms                                                                                                                    | 49.7 ms: 1.14x faster                                                                                                          |
| xml_etree_process         | 39.5 ms                                                                                                                    | 34.7 ms: 1.14x faster                                                                                                          |
| float                     | 44.7 ms                                                                                                                    | 39.7 ms: 1.13x faster                                                                                                          |
| sqlglot_v2_parse          | 844 us                                                                                                                     | 757 us: 1.12x faster                                                                                                           |
| pickle_pure_python        | 218 us                                                                                                                     | 196 us: 1.11x faster                                                                                                           |
| telco                     | 4.29 ms                                                                                                                    | 3.91 ms: 1.10x faster                                                                                                          |
| sqlglot_v2_transpile      | 1.04 ms                                                                                                                    | 962 us: 1.09x faster                                                                                                           |
| unpack_sequence           | 35.8 ns                                                                                                                    | 33.3 ns: 1.08x faster                                                                                                          |
| logging_silent            | 58.4 ns                                                                                                                    | 54.3 ns: 1.08x faster                                                                                                          |
| crypto_pyaes              | 47.8 ms                                                                                                                    | 44.8 ms: 1.07x faster                                                                                                          |
| k_core                    | 1.69 sec                                                                                                                   | 1.59 sec: 1.07x faster                                                                                                         |
| xml_etree_iterparse       | 64.9 ms                                                                                                                    | 60.9 ms: 1.07x faster                                                                                                          |
| regex_compile             | 81.4 ms                                                                                                                    | 76.8 ms: 1.06x faster                                                                                                          |
| nqueens                   | 63.0 ms                                                                                                                    | 59.5 ms: 1.06x faster                                                                                                          |
| comprehensions            | 11.3 us                                                                                                                    | 10.7 us: 1.06x faster                                                                                                          |
| connected_components      | 333 ms                                                                                                                     | 317 ms: 1.05x faster                                                                                                           |
| hexiom                    | 4.14 ms                                                                                                                    | 3.93 ms: 1.05x faster                                                                                                          |
| xml_etree_parse           | 90.2 ms                                                                                                                    | 86.0 ms: 1.05x faster                                                                                                          |
| deepcopy_memo             | 17.5 us                                                                                                                    | 16.7 us: 1.05x faster                                                                                                          |
| chaos                     | 41.8 ms                                                                                                                    | 40.0 ms: 1.05x faster                                                                                                          |
| shortest_path             | 363 ms                                                                                                                     | 347 ms: 1.05x faster                                                                                                           |
| go                        | 78.8 ms                                                                                                                    | 75.5 ms: 1.04x faster                                                                                                          |
| richards                  | 27.9 ms                                                                                                                    | 26.8 ms: 1.04x faster                                                                                                          |
| sqlite_synth              | 1.59 us                                                                                                                    | 1.52 us: 1.04x faster                                                                                                          |
| deltablue                 | 2.23 ms                                                                                                                    | 2.14 ms: 1.04x faster                                                                                                          |
| raytrace                  | 180 ms                                                                                                                     | 173 ms: 1.04x faster                                                                                                           |
| typing_runtime_protocols  | 106 us                                                                                                                     | 102 us: 1.04x faster                                                                                                           |
| html5lib                  | 38.7 ms                                                                                                                    | 37.3 ms: 1.04x faster                                                                                                          |
| mdp                       | 814 ms                                                                                                                     | 787 ms: 1.03x faster                                                                                                           |
| richards_super            | 31.3 ms                                                                                                                    | 30.3 ms: 1.03x faster                                                                                                          |
| sympy_sum                 | 87.4 ms                                                                                                                    | 84.7 ms: 1.03x faster                                                                                                          |
| deepcopy                  | 167 us                                                                                                                     | 163 us: 1.03x faster                                                                                                           |
| scimark_lu                | 60.3 ms                                                                                                                    | 58.6 ms: 1.03x faster                                                                                                          |
| scimark_monte_carlo       | 41.2 ms                                                                                                                    | 40.0 ms: 1.03x faster                                                                                                          |
| pidigits                  | 151 ms                                                                                                                     | 147 ms: 1.03x faster                                                                                                           |
| pycparser                 | 702 ms                                                                                                                     | 683 ms: 1.03x faster                                                                                                           |
| regex_dna                 | 121 ms                                                                                                                     | 118 ms: 1.03x faster                                                                                                           |
| django_template           | 24.7 ms                                                                                                                    | 24.0 ms: 1.03x faster                                                                                                          |
| json_loads                | 14.4 us                                                                                                                    | 14.0 us: 1.03x faster                                                                                                          |
| pylint                    | 197 ms                                                                                                                     | 193 ms: 1.02x faster                                                                                                           |
| generators                | 19.7 ms                                                                                                                    | 19.2 ms: 1.02x faster                                                                                                          |
| sympy_integrate           | 12.6 ms                                                                                                                    | 12.3 ms: 1.02x faster                                                                                                          |
| meteor_contest            | 73.9 ms                                                                                                                    | 72.5 ms: 1.02x faster                                                                                                          |
| spectral_norm             | 67.1 ms                                                                                                                    | 65.8 ms: 1.02x faster                                                                                                          |
| async_tree_none           | 173 ms                                                                                                                     | 170 ms: 1.02x faster                                                                                                           |
| dulwich_log               | 39.6 ms                                                                                                                    | 38.9 ms: 1.02x faster                                                                                                          |
| async_tree_none_tg        | 168 ms                                                                                                                     | 166 ms: 1.02x faster                                                                                                           |
| deepcopy_reduce           | 1.81 us                                                                                                                    | 1.78 us: 1.02x faster                                                                                                          |
| async_tree_io_tg          | 384 ms                                                                                                                     | 378 ms: 1.02x faster                                                                                                           |
| bench_mp_pool             | 90.6 ms                                                                                                                    | 89.3 ms: 1.01x faster                                                                                                          |
| sympy_str                 | 168 ms                                                                                                                     | 166 ms: 1.01x faster                                                                                                           |
| unpickle_list             | 2.81 us                                                                                                                    | 2.78 us: 1.01x faster                                                                                                          |
| json                      | 2.92 ms                                                                                                                    | 2.89 ms: 1.01x faster                                                                                                          |
| genshi_xml                | 34.5 ms                                                                                                                    | 34.2 ms: 1.01x faster                                                                                                          |
| sqlglot_v2_normalize      | 71.1 ms                                                                                                                    | 70.5 ms: 1.01x faster                                                                                                          |
| python_startup            | 25.4 ms                                                                                                                    | 25.2 ms: 1.01x faster                                                                                                          |
| logging_simple            | 5.99 us                                                                                                                    | 5.94 us: 1.01x faster                                                                                                          |
| coverage                  | 49.3 ms                                                                                                                    | 49.0 ms: 1.01x faster                                                                                                          |
| sympy_expand              | 286 ms                                                                                                                     | 288 ms: 1.01x slower                                                                                                           |
| many_optionals            | 562 us                                                                                                                     | 567 us: 1.01x slower                                                                                                           |
| async_tree_cpu_io_mixed   | 326 ms                                                                                                                     | 330 ms: 1.01x slower                                                                                                           |
| async_tree_memoization_tg | 206 ms                                                                                                                     | 210 ms: 1.02x slower                                                                                                           |
| pickle_dict               | 19.4 us                                                                                                                    | 19.8 us: 1.02x slower                                                                                                          |
| coroutines                | 14.5 ms                                                                                                                    | 15.0 ms: 1.03x slower                                                                                                          |
| pickle                    | 7.78 us                                                                                                                    | 8.01 us: 1.03x slower                                                                                                          |
| async_generators          | 230 ms                                                                                                                     | 238 ms: 1.04x slower                                                                                                           |
| asyncio_tcp_ssl           | 1.31 sec                                                                                                                   | 1.38 sec: 1.06x slower                                                                                                         |
| asyncio_tcp               | 435 ms                                                                                                                     | 491 ms: 1.13x slower                                                                                                           |
| Geometric mean            | (ref)                                                                                                                      | 1.05x faster                                                                                                                   |

Benchmark hidden because not significant (23): pathlib, bench_thread_pool, async_tree_memoization, regex_effbot, create_gc_cycles, python_startup_no_site, async_tree_cpu_io_mixed_tg, subparsers, logging_format, gc_traversal, sphinx, sqlglot_v2_optimize, asyncio_websockets, 2to3, json_dumps, thrift, docutils, scimark_sor, unpickle, genshi_text, pickle_list, regex_v8, async_tree_io

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown