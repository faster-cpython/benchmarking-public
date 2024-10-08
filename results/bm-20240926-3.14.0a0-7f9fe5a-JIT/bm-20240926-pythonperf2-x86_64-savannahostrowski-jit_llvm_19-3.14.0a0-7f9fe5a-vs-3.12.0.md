# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.01x faster
- HPT reliability: 66.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 309 ms: 1.08x slower                                                          |
| docutils       | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                          |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                          |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                          |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                          |
| nbody          | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 75.6 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                          |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                         |
| regex_compile  | 144 ms                                                       | 149 ms: 1.04x slower                                                          |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.9 ms: 1.08x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 99.5 ms: 1.03x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                         |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.02x faster                                                         |
| tomli_loads          | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                          |
| pickle_dict          | 32.5 us                                                      | 32.7 us: 1.00x slower                                                         |
| pickle               | 10.5 us                                                      | 10.7 us: 1.01x slower                                                         |
| pickle_list          | 4.43 us                                                      | 4.52 us: 1.02x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                          |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                  |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                         |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                         |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.21 ms: 1.09x faster                                                         |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                          |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                          |
| async_tree_memoization_tg  | 540 ms                                                       | 391 ms: 1.38x faster                                                          |
| async_tree_memoization     | 544 ms                                                       | 404 ms: 1.35x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 792 ms: 1.33x faster                                                          |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 802 ms: 1.30x faster                                                          |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 545 ms: 1.28x faster                                                          |
| deepcopy                   | 368 us                                                       | 298 us: 1.24x faster                                                          |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                          |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.5 us: 1.19x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 81.4 ms: 1.13x faster                                                         |
| mako                       | 10.0 ms                                                      | 9.21 ms: 1.09x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 79.9 ms: 1.08x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                         |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                          |
| nbody                      | 88.0 ms                                                      | 83.5 ms: 1.05x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.12 us: 1.05x faster                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.02 ms: 1.05x faster                                                         |
| scimark_fft                | 301 ms                                                       | 289 ms: 1.04x faster                                                          |
| bench_thread_pool          | 950 us                                                       | 915 us: 1.04x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 99.5 ms: 1.03x faster                                                         |
| xml_etree_process          | 58.4 ms                                                      | 56.5 ms: 1.03x faster                                                         |
| logging_simple             | 6.71 us                                                      | 6.53 us: 1.03x faster                                                         |
| scimark_sor                | 109 ms                                                       | 106 ms: 1.02x faster                                                          |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 96.8 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                                          |
| generators                 | 37.4 ms                                                      | 36.8 ms: 1.02x faster                                                         |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.02x faster                                                         |
| dulwich_log                | 65.4 ms                                                      | 64.4 ms: 1.02x faster                                                         |
| float                      | 76.6 ms                                                      | 75.6 ms: 1.01x faster                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.13 sec: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                          |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                          |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                        |
| go                         | 150 ms                                                       | 150 ms: 1.00x slower                                                          |
| pickle_dict                | 32.5 us                                                      | 32.7 us: 1.00x slower                                                         |
| asyncio_tcp                | 378 ms                                                       | 379 ms: 1.00x slower                                                          |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 392 ms: 1.01x slower                                                          |
| pickle                     | 10.5 us                                                      | 10.7 us: 1.01x slower                                                         |
| pyflate                    | 439 ms                                                       | 446 ms: 1.02x slower                                                          |
| pickle_list                | 4.43 us                                                      | 4.52 us: 1.02x slower                                                         |
| json                       | 5.12 ms                                                      | 5.24 ms: 1.02x slower                                                         |
| sympy_str                  | 302 ms                                                       | 309 ms: 1.02x slower                                                          |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.02x slower                                                         |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.03x slower                                                          |
| richards_super             | 51.3 ms                                                      | 52.8 ms: 1.03x slower                                                         |
| chaos                      | 64.0 ms                                                      | 66.0 ms: 1.03x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                                          |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                          |
| regex_compile              | 144 ms                                                       | 149 ms: 1.04x slower                                                          |
| raytrace                   | 298 ms                                                       | 309 ms: 1.04x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 169 ms: 1.04x slower                                                          |
| fannkuch                   | 350 ms                                                       | 366 ms: 1.04x slower                                                          |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                         |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.07x slower                                                         |
| 2to3                       | 285 ms                                                       | 309 ms: 1.08x slower                                                          |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.09x slower                                                          |
| sqlglot_transpile          | 1.78 ms                                                      | 1.93 ms: 1.09x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 98.6 ms: 1.10x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 104 ns: 1.10x slower                                                          |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 26.4 ms: 1.10x slower                                                         |
| docutils                   | 2.87 sec                                                     | 3.18 sec: 1.11x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.31 ms: 1.12x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 132 ms: 1.14x slower                                                          |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 66.3 ms: 1.15x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 7.06 ms: 1.19x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.30 ms: 1.19x slower                                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                          |
| coverage                   | 66.7 ms                                                      | 80.8 ms: 1.21x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 4.41 ms: 1.27x slower                                                         |
| unpack_sequence            | 53.2 ns                                                      | 88.0 ns: 1.65x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): scimark_monte_carlo, unpickle_list, richards, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 66.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x