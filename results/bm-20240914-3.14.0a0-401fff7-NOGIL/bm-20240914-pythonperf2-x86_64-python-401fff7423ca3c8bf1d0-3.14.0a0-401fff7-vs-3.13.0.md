# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.286x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 424 ms: 1.45x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.37 sec: 1.20x slower                                                      |
| html5lib       | 72.9 ms                                                      | 105 ms: 1.44x slower                                                        |
| tornado_http   | 119 ms                                                       | 166 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 379 ms: 1.04x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 467 ms: 1.02x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 364 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 878 ms: 1.07x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 625 ms: 1.09x slower                                                        |
| async_tree_none            | 370 ms                                                       | 411 ms: 1.11x slower                                                        |
| async_tree_io              | 832 ms                                                       | 928 ms: 1.12x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 673 ms: 1.13x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 511 ms: 1.14x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 27.8 ms: 1.29x slower                                                       |
| async_generators           | 364 ms                                                       | 489 ms: 1.34x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                        |
| float          | 81.6 ms                                                      | 142 ms: 1.74x slower                                                        |
| nbody          | 92.1 ms                                                      | 191 ms: 2.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.53x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| regex_dna      | 238 ms                                                       | 250 ms: 1.05x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 28.0 ms: 1.12x slower                                                       |
| regex_compile  | 143 ms                                                       | 224 ms: 1.57x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 107 ms: 1.07x slower                                                        |
| json_loads           | 24.7 us                                                      | 28.8 us: 1.16x slower                                                       |
| json_dumps           | 10.8 ms                                                      | 13.9 ms: 1.28x slower                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 113 ms: 1.33x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 3.33 sec: 1.37x slower                                                      |
| xml_etree_process    | 60.7 ms                                                      | 91.6 ms: 1.51x slower                                                       |
| pickle_pure_python   | 322 us                                                       | 583 us: 1.81x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 399 us: 1.84x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.34x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 17.5 ms: 1.12x slower                                                       |
| python_startup_no_site | 8.93 ms                                                      | 11.8 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 82.4 ms: 1.42x slower                                                       |
| genshi_text     | 27.2 ms                                                      | 42.3 ms: 1.56x slower                                                       |
| django_template | 38.9 ms                                                      | 66.4 ms: 1.71x slower                                                       |
| mako            | 10.3 ms                                                      | 21.4 ms: 2.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.67x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.67 ms: 1.59x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 3.04 ms: 1.47x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 379 ms: 1.04x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 467 ms: 1.02x slower                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| regex_dna                  | 238 ms                                                       | 250 ms: 1.05x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 364 ms: 1.06x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 878 ms: 1.07x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 107 ms: 1.07x slower                                                        |
| json                       | 5.62 ms                                                      | 6.03 ms: 1.07x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 625 ms: 1.09x slower                                                        |
| deepcopy                   | 388 us                                                       | 430 us: 1.11x slower                                                        |
| async_tree_none            | 370 ms                                                       | 411 ms: 1.11x slower                                                        |
| async_tree_io              | 832 ms                                                       | 928 ms: 1.12x slower                                                        |
| python_startup             | 15.6 ms                                                      | 17.5 ms: 1.12x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 28.0 ms: 1.12x slower                                                       |
| pathlib                    | 17.4 ms                                                      | 19.6 ms: 1.12x slower                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 673 ms: 1.13x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 511 ms: 1.14x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.8 us: 1.16x slower                                                       |
| telco                      | 8.77 ms                                                      | 10.4 ms: 1.19x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.37 sec: 1.20x slower                                                      |
| generators                 | 33.9 ms                                                      | 41.4 ms: 1.22x slower                                                       |
| pylint                     | 345 ms                                                       | 433 ms: 1.26x slower                                                        |
| deepcopy_memo              | 38.9 us                                                      | 49.2 us: 1.26x slower                                                       |
| coverage                   | 84.5 ms                                                      | 108 ms: 1.27x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 13.9 ms: 1.28x slower                                                       |
| mdp                        | 2.53 sec                                                     | 3.25 sec: 1.29x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 27.8 ms: 1.29x slower                                                       |
| meteor_contest             | 130 ms                                                       | 169 ms: 1.29x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.61 sec: 1.30x slower                                                      |
| deepcopy_reduce            | 3.49 us                                                      | 4.61 us: 1.32x slower                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 11.8 ms: 1.33x slower                                                       |
| pycparser                  | 1.28 sec                                                     | 1.70 sec: 1.33x slower                                                      |
| xml_etree_generate         | 85.2 ms                                                      | 113 ms: 1.33x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.63 ms: 1.34x slower                                                       |
| async_generators           | 364 ms                                                       | 489 ms: 1.34x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 89.1 ms: 1.36x slower                                                       |
| scimark_fft                | 298 ms                                                       | 407 ms: 1.37x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 3.33 sec: 1.37x slower                                                      |
| sympy_integrate            | 23.4 ms                                                      | 32.2 ms: 1.38x slower                                                       |
| tornado_http               | 119 ms                                                       | 166 ms: 1.40x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 129 ms: 1.40x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 82.4 ms: 1.42x slower                                                       |
| html5lib                   | 72.9 ms                                                      | 105 ms: 1.44x slower                                                        |
| 2to3                       | 293 ms                                                       | 424 ms: 1.45x slower                                                        |
| thrift                     | 918 us                                                       | 1.36 ms: 1.48x slower                                                       |
| fannkuch                   | 384 ms                                                       | 575 ms: 1.50x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 263 us: 1.50x slower                                                        |
| sympy_str                  | 297 ms                                                       | 446 ms: 1.51x slower                                                        |
| xml_etree_process          | 60.7 ms                                                      | 91.6 ms: 1.51x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 180 ms: 1.51x slower                                                        |
| richards                   | 52.5 ms                                                      | 79.9 ms: 1.52x slower                                                       |
| pyflate                    | 493 ms                                                       | 760 ms: 1.54x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 91.1 ms: 1.55x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 42.3 ms: 1.56x slower                                                       |
| regex_compile              | 143 ms                                                       | 224 ms: 1.57x slower                                                        |
| richards_super             | 60.2 ms                                                      | 96.3 ms: 1.60x slower                                                       |
| sympy_expand               | 506 ms                                                       | 811 ms: 1.60x slower                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 118 ms: 1.60x slower                                                        |
| pprint_safe_repr           | 835 ms                                                       | 1.37 sec: 1.64x slower                                                      |
| spectral_norm              | 97.4 ms                                                      | 160 ms: 1.64x slower                                                        |
| pprint_pformat             | 1.70 sec                                                     | 2.81 sec: 1.65x slower                                                      |
| comprehensions             | 17.3 us                                                      | 29.1 us: 1.68x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 260 ms: 1.69x slower                                                        |
| go                         | 167 ms                                                       | 285 ms: 1.71x slower                                                        |
| django_template            | 38.9 ms                                                      | 66.4 ms: 1.71x slower                                                       |
| float                      | 81.6 ms                                                      | 142 ms: 1.74x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 11.4 ms: 1.76x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 583 us: 1.81x slower                                                        |
| logging_format             | 6.95 us                                                      | 12.6 us: 1.82x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 177 ns: 1.82x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 1.70 ms: 1.83x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 399 us: 1.84x slower                                                        |
| logging_simple             | 6.28 us                                                      | 11.6 us: 1.86x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 3.35 ms: 1.90x slower                                                       |
| scimark_sor                | 125 ms                                                       | 244 ms: 1.95x slower                                                        |
| chaos                      | 60.6 ms                                                      | 122 ms: 2.01x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 133 ms: 2.04x slower                                                        |
| mako                       | 10.3 ms                                                      | 21.4 ms: 2.07x slower                                                       |
| nbody                      | 92.1 ms                                                      | 191 ms: 2.08x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 2.84 ms: 2.08x slower                                                       |
| raytrace                   | 267 ms                                                       | 596 ms: 2.23x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 228 ms: 2.34x slower                                                        |
| deltablue                  | 3.38 ms                                                      | 8.16 ms: 2.41x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.40x slower                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.286x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: 1.05x