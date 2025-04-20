# Results vs. 3.13.0

- fork: python
- ref: 71da68d5887b6c058907
- machine: windows-amd64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.193x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 204 ms: 1.06x faster                                                        |
| docutils       | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| html5lib       | 38.2 ms                                                     | 34.3 ms: 1.11x faster                                                       |
| sphinx         | 617 ms                                                      | 589 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 196 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 351 ms: 1.42x faster                                                        |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 310 ms: 1.23x faster                                                        |
| async_generators           | 223 ms                                                      | 182 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 36.0 ms: 1.41x faster                                                       |
| nbody          | 66.3 ms                                                     | 55.2 ms: 1.20x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.0 ms: 1.83x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 67.1 ms: 1.20x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.02 sec: 1.34x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 103 us: 1.26x faster                                                        |
| pickle_pure_python   | 186 us                                                      | 162 us: 1.15x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 47.7 ms: 1.12x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.55 ms: 1.11x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 32.8 ms: 1.11x faster                                                       |
| json_loads           | 15.1 us                                                     | 13.8 us: 1.10x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.3 ms: 1.35x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 27.3 ms: 1.24x faster                                                       |
| mako            | 6.56 ms                                                     | 5.81 ms: 1.13x faster                                                       |
| django_template | 20.3 ms                                                     | 19.6 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.1 ms: 2.42x faster                                                       |
| mdp                        | 1.43 sec                                                    | 668 ms: 2.14x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.0 ms: 1.83x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 13.1 us: 1.76x faster                                                       |
| deepcopy                   | 223 us                                                      | 136 us: 1.64x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 48.4 ms: 1.57x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 27.0 ms: 1.51x faster                                                       |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                        |
| go                         | 84.7 ms                                                     | 58.0 ms: 1.46x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 184 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 196 ms: 1.43x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 351 ms: 1.42x faster                                                        |
| float                      | 50.8 ms                                                     | 36.0 ms: 1.41x faster                                                       |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.41x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.46 us: 1.39x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.3 ms: 1.37x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.3 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.34x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.02 sec: 1.34x faster                                                      |
| hexiom                     | 3.84 ms                                                     | 2.88 ms: 1.33x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 41.4 ns: 1.32x faster                                                       |
| comprehensions             | 10.4 us                                                     | 8.17 us: 1.27x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 44.8 ms: 1.27x faster                                                       |
| scimark_fft                | 175 ms                                                      | 138 ms: 1.26x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 103 us: 1.26x faster                                                        |
| generators                 | 19.0 ms                                                     | 15.0 ms: 1.26x faster                                                       |
| chaos                      | 37.9 ms                                                     | 30.2 ms: 1.25x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 388 ms: 1.25x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 783 ms: 1.25x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 27.3 ms: 1.24x faster                                                       |
| pyflate                    | 283 ms                                                      | 229 ms: 1.24x faster                                                        |
| richards                   | 26.3 ms                                                     | 21.3 ms: 1.24x faster                                                       |
| fannkuch                   | 252 ms                                                      | 205 ms: 1.23x faster                                                        |
| deltablue                  | 1.89 ms                                                     | 1.54 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 310 ms: 1.23x faster                                                        |
| nqueens                    | 56.1 ms                                                     | 45.8 ms: 1.23x faster                                                       |
| async_generators           | 223 ms                                                      | 182 ms: 1.23x faster                                                        |
| telco                      | 4.85 ms                                                     | 3.96 ms: 1.22x faster                                                       |
| richards_super             | 29.8 ms                                                     | 24.3 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.14 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 316 ms: 1.21x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 67.1 ms: 1.20x faster                                                       |
| nbody                      | 66.3 ms                                                     | 55.2 ms: 1.20x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 87.3 us: 1.18x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.44 sec: 1.18x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 39.0 ms: 1.17x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 162 us: 1.15x faster                                                        |
| sympy_str                  | 167 ms                                                      | 146 ms: 1.14x faster                                                        |
| json                       | 3.30 ms                                                     | 2.90 ms: 1.14x faster                                                       |
| sympy_expand               | 286 ms                                                      | 251 ms: 1.14x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.81 ms: 1.13x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 47.7 ms: 1.12x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.1 ms: 1.12x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.55 ms: 1.11x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 34.3 ms: 1.11x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 32.8 ms: 1.11x faster                                                       |
| raytrace                   | 153 ms                                                      | 138 ms: 1.11x faster                                                        |
| pylint                     | 205 ms                                                      | 186 ms: 1.11x faster                                                        |
| sympy_sum                  | 85.2 ms                                                     | 77.0 ms: 1.11x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 65.5 ms: 1.10x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.10x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.48 us: 1.07x faster                                                       |
| pycparser                  | 695 ms                                                      | 653 ms: 1.06x faster                                                        |
| dulwich_log                | 40.1 ms                                                     | 37.8 ms: 1.06x faster                                                       |
| 2to3                       | 215 ms                                                      | 204 ms: 1.06x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.05x faster                                                      |
| sphinx                     | 617 ms                                                      | 589 ms: 1.05x faster                                                        |
| logging_simple             | 5.77 us                                                     | 5.51 us: 1.05x faster                                                       |
| logging_format             | 6.18 us                                                     | 5.95 us: 1.04x faster                                                       |
| django_template            | 20.3 ms                                                     | 19.6 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 90.1 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                        |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| docutils                   | 1.53 sec                                                    | 1.54 sec: 1.00x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.02x slower                                                        |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.10x slower                                                       |
| many_optionals             | 361 us                                                      | 401 us: 1.11x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.38 ms: 1.13x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.9 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.6 ms: 1.35x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.71 ms: 1.38x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, bench_thread_pool
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.193x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown