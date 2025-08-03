# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 65.1 ms: 1.13x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                        |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 640 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                        |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 92.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 219 ms: 1.13x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                       |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.54 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 331 us: 1.03x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.1 ms: 1.07x faster                                                       |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                       |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| deepcopy                   | 392 us                                                       | 271 us: 1.45x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.4 us: 1.41x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| go                         | 162 ms                                                       | 118 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 278 ms: 1.35x faster                                                        |
| async_tree_io              | 843 ms                                                       | 628 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 640 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 502 ms: 1.20x faster                                                        |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.20x faster                                                        |
| float                      | 81.3 ms                                                      | 67.7 ms: 1.20x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                       |
| pyflate                    | 503 ms                                                       | 424 ms: 1.19x faster                                                        |
| richards                   | 52.9 ms                                                      | 44.9 ms: 1.18x faster                                                       |
| richards_super             | 59.6 ms                                                      | 50.8 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 503 ms: 1.16x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 59.5 ms: 1.15x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 85.8 ms: 1.13x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 65.1 ms: 1.13x faster                                                       |
| regex_dna                  | 247 ms                                                       | 219 ms: 1.13x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.54 sec: 1.12x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 760 ms: 1.11x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.01 ms: 1.09x faster                                                       |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.15 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.08x faster                                                      |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                                        |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 53.1 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.6 ms: 1.07x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.0 ms: 1.07x faster                                                       |
| scimark_fft                | 328 ms                                                       | 306 ms: 1.07x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.98 us: 1.07x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 142 ms: 1.06x faster                                                        |
| json                       | 5.69 ms                                                      | 5.37 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 93.3 ms: 1.06x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 92.7 ns: 1.06x faster                                                       |
| comprehensions             | 17.0 us                                                      | 16.2 us: 1.05x faster                                                       |
| sympy_expand               | 509 ms                                                       | 484 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.61 us: 1.05x faster                                                       |
| sympy_str                  | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.07 sec: 1.05x faster                                                      |
| connected_components       | 432 ms                                                       | 413 ms: 1.05x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 280 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 867 us: 1.04x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.0 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.54 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| python_startup             | 15.9 ms                                                      | 15.4 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 165 us: 1.02x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.85 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.70 ms: 1.01x faster                                                       |
| raytrace                   | 273 ms                                                       | 275 ms: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 91.9 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.03x slower                                                       |
| coverage                   | 80.0 ms                                                      | 82.0 ms: 1.03x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 331 us: 1.03x slower                                                        |
| nbody                      | 89.3 ms                                                      | 92.0 ms: 1.03x slower                                                       |
| fannkuch                   | 363 ms                                                       | 375 ms: 1.03x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 973 us: 1.03x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 76.6 ms: 1.05x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.4 us: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.93 ms: 1.09x slower                                                       |
| many_optionals             | 930 us                                                       | 1.21 ms: 1.30x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.67 ms: 1.41x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 42.6 ms: 2.44x slower                                                       |
| telco                      | 8.79 ms                                                      | 161 ms: 18.30x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.37 sec: 267.88x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (3): djangocms, json_dumps, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x