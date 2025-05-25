# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.003x faster
- HPT reliability: 67.67%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 648 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 390 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 381 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| nbody          | 66.3 ms                                                     | 60.1 ms: 1.10x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 111 us: 1.17x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.5 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.54 ms: 1.19x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.56x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                       |
| mdp                        | 1.43 sec                                                    | 816 ms: 1.75x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 165 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 390 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 381 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.54 ms: 1.19x faster                                                      |
| float                      | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 111 us: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.26 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.14x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                                      |
| scimark_fft                | 175 ms                                                      | 156 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.59 sec: 1.11x faster                                                     |
| json                       | 3.30 ms                                                     | 2.99 ms: 1.10x faster                                                      |
| pyflate                    | 283 ms                                                      | 257 ms: 1.10x faster                                                       |
| nbody                      | 66.3 ms                                                     | 60.1 ms: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                      |
| fannkuch                   | 252 ms                                                      | 236 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                     |
| scimark_sor                | 76.2 ms                                                     | 72.8 ms: 1.05x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.52 us: 1.05x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 60.7 ms: 1.05x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.2 ms: 1.04x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.7 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.6 ms: 1.03x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                       |
| python_startup             | 24.4 ms                                                     | 24.6 ms: 1.01x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| chaos                      | 37.9 ms                                                     | 38.3 ms: 1.01x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 86.7 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 294 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 648 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 108 us: 1.05x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.1 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 855 us: 1.05x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 511 ms: 1.06x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 76.3 ms: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.07x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.05 sec: 1.08x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 91.4 ms: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.70 us: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| python_startup_no_site     | 16.9 ms                                                     | 18.5 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                       |
| django_template            | 20.3 ms                                                     | 23.6 ms: 1.16x slower                                                      |
| many_optionals             | 361 us                                                      | 451 us: 1.25x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 307 ns: 5.63x slower                                                       |
| coverage                   | 45.3 ms                                                     | 288 ms: 6.36x slower                                                       |
| thrift                     | 8.47 ms                                                     | 93.4 ms: 11.03x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (7): pylint, shortest_path, pycparser, scimark_lu, json_dumps, html5lib, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0-JIT/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 67.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown