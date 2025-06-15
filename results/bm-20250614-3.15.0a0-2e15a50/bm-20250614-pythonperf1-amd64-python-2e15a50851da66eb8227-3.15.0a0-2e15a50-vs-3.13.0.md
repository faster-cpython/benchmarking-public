# Results vs. 3.13.0

- fork: python
- ref: 2e15a50851da66eb8227
- machine: windows-amd64
- commit hash: 2e15a50
- commit date: 2025-06-14
- overall geometric mean: 1.324x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 296 ms: 1.38x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.10 sec: 1.37x slower                                                     |
| html5lib       | 38.2 ms                                                     | 51.2 ms: 1.34x slower                                                      |
| sphinx         | 617 ms                                                      | 846 ms: 1.37x slower                                                       |
| Geometric mean | (ref)                                                       | 1.36x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 294 ms: 1.05x slower                                                       |
| async_tree_io              | 513 ms                                                      | 547 ms: 1.07x slower                                                       |
| async_tree_none            | 219 ms                                                      | 243 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 296 ms: 1.12x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 566 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 437 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 442 ms: 1.16x slower                                                       |
| async_tree_none_tg         | 200 ms                                                      | 237 ms: 1.19x slower                                                       |
| async_generators           | 223 ms                                                      | 341 ms: 1.53x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 26.1 ms: 2.08x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 76.8 ms: 1.51x slower                                                      |
| nbody          | 66.3 ms                                                     | 107 ms: 1.61x slower                                                       |
| Geometric mean | (ref)                                                       | 1.35x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| regex_compile  | 80.7 ms                                                     | 124 ms: 1.53x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| json_loads           | 15.1 us                                                     | 20.5 us: 1.36x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 8.45 ms: 1.37x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 91.6 ms: 1.51x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.08 sec: 1.52x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 91.2 ms: 1.71x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 65.7 ms: 1.80x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 363 us: 1.95x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 279 us: 2.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.59x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 50.0 ms: 1.48x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 24.3 ms: 1.60x slower                                                      |
| django_template | 20.3 ms                                                     | 37.3 ms: 1.84x slower                                                      |
| mako            | 6.56 ms                                                     | 13.1 ms: 1.99x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.71x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 34.3 ms: 2.19x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 17.0 ms: 1.40x faster                                                      |
| mdp                        | 1.43 sec                                                    | 1.17 sec: 1.22x faster                                                     |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.73 ms: 1.02x slower                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 294 ms: 1.05x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.81 sec: 1.07x slower                                                     |
| async_tree_io              | 513 ms                                                      | 547 ms: 1.07x slower                                                       |
| shortest_path              | 355 ms                                                      | 383 ms: 1.08x slower                                                       |
| connected_components       | 320 ms                                                      | 351 ms: 1.10x slower                                                       |
| python_startup             | 24.4 ms                                                     | 27.0 ms: 1.11x slower                                                      |
| async_tree_none            | 219 ms                                                      | 243 ms: 1.11x slower                                                       |
| async_tree_memoization     | 265 ms                                                      | 296 ms: 1.12x slower                                                       |
| async_tree_io_tg           | 497 ms                                                      | 566 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 437 ms: 1.14x slower                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 442 ms: 1.16x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.85 us: 1.17x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 108 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.45 ms: 1.18x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 20.0 ms: 1.18x slower                                                      |
| async_tree_none_tg         | 200 ms                                                      | 237 ms: 1.19x slower                                                       |
| deepcopy                   | 223 us                                                      | 267 us: 1.19x slower                                                       |
| pylint                     | 205 ms                                                      | 248 ms: 1.21x slower                                                       |
| json                       | 3.30 ms                                                     | 4.01 ms: 1.22x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 104 ms: 1.24x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.01 ms: 1.24x slower                                                      |
| telco                      | 4.85 ms                                                     | 6.26 ms: 1.29x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 93.2 ms: 1.29x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 52.1 ms: 1.30x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 51.2 ms: 1.34x slower                                                      |
| json_loads                 | 15.1 us                                                     | 20.5 us: 1.36x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 16.7 ms: 1.36x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 116 ms: 1.36x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 8.45 ms: 1.37x slower                                                      |
| sphinx                     | 617 ms                                                      | 846 ms: 1.37x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.10 sec: 1.37x slower                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 2.78 us: 1.38x slower                                                      |
| 2to3                       | 215 ms                                                      | 296 ms: 1.38x slower                                                       |
| sympy_str                  | 167 ms                                                      | 234 ms: 1.40x slower                                                       |
| sympy_expand               | 286 ms                                                      | 402 ms: 1.41x slower                                                       |
| pycparser                  | 695 ms                                                      | 988 ms: 1.42x slower                                                       |
| deepcopy_memo              | 23.1 us                                                     | 33.6 us: 1.46x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 50.0 ms: 1.48x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.93 ms: 1.49x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 155 us: 1.51x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 4.33 sec: 1.51x slower                                                     |
| float                      | 50.8 ms                                                     | 76.8 ms: 1.51x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 91.6 ms: 1.51x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.08 sec: 1.52x slower                                                     |
| async_generators           | 223 ms                                                      | 341 ms: 1.53x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 124 ms: 1.53x slower                                                       |
| many_optionals             | 361 us                                                      | 556 us: 1.54x slower                                                       |
| go                         | 84.7 ms                                                     | 134 ms: 1.58x slower                                                       |
| scimark_fft                | 175 ms                                                      | 277 ms: 1.58x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 24.3 ms: 1.60x slower                                                      |
| logging_format             | 6.18 us                                                     | 9.91 us: 1.60x slower                                                      |
| nbody                      | 66.3 ms                                                     | 107 ms: 1.61x slower                                                       |
| logging_simple             | 5.77 us                                                     | 9.42 us: 1.63x slower                                                      |
| pyflate                    | 283 ms                                                      | 462 ms: 1.63x slower                                                       |
| fannkuch                   | 252 ms                                                      | 413 ms: 1.64x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 94.5 ms: 1.68x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 4.41 ms: 1.69x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 91.2 ms: 1.71x slower                                                      |
| chaos                      | 37.9 ms                                                     | 65.8 ms: 1.74x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 79.8 ms: 1.75x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 133 ms: 1.75x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 111 ms: 1.75x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 856 ms: 1.77x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.76 sec: 1.80x slower                                                     |
| xml_etree_process          | 36.5 ms                                                     | 65.7 ms: 1.80x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 73.9 ms: 1.81x slower                                                      |
| django_template            | 20.3 ms                                                     | 37.3 ms: 1.84x slower                                                      |
| comprehensions             | 10.4 us                                                     | 19.8 us: 1.91x slower                                                      |
| generators                 | 19.0 ms                                                     | 36.4 ms: 1.92x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 7.46 ms: 1.94x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 363 us: 1.95x slower                                                       |
| richards_super             | 29.8 ms                                                     | 58.7 ms: 1.97x slower                                                      |
| raytrace                   | 153 ms                                                      | 303 ms: 1.97x slower                                                       |
| mako                       | 6.56 ms                                                     | 13.1 ms: 1.99x slower                                                      |
| richards                   | 26.3 ms                                                     | 52.3 ms: 1.99x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 26.1 ms: 2.08x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 22.8 ms: 2.10x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 120 ms: 2.12x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 279 us: 2.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 4.38 ms: 2.31x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 501 ns: 9.19x slower                                                       |
| coverage                   | 45.3 ms                                                     | 471 ms: 10.40x slower                                                      |
| thrift                     | 8.47 ms                                                     | 103 ms: 12.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.51x slower                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250614-3.15.0a0-2e15a50/bm-20250614-pythonperf1-amd64-python-2e15a50851da66eb8227-3.15.0a0-2e15a50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.324x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: unknown