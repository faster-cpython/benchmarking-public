# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.034x slower
- HPT reliability: 99.34%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 3.10 sec: 1.87x slower                                                     |
| Geometric mean | (ref)                                                       | 1.41x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 339 ms: 2.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 361 ms: 2.03x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 153 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.78x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.1 ms: 1.20x faster                                                      |
| pidigits       | 152 ms                                                      | 138 ms: 1.10x faster                                                       |
| nbody          | 71.9 ms                                                     | 86.0 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.02x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 95.6 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 20.4 us: 1.11x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.14 us: 1.11x slower                                                      |
| pickle               | 7.43 us                                                     | 8.37 us: 1.13x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.8 ms: 1.14x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.18 us: 1.16x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.6 us: 1.19x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 234 us: 1.20x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 161 us: 1.21x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 7.12 ms: 1.25x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.4 us: 1.27x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.78 sec: 2.04x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 29.0 ms: 1.26x slower                                                      |
| mako            | 7.09 ms                                                     | 9.55 ms: 1.35x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.31x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.8 ms: 2.38x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 339 ms: 2.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 361 ms: 2.03x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 153 ms: 1.87x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.86x faster                                                       |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 315 ms: 1.59x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 217 ms: 1.56x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 333 ms: 1.47x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.35 us: 1.30x faster                                                      |
| float                      | 56.8 ms                                                     | 47.1 ms: 1.20x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.3 us: 1.15x faster                                                      |
| mdp                        | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                      |
| deepcopy                   | 238 us                                                      | 211 us: 1.13x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.36 ms: 1.12x faster                                                      |
| pidigits                   | 152 ms                                                      | 138 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.9 ms: 1.09x faster                                                      |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 462 ms: 1.05x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.6 ms: 1.05x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.7 ms: 1.01x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.64 ms: 1.02x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| go                         | 91.6 ms                                                     | 94.9 ms: 1.04x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.8 ns: 1.04x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.20 us: 1.05x slower                                                      |
| json                       | 3.05 ms                                                     | 3.20 ms: 1.05x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.4 ns: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| pycparser                  | 699 ms                                                      | 754 ms: 1.08x slower                                                       |
| chaos                      | 43.3 ms                                                     | 47.0 ms: 1.08x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 95.6 ms: 1.09x slower                                                      |
| sympy_str                  | 175 ms                                                      | 191 ms: 1.09x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 100 ms: 1.09x slower                                                       |
| async_generators           | 239 ms                                                      | 262 ms: 1.10x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.89 us: 1.10x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 15.7 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 326 ms: 1.11x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.4 us: 1.11x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.14 us: 1.11x slower                                                      |
| raytrace                   | 192 ms                                                      | 214 ms: 1.11x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.33 sec: 1.11x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 573 ms: 1.12x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.51 us: 1.12x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.37 us: 1.13x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 88.8 ms: 1.13x slower                                                      |
| spectral_norm              | 66.9 ms                                                     | 75.5 ms: 1.13x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 66.6 ms: 1.13x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.8 ms: 1.14x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.18 us: 1.16x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.77 ms: 1.16x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 80.4 ms: 1.16x slower                                                      |
| sympy_expand               | 284 ms                                                      | 331 ms: 1.17x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.54 ms: 1.18x slower                                                      |
| scimark_fft                | 184 ms                                                      | 217 ms: 1.18x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 87.9 ms: 1.18x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.9 ms: 1.19x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.8 ms: 1.19x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.6 us: 1.19x slower                                                      |
| nbody                      | 71.9 ms                                                     | 86.0 ms: 1.20x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 234 us: 1.20x slower                                                       |
| richards                   | 28.4 ms                                                     | 34.2 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 161 us: 1.21x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 59.1 ms: 1.22x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.12 ms: 1.22x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 77.3 ms: 1.23x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 7.12 ms: 1.25x slower                                                      |
| richards_super             | 32.1 ms                                                     | 40.2 ms: 1.25x slower                                                      |
| fannkuch                   | 247 ms                                                      | 309 ms: 1.25x slower                                                       |
| django_template            | 22.9 ms                                                     | 29.0 ms: 1.26x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.4 us: 1.27x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.29 ms: 1.28x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.15 ms: 1.34x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.55 ms: 1.35x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.37x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.06 ms: 1.41x slower                                                      |
| coverage                   | 40.8 ms                                                     | 68.0 ms: 1.67x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.83 sec: 1.75x slower                                                     |
| docutils                   | 1.66 sec                                                    | 3.10 sec: 1.87x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.78 sec: 2.04x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x slower

# HPT report

- Reliability score: 99.34% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown