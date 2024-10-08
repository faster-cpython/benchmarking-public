# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.03x faster
- HPT reliability: 71.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 243 ms: 1.12x slower                                                         |
| docutils       | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                       |
| tornado_http   | 89.5 ms                                                     | 97.2 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                         |
| async_tree_none            | 291 ms                                                      | 203 ms: 1.44x faster                                                         |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                         |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                                         |
| async_tree_memoization     | 339 ms                                                      | 257 ms: 1.32x faster                                                         |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                         |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                                         |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.8 ms: 1.44x faster                                                        |
| float          | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                        |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                         |
| regex_compile  | 87.5 ms                                                     | 95.1 ms: 1.09x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 16.0 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.09x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                        |
| pickle_dict          | 18.4 us                                                     | 17.7 us: 1.04x faster                                                        |
| pickle               | 7.43 us                                                     | 7.25 us: 1.02x faster                                                        |
| pickle_pure_python   | 195 us                                                      | 197 us: 1.01x slower                                                         |
| xml_etree_parse      | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 5.91 ms: 1.04x slower                                                        |
| unpickle_list        | 2.75 us                                                     | 2.86 us: 1.04x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                         |
| unpickle             | 8.18 us                                                     | 9.03 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                        |
| python_startup         | 19.5 ms                                                     | 22.6 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.00 ms: 1.42x faster                                                        |
| django_template | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.0 ms: 1.52x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 15.7 us: 1.51x faster                                                        |
| nbody                      | 71.9 ms                                                     | 49.8 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                         |
| async_tree_none            | 291 ms                                                      | 203 ms: 1.44x faster                                                         |
| async_tree_none_tg         | 285 ms                                                      | 199 ms: 1.43x faster                                                         |
| mako                       | 7.09 ms                                                     | 5.00 ms: 1.42x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 548 ms: 1.41x faster                                                         |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 257 ms: 1.32x faster                                                         |
| scimark_sor                | 78.8 ms                                                     | 60.5 ms: 1.30x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.29x faster                                                       |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                         |
| float                      | 56.8 ms                                                     | 44.4 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                         |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                         |
| crypto_pyaes               | 48.5 ms                                                     | 38.8 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 392 ms: 1.25x faster                                                         |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                         |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.17 ms: 1.18x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.84 ms: 1.17x faster                                                        |
| pyflate                    | 295 ms                                                      | 261 ms: 1.13x faster                                                         |
| xml_etree_generate         | 55.8 ms                                                     | 49.7 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.10x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.3 ms: 1.08x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 35.0 ms: 1.08x faster                                                        |
| chaos                      | 43.3 ms                                                     | 40.6 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.5 ms: 1.06x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 812 us: 1.05x faster                                                         |
| logging_simple             | 6.28 us                                                     | 5.96 us: 1.05x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.39 us: 1.05x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 57.9 ns: 1.04x faster                                                        |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                         |
| pickle_dict                | 18.4 us                                                     | 17.7 us: 1.04x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 60.8 ms: 1.03x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.25 us: 1.02x faster                                                        |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                         |
| json                       | 3.05 ms                                                     | 2.99 ms: 1.02x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.0 ms: 1.02x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 79.6 ms: 1.01x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.1 ms: 1.01x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 197 us: 1.01x slower                                                         |
| xml_etree_parse            | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.54 ms: 1.01x slower                                                        |
| go                         | 91.6 ms                                                     | 92.7 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 523 ms: 1.02x slower                                                         |
| pycparser                  | 699 ms                                                      | 716 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 5.91 ms: 1.04x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 72.1 ms: 1.04x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                       |
| async_generators           | 239 ms                                                      | 257 ms: 1.07x slower                                                         |
| sympy_sum                  | 91.5 ms                                                     | 98.3 ms: 1.07x slower                                                        |
| sympy_str                  | 175 ms                                                      | 188 ms: 1.08x slower                                                         |
| sqlglot_normalize          | 187 ms                                                      | 201 ms: 1.08x slower                                                         |
| tornado_http               | 89.5 ms                                                     | 97.2 ms: 1.09x slower                                                        |
| raytrace                   | 192 ms                                                      | 209 ms: 1.09x slower                                                         |
| regex_compile              | 87.5 ms                                                     | 95.1 ms: 1.09x slower                                                        |
| unpickle                   | 8.18 us                                                     | 9.03 us: 1.10x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.57 ms: 1.11x slower                                                        |
| 2to3                       | 218 ms                                                      | 243 ms: 1.12x slower                                                         |
| sqlglot_parse              | 804 us                                                      | 898 us: 1.12x slower                                                         |
| regex_v8                   | 14.2 ms                                                     | 16.0 ms: 1.13x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.14x slower                                                         |
| sympy_integrate            | 13.0 ms                                                     | 14.8 ms: 1.15x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.91 sec: 1.15x slower                                                       |
| django_template            | 22.9 ms                                                     | 26.6 ms: 1.16x slower                                                        |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                         |
| python_startup             | 19.5 ms                                                     | 22.6 ms: 1.16x slower                                                        |
| coverage                   | 40.8 ms                                                     | 47.7 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 40.4 ms: 1.17x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 896 us: 1.19x slower                                                         |
| hexiom                     | 4.10 ms                                                     | 4.90 ms: 1.20x slower                                                        |
| richards_super             | 32.1 ms                                                     | 39.8 ms: 1.24x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 611 ms: 1.25x slower                                                         |
| richards                   | 28.4 ms                                                     | 37.3 ms: 1.31x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 58.8 ns: 1.57x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): regex_effbot, pickle_list, generators, fannkuch
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 71.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown