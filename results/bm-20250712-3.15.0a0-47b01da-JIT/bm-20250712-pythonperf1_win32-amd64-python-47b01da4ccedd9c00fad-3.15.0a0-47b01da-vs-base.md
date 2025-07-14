# Results vs. base

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.021x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                                                                   | 1.66 sec: 1.03x slower                                                                                                         |
| sphinx         | 634 ms                                                                                                                     | 641 ms: 1.01x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 170 ms                                                                                                                     | 165 ms: 1.03x faster                                                                                                           |
| async_tree_io_tg           | 398 ms                                                                                                                     | 390 ms: 1.02x faster                                                                                                           |
| async_tree_memoization     | 204 ms                                                                                                                     | 200 ms: 1.02x faster                                                                                                           |
| coroutines                 | 14.4 ms                                                                                                                    | 14.2 ms: 1.01x faster                                                                                                          |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                                     | 337 ms: 1.01x faster                                                                                                           |
| async_tree_cpu_io_mixed    | 332 ms                                                                                                                     | 330 ms: 1.01x faster                                                                                                           |
| async_generators           | 229 ms                                                                                                                     | 248 ms: 1.08x slower                                                                                                           |
| asyncio_tcp_ssl            | 1.30 sec                                                                                                                   | 1.42 sec: 1.10x slower                                                                                                         |
| asyncio_tcp                | 399 ms                                                                                                                     | 500 ms: 1.25x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, asyncio_websockets, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.6 ms                                                                                                                    | 54.6 ms: 1.20x faster                                                                                                          |
| pidigits       | 145 ms                                                                                                                     | 146 ms: 1.00x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                                                                     | 120 ms: 1.04x slower                                                                                                           |
| regex_v8       | 13.2 ms                                                                                                                    | 14.0 ms: 1.06x slower                                                                                                          |
| regex_effbot   | 1.49 ms                                                                                                                    | 1.63 ms: 1.09x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.05x slower                                                                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 132 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| tomli_loads          | 1.35 sec                                                                                                                   | 1.13 sec: 1.20x faster                                                                                                         |
| xml_etree_process    | 38.8 ms                                                                                                                    | 35.3 ms: 1.10x faster                                                                                                          |
| xml_etree_generate   | 55.2 ms                                                                                                                    | 50.5 ms: 1.09x faster                                                                                                          |
| xml_etree_iterparse  | 63.6 ms                                                                                                                    | 61.3 ms: 1.04x faster                                                                                                          |
| pickle_pure_python   | 208 us                                                                                                                     | 201 us: 1.03x faster                                                                                                           |
| pickle               | 7.99 us                                                                                                                    | 7.86 us: 1.02x faster                                                                                                          |
| unpickle             | 8.48 us                                                                                                                    | 8.54 us: 1.01x slower                                                                                                          |
| json_loads           | 14.2 us                                                                                                                    | 14.3 us: 1.01x slower                                                                                                          |
| pickle_dict          | 19.8 us                                                                                                                    | 20.1 us: 1.01x slower                                                                                                          |
| json_dumps           | 6.13 ms                                                                                                                    | 6.23 ms: 1.02x slower                                                                                                          |
| pickle_list          | 3.29 us                                                                                                                    | 3.40 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.1 ms                                                                                                                    | 25.4 ms: 1.03x faster                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.52 ms                                                                                                                    | 5.38 ms: 1.21x faster                                                                                                          |
| genshi_text     | 15.6 ms                                                                                                                    | 15.3 ms: 1.02x faster                                                                                                          |
| django_template | 25.1 ms                                                                                                                    | 24.6 ms: 1.02x faster                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 132 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| mako                       | 6.52 ms                                                                                                                    | 5.38 ms: 1.21x faster                                                                                                          |
| fannkuch                   | 257 ms                                                                                                                     | 213 ms: 1.20x faster                                                                                                           |
| nbody                      | 65.6 ms                                                                                                                    | 54.6 ms: 1.20x faster                                                                                                          |
| tomli_loads                | 1.35 sec                                                                                                                   | 1.13 sec: 1.20x faster                                                                                                         |
| scimark_fft                | 176 ms                                                                                                                     | 149 ms: 1.18x faster                                                                                                           |
| pyflate                    | 287 ms                                                                                                                     | 253 ms: 1.14x faster                                                                                                           |
| unpack_sequence            | 37.5 ns                                                                                                                    | 33.3 ns: 1.13x faster                                                                                                          |
| bpe_tokeniser              | 2.91 sec                                                                                                                   | 2.58 sec: 1.12x faster                                                                                                         |
| scimark_sparse_mat_mult    | 2.52 ms                                                                                                                    | 2.28 ms: 1.11x faster                                                                                                          |
| xml_etree_process          | 38.8 ms                                                                                                                    | 35.3 ms: 1.10x faster                                                                                                          |
| xml_etree_generate         | 55.2 ms                                                                                                                    | 50.5 ms: 1.09x faster                                                                                                          |
| pprint_safe_repr           | 485 ms                                                                                                                     | 447 ms: 1.08x faster                                                                                                           |
| pprint_pformat             | 977 ms                                                                                                                     | 912 ms: 1.07x faster                                                                                                           |
| k_core                     | 1.71 sec                                                                                                                   | 1.60 sec: 1.06x faster                                                                                                         |
| nqueens                    | 61.4 ms                                                                                                                    | 57.7 ms: 1.06x faster                                                                                                          |
| crypto_pyaes               | 47.6 ms                                                                                                                    | 45.4 ms: 1.05x faster                                                                                                          |
| sqlglot_v2_parse           | 824 us                                                                                                                     | 785 us: 1.05x faster                                                                                                           |
| telco                      | 4.51 ms                                                                                                                    | 4.33 ms: 1.04x faster                                                                                                          |
| xml_etree_iterparse        | 63.6 ms                                                                                                                    | 61.3 ms: 1.04x faster                                                                                                          |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                                    | 991 us: 1.03x faster                                                                                                           |
| pickle_pure_python         | 208 us                                                                                                                     | 201 us: 1.03x faster                                                                                                           |
| connected_components       | 332 ms                                                                                                                     | 322 ms: 1.03x faster                                                                                                           |
| python_startup             | 26.1 ms                                                                                                                    | 25.4 ms: 1.03x faster                                                                                                          |
| subparsers                 | 17.6 ms                                                                                                                    | 17.1 ms: 1.03x faster                                                                                                          |
| async_tree_none            | 170 ms                                                                                                                     | 165 ms: 1.03x faster                                                                                                           |
| async_tree_io_tg           | 398 ms                                                                                                                     | 390 ms: 1.02x faster                                                                                                           |
| genshi_text                | 15.6 ms                                                                                                                    | 15.3 ms: 1.02x faster                                                                                                          |
| create_gc_cycles           | 1.34 ms                                                                                                                    | 1.32 ms: 1.02x faster                                                                                                          |
| shortest_path              | 360 ms                                                                                                                     | 353 ms: 1.02x faster                                                                                                           |
| django_template            | 25.1 ms                                                                                                                    | 24.6 ms: 1.02x faster                                                                                                          |
| raytrace                   | 181 ms                                                                                                                     | 178 ms: 1.02x faster                                                                                                           |
| async_tree_memoization     | 204 ms                                                                                                                     | 200 ms: 1.02x faster                                                                                                           |
| gc_traversal               | 2.17 ms                                                                                                                    | 2.13 ms: 1.02x faster                                                                                                          |
| pickle                     | 7.99 us                                                                                                                    | 7.86 us: 1.02x faster                                                                                                          |
| coroutines                 | 14.4 ms                                                                                                                    | 14.2 ms: 1.01x faster                                                                                                          |
| meteor_contest             | 71.4 ms                                                                                                                    | 70.5 ms: 1.01x faster                                                                                                          |
| dulwich_log                | 40.7 ms                                                                                                                    | 40.2 ms: 1.01x faster                                                                                                          |
| sqlite_synth               | 1.57 us                                                                                                                    | 1.55 us: 1.01x faster                                                                                                          |
| logging_simple             | 6.16 us                                                                                                                    | 6.09 us: 1.01x faster                                                                                                          |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                                     | 337 ms: 1.01x faster                                                                                                           |
| thrift                     | 495 us                                                                                                                     | 490 us: 1.01x faster                                                                                                           |
| logging_format             | 6.60 us                                                                                                                    | 6.54 us: 1.01x faster                                                                                                          |
| comprehensions             | 10.7 us                                                                                                                    | 10.6 us: 1.01x faster                                                                                                          |
| deepcopy_reduce            | 1.82 us                                                                                                                    | 1.80 us: 1.01x faster                                                                                                          |
| mdp                        | 807 ms                                                                                                                     | 800 ms: 1.01x faster                                                                                                           |
| deltablue                  | 2.16 ms                                                                                                                    | 2.14 ms: 1.01x faster                                                                                                          |
| async_tree_cpu_io_mixed    | 332 ms                                                                                                                     | 330 ms: 1.01x faster                                                                                                           |
| chaos                      | 40.2 ms                                                                                                                    | 40.0 ms: 1.01x faster                                                                                                          |
| pidigits                   | 145 ms                                                                                                                     | 146 ms: 1.00x slower                                                                                                           |
| unpickle                   | 8.48 us                                                                                                                    | 8.54 us: 1.01x slower                                                                                                          |
| richards                   | 26.6 ms                                                                                                                    | 26.9 ms: 1.01x slower                                                                                                          |
| json_loads                 | 14.2 us                                                                                                                    | 14.3 us: 1.01x slower                                                                                                          |
| sphinx                     | 634 ms                                                                                                                     | 641 ms: 1.01x slower                                                                                                           |
| spectral_norm              | 61.2 ms                                                                                                                    | 62.0 ms: 1.01x slower                                                                                                          |
| pickle_dict                | 19.8 us                                                                                                                    | 20.1 us: 1.01x slower                                                                                                          |
| json_dumps                 | 6.13 ms                                                                                                                    | 6.23 ms: 1.02x slower                                                                                                          |
| scimark_sor                | 73.3 ms                                                                                                                    | 74.5 ms: 1.02x slower                                                                                                          |
| hexiom                     | 4.04 ms                                                                                                                    | 4.11 ms: 1.02x slower                                                                                                          |
| logging_silent             | 55.2 ns                                                                                                                    | 56.1 ns: 1.02x slower                                                                                                          |
| json                       | 2.97 ms                                                                                                                    | 3.02 ms: 1.02x slower                                                                                                          |
| sympy_str                  | 170 ms                                                                                                                     | 173 ms: 1.02x slower                                                                                                           |
| scimark_monte_carlo        | 39.2 ms                                                                                                                    | 39.9 ms: 1.02x slower                                                                                                          |
| sympy_expand               | 289 ms                                                                                                                     | 295 ms: 1.02x slower                                                                                                           |
| sympy_integrate            | 12.4 ms                                                                                                                    | 12.7 ms: 1.02x slower                                                                                                          |
| go                         | 74.8 ms                                                                                                                    | 76.4 ms: 1.02x slower                                                                                                          |
| sqlglot_v2_optimize        | 33.8 ms                                                                                                                    | 34.6 ms: 1.02x slower                                                                                                          |
| many_optionals             | 440 us                                                                                                                     | 451 us: 1.03x slower                                                                                                           |
| deepcopy                   | 167 us                                                                                                                     | 171 us: 1.03x slower                                                                                                           |
| scimark_lu                 | 57.2 ms                                                                                                                    | 58.8 ms: 1.03x slower                                                                                                          |
| docutils                   | 1.61 sec                                                                                                                   | 1.66 sec: 1.03x slower                                                                                                         |
| pickle_list                | 3.29 us                                                                                                                    | 3.40 us: 1.03x slower                                                                                                          |
| regex_dna                  | 116 ms                                                                                                                     | 120 ms: 1.04x slower                                                                                                           |
| generators                 | 19.3 ms                                                                                                                    | 20.2 ms: 1.05x slower                                                                                                          |
| deepcopy_memo              | 17.2 us                                                                                                                    | 18.1 us: 1.05x slower                                                                                                          |
| regex_v8                   | 13.2 ms                                                                                                                    | 14.0 ms: 1.06x slower                                                                                                          |
| async_generators           | 229 ms                                                                                                                     | 248 ms: 1.08x slower                                                                                                           |
| regex_effbot               | 1.49 ms                                                                                                                    | 1.63 ms: 1.09x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.30 sec                                                                                                                   | 1.42 sec: 1.10x slower                                                                                                         |
| asyncio_tcp                | 399 ms                                                                                                                     | 500 ms: 1.25x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (22): async_tree_none_tg, asyncio_websockets, async_tree_io, sqlglot_v2_normalize, 2to3, genshi_xml, typing_runtime_protocols, pycparser, float, async_tree_memoization_tg, bench_thread_pool, python_startup_no_site, unpickle_list, html5lib, xml_etree_parse, pathlib, richards_super, sympy_sum, coverage, regex_compile, bench_mp_pool, pylint

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown