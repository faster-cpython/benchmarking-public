# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.04x faster
- HPT reliability: 88.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 240 ms: 1.10x slower                                             |
| docutils       | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                           |
| tornado_http   | 89.5 ms                                                     | 88.1 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                       | 1.08x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 291 ms                                                      | 202 ms: 1.45x faster                                             |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.44x faster                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                             |
| async_tree_io_tg           | 771 ms                                                      | 556 ms: 1.39x faster                                             |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                             |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                             |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 49.6 ms: 1.45x faster                                            |
| float          | 56.8 ms                                                     | 53.4 ms: 1.06x faster                                            |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                       | 1.16x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                             |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                            |
| regex_compile  | 87.5 ms                                                     | 94.7 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                       | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                            |
| xml_etree_process    | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                            |
| xml_etree_generate   | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                            |
| tomli_loads          | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                           |
| pickle_dict          | 18.4 us                                                     | 17.8 us: 1.04x faster                                            |
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                            |
| json_dumps           | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                            |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                            |
| unpickle_pure_python | 133 us                                                      | 143 us: 1.08x slower                                             |
| unpickle             | 8.18 us                                                     | 9.11 us: 1.11x slower                                            |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                     |

Benchmark hidden because not significant (4): pickle_list, pickle, pickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                            |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                            |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.20 ms: 1.36x faster                                            |
| django_template | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                            |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 23.7 us                                                     | 15.3 us: 1.55x faster                                            |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.37 sec: 1.53x faster                                           |
| spectral_norm              | 66.9 ms                                                     | 44.8 ms: 1.49x faster                                            |
| nbody                      | 71.9 ms                                                     | 49.6 ms: 1.45x faster                                            |
| async_tree_none            | 291 ms                                                      | 202 ms: 1.45x faster                                             |
| async_tree_none_tg         | 285 ms                                                      | 197 ms: 1.44x faster                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 257 ms: 1.43x faster                                             |
| async_tree_io_tg           | 771 ms                                                      | 556 ms: 1.39x faster                                             |
| mako                       | 7.09 ms                                                     | 5.20 ms: 1.36x faster                                            |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.35x faster                                            |
| async_tree_memoization     | 339 ms                                                      | 255 ms: 1.33x faster                                             |
| scimark_sor                | 78.8 ms                                                     | 60.5 ms: 1.30x faster                                            |
| deepcopy                   | 238 us                                                      | 183 us: 1.30x faster                                             |
| crypto_pyaes               | 48.5 ms                                                     | 38.1 ms: 1.27x faster                                            |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 396 ms: 1.27x faster                                             |
| async_tree_io              | 731 ms                                                      | 578 ms: 1.27x faster                                             |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 393 ms: 1.24x faster                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.06 ms: 1.24x faster                                            |
| deltablue                  | 2.16 ms                                                     | 1.83 ms: 1.18x faster                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.83 us: 1.14x faster                                            |
| pyflate                    | 295 ms                                                      | 263 ms: 1.12x faster                                             |
| scimark_lu                 | 58.9 ms                                                     | 53.9 ms: 1.09x faster                                            |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.8 ms: 1.09x faster                                            |
| xml_etree_process          | 37.7 ms                                                     | 34.8 ms: 1.08x faster                                            |
| xml_etree_generate         | 55.8 ms                                                     | 51.7 ms: 1.08x faster                                            |
| chaos                      | 43.3 ms                                                     | 40.7 ms: 1.07x faster                                            |
| float                      | 56.8 ms                                                     | 53.4 ms: 1.06x faster                                            |
| pathlib                    | 80.5 ms                                                     | 75.6 ms: 1.06x faster                                            |
| logging_simple             | 6.28 us                                                     | 5.91 us: 1.06x faster                                            |
| logging_silent             | 60.5 ns                                                     | 57.0 ns: 1.06x faster                                            |
| logging_format             | 6.72 us                                                     | 6.33 us: 1.06x faster                                            |
| fannkuch                   | 247 ms                                                      | 233 ms: 1.06x faster                                             |
| tomli_loads                | 1.37 sec                                                    | 1.29 sec: 1.06x faster                                           |
| dulwich_log                | 44.3 ms                                                     | 42.0 ms: 1.05x faster                                            |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                            |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                             |
| bench_thread_pool          | 857 us                                                      | 820 us: 1.04x faster                                             |
| nqueens                    | 62.8 ms                                                     | 60.2 ms: 1.04x faster                                            |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                            |
| pickle_dict                | 18.4 us                                                     | 17.8 us: 1.04x faster                                            |
| generators                 | 22.5 ms                                                     | 21.9 ms: 1.03x faster                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 42.7 ms: 1.02x faster                                            |
| sqlite_synth               | 1.76 us                                                     | 1.73 us: 1.02x faster                                            |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                             |
| tornado_http               | 89.5 ms                                                     | 88.1 ms: 1.02x faster                                            |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                            |
| meteor_contest             | 74.6 ms                                                     | 75.3 ms: 1.01x slower                                            |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                             |
| bench_mp_pool              | 69.2 ms                                                     | 70.2 ms: 1.01x slower                                            |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                            |
| pprint_safe_repr           | 513 ms                                                      | 524 ms: 1.02x slower                                             |
| pprint_pformat             | 1.05 sec                                                    | 1.07 sec: 1.03x slower                                           |
| raytrace                   | 192 ms                                                      | 198 ms: 1.03x slower                                             |
| json_dumps                 | 5.70 ms                                                     | 5.89 ms: 1.03x slower                                            |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                            |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                            |
| sqlglot_normalize          | 187 ms                                                      | 198 ms: 1.06x slower                                             |
| async_generators           | 239 ms                                                      | 257 ms: 1.07x slower                                             |
| unpickle_pure_python       | 133 us                                                      | 143 us: 1.08x slower                                             |
| sympy_str                  | 175 ms                                                      | 189 ms: 1.08x slower                                             |
| sympy_sum                  | 91.5 ms                                                     | 99.1 ms: 1.08x slower                                            |
| regex_compile              | 87.5 ms                                                     | 94.7 ms: 1.08x slower                                            |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                           |
| telco                      | 4.13 ms                                                     | 4.53 ms: 1.10x slower                                            |
| 2to3                       | 218 ms                                                      | 240 ms: 1.10x slower                                             |
| sqlglot_parse              | 804 us                                                      | 887 us: 1.10x slower                                             |
| unpickle                   | 8.18 us                                                     | 9.11 us: 1.11x slower                                            |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.13x slower                                            |
| python_startup             | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                            |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                            |
| sqlglot_optimize           | 34.5 ms                                                     | 39.7 ms: 1.15x slower                                            |
| sympy_integrate            | 13.0 ms                                                     | 14.9 ms: 1.15x slower                                            |
| django_template            | 22.9 ms                                                     | 26.4 ms: 1.15x slower                                            |
| docutils                   | 1.66 sec                                                    | 1.93 sec: 1.16x slower                                           |
| sympy_expand               | 284 ms                                                      | 332 ms: 1.17x slower                                             |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                             |
| create_gc_cycles           | 752 us                                                      | 895 us: 1.19x slower                                             |
| hexiom                     | 4.10 ms                                                     | 4.88 ms: 1.19x slower                                            |
| richards_super             | 32.1 ms                                                     | 39.3 ms: 1.22x slower                                            |
| richards                   | 28.4 ms                                                     | 36.6 ms: 1.29x slower                                            |
| unpack_sequence            | 37.5 ns                                                     | 59.6 ns: 1.59x slower                                            |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                     |

Benchmark hidden because not significant (7): asyncio_tcp, pickle_list, regex_effbot, pickle, go, pickle_pure_python, unpickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 88.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown