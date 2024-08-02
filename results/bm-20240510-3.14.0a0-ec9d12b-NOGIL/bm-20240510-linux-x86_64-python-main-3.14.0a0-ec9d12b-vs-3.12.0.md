# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.45x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 395 ms: 1.44x slower                                  |
| chameleon      | 7.41 ms                                                | 12.8 ms: 1.72x slower                                 |
| docutils       | 2.77 sec                                               | 3.38 sec: 1.22x slower                                |
| tornado_http   | 103 ms                                                 | 136 ms: 1.33x slower                                  |
| Geometric mean | (ref)                                                  | 1.42x slower                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 883 ms: 1.34x faster                                  |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 503 ms: 1.14x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 396 ms: 1.13x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 657 ms: 1.11x faster                                  |
| async_tree_none            | 472 ms                                                 | 453 ms: 1.04x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 559 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 715 ms: 1.02x faster                                  |
| Geometric mean             | (ref)                                                  | 1.13x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                  |
| float          | 84.7 ms                                                | 133 ms: 1.57x slower                                  |
| nbody          | 97.0 ms                                                | 227 ms: 2.34x slower                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                 |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                  |
| regex_v8       | 23.1 ms                                                | 26.5 ms: 1.14x slower                                 |
| regex_compile  | 148 ms                                                 | 217 ms: 1.46x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                  |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                 |
| unpickle_list        | 5.29 us                                                | 5.57 us: 1.05x slower                                 |
| xml_etree_iterparse  | 107 ms                                                 | 113 ms: 1.06x slower                                  |
| pickle               | 11.6 us                                                | 12.4 us: 1.07x slower                                 |
| unpickle             | 15.9 us                                                | 17.0 us: 1.07x slower                                 |
| json_loads           | 28.5 us                                                | 32.7 us: 1.15x slower                                 |
| pickle_dict          | 35.5 us                                                | 42.4 us: 1.19x slower                                 |
| xml_etree_generate   | 89.2 ms                                                | 110 ms: 1.23x slower                                  |
| json_dumps           | 10.4 ms                                                | 13.9 ms: 1.34x slower                                 |
| tomli_loads          | 2.33 sec                                               | 3.30 sec: 1.42x slower                                |
| xml_etree_process    | 61.7 ms                                                | 89.6 ms: 1.45x slower                                 |
| unpickle_pure_python | 230 us                                                 | 398 us: 1.73x slower                                  |
| pickle_pure_python   | 324 us                                                 | 570 us: 1.76x slower                                  |
| Geometric mean       | (ref)                                                  | 1.22x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.16 ms: 1.32x slower                                 |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.40x slower                                 |
| Geometric mean         | (ref)                                                  | 1.36x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 34.6 ms                                                | 60.1 ms: 1.74x slower                                 |
| mako            | 11.9 ms                                                | 20.7 ms: 1.74x slower                                 |
| Geometric mean  | (ref)                                                  | 1.74x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 883 ms: 1.34x faster                                  |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                  |
| gc_traversal               | 3.79 ms                                                | 3.21 ms: 1.18x faster                                 |
| bench_mp_pool              | 24.0 ms                                                | 21.0 ms: 1.15x faster                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 503 ms: 1.14x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 396 ms: 1.13x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 657 ms: 1.11x faster                                  |
| async_tree_none            | 472 ms                                                 | 453 ms: 1.04x faster                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.42 ms: 1.04x faster                                 |
| async_tree_memoization     | 578 ms                                                 | 559 ms: 1.03x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 715 ms: 1.02x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                 |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                  |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                  |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                  |
| pickle_list                | 5.08 us                                                | 5.34 us: 1.05x slower                                 |
| unpickle_list              | 5.29 us                                                | 5.57 us: 1.05x slower                                 |
| xml_etree_iterparse        | 107 ms                                                 | 113 ms: 1.06x slower                                  |
| pickle                     | 11.6 us                                                | 12.4 us: 1.07x slower                                 |
| unpickle                   | 15.9 us                                                | 17.0 us: 1.07x slower                                 |
| pathlib                    | 19.3 ms                                                | 20.9 ms: 1.08x slower                                 |
| sqlite_synth               | 2.83 us                                                | 3.21 us: 1.13x slower                                 |
| regex_v8                   | 23.1 ms                                                | 26.5 ms: 1.14x slower                                 |
| json_loads                 | 28.5 us                                                | 32.7 us: 1.15x slower                                 |
| json                       | 5.26 ms                                                | 6.13 ms: 1.17x slower                                 |
| generators                 | 31.2 ms                                                | 36.6 ms: 1.17x slower                                 |
| pickle_dict                | 35.5 us                                                | 42.4 us: 1.19x slower                                 |
| async_generators           | 463 ms                                                 | 553 ms: 1.20x slower                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.14 sec: 1.20x slower                                |
| asyncio_tcp                | 491 ms                                                 | 590 ms: 1.20x slower                                  |
| scimark_fft                | 382 ms                                                 | 461 ms: 1.21x slower                                  |
| docutils                   | 2.77 sec                                               | 3.38 sec: 1.22x slower                                |
| xml_etree_generate         | 89.2 ms                                                | 110 ms: 1.23x slower                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.24 ms: 1.23x slower                                 |
| comprehensions             | 21.8 us                                                | 27.7 us: 1.27x slower                                 |
| dulwich_log                | 68.5 ms                                                | 87.8 ms: 1.28x slower                                 |
| meteor_contest             | 112 ms                                                 | 145 ms: 1.29x slower                                  |
| mdp                        | 2.63 sec                                               | 3.42 sec: 1.30x slower                                |
| python_startup_no_site     | 6.94 ms                                                | 9.16 ms: 1.32x slower                                 |
| pycparser                  | 1.18 sec                                               | 1.56 sec: 1.32x slower                                |
| tornado_http               | 103 ms                                                 | 136 ms: 1.33x slower                                  |
| json_dumps                 | 10.4 ms                                                | 13.9 ms: 1.34x slower                                 |
| sympy_integrate            | 21.4 ms                                                | 29.0 ms: 1.35x slower                                 |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.40x slower                                 |
| crypto_pyaes               | 81.9 ms                                                | 115 ms: 1.40x slower                                  |
| nqueens                    | 83.3 ms                                                | 118 ms: 1.42x slower                                  |
| tomli_loads                | 2.33 sec                                               | 3.30 sec: 1.42x slower                                |
| sympy_str                  | 300 ms                                                 | 430 ms: 1.43x slower                                  |
| 2to3                       | 274 ms                                                 | 395 ms: 1.44x slower                                  |
| fannkuch                   | 417 ms                                                 | 600 ms: 1.44x slower                                  |
| coroutines                 | 23.2 ms                                                | 33.5 ms: 1.45x slower                                 |
| xml_etree_process          | 61.7 ms                                                | 89.6 ms: 1.45x slower                                 |
| regex_compile              | 148 ms                                                 | 217 ms: 1.46x slower                                  |
| sympy_sum                  | 169 ms                                                 | 258 ms: 1.53x slower                                  |
| pyflate                    | 482 ms                                                 | 749 ms: 1.55x slower                                  |
| deepcopy                   | 371 us                                                 | 578 us: 1.56x slower                                  |
| deepcopy_reduce            | 3.35 us                                                | 5.22 us: 1.56x slower                                 |
| float                      | 84.7 ms                                                | 133 ms: 1.57x slower                                  |
| sqlglot_normalize          | 110 ms                                                 | 174 ms: 1.58x slower                                  |
| sympy_expand               | 478 ms                                                 | 758 ms: 1.59x slower                                  |
| sqlglot_optimize           | 54.8 ms                                                | 87.6 ms: 1.60x slower                                 |
| deepcopy_memo              | 40.7 us                                                | 65.1 us: 1.60x slower                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 122 ms: 1.63x slower                                  |
| logging_simple             | 6.46 us                                                | 10.5 us: 1.63x slower                                 |
| logging_format             | 7.23 us                                                | 11.8 us: 1.63x slower                                 |
| spectral_norm              | 115 ms                                                 | 188 ms: 1.64x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 259 us: 1.64x slower                                  |
| pprint_safe_repr           | 776 ms                                                 | 1.31 sec: 1.69x slower                                |
| richards                   | 45.8 ms                                                | 77.8 ms: 1.70x slower                                 |
| chameleon                  | 7.41 ms                                                | 12.8 ms: 1.72x slower                                 |
| pprint_pformat             | 1.57 sec                                               | 2.70 sec: 1.72x slower                                |
| unpickle_pure_python       | 230 us                                                 | 398 us: 1.73x slower                                  |
| django_template            | 34.6 ms                                                | 60.1 ms: 1.74x slower                                 |
| mako                       | 11.9 ms                                                | 20.7 ms: 1.74x slower                                 |
| pickle_pure_python         | 324 us                                                 | 570 us: 1.76x slower                                  |
| sqlglot_transpile          | 1.68 ms                                                | 2.99 ms: 1.78x slower                                 |
| richards_super             | 51.5 ms                                                | 93.3 ms: 1.81x slower                                 |
| chaos                      | 67.0 ms                                                | 124 ms: 1.85x slower                                  |
| sqlglot_parse              | 1.36 ms                                                | 2.52 ms: 1.85x slower                                 |
| logging_silent             | 104 ns                                                 | 195 ns: 1.87x slower                                  |
| raytrace                   | 312 ms                                                 | 589 ms: 1.89x slower                                  |
| hexiom                     | 6.41 ms                                                | 12.3 ms: 1.92x slower                                 |
| scimark_lu                 | 118 ms                                                 | 238 ms: 2.02x slower                                  |
| scimark_sor                | 129 ms                                                 | 270 ms: 2.09x slower                                  |
| go                         | 139 ms                                                 | 311 ms: 2.23x slower                                  |
| deltablue                  | 3.72 ms                                                | 8.32 ms: 2.24x slower                                 |
| nbody                      | 97.0 ms                                                | 227 ms: 2.34x slower                                  |
| bench_thread_pool          | 842 us                                                 | 3.04 ms: 3.62x slower                                 |
| coverage                   | 72.7 ms                                                | 787 ms: 10.83x slower                                 |
| telco                      | 7.10 ms                                                | 317 ms: 44.61x slower                                 |
| Geometric mean             | (ref)                                                  | 1.45x slower                                          |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240510-3.14.0a0-ec9d12b-NOGIL/bm-20240510-linux-x86_64-python-main-3.14.0a0-ec9d12b.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.12x