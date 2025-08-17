# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.095x faster
- HPT reliability: 99.42%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 626 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 57.5 ms: 1.15x faster                                                      |
| pidigits       | 146 ms                                                      | 143 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.75x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| json_dumps           | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 85.3 ms: 1.08x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.8 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 200 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.28 ms: 1.24x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 491 us: 17.26x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.2 ms: 2.58x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 163 ms: 1.84x faster                                                       |
| mdp                        | 1.43 sec                                                    | 809 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.75x faster                                                      |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 380 ms: 1.31x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                      |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.28 ms: 1.24x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| telco                      | 4.85 ms                                                     | 3.96 ms: 1.23x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                       |
| fannkuch                   | 252 ms                                                      | 211 ms: 1.19x faster                                                       |
| scimark_fft                | 175 ms                                                      | 149 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.24 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| nbody                      | 66.3 ms                                                     | 57.5 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| json                       | 3.30 ms                                                     | 2.90 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 435 ms: 1.11x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 884 ms: 1.10x faster                                                       |
| go                         | 84.7 ms                                                     | 76.7 ms: 1.10x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 85.3 ms: 1.08x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.0 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.07x faster                                                      |
| pyflate                    | 283 ms                                                      | 265 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.60 ms: 1.06x faster                                                      |
| pylint                     | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.52 us: 1.05x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 69.1 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.3 ms: 1.03x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.0 ms: 1.03x faster                                                      |
| pidigits                   | 146 ms                                                      | 143 ms: 1.02x faster                                                       |
| connected_components       | 320 ms                                                      | 313 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 44.9 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.3 ms: 1.01x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 63.1 ms: 1.01x faster                                                      |
| sympy_sum                  | 85.2 ms                                                     | 85.6 ms: 1.00x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 54.9 ns: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                       |
| sphinx                     | 617 ms                                                      | 626 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.7 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.8 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 829 us: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.6 ms: 1.03x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.1 ms: 1.03x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.45 us: 1.04x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 79.6 ms: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.7 ms: 1.05x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.15 us: 1.06x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.4 ms: 1.07x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 200 us: 1.08x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.9 ms: 1.08x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 92.4 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 559 us: 1.55x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.0 ms: 2.76x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (4): pycparser, typing_runtime_protocols, html5lib, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a-JIT/bm-20250816-pythonperf1-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 99.42% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown