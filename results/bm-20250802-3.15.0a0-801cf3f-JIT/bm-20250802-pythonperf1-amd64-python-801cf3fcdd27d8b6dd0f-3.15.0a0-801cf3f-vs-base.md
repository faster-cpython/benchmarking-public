# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.64 sec                                                                                                             | 1.65 sec: 1.00x slower                                                                                                   |
| html5lib       | 40.3 ms                                                                                                              | 39.0 ms: 1.03x faster                                                                                                    |
| sphinx         | 645 ms                                                                                                               | 635 ms: 1.02x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 188 ms                                                                                                               | 180 ms: 1.04x faster                                                                                                     |
| async_tree_io_tg           | 406 ms                                                                                                               | 392 ms: 1.04x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 347 ms                                                                                                               | 335 ms: 1.04x faster                                                                                                     |
| asyncio_websockets         | 168 ms                                                                                                               | 163 ms: 1.03x faster                                                                                                     |
| async_tree_io              | 405 ms                                                                                                               | 394 ms: 1.03x faster                                                                                                     |
| async_tree_memoization_tg  | 219 ms                                                                                                               | 214 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 356 ms                                                                                                               | 349 ms: 1.02x faster                                                                                                     |
| async_tree_memoization     | 215 ms                                                                                                               | 211 ms: 1.02x faster                                                                                                     |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                             | 1.41 sec: 1.01x faster                                                                                                   |
| coroutines                 | 14.4 ms                                                                                                              | 14.8 ms: 1.02x slower                                                                                                    |
| async_generators           | 239 ms                                                                                                               | 247 ms: 1.03x slower                                                                                                     |
| asyncio_tcp                | 507 ms                                                                                                               | 527 ms: 1.04x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 67.0 ms                                                                                                              | 60.5 ms: 1.11x faster                                                                                                    |
| float          | 46.2 ms                                                                                                              | 44.7 ms: 1.04x faster                                                                                                    |
| pidigits       | 148 ms                                                                                                               | 151 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 81.2 ms                                                                                                              | 77.9 ms: 1.04x faster                                                                                                    |
| regex_dna      | 119 ms                                                                                                               | 116 ms: 1.03x faster                                                                                                     |
| regex_v8       | 13.9 ms                                                                                                              | 13.5 ms: 1.03x faster                                                                                                    |
| regex_effbot   | 1.52 ms                                                                                                              | 1.55 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 144 us                                                                                                               | 105 us: 1.37x faster                                                                                                     |
| tomli_loads          | 1.43 sec                                                                                                             | 1.10 sec: 1.30x faster                                                                                                   |
| xml_etree_generate   | 58.6 ms                                                                                                              | 50.3 ms: 1.16x faster                                                                                                    |
| xml_etree_process    | 40.7 ms                                                                                                              | 35.5 ms: 1.15x faster                                                                                                    |
| xml_etree_iterparse  | 68.0 ms                                                                                                              | 62.5 ms: 1.09x faster                                                                                                    |
| pickle_pure_python   | 223 us                                                                                                               | 209 us: 1.07x faster                                                                                                     |
| xml_etree_parse      | 92.4 ms                                                                                                              | 86.7 ms: 1.07x faster                                                                                                    |
| unpickle_list        | 3.03 us                                                                                                              | 2.91 us: 1.04x faster                                                                                                    |
| json_loads           | 14.4 us                                                                                                              | 14.1 us: 1.02x faster                                                                                                    |
| json_dumps           | 6.21 ms                                                                                                              | 6.13 ms: 1.01x faster                                                                                                    |
| pickle_list          | 3.28 us                                                                                                              | 3.35 us: 1.02x slower                                                                                                    |
| pickle_dict          | 20.2 us                                                                                                              | 20.6 us: 1.02x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.67 ms                                                                                                              | 5.35 ms: 1.25x faster                                                                                                    |
| genshi_xml      | 36.2 ms                                                                                                              | 34.7 ms: 1.04x faster                                                                                                    |
| genshi_text     | 15.9 ms                                                                                                              | 15.5 ms: 1.03x faster                                                                                                    |
| django_template | 24.6 ms                                                                                                              | 24.8 ms: 1.01x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.07x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 144 us                                                                                                               | 105 us: 1.37x faster                                                                                                     |
| tomli_loads                | 1.43 sec                                                                                                             | 1.10 sec: 1.30x faster                                                                                                   |
| scimark_fft                | 191 ms                                                                                                               | 149 ms: 1.29x faster                                                                                                     |
| fannkuch                   | 277 ms                                                                                                               | 220 ms: 1.26x faster                                                                                                     |
| mako                       | 6.67 ms                                                                                                              | 5.35 ms: 1.25x faster                                                                                                    |
| scimark_sparse_mat_mult    | 2.68 ms                                                                                                              | 2.25 ms: 1.19x faster                                                                                                    |
| bpe_tokeniser              | 2.97 sec                                                                                                             | 2.54 sec: 1.17x faster                                                                                                   |
| xml_etree_generate         | 58.6 ms                                                                                                              | 50.3 ms: 1.16x faster                                                                                                    |
| xml_etree_process          | 40.7 ms                                                                                                              | 35.5 ms: 1.15x faster                                                                                                    |
| pprint_pformat             | 1.05 sec                                                                                                             | 930 ms: 1.13x faster                                                                                                     |
| pprint_safe_repr           | 507 ms                                                                                                               | 454 ms: 1.12x faster                                                                                                     |
| nbody                      | 67.0 ms                                                                                                              | 60.5 ms: 1.11x faster                                                                                                    |
| sqlglot_v2_parse           | 856 us                                                                                                               | 779 us: 1.10x faster                                                                                                     |
| pyflate                    | 302 ms                                                                                                               | 275 ms: 1.10x faster                                                                                                     |
| telco                      | 4.64 ms                                                                                                              | 4.27 ms: 1.09x faster                                                                                                    |
| xml_etree_iterparse        | 68.0 ms                                                                                                              | 62.5 ms: 1.09x faster                                                                                                    |
| richards_super             | 33.0 ms                                                                                                              | 30.6 ms: 1.08x faster                                                                                                    |
| scimark_lu                 | 62.2 ms                                                                                                              | 57.9 ms: 1.08x faster                                                                                                    |
| pickle_pure_python         | 223 us                                                                                                               | 209 us: 1.07x faster                                                                                                     |
| dulwich_log                | 44.2 ms                                                                                                              | 41.3 ms: 1.07x faster                                                                                                    |
| crypto_pyaes               | 48.9 ms                                                                                                              | 45.8 ms: 1.07x faster                                                                                                    |
| create_gc_cycles           | 1.39 ms                                                                                                              | 1.30 ms: 1.07x faster                                                                                                    |
| xml_etree_parse            | 92.4 ms                                                                                                              | 86.7 ms: 1.07x faster                                                                                                    |
| richards                   | 28.6 ms                                                                                                              | 27.0 ms: 1.06x faster                                                                                                    |
| shortest_path              | 367 ms                                                                                                               | 346 ms: 1.06x faster                                                                                                     |
| meteor_contest             | 74.7 ms                                                                                                              | 71.0 ms: 1.05x faster                                                                                                    |
| pycparser                  | 732 ms                                                                                                               | 698 ms: 1.05x faster                                                                                                     |
| go                         | 80.7 ms                                                                                                              | 77.0 ms: 1.05x faster                                                                                                    |
| regex_compile              | 81.2 ms                                                                                                              | 77.9 ms: 1.04x faster                                                                                                    |
| nqueens                    | 63.7 ms                                                                                                              | 61.0 ms: 1.04x faster                                                                                                    |
| async_tree_none            | 188 ms                                                                                                               | 180 ms: 1.04x faster                                                                                                     |
| deepcopy_reduce            | 1.87 us                                                                                                              | 1.80 us: 1.04x faster                                                                                                    |
| genshi_xml                 | 36.2 ms                                                                                                              | 34.7 ms: 1.04x faster                                                                                                    |
| k_core                     | 1.72 sec                                                                                                             | 1.65 sec: 1.04x faster                                                                                                   |
| connected_components       | 335 ms                                                                                                               | 322 ms: 1.04x faster                                                                                                     |
| unpickle_list              | 3.03 us                                                                                                              | 2.91 us: 1.04x faster                                                                                                    |
| comprehensions             | 11.2 us                                                                                                              | 10.8 us: 1.04x faster                                                                                                    |
| async_tree_io_tg           | 406 ms                                                                                                               | 392 ms: 1.04x faster                                                                                                     |
| sqlglot_v2_transpile       | 1.05 ms                                                                                                              | 1.02 ms: 1.04x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 347 ms                                                                                                               | 335 ms: 1.04x faster                                                                                                     |
| float                      | 46.2 ms                                                                                                              | 44.7 ms: 1.04x faster                                                                                                    |
| html5lib                   | 40.3 ms                                                                                                              | 39.0 ms: 1.03x faster                                                                                                    |
| subparsers                 | 31.4 ms                                                                                                              | 30.4 ms: 1.03x faster                                                                                                    |
| asyncio_websockets         | 168 ms                                                                                                               | 163 ms: 1.03x faster                                                                                                     |
| regex_dna                  | 119 ms                                                                                                               | 116 ms: 1.03x faster                                                                                                     |
| logging_silent             | 56.6 ns                                                                                                              | 54.9 ns: 1.03x faster                                                                                                    |
| coverage                   | 49.9 ms                                                                                                              | 48.5 ms: 1.03x faster                                                                                                    |
| regex_v8                   | 13.9 ms                                                                                                              | 13.5 ms: 1.03x faster                                                                                                    |
| async_tree_io              | 405 ms                                                                                                               | 394 ms: 1.03x faster                                                                                                     |
| genshi_text                | 15.9 ms                                                                                                              | 15.5 ms: 1.03x faster                                                                                                    |
| scimark_sor                | 79.3 ms                                                                                                              | 77.3 ms: 1.03x faster                                                                                                    |
| scimark_monte_carlo        | 41.2 ms                                                                                                              | 40.2 ms: 1.03x faster                                                                                                    |
| deltablue                  | 2.22 ms                                                                                                              | 2.17 ms: 1.02x faster                                                                                                    |
| async_tree_memoization_tg  | 219 ms                                                                                                               | 214 ms: 1.02x faster                                                                                                     |
| json_loads                 | 14.4 us                                                                                                              | 14.1 us: 1.02x faster                                                                                                    |
| deepcopy                   | 172 us                                                                                                               | 169 us: 1.02x faster                                                                                                     |
| logging_format             | 6.62 us                                                                                                              | 6.48 us: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 356 ms                                                                                                               | 349 ms: 1.02x faster                                                                                                     |
| sqlglot_v2_normalize       | 72.2 ms                                                                                                              | 70.8 ms: 1.02x faster                                                                                                    |
| async_tree_memoization     | 215 ms                                                                                                               | 211 ms: 1.02x faster                                                                                                     |
| mdp                        | 834 ms                                                                                                               | 819 ms: 1.02x faster                                                                                                     |
| logging_simple             | 6.17 us                                                                                                              | 6.07 us: 1.02x faster                                                                                                    |
| sphinx                     | 645 ms                                                                                                               | 635 ms: 1.02x faster                                                                                                     |
| json_dumps                 | 6.21 ms                                                                                                              | 6.13 ms: 1.01x faster                                                                                                    |
| generators                 | 20.0 ms                                                                                                              | 19.8 ms: 1.01x faster                                                                                                    |
| deepcopy_memo              | 18.1 us                                                                                                              | 17.8 us: 1.01x faster                                                                                                    |
| sqlglot_v2_optimize        | 34.7 ms                                                                                                              | 34.3 ms: 1.01x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                             | 1.41 sec: 1.01x faster                                                                                                   |
| bench_mp_pool              | 96.1 ms                                                                                                              | 95.6 ms: 1.01x faster                                                                                                    |
| docutils                   | 1.64 sec                                                                                                             | 1.65 sec: 1.00x slower                                                                                                   |
| django_template            | 24.6 ms                                                                                                              | 24.8 ms: 1.01x slower                                                                                                    |
| regex_effbot               | 1.52 ms                                                                                                              | 1.55 ms: 1.02x slower                                                                                                    |
| chaos                      | 42.0 ms                                                                                                              | 42.7 ms: 1.02x slower                                                                                                    |
| raytrace                   | 179 ms                                                                                                               | 182 ms: 1.02x slower                                                                                                     |
| pickle_list                | 3.28 us                                                                                                              | 3.35 us: 1.02x slower                                                                                                    |
| pidigits                   | 148 ms                                                                                                               | 151 ms: 1.02x slower                                                                                                     |
| pickle_dict                | 20.2 us                                                                                                              | 20.6 us: 1.02x slower                                                                                                    |
| coroutines                 | 14.4 ms                                                                                                              | 14.8 ms: 1.02x slower                                                                                                    |
| async_generators           | 239 ms                                                                                                               | 247 ms: 1.03x slower                                                                                                     |
| asyncio_tcp                | 507 ms                                                                                                               | 527 ms: 1.04x slower                                                                                                     |
| unpack_sequence            | 33.7 ns                                                                                                              | 35.8 ns: 1.06x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (21): hexiom, python_startup_no_site, bench_thread_pool, gc_traversal, python_startup, async_tree_none_tg, thrift, sympy_sum, pickle, spectral_norm, sqlite_synth, pylint, 2to3, sympy_expand, pathlib, typing_runtime_protocols, sympy_integrate, many_optionals, sympy_str, json, unpickle

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown