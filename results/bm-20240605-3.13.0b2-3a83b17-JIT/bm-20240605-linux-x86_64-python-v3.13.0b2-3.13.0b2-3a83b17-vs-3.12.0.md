# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.04x faster
- HPT reliability: 97.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                       |
| chameleon      | 7.41 ms                                                | 7.11 ms: 1.04x faster                                      |
| docutils       | 2.77 sec                                               | 2.99 sec: 1.08x slower                                     |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 945 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                       |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                       |
| Geometric mean             | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.5 ms: 1.16x faster                                      |
| float          | 84.7 ms                                                | 73.0 ms: 1.16x faster                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.07x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                      |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                     |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 82.9 ms: 1.08x faster                                      |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                      |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.05x faster                                       |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                       |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                      |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.00x faster                                      |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                      |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.62 ms: 1.10x slower                                      |
| python_startup         | 9.55 ms                                                | 11.3 ms: 1.18x slower                                      |
| Geometric mean         | (ref)                                                  | 1.14x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.83 ms: 1.21x faster                                      |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                      |
| Geometric mean  | (ref)                                                  | 1.07x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 333 ms: 1.35x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 441 ms: 1.30x faster                                       |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                      |
| async_tree_memoization     | 578 ms                                                 | 456 ms: 1.27x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 945 ms: 1.25x faster                                       |
| async_tree_none            | 472 ms                                                 | 377 ms: 1.25x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 584 ms: 1.24x faster                                       |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                       |
| mako                       | 11.9 ms                                                | 9.83 ms: 1.21x faster                                      |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 68.0 ms: 1.20x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                      |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                       |
| fannkuch                   | 417 ms                                                 | 358 ms: 1.17x faster                                       |
| nbody                      | 97.0 ms                                                | 83.5 ms: 1.16x faster                                      |
| float                      | 84.7 ms                                                | 73.0 ms: 1.16x faster                                      |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                      |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                      |
| logging_simple             | 6.46 us                                                | 5.70 us: 1.13x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                      |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                       |
| raytrace                   | 312 ms                                                 | 280 ms: 1.12x faster                                       |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                      |
| pyflate                    | 482 ms                                                 | 436 ms: 1.11x faster                                       |
| richards                   | 45.8 ms                                                | 41.7 ms: 1.10x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 37.3 us: 1.09x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.09x faster                                       |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                     |
| xml_etree_generate         | 89.2 ms                                                | 82.9 ms: 1.08x faster                                      |
| regex_compile              | 148 ms                                                 | 138 ms: 1.07x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                       |
| richards_super             | 51.5 ms                                                | 48.4 ms: 1.07x faster                                      |
| tornado_http               | 103 ms                                                 | 96.9 ms: 1.06x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                      |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.05x faster                                       |
| chameleon                  | 7.41 ms                                                | 7.11 ms: 1.04x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                      |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.03x faster                                      |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                      |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                     |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.00x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                      |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.00x faster                                     |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                       |
| deepcopy                   | 371 us                                                 | 375 us: 1.01x slower                                       |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                      |
| dask                       | 372 ms                                                 | 377 ms: 1.01x slower                                       |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                       |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                      |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                      |
| dulwich_log                | 68.5 ms                                                | 69.7 ms: 1.02x slower                                      |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                      |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                      |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                      |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                       |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                       |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 56.8 ms: 1.04x slower                                      |
| nqueens                    | 83.3 ms                                                | 86.5 ms: 1.04x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                     |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                      |
| django_template            | 34.6 ms                                                | 36.4 ms: 1.05x slower                                      |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                      |
| asyncio_tcp                | 491 ms                                                 | 522 ms: 1.06x slower                                       |
| sympy_expand               | 478 ms                                                 | 510 ms: 1.07x slower                                       |
| generators                 | 31.2 ms                                                | 33.5 ms: 1.07x slower                                      |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                       |
| docutils                   | 2.77 sec                                               | 2.99 sec: 1.08x slower                                     |
| go                         | 139 ms                                                 | 151 ms: 1.08x slower                                       |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.34 ms: 1.08x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.25 ms: 1.09x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.09x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.62 ms: 1.10x slower                                      |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                      |
| python_startup             | 9.55 ms                                                | 11.3 ms: 1.18x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.83 ms: 1.24x slower                                      |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.28x slower                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (5): mypy2, unpickle_list, deltablue, async_generators, pickle_list
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x