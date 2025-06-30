# Results vs. base

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.013x faster
- HPT reliability: 70.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.61 sec                                                                                                             | 1.68 sec: 1.04x slower                                                                                                   |
| sphinx         | 638 ms                                                                                                               | 653 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                               | 344 ms: 1.01x slower                                                                                                     |
| async_tree_memoization     | 206 ms                                                                                                               | 208 ms: 1.01x slower                                                                                                     |
| async_tree_none            | 170 ms                                                                                                               | 171 ms: 1.01x slower                                                                                                     |
| async_tree_memoization_tg  | 209 ms                                                                                                               | 212 ms: 1.01x slower                                                                                                     |
| async_tree_none_tg         | 167 ms                                                                                                               | 169 ms: 1.01x slower                                                                                                     |
| coroutines                 | 14.2 ms                                                                                                              | 14.5 ms: 1.02x slower                                                                                                    |
| async_generators           | 226 ms                                                                                                               | 248 ms: 1.10x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.32 sec                                                                                                             | 1.45 sec: 1.10x slower                                                                                                   |
| asyncio_tcp                | 428 ms                                                                                                               | 514 ms: 1.20x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.2 ms                                                                                                              | 53.7 ms: 1.21x faster                                                                                                    |
| pidigits       | 146 ms                                                                                                               | 147 ms: 1.01x slower                                                                                                     |
| float          | 44.1 ms                                                                                                              | 44.9 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                                                               | 120 ms: 1.00x slower                                                                                                     |
| regex_v8       | 13.9 ms                                                                                                              | 14.0 ms: 1.01x slower                                                                                                    |
| regex_effbot   | 1.58 ms                                                                                                              | 1.64 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                                                                             | 1.14 sec: 1.23x faster                                                                                                   |
| unpickle_pure_python | 132 us                                                                                                               | 108 us: 1.23x faster                                                                                                     |
| xml_etree_generate   | 55.4 ms                                                                                                              | 51.2 ms: 1.08x faster                                                                                                    |
| xml_etree_process    | 38.7 ms                                                                                                              | 35.9 ms: 1.08x faster                                                                                                    |
| pickle               | 8.09 us                                                                                                              | 7.60 us: 1.06x faster                                                                                                    |
| unpickle_list        | 2.94 us                                                                                                              | 2.79 us: 1.06x faster                                                                                                    |
| pickle_pure_python   | 209 us                                                                                                               | 205 us: 1.02x faster                                                                                                     |
| xml_etree_parse      | 89.5 ms                                                                                                              | 88.9 ms: 1.01x faster                                                                                                    |
| json_loads           | 14.4 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| pickle_list          | 3.36 us                                                                                                              | 3.43 us: 1.02x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (4): pickle_dict, json_dumps, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.7 ms                                                                                                              | 26.0 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.58 ms                                                                                                              | 5.39 ms: 1.22x faster                                                                                                    |
| django_template | 24.0 ms                                                                                                              | 24.3 ms: 1.01x slower                                                                                                    |
| genshi_text     | 15.2 ms                                                                                                              | 15.6 ms: 1.02x slower                                                                                                    |
| genshi_xml      | 34.1 ms                                                                                                              | 35.2 ms: 1.03x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.03x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json | results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                | 1.39 sec                                                                                                             | 1.14 sec: 1.23x faster                                                                                                   |
| unpickle_pure_python       | 132 us                                                                                                               | 108 us: 1.23x faster                                                                                                     |
| mako                       | 6.58 ms                                                                                                              | 5.39 ms: 1.22x faster                                                                                                    |
| nbody                      | 65.2 ms                                                                                                              | 53.7 ms: 1.21x faster                                                                                                    |
| fannkuch                   | 267 ms                                                                                                               | 228 ms: 1.17x faster                                                                                                     |
| scimark_fft                | 175 ms                                                                                                               | 151 ms: 1.16x faster                                                                                                     |
| bpe_tokeniser              | 2.94 sec                                                                                                             | 2.56 sec: 1.15x faster                                                                                                   |
| scimark_sparse_mat_mult    | 2.53 ms                                                                                                              | 2.27 ms: 1.11x faster                                                                                                    |
| pyflate                    | 287 ms                                                                                                               | 258 ms: 1.11x faster                                                                                                     |
| pprint_pformat             | 1.02 sec                                                                                                             | 931 ms: 1.10x faster                                                                                                     |
| pprint_safe_repr           | 493 ms                                                                                                               | 453 ms: 1.09x faster                                                                                                     |
| xml_etree_generate         | 55.4 ms                                                                                                              | 51.2 ms: 1.08x faster                                                                                                    |
| xml_etree_process          | 38.7 ms                                                                                                              | 35.9 ms: 1.08x faster                                                                                                    |
| pickle                     | 8.09 us                                                                                                              | 7.60 us: 1.06x faster                                                                                                    |
| k_core                     | 1.74 sec                                                                                                             | 1.64 sec: 1.06x faster                                                                                                   |
| unpack_sequence            | 40.6 ns                                                                                                              | 38.5 ns: 1.06x faster                                                                                                    |
| unpickle_list              | 2.94 us                                                                                                              | 2.79 us: 1.06x faster                                                                                                    |
| telco                      | 4.61 ms                                                                                                              | 4.41 ms: 1.04x faster                                                                                                    |
| sqlglot_v2_parse           | 824 us                                                                                                               | 790 us: 1.04x faster                                                                                                     |
| nqueens                    | 62.1 ms                                                                                                              | 60.2 ms: 1.03x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.03 ms                                                                                                              | 995 us: 1.03x faster                                                                                                     |
| sqlite_synth               | 1.60 us                                                                                                              | 1.56 us: 1.02x faster                                                                                                    |
| connected_components       | 336 ms                                                                                                               | 329 ms: 1.02x faster                                                                                                     |
| pickle_pure_python         | 209 us                                                                                                               | 205 us: 1.02x faster                                                                                                     |
| sympy_sum                  | 88.2 ms                                                                                                              | 87.0 ms: 1.01x faster                                                                                                    |
| pathlib                    | 32.1 ms                                                                                                              | 31.7 ms: 1.01x faster                                                                                                    |
| meteor_contest             | 72.0 ms                                                                                                              | 71.1 ms: 1.01x faster                                                                                                    |
| shortest_path              | 366 ms                                                                                                               | 361 ms: 1.01x faster                                                                                                     |
| mdp                        | 811 ms                                                                                                               | 803 ms: 1.01x faster                                                                                                     |
| xml_etree_parse            | 89.5 ms                                                                                                              | 88.9 ms: 1.01x faster                                                                                                    |
| deepcopy                   | 170 us                                                                                                               | 169 us: 1.01x faster                                                                                                     |
| regex_dna                  | 119 ms                                                                                                               | 120 ms: 1.00x slower                                                                                                     |
| json_loads                 | 14.4 us                                                                                                              | 14.4 us: 1.01x slower                                                                                                    |
| chaos                      | 40.5 ms                                                                                                              | 40.8 ms: 1.01x slower                                                                                                    |
| deepcopy_reduce            | 1.84 us                                                                                                              | 1.85 us: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                               | 344 ms: 1.01x slower                                                                                                     |
| raytrace                   | 177 ms                                                                                                               | 179 ms: 1.01x slower                                                                                                     |
| regex_v8                   | 13.9 ms                                                                                                              | 14.0 ms: 1.01x slower                                                                                                    |
| pidigits                   | 146 ms                                                                                                               | 147 ms: 1.01x slower                                                                                                     |
| async_tree_memoization     | 206 ms                                                                                                               | 208 ms: 1.01x slower                                                                                                     |
| async_tree_none            | 170 ms                                                                                                               | 171 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_optimize        | 34.2 ms                                                                                                              | 34.6 ms: 1.01x slower                                                                                                    |
| django_template            | 24.0 ms                                                                                                              | 24.3 ms: 1.01x slower                                                                                                    |
| typing_runtime_protocols   | 102 us                                                                                                               | 103 us: 1.01x slower                                                                                                     |
| async_tree_memoization_tg  | 209 ms                                                                                                               | 212 ms: 1.01x slower                                                                                                     |
| dulwich_log                | 40.5 ms                                                                                                              | 41.1 ms: 1.01x slower                                                                                                    |
| python_startup             | 25.7 ms                                                                                                              | 26.0 ms: 1.01x slower                                                                                                    |
| async_tree_none_tg         | 167 ms                                                                                                               | 169 ms: 1.01x slower                                                                                                     |
| go                         | 77.5 ms                                                                                                              | 78.8 ms: 1.02x slower                                                                                                    |
| pickle_list                | 3.36 us                                                                                                              | 3.43 us: 1.02x slower                                                                                                    |
| sympy_str                  | 168 ms                                                                                                               | 172 ms: 1.02x slower                                                                                                     |
| float                      | 44.1 ms                                                                                                              | 44.9 ms: 1.02x slower                                                                                                    |
| scimark_lu                 | 59.7 ms                                                                                                              | 60.9 ms: 1.02x slower                                                                                                    |
| sympy_integrate            | 12.4 ms                                                                                                              | 12.6 ms: 1.02x slower                                                                                                    |
| genshi_text                | 15.2 ms                                                                                                              | 15.6 ms: 1.02x slower                                                                                                    |
| coroutines                 | 14.2 ms                                                                                                              | 14.5 ms: 1.02x slower                                                                                                    |
| scimark_monte_carlo        | 40.2 ms                                                                                                              | 41.1 ms: 1.02x slower                                                                                                    |
| spectral_norm              | 61.9 ms                                                                                                              | 63.5 ms: 1.02x slower                                                                                                    |
| sphinx                     | 638 ms                                                                                                               | 653 ms: 1.02x slower                                                                                                     |
| logging_format             | 6.49 us                                                                                                              | 6.65 us: 1.03x slower                                                                                                    |
| sympy_expand               | 288 ms                                                                                                               | 296 ms: 1.03x slower                                                                                                     |
| generators                 | 19.2 ms                                                                                                              | 19.7 ms: 1.03x slower                                                                                                    |
| richards                   | 27.1 ms                                                                                                              | 27.8 ms: 1.03x slower                                                                                                    |
| richards_super             | 30.9 ms                                                                                                              | 31.8 ms: 1.03x slower                                                                                                    |
| many_optionals             | 437 us                                                                                                               | 451 us: 1.03x slower                                                                                                     |
| genshi_xml                 | 34.1 ms                                                                                                              | 35.2 ms: 1.03x slower                                                                                                    |
| logging_simple             | 6.00 us                                                                                                              | 6.24 us: 1.04x slower                                                                                                    |
| regex_effbot               | 1.58 ms                                                                                                              | 1.64 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.61 sec                                                                                                             | 1.68 sec: 1.04x slower                                                                                                   |
| coverage                   | 48.8 ms                                                                                                              | 51.3 ms: 1.05x slower                                                                                                    |
| deltablue                  | 2.13 ms                                                                                                              | 2.26 ms: 1.06x slower                                                                                                    |
| scimark_sor                | 74.0 ms                                                                                                              | 79.3 ms: 1.07x slower                                                                                                    |
| async_generators           | 226 ms                                                                                                               | 248 ms: 1.10x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.32 sec                                                                                                             | 1.45 sec: 1.10x slower                                                                                                   |
| asyncio_tcp                | 428 ms                                                                                                               | 514 ms: 1.20x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (27): gc_traversal, pickle_dict, json_dumps, xml_etree_iterparse, asyncio_websockets, crypto_pyaes, bench_mp_pool, sqlglot_v2_normalize, unpickle, json, create_gc_cycles, python_startup_no_site, pycparser, logging_silent, regex_compile, hexiom, deepcopy_memo, comprehensions, async_tree_io_tg, subparsers, 2to3, thrift, bench_thread_pool, html5lib, async_tree_cpu_io_mixed, async_tree_io, pylint

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 70.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown