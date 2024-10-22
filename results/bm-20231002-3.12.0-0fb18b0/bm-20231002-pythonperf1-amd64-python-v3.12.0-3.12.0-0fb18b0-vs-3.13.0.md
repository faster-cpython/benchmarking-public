# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: windows-amd64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 4.98 ms: 1.06x slower                                       |
| docutils       | 1.57 sec                                                    | 1.66 sec: 1.05x slower                                      |
| tornado_http   | 92.8 ms                                                     | 89.5 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 487 ms: 1.34x faster                                        |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                        |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                       |
| async_tree_memoization     | 271 ms                                                      | 339 ms: 1.25x slower                                        |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 489 ms: 1.26x slower                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 367 ms: 1.27x slower                                        |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 2.10 sec: 1.28x slower                                      |
| async_tree_none            | 223 ms                                                      | 291 ms: 1.31x slower                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 502 ms: 1.34x slower                                        |
| async_tree_none_tg         | 206 ms                                                      | 285 ms: 1.39x slower                                        |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                        |
| async_tree_io_tg           | 512 ms                                                      | 771 ms: 1.50x slower                                        |
| Geometric mean             | (ref)                                                       | 1.23x slower                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                        |
| nbody          | 64.5 ms                                                     | 71.9 ms: 1.11x slower                                       |
| float          | 48.1 ms                                                     | 56.8 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 14.7 ms                                                     | 14.2 ms: 1.03x faster                                       |
| regex_compile  | 80.1 ms                                                     | 87.5 ms: 1.09x slower                                       |
| regex_dna      | 114 ms                                                      | 126 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle             | 8.63 us                                                     | 8.18 us: 1.06x faster                                       |
| json_loads           | 14.3 us                                                     | 13.9 us: 1.03x faster                                       |
| json_dumps           | 5.76 ms                                                     | 5.70 ms: 1.01x faster                                       |
| unpickle_list        | 2.72 us                                                     | 2.75 us: 1.01x slower                                       |
| pickle               | 7.34 us                                                     | 7.43 us: 1.01x slower                                       |
| pickle_dict          | 18.0 us                                                     | 18.4 us: 1.02x slower                                       |
| xml_etree_process    | 36.5 ms                                                     | 37.7 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                       |
| xml_etree_generate   | 53.3 ms                                                     | 55.8 ms: 1.05x slower                                       |
| unpickle_pure_python | 127 us                                                      | 133 us: 1.05x slower                                        |
| pickle_pure_python   | 183 us                                                      | 195 us: 1.07x slower                                        |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 22.2 ms                                                     | 19.5 ms: 1.14x faster                                       |
| python_startup_no_site | 17.8 ms                                                     | 16.2 ms: 1.09x faster                                       |
| Geometric mean         | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 21.8 ms                                                     | 22.9 ms: 1.05x slower                                       |
| mako            | 6.24 ms                                                     | 7.09 ms: 1.14x slower                                       |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 487 ms: 1.34x faster                                        |
| telco                      | 4.85 ms                                                     | 4.13 ms: 1.17x faster                                       |
| coverage                   | 46.7 ms                                                     | 40.8 ms: 1.14x faster                                       |
| python_startup             | 22.2 ms                                                     | 19.5 ms: 1.14x faster                                       |
| create_gc_cycles           | 829 us                                                      | 752 us: 1.10x faster                                        |
| python_startup_no_site     | 17.8 ms                                                     | 16.2 ms: 1.09x faster                                       |
| pycparser                  | 758 ms                                                      | 699 ms: 1.09x faster                                        |
| unpack_sequence            | 40.0 ns                                                     | 37.5 ns: 1.07x faster                                       |
| typing_runtime_protocols   | 100 us                                                      | 95.1 us: 1.06x faster                                       |
| unpickle                   | 8.63 us                                                     | 8.18 us: 1.06x faster                                       |
| aiohttp                    | 932 us                                                      | 884 us: 1.05x faster                                        |
| tornado_http               | 92.8 ms                                                     | 89.5 ms: 1.04x faster                                       |
| json_loads                 | 14.3 us                                                     | 13.9 us: 1.03x faster                                       |
| regex_v8                   | 14.7 ms                                                     | 14.2 ms: 1.03x faster                                       |
| gc_traversal               | 1.55 ms                                                     | 1.52 ms: 1.02x faster                                       |
| json_dumps                 | 5.76 ms                                                     | 5.70 ms: 1.01x faster                                       |
| mdp                        | 1.38 sec                                                    | 1.37 sec: 1.01x faster                                      |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                       |
| bench_mp_pool              | 69.6 ms                                                     | 69.2 ms: 1.01x faster                                       |
| sympy_expand               | 285 ms                                                      | 284 ms: 1.00x faster                                        |
| fannkuch                   | 245 ms                                                      | 247 ms: 1.01x slower                                        |
| unpickle_list              | 2.72 us                                                     | 2.75 us: 1.01x slower                                       |
| pickle                     | 7.34 us                                                     | 7.43 us: 1.01x slower                                       |
| pickle_dict                | 18.0 us                                                     | 18.4 us: 1.02x slower                                       |
| json                       | 2.98 ms                                                     | 3.05 ms: 1.02x slower                                       |
| pidigits                   | 148 ms                                                      | 152 ms: 1.03x slower                                        |
| xml_etree_process          | 36.5 ms                                                     | 37.7 ms: 1.03x slower                                       |
| meteor_contest             | 72.3 ms                                                     | 74.6 ms: 1.03x slower                                       |
| bench_thread_pool          | 828 us                                                      | 857 us: 1.04x slower                                        |
| deepcopy_reduce            | 2.02 us                                                     | 2.09 us: 1.04x slower                                       |
| pprint_safe_repr           | 493 ms                                                      | 513 ms: 1.04x slower                                        |
| sqlglot_optimize           | 33.1 ms                                                     | 34.5 ms: 1.04x slower                                       |
| xml_etree_iterparse        | 62.3 ms                                                     | 65.2 ms: 1.05x slower                                       |
| xml_etree_generate         | 53.3 ms                                                     | 55.8 ms: 1.05x slower                                       |
| unpickle_pure_python       | 127 us                                                      | 133 us: 1.05x slower                                        |
| sympy_str                  | 166 ms                                                      | 175 ms: 1.05x slower                                        |
| django_template            | 21.8 ms                                                     | 22.9 ms: 1.05x slower                                       |
| pprint_pformat             | 991 ms                                                      | 1.05 sec: 1.05x slower                                      |
| docutils                   | 1.57 sec                                                    | 1.66 sec: 1.05x slower                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.0 ms: 1.06x slower                                       |
| chameleon                  | 4.72 ms                                                     | 4.98 ms: 1.06x slower                                       |
| sqlglot_parse              | 761 us                                                      | 804 us: 1.06x slower                                        |
| scimark_fft                | 174 ms                                                      | 184 ms: 1.06x slower                                        |
| sympy_sum                  | 86.4 ms                                                     | 91.5 ms: 1.06x slower                                       |
| deepcopy                   | 223 us                                                      | 238 us: 1.07x slower                                        |
| pickle_pure_python         | 183 us                                                      | 195 us: 1.07x slower                                        |
| pyflate                    | 275 ms                                                      | 295 ms: 1.07x slower                                        |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                        |
| sqlglot_transpile          | 952 us                                                      | 1.02 ms: 1.07x slower                                       |
| go                         | 84.6 ms                                                     | 91.6 ms: 1.08x slower                                       |
| deepcopy_memo              | 21.8 us                                                     | 23.7 us: 1.09x slower                                       |
| scimark_monte_carlo        | 40.3 ms                                                     | 43.7 ms: 1.09x slower                                       |
| richards                   | 26.0 ms                                                     | 28.4 ms: 1.09x slower                                       |
| scimark_lu                 | 54.0 ms                                                     | 58.9 ms: 1.09x slower                                       |
| logging_format             | 6.15 us                                                     | 6.72 us: 1.09x slower                                       |
| regex_compile              | 80.1 ms                                                     | 87.5 ms: 1.09x slower                                       |
| sqlglot_normalize          | 171 ms                                                      | 187 ms: 1.09x slower                                        |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.56 ms: 1.09x slower                                       |
| richards_super             | 29.3 ms                                                     | 32.1 ms: 1.09x slower                                       |
| scimark_sor                | 72.0 ms                                                     | 78.8 ms: 1.09x slower                                       |
| logging_simple             | 5.72 us                                                     | 6.28 us: 1.10x slower                                       |
| dulwich_log                | 40.4 ms                                                     | 44.3 ms: 1.10x slower                                       |
| sqlite_synth               | 1.60 us                                                     | 1.76 us: 1.10x slower                                       |
| regex_dna                  | 114 ms                                                      | 126 ms: 1.11x slower                                        |
| hexiom                     | 3.69 ms                                                     | 4.10 ms: 1.11x slower                                       |
| nbody                      | 64.5 ms                                                     | 71.9 ms: 1.11x slower                                       |
| spectral_norm              | 59.2 ms                                                     | 66.9 ms: 1.13x slower                                       |
| nqueens                    | 55.5 ms                                                     | 62.8 ms: 1.13x slower                                       |
| crypto_pyaes               | 42.8 ms                                                     | 48.5 ms: 1.13x slower                                       |
| mako                       | 6.24 ms                                                     | 7.09 ms: 1.14x slower                                       |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                       |
| chaos                      | 37.9 ms                                                     | 43.3 ms: 1.14x slower                                       |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.16x slower                                       |
| deltablue                  | 1.86 ms                                                     | 2.16 ms: 1.16x slower                                       |
| float                      | 48.1 ms                                                     | 56.8 ms: 1.18x slower                                       |
| logging_silent             | 51.0 ns                                                     | 60.5 ns: 1.19x slower                                       |
| mypy2                      | 429 ms                                                      | 509 ms: 1.19x slower                                        |
| raytrace                   | 156 ms                                                      | 192 ms: 1.23x slower                                        |
| async_tree_memoization     | 271 ms                                                      | 339 ms: 1.25x slower                                        |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 489 ms: 1.26x slower                                        |
| async_tree_memoization_tg  | 288 ms                                                      | 367 ms: 1.27x slower                                        |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 2.10 sec: 1.28x slower                                      |
| async_tree_none            | 223 ms                                                      | 291 ms: 1.31x slower                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 502 ms: 1.34x slower                                        |
| comprehensions             | 10.2 us                                                     | 14.1 us: 1.38x slower                                       |
| async_tree_none_tg         | 206 ms                                                      | 285 ms: 1.39x slower                                        |
| async_tree_io              | 521 ms                                                      | 731 ms: 1.40x slower                                        |
| async_tree_io_tg           | 512 ms                                                      | 771 ms: 1.50x slower                                        |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                |

Benchmark hidden because not significant (5): pickle_list, xml_etree_parse, regex_effbot, tomli_loads, 2to3
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown