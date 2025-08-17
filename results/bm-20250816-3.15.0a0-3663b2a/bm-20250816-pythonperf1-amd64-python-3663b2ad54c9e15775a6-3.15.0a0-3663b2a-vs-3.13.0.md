# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.066x faster
- HPT reliability: 50.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 388 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                      |
| nbody          | 66.3 ms                                                     | 63.6 ms: 1.04x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.43 ms: 1.14x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.0 ms: 1.06x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.2 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 494 us: 17.12x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.7 ms: 2.62x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| mdp                        | 1.43 sec                                                    | 794 ms: 1.80x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 388 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.7 us: 1.23x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 327 ms: 1.16x faster                                                       |
| float                      | 50.8 ms                                                     | 44.2 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.43 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.3 ms: 1.13x faster                                                      |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.38 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.0 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| pylint                     | 205 ms                                                      | 195 ms: 1.06x faster                                                       |
| nbody                      | 66.3 ms                                                     | 63.6 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.5 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.0 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 55.8 ms: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.8 ms: 1.02x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.67 sec: 1.02x faster                                                     |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| sympy_expand               | 286 ms                                                      | 283 ms: 1.01x faster                                                       |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 85.8 ms: 1.01x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 489 ms: 1.01x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                      |
| scimark_fft                | 175 ms                                                      | 177 ms: 1.01x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 994 ms: 1.02x slower                                                       |
| connected_components       | 320 ms                                                      | 326 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                     |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.02x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.93 us: 1.03x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 835 us: 1.03x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.37 us: 1.03x slower                                                      |
| pyflate                    | 283 ms                                                      | 293 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                      |
| pycparser                  | 695 ms                                                      | 723 ms: 1.04x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.04x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 47.7 ms: 1.05x slower                                                      |
| fannkuch                   | 252 ms                                                      | 263 ms: 1.05x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.05x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.2 ms: 1.07x slower                                                      |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.08x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.1 ms: 1.09x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 92.2 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.0 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| raytrace                   | 153 ms                                                      | 174 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 551 us: 1.52x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.6 ms: 2.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (7): genshi_xml, html5lib, generators, shortest_path, 2to3, genshi_text, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 50.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown