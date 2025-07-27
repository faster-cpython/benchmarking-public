# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.033x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 349 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.3 ms: 1.02x faster                                                      |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 82.8 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 140 us: 1.07x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 66.4 ms: 1.10x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 59.1 ms: 1.10x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 219 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| mako            | 6.56 ms                                                     | 6.82 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 523 us: 16.20x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.6 ms: 2.31x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| mdp                        | 1.43 sec                                                    | 816 ms: 1.75x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                       |
| deepcopy                   | 223 us                                                      | 174 us: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_none            | 219 ms                                                      | 177 ms: 1.24x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.7 us: 1.23x faster                                                      |
| float                      | 50.8 ms                                                     | 43.3 ms: 1.17x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 174 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 349 ms: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.90 us: 1.06x faster                                                      |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.69 ms: 1.04x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.6 ms: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.0 ms: 1.02x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.3 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.58 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.9 ms: 1.00x slower                                                      |
| sympy_expand               | 286 ms                                                      | 287 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.4 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 77.3 ms: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 82.8 ms: 1.03x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.82 ms: 1.04x slower                                                      |
| pycparser                  | 695 ms                                                      | 723 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                       |
| pyflate                    | 283 ms                                                      | 295 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.04x slower                                                     |
| sympy_str                  | 167 ms                                                      | 174 ms: 1.04x slower                                                       |
| scimark_fft                | 175 ms                                                      | 183 ms: 1.05x slower                                                       |
| fannkuch                   | 252 ms                                                      | 264 ms: 1.05x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.03 sec: 1.05x slower                                                     |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.6 ns: 1.06x slower                                                      |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 515 ms: 1.06x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.58 us: 1.07x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 864 us: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.18 us: 1.07x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 140 us: 1.07x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.08x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 49.4 ms: 1.08x slower                                                      |
| richards                   | 26.3 ms                                                     | 28.7 ms: 1.09x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 66.4 ms: 1.10x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.23 ms: 1.10x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 59.1 ms: 1.10x slower                                                      |
| python_startup             | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.3 ms: 1.12x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.9 ms: 1.14x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 96.6 ms: 1.15x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 65.2 ms: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 219 us: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.1 ms: 1.19x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                      |
| raytrace                   | 153 ms                                                      | 187 ms: 1.22x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.2 ms: 1.24x slower                                                      |
| many_optionals             | 361 us                                                      | 573 us: 1.59x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.2 ms: 2.78x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (5): pylint, sqlite_synth, json_dumps, k_core, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown