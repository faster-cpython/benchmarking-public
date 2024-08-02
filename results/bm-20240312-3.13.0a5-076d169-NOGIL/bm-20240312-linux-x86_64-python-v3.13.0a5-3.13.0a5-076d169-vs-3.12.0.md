# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.35x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 377 ms: 1.38x slower                                       |
| chameleon      | 7.41 ms                                                | 12.3 ms: 1.66x slower                                      |
| docutils       | 2.77 sec                                               | 3.28 sec: 1.18x slower                                     |
| tornado_http   | 103 ms                                                 | 137 ms: 1.34x slower                                       |
| Geometric mean | (ref)                                                  | 1.38x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 839 ms: 1.41x faster                                       |
| async_tree_io              | 1.16 sec                                               | 877 ms: 1.32x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 369 ms: 1.22x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 472 ms: 1.22x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 623 ms: 1.17x faster                                       |
| async_tree_none            | 472 ms                                                 | 412 ms: 1.15x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 518 ms: 1.12x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 668 ms: 1.09x faster                                       |
| Geometric mean             | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 192 ms: 1.02x slower                                       |
| float          | 84.7 ms                                                | 127 ms: 1.49x slower                                       |
| nbody          | 97.0 ms                                                | 215 ms: 2.21x slower                                       |
| Geometric mean | (ref)                                                  | 1.50x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                      |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| regex_v8       | 23.1 ms                                                | 26.9 ms: 1.16x slower                                      |
| regex_compile  | 148 ms                                                 | 204 ms: 1.38x slower                                       |
| Geometric mean | (ref)                                                  | 1.14x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                       |
| pickle_list          | 5.08 us                                                | 4.97 us: 1.02x faster                                      |
| pickle               | 11.6 us                                                | 12.1 us: 1.04x slower                                      |
| unpickle_list        | 5.29 us                                                | 5.75 us: 1.09x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 117 ms: 1.10x slower                                       |
| unpickle             | 15.9 us                                                | 18.1 us: 1.14x slower                                      |
| pickle_dict          | 35.5 us                                                | 41.4 us: 1.16x slower                                      |
| xml_etree_generate   | 89.2 ms                                                | 108 ms: 1.21x slower                                       |
| json_loads           | 28.5 us                                                | 34.8 us: 1.22x slower                                      |
| json_dumps           | 10.4 ms                                                | 13.7 ms: 1.32x slower                                      |
| tomli_loads          | 2.33 sec                                               | 3.11 sec: 1.33x slower                                     |
| xml_etree_process    | 61.7 ms                                                | 86.4 ms: 1.40x slower                                      |
| unpickle_pure_python | 230 us                                                 | 367 us: 1.59x slower                                       |
| pickle_pure_python   | 324 us                                                 | 528 us: 1.63x slower                                       |
| Geometric mean       | (ref)                                                  | 1.21x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 13.6 ms: 1.43x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 11.6 ms: 1.67x slower                                      |
| Geometric mean         | (ref)                                                  | 1.55x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.6 ms                                                | 57.7 ms: 1.67x slower                                      |
| mako            | 11.9 ms                                                | 21.0 ms: 1.77x slower                                      |
| Geometric mean  | (ref)                                                  | 1.72x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| gc_traversal               | 3.79 ms                                                | 2.57 ms: 1.47x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 839 ms: 1.41x faster                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.08 ms: 1.36x faster                                      |
| async_tree_io              | 1.16 sec                                               | 877 ms: 1.32x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 369 ms: 1.22x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 472 ms: 1.22x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 623 ms: 1.17x faster                                       |
| async_tree_none            | 472 ms                                                 | 412 ms: 1.15x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 518 ms: 1.12x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 668 ms: 1.09x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                       |
| pickle_list                | 5.08 us                                                | 4.97 us: 1.02x faster                                      |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| pidigits                   | 187 ms                                                 | 192 ms: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                       |
| pickle                     | 11.6 us                                                | 12.1 us: 1.04x slower                                      |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                       |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| unpickle_list              | 5.29 us                                                | 5.75 us: 1.09x slower                                      |
| xml_etree_iterparse        | 107 ms                                                 | 117 ms: 1.10x slower                                       |
| async_generators           | 463 ms                                                 | 511 ms: 1.10x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.99 sec: 1.12x slower                                     |
| unpickle                   | 15.9 us                                                | 18.1 us: 1.14x slower                                      |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                      |
| regex_v8                   | 23.1 ms                                                | 26.9 ms: 1.16x slower                                      |
| pickle_dict                | 35.5 us                                                | 41.4 us: 1.16x slower                                      |
| comprehensions             | 21.8 us                                                | 25.7 us: 1.18x slower                                      |
| docutils                   | 2.77 sec                                               | 3.28 sec: 1.18x slower                                     |
| json                       | 5.26 ms                                                | 6.24 ms: 1.19x slower                                      |
| asyncio_tcp                | 491 ms                                                 | 584 ms: 1.19x slower                                       |
| meteor_contest             | 112 ms                                                 | 136 ms: 1.21x slower                                       |
| xml_etree_generate         | 89.2 ms                                                | 108 ms: 1.21x slower                                       |
| json_loads                 | 28.5 us                                                | 34.8 us: 1.22x slower                                      |
| mdp                        | 2.63 sec                                               | 3.30 sec: 1.25x slower                                     |
| scimark_fft                | 382 ms                                                 | 481 ms: 1.26x slower                                       |
| coroutines                 | 23.2 ms                                                | 29.3 ms: 1.26x slower                                      |
| mypy2                      | 830 ms                                                 | 1.07 sec: 1.29x slower                                     |
| dulwich_log                | 68.5 ms                                                | 89.2 ms: 1.30x slower                                      |
| json_dumps                 | 10.4 ms                                                | 13.7 ms: 1.32x slower                                      |
| crypto_pyaes               | 81.9 ms                                                | 108 ms: 1.32x slower                                       |
| sympy_integrate            | 21.4 ms                                                | 28.4 ms: 1.33x slower                                      |
| tomli_loads                | 2.33 sec                                               | 3.11 sec: 1.33x slower                                     |
| pycparser                  | 1.18 sec                                               | 1.57 sec: 1.34x slower                                     |
| pathlib                    | 19.3 ms                                                | 25.9 ms: 1.34x slower                                      |
| tornado_http               | 103 ms                                                 | 137 ms: 1.34x slower                                       |
| nqueens                    | 83.3 ms                                                | 111 ms: 1.34x slower                                       |
| fannkuch                   | 417 ms                                                 | 559 ms: 1.34x slower                                       |
| sqlite_synth               | 2.83 us                                                | 3.84 us: 1.36x slower                                      |
| 2to3                       | 274 ms                                                 | 377 ms: 1.38x slower                                       |
| regex_compile              | 148 ms                                                 | 204 ms: 1.38x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.71 ms: 1.38x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.59 ms: 1.39x slower                                      |
| xml_etree_process          | 61.7 ms                                                | 86.4 ms: 1.40x slower                                      |
| sympy_str                  | 300 ms                                                 | 421 ms: 1.41x slower                                       |
| deepcopy_reduce            | 3.35 us                                                | 4.74 us: 1.42x slower                                      |
| deepcopy                   | 371 us                                                 | 527 us: 1.42x slower                                       |
| python_startup             | 9.55 ms                                                | 13.6 ms: 1.43x slower                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 7.26 ms: 1.44x slower                                      |
| richards                   | 45.8 ms                                                | 68.0 ms: 1.48x slower                                      |
| deepcopy_memo              | 40.7 us                                                | 60.8 us: 1.49x slower                                      |
| float                      | 84.7 ms                                                | 127 ms: 1.49x slower                                       |
| sympy_sum                  | 169 ms                                                 | 254 ms: 1.50x slower                                       |
| pyflate                    | 482 ms                                                 | 728 ms: 1.51x slower                                       |
| pprint_safe_repr           | 776 ms                                                 | 1.20 sec: 1.55x slower                                     |
| sympy_expand               | 478 ms                                                 | 740 ms: 1.55x slower                                       |
| logging_format             | 7.23 us                                                | 11.2 us: 1.55x slower                                      |
| logging_simple             | 6.46 us                                                | 10.2 us: 1.57x slower                                      |
| spectral_norm              | 115 ms                                                 | 181 ms: 1.57x slower                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 119 ms: 1.59x slower                                       |
| pprint_pformat             | 1.57 sec                                               | 2.49 sec: 1.59x slower                                     |
| unpickle_pure_python       | 230 us                                                 | 367 us: 1.59x slower                                       |
| richards_super             | 51.5 ms                                                | 82.3 ms: 1.60x slower                                      |
| sqlglot_normalize          | 110 ms                                                 | 177 ms: 1.61x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 88.8 ms: 1.62x slower                                      |
| pickle_pure_python         | 324 us                                                 | 528 us: 1.63x slower                                       |
| telco                      | 7.10 ms                                                | 11.7 ms: 1.65x slower                                      |
| chameleon                  | 7.41 ms                                                | 12.3 ms: 1.66x slower                                      |
| raytrace                   | 312 ms                                                 | 518 ms: 1.66x slower                                       |
| django_template            | 34.6 ms                                                | 57.7 ms: 1.67x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 11.6 ms: 1.67x slower                                      |
| logging_silent             | 104 ns                                                 | 176 ns: 1.68x slower                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.84 ms: 1.69x slower                                      |
| hexiom                     | 6.41 ms                                                | 11.0 ms: 1.72x slower                                      |
| chaos                      | 67.0 ms                                                | 115 ms: 1.72x slower                                       |
| sqlglot_parse              | 1.36 ms                                                | 2.37 ms: 1.74x slower                                      |
| mako                       | 11.9 ms                                                | 21.0 ms: 1.77x slower                                      |
| scimark_sor                | 129 ms                                                 | 241 ms: 1.87x slower                                       |
| go                         | 139 ms                                                 | 273 ms: 1.96x slower                                       |
| deltablue                  | 3.72 ms                                                | 7.43 ms: 2.00x slower                                      |
| scimark_lu                 | 118 ms                                                 | 250 ms: 2.12x slower                                       |
| nbody                      | 97.0 ms                                                | 215 ms: 2.21x slower                                       |
| bench_thread_pool          | 842 us                                                 | 3.01 ms: 3.58x slower                                      |
| coverage                   | 72.7 ms                                                | 891 ms: 12.25x slower                                      |
| Geometric mean             | (ref)                                                  | 1.35x slower                                               |
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240312-3.13.0a5-076d169-NOGIL/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.26x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 1.07x