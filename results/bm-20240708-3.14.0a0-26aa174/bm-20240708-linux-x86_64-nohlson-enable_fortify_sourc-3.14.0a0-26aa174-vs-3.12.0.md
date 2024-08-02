# Results vs. 3.12.0

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 26aa174
- commit date: 2024-07-08
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                 |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                   |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.0 ms: 1.14x faster                                                  |
| float          | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                  |
| regex_dna      | 212 ms                                                 | 229 ms: 1.08x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 208 us: 1.11x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                  |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                   |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 844 ms: 1.40x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 850 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 542 ms: 1.34x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 256 ms: 1.22x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                  |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 70.5 ms: 1.16x faster                                                  |
| chaos                      | 67.0 ms                                                | 57.8 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| nbody                      | 97.0 ms                                                | 85.0 ms: 1.14x faster                                                  |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.7 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                   |
| float                      | 84.7 ms                                                | 75.5 ms: 1.12x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.12x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 208 us: 1.11x faster                                                   |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.10x faster                                                   |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                  |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                   |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                  |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                   |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                  |
| logging_silent             | 104 ns                                                 | 97.1 ns: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.1 ms: 1.07x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.01 ms: 1.07x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 791 us: 1.06x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                                   |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                                  |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                   |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                   |
| dask                       | 372 ms                                                 | 357 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                   |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                   |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 485 ms: 1.01x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.76 ms: 1.01x faster                                                  |
| go                         | 139 ms                                                 | 138 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.66 sec: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.82 ms: 1.06x slower                                                  |
| regex_dna                  | 212 ms                                                 | 229 ms: 1.08x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.12x slower                                                  |
| telco                      | 7.10 ms                                                | 8.26 ms: 1.16x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.18x slower                                                  |
| coverage                   | 72.7 ms                                                | 92.4 ms: 1.27x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (5): pycparser, richards_super, richards, asyncio_tcp_ssl, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240708-3.14.0a0-26aa174/bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x