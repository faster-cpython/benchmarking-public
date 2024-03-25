# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.58 ms: 1.09x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 85.1 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 563 ms: 1.37x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 275 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                       |
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                       |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| pickle_pure_python   | 195 us                                                      | 173 us: 1.13x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 17.4 us: 1.06x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| pickle               | 7.43 us                                                     | 7.36 us: 1.01x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.78 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.67 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.71 ms: 1.24x faster                                                       |
| django_template | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 563 ms: 1.37x faster                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 69.9 us: 1.36x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 270 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 50.9 ms: 1.31x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 386 ms: 1.27x faster                                                        |
| nbody                      | 71.9 ms                                                     | 57.0 ms: 1.26x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.67 sec: 1.26x faster                                                      |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.71 ms: 1.24x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 275 ms: 1.24x faster                                                        |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.23 ms: 1.14x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| pickle_pure_python         | 195 us                                                      | 173 us: 1.13x faster                                                        |
| deepcopy_memo              | 23.7 us                                                     | 21.2 us: 1.12x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 43.3 ms: 1.12x faster                                                       |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.8 ns: 1.10x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.4 ms: 1.10x faster                                                       |
| mypy2                      | 509 ms                                                      | 462 ms: 1.10x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 40.6 ms: 1.09x faster                                                       |
| scimark_fft                | 184 ms                                                      | 169 ms: 1.09x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.58 ms: 1.09x faster                                                       |
| deepcopy                   | 238 us                                                      | 219 us: 1.08x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 476 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 975 ms: 1.07x faster                                                        |
| raytrace                   | 192 ms                                                      | 181 ms: 1.06x faster                                                        |
| sympy_str                  | 175 ms                                                      | 165 ms: 1.06x faster                                                        |
| xml_etree_generate         | 55.8 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.3 ms: 1.06x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.4 us: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.05x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.96 us: 1.05x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 85.1 ms: 1.05x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.39 us: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 464 ms: 1.05x faster                                                        |
| regex_compile              | 87.5 ms                                                     | 83.7 ms: 1.05x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 76.9 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                        |
| pyflate                    | 295 ms                                                      | 283 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 87.9 ms: 1.04x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.08 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.7 ms: 1.04x faster                                                       |
| pycparser                  | 699 ms                                                      | 676 ms: 1.03x faster                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.48 ms: 1.03x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 783 us: 1.03x faster                                                        |
| create_gc_cycles           | 752 us                                                      | 733 us: 1.03x faster                                                        |
| sqlglot_normalize          | 187 ms                                                      | 183 ms: 1.02x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.00 ms: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.59 ms: 1.02x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| richards                   | 28.4 ms                                                     | 28.0 ms: 1.01x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.36 us: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.2 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 68.7 ms: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.2 ms: 1.01x faster                                                       |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.78 us: 1.01x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.2 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 92.6 ms: 1.01x slower                                                       |
| aiohttp                    | 884 us                                                      | 899 us: 1.02x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                       |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.03x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.3 ms: 1.03x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.67 us: 1.06x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.37 ms: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.55 sec: 1.13x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.77 ms: 1.15x slower                                                       |
| python_startup             | 19.5 ms                                                     | 23.2 ms: 1.19x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 70.4 ms: 1.20x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 47.7 ns: 1.27x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, sympy_expand, pickle_list
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x


# Memory

- memory change: unknown