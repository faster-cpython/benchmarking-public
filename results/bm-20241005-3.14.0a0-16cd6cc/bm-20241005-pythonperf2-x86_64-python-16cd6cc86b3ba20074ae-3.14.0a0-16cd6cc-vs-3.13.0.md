# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.032x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                       | 115 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 786 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| regex_dna      | 238 ms                                                       | 242 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 315 us: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                       | 218 us: 1.01x slower                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 86.1 ms: 1.01x slower                                                       |
| xml_etree_process    | 60.7 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.54 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                       |
| mako            | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| django_template | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 284 us: 1.37x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 29.5 us: 1.32x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.03 ms: 1.31x faster                                                       |
| go                         | 167 ms                                                       | 135 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.90 us: 1.20x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.1 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| fannkuch                   | 384 ms                                                       | 355 ms: 1.08x faster                                                        |
| thrift                     | 918 us                                                       | 855 us: 1.07x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.19 ms: 1.07x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                       |
| scimark_sor                | 125 ms                                                       | 118 ms: 1.06x faster                                                        |
| json                       | 5.62 ms                                                      | 5.34 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 786 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 93.5 ms: 1.04x faster                                                       |
| richards_super             | 60.2 ms                                                      | 57.9 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 803 ms: 1.04x faster                                                        |
| hexiom                     | 6.47 ms                                                      | 6.23 ms: 1.04x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 88.8 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| float                      | 81.6 ms                                                      | 78.8 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                        |
| sympy_expand               | 506 ms                                                       | 491 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 115 ms: 1.03x faster                                                        |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.03x faster                                                      |
| richards                   | 52.5 ms                                                      | 51.2 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| logging_format             | 6.95 us                                                      | 6.80 us: 1.02x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.98 sec: 1.02x faster                                                      |
| pickle_pure_python         | 322 us                                                       | 315 us: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.48 sec: 1.02x faster                                                      |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 176 us                                                       | 173 us: 1.02x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.01x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                       |
| deltablue                  | 3.38 ms                                                      | 3.35 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 218 us: 1.01x slower                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 74.2 ms: 1.01x slower                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 86.1 ms: 1.01x slower                                                       |
| xml_etree_process          | 60.7 ms                                                      | 61.4 ms: 1.01x slower                                                       |
| mako                       | 10.3 ms                                                      | 10.4 ms: 1.01x slower                                                       |
| coverage                   | 84.5 ms                                                      | 85.7 ms: 1.01x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.9 ms: 1.01x slower                                                       |
| regex_dna                  | 238 ms                                                       | 242 ms: 1.02x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 66.6 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 99.3 ns: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.80 ms: 1.02x slower                                                       |
| raytrace                   | 267 ms                                                       | 273 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| pyflate                    | 493 ms                                                       | 504 ms: 1.02x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| django_template            | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| chaos                      | 60.6 ms                                                      | 63.0 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.54 sec: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.41 ms: 1.05x slower                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.81 ms: 1.07x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 1.33 sec: 276.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (10): nbody, async_tree_io, bench_thread_pool, scimark_fft, spectral_norm, json_dumps, logging_simple, regex_v8, sqlglot_optimize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.032x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x