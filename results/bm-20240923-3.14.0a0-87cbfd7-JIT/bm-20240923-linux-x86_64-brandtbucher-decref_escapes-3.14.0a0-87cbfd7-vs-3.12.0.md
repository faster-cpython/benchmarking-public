# Results vs. 3.12.0

- fork: brandtbucher
- ref: decref_escapes
- machine: linux-x86_64
- commit hash: 87cbfd7
- commit date: 2024-09-23
- overall geometric mean: 1.07x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                 |
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.2 us: 1.07x faster                                                 |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                 |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 395 ms: 1.46x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                  |
| mako                       | 11.9 ms                                                | 9.77 ms: 1.22x faster                                                 |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.6 ms: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                 |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.19x faster                                                |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.1 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.32 ms: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 78.2 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                 |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                  |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                 |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                  |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                  |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.2 us: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                 |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                  |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                  |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                                  |
| json                       | 5.26 ms                                                | 5.04 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                 |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                 |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                  |
| pickle_list                | 5.08 us                                                | 5.04 us: 1.01x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 494 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                                 |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.91 ms: 1.03x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                  |
| nqueens                    | 83.3 ms                                                | 86.1 ms: 1.03x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                 |
| generators                 | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                 |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 58.2 ms: 1.06x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                |
| hexiom                     | 6.41 ms                                                | 7.00 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 112 ns: 2.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (6): pycparser, sympy_str, bench_mp_pool, dulwich_log, regex_effbot, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-87cbfd7-JIT/bm-20240923-linux-x86_64-brandtbucher-decref_escapes-3.14.0a0-87cbfd7.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x