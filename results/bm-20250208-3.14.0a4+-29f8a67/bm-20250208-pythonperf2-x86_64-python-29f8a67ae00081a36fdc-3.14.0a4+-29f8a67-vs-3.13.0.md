# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| async_tree_io              | 843 ms                                                       | 643 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                         |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.0 ms: 1.18x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 93.7 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| regex_dna      | 247 ms                                                       | 236 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.2 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                         |
| xml_etree_process    | 61.2 ms                                                      | 59.1 ms: 1.04x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.06 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 53.9 ms: 1.06x faster                                                        |
| django_template | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                        |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 337 ms: 1.38x faster                                                         |
| deepcopy                   | 392 us                                                       | 287 us: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 643 ms: 1.31x faster                                                         |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.29x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 646 ms: 1.29x faster                                                         |
| go                         | 162 ms                                                       | 127 ms: 1.27x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 31.0 us: 1.25x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.20x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.07 sec: 1.19x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                        |
| pyflate                    | 503 ms                                                       | 426 ms: 1.18x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.5 ms: 1.18x faster                                                        |
| float                      | 81.3 ms                                                      | 69.0 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 519 ms: 1.16x faster                                                         |
| richards                   | 52.9 ms                                                      | 45.7 ms: 1.16x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.6 ms: 1.15x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 84.1 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 509 ms: 1.14x faster                                                         |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.55 sec: 1.12x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.89 ms: 1.11x faster                                                        |
| async_generators           | 457 ms                                                       | 410 ms: 1.11x faster                                                         |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                         |
| html5lib                   | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                        |
| scimark_fft                | 328 ms                                                       | 302 ms: 1.09x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.06 ms: 1.08x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.3 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.2 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 781 ms: 1.08x faster                                                         |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.5 ms: 1.07x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 16.4 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.9 ms: 1.06x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                         |
| thrift                     | 901 us                                                       | 856 us: 1.05x faster                                                         |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                         |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                         |
| regex_v8                   | 26.1 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.35 ms: 1.04x faster                                                        |
| json                       | 5.69 ms                                                      | 5.47 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                         |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                                         |
| scimark_lu                 | 98.7 ms                                                      | 95.0 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.04x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 59.1 ms: 1.04x faster                                                        |
| sqlglot_optimize           | 59.3 ms                                                      | 57.4 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.31 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 494 ms: 1.03x faster                                                         |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.23 us: 1.03x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.77 us: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.0 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 88.6 ms: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.49 sec: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.67 ms: 1.02x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.6 ms: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 23.2 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 153 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 85.6 ms: 1.01x faster                                                        |
| coverage                   | 80.0 ms                                                      | 79.5 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 72.9 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| comprehensions             | 17.0 us                                                      | 17.2 us: 1.01x slower                                                        |
| fannkuch                   | 363 ms                                                       | 367 ms: 1.01x slower                                                         |
| raytrace                   | 273 ms                                                       | 276 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.06 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.02x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| nbody                      | 89.3 ms                                                      | 93.7 ms: 1.05x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.85 ms: 1.06x slower                                                        |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.07x slower                                                        |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.31x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.37 ms: 1.34x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 889 ms: 173.56x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (6): bench_thread_pool, asyncio_websockets, chaos, logging_silent, pycparser, typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x