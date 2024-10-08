# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.02x slower
- HPT reliability: 99.90%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 243 ms: 1.18x slower                                                         |
| docutils       | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                       |
| html5lib       | 35.0 ms                                                         | 41.8 ms: 1.19x slower                                                        |
| tornado_http   | 81.8 ms                                                         | 97.2 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                           | 1.18x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 548 ms: 1.10x faster                                                         |
| async_tree_none            | 218 ms                                                          | 203 ms: 1.07x faster                                                         |
| async_tree_memoization     | 264 ms                                                          | 257 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.8 ms: 1.36x faster                                                        |
| float          | 49.7 ms                                                         | 44.4 ms: 1.12x faster                                                        |
| pidigits       | 150 ms                                                          | 149 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                        |
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                         |
| regex_compile  | 78.0 ms                                                         | 95.1 ms: 1.22x slower                                                        |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 49.7 ms: 1.07x faster                                                        |
| xml_etree_process    | 36.4 ms                                                         | 35.0 ms: 1.04x faster                                                        |
| pickle_list          | 2.90 us                                                         | 2.82 us: 1.03x faster                                                        |
| pickle_dict          | 18.1 us                                                         | 17.7 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                        |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                        |
| pickle               | 7.11 us                                                         | 7.25 us: 1.02x slower                                                        |
| xml_etree_parse      | 90.9 ms                                                         | 94.1 ms: 1.03x slower                                                        |
| json_dumps           | 5.61 ms                                                         | 5.91 ms: 1.05x slower                                                        |
| unpickle             | 8.40 us                                                         | 9.03 us: 1.07x slower                                                        |
| unpickle_list        | 2.62 us                                                         | 2.86 us: 1.09x slower                                                        |
| pickle_pure_python   | 175 us                                                          | 197 us: 1.13x slower                                                         |
| unpickle_pure_python | 122 us                                                          | 142 us: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.6 ms: 1.12x slower                                                        |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.00 ms: 1.27x faster                                                        |
| django_template | 21.7 ms                                                         | 26.6 ms: 1.23x slower                                                        |
| genshi_text     | 14.4 ms                                                         | 19.3 ms: 1.34x slower                                                        |
| genshi_xml      | 31.6 ms                                                         | 46.0 ms: 1.46x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.17x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 510 us: 15.89x faster                                                        |
| spectral_norm              | 63.7 ms                                                         | 44.0 ms: 1.45x faster                                                        |
| deepcopy_memo              | 22.1 us                                                         | 15.7 us: 1.41x faster                                                        |
| nbody                      | 67.6 ms                                                         | 49.8 ms: 1.36x faster                                                        |
| mako                       | 6.36 ms                                                         | 5.00 ms: 1.27x faster                                                        |
| scimark_sor                | 75.3 ms                                                         | 60.5 ms: 1.24x faster                                                        |
| deepcopy                   | 220 us                                                          | 185 us: 1.19x faster                                                         |
| crypto_pyaes               | 45.5 ms                                                         | 38.8 ms: 1.17x faster                                                        |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.17 ms: 1.15x faster                                                        |
| scimark_fft                | 171 ms                                                          | 149 ms: 1.15x faster                                                         |
| float                      | 49.7 ms                                                         | 44.4 ms: 1.12x faster                                                        |
| async_tree_io_tg           | 605 ms                                                          | 548 ms: 1.10x faster                                                         |
| tomli_loads                | 1.35 sec                                                        | 1.25 sec: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 203 ms: 1.07x faster                                                         |
| xml_etree_generate         | 53.2 ms                                                         | 49.7 ms: 1.07x faster                                                        |
| deepcopy_reduce            | 1.99 us                                                         | 1.86 us: 1.07x faster                                                        |
| pyflate                    | 279 ms                                                          | 261 ms: 1.07x faster                                                         |
| json                       | 3.19 ms                                                         | 2.99 ms: 1.07x faster                                                        |
| scimark_lu                 | 56.6 ms                                                         | 54.3 ms: 1.04x faster                                                        |
| xml_etree_process          | 36.4 ms                                                         | 35.0 ms: 1.04x faster                                                        |
| pickle_list                | 2.90 us                                                         | 2.82 us: 1.03x faster                                                        |
| pickle_dict                | 18.1 us                                                         | 17.7 us: 1.03x faster                                                        |
| async_tree_memoization     | 264 ms                                                          | 257 ms: 1.03x faster                                                         |
| deltablue                  | 1.88 ms                                                         | 1.84 ms: 1.02x faster                                                        |
| telco                      | 4.67 ms                                                         | 4.57 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 62.3 ms                                                         | 61.5 ms: 1.01x faster                                                        |
| gc_traversal               | 1.55 ms                                                         | 1.54 ms: 1.01x faster                                                        |
| pidigits                   | 150 ms                                                          | 149 ms: 1.01x faster                                                         |
| sqlite_synth               | 1.60 us                                                         | 1.61 us: 1.00x slower                                                        |
| fannkuch                   | 243 ms                                                          | 247 ms: 1.01x slower                                                         |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.01x slower                                                        |
| regex_effbot               | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                        |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                                         |
| pickle                     | 7.11 us                                                         | 7.25 us: 1.02x slower                                                        |
| logging_format             | 6.22 us                                                         | 6.39 us: 1.03x slower                                                        |
| comprehensions             | 10.4 us                                                         | 10.7 us: 1.03x slower                                                        |
| logging_simple             | 5.78 us                                                         | 5.96 us: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                         |
| xml_etree_parse            | 90.9 ms                                                         | 94.1 ms: 1.03x slower                                                        |
| pathlib                    | 75.9 ms                                                         | 79.6 ms: 1.05x slower                                                        |
| json_dumps                 | 5.61 ms                                                         | 5.91 ms: 1.05x slower                                                        |
| bench_thread_pool          | 768 us                                                          | 812 us: 1.06x slower                                                         |
| chaos                      | 38.4 ms                                                         | 40.6 ms: 1.06x slower                                                        |
| nqueens                    | 56.7 ms                                                         | 60.8 ms: 1.07x slower                                                        |
| meteor_contest             | 69.9 ms                                                         | 75.1 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 101 us                                                          | 108 us: 1.07x slower                                                         |
| unpickle                   | 8.40 us                                                         | 9.03 us: 1.07x slower                                                        |
| unpickle_list              | 2.62 us                                                         | 2.86 us: 1.09x slower                                                        |
| logging_silent             | 52.9 ns                                                         | 57.9 ns: 1.09x slower                                                        |
| scimark_monte_carlo        | 39.1 ms                                                         | 43.0 ms: 1.10x slower                                                        |
| coroutines                 | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                        |
| pprint_safe_repr           | 474 ms                                                          | 523 ms: 1.10x slower                                                         |
| pprint_pformat             | 966 ms                                                          | 1.07 sec: 1.11x slower                                                       |
| bench_mp_pool              | 64.8 ms                                                         | 72.1 ms: 1.11x slower                                                        |
| python_startup             | 20.3 ms                                                         | 22.6 ms: 1.12x slower                                                        |
| mdp                        | 1.31 sec                                                        | 1.47 sec: 1.12x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 197 us: 1.13x slower                                                         |
| go                         | 82.1 ms                                                         | 92.7 ms: 1.13x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                         | 18.4 ms: 1.13x slower                                                        |
| coverage                   | 42.1 ms                                                         | 47.7 ms: 1.13x slower                                                        |
| dulwich_log                | 38.0 ms                                                         | 43.4 ms: 1.14x slower                                                        |
| async_generators           | 223 ms                                                          | 257 ms: 1.15x slower                                                         |
| generators                 | 19.6 ms                                                         | 22.5 ms: 1.15x slower                                                        |
| sqlglot_normalize          | 173 ms                                                          | 201 ms: 1.16x slower                                                         |
| sympy_sum                  | 84.4 ms                                                         | 98.3 ms: 1.16x slower                                                        |
| unpickle_pure_python       | 122 us                                                          | 142 us: 1.17x slower                                                         |
| docutils                   | 1.63 sec                                                        | 1.91 sec: 1.18x slower                                                       |
| 2to3                       | 207 ms                                                          | 243 ms: 1.18x slower                                                         |
| sympy_str                  | 159 ms                                                          | 188 ms: 1.18x slower                                                         |
| tornado_http               | 81.8 ms                                                         | 97.2 ms: 1.19x slower                                                        |
| html5lib                   | 35.0 ms                                                         | 41.8 ms: 1.19x slower                                                        |
| sqlglot_parse              | 748 us                                                          | 898 us: 1.20x slower                                                         |
| sqlglot_transpile          | 955 us                                                          | 1.16 ms: 1.21x slower                                                        |
| sympy_integrate            | 12.2 ms                                                         | 14.8 ms: 1.21x slower                                                        |
| sympy_expand               | 271 ms                                                          | 329 ms: 1.22x slower                                                         |
| regex_compile              | 78.0 ms                                                         | 95.1 ms: 1.22x slower                                                        |
| django_template            | 21.7 ms                                                         | 26.6 ms: 1.23x slower                                                        |
| sqlglot_optimize           | 32.7 ms                                                         | 40.4 ms: 1.24x slower                                                        |
| raytrace                   | 162 ms                                                          | 209 ms: 1.29x slower                                                         |
| pylint                     | 205 ms                                                          | 265 ms: 1.29x slower                                                         |
| asyncio_tcp                | 471 ms                                                          | 611 ms: 1.30x slower                                                         |
| hexiom                     | 3.72 ms                                                         | 4.90 ms: 1.32x slower                                                        |
| richards_super             | 30.2 ms                                                         | 39.8 ms: 1.32x slower                                                        |
| genshi_text                | 14.4 ms                                                         | 19.3 ms: 1.34x slower                                                        |
| richards                   | 26.7 ms                                                         | 37.3 ms: 1.40x slower                                                        |
| genshi_xml                 | 31.6 ms                                                         | 46.0 ms: 1.46x slower                                                        |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                 |

Benchmark hidden because not significant (8): pycparser, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, create_gc_cycles, regex_v8, asyncio_tcp_ssl
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: unpack_sequence

# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown