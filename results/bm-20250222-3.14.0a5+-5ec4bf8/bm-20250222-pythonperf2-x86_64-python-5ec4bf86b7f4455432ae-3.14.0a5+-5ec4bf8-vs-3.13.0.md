# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 68.4 ms: 1.07x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| async_tree_none            | 376 ms                                                       | 285 ms: 1.32x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 345 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 514 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| async_generators           | 457 ms                                                       | 412 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                        |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                        |
| regex_compile  | 143 ms                                                       | 135 ms: 1.05x faster                                                         |
| regex_dna      | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| regex_v8       | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.8 ms: 1.07x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 58.5 ms: 1.05x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.8 ms: 1.05x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 210 us: 1.04x faster                                                         |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 331 us: 1.03x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.9 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                        |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                        |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                         |
| deepcopy                   | 392 us                                                       | 290 us: 1.35x faster                                                         |
| async_tree_none            | 376 ms                                                       | 285 ms: 1.32x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 345 ms: 1.32x faster                                                         |
| async_tree_io              | 843 ms                                                       | 642 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 641 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                                         |
| go                         | 162 ms                                                       | 132 ms: 1.23x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.19x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.09 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 514 ms: 1.18x faster                                                         |
| pyflate                    | 503 ms                                                       | 430 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 501 ms: 1.16x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 83.8 ms: 1.16x faster                                                        |
| float                      | 81.3 ms                                                      | 70.3 ms: 1.16x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.9 ms: 1.15x faster                                                        |
| richards_super             | 59.6 ms                                                      | 51.8 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 412 ms: 1.11x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.95 ms: 1.10x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                         |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                         |
| scimark_sor                | 123 ms                                                       | 113 ms: 1.09x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.2 ms: 1.08x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 68.4 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.8 ms: 1.07x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 24.5 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.60 sec: 1.07x faster                                                       |
| thrift                     | 901 us                                                       | 842 us: 1.07x faster                                                         |
| hexiom                     | 6.55 ms                                                      | 6.13 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 789 ms: 1.07x faster                                                         |
| json                       | 5.69 ms                                                      | 5.33 ms: 1.07x faster                                                        |
| regex_compile              | 143 ms                                                       | 135 ms: 1.05x faster                                                         |
| scimark_fft                | 328 ms                                                       | 312 ms: 1.05x faster                                                         |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.2 ms                                                      | 58.5 ms: 1.05x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.05x faster                                                         |
| xml_etree_generate         | 86.5 ms                                                      | 82.8 ms: 1.05x faster                                                        |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.79 us: 1.04x faster                                                        |
| connected_components       | 432 ms                                                       | 415 ms: 1.04x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.34 ms: 1.04x faster                                                        |
| sympy_str                  | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 55.0 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 210 us: 1.04x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 57.2 ms: 1.04x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.45 sec: 1.04x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.6 ms: 1.04x faster                                                        |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.03x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.03x faster                                                        |
| regex_dna                  | 247 ms                                                       | 239 ms: 1.03x faster                                                         |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                         |
| deltablue                  | 3.42 ms                                                      | 3.31 ms: 1.03x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 87.9 ms: 1.03x faster                                                        |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                                         |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.8 ms: 1.03x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 25.3 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 96.4 ns: 1.02x faster                                                        |
| fannkuch                   | 363 ms                                                       | 358 ms: 1.01x faster                                                         |
| dulwich_log                | 68.2 ms                                                      | 67.2 ms: 1.01x faster                                                        |
| coverage                   | 80.0 ms                                                      | 78.9 ms: 1.01x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                                       |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 98.1 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.78 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.01 ms: 1.01x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 73.8 ms: 1.01x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.45 us: 1.01x slower                                                        |
| raytrace                   | 273 ms                                                       | 275 ms: 1.01x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.04 us: 1.01x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 172 us: 1.02x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 331 us: 1.03x slower                                                         |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                        |
| nbody                      | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                        |
| json_loads                 | 24.7 us                                                      | 25.9 us: 1.05x slower                                                        |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 854 ms: 166.66x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, bench_thread_pool, comprehensions, chaos, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.03x