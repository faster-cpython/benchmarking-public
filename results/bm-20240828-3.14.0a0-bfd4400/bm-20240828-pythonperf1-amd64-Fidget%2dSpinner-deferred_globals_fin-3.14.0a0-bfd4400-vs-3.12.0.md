# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.01x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 249 ms: 1.47x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.45x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 546 ms: 1.41x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.33x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.29x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| nbody          | 71.9 ms                                                     | 83.5 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                                |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.0 us: 1.01x slower                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                                |
| xml_etree_parse      | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                                 |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.10x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                                |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.97 ms: 1.02x faster                                                                |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 249 ms: 1.47x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.45x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 546 ms: 1.41x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 218 ms: 1.33x faster                                                                 |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.59 sec: 1.32x faster                                                               |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.29x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 392 ms: 1.28x faster                                                                 |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 20.0 us: 1.18x faster                                                                |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.18x faster                                                                |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                                |
| generators                 | 22.5 ms                                                     | 20.8 ms: 1.08x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 824 us: 1.04x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 43.2 ms: 1.03x faster                                                                |
| pathlib                    | 80.5 ms                                                     | 78.9 ms: 1.02x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.97 ms: 1.02x faster                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 68.2 ms: 1.01x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                                |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 63.1 ms: 1.01x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                                |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.01x slower                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.8 ms: 1.01x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.34 us: 1.01x slower                                                                |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                                |
| spectral_norm              | 66.9 ms                                                     | 68.3 ms: 1.02x slower                                                                |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                                 |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 95.9 ms: 1.03x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                                |
| tornado_http               | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 62.7 ns: 1.04x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 57.9 ms: 1.04x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                                |
| async_generators           | 239 ms                                                      | 250 ms: 1.04x slower                                                                 |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                               |
| scimark_lu                 | 58.9 ms                                                     | 61.6 ms: 1.05x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.27 ms: 1.05x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 78.5 ms: 1.05x slower                                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.33 ms: 1.06x slower                                                                |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                                 |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                                                 |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                               |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.16 ms: 1.08x slower                                                                |
| go                         | 91.6 ms                                                     | 99.2 ms: 1.08x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.09x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                               |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.10x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.10x slower                                                                |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 890 us: 1.11x slower                                                                 |
| asyncio_tcp                | 487 ms                                                      | 540 ms: 1.11x slower                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.0 ms: 1.12x slower                                                                |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.12x slower                                                                |
| richards_super             | 32.1 ms                                                     | 36.5 ms: 1.14x slower                                                                |
| scimark_sor                | 78.8 ms                                                     | 90.2 ms: 1.14x slower                                                                |
| richards                   | 28.4 ms                                                     | 32.5 ms: 1.15x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| nbody                      | 71.9 ms                                                     | 83.5 ms: 1.16x slower                                                                |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                                |
| fannkuch                   | 247 ms                                                      | 290 ms: 1.18x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 910 us: 1.21x slower                                                                 |
| telco                      | 4.13 ms                                                     | 5.02 ms: 1.22x slower                                                                |
| pycparser                  | 699 ms                                                      | 883 ms: 1.26x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (5): sympy_sum, coroutines, float, chaos, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown