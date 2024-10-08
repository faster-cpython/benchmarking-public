# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.03x faster
- HPT reliability: 98.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| chameleon      | 7.41 ms                                                | 7.22 ms: 1.03x faster                                      |
| docutils       | 2.77 sec                                               | 2.83 sec: 1.02x slower                                     |
| tornado_http   | 103 ms                                                 | 94.6 ms: 1.08x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 936 ms: 1.26x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                       |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 611 ms: 1.19x faster                                       |
| Geometric mean             | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.3 ms: 1.10x faster                                      |
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                      |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                     |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                       |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                       |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.4 ms: 1.02x faster                                      |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 61.2 ms: 1.01x faster                                      |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.00x slower                                      |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                      |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                      |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                       |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                      |
| python_startup         | 9.55 ms                                                | 10.8 ms: 1.13x slower                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |
| django_template | 34.6 ms                                                | 34.8 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 336 ms: 1.34x faster                                       |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 444 ms: 1.29x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 936 ms: 1.26x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 463 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 378 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 587 ms: 1.24x faster                                       |
| async_tree_io              | 1.16 sec                                               | 939 ms: 1.23x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 611 ms: 1.19x faster                                       |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                      |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.12x faster                                      |
| mypy2                      | 830 ms                                                 | 742 ms: 1.12x faster                                       |
| logging_format             | 7.23 us                                                | 6.47 us: 1.12x faster                                      |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                     |
| nbody                      | 97.0 ms                                                | 88.3 ms: 1.10x faster                                      |
| chaos                      | 67.0 ms                                                | 61.3 ms: 1.09x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 69.2 ms: 1.09x faster                                      |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                       |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                       |
| tornado_http               | 103 ms                                                 | 94.6 ms: 1.08x faster                                      |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                      |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                       |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                       |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 77.5 ms: 1.06x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                       |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                      |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| async_generators           | 463 ms                                                 | 442 ms: 1.05x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                      |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                      |
| chameleon                  | 7.41 ms                                                | 7.22 ms: 1.03x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 39.7 us: 1.03x faster                                      |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                       |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 758 ms: 1.02x faster                                       |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                      |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.4 ms: 1.02x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                     |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                       |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                       |
| deepcopy                   | 371 us                                                 | 367 us: 1.01x faster                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| bench_thread_pool          | 842 us                                                 | 834 us: 1.01x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 61.2 ms: 1.01x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                       |
| pyflate                    | 482 ms                                                 | 484 ms: 1.00x slower                                       |
| pickle_list                | 5.08 us                                                | 5.11 us: 1.00x slower                                      |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.01x slower                                      |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                      |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                      |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                      |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                      |
| docutils                   | 2.77 sec                                               | 2.83 sec: 1.02x slower                                     |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.18 ms: 1.03x slower                                      |
| scimark_fft                | 382 ms                                                 | 392 ms: 1.03x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                      |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                      |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                       |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.27 ms: 1.04x slower                                      |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                       |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                       |
| gc_traversal               | 3.79 ms                                                | 3.98 ms: 1.05x slower                                      |
| sqlite_synth               | 2.83 us                                                | 2.99 us: 1.06x slower                                      |
| mdp                        | 2.63 sec                                               | 2.79 sec: 1.06x slower                                     |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                      |
| richards                   | 45.8 ms                                                | 50.9 ms: 1.11x slower                                      |
| richards_super             | 51.5 ms                                                | 57.4 ms: 1.11x slower                                      |
| python_startup             | 9.55 ms                                                | 10.8 ms: 1.13x slower                                      |
| telco                      | 7.10 ms                                                | 8.41 ms: 1.19x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                      |
| coverage                   | 72.7 ms                                                | 93.1 ms: 1.28x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (6): dask, 2to3, sqlglot_normalize, coroutines, deepcopy_reduce, xml_etree_iterparse
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x