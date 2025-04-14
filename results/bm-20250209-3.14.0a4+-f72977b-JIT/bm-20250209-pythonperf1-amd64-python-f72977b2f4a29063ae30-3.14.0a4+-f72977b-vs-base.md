# Results vs. base

- fork: python
- ref: f72977b2f4a29063ae30
- machine: windows-amd64
- commit hash: f72977b
- commit date: 2025-02-09
- overall geometric mean: 1.010x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                      | 223 ms: 1.01x faster                                                        |
| docutils       | 1.74 sec                                                                    | 1.72 sec: 1.01x faster                                                      |
| html5lib       | 39.3 ms                                                                     | 39.8 ms: 1.01x slower                                                       |
| sphinx         | 656 ms                                                                      | 646 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 317 ms                                                                      | 300 ms: 1.06x faster                                                        |
| async_tree_io              | 419 ms                                                                      | 408 ms: 1.03x faster                                                        |
| async_tree_none            | 186 ms                                                                      | 183 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 342 ms                                                                      | 337 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                      | 342 ms: 1.01x faster                                                        |
| coroutines                 | 12.8 ms                                                                     | 13.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): async_tree_memoization, async_generators, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                                      | 151 ms: 1.01x faster                                                        |
| nbody          | 57.1 ms                                                                     | 59.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.51 ms                                                                     | 1.42 ms: 1.06x faster                                                       |
| regex_dna      | 117 ms                                                                      | 113 ms: 1.04x faster                                                        |
| regex_v8       | 15.0 ms                                                                     | 14.7 ms: 1.02x faster                                                       |
| regex_compile  | 82.2 ms                                                                     | 81.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 217 us                                                                      | 208 us: 1.05x faster                                                        |
| xml_etree_process    | 36.7 ms                                                                     | 35.8 ms: 1.03x faster                                                       |
| xml_etree_generate   | 50.8 ms                                                                     | 49.7 ms: 1.02x faster                                                       |
| json_dumps           | 6.69 ms                                                                     | 6.57 ms: 1.02x faster                                                       |
| xml_etree_parse      | 90.1 ms                                                                     | 88.7 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 61.1 ms                                                                     | 60.2 ms: 1.01x faster                                                       |
| json_loads           | 15.5 us                                                                     | 15.2 us: 1.01x faster                                                       |
| unpickle_pure_python | 113 us                                                                      | 113 us: 1.00x faster                                                        |
| tomli_loads          | 1.19 sec                                                                    | 1.19 sec: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 26.4 ms                                                                     | 25.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 19.7 ms                                                                     | 19.2 ms: 1.03x faster                                                       |
| Geometric mean         | (ref)                                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 25.8 ms                                                                     | 25.3 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 62.1 ms                                                                     | 58.1 ms: 1.07x faster                                                       |
| regex_effbot               | 1.51 ms                                                                     | 1.42 ms: 1.06x faster                                                       |
| asyncio_websockets         | 317 ms                                                                      | 300 ms: 1.06x faster                                                        |
| coverage                   | 49.6 ms                                                                     | 47.4 ms: 1.05x faster                                                       |
| fannkuch                   | 239 ms                                                                      | 228 ms: 1.05x faster                                                        |
| pickle_pure_python         | 217 us                                                                      | 208 us: 1.05x faster                                                        |
| python_startup             | 26.4 ms                                                                     | 25.3 ms: 1.04x faster                                                       |
| regex_dna                  | 117 ms                                                                      | 113 ms: 1.04x faster                                                        |
| richards                   | 29.7 ms                                                                     | 28.5 ms: 1.04x faster                                                       |
| gc_traversal               | 2.05 ms                                                                     | 1.97 ms: 1.04x faster                                                       |
| scimark_monte_carlo        | 45.4 ms                                                                     | 43.9 ms: 1.03x faster                                                       |
| richards_super             | 33.6 ms                                                                     | 32.7 ms: 1.03x faster                                                       |
| logging_silent             | 59.5 ns                                                                     | 58.0 ns: 1.03x faster                                                       |
| python_startup_no_site     | 19.7 ms                                                                     | 19.2 ms: 1.03x faster                                                       |
| xml_etree_process          | 36.7 ms                                                                     | 35.8 ms: 1.03x faster                                                       |
| async_tree_io              | 419 ms                                                                      | 408 ms: 1.03x faster                                                        |
| bench_mp_pool              | 89.9 ms                                                                     | 87.7 ms: 1.02x faster                                                       |
| dulwich_log                | 42.5 ms                                                                     | 41.5 ms: 1.02x faster                                                       |
| regex_v8                   | 15.0 ms                                                                     | 14.7 ms: 1.02x faster                                                       |
| logging_simple             | 6.41 us                                                                     | 6.27 us: 1.02x faster                                                       |
| logging_format             | 6.83 us                                                                     | 6.68 us: 1.02x faster                                                       |
| deltablue                  | 2.34 ms                                                                     | 2.29 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.24 ms                                                                     | 1.21 ms: 1.02x faster                                                       |
| xml_etree_generate         | 50.8 ms                                                                     | 49.7 ms: 1.02x faster                                                       |
| django_template            | 25.8 ms                                                                     | 25.3 ms: 1.02x faster                                                       |
| go                         | 87.6 ms                                                                     | 85.9 ms: 1.02x faster                                                       |
| json_dumps                 | 6.69 ms                                                                     | 6.57 ms: 1.02x faster                                                       |
| xml_etree_parse            | 90.1 ms                                                                     | 88.7 ms: 1.02x faster                                                       |
| async_tree_none            | 186 ms                                                                      | 183 ms: 1.02x faster                                                        |
| generators                 | 20.2 ms                                                                     | 19.8 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 37.6 ms                                                                     | 37.0 ms: 1.02x faster                                                       |
| pycparser                  | 713 ms                                                                      | 703 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 203 ms                                                                      | 200 ms: 1.01x faster                                                        |
| sphinx                     | 656 ms                                                                      | 646 ms: 1.01x faster                                                        |
| nqueens                    | 62.0 ms                                                                     | 61.1 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 61.1 ms                                                                     | 60.2 ms: 1.01x faster                                                       |
| json_loads                 | 15.5 us                                                                     | 15.2 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 342 ms                                                                      | 337 ms: 1.01x faster                                                        |
| deepcopy                   | 186 us                                                                      | 184 us: 1.01x faster                                                        |
| meteor_contest             | 75.8 ms                                                                     | 74.9 ms: 1.01x faster                                                       |
| sympy_sum                  | 90.5 ms                                                                     | 89.5 ms: 1.01x faster                                                       |
| connected_components       | 314 ms                                                                      | 311 ms: 1.01x faster                                                        |
| shortest_path              | 347 ms                                                                      | 344 ms: 1.01x faster                                                        |
| 2to3                       | 225 ms                                                                      | 223 ms: 1.01x faster                                                        |
| comprehensions             | 11.2 us                                                                     | 11.1 us: 1.01x faster                                                       |
| pidigits                   | 152 ms                                                                      | 151 ms: 1.01x faster                                                        |
| sympy_expand               | 307 ms                                                                      | 304 ms: 1.01x faster                                                        |
| docutils                   | 1.74 sec                                                                    | 1.72 sec: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                      | 342 ms: 1.01x faster                                                        |
| sympy_str                  | 177 ms                                                                      | 175 ms: 1.01x faster                                                        |
| hexiom                     | 4.42 ms                                                                     | 4.38 ms: 1.01x faster                                                       |
| sympy_integrate            | 13.5 ms                                                                     | 13.4 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.54 us                                                                     | 1.53 us: 1.01x faster                                                       |
| scimark_lu                 | 61.1 ms                                                                     | 60.6 ms: 1.01x faster                                                       |
| chaos                      | 41.7 ms                                                                     | 41.4 ms: 1.01x faster                                                       |
| scimark_sor                | 84.2 ms                                                                     | 83.6 ms: 1.01x faster                                                       |
| scimark_fft                | 148 ms                                                                      | 147 ms: 1.01x faster                                                        |
| mdp                        | 1.60 sec                                                                    | 1.59 sec: 1.01x faster                                                      |
| regex_compile              | 82.2 ms                                                                     | 81.8 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 113 us                                                                      | 113 us: 1.00x faster                                                        |
| crypto_pyaes               | 45.8 ms                                                                     | 45.6 ms: 1.00x faster                                                       |
| tomli_loads                | 1.19 sec                                                                    | 1.19 sec: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 2.09 ms                                                                     | 2.10 ms: 1.01x slower                                                       |
| spectral_norm              | 57.9 ms                                                                     | 58.4 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 2.56 sec                                                                    | 2.58 sec: 1.01x slower                                                      |
| pprint_pformat             | 975 ms                                                                      | 987 ms: 1.01x slower                                                        |
| html5lib                   | 39.3 ms                                                                     | 39.8 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 1.95 us                                                                     | 1.97 us: 1.01x slower                                                       |
| coroutines                 | 12.8 ms                                                                     | 13.1 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 108 us                                                                      | 110 us: 1.02x slower                                                        |
| many_optionals             | 441 us                                                                      | 452 us: 1.03x slower                                                        |
| deepcopy_memo              | 19.4 us                                                                     | 20.2 us: 1.04x slower                                                       |
| nbody                      | 57.1 ms                                                                     | 59.4 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (21): bench_thread_pool, pprint_safe_repr, k_core, telco, pylint, async_tree_memoization, async_generators, thrift, genshi_xml, genshi_text, sqlglot_parse, subparsers, float, async_tree_io_tg, async_tree_none_tg, sqlglot_transpile, pyflate, mako, raytrace, async_tree_memoization_tg, json
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown