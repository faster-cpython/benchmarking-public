# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-x86_64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 786 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 357 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 78.0 ms: 1.05x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| regex_dna      | 238 ms                                                       | 248 ms: 1.04x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 312 us: 1.03x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.2 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 217 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.2 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 40.6 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 282 us: 1.38x faster                                                        |
| deepcopy_memo              | 38.9 us                                                      | 28.8 us: 1.35x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.97 ms: 1.34x faster                                                       |
| go                         | 167 ms                                                       | 132 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.92 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| generators                 | 33.9 ms                                                      | 28.8 ms: 1.18x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 320 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| genshi_text                | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| fannkuch                   | 384 ms                                                       | 352 ms: 1.09x faster                                                        |
| thrift                     | 918 us                                                       | 852 us: 1.08x faster                                                        |
| genshi_xml                 | 58.0 ms                                                      | 54.2 ms: 1.07x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.20 ms: 1.07x faster                                                       |
| richards_super             | 60.2 ms                                                      | 56.4 ms: 1.07x faster                                                       |
| json                       | 5.62 ms                                                      | 5.34 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 786 ms: 1.05x faster                                                        |
| float                      | 81.6 ms                                                      | 78.0 ms: 1.05x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.19 ms: 1.05x faster                                                       |
| richards                   | 52.5 ms                                                      | 50.2 ms: 1.05x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                                      |
| scimark_sor                | 125 ms                                                       | 120 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 93.7 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 282 ms: 1.04x faster                                                        |
| sympy_expand               | 506 ms                                                       | 488 ms: 1.04x faster                                                        |
| nqueens                    | 92.3 ms                                                      | 88.9 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| logging_format             | 6.95 us                                                      | 6.74 us: 1.03x faster                                                       |
| typing_runtime_protocols   | 176 us                                                       | 170 us: 1.03x faster                                                        |
| coverage                   | 84.5 ms                                                      | 82.0 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                        |
| pickle_pure_python         | 322 us                                                       | 312 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.95 sec: 1.03x faster                                                      |
| bench_thread_pool          | 929 us                                                       | 904 us: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| sympy_str                  | 297 ms                                                       | 289 ms: 1.03x faster                                                        |
| scimark_fft                | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.46 sec: 1.03x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 814 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.2 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                      | 6.13 us: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 71.9 ms: 1.02x faster                                                       |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 357 ms: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                                      |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.34 ms: 1.01x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.48 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.45 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.00x faster                                                       |
| pyflate                    | 493 ms                                                       | 490 ms: 1.00x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 97.2 ms: 1.00x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 217 us: 1.01x slower                                                        |
| raytrace                   | 267 ms                                                       | 269 ms: 1.01x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 66.1 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 65.9 ms: 1.01x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 98.6 ns: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 102 ms: 1.02x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.03x slower                                                      |
| sqlglot_parse              | 1.37 ms                                                      | 1.40 ms: 1.03x slower                                                       |
| chaos                      | 60.6 ms                                                      | 62.3 ms: 1.03x slower                                                       |
| regex_dna                  | 238 ms                                                       | 248 ms: 1.04x slower                                                        |
| django_template            | 38.9 ms                                                      | 40.6 ms: 1.04x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 26.2 ms: 1.05x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                      |
| bench_mp_pool              | 4.82 ms                                                      | 1.40 sec: 290.89x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (8): nbody, async_tree_io, asyncio_websockets, mako, json_dumps, sqlglot_optimize, scimark_sparse_mat_mult, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x