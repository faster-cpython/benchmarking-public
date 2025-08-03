# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 627 ms: 1.35x faster                                                        |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.9 ms: 1.27x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 98.1 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| regex_dna      | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.70 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 195 us: 1.12x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 56.6 ms: 1.08x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 146 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.0 ms: 1.01x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| mako            | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                       |
| django_template | 36.4 ms                                                      | 34.8 ms: 1.05x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| richards                   | 52.9 ms                                                      | 35.6 ms: 1.49x faster                                                       |
| richards_super             | 59.6 ms                                                      | 41.2 ms: 1.45x faster                                                       |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.38x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.4 us: 1.36x faster                                                       |
| async_tree_io              | 843 ms                                                       | 627 ms: 1.35x faster                                                        |
| async_tree_none            | 376 ms                                                       | 283 ms: 1.33x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 643 ms: 1.29x faster                                                        |
| go                         | 162 ms                                                       | 128 ms: 1.27x faster                                                        |
| float                      | 81.3 ms                                                      | 63.9 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 274 ms: 1.26x faster                                                        |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 81.2 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 507 ms: 1.19x faster                                                        |
| pyflate                    | 503 ms                                                       | 423 ms: 1.19x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.88 ms: 1.19x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.49 sec: 1.16x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 729 ms: 1.16x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.2 ms: 1.15x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.7 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.1 ms: 1.13x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 195 us: 1.12x faster                                                        |
| scimark_fft                | 328 ms                                                       | 297 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.61 sec: 1.10x faster                                                      |
| html5lib                   | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                       |
| regex_dna                  | 247 ms                                                       | 227 ms: 1.09x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 56.6 ms: 1.08x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.91 us: 1.08x faster                                                       |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.01 sec: 1.08x faster                                                      |
| json                       | 5.69 ms                                                      | 5.32 ms: 1.07x faster                                                       |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.50 us: 1.07x faster                                                       |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                        |
| connected_components       | 432 ms                                                       | 406 ms: 1.06x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.79 ms: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 852 us: 1.06x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.20 ms: 1.06x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                       |
| django_template            | 36.4 ms                                                      | 34.8 ms: 1.05x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.6 ms: 1.05x faster                                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.79 us: 1.04x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 94.5 ns: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.03x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 146 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.2 ms: 1.03x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                                       |
| async_generators           | 457 ms                                                       | 448 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.0 ms: 1.01x faster                                                       |
| fannkuch                   | 363 ms                                                       | 362 ms: 1.00x faster                                                        |
| coverage                   | 80.0 ms                                                      | 79.7 ms: 1.00x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.70 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.83 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 93.3 ms: 1.03x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| raytrace                   | 273 ms                                                       | 282 ms: 1.04x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 987 us: 1.05x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 77.3 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                       |
| nbody                      | 89.3 ms                                                      | 98.1 ms: 1.10x slower                                                       |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.28 ms: 1.33x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 43.0 ms: 2.46x slower                                                       |
| telco                      | 8.79 ms                                                      | 158 ms: 17.97x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.38 sec: 270.21x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): pycparser, djangocms
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x