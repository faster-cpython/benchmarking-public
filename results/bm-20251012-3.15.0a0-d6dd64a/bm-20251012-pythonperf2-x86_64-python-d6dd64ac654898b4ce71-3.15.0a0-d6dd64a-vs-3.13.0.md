# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 278 ms: 1.05x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                      |
| html5lib       | 73.5 ms                                                      | 64.0 ms: 1.15x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.9 ms: 1.18x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 220 ms: 1.12x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.32 ms: 1.11x faster                                                       |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.8 ms: 1.04x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 329 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.5 ms: 1.07x faster                                                       |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 2.00x faster                                                      |
| deepcopy_memo              | 38.6 us                                                      | 25.3 us: 1.53x faster                                                       |
| deepcopy                   | 392 us                                                       | 267 us: 1.47x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                        |
| go                         | 162 ms                                                       | 117 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 328 ms: 1.38x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 634 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 270 ms: 1.28x faster                                                        |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 501 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                                       |
| richards                   | 52.9 ms                                                      | 44.4 ms: 1.19x faster                                                       |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.19x faster                                                        |
| richards_super             | 59.6 ms                                                      | 50.2 ms: 1.19x faster                                                       |
| scimark_fft                | 328 ms                                                       | 276 ms: 1.19x faster                                                        |
| float                      | 81.3 ms                                                      | 68.9 ms: 1.18x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 59.3 ms: 1.15x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 64.0 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.4 ms: 1.14x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 85.4 ms: 1.14x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.77 ms: 1.14x faster                                                       |
| regex_dna                  | 247 ms                                                       | 220 ms: 1.12x faster                                                        |
| generators                 | 33.6 ms                                                      | 30.2 ms: 1.11x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.32 ms: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.56 sec: 1.10x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 769 ms: 1.10x faster                                                        |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                        |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.89 us: 1.08x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.0 ms: 1.08x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 21.8 ms: 1.08x faster                                                       |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.17 ms: 1.08x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 24.3 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.74 sec: 1.07x faster                                                      |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                        |
| comprehensions             | 17.0 us                                                      | 15.9 us: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.47 ms: 1.07x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.51 us: 1.07x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.5 ms: 1.07x faster                                                       |
| json                       | 5.69 ms                                                      | 5.34 ms: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 847 us: 1.06x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 58.0 ms: 1.05x faster                                                       |
| 2to3                       | 293 ms                                                       | 278 ms: 1.05x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| sympy_expand               | 509 ms                                                       | 486 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 82.8 ms: 1.04x faster                                                       |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                        |
| chaos                      | 60.2 ms                                                      | 57.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 98.8 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| logging_silent             | 97.9 ns                                                      | 94.1 ns: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 96.1 ms: 1.03x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                      |
| connected_components       | 432 ms                                                       | 422 ms: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.85 us: 1.02x faster                                                       |
| typing_runtime_protocols   | 169 us                                                       | 166 us: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.81 ms: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 455 ms: 1.01x faster                                                        |
| fannkuch                   | 363 ms                                                       | 359 ms: 1.01x faster                                                        |
| docutils                   | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                      |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 92.1 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 329 us: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 75.5 ms: 1.03x slower                                                       |
| raytrace                   | 273 ms                                                       | 283 ms: 1.04x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.87 ms: 1.07x slower                                                       |
| coverage                   | 80.0 ms                                                      | 87.4 ms: 1.09x slower                                                       |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.49 ms: 1.37x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 44.7 ms: 2.56x slower                                                       |
| telco                      | 8.79 ms                                                      | 154 ms: 17.57x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.98 sec: 386.19x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (4): bench_thread_pool, djangocms, asyncio_websockets, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x