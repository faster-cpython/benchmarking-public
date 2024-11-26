# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.021x faster
- HPT reliability: 93.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 309 ms: 1.06x slower                                                          |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                        |
| html5lib       | 72.9 ms                                                      | 70.6 ms: 1.03x faster                                                         |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                          |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                          |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                          |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                          |
| async_tree_io              | 832 ms                                                       | 802 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                          |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                         |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.5 ms: 1.10x faster                                                         |
| float          | 81.6 ms                                                      | 75.6 ms: 1.08x faster                                                         |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 236 ms: 1.01x faster                                                          |
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 26.1 ms: 1.04x slower                                                         |
| regex_compile  | 143 ms                                                       | 149 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads        | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                        |
| xml_etree_process  | 60.7 ms                                                      | 56.5 ms: 1.07x faster                                                         |
| xml_etree_generate | 85.2 ms                                                      | 79.9 ms: 1.07x faster                                                         |
| json_loads         | 24.7 us                                                      | 24.0 us: 1.03x faster                                                         |
| json_dumps         | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                         |
| xml_etree_parse    | 144 ms                                                       | 142 ms: 1.01x faster                                                          |
| pickle_pure_python | 322 us                                                       | 330 us: 1.02x slower                                                          |
| Geometric mean     | (ref)                                                        | 1.03x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                         |
| python_startup_no_site | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.21 ms: 1.12x faster                                                         |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                         |
| genshi_text     | 27.2 ms                                                      | 29.3 ms: 1.08x slower                                                         |
| genshi_xml      | 58.0 ms                                                      | 64.3 ms: 1.11x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                         |
| deepcopy_memo              | 38.9 us                                                      | 28.0 us: 1.39x faster                                                         |
| deepcopy                   | 388 us                                                       | 298 us: 1.30x faster                                                          |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 2.95 us: 1.18x faster                                                         |
| scimark_sor                | 125 ms                                                       | 106 ms: 1.17x faster                                                          |
| async_tree_memoization_tg  | 458 ms                                                       | 391 ms: 1.17x faster                                                          |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                         |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                          |
| richards                   | 52.5 ms                                                      | 45.9 ms: 1.14x faster                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                        |
| richards_super             | 60.2 ms                                                      | 52.8 ms: 1.14x faster                                                         |
| mako                       | 10.3 ms                                                      | 9.21 ms: 1.12x faster                                                         |
| go                         | 167 ms                                                       | 150 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 342 ms                                                       | 308 ms: 1.11x faster                                                          |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                         |
| pyflate                    | 493 ms                                                       | 446 ms: 1.11x faster                                                          |
| nbody                      | 92.1 ms                                                      | 83.5 ms: 1.10x faster                                                         |
| float                      | 81.6 ms                                                      | 75.6 ms: 1.08x faster                                                         |
| xml_etree_process          | 60.7 ms                                                      | 56.5 ms: 1.07x faster                                                         |
| json                       | 5.62 ms                                                      | 5.24 ms: 1.07x faster                                                         |
| xml_etree_generate         | 85.2 ms                                                      | 79.9 ms: 1.07x faster                                                         |
| telco                      | 8.77 ms                                                      | 8.30 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.82 sec: 1.06x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                                          |
| deltablue                  | 3.38 ms                                                      | 3.21 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                          |
| fannkuch                   | 384 ms                                                       | 366 ms: 1.05x faster                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.02 ms: 1.05x faster                                                         |
| coverage                   | 84.5 ms                                                      | 80.8 ms: 1.05x faster                                                         |
| async_tree_io_tg           | 823 ms                                                       | 792 ms: 1.04x faster                                                          |
| async_tree_io              | 832 ms                                                       | 802 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.70 sec                                                     | 1.64 sec: 1.04x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 71.1 ms: 1.03x faster                                                         |
| html5lib                   | 72.9 ms                                                      | 70.6 ms: 1.03x faster                                                         |
| scimark_fft                | 298 ms                                                       | 289 ms: 1.03x faster                                                          |
| thrift                     | 918 us                                                       | 889 us: 1.03x faster                                                          |
| json_loads                 | 24.7 us                                                      | 24.0 us: 1.03x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 64.4 ms: 1.02x faster                                                         |
| bench_thread_pool          | 929 us                                                       | 915 us: 1.02x faster                                                          |
| gc_traversal               | 4.48 ms                                                      | 4.41 ms: 1.02x faster                                                         |
| regex_dna                  | 238 ms                                                       | 236 ms: 1.01x faster                                                          |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                         |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                          |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                          |
| scimark_lu                 | 97.4 ms                                                      | 96.8 ms: 1.01x faster                                                         |
| python_startup_no_site     | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                         |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                          |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.12 us: 1.02x slower                                                         |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.02x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 330 us: 1.02x slower                                                          |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                          |
| sympy_expand               | 506 ms                                                       | 525 ms: 1.04x slower                                                          |
| logging_simple             | 6.28 us                                                      | 6.53 us: 1.04x slower                                                         |
| sympy_str                  | 297 ms                                                       | 309 ms: 1.04x slower                                                          |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                          |
| regex_v8                   | 24.9 ms                                                      | 26.1 ms: 1.04x slower                                                         |
| regex_compile              | 143 ms                                                       | 149 ms: 1.05x slower                                                          |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.8 ms: 1.05x slower                                                         |
| 2to3                       | 293 ms                                                       | 309 ms: 1.06x slower                                                          |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                          |
| logging_silent             | 97.5 ns                                                      | 104 ns: 1.06x slower                                                          |
| nqueens                    | 92.3 ms                                                      | 98.6 ms: 1.07x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 29.3 ms: 1.08x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.48 ms: 1.08x slower                                                         |
| generators                 | 33.9 ms                                                      | 36.8 ms: 1.08x slower                                                         |
| chaos                      | 60.6 ms                                                      | 66.0 ms: 1.09x slower                                                         |
| hexiom                     | 6.47 ms                                                      | 7.06 ms: 1.09x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.93 ms: 1.10x slower                                                         |
| sympy_sum                  | 154 ms                                                       | 169 ms: 1.10x slower                                                          |
| bench_mp_pool              | 4.82 ms                                                      | 5.31 ms: 1.10x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 64.3 ms: 1.11x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                                          |
| sympy_integrate            | 23.4 ms                                                      | 26.4 ms: 1.13x slower                                                         |
| sqlglot_optimize           | 58.7 ms                                                      | 66.3 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                        |
| raytrace                   | 267 ms                                                       | 309 ms: 1.16x slower                                                          |
| pylint                     | 345 ms                                                       | 410 ms: 1.19x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, xml_etree_iterparse, pycparser, unpickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x faster
# HPT report

- Reliability score: 93.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x