# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x faster
- HPT reliability: 88.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 309 ms: 1.06x slower                                                          |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                        |
| html5lib       | 71.9 ms                                                      | 70.6 ms: 1.02x faster                                                         |
| tornado_http   | 120 ms                                                       | 122 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                          |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                          |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                          |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                          |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                          |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                          |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                         |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                          |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                          |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 75.6 ms: 1.08x faster                                                         |
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                         |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 236 ms: 1.03x faster                                                          |
| regex_v8       | 26.2 ms                                                      | 26.1 ms: 1.01x faster                                                         |
| regex_compile  | 144 ms                                                       | 149 ms: 1.03x slower                                                          |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                        |
| xml_etree_process    | 60.9 ms                                                      | 56.5 ms: 1.08x faster                                                         |
| xml_etree_generate   | 85.3 ms                                                      | 79.9 ms: 1.07x faster                                                         |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                         |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                          |
| pickle_list          | 4.59 us                                                      | 4.52 us: 1.01x faster                                                         |
| xml_etree_iterparse  | 100 ms                                                       | 99.5 ms: 1.01x faster                                                         |
| unpickle_list        | 4.62 us                                                      | 4.67 us: 1.01x slower                                                         |
| unpickle_pure_python | 214 us                                                       | 217 us: 1.01x slower                                                          |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                         |
| pickle_dict          | 32.1 us                                                      | 32.7 us: 1.02x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                         |
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.21 ms: 1.13x faster                                                         |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                         |
| genshi_text     | 26.6 ms                                                      | 29.3 ms: 1.10x slower                                                         |
| genshi_xml      | 57.3 ms                                                      | 64.3 ms: 1.12x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.0 us: 1.41x faster                                                         |
| deepcopy                   | 397 us                                                       | 298 us: 1.33x faster                                                          |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                         |
| scimark_sor                | 126 ms                                                       | 106 ms: 1.18x faster                                                          |
| async_tree_memoization_tg  | 461 ms                                                       | 391 ms: 1.18x faster                                                          |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                          |
| richards                   | 52.7 ms                                                      | 45.9 ms: 1.15x faster                                                         |
| richards_super             | 59.8 ms                                                      | 52.8 ms: 1.13x faster                                                         |
| mako                       | 10.4 ms                                                      | 9.21 ms: 1.13x faster                                                         |
| tomli_loads                | 2.41 sec                                                     | 2.13 sec: 1.13x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 404 ms: 1.12x faster                                                          |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                         |
| pyflate                    | 492 ms                                                       | 446 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                          |
| scimark_fft                | 314 ms                                                       | 289 ms: 1.09x faster                                                          |
| float                      | 81.9 ms                                                      | 75.6 ms: 1.08x faster                                                         |
| xml_etree_process          | 60.9 ms                                                      | 56.5 ms: 1.08x faster                                                         |
| go                         | 160 ms                                                       | 150 ms: 1.07x faster                                                          |
| xml_etree_generate         | 85.3 ms                                                      | 79.9 ms: 1.07x faster                                                         |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.02 ms: 1.07x faster                                                         |
| deltablue                  | 3.41 ms                                                      | 3.21 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 5.10 sec                                                     | 4.82 sec: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.06x faster                                                          |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 545 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                          |
| telco                      | 8.58 ms                                                      | 8.30 ms: 1.03x faster                                                         |
| async_tree_io_tg           | 819 ms                                                       | 792 ms: 1.03x faster                                                          |
| regex_dna                  | 244 ms                                                       | 236 ms: 1.03x faster                                                          |
| sqlite_synth               | 2.79 us                                                      | 2.72 us: 1.03x faster                                                         |
| pprint_safe_repr           | 812 ms                                                       | 792 ms: 1.02x faster                                                          |
| crypto_pyaes               | 72.8 ms                                                      | 71.1 ms: 1.02x faster                                                         |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                         |
| html5lib                   | 71.9 ms                                                      | 70.6 ms: 1.02x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 64.4 ms: 1.02x faster                                                         |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                          |
| pickle_list                | 4.59 us                                                      | 4.52 us: 1.01x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                         |
| scimark_lu                 | 97.8 ms                                                      | 96.8 ms: 1.01x faster                                                         |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                          |
| regex_v8                   | 26.2 ms                                                      | 26.1 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 100 ms                                                       | 99.5 ms: 1.01x faster                                                         |
| coverage                   | 81.1 ms                                                      | 80.8 ms: 1.00x faster                                                         |
| python_startup_no_site     | 8.94 ms                                                      | 8.98 ms: 1.00x slower                                                         |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                         |
| logging_format             | 7.07 us                                                      | 7.12 us: 1.01x slower                                                         |
| unpickle_list              | 4.62 us                                                      | 4.67 us: 1.01x slower                                                         |
| unpickle_pure_python       | 214 us                                                       | 217 us: 1.01x slower                                                          |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                         |
| thrift                     | 877 us                                                       | 889 us: 1.01x slower                                                          |
| bench_thread_pool          | 901 us                                                       | 915 us: 1.02x slower                                                          |
| pickle_dict                | 32.1 us                                                      | 32.7 us: 1.02x slower                                                         |
| tornado_http               | 120 ms                                                       | 122 ms: 1.02x slower                                                          |
| pycparser                  | 1.26 sec                                                     | 1.28 sec: 1.02x slower                                                        |
| logging_simple             | 6.40 us                                                      | 6.53 us: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                          |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.03x slower                                                          |
| mdp                        | 2.52 sec                                                     | 2.59 sec: 1.03x slower                                                        |
| regex_compile              | 144 ms                                                       | 149 ms: 1.03x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                          |
| sympy_expand               | 505 ms                                                       | 525 ms: 1.04x slower                                                          |
| sympy_str                  | 296 ms                                                       | 309 ms: 1.05x slower                                                          |
| django_template            | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                         |
| typing_runtime_protocols   | 174 us                                                       | 183 us: 1.05x slower                                                          |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                         |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.8 ms: 1.06x slower                                                         |
| logging_silent             | 97.7 ns                                                      | 104 ns: 1.06x slower                                                          |
| 2to3                       | 291 ms                                                       | 309 ms: 1.06x slower                                                          |
| raytrace                   | 289 ms                                                       | 309 ms: 1.07x slower                                                          |
| chaos                      | 61.7 ms                                                      | 66.0 ms: 1.07x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.07x slower                                                         |
| gc_traversal               | 4.11 ms                                                      | 4.41 ms: 1.07x slower                                                         |
| async_generators           | 359 ms                                                       | 386 ms: 1.08x slower                                                          |
| create_gc_cycles           | 1.76 ms                                                      | 1.91 ms: 1.09x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.93 ms: 1.09x slower                                                         |
| generators                 | 33.5 ms                                                      | 36.8 ms: 1.10x slower                                                         |
| sympy_sum                  | 154 ms                                                       | 169 ms: 1.10x slower                                                          |
| genshi_text                | 26.6 ms                                                      | 29.3 ms: 1.10x slower                                                         |
| sqlglot_optimize           | 59.7 ms                                                      | 66.3 ms: 1.11x slower                                                         |
| hexiom                     | 6.33 ms                                                      | 7.06 ms: 1.12x slower                                                         |
| nqueens                    | 88.2 ms                                                      | 98.6 ms: 1.12x slower                                                         |
| sqlglot_normalize          | 118 ms                                                       | 132 ms: 1.12x slower                                                          |
| genshi_xml                 | 57.3 ms                                                      | 64.3 ms: 1.12x slower                                                         |
| sympy_integrate            | 23.3 ms                                                      | 26.4 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 5.31 ms: 1.14x slower                                                         |
| pylint                     | 346 ms                                                       | 410 ms: 1.18x slower                                                          |
| unpack_sequence            | 56.8 ns                                                      | 88.0 ns: 1.55x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                  |

Benchmark hidden because not significant (7): pprint_pformat, asyncio_tcp, json_loads, asyncio_tcp_ssl, unpickle, json, fannkuch
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 88.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x