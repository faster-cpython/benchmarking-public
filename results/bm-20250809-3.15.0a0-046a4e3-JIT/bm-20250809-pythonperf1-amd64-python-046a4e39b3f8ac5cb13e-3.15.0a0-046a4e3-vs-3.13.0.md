# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.079x faster
- HPT reliability: 91.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 57.5 ms: 1.15x faster                                                      |
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.1 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.23x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 488 us: 17.36x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 804 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                      |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.26 ms: 1.25x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| fannkuch                   | 252 ms                                                      | 217 ms: 1.16x faster                                                       |
| nbody                      | 66.3 ms                                                     | 57.5 ms: 1.15x faster                                                      |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.53 sec: 1.13x faster                                                     |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                                      |
| go                         | 84.7 ms                                                     | 75.5 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 436 ms: 1.11x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 889 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 261 ms: 1.08x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.1 ms: 1.03x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.9 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                      |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.3 ms: 1.01x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 76.8 ms: 1.01x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.1 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 86.7 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.6 ms: 1.03x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.41 us: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.3 ms: 1.05x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.05 us: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 862 us: 1.06x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.2 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                     |
| python_startup             | 24.4 ms                                                     | 26.6 ms: 1.09x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.5 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 96.3 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.8 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 576 us: 1.59x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.1 ms: 2.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (6): pylint, pidigits, typing_runtime_protocols, pycparser, html5lib, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 91.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown