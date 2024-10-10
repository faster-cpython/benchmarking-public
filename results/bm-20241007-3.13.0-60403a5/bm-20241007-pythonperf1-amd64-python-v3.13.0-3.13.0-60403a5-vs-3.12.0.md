# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| chameleon      | 4.98 ms                                                     | 4.72 ms: 1.06x faster                                       |
| docutils       | 1.66 sec                                                    | 1.57 sec: 1.05x faster                                      |
| tornado_http   | 89.5 ms                                                     | 92.8 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 512 ms: 1.50x faster                                        |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 206 ms: 1.39x faster                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                        |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 271 ms: 1.25x faster                                        |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                       |
| nbody          | 71.9 ms                                                     | 64.5 ms: 1.11x faster                                       |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                        |
| regex_compile  | 87.5 ms                                                     | 80.1 ms: 1.09x faster                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 183 us: 1.07x faster                                        |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                       |
| pickle_dict          | 18.4 us                                                     | 18.0 us: 1.02x faster                                       |
| pickle               | 7.43 us                                                     | 7.34 us: 1.01x faster                                       |
| unpickle_list        | 2.75 us                                                     | 2.72 us: 1.01x faster                                       |
| json_dumps           | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                       |
| unpickle             | 8.18 us                                                     | 8.63 us: 1.06x slower                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                       |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.24 ms: 1.14x faster                                       |
| django_template | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 512 ms: 1.50x faster                                        |
| async_tree_io              | 731 ms                                                      | 521 ms: 1.40x faster                                        |
| async_tree_none_tg         | 285 ms                                                      | 206 ms: 1.39x faster                                        |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 375 ms: 1.34x faster                                        |
| async_tree_none            | 291 ms                                                      | 223 ms: 1.31x faster                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.64 sec: 1.28x faster                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 288 ms: 1.27x faster                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                        |
| async_tree_memoization     | 339 ms                                                      | 271 ms: 1.25x faster                                        |
| raytrace                   | 192 ms                                                      | 156 ms: 1.23x faster                                        |
| mypy2                      | 509 ms                                                      | 429 ms: 1.19x faster                                        |
| logging_silent             | 60.5 ns                                                     | 51.0 ns: 1.19x faster                                       |
| float                      | 56.8 ms                                                     | 48.1 ms: 1.18x faster                                       |
| deltablue                  | 2.16 ms                                                     | 1.86 ms: 1.16x faster                                       |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                       |
| coroutines                 | 14.3 ms                                                     | 12.5 ms: 1.14x faster                                       |
| mako                       | 7.09 ms                                                     | 6.24 ms: 1.14x faster                                       |
| crypto_pyaes               | 48.5 ms                                                     | 42.8 ms: 1.13x faster                                       |
| nqueens                    | 62.8 ms                                                     | 55.5 ms: 1.13x faster                                       |
| spectral_norm              | 66.9 ms                                                     | 59.2 ms: 1.13x faster                                       |
| nbody                      | 71.9 ms                                                     | 64.5 ms: 1.11x faster                                       |
| hexiom                     | 4.10 ms                                                     | 3.69 ms: 1.11x faster                                       |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                        |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                       |
| dulwich_log                | 44.3 ms                                                     | 40.4 ms: 1.10x faster                                       |
| logging_simple             | 6.28 us                                                     | 5.72 us: 1.10x faster                                       |
| scimark_sor                | 78.8 ms                                                     | 72.0 ms: 1.09x faster                                       |
| richards_super             | 32.1 ms                                                     | 29.3 ms: 1.09x faster                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.34 ms: 1.09x faster                                       |
| sqlglot_normalize          | 187 ms                                                      | 171 ms: 1.09x faster                                        |
| regex_compile              | 87.5 ms                                                     | 80.1 ms: 1.09x faster                                       |
| logging_format             | 6.72 us                                                     | 6.15 us: 1.09x faster                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                       |
| richards                   | 28.4 ms                                                     | 26.0 ms: 1.09x faster                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.09x faster                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.8 us: 1.09x faster                                       |
| go                         | 91.6 ms                                                     | 84.6 ms: 1.08x faster                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 952 us: 1.07x faster                                        |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                        |
| pyflate                    | 295 ms                                                      | 275 ms: 1.07x faster                                        |
| pickle_pure_python         | 195 us                                                      | 183 us: 1.07x faster                                        |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                        |
| sympy_sum                  | 91.5 ms                                                     | 86.4 ms: 1.06x faster                                       |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                        |
| sqlglot_parse              | 804 us                                                      | 761 us: 1.06x faster                                        |
| chameleon                  | 4.98 ms                                                     | 4.72 ms: 1.06x faster                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                       |
| docutils                   | 1.66 sec                                                    | 1.57 sec: 1.05x faster                                      |
| pprint_pformat             | 1.05 sec                                                    | 991 ms: 1.05x faster                                        |
| django_template            | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                       |
| sympy_str                  | 175 ms                                                      | 166 ms: 1.05x faster                                        |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                        |
| xml_etree_generate         | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.3 ms: 1.05x faster                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.1 ms: 1.04x faster                                       |
| pprint_safe_repr           | 513 ms                                                      | 493 ms: 1.04x faster                                        |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.04x faster                                       |
| bench_thread_pool          | 857 us                                                      | 828 us: 1.04x faster                                        |
| meteor_contest             | 74.6 ms                                                     | 72.3 ms: 1.03x faster                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                        |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                       |
| pickle_dict                | 18.4 us                                                     | 18.0 us: 1.02x faster                                       |
| pickle                     | 7.43 us                                                     | 7.34 us: 1.01x faster                                       |
| unpickle_list              | 2.75 us                                                     | 2.72 us: 1.01x faster                                       |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                        |
| sympy_expand               | 284 ms                                                      | 285 ms: 1.00x slower                                        |
| bench_mp_pool              | 69.2 ms                                                     | 69.6 ms: 1.01x slower                                       |
| pathlib                    | 80.5 ms                                                     | 81.2 ms: 1.01x slower                                       |
| mdp                        | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                      |
| json_dumps                 | 5.70 ms                                                     | 5.76 ms: 1.01x slower                                       |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                       |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                       |
| tornado_http               | 89.5 ms                                                     | 92.8 ms: 1.04x slower                                       |
| aiohttp                    | 884 us                                                      | 932 us: 1.05x slower                                        |
| unpickle                   | 8.18 us                                                     | 8.63 us: 1.06x slower                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 100 us: 1.06x slower                                        |
| unpack_sequence            | 37.5 ns                                                     | 40.0 ns: 1.07x slower                                       |
| pycparser                  | 699 ms                                                      | 758 ms: 1.09x slower                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                       |
| create_gc_cycles           | 752 us                                                      | 829 us: 1.10x slower                                        |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                       |
| coverage                   | 40.8 ms                                                     | 46.7 ms: 1.14x slower                                       |
| telco                      | 4.13 ms                                                     | 4.85 ms: 1.17x slower                                       |
| asyncio_tcp                | 487 ms                                                      | 654 ms: 1.34x slower                                        |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                |

Benchmark hidden because not significant (5): 2to3, tomli_loads, regex_effbot, xml_etree_parse, pickle_list
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown