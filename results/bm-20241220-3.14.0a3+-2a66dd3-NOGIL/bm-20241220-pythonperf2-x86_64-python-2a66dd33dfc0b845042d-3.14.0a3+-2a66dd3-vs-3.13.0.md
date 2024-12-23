# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.174x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 386 ms: 1.32x slower                                                         |
| docutils       | 2.83 sec                                                     | 3.12 sec: 1.10x slower                                                       |
| html5lib       | 73.5 ms                                                      | 93.1 ms: 1.27x slower                                                        |
| sphinx         | 1.12 sec                                                     | 1.23 sec: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 413 ms: 1.13x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 745 ms: 1.12x faster                                                         |
| async_tree_io              | 843 ms                                                       | 783 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 322 ms: 1.08x faster                                                         |
| async_tree_none            | 376 ms                                                       | 360 ms: 1.05x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 378 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 577 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 610 ms: 1.01x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                        |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| float          | 81.3 ms                                                      | 108 ms: 1.33x slower                                                         |
| nbody          | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| Geometric mean | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.29 ms: 1.12x faster                                                        |
| regex_dna      | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| regex_compile  | 143 ms                                                       | 173 ms: 1.22x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 92.5 ms: 1.11x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.62 sec: 1.06x slower                                                       |
| json_loads           | 24.7 us                                                      | 27.6 us: 1.12x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 75.7 ms: 1.24x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.3 ms: 1.28x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 321 us: 1.48x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 506 us: 1.57x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.17x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.6 ms: 1.24x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 12.2 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 69.4 ms: 1.22x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 33.6 ms: 1.28x slower                                                        |
| django_template | 36.4 ms                                                      | 53.9 ms: 1.48x slower                                                        |
| mako            | 10.4 ms                                                      | 19.6 ms: 1.89x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.45x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.87 ms: 1.23x faster                                                        |
| deepcopy                   | 392 us                                                       | 343 us: 1.14x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 413 ms: 1.13x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.29 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 745 ms: 1.12x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 92.5 ms: 1.11x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.67 us: 1.09x faster                                                        |
| async_tree_io              | 843 ms                                                       | 783 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 322 ms: 1.08x faster                                                         |
| async_tree_none            | 376 ms                                                       | 360 ms: 1.05x faster                                                         |
| json                       | 5.69 ms                                                      | 5.47 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 378 ms: 1.03x faster                                                         |
| pidigits                   | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| regex_dna                  | 247 ms                                                       | 242 ms: 1.02x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.3 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 577 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 610 ms: 1.01x slower                                                         |
| deepcopy_memo              | 38.6 us                                                      | 39.4 us: 1.02x slower                                                        |
| scimark_fft                | 328 ms                                                       | 341 ms: 1.04x slower                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 3.70 us: 1.05x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 102 ms: 1.06x slower                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.62 sec: 1.06x slower                                                       |
| telco                      | 8.79 ms                                                      | 9.42 ms: 1.07x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 23.1 ms: 1.07x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.53 sec: 1.09x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.23 sec: 1.10x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.12 sec: 1.10x slower                                                       |
| pylint                     | 347 ms                                                       | 386 ms: 1.11x slower                                                         |
| json_loads                 | 24.7 us                                                      | 27.6 us: 1.12x slower                                                        |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                         |
| k_core                     | 2.17 sec                                                     | 2.45 sec: 1.13x slower                                                       |
| mdp                        | 2.54 sec                                                     | 2.88 sec: 1.13x slower                                                       |
| generators                 | 33.6 ms                                                      | 38.6 ms: 1.15x slower                                                        |
| dulwich_log                | 68.2 ms                                                      | 78.4 ms: 1.15x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 99.6 ms: 1.15x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.46 sec: 1.17x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.60 ms: 1.17x slower                                                        |
| shortest_path              | 460 ms                                                       | 541 ms: 1.18x slower                                                         |
| connected_components       | 432 ms                                                       | 510 ms: 1.18x slower                                                         |
| regex_compile              | 143 ms                                                       | 173 ms: 1.22x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 69.4 ms: 1.22x slower                                                        |
| meteor_contest             | 130 ms                                                       | 158 ms: 1.22x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 146 ms: 1.22x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 72.5 ms: 1.22x slower                                                        |
| thrift                     | 901 us                                                       | 1.11 ms: 1.23x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 1.03 sec: 1.23x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.23x slower                                                         |
| python_startup             | 15.9 ms                                                      | 19.6 ms: 1.24x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 75.7 ms: 1.24x slower                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 22.6 ms: 1.24x slower                                                        |
| many_optionals             | 930 us                                                       | 1.15 ms: 1.24x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.17 sec: 1.26x slower                                                       |
| html5lib                   | 73.5 ms                                                      | 93.1 ms: 1.27x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 33.6 ms: 1.28x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 30.2 ms: 1.28x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.3 ms: 1.28x slower                                                        |
| pyflate                    | 503 ms                                                       | 646 ms: 1.28x slower                                                         |
| 2to3                       | 293 ms                                                       | 386 ms: 1.32x slower                                                         |
| richards_super             | 59.6 ms                                                      | 78.9 ms: 1.33x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 224 us: 1.33x slower                                                         |
| float                      | 81.3 ms                                                      | 108 ms: 1.33x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 98.6 ms: 1.35x slower                                                        |
| richards                   | 52.9 ms                                                      | 71.3 ms: 1.35x slower                                                        |
| coverage                   | 80.0 ms                                                      | 108 ms: 1.35x slower                                                         |
| sympy_str                  | 298 ms                                                       | 403 ms: 1.35x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 12.2 ms: 1.36x slower                                                        |
| fannkuch                   | 363 ms                                                       | 497 ms: 1.37x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 135 ms: 1.37x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 204 ms: 1.37x slower                                                         |
| logging_simple             | 6.39 us                                                      | 8.79 us: 1.37x slower                                                        |
| logging_format             | 6.94 us                                                      | 9.71 us: 1.40x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 9.31 ms: 1.42x slower                                                        |
| sympy_expand               | 509 ms                                                       | 734 ms: 1.44x slower                                                         |
| nbody                      | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 321 us: 1.48x slower                                                         |
| django_template            | 36.4 ms                                                      | 53.9 ms: 1.48x slower                                                        |
| go                         | 162 ms                                                       | 244 ms: 1.50x slower                                                         |
| sympy_sum                  | 155 ms                                                       | 240 ms: 1.55x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 506 us: 1.57x slower                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 2.82 ms: 1.58x slower                                                        |
| chaos                      | 60.2 ms                                                      | 95.2 ms: 1.58x slower                                                        |
| scimark_sor                | 123 ms                                                       | 195 ms: 1.59x slower                                                         |
| comprehensions             | 17.0 us                                                      | 27.1 us: 1.59x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 107 ms: 1.62x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 28.3 ms: 1.62x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.55 ms: 1.65x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 162 ns: 1.66x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 2.37 ms: 1.70x slower                                                        |
| raytrace                   | 273 ms                                                       | 480 ms: 1.76x slower                                                         |
| mako                       | 10.4 ms                                                      | 19.6 ms: 1.89x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 7.15 ms: 2.09x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 53.7 ms: 10.48x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.24x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_memoization, create_gc_cycles, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.174x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.22x