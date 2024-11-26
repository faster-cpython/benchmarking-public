# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.4 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 322 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 785 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 809 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 88.6 ms: 1.04x faster                                                       |
| float          | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                                       |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.58 ms: 1.02x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                       |
| regex_dna      | 238 ms                                                       | 248 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                       | 213 us: 1.02x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 84.8 ms: 1.01x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 2.64 sec: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 54.4 ms: 1.07x faster                                                       |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 286 us: 1.36x faster                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.01 ms: 1.32x faster                                                       |
| deepcopy_memo              | 38.9 us                                                      | 30.0 us: 1.30x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.89 us: 1.21x faster                                                       |
| go                         | 167 ms                                                       | 138 ms: 1.21x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_none            | 370 ms                                                       | 322 ms: 1.15x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.7 ms: 1.14x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 399 ms: 1.12x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 24.6 ms: 1.10x faster                                                       |
| scimark_sor                | 125 ms                                                       | 115 ms: 1.08x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.0 ms: 1.08x faster                                                       |
| bench_thread_pool          | 929 us                                                       | 865 us: 1.07x faster                                                        |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                                       |
| genshi_xml                 | 58.0 ms                                                      | 54.4 ms: 1.07x faster                                                       |
| fannkuch                   | 384 ms                                                       | 361 ms: 1.06x faster                                                        |
| thrift                     | 918 us                                                       | 863 us: 1.06x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.29 ms: 1.06x faster                                                       |
| richards                   | 52.5 ms                                                      | 49.7 ms: 1.06x faster                                                       |
| nqueens                    | 92.3 ms                                                      | 87.6 ms: 1.05x faster                                                       |
| async_tree_io_tg           | 823 ms                                                       | 785 ms: 1.05x faster                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 4.62 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 572 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.89 sec: 1.04x faster                                                      |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 803 ms: 1.04x faster                                                        |
| nbody                      | 92.1 ms                                                      | 88.6 ms: 1.04x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.23 sec: 1.04x faster                                                      |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                                        |
| async_tree_io              | 832 ms                                                       | 809 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| regex_compile              | 143 ms                                                       | 139 ms: 1.03x faster                                                        |
| float                      | 81.6 ms                                                      | 79.6 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.4 ms                                                      | 22.8 ms: 1.02x faster                                                       |
| coverage                   | 84.5 ms                                                      | 82.6 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 71.9 ms: 1.02x faster                                                       |
| hexiom                     | 6.47 ms                                                      | 6.33 ms: 1.02x faster                                                       |
| sympy_str                  | 297 ms                                                       | 290 ms: 1.02x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.4 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 389 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 213 us: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 498 ms: 1.02x faster                                                        |
| mdp                        | 2.53 sec                                                     | 2.49 sec: 1.02x faster                                                      |
| scimark_lu                 | 97.4 ms                                                      | 96.0 ms: 1.02x faster                                                       |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 358 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.9 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.16 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| pyflate                    | 493 ms                                                       | 487 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 152 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 58.3 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.8 ms: 1.01x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.2 us: 1.01x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                       |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 97.9 ns: 1.00x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 66.0 ms: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.58 ms: 1.02x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 66.9 ms: 1.02x slower                                                       |
| chaos                      | 60.6 ms                                                      | 62.0 ms: 1.02x slower                                                       |
| regex_v8                   | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.81 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| logging_simple             | 6.28 us                                                      | 6.50 us: 1.04x slower                                                       |
| logging_format             | 6.95 us                                                      | 7.21 us: 1.04x slower                                                       |
| regex_dna                  | 238 ms                                                       | 248 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.43 ms: 1.05x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                       |
| raytrace                   | 267 ms                                                       | 283 ms: 1.06x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.78 ms: 1.07x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.64 sec: 1.09x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (7): pickle_pure_python, scimark_fft, json_dumps, coroutines, deltablue, mako, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf2-x86_64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.91x