# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: init_slots
- machine: linux-x86_64
- commit hash: 8757207
- commit date: 2024-12-25
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 326 ms: 1.43x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 625 ms: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 635 ms: 1.33x faster                                                         |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 265 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 509 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 492 ms: 1.18x faster                                                         |
| async_generators           | 457 ms                                                       | 430 ms: 1.06x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.7 ms: 1.15x faster                                                        |
| nbody          | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.21 ms: 1.15x faster                                                        |
| regex_dna      | 247 ms                                                       | 236 ms: 1.04x faster                                                         |
| regex_compile  | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.5 ms: 1.03x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.0 us: 1.03x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.6 ms: 1.06x faster                                                        |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                        |
| mako            | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 326 ms: 1.43x faster                                                         |
| deepcopy                   | 392 us                                                       | 284 us: 1.38x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 625 ms: 1.33x faster                                                         |
| async_tree_io              | 843 ms                                                       | 635 ms: 1.33x faster                                                         |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 265 ms: 1.31x faster                                                         |
| go                         | 162 ms                                                       | 125 ms: 1.30x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 349 ms: 1.30x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 30.4 us: 1.27x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.87 us: 1.24x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 509 ms: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 492 ms: 1.18x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.8 ms: 1.16x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.7 ms: 1.15x faster                                                        |
| float                      | 81.3 ms                                                      | 70.7 ms: 1.15x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.21 ms: 1.15x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.85 ms: 1.12x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| pyflate                    | 503 ms                                                       | 454 ms: 1.11x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 23.8 ms: 1.10x faster                                                        |
| json                       | 5.69 ms                                                      | 5.17 ms: 1.10x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 88.5 ms: 1.10x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 771 ms: 1.09x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.1 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.4 ms: 1.09x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.01 ms: 1.09x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.67 sec: 1.09x faster                                                       |
| scimark_sor                | 123 ms                                                       | 113 ms: 1.09x faster                                                         |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.6 ms: 1.08x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 53.6 ms: 1.06x faster                                                        |
| async_generators           | 457 ms                                                       | 430 ms: 1.06x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.6 ms: 1.06x faster                                                        |
| scimark_fft                | 328 ms                                                       | 311 ms: 1.05x faster                                                         |
| thrift                     | 901 us                                                       | 859 us: 1.05x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                        |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.04x faster                                                         |
| regex_compile              | 143 ms                                                       | 137 ms: 1.04x faster                                                         |
| shortest_path              | 460 ms                                                       | 441 ms: 1.04x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                       |
| connected_components       | 432 ms                                                       | 417 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 283 ms: 1.04x faster                                                         |
| raytrace                   | 273 ms                                                       | 264 ms: 1.03x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 95.4 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 83.7 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.03x faster                                                         |
| nbody                      | 89.3 ms                                                      | 86.5 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                         |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.74 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.2 ms: 1.03x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 59.5 ms: 1.03x faster                                                        |
| json_loads                 | 24.7 us                                                      | 24.0 us: 1.03x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.03x faster                                                       |
| sympy_str                  | 298 ms                                                       | 291 ms: 1.03x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 57.8 ms: 1.02x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.34 ms: 1.02x faster                                                        |
| sympy_expand               | 509 ms                                                       | 498 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                        |
| coverage                   | 80.0 ms                                                      | 78.3 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 67.1 ms: 1.02x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.31 us: 1.01x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.86 us: 1.01x faster                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 72.8 ms: 1.01x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 98.7 ns: 1.01x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.84 ms: 1.01x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.78 ms: 1.04x slower                                                        |
| chaos                      | 60.2 ms                                                      | 62.5 ms: 1.04x slower                                                        |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.4 ms: 1.28x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.58 ms: 1.39x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.44 sec: 280.36x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (7): bench_thread_pool, regex_v8, sphinx, djangocms, pidigits, fannkuch, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241225-3.14.0a3+-8757207/bm-20241225-pythonperf2-x86_64-Fidget%2dSpinner-init_slots-3.14.0a3+-8757207.json: mypy2

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x