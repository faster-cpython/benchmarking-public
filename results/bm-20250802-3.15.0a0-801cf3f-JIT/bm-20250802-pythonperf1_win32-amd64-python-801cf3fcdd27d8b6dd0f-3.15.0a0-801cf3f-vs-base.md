# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.020x faster
- HPT reliability: 93.47%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                                                                     | 224 ms: 1.02x faster                                                                                                           |
| docutils       | 1.61 sec                                                                                                                   | 1.67 sec: 1.04x slower                                                                                                         |
| html5lib       | 39.5 ms                                                                                                                    | 41.9 ms: 1.06x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization     | 218 ms                                                                                                                     | 210 ms: 1.04x faster                                                                                                           |
| async_tree_io_tg           | 406 ms                                                                                                                     | 396 ms: 1.03x faster                                                                                                           |
| async_tree_none_tg         | 173 ms                                                                                                                     | 171 ms: 1.01x faster                                                                                                           |
| async_tree_cpu_io_mixed_tg | 348 ms                                                                                                                     | 353 ms: 1.01x slower                                                                                                           |
| async_generators           | 237 ms                                                                                                                     | 244 ms: 1.03x slower                                                                                                           |
| asyncio_tcp_ssl            | 1.30 sec                                                                                                                   | 1.44 sec: 1.11x slower                                                                                                         |
| asyncio_tcp                | 448 ms                                                                                                                     | 502 ms: 1.12x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (6): async_tree_memoization_tg, coroutines, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                                                                    | 55.3 ms: 1.18x faster                                                                                                          |
| float          | 43.5 ms                                                                                                                    | 44.3 ms: 1.02x slower                                                                                                          |
| pidigits       | 146 ms                                                                                                                     | 149 ms: 1.02x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 81.0 ms                                                                                                                    | 82.4 ms: 1.02x slower                                                                                                          |
| regex_dna      | 121 ms                                                                                                                     | 124 ms: 1.03x slower                                                                                                           |
| regex_effbot   | 1.64 ms                                                                                                                    | 1.70 ms: 1.03x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                                     | 108 us: 1.24x faster                                                                                                           |
| tomli_loads          | 1.42 sec                                                                                                                   | 1.14 sec: 1.24x faster                                                                                                         |
| xml_etree_generate   | 58.0 ms                                                                                                                    | 51.0 ms: 1.14x faster                                                                                                          |
| xml_etree_process    | 40.0 ms                                                                                                                    | 35.9 ms: 1.11x faster                                                                                                          |
| pickle               | 8.36 us                                                                                                                    | 7.87 us: 1.06x faster                                                                                                          |
| xml_etree_iterparse  | 66.1 ms                                                                                                                    | 63.4 ms: 1.04x faster                                                                                                          |
| pickle_dict          | 20.6 us                                                                                                                    | 19.9 us: 1.03x faster                                                                                                          |
| xml_etree_parse      | 90.8 ms                                                                                                                    | 89.3 ms: 1.02x faster                                                                                                          |
| unpickle_list        | 2.83 us                                                                                                                    | 2.90 us: 1.03x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.06x faster                                                                                                                   |

Benchmark hidden because not significant (5): pickle_pure_python, pickle_list, json_dumps, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 27.2 ms                                                                                                                    | 26.5 ms: 1.02x faster                                                                                                          |
| python_startup_no_site | 20.4 ms                                                                                                                    | 20.0 ms: 1.02x faster                                                                                                          |
| Geometric mean         | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.67 ms                                                                                                                    | 5.34 ms: 1.25x faster                                                                                                          |
| genshi_xml      | 35.2 ms                                                                                                                    | 34.7 ms: 1.02x faster                                                                                                          |
| genshi_text     | 15.7 ms                                                                                                                    | 15.9 ms: 1.01x slower                                                                                                          |
| django_template | 24.6 ms                                                                                                                    | 26.0 ms: 1.06x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

