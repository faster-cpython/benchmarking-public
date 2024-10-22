# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-amd64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.02x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 94.1 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.41x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 581 ms: 1.33x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 594 ms: 1.23x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.1 ms: 1.05x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| nbody          | 71.9 ms                                                     | 82.9 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                                |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_list        | 2.75 us                                                     | 2.77 us: 1.01x slower                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.0 ms: 1.03x slower                                                                |
| xml_etree_parse      | 93.0 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                                |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                                |
| pickle_list          | 2.83 us                                                     | 2.97 us: 1.05x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                                 |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| unpickle             | 8.18 us                                                     | 9.47 us: 1.16x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.65 sec: 1.21x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                                |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                                |
| django_template | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 259 ms: 1.41x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 209 ms: 1.37x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 581 ms: 1.33x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 270 ms: 1.26x faster                                                                 |
| deepcopy                   | 238 us                                                      | 193 us: 1.24x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 396 ms: 1.23x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 594 ms: 1.23x faster                                                                 |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.72 sec: 1.22x faster                                                               |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                                |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                                 |
| go                         | 91.6 ms                                                     | 86.4 ms: 1.06x faster                                                                |
| float                      | 56.8 ms                                                     | 54.1 ms: 1.05x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.68 us: 1.05x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                                 |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                                                |
| generators                 | 22.5 ms                                                     | 21.8 ms: 1.03x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 89.8 ms: 1.02x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 43.9 ms: 1.01x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 68.7 ms: 1.01x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 60.8 ns: 1.00x slower                                                                |
| unpickle_list              | 2.75 us                                                     | 2.77 us: 1.01x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                                |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 59.6 ms: 1.01x slower                                                                |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                                 |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                                |
| chaos                      | 43.3 ms                                                     | 44.2 ms: 1.02x slower                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.0 ms: 1.03x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 64.6 ms: 1.03x slower                                                                |
| spectral_norm              | 66.9 ms                                                     | 69.0 ms: 1.03x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.03x slower                                                               |
| xml_etree_parse            | 93.0 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 90.8 ms: 1.04x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 77.6 ms: 1.04x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.67 ms: 1.04x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.05x slower                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                                |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                                |
| pickle_list                | 2.83 us                                                     | 2.97 us: 1.05x slower                                                                |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| tornado_http               | 89.5 ms                                                     | 94.1 ms: 1.05x slower                                                                |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                                 |
| sqlglot_normalize          | 187 ms                                                      | 198 ms: 1.06x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                                |
| pycparser                  | 699 ms                                                      | 741 ms: 1.06x slower                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 547 ms: 1.07x slower                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.6 ms: 1.07x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                               |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.08x slower                                                                |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                                |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                                |
| scimark_fft                | 184 ms                                                      | 204 ms: 1.11x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                                |
| sqlglot_parse              | 804 us                                                      | 894 us: 1.11x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                                 |
| richards_super             | 32.1 ms                                                     | 35.7 ms: 1.11x slower                                                                |
| richards                   | 28.4 ms                                                     | 31.7 ms: 1.12x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                                |
| scimark_sor                | 78.8 ms                                                     | 90.1 ms: 1.14x slower                                                                |
| django_template            | 22.9 ms                                                     | 26.3 ms: 1.15x slower                                                                |
| nbody                      | 71.9 ms                                                     | 82.9 ms: 1.15x slower                                                                |
| unpickle                   | 8.18 us                                                     | 9.47 us: 1.16x slower                                                                |
| fannkuch                   | 247 ms                                                      | 286 ms: 1.16x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                                |
| coverage                   | 40.8 ms                                                     | 48.6 ms: 1.19x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.65 sec: 1.21x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 939 us: 1.25x slower                                                                 |
| asyncio_tcp                | 487 ms                                                      | 641 ms: 1.32x slower                                                                 |
| json                       | 3.05 ms                                                     | 4.46 ms: 1.46x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (5): unpack_sequence, pickle, pathlib, logging_simple, coroutines
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown