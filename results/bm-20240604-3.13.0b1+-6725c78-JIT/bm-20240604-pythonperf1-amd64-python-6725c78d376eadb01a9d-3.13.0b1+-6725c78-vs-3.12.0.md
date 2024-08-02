# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.05x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.94 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 216 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 230 ms: 1.27x faster                                                        |
| async_tree_io              | 731 ms                                                      | 589 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 625 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                       |
| float          | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.14x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.05x faster                                                        |
| xml_etree_process    | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.81 us: 1.01x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.74 ms: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.85 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.54 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.02 ms: 1.41x faster                                                       |
| django_template | 22.9 ms                                                     | 25.8 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.8 ms: 1.49x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.02 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.49 sec: 1.41x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.1 ms: 1.41x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 216 ms: 1.32x faster                                                        |
| float                      | 56.8 ms                                                     | 43.7 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 230 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.04 ms: 1.25x faster                                                       |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.25x faster                                                        |
| async_tree_io              | 731 ms                                                      | 589 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 625 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 40.8 ms: 1.19x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.3 us: 1.17x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.9 ms: 1.15x faster                                                       |
| fannkuch                   | 247 ms                                                      | 215 ms: 1.15x faster                                                        |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.14x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 452 ms: 1.13x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 930 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.22 sec: 1.12x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.3 ns: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.1 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.82 us: 1.08x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.5 ms: 1.08x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.29 us: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.05x faster                                                        |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 820 us: 1.04x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 86.1 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.3 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.1 ms: 1.03x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.7 ms: 1.03x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.9 us: 1.03x faster                                                       |
| regex_dna                  | 126 ms                                                      | 124 ms: 1.02x faster                                                        |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.94 ms: 1.01x faster                                                       |
| pickle_list                | 2.83 us                                                     | 2.81 us: 1.01x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 69.6 ms: 1.01x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.74 ms: 1.01x slower                                                       |
| deepcopy                   | 238 us                                                      | 241 us: 1.01x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.2 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.14 us: 1.02x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 80.7 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 94.0 ms: 1.03x slower                                                       |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                        |
| richards_super             | 32.1 ms                                                     | 33.1 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 723 ms: 1.03x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.85 us: 1.04x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.4 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.54 us: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 252 ms: 1.05x slower                                                        |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| aiohttp                    | 884 us                                                      | 930 us: 1.05x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 37.0 ms: 1.07x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.52 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                                       |
| coverage                   | 40.8 ms                                                     | 45.7 ms: 1.12x slower                                                       |
| sympy_expand               | 284 ms                                                      | 319 ms: 1.12x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.8 ms: 1.12x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.68 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 70.2 ms: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 923 us: 1.23x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (6): mypy2, asyncio_tcp, pickle, regex_effbot, regex_compile, sqlglot_parse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown