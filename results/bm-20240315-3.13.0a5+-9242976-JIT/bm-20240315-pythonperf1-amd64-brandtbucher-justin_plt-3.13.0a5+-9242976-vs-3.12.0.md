# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_plt
- machine: windows-amd64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                    |
| chameleon      | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                   |
| docutils       | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                  |
| tornado_http   | 89.5 ms                                                     | 83.9 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                       | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 262 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 451 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 464 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 339 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 285 ms                                                      | 268 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 771 ms                                                      | 740 ms: 1.04x faster                                                    |
| async_tree_io              | 731 ms                                                      | 714 ms: 1.02x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                            |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 57.3 ms: 1.25x faster                                                   |
| float          | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                   |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                       | 1.15x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.3 ms: 1.06x faster                                                   |
| regex_dna      | 126 ms                                                      | 125 ms: 1.01x faster                                                    |
| regex_v8       | 14.2 ms                                                     | 17.2 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                       | 1.03x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                  |
| pickle_pure_python   | 195 us                                                      | 174 us: 1.13x faster                                                    |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.07x faster                                                    |
| pickle_dict          | 18.4 us                                                     | 17.5 us: 1.05x faster                                                   |
| xml_etree_generate   | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                   |
| json_dumps           | 5.70 ms                                                     | 5.48 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                   |
| pickle               | 7.43 us                                                     | 7.25 us: 1.03x faster                                                   |
| json_loads           | 13.9 us                                                     | 13.6 us: 1.02x faster                                                   |
| pickle_list          | 2.83 us                                                     | 2.77 us: 1.02x faster                                                   |
| xml_etree_process    | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                   |
| xml_etree_parse      | 93.0 ms                                                     | 93.7 ms: 1.01x slower                                                   |
| unpickle             | 8.18 us                                                     | 8.57 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 23.1 ms: 1.19x slower                                                   |
| python_startup_no_site | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.52 ms: 1.28x faster                                                   |
| django_template | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols   | 95.1 us                                                     | 68.2 us: 1.39x faster                                                   |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                   |
| spectral_norm              | 66.9 ms                                                     | 51.5 ms: 1.30x faster                                                   |
| mako                       | 7.09 ms                                                     | 5.52 ms: 1.28x faster                                                   |
| nbody                      | 71.9 ms                                                     | 57.3 ms: 1.25x faster                                                   |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.73 sec: 1.21x faster                                                  |
| float                      | 56.8 ms                                                     | 48.3 ms: 1.18x faster                                                   |
| mypy2                      | 509 ms                                                      | 435 ms: 1.17x faster                                                    |
| fannkuch                   | 247 ms                                                      | 212 ms: 1.16x faster                                                    |
| tomli_loads                | 1.37 sec                                                    | 1.19 sec: 1.15x faster                                                  |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.24 ms: 1.14x faster                                                   |
| logging_silent             | 60.5 ns                                                     | 53.2 ns: 1.14x faster                                                   |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.13x faster                                                    |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                   |
| crypto_pyaes               | 48.5 ms                                                     | 43.5 ms: 1.11x faster                                                   |
| async_tree_none            | 291 ms                                                      | 262 ms: 1.11x faster                                                    |
| coroutines                 | 14.3 ms                                                     | 12.9 ms: 1.10x faster                                                   |
| pprint_pformat             | 1.05 sec                                                    | 948 ms: 1.10x faster                                                    |
| pprint_safe_repr           | 513 ms                                                      | 467 ms: 1.10x faster                                                    |
| deepcopy_memo              | 23.7 us                                                     | 21.6 us: 1.10x faster                                                   |
| scimark_fft                | 184 ms                                                      | 169 ms: 1.09x faster                                                    |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.1 ms: 1.09x faster                                                   |
| chaos                      | 43.3 ms                                                     | 39.8 ms: 1.09x faster                                                   |
| deepcopy                   | 238 us                                                      | 219 us: 1.09x faster                                                    |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 451 ms: 1.09x faster                                                    |
| sympy_str                  | 175 ms                                                      | 162 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 464 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 339 ms: 1.08x faster                                                    |
| deltablue                  | 2.16 ms                                                     | 2.00 ms: 1.08x faster                                                   |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                   |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                    |
| sympy_sum                  | 91.5 ms                                                     | 85.7 ms: 1.07x faster                                                   |
| tornado_http               | 89.5 ms                                                     | 83.9 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.07x faster                                                    |
| logging_simple             | 6.28 us                                                     | 5.89 us: 1.06x faster                                                   |
| pyflate                    | 295 ms                                                      | 277 ms: 1.06x faster                                                    |
| dulwich_log                | 44.3 ms                                                     | 41.6 ms: 1.06x faster                                                   |
| regex_compile              | 87.5 ms                                                     | 82.3 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 268 ms: 1.06x faster                                                    |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                                   |
| chameleon                  | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                   |
| sqlglot_parse              | 804 us                                                      | 761 us: 1.06x faster                                                    |
| docutils                   | 1.66 sec                                                    | 1.58 sec: 1.05x faster                                                  |
| pickle_dict                | 18.4 us                                                     | 17.5 us: 1.05x faster                                                   |
| django_template            | 22.9 ms                                                     | 21.8 ms: 1.05x faster                                                   |
| pathlib                    | 80.5 ms                                                     | 76.6 ms: 1.05x faster                                                   |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                   |
| pycparser                  | 699 ms                                                      | 669 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 771 ms                                                      | 740 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.02 ms                                                     | 981 us: 1.04x faster                                                    |
| nqueens                    | 62.8 ms                                                     | 60.3 ms: 1.04x faster                                                   |
| json_dumps                 | 5.70 ms                                                     | 5.48 ms: 1.04x faster                                                   |
| richards                   | 28.4 ms                                                     | 27.4 ms: 1.04x faster                                                   |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.1 ms: 1.03x faster                                                   |
| meteor_contest             | 74.6 ms                                                     | 72.7 ms: 1.03x faster                                                   |
| pickle                     | 7.43 us                                                     | 7.25 us: 1.03x faster                                                   |
| json_loads                 | 13.9 us                                                     | 13.6 us: 1.02x faster                                                   |
| async_tree_io              | 731 ms                                                      | 714 ms: 1.02x faster                                                    |
| pickle_list                | 2.83 us                                                     | 2.77 us: 1.02x faster                                                   |
| xml_etree_process          | 37.7 ms                                                     | 36.9 ms: 1.02x faster                                                   |
| sympy_expand               | 284 ms                                                      | 278 ms: 1.02x faster                                                    |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 33.9 ms: 1.02x faster                                                   |
| async_generators           | 239 ms                                                      | 236 ms: 1.01x faster                                                    |
| regex_dna                  | 126 ms                                                      | 125 ms: 1.01x faster                                                    |
| xml_etree_parse            | 93.0 ms                                                     | 93.7 ms: 1.01x slower                                                   |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                    |
| aiohttp                    | 884 us                                                      | 897 us: 1.01x slower                                                    |
| go                         | 91.6 ms                                                     | 94.1 ms: 1.03x slower                                                   |
| scimark_sor                | 78.8 ms                                                     | 81.0 ms: 1.03x slower                                                   |
| hexiom                     | 4.10 ms                                                     | 4.29 ms: 1.05x slower                                                   |
| unpickle                   | 8.18 us                                                     | 8.57 us: 1.05x slower                                                   |
| mdp                        | 1.37 sec                                                    | 1.49 sec: 1.09x slower                                                  |
| telco                      | 4.13 ms                                                     | 4.70 ms: 1.14x slower                                                   |
| coverage                   | 40.8 ms                                                     | 47.3 ms: 1.16x slower                                                   |
| python_startup             | 19.5 ms                                                     | 23.1 ms: 1.19x slower                                                   |
| regex_v8                   | 14.2 ms                                                     | 17.2 ms: 1.21x slower                                                   |
| scimark_lu                 | 58.9 ms                                                     | 72.2 ms: 1.23x slower                                                   |
| python_startup_no_site     | 16.2 ms                                                     | 21.0 ms: 1.29x slower                                                   |
| unpack_sequence            | 37.5 ns                                                     | 49.1 ns: 1.31x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                            |

Benchmark hidden because not significant (9): bench_thread_pool, async_tree_memoization, regex_effbot, create_gc_cycles, sympy_integrate, bench_mp_pool, unpickle_list, gc_traversal, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x


# Memory

- memory change: unknown