# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 639 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 431 ms: 1.06x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 77.9 ms: 1.04x faster                                                        |
| pidigits       | 252 ms                                                       | 252 ms: 1.00x faster                                                         |
| nbody          | 89.3 ms                                                      | 97.3 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                        |
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| regex_dna      | 247 ms                                                       | 248 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse     | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| xml_etree_iterparse | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| json_loads          | 24.7 us                                                      | 23.9 us: 1.03x faster                                                        |
| tomli_loads         | 2.46 sec                                                     | 2.39 sec: 1.03x faster                                                       |
| xml_etree_generate  | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                        |
| xml_etree_process   | 61.2 ms                                                      | 60.6 ms: 1.01x faster                                                        |
| pickle_pure_python  | 323 us                                                       | 331 us: 1.02x slower                                                         |
| json_dumps          | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| genshi_xml     | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| mako           | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| deepcopy                   | 392 us                                                       | 285 us: 1.38x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.6 us: 1.31x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 639 ms: 1.30x faster                                                         |
| async_tree_io              | 843 ms                                                       | 654 ms: 1.29x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 360 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 277 ms: 1.25x faster                                                         |
| go                         | 162 ms                                                       | 133 ms: 1.22x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.6 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 524 ms: 1.15x faster                                                         |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 511 ms: 1.14x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.74 ms: 1.13x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.24 ms: 1.13x faster                                                        |
| json                       | 5.69 ms                                                      | 5.07 ms: 1.12x faster                                                        |
| scimark_fft                | 328 ms                                                       | 295 ms: 1.11x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 87.7 ms: 1.11x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.0 ms: 1.10x faster                                                        |
| pylint                     | 347 ms                                                       | 317 ms: 1.09x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.70 sec: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.44 ms: 1.08x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| pyflate                    | 503 ms                                                       | 473 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| async_generators           | 457 ms                                                       | 431 ms: 1.06x faster                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 140 ms: 1.06x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.21 ms: 1.05x faster                                                        |
| richards_super             | 59.6 ms                                                      | 56.9 ms: 1.05x faster                                                        |
| richards                   | 52.9 ms                                                      | 50.6 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 807 ms: 1.04x faster                                                         |
| thrift                     | 901 us                                                       | 862 us: 1.04x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                        |
| float                      | 81.3 ms                                                      | 77.9 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.65 sec: 1.04x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 70.8 ms: 1.04x faster                                                        |
| coverage                   | 80.0 ms                                                      | 77.3 ms: 1.04x faster                                                        |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.35 ms: 1.03x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.46 sec: 1.03x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.20 sec: 1.03x faster                                                       |
| sympy_expand               | 509 ms                                                       | 493 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                        |
| json_loads                 | 24.7 us                                                      | 23.9 us: 1.03x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 95.7 ms: 1.03x faster                                                        |
| fannkuch                   | 363 ms                                                       | 353 ms: 1.03x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.39 sec: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 57.7 ms: 1.03x faster                                                        |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                       |
| nqueens                    | 90.7 ms                                                      | 88.6 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.75 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 84.9 ms: 1.02x faster                                                        |
| raytrace                   | 273 ms                                                       | 269 ms: 1.01x faster                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 72.3 ms: 1.01x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 67.5 ms: 1.01x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 60.6 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                        |
| shortest_path              | 460 ms                                                       | 457 ms: 1.01x faster                                                         |
| pidigits                   | 252 ms                                                       | 252 ms: 1.00x faster                                                         |
| regex_dna                  | 247 ms                                                       | 248 ms: 1.00x slower                                                         |
| logging_format             | 6.94 us                                                      | 7.00 us: 1.01x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.50 ms: 1.02x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 331 us: 1.02x slower                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.03x slower                                                        |
| chaos                      | 60.2 ms                                                      | 62.0 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 101 ns: 1.03x slower                                                         |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 176 us: 1.04x slower                                                         |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| nbody                      | 89.3 ms                                                      | 97.3 ms: 1.09x slower                                                        |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.11x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.4 ms: 1.34x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.59 ms: 1.39x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.21 sec: 235.48x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (8): bench_thread_pool, logging_simple, djangocms, regex_v8, connected_components, django_template, unpickle_pure_python, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x