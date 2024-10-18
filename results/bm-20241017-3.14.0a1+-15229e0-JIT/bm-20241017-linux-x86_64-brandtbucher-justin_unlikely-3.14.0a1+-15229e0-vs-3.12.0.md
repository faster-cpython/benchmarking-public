# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.04x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                    |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                  |
| tornado_http   | 103 ms                                                 | 95.4 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 374 ms: 1.54x faster                                                    |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                   |
| float          | 84.7 ms                                                | 75.3 ms: 1.12x faster                                                   |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 141 ms: 1.05x faster                                                    |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                    |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                    |
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                    |
| pickle_dict          | 35.5 us                                                | 35.8 us: 1.01x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                                   |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                   |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                   |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 374 ms: 1.54x faster                                                    |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 318 ms: 1.41x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                   |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                    |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.27x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 974 ms: 1.21x faster                                                    |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                   |
| nbody                      | 97.0 ms                                                | 80.9 ms: 1.20x faster                                                   |
| mako                       | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                   |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.15x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                   |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                    |
| float                      | 84.7 ms                                                | 75.3 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                   |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                   |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                   |
| tornado_http               | 103 ms                                                 | 95.4 ms: 1.08x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                   |
| json                       | 5.26 ms                                                | 4.92 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                    |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                    |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                                   |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                    |
| go                         | 139 ms                                                 | 132 ms: 1.05x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                    |
| regex_compile              | 148 ms                                                 | 141 ms: 1.05x faster                                                    |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.0 ms: 1.02x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 461 ms: 1.00x faster                                                    |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.01x slower                                                    |
| pickle_dict                | 35.5 us                                                | 35.8 us: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                    |
| pickle_list                | 5.08 us                                                | 5.16 us: 1.02x slower                                                   |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                    |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                    |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                   |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                    |
| sympy_expand               | 478 ms                                                 | 499 ms: 1.04x slower                                                    |
| sympy_sum                  | 169 ms                                                 | 177 ms: 1.05x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                   |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                   |
| nqueens                    | 83.3 ms                                                | 88.4 ms: 1.06x slower                                                   |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.98 ms: 1.09x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.9 ms: 1.09x slower                                                   |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.5 ms: 1.10x slower                                                   |
| generators                 | 31.2 ms                                                | 35.3 ms: 1.13x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.0 ms: 1.16x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.45 ms: 1.17x slower                                                   |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                   |
| unpack_sequence            | 54.0 ns                                                | 106 ns: 1.96x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 84.2 ms: 3.51x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (4): sqlglot_transpile, pycparser, unpickle_list, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x