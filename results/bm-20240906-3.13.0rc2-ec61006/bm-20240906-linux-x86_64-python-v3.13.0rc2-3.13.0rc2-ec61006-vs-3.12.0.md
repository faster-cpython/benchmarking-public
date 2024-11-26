# Results vs. 3.12.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                         |
| chameleon      | 7.41 ms                                                | 6.97 ms: 1.06x faster                                        |
| docutils       | 2.77 sec                                               | 2.74 sec: 1.01x faster                                       |
| tornado_http   | 103 ms                                                 | 91.4 ms: 1.12x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 434 ms: 1.32x faster                                         |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                         |
| async_tree_io              | 1.16 sec                                               | 889 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 588 ms: 1.23x faster                                         |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.0 ms: 1.10x faster                                        |
| float          | 84.7 ms                                                | 77.4 ms: 1.09x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.03x faster                                        |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                         |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                       |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                         |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                        |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                         |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                        |
| unpickle_list        | 5.29 us                                                | 5.06 us: 1.04x faster                                        |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 87.5 ms: 1.02x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 60.8 ms: 1.02x faster                                        |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                        |
| pickle_list          | 5.08 us                                                | 5.25 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                        |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                         |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.32x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 434 ms: 1.32x faster                                         |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                         |
| async_tree_io              | 1.16 sec                                               | 889 ms: 1.30x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 931 ms: 1.27x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 588 ms: 1.23x faster                                         |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                         |
| mypy2                      | 830 ms                                                 | 717 ms: 1.16x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                        |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                        |
| logging_format             | 7.23 us                                                | 6.39 us: 1.13x faster                                        |
| unpack_sequence            | 54.0 ns                                                | 47.9 ns: 1.13x faster                                        |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                       |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                        |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                        |
| tornado_http               | 103 ms                                                 | 91.4 ms: 1.12x faster                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                         |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                         |
| nbody                      | 97.0 ms                                                | 88.0 ms: 1.10x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                        |
| float                      | 84.7 ms                                                | 77.4 ms: 1.09x faster                                        |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                        |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                        |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                        |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                         |
| chameleon                  | 7.41 ms                                                | 6.97 ms: 1.06x faster                                        |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                         |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                        |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                         |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                        |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                         |
| coroutines                 | 23.2 ms                                                | 22.1 ms: 1.05x faster                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                         |
| scimark_fft                | 382 ms                                                 | 365 ms: 1.05x faster                                         |
| unpickle_list              | 5.29 us                                                | 5.06 us: 1.04x faster                                        |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                         |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.22 us: 1.04x faster                                        |
| dask                       | 372 ms                                                 | 358 ms: 1.04x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.03x faster                                        |
| deepcopy                   | 371 us                                                 | 359 us: 1.03x faster                                         |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 39.5 us: 1.03x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                       |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                        |
| sympy_expand               | 478 ms                                                 | 464 ms: 1.03x faster                                         |
| bench_thread_pool          | 842 us                                                 | 818 us: 1.03x faster                                         |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                         |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                         |
| asyncio_tcp                | 491 ms                                                 | 480 ms: 1.02x faster                                         |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 87.5 ms: 1.02x faster                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                        |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 60.8 ms: 1.02x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                         |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                        |
| docutils                   | 2.77 sec                                               | 2.74 sec: 1.01x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| aiohttp                    | 1.15 ms                                                | 1.14 ms: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                       |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                         |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                         |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                         |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                         |
| richards                   | 45.8 ms                                                | 47.3 ms: 1.03x slower                                        |
| pickle_list                | 5.08 us                                                | 5.25 us: 1.03x slower                                        |
| richards_super             | 51.5 ms                                                | 53.2 ms: 1.03x slower                                        |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.04x slower                                        |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.05x slower                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                        |
| telco                      | 7.10 ms                                                | 8.63 ms: 1.22x slower                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (6): gunicorn, json, json_dumps, bench_mp_pool, sqlite_synth, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (8) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.060x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.98x