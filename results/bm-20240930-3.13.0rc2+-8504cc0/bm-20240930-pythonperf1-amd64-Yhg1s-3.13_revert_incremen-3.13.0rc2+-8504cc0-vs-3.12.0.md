# Results vs. 3.12.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-amd64
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 215 ms: 1.01x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.78 ms: 1.04x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 92.5 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                        |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 370 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 377 ms: 1.30x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                                       |
| nbody          | 71.9 ms                                                     | 68.5 ms: 1.05x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.9 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 180 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                        |
| pickle               | 7.43 us                                                     | 7.11 us: 1.05x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.64 us: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.86 us: 1.08x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| python_startup         | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| django_template | 22.9 ms                                                     | 22.2 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 505 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 200 ms: 1.43x faster                                                        |
| async_tree_io              | 731 ms                                                      | 516 ms: 1.42x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.1 us: 1.39x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 370 ms: 1.36x faster                                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 377 ms: 1.30x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 286 ms: 1.28x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 269 ms: 1.26x faster                                                        |
| mypy2                      | 509 ms                                                      | 430 ms: 1.18x faster                                                        |
| raytrace                   | 192 ms                                                      | 163 ms: 1.18x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.88 ms: 1.15x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                       |
| float                      | 56.8 ms                                                     | 49.9 ms: 1.14x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 53.2 ns: 1.14x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.4 ms: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.5 ms: 1.12x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.72 ms: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.72 us: 1.10x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.12 us: 1.10x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.4 ms: 1.09x faster                                                       |
| async_generators           | 239 ms                                                      | 219 ms: 1.09x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 44.4 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.1 ms: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 180 us: 1.09x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                        |
| richards_super             | 32.1 ms                                                     | 29.8 ms: 1.08x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 81.6 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 175 ms: 1.07x faster                                                        |
| unpack_sequence            | 37.5 ns                                                     | 35.0 ns: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.40 ms: 1.07x faster                                                       |
| pyflate                    | 295 ms                                                      | 277 ms: 1.07x faster                                                        |
| docutils                   | 1.66 sec                                                    | 1.56 sec: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 86.6 ms: 1.06x faster                                                       |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                        |
| nbody                      | 71.9 ms                                                     | 68.5 ms: 1.05x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 816 us: 1.05x faster                                                        |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 769 us: 1.05x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.11 us: 1.05x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 978 us: 1.05x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.78 ms: 1.04x faster                                                       |
| deepcopy                   | 238 us                                                      | 228 us: 1.04x faster                                                        |
| unpickle_list              | 2.75 us                                                     | 2.64 us: 1.04x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.8 us: 1.04x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.7 ms: 1.04x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 75.8 ms: 1.04x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 494 ms: 1.04x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 2.02 us: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 88.7 ms: 1.03x faster                                                       |
| django_template            | 22.9 ms                                                     | 22.2 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.9 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| 2to3                       | 218 ms                                                      | 215 ms: 1.01x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 245 ms: 1.01x faster                                                        |
| mdp                        | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| sympy_expand               | 284 ms                                                      | 288 ms: 1.01x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                       |
| tornado_http               | 89.5 ms                                                     | 92.5 ms: 1.03x slower                                                       |
| aiohttp                    | 884 us                                                      | 933 us: 1.05x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 813 us: 1.08x slower                                                        |
| pycparser                  | 699 ms                                                      | 756 ms: 1.08x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.86 us: 1.08x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.08 us: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.9 ms: 1.12x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.4 ms: 1.14x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.3 ms: 1.14x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.78 ms: 1.16x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 579 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (4): pathlib, bench_mp_pool, json_dumps, json
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.073x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown