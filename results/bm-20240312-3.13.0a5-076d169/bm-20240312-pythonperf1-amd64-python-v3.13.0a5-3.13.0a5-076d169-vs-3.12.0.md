# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: windows-amd64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 216 ms: 1.01x faster                                            |
| chameleon      | 4.98 ms                                                     | 4.84 ms: 1.03x faster                                           |
| docutils       | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                          |
| tornado_http   | 89.5 ms                                                     | 84.8 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 270 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 474 ms: 1.06x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 274 ms: 1.04x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 758 ms: 1.02x faster                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                    |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.8 ms: 1.12x faster                                           |
| nbody          | 71.9 ms                                                     | 68.2 ms: 1.05x faster                                           |
| pidigits       | 152 ms                                                      | 147 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                       | 1.07x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                           |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                           |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 180 us: 1.09x faster                                            |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                           |
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                           |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.68 us: 1.03x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.63 ms: 1.01x faster                                           |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.01x slower                                           |
| unpickle             | 8.18 us                                                     | 8.29 us: 1.01x slower                                           |
| pickle_list          | 2.83 us                                                     | 2.90 us: 1.03x slower                                           |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                          |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                           |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.21 ms: 1.14x faster                                           |
| django_template | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                           |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 75.1 us: 1.27x faster                                           |
| mypy2                      | 509 ms                                                      | 413 ms: 1.23x faster                                            |
| raytrace                   | 192 ms                                                      | 160 ms: 1.20x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.80 sec: 1.16x faster                                          |
| mako                       | 7.09 ms                                                     | 6.21 ms: 1.14x faster                                           |
| crypto_pyaes               | 48.5 ms                                                     | 42.6 ms: 1.14x faster                                           |
| logging_silent             | 60.5 ns                                                     | 53.5 ns: 1.13x faster                                           |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 59.7 ms: 1.12x faster                                           |
| regex_compile              | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                           |
| float                      | 56.8 ms                                                     | 50.8 ms: 1.12x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.2 ms: 1.12x faster                                           |
| sympy_str                  | 175 ms                                                      | 158 ms: 1.11x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                           |
| sympy_sum                  | 91.5 ms                                                     | 82.9 ms: 1.10x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                           |
| generators                 | 22.5 ms                                                     | 20.6 ms: 1.10x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.98 ms: 1.09x faster                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.35 ms: 1.09x faster                                           |
| pickle_pure_python         | 195 us                                                      | 180 us: 1.09x faster                                            |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                           |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.08x faster                                            |
| deepcopy                   | 238 us                                                      | 220 us: 1.08x faster                                            |
| async_tree_none            | 291 ms                                                      | 270 ms: 1.08x faster                                            |
| docutils                   | 1.66 sec                                                    | 1.54 sec: 1.08x faster                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 454 ms: 1.08x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.08x faster                                           |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                            |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                            |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                            |
| async_generators           | 239 ms                                                      | 224 ms: 1.07x faster                                            |
| go                         | 91.6 ms                                                     | 86.1 ms: 1.06x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 22.3 us: 1.06x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 55.5 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 474 ms: 1.06x faster                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 32.6 ms: 1.06x faster                                           |
| tornado_http               | 89.5 ms                                                     | 84.8 ms: 1.06x faster                                           |
| sqlglot_parse              | 804 us                                                      | 762 us: 1.06x faster                                            |
| pprint_pformat             | 1.05 sec                                                    | 992 ms: 1.05x faster                                            |
| nbody                      | 71.9 ms                                                     | 68.2 ms: 1.05x faster                                           |
| sympy_expand               | 284 ms                                                      | 270 ms: 1.05x faster                                            |
| pprint_safe_repr           | 513 ms                                                      | 487 ms: 1.05x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| logging_simple             | 6.28 us                                                     | 5.97 us: 1.05x faster                                           |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.05x faster                                           |
| nqueens                    | 62.8 ms                                                     | 59.9 ms: 1.05x faster                                           |
| hexiom                     | 4.10 ms                                                     | 3.91 ms: 1.05x faster                                           |
| logging_format             | 6.72 us                                                     | 6.41 us: 1.05x faster                                           |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                            |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                           |
| scimark_sor                | 78.8 ms                                                     | 75.4 ms: 1.04x faster                                           |
| sqlglot_transpile          | 1.02 ms                                                     | 980 us: 1.04x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 274 ms: 1.04x faster                                            |
| bench_mp_pool              | 69.2 ms                                                     | 66.6 ms: 1.04x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                           |
| django_template            | 22.9 ms                                                     | 22.1 ms: 1.04x faster                                           |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                           |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                           |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                           |
| pidigits                   | 152 ms                                                      | 147 ms: 1.03x faster                                            |
| bench_thread_pool          | 857 us                                                      | 831 us: 1.03x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.84 ms: 1.03x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                           |
| unpickle_list              | 2.75 us                                                     | 2.68 us: 1.03x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 72.8 ms: 1.02x faster                                           |
| async_tree_io_tg           | 771 ms                                                      | 758 ms: 1.02x faster                                            |
| gc_traversal               | 1.52 ms                                                     | 1.50 ms: 1.01x faster                                           |
| fannkuch                   | 247 ms                                                      | 243 ms: 1.01x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.63 ms: 1.01x faster                                           |
| 2to3                       | 218 ms                                                      | 216 ms: 1.01x faster                                            |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.01x slower                                           |
| unpickle                   | 8.18 us                                                     | 8.29 us: 1.01x slower                                           |
| aiohttp                    | 884 us                                                      | 896 us: 1.01x slower                                            |
| pickle_list                | 2.83 us                                                     | 2.90 us: 1.03x slower                                           |
| python_startup             | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                           |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                          |
| json                       | 3.05 ms                                                     | 3.23 ms: 1.06x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                           |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                           |
| coverage                   | 40.8 ms                                                     | 47.1 ms: 1.15x slower                                           |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (9): asyncio_tcp, create_gc_cycles, pycparser, pathlib, json_loads, mdp, async_tree_memoization, xml_etree_parse, async_tree_io
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1-amd64-python-v3.13.0a5-3.13.0a5-076d169.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown