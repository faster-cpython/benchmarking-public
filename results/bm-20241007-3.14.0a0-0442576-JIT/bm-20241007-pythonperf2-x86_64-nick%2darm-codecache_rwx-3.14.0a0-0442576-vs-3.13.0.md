# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.014x faster
- HPT reliability: 85.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 315 ms: 1.08x slower                                                     |
| docutils       | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                   |
| html5lib       | 72.9 ms                                                      | 73.1 ms: 1.00x slower                                                    |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                     |
| async_tree_none            | 370 ms                                                       | 329 ms: 1.13x faster                                                     |
| async_tree_memoization     | 447 ms                                                       | 407 ms: 1.10x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                     |
| async_tree_io_tg           | 823 ms                                                       | 782 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                     |
| async_tree_io              | 832 ms                                                       | 805 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                     |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                     |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                    |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.3 ms: 1.11x faster                                                    |
| float          | 81.6 ms                                                      | 75.3 ms: 1.08x faster                                                    |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                        | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 236 ms: 1.01x faster                                                     |
| regex_v8       | 24.9 ms                                                      | 24.8 ms: 1.00x faster                                                    |
| regex_effbot   | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                    |
| regex_compile  | 143 ms                                                       | 150 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.20 sec: 1.11x faster                                                   |
| xml_etree_generate   | 85.2 ms                                                      | 78.8 ms: 1.08x faster                                                    |
| xml_etree_process    | 60.7 ms                                                      | 56.4 ms: 1.08x faster                                                    |
| json_loads           | 24.7 us                                                      | 23.8 us: 1.04x faster                                                    |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                    |
| pickle_pure_python   | 322 us                                                       | 325 us: 1.01x slower                                                     |
| unpickle_pure_python | 216 us                                                       | 219 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                    |
| python_startup_no_site | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                                    |
| genshi_text     | 27.2 ms                                                      | 29.8 ms: 1.10x slower                                                    |
| genshi_xml      | 58.0 ms                                                      | 66.2 ms: 1.14x slower                                                    |
| django_template | 38.9 ms                                                      | 46.0 ms: 1.18x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 27.3 us: 1.42x faster                                                    |
| create_gc_cycles           | 2.65 ms                                                      | 1.90 ms: 1.39x faster                                                    |
| deepcopy                   | 388 us                                                       | 300 us: 1.29x faster                                                     |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.18x faster                                                    |
| spectral_norm              | 97.4 ms                                                      | 82.8 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                     |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                    |
| telco                      | 8.77 ms                                                      | 7.63 ms: 1.15x faster                                                    |
| mako                       | 10.3 ms                                                      | 9.15 ms: 1.13x faster                                                    |
| async_tree_none            | 370 ms                                                       | 329 ms: 1.13x faster                                                     |
| fannkuch                   | 384 ms                                                       | 346 ms: 1.11x faster                                                     |
| richards                   | 52.5 ms                                                      | 47.3 ms: 1.11x faster                                                    |
| tomli_loads                | 2.43 sec                                                     | 2.20 sec: 1.11x faster                                                   |
| nbody                      | 92.1 ms                                                      | 83.3 ms: 1.11x faster                                                    |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                    |
| async_tree_memoization     | 447 ms                                                       | 407 ms: 1.10x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                     |
| pprint_safe_repr           | 835 ms                                                       | 762 ms: 1.10x faster                                                     |
| richards_super             | 60.2 ms                                                      | 55.4 ms: 1.09x faster                                                    |
| float                      | 81.6 ms                                                      | 75.3 ms: 1.08x faster                                                    |
| json                       | 5.62 ms                                                      | 5.19 ms: 1.08x faster                                                    |
| xml_etree_generate         | 85.2 ms                                                      | 78.8 ms: 1.08x faster                                                    |
| pyflate                    | 493 ms                                                       | 456 ms: 1.08x faster                                                     |
| xml_etree_process          | 60.7 ms                                                      | 56.4 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 5.09 sec                                                     | 4.75 sec: 1.07x faster                                                   |
| scimark_fft                | 298 ms                                                       | 280 ms: 1.06x faster                                                     |
| pprint_pformat             | 1.70 sec                                                     | 1.60 sec: 1.06x faster                                                   |
| go                         | 167 ms                                                       | 158 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 823 ms                                                       | 782 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                     |
| crypto_pyaes               | 73.5 ms                                                      | 70.0 ms: 1.05x faster                                                    |
| deltablue                  | 3.38 ms                                                      | 3.23 ms: 1.05x faster                                                    |
| gc_traversal               | 4.48 ms                                                      | 4.31 ms: 1.04x faster                                                    |
| json_loads                 | 24.7 us                                                      | 23.8 us: 1.04x faster                                                    |
| async_tree_io              | 832 ms                                                       | 805 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                     |
| coverage                   | 84.5 ms                                                      | 82.6 ms: 1.02x faster                                                    |
| scimark_lu                 | 97.4 ms                                                      | 96.0 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.15 ms: 1.01x faster                                                    |
| asyncio_websockets         | 395 ms                                                       | 390 ms: 1.01x faster                                                     |
| dulwich_log                | 65.5 ms                                                      | 64.8 ms: 1.01x faster                                                    |
| regex_dna                  | 238 ms                                                       | 236 ms: 1.01x faster                                                     |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                    |
| regex_v8                   | 24.9 ms                                                      | 24.8 ms: 1.00x faster                                                    |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                     |
| html5lib                   | 72.9 ms                                                      | 73.1 ms: 1.00x slower                                                    |
| python_startup_no_site     | 8.93 ms                                                      | 8.97 ms: 1.00x slower                                                    |
| logging_silent             | 97.5 ns                                                      | 98.1 ns: 1.01x slower                                                    |
| pickle_pure_python         | 322 us                                                       | 325 us: 1.01x slower                                                     |
| unpickle_pure_python       | 216 us                                                       | 219 us: 1.01x slower                                                     |
| bench_thread_pool          | 929 us                                                       | 946 us: 1.02x slower                                                     |
| regex_effbot               | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                    |
| pycparser                  | 1.28 sec                                                     | 1.31 sec: 1.02x slower                                                   |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                    |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                   |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.03x slower                                                     |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                     |
| logging_format             | 6.95 us                                                      | 7.28 us: 1.05x slower                                                    |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                     |
| regex_compile              | 143 ms                                                       | 150 ms: 1.05x slower                                                     |
| sympy_expand               | 506 ms                                                       | 534 ms: 1.06x slower                                                     |
| logging_simple             | 6.28 us                                                      | 6.63 us: 1.06x slower                                                    |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.8 ms: 1.06x slower                                                    |
| sympy_str                  | 297 ms                                                       | 318 ms: 1.07x slower                                                     |
| 2to3                       | 293 ms                                                       | 315 ms: 1.08x slower                                                     |
| comprehensions             | 17.3 us                                                      | 18.7 us: 1.08x slower                                                    |
| hexiom                     | 6.47 ms                                                      | 7.09 ms: 1.09x slower                                                    |
| genshi_text                | 27.2 ms                                                      | 29.8 ms: 1.10x slower                                                    |
| generators                 | 33.9 ms                                                      | 37.3 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                    |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.11x slower                                                     |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.11x slower                                                    |
| sympy_sum                  | 154 ms                                                       | 172 ms: 1.12x slower                                                     |
| chaos                      | 60.6 ms                                                      | 68.0 ms: 1.12x slower                                                    |
| docutils                   | 2.81 sec                                                     | 3.17 sec: 1.13x slower                                                   |
| sqlglot_normalize          | 119 ms                                                       | 136 ms: 1.14x slower                                                     |
| genshi_xml                 | 58.0 ms                                                      | 66.2 ms: 1.14x slower                                                    |
| sympy_integrate            | 23.4 ms                                                      | 27.0 ms: 1.15x slower                                                    |
| pylint                     | 345 ms                                                       | 407 ms: 1.18x slower                                                     |
| django_template            | 38.9 ms                                                      | 46.0 ms: 1.18x slower                                                    |
| sqlglot_optimize           | 58.7 ms                                                      | 69.6 ms: 1.19x slower                                                    |
| raytrace                   | 267 ms                                                       | 323 ms: 1.21x slower                                                     |
| bench_mp_pool              | 4.82 ms                                                      | 3.26 sec: 676.07x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                             |

Benchmark hidden because not significant (4): thrift, xml_etree_iterparse, xml_etree_parse, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 85.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x