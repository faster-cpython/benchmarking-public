# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.090x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 232 ms: 1.08x slower                                                       |
| docutils       | 1.53 sec                                                    | 3.10 sec: 2.02x slower                                                     |
| html5lib       | 38.2 ms                                                     | 42.2 ms: 1.11x slower                                                      |
| sphinx         | 617 ms                                                      | 753 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.14x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 339 ms: 1.47x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.42x faster                                                       |
| async_tree_io              | 513 ms                                                      | 361 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 153 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.18x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.7 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 47.1 ms: 1.08x faster                                                      |
| pidigits       | 146 ms                                                      | 138 ms: 1.06x faster                                                       |
| nbody          | 66.3 ms                                                     | 86.0 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| regex_compile  | 80.7 ms                                                     | 95.6 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 59.9 ms: 1.01x faster                                                      |
| json_loads           | 15.1 us                                                     | 16.6 us: 1.10x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 7.12 ms: 1.15x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 63.8 ms: 1.19x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 161 us: 1.24x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 234 us: 1.26x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.78 sec: 2.03x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.22x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 41.6 ms: 1.23x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 20.2 ms: 1.33x slower                                                      |
| django_template | 20.3 ms                                                     | 29.0 ms: 1.43x slower                                                      |
| mako            | 6.56 ms                                                     | 9.55 ms: 1.45x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.36x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 570 us: 14.85x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 33.8 ms: 2.23x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.14x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 339 ms: 1.47x faster                                                       |
| gc_traversal               | 1.96 ms                                                     | 1.36 ms: 1.44x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.42x faster                                                       |
| async_tree_io              | 513 ms                                                      | 361 ms: 1.42x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 153 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 315 ms: 1.21x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.21 sec: 1.18x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.35 us: 1.17x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.06 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 333 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.0 us: 1.10x faster                                                      |
| float                      | 50.8 ms                                                     | 47.1 ms: 1.08x faster                                                      |
| pidigits                   | 146 ms                                                      | 138 ms: 1.06x faster                                                       |
| deepcopy                   | 223 us                                                      | 211 us: 1.06x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 80.4 ms: 1.05x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.64 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.9 ms: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 232 ms: 1.08x slower                                                       |
| pycparser                  | 695 ms                                                      | 754 ms: 1.08x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.20 us: 1.09x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 43.7 ms: 1.09x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.29 ms: 1.09x slower                                                      |
| json_loads                 | 15.1 us                                                     | 16.6 us: 1.10x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 42.2 ms: 1.11x slower                                                      |
| python_startup             | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| go                         | 84.7 ms                                                     | 94.9 ms: 1.12x slower                                                      |
| sympy_str                  | 167 ms                                                      | 191 ms: 1.15x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.12 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 326 ms: 1.15x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.8 ns: 1.15x slower                                                      |
| sympy_expand               | 286 ms                                                      | 331 ms: 1.16x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 88.8 ms: 1.17x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 66.6 ms: 1.17x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 100 ms: 1.18x slower                                                       |
| async_generators           | 223 ms                                                      | 262 ms: 1.18x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 573 ms: 1.18x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 95.6 ms: 1.18x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.3 us: 1.19x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 75.5 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.89 us: 1.19x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 63.8 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.12 ms: 1.20x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.9 ms: 1.21x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.51 us: 1.22x slower                                                      |
| sphinx                     | 617 ms                                                      | 753 ms: 1.22x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 87.9 ms: 1.22x slower                                                      |
| generators                 | 19.0 ms                                                     | 23.2 ms: 1.22x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.8 ms: 1.23x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 41.6 ms: 1.23x slower                                                      |
| fannkuch                   | 252 ms                                                      | 309 ms: 1.23x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 161 us: 1.24x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.77 ms: 1.24x slower                                                      |
| chaos                      | 37.9 ms                                                     | 47.0 ms: 1.24x slower                                                      |
| scimark_fft                | 175 ms                                                      | 217 ms: 1.24x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.7 ms: 1.25x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 234 us: 1.26x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 130 us: 1.26x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 51.9 ms: 1.27x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 59.1 ms: 1.30x slower                                                      |
| nbody                      | 66.3 ms                                                     | 86.0 ms: 1.30x slower                                                      |
| richards                   | 26.3 ms                                                     | 34.2 ms: 1.30x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 20.2 ms: 1.33x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.54 ms: 1.34x slower                                                      |
| richards_super             | 29.8 ms                                                     | 40.2 ms: 1.35x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 77.3 ms: 1.38x slower                                                      |
| raytrace                   | 153 ms                                                      | 214 ms: 1.39x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.15 ms: 1.42x slower                                                      |
| django_template            | 20.3 ms                                                     | 29.0 ms: 1.43x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.55 ms: 1.45x slower                                                      |
| coverage                   | 45.3 ms                                                     | 68.0 ms: 1.50x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.71 sec: 1.60x slower                                                     |
| many_optionals             | 361 us                                                      | 642 us: 1.78x slower                                                       |
| shortest_path              | 355 ms                                                      | 666 ms: 1.87x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.83 sec: 1.87x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.65 sec: 1.97x slower                                                     |
| connected_components       | 320 ms                                                      | 631 ms: 1.97x slower                                                       |
| docutils                   | 1.53 sec                                                    | 3.10 sec: 2.02x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.78 sec: 2.03x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 34.7 ms: 3.20x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x slower                                                               |

Benchmark hidden because not significant (3): json, xml_etree_parse, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.090x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown