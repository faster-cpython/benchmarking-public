# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 273 ms: 1.00x faster                                                  |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                |
| tornado_http   | 103 ms                                                 | 94.0 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                  |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 483 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 990 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 608 ms: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                 |
| nbody          | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                 |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.9 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                                 |
| unpickle_list        | 5.29 us                                                | 5.12 us: 1.03x faster                                                 |
| pickle_list          | 5.08 us                                                | 4.99 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                 |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.43 ms: 1.07x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                 |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                 |
| deepcopy                   | 371 us                                                 | 278 us: 1.34x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_none            | 472 ms                                                 | 364 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 454 ms: 1.27x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 934 ms: 1.24x faster                                                  |
| mako                       | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 67.4 ms: 1.22x faster                                                 |
| float                      | 84.7 ms                                                | 69.8 ms: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                 |
| nbody                      | 97.0 ms                                                | 80.3 ms: 1.21x faster                                                 |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                |
| fannkuch                   | 417 ms                                                 | 348 ms: 1.20x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 483 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 990 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 608 ms: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.2 ms: 1.19x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                 |
| raytrace                   | 312 ms                                                 | 273 ms: 1.15x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                 |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                 |
| richards                   | 45.8 ms                                                | 41.5 ms: 1.11x faster                                                 |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                  |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.61 ms: 1.10x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                                  |
| tornado_http               | 103 ms                                                 | 94.0 ms: 1.09x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| richards_super             | 51.5 ms                                                | 47.7 ms: 1.08x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 57.2 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.9 ms: 1.07x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                                 |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                |
| unpickle_list              | 5.29 us                                                | 5.12 us: 1.03x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                 |
| pickle_list                | 5.08 us                                                | 4.99 us: 1.02x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.73 ms: 1.02x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                 |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 831 us: 1.01x faster                                                  |
| dask                       | 372 ms                                                 | 367 ms: 1.01x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                  |
| pickle_dict                | 35.5 us                                                | 35.2 us: 1.01x faster                                                 |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 68.0 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| 2to3                       | 274 ms                                                 | 273 ms: 1.00x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.00x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.66 ms: 1.01x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 56.1 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 22.0 ms: 1.03x slower                                                 |
| nqueens                    | 83.3 ms                                                | 85.5 ms: 1.03x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                 |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                                  |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                  |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.43 ms: 1.07x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.9 ms: 1.14x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.5 ms: 1.29x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (4): sqlite_synth, scimark_sor, bench_mp_pool, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x