# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: windows-amd64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.005x faster
- HPT reliability: 67.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                                                               | 227 ms: 1.01x slower                                                                                                     |
| docutils       | 1.66 sec                                                                                                             | 1.69 sec: 1.02x slower                                                                                                   |
| html5lib       | 39.0 ms                                                                                                              | 37.6 ms: 1.04x faster                                                                                                    |
| sphinx         | 650 ms                                                                                                               | 658 ms: 1.01x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                               | 335 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 171 ms                                                                                                               | 169 ms: 1.01x faster                                                                                                     |
| coroutines                 | 13.6 ms                                                                                                              | 13.8 ms: 1.01x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.46 sec                                                                                                             | 1.47 sec: 1.01x slower                                                                                                   |
| asyncio_tcp                | 522 ms                                                                                                               | 548 ms: 1.05x slower                                                                                                     |
| async_generators           | 234 ms                                                                                                               | 256 ms: 1.09x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 61.9 ms                                                                                                              | 58.0 ms: 1.07x faster                                                                                                    |
| float          | 43.3 ms                                                                                                              | 44.4 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.3 ms                                                                                                              | 13.9 ms: 1.03x faster                                                                                                    |
| regex_dna      | 120 ms                                                                                                               | 118 ms: 1.02x faster                                                                                                     |
| regex_compile  | 80.4 ms                                                                                                              | 79.6 ms: 1.01x faster                                                                                                    |
| regex_effbot   | 1.54 ms                                                                                                              | 1.57 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                                                                             | 1.16 sec: 1.18x faster                                                                                                   |
| unpickle_pure_python | 130 us                                                                                                               | 118 us: 1.10x faster                                                                                                     |
| xml_etree_generate   | 56.3 ms                                                                                                              | 51.4 ms: 1.10x faster                                                                                                    |
| xml_etree_process    | 39.8 ms                                                                                                              | 36.7 ms: 1.08x faster                                                                                                    |
| json_loads           | 15.4 us                                                                                                              | 14.8 us: 1.04x faster                                                                                                    |
| pickle_list          | 3.59 us                                                                                                              | 3.47 us: 1.04x faster                                                                                                    |
| unpickle             | 8.54 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| json_dumps           | 6.64 ms                                                                                                              | 6.75 ms: 1.02x slower                                                                                                    |
| unpickle_list        | 2.78 us                                                                                                              | 2.87 us: 1.03x slower                                                                                                    |
| pickle               | 7.89 us                                                                                                              | 8.29 us: 1.05x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_dict, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.3 ms                                                                                                              | 26.7 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.59 ms                                                                                                              | 5.66 ms: 1.16x faster                                                                                                    |
| genshi_text     | 15.3 ms                                                                                                              | 15.5 ms: 1.01x slower                                                                                                    |
| django_template | 24.0 ms                                                                                                              | 24.5 ms: 1.02x slower                                                                                                    |
| genshi_xml      | 34.2 ms                                                                                                              | 34.9 ms: 1.02x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.03x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf1-amd64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                | 1.37 sec                                                                                                             | 1.16 sec: 1.18x faster                                                                                                   |
| mako                       | 6.59 ms                                                                                                              | 5.66 ms: 1.16x faster                                                                                                    |
| unpickle_pure_python       | 130 us                                                                                                               | 118 us: 1.10x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.53 ms                                                                                                              | 2.30 ms: 1.10x faster                                                                                                    |
| bpe_tokeniser              | 2.89 sec                                                                                                             | 2.63 sec: 1.10x faster                                                                                                   |
| xml_etree_generate         | 56.3 ms                                                                                                              | 51.4 ms: 1.10x faster                                                                                                    |
| scimark_fft                | 170 ms                                                                                                               | 156 ms: 1.09x faster                                                                                                     |
| xml_etree_process          | 39.8 ms                                                                                                              | 36.7 ms: 1.08x faster                                                                                                    |
| nbody                      | 61.9 ms                                                                                                              | 58.0 ms: 1.07x faster                                                                                                    |
| k_core                     | 1.73 sec                                                                                                             | 1.63 sec: 1.06x faster                                                                                                   |
| pyflate                    | 282 ms                                                                                                               | 268 ms: 1.05x faster                                                                                                     |
| telco                      | 4.59 ms                                                                                                              | 4.40 ms: 1.04x faster                                                                                                    |
| json_loads                 | 15.4 us                                                                                                              | 14.8 us: 1.04x faster                                                                                                    |
| html5lib                   | 39.0 ms                                                                                                              | 37.6 ms: 1.04x faster                                                                                                    |
| pickle_list                | 3.59 us                                                                                                              | 3.47 us: 1.04x faster                                                                                                    |
| regex_v8                   | 14.3 ms                                                                                                              | 13.9 ms: 1.03x faster                                                                                                    |
| json                       | 3.06 ms                                                                                                              | 2.99 ms: 1.02x faster                                                                                                    |
| pycparser                  | 718 ms                                                                                                               | 702 ms: 1.02x faster                                                                                                     |
| raytrace                   | 179 ms                                                                                                               | 175 ms: 1.02x faster                                                                                                     |
| thrift                     | 102 ms                                                                                                               | 100 ms: 1.02x faster                                                                                                     |
| regex_dna                  | 120 ms                                                                                                               | 118 ms: 1.02x faster                                                                                                     |
| sqlite_synth               | 1.60 us                                                                                                              | 1.58 us: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                                                               | 335 ms: 1.02x faster                                                                                                     |
| connected_components       | 331 ms                                                                                                               | 326 ms: 1.01x faster                                                                                                     |
| sqlglot_v2_parse           | 805 us                                                                                                               | 794 us: 1.01x faster                                                                                                     |
| crypto_pyaes               | 47.5 ms                                                                                                              | 46.9 ms: 1.01x faster                                                                                                    |
| shortest_path              | 363 ms                                                                                                               | 358 ms: 1.01x faster                                                                                                     |
| async_tree_none_tg         | 171 ms                                                                                                               | 169 ms: 1.01x faster                                                                                                     |
| regex_compile              | 80.4 ms                                                                                                              | 79.6 ms: 1.01x faster                                                                                                    |
| unpickle                   | 8.54 us                                                                                                              | 8.48 us: 1.01x faster                                                                                                    |
| sqlglot_v2_normalize       | 71.0 ms                                                                                                              | 71.4 ms: 1.01x slower                                                                                                    |
| sqlglot_v2_transpile       | 1.01 ms                                                                                                              | 1.01 ms: 1.01x slower                                                                                                    |
| sympy_str                  | 170 ms                                                                                                               | 171 ms: 1.01x slower                                                                                                     |
| coroutines                 | 13.6 ms                                                                                                              | 13.8 ms: 1.01x slower                                                                                                    |
| dulwich_log                | 41.9 ms                                                                                                              | 42.3 ms: 1.01x slower                                                                                                    |
| sympy_integrate            | 12.5 ms                                                                                                              | 12.6 ms: 1.01x slower                                                                                                    |
| genshi_text                | 15.3 ms                                                                                                              | 15.5 ms: 1.01x slower                                                                                                    |
| logging_simple             | 6.44 us                                                                                                              | 6.50 us: 1.01x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.46 sec                                                                                                             | 1.47 sec: 1.01x slower                                                                                                   |
| logging_format             | 6.92 us                                                                                                              | 7.00 us: 1.01x slower                                                                                                    |
| 2to3                       | 225 ms                                                                                                               | 227 ms: 1.01x slower                                                                                                     |
| mdp                        | 792 ms                                                                                                               | 802 ms: 1.01x slower                                                                                                     |
| typing_runtime_protocols   | 107 us                                                                                                               | 108 us: 1.01x slower                                                                                                     |
| sphinx                     | 650 ms                                                                                                               | 658 ms: 1.01x slower                                                                                                     |
| comprehensions             | 11.3 us                                                                                                              | 11.5 us: 1.01x slower                                                                                                    |
| python_startup             | 26.3 ms                                                                                                              | 26.7 ms: 1.01x slower                                                                                                    |
| deepcopy                   | 173 us                                                                                                               | 176 us: 1.01x slower                                                                                                     |
| json_dumps                 | 6.64 ms                                                                                                              | 6.75 ms: 1.02x slower                                                                                                    |
| chaos                      | 38.0 ms                                                                                                              | 38.7 ms: 1.02x slower                                                                                                    |
| docutils                   | 1.66 sec                                                                                                             | 1.69 sec: 1.02x slower                                                                                                   |
| django_template            | 24.0 ms                                                                                                              | 24.5 ms: 1.02x slower                                                                                                    |
| sympy_expand               | 292 ms                                                                                                               | 297 ms: 1.02x slower                                                                                                     |
| meteor_contest             | 74.4 ms                                                                                                              | 75.8 ms: 1.02x slower                                                                                                    |
| many_optionals             | 440 us                                                                                                               | 448 us: 1.02x slower                                                                                                     |
| regex_effbot               | 1.54 ms                                                                                                              | 1.57 ms: 1.02x slower                                                                                                    |
| genshi_xml                 | 34.2 ms                                                                                                              | 34.9 ms: 1.02x slower                                                                                                    |
| create_gc_cycles           | 1.31 ms                                                                                                              | 1.34 ms: 1.02x slower                                                                                                    |
| richards_super             | 30.9 ms                                                                                                              | 31.6 ms: 1.02x slower                                                                                                    |
| float                      | 43.3 ms                                                                                                              | 44.4 ms: 1.03x slower                                                                                                    |
| deltablue                  | 2.10 ms                                                                                                              | 2.16 ms: 1.03x slower                                                                                                    |
| fannkuch                   | 242 ms                                                                                                               | 249 ms: 1.03x slower                                                                                                     |
| sqlglot_v2_optimize        | 33.9 ms                                                                                                              | 34.9 ms: 1.03x slower                                                                                                    |
| subparsers                 | 16.9 ms                                                                                                              | 17.4 ms: 1.03x slower                                                                                                    |
| unpickle_list              | 2.78 us                                                                                                              | 2.87 us: 1.03x slower                                                                                                    |
| richards                   | 26.8 ms                                                                                                              | 27.6 ms: 1.03x slower                                                                                                    |
| scimark_sor                | 72.7 ms                                                                                                              | 74.9 ms: 1.03x slower                                                                                                    |
| go                         | 77.2 ms                                                                                                              | 79.6 ms: 1.03x slower                                                                                                    |
| logging_silent             | 318 ns                                                                                                               | 328 ns: 1.03x slower                                                                                                     |
| coverage                   | 290 ms                                                                                                               | 300 ms: 1.04x slower                                                                                                     |
| scimark_monte_carlo        | 39.3 ms                                                                                                              | 40.9 ms: 1.04x slower                                                                                                    |
| scimark_lu                 | 57.1 ms                                                                                                              | 59.5 ms: 1.04x slower                                                                                                    |
| asyncio_tcp                | 522 ms                                                                                                               | 548 ms: 1.05x slower                                                                                                     |
| pickle                     | 7.89 us                                                                                                              | 8.29 us: 1.05x slower                                                                                                    |
| hexiom                     | 3.98 ms                                                                                                              | 4.20 ms: 1.06x slower                                                                                                    |
| spectral_norm              | 57.0 ms                                                                                                              | 60.9 ms: 1.07x slower                                                                                                    |
| unpack_sequence            | 38.2 ns                                                                                                              | 41.8 ns: 1.09x slower                                                                                                    |
| async_generators           | 234 ms                                                                                                               | 256 ms: 1.09x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.00x faster                                                                                                             |

Benchmark hidden because not significant (25): pprint_safe_repr, sympy_sum, deepcopy_reduce, generators, async_tree_io, bench_mp_pool, async_tree_none, xml_etree_parse, pprint_pformat, pickle_dict, pathlib, deepcopy_memo, pidigits, xml_etree_iterparse, async_tree_cpu_io_mixed, nqueens, async_tree_memoization_tg, pickle_pure_python, bench_thread_pool, async_tree_memoization, gc_traversal, pylint, python_startup_no_site, async_tree_io_tg, asyncio_websockets

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 67.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown