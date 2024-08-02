# Results vs. 3.12.0

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 0a5aba7
- commit date: 2024-06-25
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| docutils       | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                 |
| tornado_http   | 103 ms                                                 | 96.2 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 852 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.4 ms: 1.14x faster                                                  |
| float          | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.11x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                  |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.6 us: 1.03x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 302 ms: 1.49x faster                                                   |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                   |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 852 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 840 ms: 1.38x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 548 ms: 1.32x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                  |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                  |
| nbody                      | 97.0 ms                                                | 85.4 ms: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                  |
| regex_compile              | 148 ms                                                 | 133 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                  |
| float                      | 84.7 ms                                                | 77.0 ms: 1.10x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                   |
| generators                 | 31.2 ms                                                | 29.1 ms: 1.07x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 158 ms: 1.07x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.54 ms: 1.07x faster                                                  |
| scimark_fft                | 382 ms                                                 | 357 ms: 1.07x faster                                                   |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                  |
| tornado_http               | 103 ms                                                 | 96.2 ms: 1.07x faster                                                  |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                                   |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.1 ms: 1.05x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                                  |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 804 us: 1.05x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                  |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                  |
| dask                       | 372 ms                                                 | 360 ms: 1.03x faster                                                   |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                  |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                   |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                   |
| pickle_dict                | 35.5 us                                                | 34.6 us: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.3 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                   |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 482 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.74 sec: 1.01x faster                                                 |
| pyflate                    | 482 ms                                                 | 479 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 54.5 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 68.8 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| go                         | 139 ms                                                 | 142 ms: 1.02x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                  |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.03x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.96 us: 1.05x slower                                                  |
| richards_super             | 51.5 ms                                                | 54.2 ms: 1.05x slower                                                  |
| richards                   | 45.8 ms                                                | 48.4 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                   |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                  |
| telco                      | 7.10 ms                                                | 8.31 ms: 1.17x slower                                                  |
| coverage                   | 72.7 ms                                                | 91.3 ms: 1.26x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (9): xml_etree_parse, unpickle_list, django_template, pickle_list, bench_mp_pool, pidigits, scimark_sparse_mat_mult, coroutines, pycparser
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240625-3.14.0a0-0a5aba7/bm-20240625-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-0a5aba7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.97x