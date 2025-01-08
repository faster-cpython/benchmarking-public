# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                              |
| html5lib       | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                               |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                        | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 323 ms: 1.44x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 620 ms: 1.34x faster                                                |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.34x faster                                                |
| async_tree_memoization     | 453 ms                                                       | 344 ms: 1.32x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 494 ms: 1.18x faster                                                |
| async_generators           | 457 ms                                                       | 431 ms: 1.06x faster                                                |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                               |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                               |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                        | 1.04x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                               |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                                |
| regex_dna      | 247 ms                                                       | 244 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                        | 1.04x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                              |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 103 ms                                                       | 97.3 ms: 1.06x faster                                               |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                |
| json_loads           | 24.7 us                                                      | 23.6 us: 1.04x faster                                               |
| xml_etree_process    | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                               |
| xml_etree_generate   | 86.5 ms                                                      | 83.3 ms: 1.04x faster                                               |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                               |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                               |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                               |
| django_template | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                               |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 323 ms: 1.44x faster                                                |
| deepcopy                   | 392 us                                                       | 281 us: 1.39x faster                                                |
| async_tree_io_tg           | 831 ms                                                       | 620 ms: 1.34x faster                                                |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.34x faster                                                |
| async_tree_memoization     | 453 ms                                                       | 344 ms: 1.32x faster                                                |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.30x faster                                                |
| deepcopy_memo              | 38.6 us                                                      | 30.0 us: 1.29x faster                                               |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.20x faster                                               |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                              |
| generators                 | 33.6 ms                                                      | 28.4 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 494 ms: 1.18x faster                                                |
| richards                   | 52.9 ms                                                      | 46.0 ms: 1.15x faster                                               |
| richards_super             | 59.6 ms                                                      | 51.9 ms: 1.15x faster                                               |
| float                      | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                               |
| regex_effbot               | 3.67 ms                                                      | 3.26 ms: 1.13x faster                                               |
| json                       | 5.69 ms                                                      | 5.09 ms: 1.12x faster                                               |
| scimark_sor                | 123 ms                                                       | 111 ms: 1.11x faster                                                |
| pyflate                    | 503 ms                                                       | 453 ms: 1.11x faster                                                |
| telco                      | 8.79 ms                                                      | 7.92 ms: 1.11x faster                                               |
| scimark_fft                | 328 ms                                                       | 298 ms: 1.10x faster                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                              |
| pylint                     | 347 ms                                                       | 317 ms: 1.10x faster                                                |
| pprint_safe_repr           | 843 ms                                                       | 770 ms: 1.09x faster                                                |
| html5lib                   | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                               |
| genshi_text                | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                               |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                |
| spectral_norm              | 97.0 ms                                                      | 90.0 ms: 1.08x faster                                               |
| hexiom                     | 6.55 ms                                                      | 6.09 ms: 1.08x faster                                               |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                               |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                              |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.45 ms: 1.07x faster                                               |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.0 ms: 1.07x faster                                               |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                               |
| async_generators           | 457 ms                                                       | 431 ms: 1.06x faster                                                |
| xml_etree_iterparse        | 103 ms                                                       | 97.3 ms: 1.06x faster                                               |
| thrift                     | 901 us                                                       | 857 us: 1.05x faster                                                |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                               |
| scimark_lu                 | 98.7 ms                                                      | 94.1 ms: 1.05x faster                                               |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                                |
| json_loads                 | 24.7 us                                                      | 23.6 us: 1.04x faster                                               |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.04x faster                                                |
| xml_etree_process          | 61.2 ms                                                      | 58.8 ms: 1.04x faster                                               |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                |
| xml_etree_generate         | 86.5 ms                                                      | 83.3 ms: 1.04x faster                                               |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.03x faster                                               |
| dulwich_log                | 68.2 ms                                                      | 65.9 ms: 1.03x faster                                               |
| k_core                     | 2.17 sec                                                     | 2.10 sec: 1.03x faster                                              |
| coverage                   | 80.0 ms                                                      | 77.4 ms: 1.03x faster                                               |
| sqlglot_optimize           | 59.3 ms                                                      | 57.3 ms: 1.03x faster                                               |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                               |
| bench_thread_pool          | 942 us                                                       | 915 us: 1.03x faster                                                |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.02x faster                                              |
| sympy_expand               | 509 ms                                                       | 497 ms: 1.02x faster                                                |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                               |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                               |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                |
| raytrace                   | 273 ms                                                       | 268 ms: 1.02x faster                                                |
| crypto_pyaes               | 73.3 ms                                                      | 72.1 ms: 1.02x faster                                               |
| sqlite_synth               | 2.91 us                                                      | 2.86 us: 1.01x faster                                               |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                              |
| regex_dna                  | 247 ms                                                       | 244 ms: 1.01x faster                                                |
| django_template            | 36.4 ms                                                      | 35.9 ms: 1.01x faster                                               |
| deltablue                  | 3.42 ms                                                      | 3.38 ms: 1.01x faster                                               |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                |
| fannkuch                   | 363 ms                                                       | 365 ms: 1.00x slower                                                |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                               |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                               |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                              |
| logging_format             | 6.94 us                                                      | 7.08 us: 1.02x slower                                               |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.02x slower                                               |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.03x slower                                               |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                               |
| chaos                      | 60.2 ms                                                      | 61.9 ms: 1.03x slower                                               |
| typing_runtime_protocols   | 169 us                                                       | 175 us: 1.03x slower                                                |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                               |
| many_optionals             | 930 us                                                       | 1.03 ms: 1.10x slower                                               |
| gc_traversal               | 4.74 ms                                                      | 6.06 ms: 1.28x slower                                               |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.31x slower                                               |
| bench_mp_pool              | 5.12 ms                                                      | 1.58 sec: 307.56x slower                                            |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                        |

Benchmark hidden because not significant (6): pycparser, nqueens, logging_simple, nbody, logging_silent, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: mypy2

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x