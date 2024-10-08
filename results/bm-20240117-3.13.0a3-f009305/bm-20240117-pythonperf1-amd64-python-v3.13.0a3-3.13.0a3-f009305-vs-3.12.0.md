# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: windows-amd64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 210 ms: 1.04x faster                                            |
| chameleon      | 4.98 ms                                                     | 4.91 ms: 1.01x faster                                           |
| docutils       | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                          |
| tornado_http   | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.04x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 263 ms: 1.11x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 448 ms: 1.09x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 465 ms: 1.08x faster                                            |
| async_tree_none_tg         | 285 ms                                                      | 270 ms: 1.06x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| async_tree_io_tg           | 771 ms                                                      | 750 ms: 1.03x faster                                            |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.5 ms: 1.08x faster                                           |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| nbody          | 71.9 ms                                                     | 74.1 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.7 ms: 1.13x faster                                           |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                            |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 53.6 ms: 1.04x faster                                           |
| unpickle_pure_python | 133 us                                                      | 128 us: 1.04x faster                                            |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                           |
| json_dumps           | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                           |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                           |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.02x faster                                           |
| pickle               | 7.43 us                                                     | 7.31 us: 1.02x faster                                           |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                           |
| unpickle_list        | 2.75 us                                                     | 2.73 us: 1.01x faster                                           |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                          |
| pickle_list          | 2.83 us                                                     | 2.89 us: 1.02x slower                                           |
| unpickle             | 8.18 us                                                     | 8.42 us: 1.03x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                           |
| python_startup_no_site | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                           |
| django_template | 22.9 ms                                                     | 21.4 ms: 1.07x faster                                           |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 70.5 us: 1.35x faster                                           |
| mypy2                      | 509 ms                                                      | 409 ms: 1.25x faster                                            |
| raytrace                   | 192 ms                                                      | 161 ms: 1.20x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.83 sec: 1.14x faster                                          |
| crypto_pyaes               | 48.5 ms                                                     | 42.8 ms: 1.13x faster                                           |
| regex_compile              | 87.5 ms                                                     | 77.7 ms: 1.13x faster                                           |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                           |
| sympy_str                  | 175 ms                                                      | 156 ms: 1.12x faster                                            |
| logging_silent             | 60.5 ns                                                     | 54.1 ns: 1.12x faster                                           |
| async_tree_none            | 291 ms                                                      | 263 ms: 1.11x faster                                            |
| sympy_sum                  | 91.5 ms                                                     | 82.6 ms: 1.11x faster                                           |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.10x faster                                           |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                           |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                           |
| deltablue                  | 2.16 ms                                                     | 1.97 ms: 1.10x faster                                           |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                            |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 448 ms: 1.09x faster                                            |
| spectral_norm              | 66.9 ms                                                     | 61.6 ms: 1.09x faster                                           |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.09x faster                                           |
| docutils                   | 1.66 sec                                                    | 1.53 sec: 1.08x faster                                          |
| float                      | 56.8 ms                                                     | 52.5 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 465 ms: 1.08x faster                                            |
| mako                       | 7.09 ms                                                     | 6.57 ms: 1.08x faster                                           |
| go                         | 91.6 ms                                                     | 84.9 ms: 1.08x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                           |
| hexiom                     | 4.10 ms                                                     | 3.82 ms: 1.07x faster                                           |
| scimark_lu                 | 58.9 ms                                                     | 54.9 ms: 1.07x faster                                           |
| django_template            | 22.9 ms                                                     | 21.4 ms: 1.07x faster                                           |
| deepcopy_memo              | 23.7 us                                                     | 22.2 us: 1.07x faster                                           |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                            |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                            |
| sympy_expand               | 284 ms                                                      | 268 ms: 1.06x faster                                            |
| nqueens                    | 62.8 ms                                                     | 59.3 ms: 1.06x faster                                           |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                           |
| sqlglot_parse              | 804 us                                                      | 761 us: 1.06x faster                                            |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                           |
| async_tree_none_tg         | 285 ms                                                      | 270 ms: 1.06x faster                                            |
| asyncio_tcp                | 487 ms                                                      | 462 ms: 1.05x faster                                            |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                            |
| async_tree_memoization_tg  | 367 ms                                                      | 349 ms: 1.05x faster                                            |
| tornado_http               | 89.5 ms                                                     | 85.5 ms: 1.05x faster                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 33.0 ms: 1.05x faster                                           |
| pprint_safe_repr           | 513 ms                                                      | 491 ms: 1.05x faster                                            |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 981 us: 1.04x faster                                            |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                           |
| xml_etree_generate         | 55.8 ms                                                     | 53.6 ms: 1.04x faster                                           |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.04x faster                                          |
| logging_simple             | 6.28 us                                                     | 6.04 us: 1.04x faster                                           |
| bench_mp_pool              | 69.2 ms                                                     | 66.6 ms: 1.04x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 128 us: 1.04x faster                                            |
| logging_format             | 6.72 us                                                     | 6.47 us: 1.04x faster                                           |
| meteor_contest             | 74.6 ms                                                     | 71.9 ms: 1.04x faster                                           |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                           |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.04x faster                                           |
| 2to3                       | 218 ms                                                      | 210 ms: 1.04x faster                                            |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.04x faster                                            |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                            |
| json_dumps                 | 5.70 ms                                                     | 5.54 ms: 1.03x faster                                           |
| async_tree_io_tg           | 771 ms                                                      | 750 ms: 1.03x faster                                            |
| create_gc_cycles           | 752 us                                                      | 732 us: 1.03x faster                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.5 ms: 1.03x faster                                           |
| pyflate                    | 295 ms                                                      | 288 ms: 1.02x faster                                            |
| bench_thread_pool          | 857 us                                                      | 839 us: 1.02x faster                                            |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.02x faster                                           |
| pickle                     | 7.43 us                                                     | 7.31 us: 1.02x faster                                           |
| generators                 | 22.5 ms                                                     | 22.1 ms: 1.02x faster                                           |
| pathlib                    | 80.5 ms                                                     | 79.3 ms: 1.01x faster                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.52 ms: 1.01x faster                                           |
| chameleon                  | 4.98 ms                                                     | 4.91 ms: 1.01x faster                                           |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                           |
| scimark_sor                | 78.8 ms                                                     | 78.0 ms: 1.01x faster                                           |
| unpickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                           |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                            |
| aiohttp                    | 884 us                                                      | 896 us: 1.01x slower                                            |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                          |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                          |
| pickle_list                | 2.83 us                                                     | 2.89 us: 1.02x slower                                           |
| unpickle                   | 8.18 us                                                     | 8.42 us: 1.03x slower                                           |
| nbody                      | 71.9 ms                                                     | 74.1 ms: 1.03x slower                                           |
| python_startup             | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                           |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.07x slower                                           |
| coverage                   | 40.8 ms                                                     | 44.3 ms: 1.09x slower                                           |
| python_startup_no_site     | 16.2 ms                                                     | 17.9 ms: 1.10x slower                                           |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.16x slower                                           |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                    |

Benchmark hidden because not significant (5): async_tree_io, gc_traversal, xml_etree_parse, pycparser, async_tree_memoization
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1-amd64-python-v3.13.0a3-3.13.0a3-f009305.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown