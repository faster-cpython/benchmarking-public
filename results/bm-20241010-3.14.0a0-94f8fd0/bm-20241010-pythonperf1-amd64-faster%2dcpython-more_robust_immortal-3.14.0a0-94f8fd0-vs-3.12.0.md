# Results vs. 3.12.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.02x slower
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 94.8 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 587 ms: 1.31x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 593 ms: 1.23x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 398 ms: 1.23x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 54.8 ms: 1.04x faster                                                                |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                                                 |
| nbody          | 71.9 ms                                                     | 80.7 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 115 ms: 1.10x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                                |
| regex_v8       | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.9 ms: 1.03x slower                                                                |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                                |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                                |
| unpickle_list        | 2.75 us                                                     | 2.89 us: 1.05x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| unpickle             | 8.18 us                                                     | 9.35 us: 1.14x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                                |
| python_startup         | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                                |
| django_template | 22.9 ms                                                     | 26.7 ms: 1.17x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 212 ms: 1.38x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 207 ms: 1.38x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 587 ms: 1.31x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 393 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 273 ms: 1.24x faster                                                                 |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 593 ms: 1.23x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 398 ms: 1.23x faster                                                                 |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.73 sec: 1.21x faster                                                               |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.19x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 19.9 us: 1.19x faster                                                                |
| regex_dna                  | 126 ms                                                      | 115 ms: 1.10x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.65 us: 1.07x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                                |
| go                         | 91.6 ms                                                     | 87.4 ms: 1.05x faster                                                                |
| generators                 | 22.5 ms                                                     | 21.7 ms: 1.04x faster                                                                |
| float                      | 56.8 ms                                                     | 54.8 ms: 1.04x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.03x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.85 ms: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                                                 |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 57.4 ms: 1.02x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 838 us: 1.02x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 60.1 ns: 1.01x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 48.3 ms: 1.00x faster                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.53 ms: 1.01x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 69.6 ms: 1.01x slower                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 93.9 ms: 1.01x slower                                                                |
| chaos                      | 43.3 ms                                                     | 43.8 ms: 1.01x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 64.1 ms: 1.02x slower                                                                |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                                 |
| meteor_contest             | 74.6 ms                                                     | 76.4 ms: 1.02x slower                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.9 ms: 1.03x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.45 us: 1.03x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.91 us: 1.03x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 90.1 ms: 1.03x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                               |
| spectral_norm              | 66.9 ms                                                     | 69.3 ms: 1.04x slower                                                                |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                                |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                                |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.9 ms: 1.05x slower                                                                |
| unpickle_list              | 2.75 us                                                     | 2.89 us: 1.05x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.32 ms: 1.05x slower                                                                |
| async_generators           | 239 ms                                                      | 253 ms: 1.05x slower                                                                 |
| tornado_http               | 89.5 ms                                                     | 94.8 ms: 1.06x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                                |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.9 ms: 1.07x slower                                                                |
| unpack_sequence            | 37.5 ns                                                     | 40.2 ns: 1.07x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 552 ms: 1.07x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                               |
| pycparser                  | 699 ms                                                      | 756 ms: 1.08x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                                 |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                                 |
| sqlglot_optimize           | 34.5 ms                                                     | 37.6 ms: 1.09x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| scimark_fft                | 184 ms                                                      | 202 ms: 1.10x slower                                                                 |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.34 ms: 1.11x slower                                                                |
| sqlglot_transpile          | 1.02 ms                                                     | 1.14 ms: 1.12x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| scimark_sor                | 78.8 ms                                                     | 88.0 ms: 1.12x slower                                                                |
| nbody                      | 71.9 ms                                                     | 80.7 ms: 1.12x slower                                                                |
| fannkuch                   | 247 ms                                                      | 279 ms: 1.13x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 912 us: 1.13x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                                |
| richards_super             | 32.1 ms                                                     | 36.6 ms: 1.14x slower                                                                |
| unpickle                   | 8.18 us                                                     | 9.35 us: 1.14x slower                                                                |
| richards                   | 28.4 ms                                                     | 32.5 ms: 1.14x slower                                                                |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                               |
| django_template            | 22.9 ms                                                     | 26.7 ms: 1.17x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.93 ms: 1.19x slower                                                                |
| coverage                   | 40.8 ms                                                     | 48.9 ms: 1.20x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 934 us: 1.24x slower                                                                 |
| json                       | 3.05 ms                                                     | 4.15 ms: 1.36x slower                                                                |
| asyncio_tcp                | 487 ms                                                      | 695 ms: 1.43x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (4): dulwich_log, pathlib, raytrace, pickle
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.56% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown