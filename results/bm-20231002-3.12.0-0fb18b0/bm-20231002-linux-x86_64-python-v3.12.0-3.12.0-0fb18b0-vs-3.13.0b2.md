# Results vs. 3.13.0b2

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.03x slower
- HPT reliability: 98.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| chameleon      | 7.22 ms                                                    | 7.41 ms: 1.03x slower                                  |
| docutils       | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                 |
| tornado_http   | 94.6 ms                                                    | 103 ms: 1.08x slower                                   |
| Geometric mean | (ref)                                                      | 1.02x slower                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 611 ms                                                     | 726 ms: 1.19x slower                                   |
| async_tree_io              | 939 ms                                                     | 1.16 sec: 1.23x slower                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 726 ms: 1.24x slower                                   |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                                   |
| async_tree_memoization     | 463 ms                                                     | 578 ms: 1.25x slower                                   |
| async_tree_io_tg           | 936 ms                                                     | 1.18 sec: 1.26x slower                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 575 ms: 1.29x slower                                   |
| async_tree_none_tg         | 336 ms                                                     | 450 ms: 1.34x slower                                   |
| Geometric mean             | (ref)                                                      | 1.25x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                   |
| float          | 78.9 ms                                                    | 84.7 ms: 1.07x slower                                  |
| nbody          | 88.3 ms                                                    | 97.0 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                      | 1.05x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 23.1 ms: 1.09x faster                                  |
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                   |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                  |
| regex_compile  | 137 ms                                                     | 148 ms: 1.08x slower                                   |
| Geometric mean | (ref)                                                      | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                  |
| xml_etree_parse      | 162 ms                                                     | 159 ms: 1.01x faster                                   |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.01x faster                                  |
| unpickle_list        | 5.34 us                                                    | 5.29 us: 1.01x faster                                  |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                  |
| xml_etree_process    | 61.2 ms                                                    | 61.7 ms: 1.01x slower                                  |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                  |
| xml_etree_generate   | 87.4 ms                                                    | 89.2 ms: 1.02x slower                                  |
| pickle_dict          | 34.8 us                                                    | 35.5 us: 1.02x slower                                  |
| unpickle             | 15.1 us                                                    | 15.9 us: 1.05x slower                                  |
| unpickle_pure_python | 218 us                                                     | 230 us: 1.05x slower                                   |
| pickle_pure_python   | 305 us                                                     | 324 us: 1.06x slower                                   |
| tomli_loads          | 2.12 sec                                                   | 2.33 sec: 1.10x slower                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 9.55 ms: 1.13x faster                                  |
| python_startup_no_site | 7.11 ms                                                    | 6.94 ms: 1.02x faster                                  |
| Geometric mean         | (ref)                                                      | 1.07x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                  |
| mako            | 11.2 ms                                                    | 11.9 ms: 1.06x slower                                  |
| Geometric mean  | (ref)                                                      | 1.03x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| coverage                   | 93.1 ms                                                    | 72.7 ms: 1.28x faster                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.48 ms: 1.23x faster                                  |
| telco                      | 8.41 ms                                                    | 7.10 ms: 1.19x faster                                  |
| python_startup             | 10.8 ms                                                    | 9.55 ms: 1.13x faster                                  |
| richards_super             | 57.4 ms                                                    | 51.5 ms: 1.11x faster                                  |
| richards                   | 50.9 ms                                                    | 45.8 ms: 1.11x faster                                  |
| regex_v8                   | 25.1 ms                                                    | 23.1 ms: 1.09x faster                                  |
| mdp                        | 2.79 sec                                                   | 2.63 sec: 1.06x faster                                 |
| sqlite_synth               | 2.99 us                                                    | 2.83 us: 1.06x faster                                  |
| gc_traversal               | 3.98 ms                                                    | 3.79 ms: 1.05x faster                                  |
| typing_runtime_protocols   | 165 us                                                     | 158 us: 1.04x faster                                   |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.06 ms: 1.04x faster                                  |
| go                         | 145 ms                                                     | 139 ms: 1.04x faster                                   |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.04x faster                                   |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                 |
| scimark_lu                 | 122 ms                                                     | 118 ms: 1.03x faster                                   |
| gunicorn                   | 1.28 ms                                                    | 1.24 ms: 1.03x faster                                  |
| asyncio_websockets         | 567 ms                                                     | 551 ms: 1.03x faster                                   |
| scimark_fft                | 392 ms                                                     | 382 ms: 1.03x faster                                   |
| aiohttp                    | 1.18 ms                                                    | 1.15 ms: 1.03x faster                                  |
| python_startup_no_site     | 7.11 ms                                                    | 6.94 ms: 1.02x faster                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                   |
| docutils                   | 2.83 sec                                                   | 2.77 sec: 1.02x faster                                 |
| regex_effbot               | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                  |
| xml_etree_parse            | 162 ms                                                     | 159 ms: 1.01x faster                                   |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.01x faster                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 54.8 ms: 1.01x faster                                  |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                   |
| unpickle_list              | 5.34 us                                                    | 5.29 us: 1.01x faster                                  |
| json                       | 5.31 ms                                                    | 5.26 ms: 1.01x faster                                  |
| django_template            | 34.8 ms                                                    | 34.6 ms: 1.01x faster                                  |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                  |
| pyflate                    | 484 ms                                                     | 482 ms: 1.00x faster                                   |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                 |
| xml_etree_process          | 61.2 ms                                                    | 61.7 ms: 1.01x slower                                  |
| bench_thread_pool          | 834 us                                                     | 842 us: 1.01x slower                                   |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                  |
| deepcopy                   | 367 us                                                     | 371 us: 1.01x slower                                   |
| sympy_expand               | 473 ms                                                     | 478 ms: 1.01x slower                                   |
| scimark_sor                | 127 ms                                                     | 129 ms: 1.01x slower                                   |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                 |
| hexiom                     | 6.30 ms                                                    | 6.41 ms: 1.02x slower                                  |
| xml_etree_generate         | 87.4 ms                                                    | 89.2 ms: 1.02x slower                                  |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                  |
| pickle_dict                | 34.8 us                                                    | 35.5 us: 1.02x slower                                  |
| pprint_safe_repr           | 758 ms                                                     | 776 ms: 1.02x slower                                   |
| nqueens                    | 81.4 ms                                                    | 83.3 ms: 1.02x slower                                  |
| meteor_contest             | 110 ms                                                     | 112 ms: 1.02x slower                                   |
| deepcopy_memo              | 39.7 us                                                    | 40.7 us: 1.03x slower                                  |
| chameleon                  | 7.22 ms                                                    | 7.41 ms: 1.03x slower                                  |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                                  |
| fannkuch                   | 402 ms                                                     | 417 ms: 1.04x slower                                   |
| sympy_integrate            | 20.5 ms                                                    | 21.4 ms: 1.04x slower                                  |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                   |
| unpickle                   | 15.1 us                                                    | 15.9 us: 1.05x slower                                  |
| generators                 | 29.6 ms                                                    | 31.2 ms: 1.05x slower                                  |
| unpickle_pure_python       | 218 us                                                     | 230 us: 1.05x slower                                   |
| crypto_pyaes               | 77.5 ms                                                    | 81.9 ms: 1.06x slower                                  |
| mako                       | 11.2 ms                                                    | 11.9 ms: 1.06x slower                                  |
| pickle_pure_python         | 305 us                                                     | 324 us: 1.06x slower                                   |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                   |
| float                      | 78.9 ms                                                    | 84.7 ms: 1.07x slower                                  |
| tornado_http               | 94.6 ms                                                    | 103 ms: 1.08x slower                                   |
| regex_compile              | 137 ms                                                     | 148 ms: 1.08x slower                                   |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.08x slower                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 75.1 ms: 1.09x slower                                  |
| chaos                      | 61.3 ms                                                    | 67.0 ms: 1.09x slower                                  |
| nbody                      | 88.3 ms                                                    | 97.0 ms: 1.10x slower                                  |
| tomli_loads                | 2.12 sec                                                   | 2.33 sec: 1.10x slower                                 |
| pathlib                    | 17.3 ms                                                    | 19.3 ms: 1.12x slower                                  |
| logging_format             | 6.47 us                                                    | 7.23 us: 1.12x slower                                  |
| mypy2                      | 742 ms                                                     | 830 ms: 1.12x slower                                   |
| logging_simple             | 5.74 us                                                    | 6.46 us: 1.12x slower                                  |
| deltablue                  | 3.25 ms                                                    | 3.72 ms: 1.14x slower                                  |
| raytrace                   | 267 ms                                                     | 312 ms: 1.17x slower                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 726 ms: 1.19x slower                                   |
| async_tree_io              | 939 ms                                                     | 1.16 sec: 1.23x slower                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 726 ms: 1.24x slower                                   |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                                   |
| async_tree_memoization     | 463 ms                                                     | 578 ms: 1.25x slower                                   |
| async_tree_io_tg           | 936 ms                                                     | 1.18 sec: 1.26x slower                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 575 ms: 1.29x slower                                   |
| comprehensions             | 16.6 us                                                    | 21.8 us: 1.31x slower                                  |
| async_tree_none_tg         | 336 ms                                                     | 450 ms: 1.34x slower                                   |
| Geometric mean             | (ref)                                                      | 1.03x slower                                           |

Benchmark hidden because not significant (6): xml_etree_iterparse, deepcopy_reduce, coroutines, sqlglot_normalize, 2to3, dask
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 98.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x