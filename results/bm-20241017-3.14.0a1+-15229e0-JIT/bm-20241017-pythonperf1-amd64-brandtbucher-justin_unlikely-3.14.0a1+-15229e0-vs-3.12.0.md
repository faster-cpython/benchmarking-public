# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-amd64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.00x faster
- HPT reliability: 65.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 251 ms: 1.15x slower                                                         |
| docutils       | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                       |
| tornado_http   | 89.5 ms                                                     | 101 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                       | 1.15x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 264 ms: 1.39x faster                                                         |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                         |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                         |
| async_tree_io              | 731 ms                                                      | 557 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 406 ms: 1.24x faster                                                         |
| async_tree_io_tg           | 771 ms                                                      | 637 ms: 1.21x faster                                                         |
| async_tree_memoization     | 339 ms                                                      | 283 ms: 1.20x faster                                                         |
| Geometric mean             | (ref)                                                       | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.8 ms: 1.39x faster                                                        |
| float          | 56.8 ms                                                     | 46.7 ms: 1.22x faster                                                        |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.10x faster                                                         |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                        |
| regex_compile  | 87.5 ms                                                     | 92.5 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 55.8 ms                                                     | 51.0 ms: 1.10x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                                        |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                        |
| pickle_list          | 2.83 us                                                     | 2.74 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                        |
| pickle               | 7.43 us                                                     | 7.38 us: 1.01x faster                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 202 us: 1.04x slower                                                         |
| unpickle_list        | 2.75 us                                                     | 2.86 us: 1.04x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 147 us: 1.11x slower                                                         |
| unpickle             | 8.18 us                                                     | 9.08 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                        |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.02 ms: 1.41x faster                                                        |
| django_template | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako                       | 7.09 ms                                                     | 5.02 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 264 ms: 1.39x faster                                                         |
| deepcopy_memo              | 23.7 us                                                     | 17.1 us: 1.39x faster                                                        |
| nbody                      | 71.9 ms                                                     | 51.8 ms: 1.39x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 211 ms: 1.35x faster                                                         |
| async_tree_none            | 291 ms                                                      | 220 ms: 1.33x faster                                                         |
| async_tree_io              | 731 ms                                                      | 557 ms: 1.31x faster                                                         |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                         |
| spectral_norm              | 66.9 ms                                                     | 53.2 ms: 1.26x faster                                                        |
| scimark_sor                | 78.8 ms                                                     | 62.8 ms: 1.25x faster                                                        |
| deepcopy                   | 238 us                                                      | 192 us: 1.24x faster                                                         |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 406 ms: 1.24x faster                                                         |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.22x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 39.9 ms: 1.22x faster                                                        |
| float                      | 56.8 ms                                                     | 46.7 ms: 1.22x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 637 ms: 1.21x faster                                                         |
| async_tree_memoization     | 339 ms                                                      | 283 ms: 1.20x faster                                                         |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.17x faster                                                         |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.8 ms: 1.16x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 449 ms: 1.14x faster                                                         |
| pprint_pformat             | 1.05 sec                                                    | 924 ms: 1.13x faster                                                         |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.26 ms: 1.13x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                        |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.10x faster                                                         |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 51.0 ms: 1.10x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 55.0 ms: 1.07x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 57.4 ns: 1.05x faster                                                        |
| fannkuch                   | 247 ms                                                      | 234 ms: 1.05x faster                                                         |
| chaos                      | 43.3 ms                                                     | 41.5 ms: 1.04x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 825 us: 1.04x faster                                                         |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.03x faster                                                        |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                         |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                        |
| pickle_list                | 2.83 us                                                     | 2.74 us: 1.03x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                                        |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                         |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                        |
| logging_simple             | 6.28 us                                                     | 6.18 us: 1.02x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.66 us: 1.01x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.38 us: 1.01x faster                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.2 ms: 1.01x slower                                                        |
| pathlib                    | 80.5 ms                                                     | 81.3 ms: 1.01x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                        |
| generators                 | 22.5 ms                                                     | 22.9 ms: 1.02x slower                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 95.3 ms: 1.02x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 202 us: 1.04x slower                                                         |
| unpickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                        |
| go                         | 91.6 ms                                                     | 95.4 ms: 1.04x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 92.5 ms: 1.06x slower                                                        |
| pycparser                  | 699 ms                                                      | 745 ms: 1.07x slower                                                         |
| telco                      | 4.13 ms                                                     | 4.42 ms: 1.07x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 147 us: 1.11x slower                                                         |
| unpickle                   | 8.18 us                                                     | 9.08 us: 1.11x slower                                                        |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                         |
| sqlglot_normalize          | 187 ms                                                      | 209 ms: 1.12x slower                                                         |
| sympy_str                  | 175 ms                                                      | 196 ms: 1.12x slower                                                         |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                         |
| async_generators           | 239 ms                                                      | 269 ms: 1.12x slower                                                         |
| tornado_http               | 89.5 ms                                                     | 101 ms: 1.12x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.4 ms: 1.13x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 915 us: 1.14x slower                                                         |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                                        |
| 2to3                       | 218 ms                                                      | 251 ms: 1.15x slower                                                         |
| docutils                   | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                                       |
| sympy_expand               | 284 ms                                                      | 331 ms: 1.16x slower                                                         |
| django_template            | 22.9 ms                                                     | 27.0 ms: 1.18x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.21 ms: 1.19x slower                                                        |
| richards                   | 28.4 ms                                                     | 34.5 ms: 1.21x slower                                                        |
| richards_super             | 32.1 ms                                                     | 39.1 ms: 1.22x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                         |
| sympy_integrate            | 13.0 ms                                                     | 15.9 ms: 1.23x slower                                                        |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 43.2 ms: 1.25x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 5.25 ms: 1.28x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.96 ms: 1.29x slower                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 89.3 ms: 1.29x slower                                                        |
| asyncio_tcp                | 487 ms                                                      | 666 ms: 1.37x slower                                                         |
| unpack_sequence            | 37.5 ns                                                     | 60.8 ns: 1.62x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 1.42 ms: 1.88x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                 |
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1-amd64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 65.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown