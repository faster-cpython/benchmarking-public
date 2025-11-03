# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 64.4 ms: 1.14x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.07 sec: 1.05x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 376 ms                                                       | 248 ms: 1.52x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 306 ms: 1.48x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 315 ms: 1.48x faster                                                         |
| async_tree_io              | 843 ms                                                       | 578 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 576 ms: 1.44x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 255 ms: 1.36x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 476 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 480 ms: 1.21x faster                                                         |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 411 ms: 1.06x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 22.9 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 65.3 ms: 1.24x faster                                                        |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 92.7 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                        |
| regex_dna      | 247 ms                                                       | 228 ms: 1.08x faster                                                         |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                         |
| regex_effbot   | 3.67 ms                                                      | 3.51 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 85.4 ms: 1.20x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 133 ms: 1.13x faster                                                         |
| unpickle_pure_python | 217 us                                                       | 194 us: 1.12x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 55.4 ms: 1.10x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 78.7 ms: 1.10x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 329 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.0 ms: 1.06x faster                                                        |
| python_startup_no_site | 8.96 ms                                                      | 8.74 ms: 1.02x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                        |
| mako            | 10.4 ms                                                      | 9.74 ms: 1.07x faster                                                        |
| django_template | 36.4 ms                                                      | 34.8 ms: 1.05x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 56.1 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 2.00x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 24.0 us: 1.61x faster                                                        |
| async_tree_none            | 376 ms                                                       | 248 ms: 1.52x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 306 ms: 1.48x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 315 ms: 1.48x faster                                                         |
| deepcopy                   | 392 us                                                       | 267 us: 1.47x faster                                                         |
| async_tree_io              | 843 ms                                                       | 578 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 576 ms: 1.44x faster                                                         |
| richards                   | 52.9 ms                                                      | 37.9 ms: 1.40x faster                                                        |
| go                         | 162 ms                                                       | 119 ms: 1.36x faster                                                         |
| richards_super             | 59.6 ms                                                      | 43.8 ms: 1.36x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 255 ms: 1.36x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                       |
| pyflate                    | 503 ms                                                       | 394 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 476 ms: 1.27x faster                                                         |
| float                      | 81.3 ms                                                      | 65.3 ms: 1.24x faster                                                        |
| scimark_sor                | 123 ms                                                       | 100 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 480 ms: 1.21x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 85.4 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                        |
| scimark_fft                | 328 ms                                                       | 276 ms: 1.19x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.46 sec: 1.17x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.1 ms: 1.16x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 83.7 ms: 1.16x faster                                                        |
| k_core                     | 2.17 sec                                                     | 1.87 sec: 1.16x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 730 ms: 1.15x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 59.3 ms: 1.15x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.4 ms: 1.14x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 64.4 ms: 1.14x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 133 ms: 1.13x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 194 us: 1.12x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 5.88 ms: 1.11x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.5 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.4 ms: 1.10x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.62 sec: 1.10x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 78.7 ms: 1.10x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                        |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.10x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.86 us: 1.09x faster                                                        |
| regex_dna                  | 247 ms                                                       | 228 ms: 1.08x faster                                                         |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                         |
| logging_format             | 6.94 us                                                      | 6.44 us: 1.08x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.6 ms: 1.07x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.20 ms: 1.07x faster                                                        |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.74 ms: 1.07x faster                                                        |
| thrift                     | 901 us                                                       | 848 us: 1.06x faster                                                         |
| connected_components       | 432 ms                                                       | 408 ms: 1.06x faster                                                         |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                         |
| python_startup             | 15.9 ms                                                      | 15.0 ms: 1.06x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.3 ms: 1.06x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 93.0 ns: 1.05x faster                                                        |
| chaos                      | 60.2 ms                                                      | 57.4 ms: 1.05x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.07 sec: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.44 ms: 1.05x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.51 ms: 1.05x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.8 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 280 ms: 1.04x faster                                                         |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                         |
| async_generators           | 457 ms                                                       | 444 ms: 1.03x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 96.2 ms: 1.03x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.74 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                         |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                         |
| sympy_expand               | 509 ms                                                       | 500 ms: 1.02x faster                                                         |
| coverage                   | 80.0 ms                                                      | 78.5 ms: 1.02x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 56.1 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.74 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 91.9 ms: 1.01x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 329 us: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 173 us: 1.02x slower                                                         |
| fannkuch                   | 363 ms                                                       | 375 ms: 1.03x slower                                                         |
| nbody                      | 89.3 ms                                                      | 92.7 ms: 1.04x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 76.8 ms: 1.05x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 411 ms: 1.06x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 22.9 ms: 1.06x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.94 ms: 1.09x slower                                                        |
| many_optionals             | 930 us                                                       | 1.19 ms: 1.28x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.88 ms: 1.45x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 44.1 ms: 2.52x slower                                                        |
| telco                      | 8.79 ms                                                      | 156 ms: 17.73x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.33 sec: 260.40x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (4): raytrace, comprehensions, djangocms, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f-JIT/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x