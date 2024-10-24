# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_escape
- machine: linux-x86_64
- commit hash: 3bd6587
- commit date: 2024-07-24
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                             |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                           |
| tornado_http   | 103 ms                                                 | 93.4 ms: 1.10x faster                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                             |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                             |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                             |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                            |
| nbody          | 97.0 ms                                                | 81.3 ms: 1.19x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.13x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                             |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                            |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                            |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                           |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                            |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                             |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                             |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                            |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                     |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                            |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.72 ms: 1.22x faster                                            |
| django_template | 34.6 ms                                                | 36.3 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 301 ms: 1.49x faster                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.1 us: 1.45x faster                                            |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 868 ms: 1.36x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 426 ms: 1.36x faster                                             |
| deepcopy                   | 371 us                                                 | 275 us: 1.35x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 564 ms: 1.29x faster                                             |
| async_tree_io              | 1.16 sec                                               | 899 ms: 1.29x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 59.9 ms: 1.25x faster                                            |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                            |
| mako                       | 11.9 ms                                                | 9.72 ms: 1.22x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                            |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.22 ms: 1.20x faster                                            |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                            |
| nbody                      | 97.0 ms                                                | 81.3 ms: 1.19x faster                                            |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                            |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                            |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                             |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                            |
| fannkuch                   | 417 ms                                                 | 366 ms: 1.14x faster                                             |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                            |
| richards                   | 45.8 ms                                                | 41.5 ms: 1.11x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 704 ms: 1.10x faster                                             |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                            |
| tornado_http               | 103 ms                                                 | 93.4 ms: 1.10x faster                                            |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                            |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                            |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                           |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                           |
| deltablue                  | 3.72 ms                                                | 3.53 ms: 1.05x faster                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                            |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                           |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                            |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.02x faster                                             |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                            |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                            |
| dask                       | 372 ms                                                 | 364 ms: 1.02x faster                                             |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                             |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                             |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                             |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                             |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.79 ms: 1.00x faster                                            |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                           |
| hexiom                     | 6.41 ms                                                | 6.51 ms: 1.02x slower                                            |
| nqueens                    | 83.3 ms                                                | 84.8 ms: 1.02x slower                                            |
| sqlglot_optimize           | 54.8 ms                                                | 56.0 ms: 1.02x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                             |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                            |
| sympy_integrate            | 21.4 ms                                                | 22.2 ms: 1.04x slower                                            |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                            |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                            |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                           |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                             |
| django_template            | 34.6 ms                                                | 36.3 ms: 1.05x slower                                            |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                             |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                             |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                            |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                            |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                            |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                     |

Benchmark hidden because not significant (3): json_dumps, bench_mp_pool, sympy_sum
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240724-3.14.0a0-3bd6587-JIT/bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x