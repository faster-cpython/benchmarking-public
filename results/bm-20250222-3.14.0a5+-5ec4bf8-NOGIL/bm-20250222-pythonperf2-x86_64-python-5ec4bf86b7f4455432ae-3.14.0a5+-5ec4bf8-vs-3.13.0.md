# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.044x slower
- HPT reliability: 99.84%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 329 ms: 1.12x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                       |
| html5lib       | 73.5 ms                                                      | 74.1 ms: 1.01x slower                                                        |
| sphinx         | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 553 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 317 ms: 1.47x faster                                                         |
| async_tree_io              | 843 ms                                                       | 589 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 247 ms: 1.40x faster                                                         |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 479 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                         |
| async_generators           | 457 ms                                                       | 466 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 74.7 ms: 1.09x faster                                                        |
| pidigits       | 252 ms                                                       | 248 ms: 1.02x faster                                                         |
| nbody          | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| regex_dna      | 247 ms                                                       | 245 ms: 1.01x faster                                                         |
| regex_compile  | 143 ms                                                       | 160 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 90.9 ms: 1.13x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.43 sec: 1.01x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 365 us: 1.13x slower                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 98.0 ms: 1.13x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 71.2 ms: 1.16x slower                                                        |
| json_loads           | 24.7 us                                                      | 28.7 us: 1.17x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 13.2 ms: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 64.3 ms: 1.13x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 29.8 ms: 1.14x slower                                                        |
| django_template | 36.4 ms                                                      | 45.6 ms: 1.25x slower                                                        |
| mako            | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.05 ms: 2.31x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 553 ms: 1.50x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 317 ms: 1.47x faster                                                         |
| async_tree_io              | 843 ms                                                       | 589 ms: 1.43x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 247 ms: 1.40x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 1.96 ms: 1.36x faster                                                        |
| async_tree_none            | 376 ms                                                       | 284 ms: 1.33x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 479 ms: 1.21x faster                                                         |
| deepcopy                   | 392 us                                                       | 329 us: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 517 ms: 1.17x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.18 ms: 1.15x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 90.9 ms: 1.13x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.58 us: 1.13x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 35.2 us: 1.10x faster                                                        |
| float                      | 81.3 ms                                                      | 74.7 ms: 1.09x faster                                                        |
| go                         | 162 ms                                                       | 151 ms: 1.07x faster                                                         |
| scimark_sor                | 123 ms                                                       | 117 ms: 1.05x faster                                                         |
| generators                 | 33.6 ms                                                      | 32.1 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                        |
| pyflate                    | 503 ms                                                       | 487 ms: 1.03x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                         |
| pidigits                   | 252 ms                                                       | 248 ms: 1.02x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 17.3 ms: 1.01x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.43 sec: 1.01x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                       |
| regex_dna                  | 247 ms                                                       | 245 ms: 1.01x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 96.3 ms: 1.01x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 74.1 ms: 1.01x slower                                                        |
| async_generators           | 457 ms                                                       | 466 ms: 1.02x slower                                                         |
| logging_silent             | 97.9 ns                                                      | 100 ns: 1.02x slower                                                         |
| dulwich_log                | 68.2 ms                                                      | 69.8 ms: 1.02x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.30 sec: 1.04x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                       |
| telco                      | 8.79 ms                                                      | 9.23 ms: 1.05x slower                                                        |
| scimark_fft                | 328 ms                                                       | 347 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 843 ms                                                       | 911 ms: 1.08x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 129 ms: 1.08x slower                                                         |
| thrift                     | 901 us                                                       | 975 us: 1.08x slower                                                         |
| richards                   | 52.9 ms                                                      | 57.6 ms: 1.09x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.89 sec: 1.10x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                         |
| logging_simple             | 6.39 us                                                      | 7.07 us: 1.11x slower                                                        |
| mdp                        | 2.54 sec                                                     | 2.81 sec: 1.11x slower                                                       |
| sympy_expand               | 509 ms                                                       | 565 ms: 1.11x slower                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.3 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 65.8 ms: 1.11x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 7.31 ms: 1.12x slower                                                        |
| richards_super             | 59.6 ms                                                      | 66.8 ms: 1.12x slower                                                        |
| 2to3                       | 293 ms                                                       | 329 ms: 1.12x slower                                                         |
| regex_compile              | 143 ms                                                       | 160 ms: 1.12x slower                                                         |
| sympy_str                  | 298 ms                                                       | 335 ms: 1.12x slower                                                         |
| sympy_sum                  | 155 ms                                                       | 174 ms: 1.13x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 64.3 ms: 1.13x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.85 us: 1.13x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 365 us: 1.13x slower                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 98.0 ms: 1.13x slower                                                        |
| connected_components       | 432 ms                                                       | 491 ms: 1.14x slower                                                         |
| genshi_text                | 26.2 ms                                                      | 29.8 ms: 1.14x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                        |
| shortest_path              | 460 ms                                                       | 527 ms: 1.15x slower                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 2.06 ms: 1.15x slower                                                        |
| chaos                      | 60.2 ms                                                      | 69.5 ms: 1.15x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 171 ms: 1.16x slower                                                         |
| comprehensions             | 17.0 us                                                      | 19.7 us: 1.16x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 3.97 ms: 1.16x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 71.2 ms: 1.16x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.7 us: 1.17x slower                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.65 ms: 1.18x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 13.2 ms: 1.18x slower                                                        |
| meteor_contest             | 130 ms                                                       | 153 ms: 1.19x slower                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.68 ms: 1.19x slower                                                        |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.19x slower                                                        |
| python_startup             | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 119 ms: 1.21x slower                                                         |
| raytrace                   | 273 ms                                                       | 334 ms: 1.22x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.23x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 91.8 ms: 1.25x slower                                                        |
| django_template            | 36.4 ms                                                      | 45.6 ms: 1.25x slower                                                        |
| coverage                   | 80.0 ms                                                      | 102 ms: 1.27x slower                                                         |
| typing_runtime_protocols   | 169 us                                                       | 219 us: 1.30x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                        |
| fannkuch                   | 363 ms                                                       | 480 ms: 1.32x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 88.5 ms: 1.34x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 25.2 ms: 1.44x slower                                                        |
| nbody                      | 89.3 ms                                                      | 129 ms: 1.45x slower                                                         |
| bench_thread_pool          | 942 us                                                       | 1.44 ms: 1.53x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.6 ms: 1.70x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 48.9 ms: 9.54x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                 |

Benchmark hidden because not significant (4): regex_v8, json, deepcopy_reduce, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.84% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.23x