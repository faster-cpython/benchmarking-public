# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.049x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 332 ms: 1.13x slower                                                         |
| docutils       | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                       |
| html5lib       | 73.5 ms                                                      | 72.6 ms: 1.01x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 577 ms: 1.44x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 256 ms: 1.35x faster                                                         |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.13x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                         |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 74.5 ms: 1.09x faster                                                        |
| pidigits       | 252 ms                                                       | 248 ms: 1.02x faster                                                         |
| nbody          | 89.3 ms                                                      | 128 ms: 1.44x slower                                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| regex_dna      | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                        |
| regex_compile  | 143 ms                                                       | 153 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 89.6 ms: 1.15x faster                                                        |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| tomli_loads          | 2.46 sec                                                     | 2.38 sec: 1.04x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 236 us: 1.09x slower                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 96.8 ms: 1.12x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 70.0 ms: 1.14x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 370 us: 1.15x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 13.7 ms: 1.23x slower                                                        |
| json_loads           | 24.7 us                                                      | 32.9 us: 1.33x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 18.7 ms: 1.17x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 63.6 ms: 1.12x slower                                                        |
| genshi_text     | 26.2 ms                                                      | 29.6 ms: 1.13x slower                                                        |
| django_template | 36.4 ms                                                      | 45.4 ms: 1.25x slower                                                        |
| mako            | 10.4 ms                                                      | 17.9 ms: 1.73x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.05 ms: 2.32x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 577 ms: 1.44x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| async_tree_io              | 843 ms                                                       | 619 ms: 1.36x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 256 ms: 1.35x faster                                                         |
| create_gc_cycles           | 2.68 ms                                                      | 2.02 ms: 1.33x faster                                                        |
| async_tree_none            | 376 ms                                                       | 297 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 365 ms: 1.24x faster                                                         |
| deepcopy                   | 392 us                                                       | 327 us: 1.20x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 495 ms: 1.18x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.20 ms: 1.15x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 89.6 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 532 ms: 1.13x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.59 us: 1.12x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                         |
| float                      | 81.3 ms                                                      | 74.5 ms: 1.09x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.1 ms: 1.09x faster                                                        |
| go                         | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 36.3 us: 1.06x faster                                                        |
| generators                 | 33.6 ms                                                      | 32.0 ms: 1.05x faster                                                        |
| scimark_sor                | 123 ms                                                       | 118 ms: 1.05x faster                                                         |
| regex_dna                  | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| tomli_loads                | 2.46 sec                                                     | 2.38 sec: 1.04x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 25.5 ms: 1.03x faster                                                        |
| pyflate                    | 503 ms                                                       | 491 ms: 1.02x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 379 ms: 1.02x faster                                                         |
| pidigits                   | 252 ms                                                       | 248 ms: 1.02x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 72.6 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.11 sec: 1.00x slower                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.56 us: 1.01x slower                                                        |
| dulwich_log                | 68.2 ms                                                      | 69.0 ms: 1.01x slower                                                        |
| logging_silent             | 97.9 ns                                                      | 99.6 ns: 1.02x slower                                                        |
| scimark_fft                | 328 ms                                                       | 337 ms: 1.03x slower                                                         |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                         |
| telco                      | 8.79 ms                                                      | 9.12 ms: 1.04x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.04x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.96 sec: 1.05x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.18 sec: 1.05x slower                                                       |
| pprint_safe_repr           | 843 ms                                                       | 896 ms: 1.06x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 128 ms: 1.07x slower                                                         |
| regex_compile              | 143 ms                                                       | 153 ms: 1.07x slower                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.86 sec: 1.08x slower                                                       |
| json                       | 5.69 ms                                                      | 6.15 ms: 1.08x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 236 us: 1.09x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.76 sec: 1.09x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 7.19 ms: 1.10x slower                                                        |
| sympy_expand               | 509 ms                                                       | 561 ms: 1.10x slower                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 65.7 ms: 1.11x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 63.6 ms: 1.12x slower                                                        |
| richards                   | 52.9 ms                                                      | 59.2 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 96.8 ms: 1.12x slower                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 20.5 ms: 1.12x slower                                                        |
| thrift                     | 901 us                                                       | 1.01 ms: 1.12x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 174 ms: 1.13x slower                                                         |
| richards_super             | 59.6 ms                                                      | 67.2 ms: 1.13x slower                                                        |
| logging_simple             | 6.39 us                                                      | 7.21 us: 1.13x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 29.6 ms: 1.13x slower                                                        |
| sympy_str                  | 298 ms                                                       | 337 ms: 1.13x slower                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 2.03 ms: 1.13x slower                                                        |
| 2to3                       | 293 ms                                                       | 332 ms: 1.13x slower                                                         |
| connected_components       | 432 ms                                                       | 491 ms: 1.14x slower                                                         |
| sympy_integrate            | 23.6 ms                                                      | 26.9 ms: 1.14x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 70.0 ms: 1.14x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.47 ms: 1.15x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 370 us: 1.15x slower                                                         |
| shortest_path              | 460 ms                                                       | 529 ms: 1.15x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 171 ms: 1.15x slower                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.62 ms: 1.16x slower                                                        |
| comprehensions             | 17.0 us                                                      | 19.7 us: 1.16x slower                                                        |
| logging_format             | 6.94 us                                                      | 8.07 us: 1.16x slower                                                        |
| chaos                      | 60.2 ms                                                      | 70.2 ms: 1.17x slower                                                        |
| python_startup             | 15.9 ms                                                      | 18.7 ms: 1.17x slower                                                        |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.19x slower                                                        |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.20x slower                                                         |
| scimark_lu                 | 98.7 ms                                                      | 119 ms: 1.21x slower                                                         |
| nqueens                    | 90.7 ms                                                      | 111 ms: 1.22x slower                                                         |
| json_dumps                 | 11.1 ms                                                      | 13.7 ms: 1.23x slower                                                        |
| raytrace                   | 273 ms                                                       | 337 ms: 1.24x slower                                                         |
| django_template            | 36.4 ms                                                      | 45.4 ms: 1.25x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 213 us: 1.26x slower                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 84.4 ms: 1.28x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.6 ms: 1.28x slower                                                        |
| fannkuch                   | 363 ms                                                       | 476 ms: 1.31x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                        |
| deltablue                  | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                        |
| json_loads                 | 24.7 us                                                      | 32.9 us: 1.33x slower                                                        |
| coverage                   | 80.0 ms                                                      | 108 ms: 1.36x slower                                                         |
| nbody                      | 89.3 ms                                                      | 128 ms: 1.44x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 25.5 ms: 1.46x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.46 ms: 1.55x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.9 ms: 1.73x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 47.5 ms: 9.27x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (2): pycparser, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.22x