# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.8 ms: 1.07x faster                                                       |
| float          | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 138 ms: 1.03x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.45 ms: 1.02x faster                                                       |
| regex_dna      | 238 ms                                                       | 236 ms: 1.01x faster                                                        |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process  | 60.7 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| xml_etree_generate | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| xml_etree_parse    | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_dumps         | 10.8 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| json_loads         | 24.7 us                                                      | 25.3 us: 1.02x slower                                                       |
| tomli_loads        | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| Geometric mean     | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (3): pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                                       |
| django_template | 38.9 ms                                                      | 39.0 ms: 1.00x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 286 us: 1.36x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 29.1 us: 1.34x faster                                                       |
| go                         | 167 ms                                                       | 137 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.91 us: 1.20x faster                                                       |
| generators                 | 33.9 ms                                                      | 28.9 ms: 1.17x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 318 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 400 ms: 1.12x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 53.4 ms: 1.09x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 863 us: 1.08x faster                                                        |
| nbody                      | 92.1 ms                                                      | 85.8 ms: 1.07x faster                                                       |
| thrift                     | 918 us                                                       | 857 us: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.25 ms: 1.07x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.8 ms: 1.06x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.21 sec: 1.06x faster                                                      |
| telco                      | 8.77 ms                                                      | 8.34 ms: 1.05x faster                                                       |
| fannkuch                   | 384 ms                                                       | 366 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 783 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 88.7 ms: 1.04x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.5 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 803 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 803 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.09 ms: 1.03x faster                                                       |
| regex_compile              | 143 ms                                                       | 138 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 71.1 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.97 sec: 1.03x faster                                                      |
| typing_runtime_protocols   | 176 us                                                       | 171 us: 1.03x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 95.1 ms: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.02x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.47 sec: 1.02x faster                                                      |
| coverage                   | 84.5 ms                                                      | 82.7 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 387 ms: 1.02x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.45 ms: 1.02x faster                                                       |
| sympy_expand               | 506 ms                                                       | 497 ms: 1.02x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.36 ms: 1.02x faster                                                       |
| scimark_sor                | 125 ms                                                       | 123 ms: 1.02x faster                                                        |
| scimark_fft                | 298 ms                                                       | 293 ms: 1.02x faster                                                        |
| sympy_integrate            | 23.4 ms                                                      | 23.0 ms: 1.02x faster                                                       |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 72.6 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| float                      | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 60.1 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| regex_dna                  | 238 ms                                                       | 236 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 58.8 ms: 1.00x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.0 ms: 1.00x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.41 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| raytrace                   | 267 ms                                                       | 270 ms: 1.01x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.35 us: 1.01x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| pyflate                    | 493 ms                                                       | 503 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 67.0 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.02x slower                                                       |
| chaos                      | 60.6 ms                                                      | 62.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.40 ms: 1.03x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| gc_traversal               | 4.48 ms                                                      | 4.65 ms: 1.04x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.8 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, sqlglot_normalize, pidigits, pickle_pure_python, comprehensions, unpickle_pure_python, logging_format, xml_etree_iterparse, mako, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x