# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.01x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 243 ms: 1.12x slower                                                         |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                       |
| html5lib       | 38.6 ms                                                     | 41.8 ms: 1.08x slower                                                        |
| tornado_http   | 92.8 ms                                                     | 97.2 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                         |
| async_tree_none            | 223 ms                                                      | 203 ms: 1.10x faster                                                         |
| asyncio_tcp                | 654 ms                                                      | 611 ms: 1.07x faster                                                         |
| async_tree_memoization     | 271 ms                                                      | 257 ms: 1.05x faster                                                         |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                                         |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                         |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                        |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 64.5 ms                                                     | 49.8 ms: 1.29x faster                                                        |
| float          | 48.1 ms                                                     | 44.4 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 114 ms                                                      | 121 ms: 1.06x slower                                                         |
| regex_v8       | 14.7 ms                                                     | 16.0 ms: 1.09x slower                                                        |
| regex_compile  | 80.1 ms                                                     | 95.1 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                       |
| xml_etree_generate   | 53.3 ms                                                     | 49.7 ms: 1.07x faster                                                        |
| xml_etree_process    | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                        |
| pickle_dict          | 18.0 us                                                     | 17.7 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                        |
| pickle               | 7.34 us                                                     | 7.25 us: 1.01x faster                                                        |
| xml_etree_parse      | 93.2 ms                                                     | 94.1 ms: 1.01x slower                                                        |
| json_dumps           | 5.76 ms                                                     | 5.91 ms: 1.03x slower                                                        |
| unpickle             | 8.63 us                                                     | 9.03 us: 1.05x slower                                                        |
| unpickle_list        | 2.72 us                                                     | 2.86 us: 1.05x slower                                                        |
| pickle_pure_python   | 183 us                                                      | 197 us: 1.08x slower                                                         |
| unpickle_pure_python | 127 us                                                      | 142 us: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 22.6 ms: 1.02x slower                                                        |
| python_startup_no_site | 17.8 ms                                                     | 18.4 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 5.00 ms: 1.25x faster                                                        |
| django_template | 21.8 ms                                                     | 26.6 ms: 1.22x slower                                                        |
| genshi_text     | 14.9 ms                                                     | 19.3 ms: 1.30x slower                                                        |
| genshi_xml      | 32.8 ms                                                     | 46.0 ms: 1.40x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 510 us: 17.01x faster                                                        |
| deepcopy_memo              | 21.8 us                                                     | 15.7 us: 1.39x faster                                                        |
| spectral_norm              | 59.2 ms                                                     | 44.0 ms: 1.34x faster                                                        |
| nbody                      | 64.5 ms                                                     | 49.8 ms: 1.29x faster                                                        |
| mako                       | 6.24 ms                                                     | 5.00 ms: 1.25x faster                                                        |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                         |
| scimark_sor                | 72.0 ms                                                     | 60.5 ms: 1.19x faster                                                        |
| scimark_fft                | 174 ms                                                      | 149 ms: 1.17x faster                                                         |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                         |
| crypto_pyaes               | 42.8 ms                                                     | 38.8 ms: 1.10x faster                                                        |
| async_tree_none            | 223 ms                                                      | 203 ms: 1.10x faster                                                         |
| tomli_loads                | 1.36 sec                                                    | 1.25 sec: 1.09x faster                                                       |
| float                      | 48.1 ms                                                     | 44.4 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.86 us: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.17 ms: 1.08x faster                                                        |
| xml_etree_generate         | 53.3 ms                                                     | 49.7 ms: 1.07x faster                                                        |
| asyncio_tcp                | 654 ms                                                      | 611 ms: 1.07x faster                                                         |
| telco                      | 4.85 ms                                                     | 4.57 ms: 1.06x faster                                                        |
| pycparser                  | 758 ms                                                      | 716 ms: 1.06x faster                                                         |
| async_tree_memoization     | 271 ms                                                      | 257 ms: 1.05x faster                                                         |
| pyflate                    | 275 ms                                                      | 261 ms: 1.05x faster                                                         |
| xml_etree_process          | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                        |
| async_tree_none_tg         | 206 ms                                                      | 199 ms: 1.03x faster                                                         |
| pickle_dict                | 18.0 us                                                     | 17.7 us: 1.02x faster                                                        |
| pathlib                    | 81.2 ms                                                     | 79.6 ms: 1.02x faster                                                        |
| bench_thread_pool          | 828 us                                                      | 812 us: 1.02x faster                                                         |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.5 ms: 1.01x faster                                                        |
| deltablue                  | 1.86 ms                                                     | 1.84 ms: 1.01x faster                                                        |
| pickle                     | 7.34 us                                                     | 7.25 us: 1.01x faster                                                        |
| gc_traversal               | 1.55 ms                                                     | 1.54 ms: 1.01x faster                                                        |
| sqlite_synth               | 1.60 us                                                     | 1.61 us: 1.01x slower                                                        |
| scimark_lu                 | 54.0 ms                                                     | 54.3 ms: 1.01x slower                                                        |
| xml_etree_parse            | 93.2 ms                                                     | 94.1 ms: 1.01x slower                                                        |
| python_startup             | 22.2 ms                                                     | 22.6 ms: 1.02x slower                                                        |
| coverage                   | 46.7 ms                                                     | 47.7 ms: 1.02x slower                                                        |
| json_dumps                 | 5.76 ms                                                     | 5.91 ms: 1.03x slower                                                        |
| python_startup_no_site     | 17.8 ms                                                     | 18.4 ms: 1.03x slower                                                        |
| bench_mp_pool              | 69.6 ms                                                     | 72.1 ms: 1.04x slower                                                        |
| meteor_contest             | 72.3 ms                                                     | 75.1 ms: 1.04x slower                                                        |
| logging_format             | 6.15 us                                                     | 6.39 us: 1.04x slower                                                        |
| logging_simple             | 5.72 us                                                     | 5.96 us: 1.04x slower                                                        |
| comprehensions             | 10.2 us                                                     | 10.7 us: 1.04x slower                                                        |
| unpickle                   | 8.63 us                                                     | 9.03 us: 1.05x slower                                                        |
| tornado_http               | 92.8 ms                                                     | 97.2 ms: 1.05x slower                                                        |
| unpickle_list              | 2.72 us                                                     | 2.86 us: 1.05x slower                                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 395 ms: 1.05x slower                                                         |
| regex_dna                  | 114 ms                                                      | 121 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 493 ms                                                      | 523 ms: 1.06x slower                                                         |
| mdp                        | 1.38 sec                                                    | 1.47 sec: 1.06x slower                                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 43.0 ms: 1.07x slower                                                        |
| async_tree_io_tg           | 512 ms                                                      | 548 ms: 1.07x slower                                                         |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                        |
| dulwich_log                | 40.4 ms                                                     | 43.4 ms: 1.08x slower                                                        |
| pickle_pure_python         | 183 us                                                      | 197 us: 1.08x slower                                                         |
| typing_runtime_protocols   | 100 us                                                      | 108 us: 1.08x slower                                                         |
| create_gc_cycles           | 829 us                                                      | 896 us: 1.08x slower                                                         |
| html5lib                   | 38.6 ms                                                     | 41.8 ms: 1.08x slower                                                        |
| pprint_pformat             | 991 ms                                                      | 1.07 sec: 1.08x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 16.0 ms: 1.09x slower                                                        |
| nqueens                    | 55.5 ms                                                     | 60.8 ms: 1.09x slower                                                        |
| go                         | 84.6 ms                                                     | 92.7 ms: 1.10x slower                                                        |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                         |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                        |
| 2to3                       | 217 ms                                                      | 243 ms: 1.12x slower                                                         |
| unpickle_pure_python       | 127 us                                                      | 142 us: 1.12x slower                                                         |
| sympy_str                  | 166 ms                                                      | 188 ms: 1.13x slower                                                         |
| logging_silent             | 51.0 ns                                                     | 57.9 ns: 1.14x slower                                                        |
| sympy_sum                  | 86.4 ms                                                     | 98.3 ms: 1.14x slower                                                        |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                         |
| sympy_expand               | 285 ms                                                      | 329 ms: 1.15x slower                                                         |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                                        |
| sqlglot_normalize          | 171 ms                                                      | 201 ms: 1.18x slower                                                         |
| sqlglot_parse              | 761 us                                                      | 898 us: 1.18x slower                                                         |
| regex_compile              | 80.1 ms                                                     | 95.1 ms: 1.19x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 14.8 ms: 1.21x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.21x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 1.16 ms: 1.22x slower                                                        |
| django_template            | 21.8 ms                                                     | 26.6 ms: 1.22x slower                                                        |
| sqlglot_optimize           | 33.1 ms                                                     | 40.4 ms: 1.22x slower                                                        |
| pylint                     | 211 ms                                                      | 265 ms: 1.26x slower                                                         |
| genshi_text                | 14.9 ms                                                     | 19.3 ms: 1.30x slower                                                        |
| hexiom                     | 3.69 ms                                                     | 4.90 ms: 1.33x slower                                                        |
| raytrace                   | 156 ms                                                      | 209 ms: 1.34x slower                                                         |
| richards_super             | 29.3 ms                                                     | 39.8 ms: 1.36x slower                                                        |
| genshi_xml                 | 32.8 ms                                                     | 46.0 ms: 1.40x slower                                                        |
| richards                   | 26.0 ms                                                     | 37.3 ms: 1.43x slower                                                        |
| unpack_sequence            | 40.0 ns                                                     | 58.8 ns: 1.47x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                 |

Benchmark hidden because not significant (8): pickle_list, asyncio_tcp_ssl, regex_effbot, json, pidigits, json_loads, fannkuch, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown