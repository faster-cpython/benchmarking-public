# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.126x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 204 ms: 1.05x faster                                                       |
| html5lib       | 38.2 ms                                                     | 34.5 ms: 1.11x faster                                                      |
| sphinx         | 617 ms                                                      | 594 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| async_tree_none            | 219 ms                                                      | 149 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 195 ms: 1.44x faster                                                       |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 185 ms: 1.43x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 353 ms: 1.41x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 314 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                       |
| async_generators           | 223 ms                                                      | 195 ms: 1.14x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 11.4 ms: 1.10x faster                                                      |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 37.3 ms: 1.36x faster                                                      |
| nbody          | 66.3 ms                                                     | 50.7 ms: 1.31x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 12.8 ms: 1.86x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 67.6 ms: 1.19x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                      |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 103 us: 1.26x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.20 ms: 1.19x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 47.7 ms: 1.12x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                      |
| pickle_pure_python   | 186 us                                                      | 167 us: 1.11x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.5 ms: 1.32x faster                                                      |
| genshi_xml      | 33.9 ms                                                     | 27.5 ms: 1.23x faster                                                      |
| mako            | 6.56 ms                                                     | 5.90 ms: 1.11x faster                                                      |
| django_template | 20.3 ms                                                     | 20.1 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 27.8 ms: 2.71x faster                                                      |
| mdp                        | 1.43 sec                                                    | 683 ms: 2.10x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 12.8 ms: 1.86x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 13.8 us: 1.67x faster                                                      |
| deepcopy                   | 223 us                                                      | 139 us: 1.61x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 48.6 ms: 1.57x faster                                                      |
| async_tree_none            | 219 ms                                                      | 149 ms: 1.47x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 28.0 ms: 1.46x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 195 ms: 1.44x faster                                                       |
| async_tree_io              | 513 ms                                                      | 358 ms: 1.43x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 185 ms: 1.43x faster                                                       |
| go                         | 84.7 ms                                                     | 59.9 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 353 ms: 1.41x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.46 us: 1.39x faster                                                      |
| float                      | 50.8 ms                                                     | 37.3 ms: 1.36x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.5 ms: 1.32x faster                                                      |
| nbody                      | 66.3 ms                                                     | 50.7 ms: 1.31x faster                                                      |
| hexiom                     | 3.84 ms                                                     | 2.95 ms: 1.30x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 48.8 ms: 1.30x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                     |
| fannkuch                   | 252 ms                                                      | 196 ms: 1.29x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 103 us: 1.26x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 45.7 ms: 1.24x faster                                                      |
| generators                 | 19.0 ms                                                     | 15.3 ms: 1.24x faster                                                      |
| richards                   | 26.3 ms                                                     | 21.3 ms: 1.23x faster                                                      |
| genshi_xml                 | 33.9 ms                                                     | 27.5 ms: 1.23x faster                                                      |
| chaos                      | 37.9 ms                                                     | 31.0 ms: 1.22x faster                                                      |
| scimark_fft                | 175 ms                                                      | 143 ms: 1.22x faster                                                       |
| richards_super             | 29.8 ms                                                     | 24.6 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 314 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.61 us: 1.20x faster                                                      |
| deltablue                  | 1.89 ms                                                     | 1.58 ms: 1.20x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 67.6 ms: 1.19x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.20 ms: 1.19x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.08 ms: 1.19x faster                                                      |
| pyflate                    | 283 ms                                                      | 238 ms: 1.19x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                      |
| nqueens                    | 56.1 ms                                                     | 48.8 ms: 1.15x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.50 sec: 1.15x faster                                                     |
| async_generators           | 223 ms                                                      | 195 ms: 1.14x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 40.1 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.29 ms: 1.14x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 90.8 us: 1.14x faster                                                      |
| sympy_expand               | 286 ms                                                      | 254 ms: 1.12x faster                                                       |
| json                       | 3.30 ms                                                     | 2.94 ms: 1.12x faster                                                      |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 47.7 ms: 1.12x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 32.7 ms: 1.12x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.90 ms: 1.11x faster                                                      |
| pickle_pure_python         | 186 us                                                      | 167 us: 1.11x faster                                                       |
| pylint                     | 205 ms                                                      | 185 ms: 1.11x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 34.5 ms: 1.11x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 11.2 ms: 1.10x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 65.3 ms: 1.10x faster                                                      |
| coroutines                 | 12.5 ms                                                     | 11.4 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 444 ms: 1.09x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 78.4 ms: 1.09x faster                                                      |
| pycparser                  | 695 ms                                                      | 643 ms: 1.08x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 37.3 ms: 1.08x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 908 ms: 1.08x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.48 us: 1.07x faster                                                      |
| 2to3                       | 215 ms                                                      | 204 ms: 1.05x faster                                                       |
| raytrace                   | 153 ms                                                      | 146 ms: 1.05x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| sphinx                     | 617 ms                                                      | 594 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.1 ms: 1.03x faster                                                      |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                       |
| logging_format             | 6.18 us                                                     | 6.01 us: 1.03x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                       |
| logging_simple             | 5.77 us                                                     | 5.64 us: 1.02x faster                                                      |
| django_template            | 20.3 ms                                                     | 20.1 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| connected_components       | 320 ms                                                      | 322 ms: 1.01x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 92.0 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                      |
| many_optionals             | 361 us                                                      | 414 us: 1.15x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.42 ms: 1.16x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.71 ms: 1.38x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                      |
| coverage                   | 45.3 ms                                                     | 221 ms: 4.89x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 271 ns: 4.96x slower                                                       |
| thrift                     | 8.47 ms                                                     | 85.9 ms: 10.15x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (3): docutils, xml_etree_iterparse, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.126x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown