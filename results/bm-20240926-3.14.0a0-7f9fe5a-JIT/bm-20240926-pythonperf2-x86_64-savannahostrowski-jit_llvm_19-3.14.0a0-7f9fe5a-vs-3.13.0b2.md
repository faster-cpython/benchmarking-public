# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.01x faster
- HPT reliability: 81.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 309 ms: 1.06x slower                                                          |
| docutils       | 2.98 sec                                                         | 3.18 sec: 1.07x slower                                                        |
| html5lib       | 74.7 ms                                                          | 70.6 ms: 1.06x faster                                                         |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                          |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                          |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                          |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                          |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                                          |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                          |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.6 ms: 1.06x faster                                                         |
| nbody          | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                         |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.06x faster                                                          |
| regex_v8       | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                         |
| regex_compile  | 144 ms                                                           | 149 ms: 1.04x slower                                                          |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 79.9 ms: 1.07x faster                                                         |
| xml_etree_process    | 59.7 ms                                                          | 56.5 ms: 1.06x faster                                                         |
| json_loads           | 25.0 us                                                          | 24.0 us: 1.04x faster                                                         |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                          |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                           | 99.5 ms: 1.03x faster                                                         |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                          |
| pickle_dict          | 32.8 us                                                          | 32.7 us: 1.01x faster                                                         |
| pickle               | 10.6 us                                                          | 10.7 us: 1.00x slower                                                         |
| pickle_list          | 4.44 us                                                          | 4.52 us: 1.02x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 330 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                         |
| python_startup_no_site | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.21 ms: 1.13x faster                                                         |
| django_template | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                         |
| genshi_xml      | 58.1 ms                                                          | 64.3 ms: 1.11x slower                                                         |
| genshi_text     | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                         |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.0 us: 1.33x faster                                                         |
| deepcopy                   | 377 us                                                           | 298 us: 1.27x faster                                                          |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                         |
| richards                   | 53.4 ms                                                          | 45.9 ms: 1.17x faster                                                         |
| richards_super             | 61.2 ms                                                          | 52.8 ms: 1.16x faster                                                         |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                         |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                          |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                          |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                          |
| tomli_loads                | 2.40 sec                                                         | 2.13 sec: 1.13x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.21 ms: 1.13x faster                                                         |
| scimark_sor                | 119 ms                                                           | 106 ms: 1.11x faster                                                          |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                          |
| go                         | 165 ms                                                           | 150 ms: 1.10x faster                                                          |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                                          |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                         |
| scimark_fft                | 312 ms                                                           | 289 ms: 1.08x faster                                                          |
| pyflate                    | 482 ms                                                           | 446 ms: 1.08x faster                                                          |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                          |
| xml_etree_generate         | 85.7 ms                                                          | 79.9 ms: 1.07x faster                                                         |
| bpe_tokeniser              | 5.14 sec                                                         | 4.82 sec: 1.07x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.02 ms: 1.07x faster                                                         |
| gc_traversal               | 4.69 ms                                                          | 4.41 ms: 1.06x faster                                                         |
| float                      | 80.2 ms                                                          | 75.6 ms: 1.06x faster                                                         |
| html5lib                   | 74.7 ms                                                          | 70.6 ms: 1.06x faster                                                         |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.06x faster                                                          |
| xml_etree_process          | 59.7 ms                                                          | 56.5 ms: 1.06x faster                                                         |
| nbody                      | 87.8 ms                                                          | 83.5 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                          |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                          |
| create_gc_cycles           | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                         |
| dulwich_log                | 67.3 ms                                                          | 64.4 ms: 1.05x faster                                                         |
| json_loads                 | 25.0 us                                                          | 24.0 us: 1.04x faster                                                         |
| crypto_pyaes               | 73.6 ms                                                          | 71.1 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                          |
| unpickle                   | 15.7 us                                                          | 15.2 us: 1.03x faster                                                         |
| coverage                   | 83.5 ms                                                          | 80.8 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 818 ms                                                           | 792 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                           | 99.5 ms: 1.03x faster                                                         |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.80 us                                                          | 2.72 us: 1.03x faster                                                         |
| json                       | 5.35 ms                                                          | 5.24 ms: 1.02x faster                                                         |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                          |
| asyncio_websockets         | 395 ms                                                           | 392 ms: 1.01x faster                                                          |
| scimark_lu                 | 97.5 ms                                                          | 96.8 ms: 1.01x faster                                                         |
| pickle_dict                | 32.8 us                                                          | 32.7 us: 1.01x faster                                                         |
| regex_v8                   | 26.0 ms                                                          | 26.1 ms: 1.00x slower                                                         |
| asyncio_tcp                | 378 ms                                                           | 379 ms: 1.00x slower                                                          |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.00x slower                                                         |
| thrift                     | 880 us                                                           | 889 us: 1.01x slower                                                          |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                         |
| pickle_list                | 4.44 us                                                          | 4.52 us: 1.02x slower                                                         |
| logging_simple             | 6.40 us                                                          | 6.53 us: 1.02x slower                                                         |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                          |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.03x slower                                                          |
| regex_compile              | 144 ms                                                           | 149 ms: 1.04x slower                                                          |
| fannkuch                   | 353 ms                                                           | 366 ms: 1.04x slower                                                          |
| regex_effbot               | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                         |
| django_template            | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                         |
| sympy_expand               | 501 ms                                                           | 525 ms: 1.05x slower                                                          |
| sympy_str                  | 295 ms                                                           | 309 ms: 1.05x slower                                                          |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.8 ms: 1.05x slower                                                         |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                        |
| 2to3                       | 291 ms                                                           | 309 ms: 1.06x slower                                                          |
| sqlglot_parse              | 1.39 ms                                                          | 1.48 ms: 1.06x slower                                                         |
| async_generators           | 363 ms                                                           | 386 ms: 1.07x slower                                                          |
| docutils                   | 2.98 sec                                                         | 3.18 sec: 1.07x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 330 us: 1.07x slower                                                          |
| typing_runtime_protocols   | 171 us                                                           | 183 us: 1.07x slower                                                          |
| logging_silent             | 96.3 ns                                                          | 104 ns: 1.08x slower                                                          |
| bench_mp_pool              | 4.91 ms                                                          | 5.31 ms: 1.08x slower                                                         |
| comprehensions             | 17.0 us                                                          | 18.5 us: 1.09x slower                                                         |
| sympy_sum                  | 155 ms                                                           | 169 ms: 1.09x slower                                                          |
| sqlglot_transpile          | 1.76 ms                                                          | 1.93 ms: 1.10x slower                                                         |
| generators                 | 33.5 ms                                                          | 36.8 ms: 1.10x slower                                                         |
| sqlglot_normalize          | 120 ms                                                           | 132 ms: 1.10x slower                                                          |
| genshi_xml                 | 58.1 ms                                                          | 64.3 ms: 1.11x slower                                                         |
| chaos                      | 59.6 ms                                                          | 66.0 ms: 1.11x slower                                                         |
| hexiom                     | 6.35 ms                                                          | 7.06 ms: 1.11x slower                                                         |
| sqlglot_optimize           | 59.5 ms                                                          | 66.3 ms: 1.11x slower                                                         |
| nqueens                    | 88.4 ms                                                          | 98.6 ms: 1.12x slower                                                         |
| genshi_text                | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                         |
| sympy_integrate            | 23.2 ms                                                          | 26.4 ms: 1.14x slower                                                         |
| raytrace                   | 260 ms                                                           | 309 ms: 1.19x slower                                                          |
| pylint                     | 339 ms                                                           | 410 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                  |

Benchmark hidden because not significant (6): telco, unpickle_list, json_dumps, asyncio_tcp_ssl, logging_format, bench_thread_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: unpack_sequence

# HPT report

- Reliability score: 81.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x