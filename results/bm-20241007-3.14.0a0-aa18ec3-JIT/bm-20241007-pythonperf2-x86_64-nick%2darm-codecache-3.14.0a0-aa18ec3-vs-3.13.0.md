# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.019x faster
- HPT reliability: 94.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                 |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                               |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                        | 1.06x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                 |
| async_tree_none            | 370 ms                                                       | 327 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                 |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.04x faster                                                 |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                 |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                 |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                 |
| async_generators           | 364 ms                                                       | 383 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 84.2 ms: 1.09x faster                                                |
| float          | 81.6 ms                                                      | 75.8 ms: 1.08x faster                                                |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.43 ms: 1.02x faster                                                |
| regex_v8       | 24.9 ms                                                      | 24.7 ms: 1.01x faster                                                |
| regex_dna      | 238 ms                                                       | 245 ms: 1.03x slower                                                 |
| regex_compile  | 143 ms                                                       | 152 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.17 sec: 1.12x faster                                               |
| xml_etree_generate   | 85.2 ms                                                      | 78.0 ms: 1.09x faster                                                |
| xml_etree_process    | 60.7 ms                                                      | 56.2 ms: 1.08x faster                                                |
| json_loads           | 24.7 us                                                      | 23.8 us: 1.04x faster                                                |
| json_dumps           | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                                |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 99.8 ms                                                      | 98.4 ms: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                       | 215 us: 1.01x faster                                                 |
| pickle_pure_python   | 322 us                                                       | 329 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                |
| python_startup_no_site | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.20 ms: 1.12x faster                                                |
| genshi_text     | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                |
| genshi_xml      | 58.0 ms                                                      | 64.4 ms: 1.11x slower                                                |
| django_template | 38.9 ms                                                      | 43.2 ms: 1.11x slower                                                |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.87 ms: 1.42x faster                                                |
| deepcopy_memo              | 38.9 us                                                      | 27.7 us: 1.40x faster                                                |
| deepcopy                   | 388 us                                                       | 299 us: 1.30x faster                                                 |
| richards_super             | 60.2 ms                                                      | 50.6 ms: 1.19x faster                                                |
| richards                   | 52.5 ms                                                      | 44.2 ms: 1.19x faster                                                |
| deepcopy_reduce            | 3.49 us                                                      | 2.96 us: 1.18x faster                                                |
| scimark_sor                | 125 ms                                                       | 107 ms: 1.17x faster                                                 |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                 |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                |
| spectral_norm              | 97.4 ms                                                      | 83.3 ms: 1.17x faster                                                |
| telco                      | 8.77 ms                                                      | 7.71 ms: 1.14x faster                                                |
| async_tree_none            | 370 ms                                                       | 327 ms: 1.13x faster                                                 |
| mako                       | 10.3 ms                                                      | 9.20 ms: 1.12x faster                                                |
| tomli_loads                | 2.43 sec                                                     | 2.17 sec: 1.12x faster                                               |
| pprint_safe_repr           | 835 ms                                                       | 755 ms: 1.11x faster                                                 |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                |
| async_tree_none_tg         | 342 ms                                                       | 310 ms: 1.10x faster                                                 |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                 |
| nbody                      | 92.1 ms                                                      | 84.2 ms: 1.09x faster                                                |
| xml_etree_generate         | 85.2 ms                                                      | 78.0 ms: 1.09x faster                                                |
| pyflate                    | 493 ms                                                       | 451 ms: 1.09x faster                                                 |
| go                         | 167 ms                                                       | 154 ms: 1.09x faster                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.70 sec: 1.08x faster                                               |
| json                       | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                                |
| xml_etree_process          | 60.7 ms                                                      | 56.2 ms: 1.08x faster                                                |
| fannkuch                   | 384 ms                                                       | 356 ms: 1.08x faster                                                 |
| pprint_pformat             | 1.70 sec                                                     | 1.58 sec: 1.08x faster                                               |
| float                      | 81.6 ms                                                      | 75.8 ms: 1.08x faster                                                |
| deltablue                  | 3.38 ms                                                      | 3.21 ms: 1.06x faster                                                |
| scimark_fft                | 298 ms                                                       | 283 ms: 1.05x faster                                                 |
| coverage                   | 84.5 ms                                                      | 80.7 ms: 1.05x faster                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.04x faster                                                 |
| gc_traversal               | 4.48 ms                                                      | 4.30 ms: 1.04x faster                                                |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                 |
| crypto_pyaes               | 73.5 ms                                                      | 70.7 ms: 1.04x faster                                                |
| json_loads                 | 24.7 us                                                      | 23.8 us: 1.04x faster                                                |
| async_tree_io              | 832 ms                                                       | 804 ms: 1.03x faster                                                 |
| json_dumps                 | 10.8 ms                                                      | 10.5 ms: 1.03x faster                                                |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                 |
| dulwich_log                | 65.5 ms                                                      | 64.0 ms: 1.02x faster                                                |
| regex_effbot               | 3.51 ms                                                      | 3.43 ms: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.4 ms: 1.01x faster                                                |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                 |
| regex_v8                   | 24.9 ms                                                      | 24.7 ms: 1.01x faster                                                |
| unpickle_pure_python       | 216 us                                                       | 215 us: 1.01x faster                                                 |
| python_startup_no_site     | 8.93 ms                                                      | 8.96 ms: 1.00x slower                                                |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                               |
| mdp                        | 2.53 sec                                                     | 2.56 sec: 1.01x slower                                               |
| logging_silent             | 97.5 ns                                                      | 98.9 ns: 1.02x slower                                                |
| bench_thread_pool          | 929 us                                                       | 947 us: 1.02x slower                                                 |
| meteor_contest             | 130 ms                                                       | 133 ms: 1.02x slower                                                 |
| pickle_pure_python         | 322 us                                                       | 329 us: 1.02x slower                                                 |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                 |
| regex_dna                  | 238 ms                                                       | 245 ms: 1.03x slower                                                 |
| logging_format             | 6.95 us                                                      | 7.18 us: 1.03x slower                                                |
| sympy_expand               | 506 ms                                                       | 525 ms: 1.04x slower                                                 |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.7 ms: 1.05x slower                                                |
| logging_simple             | 6.28 us                                                      | 6.61 us: 1.05x slower                                                |
| async_generators           | 364 ms                                                       | 383 ms: 1.05x slower                                                 |
| regex_compile              | 143 ms                                                       | 152 ms: 1.07x slower                                                 |
| genshi_text                | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                |
| sympy_str                  | 297 ms                                                       | 318 ms: 1.07x slower                                                 |
| typing_runtime_protocols   | 176 us                                                       | 189 us: 1.08x slower                                                 |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                 |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                |
| hexiom                     | 6.47 ms                                                      | 7.06 ms: 1.09x slower                                                |
| nqueens                    | 92.3 ms                                                      | 101 ms: 1.09x slower                                                 |
| sqlglot_normalize          | 119 ms                                                       | 130 ms: 1.10x slower                                                 |
| chaos                      | 60.6 ms                                                      | 66.8 ms: 1.10x slower                                                |
| genshi_xml                 | 58.0 ms                                                      | 64.4 ms: 1.11x slower                                                |
| django_template            | 38.9 ms                                                      | 43.2 ms: 1.11x slower                                                |
| sqlglot_parse              | 1.37 ms                                                      | 1.52 ms: 1.12x slower                                                |
| sympy_sum                  | 154 ms                                                       | 173 ms: 1.12x slower                                                 |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                               |
| sympy_integrate            | 23.4 ms                                                      | 27.2 ms: 1.16x slower                                                |
| generators                 | 33.9 ms                                                      | 39.5 ms: 1.17x slower                                                |
| sqlglot_optimize           | 58.7 ms                                                      | 68.7 ms: 1.17x slower                                                |
| pylint                     | 345 ms                                                       | 414 ms: 1.20x slower                                                 |
| raytrace                   | 267 ms                                                       | 322 ms: 1.20x slower                                                 |
| bench_mp_pool              | 4.82 ms                                                      | 4.58 sec: 951.66x slower                                             |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                         |

Benchmark hidden because not significant (3): scimark_lu, thrift, html5lib
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.019x faster
# HPT report

- Reliability score: 94.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x