# Results vs. 3.12.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-x86_64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.003x slower
- HPT reliability: 59.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                                       |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 819 ms: 1.29x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.25x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                                         |
| async_tree_none            | 452 ms                                                       | 378 ms: 1.20x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 457 ms: 1.19x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 468 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 606 ms: 1.15x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| nbody          | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| float          | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.0 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 100.0 ms: 1.03x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                        |
| pickle               | 10.5 us                                                      | 10.6 us: 1.00x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.46 us: 1.01x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.73 us: 1.02x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.03x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.28 sec: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                        |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 819 ms: 1.29x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.25x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 580 ms: 1.20x faster                                                         |
| async_tree_none            | 452 ms                                                       | 378 ms: 1.20x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 457 ms: 1.19x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 468 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 606 ms: 1.15x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.1 ms: 1.13x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 49.8 ns: 1.07x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 75.3 ms: 1.07x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.8 ms: 1.06x faster                                                        |
| raytrace                   | 298 ms                                                       | 280 ms: 1.06x faster                                                         |
| async_generators           | 390 ms                                                       | 368 ms: 1.06x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 903 us: 1.05x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 31.0 us: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.18 us: 1.04x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.8 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100.0 ms: 1.03x faster                                                       |
| chaos                      | 64.0 ms                                                      | 62.2 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                        |
| dask                       | 392 ms                                                       | 382 ms: 1.03x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| docutils                   | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                                       |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                                         |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 97.7 ms: 1.01x faster                                                        |
| nbody                      | 88.0 ms                                                      | 87.0 ms: 1.01x faster                                                        |
| regex_compile              | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 65.0 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.00x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                                         |
| pickle_list                | 4.43 us                                                      | 4.46 us: 1.01x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 90.6 ms: 1.01x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                         |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.01x slower                                                         |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 4.73 us: 1.02x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 820 ms: 1.02x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.02x slower                                                         |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 59.6 ms: 1.02x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.45 us: 1.02x slower                                                        |
| json                       | 5.12 ms                                                      | 5.25 ms: 1.03x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.03x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.35 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.95 ms: 1.04x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 98.5 ns: 1.04x slower                                                        |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                                         |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                        |
| sympy_expand               | 484 ms                                                       | 507 ms: 1.05x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 38.6 us: 1.05x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 60.3 ms: 1.05x slower                                                        |
| deepcopy                   | 368 us                                                       | 388 us: 1.05x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.28 sec: 1.05x slower                                                       |
| aiohttp                    | 1.02 ms                                                      | 1.08 ms: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.37 ms: 1.07x slower                                                        |
| float                      | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                                        |
| spectral_norm              | 91.6 ms                                                      | 98.3 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.8 ms: 1.09x slower                                                        |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                         |
| fannkuch                   | 350 ms                                                       | 390 ms: 1.12x slower                                                         |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.13x slower                                                         |
| pyflate                    | 439 ms                                                       | 494 ms: 1.13x slower                                                         |
| richards                   | 45.7 ms                                                      | 51.9 ms: 1.13x slower                                                        |
| richards_super             | 51.3 ms                                                      | 58.4 ms: 1.14x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.83 ms: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.6 ms: 1.18x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.16 ms: 1.20x slower                                                        |
| scimark_sor                | 109 ms                                                       | 131 ms: 1.21x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.53 ms: 1.23x slower                                                        |
| mypy2                      | 830 ms                                                       | 1.05 sec: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): bench_mp_pool, pickle_pure_python, json_loads, sqlglot_transpile, asyncio_websockets
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 59.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x