All benchmarks:
===============

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako                       | 6.67 ms                                                                                                                    | 5.34 ms: 1.25x faster                                                                                                          |
| unpickle_pure_python       | 134 us                                                                                                                     | 108 us: 1.24x faster                                                                                                           |
| tomli_loads                | 1.42 sec                                                                                                                   | 1.14 sec: 1.24x faster                                                                                                         |
| scimark_fft                | 184 ms                                                                                                                     | 149 ms: 1.24x faster                                                                                                           |
| fannkuch                   | 256 ms                                                                                                                     | 214 ms: 1.20x faster                                                                                                           |
| nbody                      | 65.3 ms                                                                                                                    | 55.3 ms: 1.18x faster                                                                                                          |
| bpe_tokeniser              | 2.96 sec                                                                                                                   | 2.53 sec: 1.17x faster                                                                                                         |
| scimark_sparse_mat_mult    | 2.60 ms                                                                                                                    | 2.28 ms: 1.14x faster                                                                                                          |
| xml_etree_generate         | 58.0 ms                                                                                                                    | 51.0 ms: 1.14x faster                                                                                                          |
| pprint_pformat             | 1.03 sec                                                                                                                   | 919 ms: 1.12x faster                                                                                                           |
| pprint_safe_repr           | 509 ms                                                                                                                     | 456 ms: 1.12x faster                                                                                                           |
| xml_etree_process          | 40.0 ms                                                                                                                    | 35.9 ms: 1.11x faster                                                                                                          |
| pyflate                    | 289 ms                                                                                                                     | 267 ms: 1.08x faster                                                                                                           |
| pickle                     | 8.36 us                                                                                                                    | 7.87 us: 1.06x faster                                                                                                          |
| pycparser                  | 739 ms                                                                                                                     | 703 ms: 1.05x faster                                                                                                           |
| xml_etree_iterparse        | 66.1 ms                                                                                                                    | 63.4 ms: 1.04x faster                                                                                                          |
| sqlglot_v2_parse           | 831 us                                                                                                                     | 800 us: 1.04x faster                                                                                                           |
| logging_silent             | 58.6 ns                                                                                                                    | 56.4 ns: 1.04x faster                                                                                                          |
| richards                   | 29.0 ms                                                                                                                    | 27.9 ms: 1.04x faster                                                                                                          |
| async_tree_memoization     | 218 ms                                                                                                                     | 210 ms: 1.04x faster                                                                                                           |
| k_core                     | 1.68 sec                                                                                                                   | 1.63 sec: 1.04x faster                                                                                                         |
| spectral_norm              | 67.2 ms                                                                                                                    | 65.0 ms: 1.03x faster                                                                                                          |
| pickle_dict                | 20.6 us                                                                                                                    | 19.9 us: 1.03x faster                                                                                                          |
| crypto_pyaes               | 49.2 ms                                                                                                                    | 47.8 ms: 1.03x faster                                                                                                          |
| scimark_monte_carlo        | 41.9 ms                                                                                                                    | 40.7 ms: 1.03x faster                                                                                                          |
| connected_components       | 335 ms                                                                                                                     | 326 ms: 1.03x faster                                                                                                           |
| async_tree_io_tg           | 406 ms                                                                                                                     | 396 ms: 1.03x faster                                                                                                           |
| nqueens                    | 63.5 ms                                                                                                                    | 62.1 ms: 1.02x faster                                                                                                          |
| python_startup             | 27.2 ms                                                                                                                    | 26.5 ms: 1.02x faster                                                                                                          |
| sqlglot_v2_transpile       | 1.03 ms                                                                                                                    | 1.01 ms: 1.02x faster                                                                                                          |
| richards_super             | 32.1 ms                                                                                                                    | 31.5 ms: 1.02x faster                                                                                                          |
| python_startup_no_site     | 20.4 ms                                                                                                                    | 20.0 ms: 1.02x faster                                                                                                          |
| mdp                        | 824 ms                                                                                                                     | 807 ms: 1.02x faster                                                                                                           |
| xml_etree_parse            | 90.8 ms                                                                                                                    | 89.3 ms: 1.02x faster                                                                                                          |
| genshi_xml                 | 35.2 ms                                                                                                                    | 34.7 ms: 1.02x faster                                                                                                          |
| 2to3                       | 227 ms                                                                                                                     | 224 ms: 1.02x faster                                                                                                           |
| async_tree_none_tg         | 173 ms                                                                                                                     | 171 ms: 1.01x faster                                                                                                           |
| shortest_path              | 361 ms                                                                                                                     | 357 ms: 1.01x faster                                                                                                           |
| meteor_contest             | 72.2 ms                                                                                                                    | 73.1 ms: 1.01x slower                                                                                                          |
| genshi_text                | 15.7 ms                                                                                                                    | 15.9 ms: 1.01x slower                                                                                                          |
| async_tree_cpu_io_mixed_tg | 348 ms                                                                                                                     | 353 ms: 1.01x slower                                                                                                           |
| telco                      | 4.61 ms                                                                                                                    | 4.68 ms: 1.02x slower                                                                                                          |
| chaos                      | 41.3 ms                                                                                                                    | 41.9 ms: 1.02x slower                                                                                                          |
| regex_compile              | 81.0 ms                                                                                                                    | 82.4 ms: 1.02x slower                                                                                                          |
| generators                 | 19.4 ms                                                                                                                    | 19.8 ms: 1.02x slower                                                                                                          |
| deepcopy                   | 175 us                                                                                                                     | 179 us: 1.02x slower                                                                                                           |
| float                      | 43.5 ms                                                                                                                    | 44.3 ms: 1.02x slower                                                                                                          |
| pidigits                   | 146 ms                                                                                                                     | 149 ms: 1.02x slower                                                                                                           |
| hexiom                     | 4.19 ms                                                                                                                    | 4.28 ms: 1.02x slower                                                                                                          |
| create_gc_cycles           | 1.33 ms                                                                                                                    | 1.36 ms: 1.02x slower                                                                                                          |
| json                       | 3.09 ms                                                                                                                    | 3.17 ms: 1.03x slower                                                                                                          |
| unpickle_list              | 2.83 us                                                                                                                    | 2.90 us: 1.03x slower                                                                                                          |
| sympy_str                  | 171 ms                                                                                                                     | 175 ms: 1.03x slower                                                                                                           |
| dulwich_log                | 41.1 ms                                                                                                                    | 42.2 ms: 1.03x slower                                                                                                          |
| regex_dna                  | 121 ms                                                                                                                     | 124 ms: 1.03x slower                                                                                                           |
| sqlglot_v2_optimize        | 34.5 ms                                                                                                                    | 35.5 ms: 1.03x slower                                                                                                          |
| async_generators           | 237 ms                                                                                                                     | 244 ms: 1.03x slower                                                                                                           |
| go                         | 77.1 ms                                                                                                                    | 79.5 ms: 1.03x slower                                                                                                          |
| deltablue                  | 2.27 ms                                                                                                                    | 2.34 ms: 1.03x slower                                                                                                          |
| regex_effbot               | 1.64 ms                                                                                                                    | 1.70 ms: 1.03x slower                                                                                                          |
| docutils                   | 1.61 sec                                                                                                                   | 1.67 sec: 1.04x slower                                                                                                         |
| sympy_integrate            | 12.6 ms                                                                                                                    | 13.0 ms: 1.04x slower                                                                                                          |
| pylint                     | 199 ms                                                                                                                     | 206 ms: 1.04x slower                                                                                                           |
| deepcopy_memo              | 18.4 us                                                                                                                    | 19.2 us: 1.04x slower                                                                                                          |
| raytrace                   | 181 ms                                                                                                                     | 189 ms: 1.05x slower                                                                                                           |
| typing_runtime_protocols   | 102 us                                                                                                                     | 107 us: 1.05x slower                                                                                                           |
| sympy_expand               | 288 ms                                                                                                                     | 303 ms: 1.05x slower                                                                                                           |
| gc_traversal               | 2.10 ms                                                                                                                    | 2.21 ms: 1.05x slower                                                                                                          |
| django_template            | 24.6 ms                                                                                                                    | 26.0 ms: 1.06x slower                                                                                                          |
| html5lib                   | 39.5 ms                                                                                                                    | 41.9 ms: 1.06x slower                                                                                                          |
| asyncio_tcp_ssl            | 1.30 sec                                                                                                                   | 1.44 sec: 1.11x slower                                                                                                         |
| asyncio_tcp                | 448 ms                                                                                                                     | 502 ms: 1.12x slower                                                                                                           |
| Geometric mean             | (ref)                                                                                                                      | 1.02x faster                                                                                                                   |

Benchmark hidden because not significant (30): subparsers, async_tree_memoization_tg, coroutines, comprehensions, async_tree_none, sqlglot_v2_normalize, scimark_lu, pickle_pure_python, unpack_sequence, regex_v8, logging_simple, bench_mp_pool, thrift, sphinx, bench_thread_pool, pickle_list, scimark_sor, async_tree_cpu_io_mixed, sympy_sum, json_dumps, coverage, deepcopy_reduce, json_loads, async_tree_io, many_optionals, unpickle, logging_format, sqlite_synth, pathlib, asyncio_websockets

- Geometric mean (including insignificant results): 1.020x faster

# HPT report

- Reliability score: 93.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown