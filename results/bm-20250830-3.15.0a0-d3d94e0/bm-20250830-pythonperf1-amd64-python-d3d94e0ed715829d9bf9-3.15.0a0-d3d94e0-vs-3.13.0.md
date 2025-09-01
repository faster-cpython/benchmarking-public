# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.062x faster
- HPT reliability: 62.29%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.3 ms: 1.01x faster                                                      |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.41 ms: 1.15x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 85.4 ms: 1.08x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 135 us: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| mako            | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 484 us: 17.48x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.7 ms: 2.53x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                      |
| mdp                        | 1.43 sec                                                    | 793 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                      |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.10 ms: 1.18x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.41 ms: 1.15x faster                                                      |
| float                      | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 77.1 ms: 1.10x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 85.4 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| pylint                     | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.5 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                     |
| regex_compile              | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                      |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.3 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| sympy_expand               | 286 ms                                                      | 283 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.3 ms: 1.00x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| pyflate                    | 283 ms                                                      | 287 ms: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 495 ms: 1.02x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 64.8 ms: 1.02x slower                                                      |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.03x slower                                                     |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.4 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 78.7 ms: 1.03x slower                                                      |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| logging_silent             | 54.6 ns                                                     | 56.4 ns: 1.03x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.79 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 135 us: 1.04x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.43 us: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.5 ms: 1.04x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 846 us: 1.04x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.07 us: 1.05x slower                                                      |
| scimark_fft                | 175 ms                                                      | 184 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.5 ms: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.9 ms: 1.07x slower                                                      |
| fannkuch                   | 252 ms                                                      | 269 ms: 1.07x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.11 ms: 1.07x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 93.1 ms: 1.11x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 550 us: 1.52x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.4 ms: 2.71x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (10): html5lib, sphinx, sqlite_synth, pycparser, sympy_str, scimark_monte_carlo, sympy_sum, typing_runtime_protocols, shortest_path, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 62.29% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown