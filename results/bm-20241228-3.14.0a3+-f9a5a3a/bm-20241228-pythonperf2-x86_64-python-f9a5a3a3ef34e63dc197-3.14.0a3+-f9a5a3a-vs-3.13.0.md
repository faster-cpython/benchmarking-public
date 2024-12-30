# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 647 ms: 1.30x faster                                                         |
| async_tree_none            | 376 ms                                                       | 294 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| async_generators           | 457 ms                                                       | 371 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 75.2 ms: 1.08x faster                                                        |
| nbody          | 89.3 ms                                                      | 87.2 ms: 1.02x faster                                                        |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.28 ms: 1.12x faster                                                        |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| regex_dna      | 247 ms                                                       | 246 ms: 1.00x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 27.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.06x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 83.1 ms: 1.04x faster                                                        |
| json_loads           | 24.7 us                                                      | 23.8 us: 1.04x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 327 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.4 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.0 ms: 1.06x faster                                                        |
| django_template | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                        |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 332 ms: 1.40x faster                                                         |
| deepcopy                   | 392 us                                                       | 283 us: 1.39x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 632 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 647 ms: 1.30x faster                                                         |
| go                         | 162 ms                                                       | 126 ms: 1.28x faster                                                         |
| async_tree_none            | 376 ms                                                       | 294 ms: 1.28x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.3 us: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| async_generators           | 457 ms                                                       | 371 ms: 1.23x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.88 us: 1.23x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 518 ms: 1.17x faster                                                         |
| richards                   | 52.9 ms                                                      | 45.5 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| pyflate                    | 503 ms                                                       | 436 ms: 1.15x faster                                                         |
| richards_super             | 59.6 ms                                                      | 51.8 ms: 1.15x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.28 ms: 1.12x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.85 ms: 1.12x faster                                                        |
| json                       | 5.69 ms                                                      | 5.10 ms: 1.11x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.8 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 87.8 ms: 1.10x faster                                                        |
| scimark_sor                | 123 ms                                                       | 112 ms: 1.10x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                       |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.02 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 777 ms: 1.08x faster                                                         |
| float                      | 81.3 ms                                                      | 75.2 ms: 1.08x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 68.2 ms: 1.08x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.4 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.50 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.06x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 54.0 ms: 1.06x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.05x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                        |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                         |
| scimark_fft                | 328 ms                                                       | 313 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                        |
| shortest_path              | 460 ms                                                       | 441 ms: 1.04x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.5 ms: 1.04x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 83.1 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                        |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 57.1 ms: 1.04x faster                                                        |
| json_loads                 | 24.7 us                                                      | 23.8 us: 1.04x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| connected_components       | 432 ms                                                       | 418 ms: 1.04x faster                                                         |
| logging_simple             | 6.39 us                                                      | 6.18 us: 1.03x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                                       |
| fannkuch                   | 363 ms                                                       | 353 ms: 1.03x faster                                                         |
| mdp                        | 2.54 sec                                                     | 2.47 sec: 1.03x faster                                                       |
| nbody                      | 89.3 ms                                                      | 87.2 ms: 1.02x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.5 ms: 1.02x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.78 us: 1.02x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.5 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                       |
| bench_thread_pool          | 942 us                                                       | 924 us: 1.02x faster                                                         |
| sympy_str                  | 298 ms                                                       | 293 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                        |
| sympy_expand               | 509 ms                                                       | 504 ms: 1.01x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 153 ms: 1.01x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 72.9 ms: 1.01x faster                                                        |
| regex_dna                  | 247 ms                                                       | 246 ms: 1.00x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 98.8 ns: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 327 us: 1.01x slower                                                         |
| raytrace                   | 273 ms                                                       | 278 ms: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 101 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                         |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.77 ms: 1.03x slower                                                        |
| regex_v8                   | 26.1 ms                                                      | 27.0 ms: 1.03x slower                                                        |
| chaos                      | 60.2 ms                                                      | 62.7 ms: 1.04x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.05x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.9 ms: 1.31x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.35 ms: 1.34x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.97 sec: 384.24x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): dulwich_log, deltablue, asyncio_websockets, djangocms, coverage
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x