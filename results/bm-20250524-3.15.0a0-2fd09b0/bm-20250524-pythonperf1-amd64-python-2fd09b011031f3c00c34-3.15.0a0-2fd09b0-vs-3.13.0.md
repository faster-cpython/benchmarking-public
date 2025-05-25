# Results vs. 3.13.0

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.018x slower
- HPT reliability: 90.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 646 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 54.1 ms: 1.01x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.32 ms: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 37.9 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 211 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.9 ms                                                     | 18.4 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.46 ms: 1.02x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 29.8 ms: 2.53x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.4 ms: 1.66x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                      |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| float                      | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.11x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 57.3 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.44 ms: 1.07x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.7 ms: 1.06x faster                                                      |
| go                         | 84.7 ms                                                     | 80.2 ms: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                      |
| scimark_fft                | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                      |
| mako                       | 6.56 ms                                                     | 6.46 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.5 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.2 ms: 1.01x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.4 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 251 ms: 1.00x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.3 ms: 1.00x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                     |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 54.1 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.9 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.92 sec: 1.02x slower                                                     |
| sympy_expand               | 286 ms                                                      | 290 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.32 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.02x slower                                                      |
| async_generators           | 223 ms                                                      | 228 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 37.9 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 646 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.28 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 852 us: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.11 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 91.2 ms: 1.08x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.4 ms: 1.09x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.38 us: 1.10x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 543 ms: 1.12x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.93 us: 1.12x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 211 us: 1.13x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 442 us: 1.22x slower                                                       |
| raytrace                   | 153 ms                                                      | 195 ms: 1.27x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 317 ns: 5.82x slower                                                       |
| coverage                   | 45.3 ms                                                     | 296 ms: 6.53x slower                                                       |
| thrift                     | 8.47 ms                                                     | 92.7 ms: 10.95x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (9): pylint, scimark_lu, pyflate, k_core, shortest_path, python_startup, html5lib, pycparser, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250524-3.15.0a0-2fd09b0/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x slower

# HPT report

- Reliability score: 90.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown