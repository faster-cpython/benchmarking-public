# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 276 ms: 1.06x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                       |
| html5lib       | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 296 ms: 1.58x faster                                                         |
| async_tree_none            | 376 ms                                                       | 243 ms: 1.55x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 301 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 558 ms: 1.49x faster                                                         |
| async_tree_io              | 843 ms                                                       | 568 ms: 1.48x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 249 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 474 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 476 ms: 1.22x faster                                                         |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 409 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 64.8 ms: 1.26x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                         |
| regex_effbot   | 3.67 ms                                                      | 3.48 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.97 sec: 1.25x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 86.2 ms: 1.19x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 81.1 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 57.4 ms: 1.07x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.06x faster                                                         |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.0 ms: 1.06x faster                                                        |
| python_startup_no_site | 8.96 ms                                                      | 8.67 ms: 1.03x faster                                                        |
| Geometric mean         | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.8 ms: 1.15x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.2 ms: 1.07x faster                                                        |
| django_template | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                        |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.25 sec: 2.03x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 296 ms: 1.58x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 24.9 us: 1.55x faster                                                        |
| async_tree_none            | 376 ms                                                       | 243 ms: 1.55x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 301 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 558 ms: 1.49x faster                                                         |
| deepcopy                   | 392 us                                                       | 264 us: 1.48x faster                                                         |
| async_tree_io              | 843 ms                                                       | 568 ms: 1.48x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 249 ms: 1.39x faster                                                         |
| go                         | 162 ms                                                       | 118 ms: 1.38x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 474 ms: 1.27x faster                                                         |
| float                      | 81.3 ms                                                      | 64.8 ms: 1.26x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.97 sec: 1.25x faster                                                       |
| scimark_sor                | 123 ms                                                       | 98.6 ms: 1.25x faster                                                        |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.90 us: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 476 ms: 1.22x faster                                                         |
| richards                   | 52.9 ms                                                      | 44.2 ms: 1.20x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 86.2 ms: 1.19x faster                                                        |
| richards_super             | 59.6 ms                                                      | 50.1 ms: 1.19x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 14.8 ms: 1.18x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 82.9 ms: 1.17x faster                                                        |
| scimark_fft                | 328 ms                                                       | 281 ms: 1.17x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 59.0 ms: 1.16x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 5.67 ms: 1.15x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 22.8 ms: 1.15x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 64.7 ms: 1.14x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.8 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 59.1 ms: 1.12x faster                                                        |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                         |
| k_core                     | 2.17 sec                                                     | 1.95 sec: 1.11x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.10x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.12 ms: 1.09x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 771 ms: 1.09x faster                                                         |
| meteor_contest             | 130 ms                                                       | 119 ms: 1.09x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.90 us: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                         |
| chaos                      | 60.2 ms                                                      | 55.7 ms: 1.08x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 91.6 ms: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 323 ms: 1.07x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 21.9 ms: 1.07x faster                                                        |
| async_generators           | 457 ms                                                       | 426 ms: 1.07x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 53.2 ms: 1.07x faster                                                        |
| thrift                     | 901 us                                                       | 841 us: 1.07x faster                                                         |
| logging_format             | 6.94 us                                                      | 6.49 us: 1.07x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 81.1 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.4 ms: 1.07x faster                                                        |
| json                       | 5.69 ms                                                      | 5.34 ms: 1.07x faster                                                        |
| python_startup             | 15.9 ms                                                      | 15.0 ms: 1.06x faster                                                        |
| 2to3                       | 293 ms                                                       | 276 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.49 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.06x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.06 sec: 1.06x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.48 ms: 1.06x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 93.0 ns: 1.05x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.2 us: 1.05x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                         |
| sympy_expand               | 509 ms                                                       | 490 ms: 1.04x faster                                                         |
| sympy_str                  | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 8.67 ms: 1.03x faster                                                        |
| connected_components       | 432 ms                                                       | 422 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| raytrace                   | 273 ms                                                       | 268 ms: 1.02x faster                                                         |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| fannkuch                   | 363 ms                                                       | 358 ms: 1.01x faster                                                         |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                         |
| docutils                   | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 91.7 ms: 1.01x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 74.9 ms: 1.02x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.4 ms: 1.04x slower                                                        |
| asyncio_websockets         | 388 ms                                                       | 409 ms: 1.05x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.86 ms: 1.07x slower                                                        |
| many_optionals             | 930 us                                                       | 1.19 ms: 1.28x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.14 ms: 1.29x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 44.4 ms: 2.54x slower                                                        |
| telco                      | 8.79 ms                                                      | 152 ms: 17.31x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 2.57 sec: 501.15x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (5): bench_thread_pool, pickle_pure_python, coverage, djangocms, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x