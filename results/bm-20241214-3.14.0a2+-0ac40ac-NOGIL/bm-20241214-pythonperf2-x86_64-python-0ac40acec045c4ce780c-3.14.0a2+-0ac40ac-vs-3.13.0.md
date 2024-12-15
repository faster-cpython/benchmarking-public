# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.199x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 391 ms: 1.34x slower                                                         |
| docutils       | 2.83 sec                                                     | 3.18 sec: 1.13x slower                                                       |
| html5lib       | 73.5 ms                                                      | 97.9 ms: 1.33x slower                                                        |
| sphinx         | 1.12 sec                                                     | 1.24 sec: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.22x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 785 ms: 1.06x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 445 ms: 1.05x faster                                                         |
| async_tree_io              | 843 ms                                                       | 811 ms: 1.04x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                         |
| async_tree_none            | 376 ms                                                       | 373 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 344 ms: 1.01x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 463 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 602 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 625 ms: 1.04x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.07x slower                                                        |
| async_generators           | 457 ms                                                       | 519 ms: 1.14x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| nbody          | 89.3 ms                                                      | 137 ms: 1.53x slower                                                         |
| float          | 81.3 ms                                                      | 130 ms: 1.60x slower                                                         |
| Geometric mean | (ref)                                                        | 1.34x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.32 ms: 1.10x faster                                                        |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| regex_compile  | 143 ms                                                       | 182 ms: 1.28x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.7 ms: 1.07x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.71 sec: 1.10x slower                                                       |
| json_loads           | 24.7 us                                                      | 27.5 us: 1.12x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 102 ms: 1.18x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 14.3 ms: 1.28x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 81.2 ms: 1.33x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 330 us: 1.52x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 525 us: 1.62x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.7 ms: 1.24x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 12.3 ms: 1.37x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 69.3 ms: 1.22x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 34.0 ms: 1.30x slower                                                        |
| django_template | 36.4 ms                                                      | 54.3 ms: 1.49x slower                                                        |
| mako            | 10.4 ms                                                      | 19.3 ms: 1.86x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.88 ms: 1.22x faster                                                        |
| deepcopy                   | 392 us                                                       | 350 us: 1.12x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.32 ms: 1.10x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.7 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.72 us: 1.07x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 785 ms: 1.06x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 445 ms: 1.05x faster                                                         |
| async_tree_io              | 843 ms                                                       | 811 ms: 1.04x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 380 ms: 1.02x faster                                                         |
| pidigits                   | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| json                       | 5.69 ms                                                      | 5.59 ms: 1.02x faster                                                        |
| regex_dna                  | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| async_tree_none            | 376 ms                                                       | 373 ms: 1.01x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 344 ms: 1.01x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.6 ms: 1.01x slower                                                        |
| async_tree_memoization     | 453 ms                                                       | 463 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 602 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 625 ms: 1.04x slower                                                         |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.05x slower                                                         |
| deepcopy_memo              | 38.6 us                                                      | 40.4 us: 1.05x slower                                                        |
| scimark_fft                | 328 ms                                                       | 343 ms: 1.05x slower                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 5.45 sec: 1.07x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.07x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.81 us: 1.07x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.49 ms: 1.08x slower                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.71 sec: 1.10x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.24 sec: 1.10x slower                                                       |
| json_loads                 | 24.7 us                                                      | 27.5 us: 1.12x slower                                                        |
| k_core                     | 2.17 sec                                                     | 2.44 sec: 1.13x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.18 sec: 1.13x slower                                                       |
| async_generators           | 457 ms                                                       | 519 ms: 1.14x slower                                                         |
| pylint                     | 347 ms                                                       | 394 ms: 1.14x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.90 sec: 1.14x slower                                                       |
| generators                 | 33.6 ms                                                      | 38.6 ms: 1.15x slower                                                        |
| shortest_path              | 460 ms                                                       | 541 ms: 1.18x slower                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 102 ms: 1.18x slower                                                         |
| connected_components       | 432 ms                                                       | 510 ms: 1.18x slower                                                         |
| dulwich_log                | 68.2 ms                                                      | 81.5 ms: 1.20x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.76 ms: 1.21x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 144 ms: 1.21x slower                                                         |
| meteor_contest             | 130 ms                                                       | 157 ms: 1.21x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 110 ms: 1.21x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 69.3 ms: 1.22x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 72.2 ms: 1.22x slower                                                        |
| python_startup             | 15.9 ms                                                      | 19.7 ms: 1.24x slower                                                        |
| many_optionals             | 930 us                                                       | 1.16 ms: 1.25x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.07 sec: 1.27x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 30.0 ms: 1.27x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.59 sec: 1.28x slower                                                       |
| regex_compile              | 143 ms                                                       | 182 ms: 1.28x slower                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 23.4 ms: 1.28x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.3 ms: 1.28x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.21 sec: 1.28x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 34.0 ms: 1.30x slower                                                        |
| coverage                   | 80.0 ms                                                      | 105 ms: 1.32x slower                                                         |
| xml_etree_process          | 61.2 ms                                                      | 81.2 ms: 1.33x slower                                                        |
| html5lib                   | 73.5 ms                                                      | 97.9 ms: 1.33x slower                                                        |
| 2to3                       | 293 ms                                                       | 391 ms: 1.34x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 226 us: 1.34x slower                                                         |
| thrift                     | 901 us                                                       | 1.21 ms: 1.34x slower                                                        |
| sympy_str                  | 298 ms                                                       | 403 ms: 1.35x slower                                                         |
| pyflate                    | 503 ms                                                       | 680 ms: 1.35x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 99.6 ms: 1.36x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 12.3 ms: 1.37x slower                                                        |
| fannkuch                   | 363 ms                                                       | 509 ms: 1.40x slower                                                         |
| richards_super             | 59.6 ms                                                      | 84.1 ms: 1.41x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 210 ms: 1.41x slower                                                         |
| sympy_expand               | 509 ms                                                       | 739 ms: 1.45x slower                                                         |
| richards                   | 52.9 ms                                                      | 78.2 ms: 1.48x slower                                                        |
| logging_simple             | 6.39 us                                                      | 9.49 us: 1.48x slower                                                        |
| logging_format             | 6.94 us                                                      | 10.3 us: 1.49x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 9.76 ms: 1.49x slower                                                        |
| django_template            | 36.4 ms                                                      | 54.3 ms: 1.49x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 330 us: 1.52x slower                                                         |
| nbody                      | 89.3 ms                                                      | 137 ms: 1.53x slower                                                         |
| sympy_sum                  | 155 ms                                                       | 239 ms: 1.55x slower                                                         |
| float                      | 81.3 ms                                                      | 130 ms: 1.60x slower                                                         |
| comprehensions             | 17.0 us                                                      | 27.3 us: 1.61x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 525 us: 1.62x slower                                                         |
| go                         | 162 ms                                                       | 266 ms: 1.64x slower                                                         |
| scimark_sor                | 123 ms                                                       | 202 ms: 1.64x slower                                                         |
| chaos                      | 60.2 ms                                                      | 101 ms: 1.68x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 1.59 ms: 1.69x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 29.7 ms: 1.70x slower                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 3.04 ms: 1.70x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 174 ns: 1.78x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 179 ms: 1.82x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 121 ms: 1.84x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 2.58 ms: 1.84x slower                                                        |
| mako                       | 10.4 ms                                                      | 19.3 ms: 1.86x slower                                                        |
| raytrace                   | 273 ms                                                       | 513 ms: 1.88x slower                                                         |
| deltablue                  | 3.42 ms                                                      | 7.77 ms: 2.27x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 53.8 ms: 10.51x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.28x slower                                                                 |

Benchmark hidden because not significant (2): create_gc_cycles, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.199x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.22x