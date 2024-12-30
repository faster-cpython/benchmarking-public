# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-x86_64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.166x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 382 ms: 1.30x slower                                                         |
| docutils       | 2.83 sec                                                     | 3.11 sec: 1.10x slower                                                       |
| html5lib       | 73.5 ms                                                      | 93.1 ms: 1.27x slower                                                        |
| sphinx         | 1.12 sec                                                     | 1.23 sec: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 407 ms: 1.14x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 740 ms: 1.12x faster                                                         |
| async_tree_io              | 843 ms                                                       | 774 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 319 ms: 1.09x faster                                                         |
| async_tree_none            | 376 ms                                                       | 354 ms: 1.06x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 440 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 574 ms: 1.01x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 608 ms: 1.01x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.07x slower                                                        |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| float          | 81.3 ms                                                      | 109 ms: 1.34x slower                                                         |
| nbody          | 89.3 ms                                                      | 130 ms: 1.46x slower                                                         |
| Geometric mean | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.30 ms: 1.11x faster                                                        |
| regex_dna      | 247 ms                                                       | 248 ms: 1.00x slower                                                         |
| regex_compile  | 143 ms                                                       | 173 ms: 1.21x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 93.6 ms: 1.10x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.61 sec: 1.06x slower                                                       |
| json_loads           | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 98.6 ms: 1.14x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 74.7 ms: 1.22x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 323 us: 1.49x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 506 us: 1.57x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.16x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 12.0 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 67.6 ms: 1.18x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 33.0 ms: 1.26x slower                                                        |
| django_template | 36.4 ms                                                      | 53.6 ms: 1.48x slower                                                        |
| mako            | 10.4 ms                                                      | 19.5 ms: 1.88x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.43x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.82 ms: 1.24x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 407 ms: 1.14x faster                                                         |
| deepcopy                   | 392 us                                                       | 346 us: 1.13x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 740 ms: 1.12x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.30 ms: 1.11x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 93.6 ms: 1.10x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.65 us: 1.10x faster                                                        |
| async_tree_io              | 843 ms                                                       | 774 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 319 ms: 1.09x faster                                                         |
| async_tree_none            | 376 ms                                                       | 354 ms: 1.06x faster                                                         |
| json                       | 5.69 ms                                                      | 5.43 ms: 1.05x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 440 ms: 1.03x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                        |
| pidigits                   | 252 ms                                                       | 247 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 574 ms: 1.01x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                         |
| regex_dna                  | 247 ms                                                       | 248 ms: 1.00x slower                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 608 ms: 1.01x slower                                                         |
| deepcopy_memo              | 38.6 us                                                      | 39.3 us: 1.02x slower                                                        |
| telco                      | 8.79 ms                                                      | 9.18 ms: 1.04x slower                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.61 sec: 1.06x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.75 us: 1.06x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 103 ms: 1.06x slower                                                         |
| scimark_fft                | 328 ms                                                       | 350 ms: 1.07x slower                                                         |
| coroutines                 | 21.6 ms                                                      | 23.2 ms: 1.07x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.50 sec: 1.08x slower                                                       |
| json_loads                 | 24.7 us                                                      | 26.8 us: 1.09x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.23 sec: 1.10x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.11 sec: 1.10x slower                                                       |
| pylint                     | 347 ms                                                       | 382 ms: 1.10x slower                                                         |
| async_generators           | 457 ms                                                       | 515 ms: 1.13x slower                                                         |
| k_core                     | 2.17 sec                                                     | 2.45 sec: 1.13x slower                                                       |
| generators                 | 33.6 ms                                                      | 38.2 ms: 1.14x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 98.6 ms: 1.14x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.90 sec: 1.14x slower                                                       |
| pycparser                  | 1.24 sec                                                     | 1.42 sec: 1.14x slower                                                       |
| dulwich_log                | 68.2 ms                                                      | 78.2 ms: 1.15x slower                                                        |
| connected_components       | 432 ms                                                       | 504 ms: 1.17x slower                                                         |
| sympy_expand               | 509 ms                                                       | 598 ms: 1.17x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 67.6 ms: 1.18x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 185 ms: 1.20x slower                                                         |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                         |
| sympy_str                  | 298 ms                                                       | 358 ms: 1.20x slower                                                         |
| shortest_path              | 460 ms                                                       | 554 ms: 1.20x slower                                                         |
| python_startup             | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                        |
| regex_compile              | 143 ms                                                       | 173 ms: 1.21x slower                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.78 ms: 1.21x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 28.6 ms: 1.21x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 72.1 ms: 1.22x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 74.7 ms: 1.22x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 146 ms: 1.22x slower                                                         |
| pprint_safe_repr           | 843 ms                                                       | 1.03 sec: 1.23x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 112 ms: 1.24x slower                                                         |
| many_optionals             | 930 us                                                       | 1.16 ms: 1.24x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.14 sec: 1.25x slower                                                       |
| thrift                     | 901 us                                                       | 1.12 ms: 1.25x slower                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 22.9 ms: 1.25x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 33.0 ms: 1.26x slower                                                        |
| html5lib                   | 73.5 ms                                                      | 93.1 ms: 1.27x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 14.2 ms: 1.27x slower                                                        |
| pyflate                    | 503 ms                                                       | 646 ms: 1.28x slower                                                         |
| coverage                   | 80.0 ms                                                      | 103 ms: 1.28x slower                                                         |
| 2to3                       | 293 ms                                                       | 382 ms: 1.30x slower                                                         |
| richards_super             | 59.6 ms                                                      | 79.0 ms: 1.33x slower                                                        |
| float                      | 81.3 ms                                                      | 109 ms: 1.34x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 12.0 ms: 1.34x slower                                                        |
| richards                   | 52.9 ms                                                      | 71.4 ms: 1.35x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 200 ms: 1.35x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 229 us: 1.36x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 99.8 ms: 1.36x slower                                                        |
| logging_simple             | 6.39 us                                                      | 8.74 us: 1.37x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 135 ms: 1.37x slower                                                         |
| fannkuch                   | 363 ms                                                       | 504 ms: 1.39x slower                                                         |
| logging_format             | 6.94 us                                                      | 9.64 us: 1.39x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 9.40 ms: 1.43x slower                                                        |
| nbody                      | 89.3 ms                                                      | 130 ms: 1.46x slower                                                         |
| django_template            | 36.4 ms                                                      | 53.6 ms: 1.48x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 323 us: 1.49x slower                                                         |
| go                         | 162 ms                                                       | 244 ms: 1.50x slower                                                         |
| scimark_sor                | 123 ms                                                       | 192 ms: 1.56x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 506 us: 1.57x slower                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 2.82 ms: 1.57x slower                                                        |
| chaos                      | 60.2 ms                                                      | 94.9 ms: 1.58x slower                                                        |
| comprehensions             | 17.0 us                                                      | 27.0 us: 1.58x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 106 ms: 1.61x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 28.3 ms: 1.62x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.56 ms: 1.66x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 162 ns: 1.66x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 2.36 ms: 1.69x slower                                                        |
| raytrace                   | 273 ms                                                       | 481 ms: 1.76x slower                                                         |
| mako                       | 10.4 ms                                                      | 19.5 ms: 1.88x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 7.13 ms: 2.09x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 52.3 ms: 10.21x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.23x slower                                                                 |

Benchmark hidden because not significant (2): create_gc_cycles, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-pythonperf2-x86_64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: mypy2

- Geometric mean (including insignificant results): 1.166x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.22x