# Results vs. base

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.022x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.63 sec                                                                                                             | 1.67 sec: 1.02x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 398 ms                                                                                                               | 381 ms: 1.04x faster                                                                                                     |
| asyncio_tcp                | 404 ms                                                                                                               | 388 ms: 1.04x faster                                                                                                     |
| async_tree_none            | 171 ms                                                                                                               | 165 ms: 1.03x faster                                                                                                     |
| async_tree_memoization     | 204 ms                                                                                                               | 199 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 171 ms                                                                                                               | 167 ms: 1.02x faster                                                                                                     |
| async_tree_io              | 397 ms                                                                                                               | 390 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                                                               | 334 ms: 1.01x faster                                                                                                     |
| coroutines                 | 13.8 ms                                                                                                              | 13.9 ms: 1.01x slower                                                                                                    |
| async_generators           | 228 ms                                                                                                               | 249 ms: 1.09x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (4): async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 62.7 ms                                                                                                              | 60.1 ms: 1.04x faster                                                                                                    |
| float          | 44.6 ms                                                                                                              | 42.9 ms: 1.04x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.4 ms                                                                                                              | 13.7 ms: 1.05x faster                                                                                                    |
| regex_dna      | 120 ms                                                                                                               | 117 ms: 1.03x faster                                                                                                     |
| regex_compile  | 79.5 ms                                                                                                              | 78.4 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.48 ms                                                                                                              | 1.55 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.38 sec                                                                                                             | 1.14 sec: 1.21x faster                                                                                                   |
| unpickle_pure_python | 134 us                                                                                                               | 111 us: 1.20x faster                                                                                                     |
| pickle               | 8.02 us                                                                                                              | 7.52 us: 1.07x faster                                                                                                    |
| xml_etree_generate   | 54.1 ms                                                                                                              | 51.2 ms: 1.06x faster                                                                                                    |
| xml_etree_process    | 37.9 ms                                                                                                              | 36.2 ms: 1.05x faster                                                                                                    |
| unpickle_list        | 2.81 us                                                                                                              | 2.73 us: 1.03x faster                                                                                                    |
| pickle_list          | 3.40 us                                                                                                              | 3.31 us: 1.03x faster                                                                                                    |
| pickle_pure_python   | 211 us                                                                                                               | 205 us: 1.03x faster                                                                                                     |
| json_dumps           | 6.32 ms                                                                                                              | 6.20 ms: 1.02x faster                                                                                                    |
| unpickle             | 8.53 us                                                                                                              | 8.47 us: 1.01x faster                                                                                                    |
| pickle_dict          | 19.6 us                                                                                                              | 19.5 us: 1.01x faster                                                                                                    |
| json_loads           | 14.8 us                                                                                                              | 14.9 us: 1.01x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 24.4 ms                                                                                                              | 24.6 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.46 ms                                                                                                              | 5.54 ms: 1.17x faster                                                                                                    |
| django_template | 24.4 ms                                                                                                              | 23.6 ms: 1.03x faster                                                                                                    |
| genshi_text     | 15.7 ms                                                                                                              | 15.4 ms: 1.02x faster                                                                                                    |
| genshi_xml      | 34.8 ms                                                                                                              | 34.3 ms: 1.01x faster                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.06x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json | results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                | 1.38 sec                                                                                                             | 1.14 sec: 1.21x faster                                                                                                   |
| unpickle_pure_python       | 134 us                                                                                                               | 111 us: 1.20x faster                                                                                                     |
| mako                       | 6.46 ms                                                                                                              | 5.54 ms: 1.17x faster                                                                                                    |
| bpe_tokeniser              | 2.92 sec                                                                                                             | 2.59 sec: 1.13x faster                                                                                                   |
| pyflate                    | 283 ms                                                                                                               | 257 ms: 1.10x faster                                                                                                     |
| scimark_fft                | 171 ms                                                                                                               | 156 ms: 1.10x faster                                                                                                     |
| raytrace                   | 195 ms                                                                                                               | 178 ms: 1.09x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.44 ms                                                                                                              | 2.26 ms: 1.08x faster                                                                                                    |
| pickle                     | 8.02 us                                                                                                              | 7.52 us: 1.07x faster                                                                                                    |
| telco                      | 4.56 ms                                                                                                              | 4.29 ms: 1.06x faster                                                                                                    |
| sqlglot_v2_parse           | 833 us                                                                                                               | 783 us: 1.06x faster                                                                                                     |
| fannkuch                   | 251 ms                                                                                                               | 236 ms: 1.06x faster                                                                                                     |
| pprint_safe_repr           | 543 ms                                                                                                               | 511 ms: 1.06x faster                                                                                                     |
| xml_etree_generate         | 54.1 ms                                                                                                              | 51.2 ms: 1.06x faster                                                                                                    |
| regex_v8                   | 14.4 ms                                                                                                              | 13.7 ms: 1.05x faster                                                                                                    |
| xml_etree_process          | 37.9 ms                                                                                                              | 36.2 ms: 1.05x faster                                                                                                    |
| k_core                     | 1.70 sec                                                                                                             | 1.62 sec: 1.05x faster                                                                                                   |
| async_tree_io_tg           | 398 ms                                                                                                               | 381 ms: 1.04x faster                                                                                                     |
| nbody                      | 62.7 ms                                                                                                              | 60.1 ms: 1.04x faster                                                                                                    |
| pprint_pformat             | 1.10 sec                                                                                                             | 1.05 sec: 1.04x faster                                                                                                   |
| asyncio_tcp                | 404 ms                                                                                                               | 388 ms: 1.04x faster                                                                                                     |
| chaos                      | 39.9 ms                                                                                                              | 38.3 ms: 1.04x faster                                                                                                    |
| sqlite_synth               | 1.58 us                                                                                                              | 1.52 us: 1.04x faster                                                                                                    |
| float                      | 44.6 ms                                                                                                              | 42.9 ms: 1.04x faster                                                                                                    |
| go                         | 80.2 ms                                                                                                              | 77.4 ms: 1.04x faster                                                                                                    |
| scimark_sor                | 75.4 ms                                                                                                              | 72.8 ms: 1.04x faster                                                                                                    |
| logging_silent             | 317 ns                                                                                                               | 307 ns: 1.03x faster                                                                                                     |
| async_tree_none            | 171 ms                                                                                                               | 165 ms: 1.03x faster                                                                                                     |
| logging_format             | 6.93 us                                                                                                              | 6.70 us: 1.03x faster                                                                                                    |
| deepcopy                   | 173 us                                                                                                               | 168 us: 1.03x faster                                                                                                     |
| django_template            | 24.4 ms                                                                                                              | 23.6 ms: 1.03x faster                                                                                                    |
| regex_dna                  | 120 ms                                                                                                               | 117 ms: 1.03x faster                                                                                                     |
| sqlglot_v2_normalize       | 71.5 ms                                                                                                              | 69.5 ms: 1.03x faster                                                                                                    |
| unpickle_list              | 2.81 us                                                                                                              | 2.73 us: 1.03x faster                                                                                                    |
| coverage                   | 296 ms                                                                                                               | 288 ms: 1.03x faster                                                                                                     |
| pickle_list                | 3.40 us                                                                                                              | 3.31 us: 1.03x faster                                                                                                    |
| pickle_pure_python         | 211 us                                                                                                               | 205 us: 1.03x faster                                                                                                     |
| async_tree_memoization     | 204 ms                                                                                                               | 199 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 171 ms                                                                                                               | 167 ms: 1.02x faster                                                                                                     |
| deepcopy_reduce            | 1.82 us                                                                                                              | 1.78 us: 1.02x faster                                                                                                    |
| logging_simple             | 6.38 us                                                                                                              | 6.25 us: 1.02x faster                                                                                                    |
| nqueens                    | 60.3 ms                                                                                                              | 59.1 ms: 1.02x faster                                                                                                    |
| genshi_text                | 15.7 ms                                                                                                              | 15.4 ms: 1.02x faster                                                                                                    |
| async_tree_io              | 397 ms                                                                                                               | 390 ms: 1.02x faster                                                                                                     |
| json_dumps                 | 6.32 ms                                                                                                              | 6.20 ms: 1.02x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                              | 995 us: 1.02x faster                                                                                                     |
| pycparser                  | 705 ms                                                                                                               | 693 ms: 1.02x faster                                                                                                     |
| scimark_monte_carlo        | 40.2 ms                                                                                                              | 39.6 ms: 1.01x faster                                                                                                    |
| regex_compile              | 79.5 ms                                                                                                              | 78.4 ms: 1.01x faster                                                                                                    |
| genshi_xml                 | 34.8 ms                                                                                                              | 34.3 ms: 1.01x faster                                                                                                    |
| richards                   | 27.3 ms                                                                                                              | 26.9 ms: 1.01x faster                                                                                                    |
| richards_super             | 31.0 ms                                                                                                              | 30.7 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                                                               | 334 ms: 1.01x faster                                                                                                     |
| deepcopy_memo              | 17.9 us                                                                                                              | 17.8 us: 1.01x faster                                                                                                    |
| unpickle                   | 8.53 us                                                                                                              | 8.47 us: 1.01x faster                                                                                                    |
| pickle_dict                | 19.6 us                                                                                                              | 19.5 us: 1.01x faster                                                                                                    |
| deltablue                  | 2.16 ms                                                                                                              | 2.15 ms: 1.01x faster                                                                                                    |
| shortest_path              | 356 ms                                                                                                               | 354 ms: 1.00x faster                                                                                                     |
| generators                 | 19.4 ms                                                                                                              | 19.3 ms: 1.00x faster                                                                                                    |
| sympy_str                  | 169 ms                                                                                                               | 170 ms: 1.00x slower                                                                                                     |
| dulwich_log                | 40.3 ms                                                                                                              | 40.5 ms: 1.01x slower                                                                                                    |
| json_loads                 | 14.8 us                                                                                                              | 14.9 us: 1.01x slower                                                                                                    |
| python_startup             | 24.4 ms                                                                                                              | 24.6 ms: 1.01x slower                                                                                                    |
| mdp                        | 811 ms                                                                                                               | 816 ms: 1.01x slower                                                                                                     |
| thrift                     | 92.7 ms                                                                                                              | 93.4 ms: 1.01x slower                                                                                                    |
| json                       | 2.96 ms                                                                                                              | 2.99 ms: 1.01x slower                                                                                                    |
| create_gc_cycles           | 1.28 ms                                                                                                              | 1.30 ms: 1.01x slower                                                                                                    |
| coroutines                 | 13.8 ms                                                                                                              | 13.9 ms: 1.01x slower                                                                                                    |
| sympy_integrate            | 12.4 ms                                                                                                              | 12.6 ms: 1.01x slower                                                                                                    |
| sympy_expand               | 290 ms                                                                                                               | 294 ms: 1.01x slower                                                                                                     |
| many_optionals             | 442 us                                                                                                               | 451 us: 1.02x slower                                                                                                     |
| docutils                   | 1.63 sec                                                                                                             | 1.67 sec: 1.02x slower                                                                                                   |
| gc_traversal               | 2.09 ms                                                                                                              | 2.15 ms: 1.03x slower                                                                                                    |
| typing_runtime_protocols   | 106 us                                                                                                               | 108 us: 1.03x slower                                                                                                     |
| regex_effbot               | 1.48 ms                                                                                                              | 1.55 ms: 1.04x slower                                                                                                    |
| meteor_contest             | 72.9 ms                                                                                                              | 76.3 ms: 1.05x slower                                                                                                    |
| spectral_norm              | 57.3 ms                                                                                                              | 60.7 ms: 1.06x slower                                                                                                    |
| async_generators           | 228 ms                                                                                                               | 249 ms: 1.09x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (24): pathlib, async_tree_memoization_tg, subparsers, comprehensions, sympy_sum, 2to3, connected_components, sqlglot_v2_optimize, crypto_pyaes, scimark_lu, unpack_sequence, asyncio_tcp_ssl, html5lib, xml_etree_iterparse, pidigits, xml_etree_parse, bench_mp_pool, python_startup_no_site, bench_thread_pool, async_tree_cpu_io_mixed, hexiom, sphinx, asyncio_websockets, pylint

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown