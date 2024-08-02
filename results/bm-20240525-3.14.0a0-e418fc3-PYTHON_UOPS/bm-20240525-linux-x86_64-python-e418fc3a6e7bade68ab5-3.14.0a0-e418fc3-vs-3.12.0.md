# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.27x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 375 ms: 1.37x slower                                                  |
| chameleon      | 7.41 ms                                                | 8.91 ms: 1.20x slower                                                 |
| docutils       | 2.77 sec                                               | 3.51 sec: 1.27x slower                                                |
| tornado_http   | 103 ms                                                 | 107 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 366 ms: 1.23x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 477 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 620 ms: 1.17x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 1.03 sec: 1.12x faster                                                |
| async_tree_none            | 472 ms                                                 | 428 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 665 ms: 1.09x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 531 ms: 1.09x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 194 ms: 1.03x slower                                                  |
| float          | 84.7 ms                                                | 130 ms: 1.53x slower                                                  |
| nbody          | 97.0 ms                                                | 193 ms: 1.99x slower                                                  |
| Geometric mean | (ref)                                                  | 1.47x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                 |
| regex_dna      | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.9 ms: 1.16x slower                                                 |
| regex_compile  | 148 ms                                                 | 236 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle             | 15.9 us                                                | 15.2 us: 1.05x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| unpickle_list        | 5.29 us                                                | 5.17 us: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| pickle               | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 125 ms: 1.18x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 78.3 ms: 1.27x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 114 ms: 1.27x slower                                                  |
| tomli_loads          | 2.33 sec                                               | 3.49 sec: 1.50x slower                                                |
| unpickle_pure_python | 230 us                                                 | 396 us: 1.72x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 560 us: 1.73x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x slower                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 49.6 ms: 1.43x slower                                                 |
| mako            | 11.9 ms                                                | 19.9 ms: 1.67x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.55x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 366 ms: 1.23x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 477 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 1.00 sec: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 620 ms: 1.17x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 1.03 sec: 1.12x faster                                                |
| async_tree_none            | 472 ms                                                 | 428 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 665 ms: 1.09x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 531 ms: 1.09x faster                                                  |
| pathlib                    | 19.3 ms                                                | 18.0 ms: 1.08x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.05x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                  |
| unpickle_list              | 5.29 us                                                | 5.17 us: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                 |
| generators                 | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| logging_format             | 7.23 us                                                | 7.42 us: 1.03x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.89 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| logging_simple             | 6.46 us                                                | 6.65 us: 1.03x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.23 us: 1.03x slower                                                 |
| pidigits                   | 187 ms                                                 | 194 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.03x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| tornado_http               | 103 ms                                                 | 107 ms: 1.05x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.87 sec: 1.05x slower                                                |
| pickle                     | 11.6 us                                                | 12.2 us: 1.05x slower                                                 |
| dask                       | 372 ms                                                 | 394 ms: 1.06x slower                                                  |
| json                       | 5.26 ms                                                | 5.62 ms: 1.07x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 525 ms: 1.07x slower                                                  |
| async_generators           | 463 ms                                                 | 496 ms: 1.07x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.87 ms: 1.07x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.13 us: 1.11x slower                                                 |
| regex_dna                  | 212 ms                                                 | 235 ms: 1.11x slower                                                  |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 77.3 ms: 1.13x slower                                                 |
| mdp                        | 2.63 sec                                               | 3.05 sec: 1.16x slower                                                |
| regex_v8                   | 23.1 ms                                                | 26.9 ms: 1.16x slower                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 125 ms: 1.18x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 199 ms: 1.18x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 996 us: 1.18x slower                                                  |
| chameleon                  | 7.41 ms                                                | 8.91 ms: 1.20x slower                                                 |
| raytrace                   | 312 ms                                                 | 384 ms: 1.23x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.25x slower                                                 |
| sympy_str                  | 300 ms                                                 | 378 ms: 1.26x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 78.3 ms: 1.27x slower                                                 |
| docutils                   | 2.77 sec                                               | 3.51 sec: 1.27x slower                                                |
| xml_etree_generate         | 89.2 ms                                                | 114 ms: 1.27x slower                                                  |
| sympy_expand               | 478 ms                                                 | 615 ms: 1.29x slower                                                  |
| meteor_contest             | 112 ms                                                 | 145 ms: 1.29x slower                                                  |
| coverage                   | 72.7 ms                                                | 94.1 ms: 1.29x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                | 4.38 us: 1.31x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 28.2 ms: 1.32x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 150 ms: 1.36x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.61 sec: 1.36x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 216 us: 1.37x slower                                                  |
| 2to3                       | 274 ms                                                 | 375 ms: 1.37x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 75.6 ms: 1.38x slower                                                 |
| scimark_sor                | 129 ms                                                 | 179 ms: 1.38x slower                                                  |
| django_template            | 34.6 ms                                                | 49.6 ms: 1.43x slower                                                 |
| deltablue                  | 3.72 ms                                                | 5.33 ms: 1.43x slower                                                 |
| deepcopy                   | 371 us                                                 | 554 us: 1.49x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 3.49 sec: 1.50x slower                                                |
| telco                      | 7.10 ms                                                | 10.6 ms: 1.50x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 2.57 ms: 1.53x slower                                                 |
| float                      | 84.7 ms                                                | 130 ms: 1.53x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 128 ms: 1.56x slower                                                  |
| scimark_fft                | 382 ms                                                 | 598 ms: 1.57x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 2.14 ms: 1.57x slower                                                 |
| regex_compile              | 148 ms                                                 | 236 ms: 1.59x slower                                                  |
| go                         | 139 ms                                                 | 222 ms: 1.59x slower                                                  |
| chaos                      | 67.0 ms                                                | 109 ms: 1.63x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 1.27 sec: 1.63x slower                                                |
| scimark_lu                 | 118 ms                                                 | 196 ms: 1.66x slower                                                  |
| mako                       | 11.9 ms                                                | 19.9 ms: 1.67x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.63 sec: 1.68x slower                                                |
| fannkuch                   | 417 ms                                                 | 701 ms: 1.68x slower                                                  |
| richards_super             | 51.5 ms                                                | 88.1 ms: 1.71x slower                                                 |
| pyflate                    | 482 ms                                                 | 826 ms: 1.71x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 396 us: 1.72x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 8.72 ms: 1.72x slower                                                 |
| comprehensions             | 21.8 us                                                | 37.6 us: 1.73x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 560 us: 1.73x slower                                                  |
| nqueens                    | 83.3 ms                                                | 145 ms: 1.75x slower                                                  |
| richards                   | 45.8 ms                                                | 81.0 ms: 1.77x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 135 ms: 1.80x slower                                                  |
| spectral_norm              | 115 ms                                                 | 216 ms: 1.88x slower                                                  |
| deepcopy_memo              | 40.7 us                                                | 77.8 us: 1.91x slower                                                 |
| nbody                      | 97.0 ms                                                | 193 ms: 1.99x slower                                                  |
| logging_silent             | 104 ns                                                 | 222 ns: 2.13x slower                                                  |
| hexiom                     | 6.41 ms                                                | 15.0 ms: 2.33x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.27x slower                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_dict
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 0.98x