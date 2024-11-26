# Results vs. 3.12.0

- fork: python
- ref: cfbc841ef3c27b3e65d1
- machine: linux-x86_64
- commit hash: cfbc841
- commit date: 2024-09-03
- overall geometric mean: 1.089x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                  |
| docutils       | 2.77 sec                                               | 3.03 sec: 1.09x slower                                                |
| tornado_http   | 103 ms                                                 | 95.6 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 900 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.1 ms: 1.23x faster                                                 |
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                 |
| django_template | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                 |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                  |
| deepcopy                   | 371 us                                                 | 266 us: 1.40x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 900 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 571 ms: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 65.9 ms: 1.24x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                  |
| nbody                      | 97.0 ms                                                | 79.1 ms: 1.23x faster                                                 |
| mako                       | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                 |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.20 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                 |
| richards                   | 45.8 ms                                                | 39.2 ms: 1.17x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                 |
| spectral_norm              | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                 |
| richards_super             | 51.5 ms                                                | 45.4 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                                 |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                 |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 109 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                                  |
| tornado_http               | 103 ms                                                 | 95.6 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                  |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                  |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.01x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 485 ms: 1.01x faster                                                  |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                                  |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                  |
| dulwich_log                | 68.5 ms                                                | 68.8 ms: 1.00x slower                                                 |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 173 ms: 1.02x slower                                                  |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                 |
| django_template            | 34.6 ms                                                | 35.6 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 57.7 ms: 1.05x slower                                                 |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                  |
| json                       | 5.26 ms                                                | 5.56 ms: 1.06x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.85 ms: 1.07x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.03 sec: 1.09x slower                                                |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                 |
| coverage                   | 72.7 ms                                                | 86.5 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): pycparser, sympy_str, bench_mp_pool, json_loads
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240903-3.14.0a0-cfbc841-JIT/bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.089x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x