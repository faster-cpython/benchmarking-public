# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.066x faster
- HPT reliability: 82.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.2 ms: 1.18x faster                                                      |
| nbody          | 66.3 ms                                                     | 56.5 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 106 us: 1.23x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 51.3 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 94.8 ms: 1.03x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.42 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.2 ms: 1.08x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.42 ms: 1.21x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 510 us: 16.61x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 33.4 ms: 2.25x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                       |
| mdp                        | 1.43 sec                                                    | 820 ms: 1.75x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 213 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 390 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                      |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.23x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| fannkuch                   | 252 ms                                                      | 207 ms: 1.22x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.42 ms: 1.21x faster                                                      |
| float                      | 50.8 ms                                                     | 43.2 ms: 1.18x faster                                                      |
| nbody                      | 66.3 ms                                                     | 56.5 ms: 1.17x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.53 sec: 1.14x faster                                                     |
| telco                      | 4.85 ms                                                     | 4.27 ms: 1.14x faster                                                      |
| pyflate                    | 283 ms                                                      | 249 ms: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 75.1 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                       |
| scimark_fft                | 175 ms                                                      | 156 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 443 ms: 1.09x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 896 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 51.3 ms: 1.04x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.3 ms: 1.01x faster                                                      |
| shortest_path              | 355 ms                                                      | 357 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.9 ms: 1.01x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.3 ms: 1.01x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 56.1 ns: 1.03x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 94.8 ms: 1.03x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.4 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.03x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.42 ms: 1.04x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.6 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.05 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 857 us: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.2 ms: 1.06x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.1 ms: 1.06x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.2 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.2 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.7 ms: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                     |
| gc_traversal               | 1.96 ms                                                     | 2.18 ms: 1.11x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.89 us: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.1 ms: 1.13x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.53 us: 1.13x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 95.8 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                                      |
| many_optionals             | 361 us                                                      | 594 us: 1.64x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.1 ms: 2.87x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (8): pylint, scimark_monte_carlo, pycparser, pidigits, xml_etree_process, html5lib, crypto_pyaes, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 82.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown