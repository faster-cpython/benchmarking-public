# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.32x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 379 ms: 1.38x slower                                                  |
| chameleon      | 7.41 ms                                                | 8.87 ms: 1.20x slower                                                 |
| docutils       | 2.77 sec                                               | 3.57 sec: 1.29x slower                                                |
| tornado_http   | 103 ms                                                 | 107 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.22x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 382 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 624 ms: 1.16x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 998 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 496 ms: 1.16x faster                                                  |
| async_tree_none            | 472 ms                                                 | 409 ms: 1.15x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 1.05 sec: 1.13x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 665 ms: 1.09x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 532 ms: 1.09x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                  |
| float          | 84.7 ms                                                | 131 ms: 1.55x slower                                                  |
| nbody          | 97.0 ms                                                | 198 ms: 2.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.48x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| regex_compile  | 148 ms                                                 | 239 ms: 1.61x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 35.5 us                                                | 33.5 us: 1.06x faster                                                 |
| unpickle             | 15.9 us                                                | 15.5 us: 1.03x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.70 us: 1.08x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.54 us: 1.09x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 128 ms: 1.20x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 80.1 ms: 1.30x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 116 ms: 1.30x slower                                                  |
| tomli_loads          | 2.33 sec                                               | 3.61 sec: 1.55x slower                                                |
| pickle_pure_python   | 324 us                                                 | 556 us: 1.72x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 405 us: 1.76x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 49.6 ms: 1.43x slower                                                 |
| mako            | 11.9 ms                                                | 20.9 ms: 1.75x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.59x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 382 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 624 ms: 1.16x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 998 ms: 1.16x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 496 ms: 1.16x faster                                                  |
| async_tree_none            | 472 ms                                                 | 409 ms: 1.15x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 1.05 sec: 1.13x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 665 ms: 1.09x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 532 ms: 1.09x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.9 ms: 1.08x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.5 us: 1.06x faster                                                 |
| unpickle                   | 15.9 us                                                | 15.5 us: 1.03x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                 |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| generators                 | 31.2 ms                                                | 32.1 ms: 1.03x slower                                                 |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                 |
| logging_format             | 7.23 us                                                | 7.54 us: 1.04x slower                                                 |
| tornado_http               | 103 ms                                                 | 107 ms: 1.05x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.87 sec: 1.05x slower                                                |
| logging_simple             | 6.46 us                                                | 6.78 us: 1.05x slower                                                 |
| coroutines                 | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                 |
| dask                       | 372 ms                                                 | 400 ms: 1.08x slower                                                  |
| async_generators           | 463 ms                                                 | 499 ms: 1.08x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.70 us: 1.08x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 532 ms: 1.08x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.54 us: 1.09x slower                                                 |
| json                       | 5.26 ms                                                | 5.76 ms: 1.09x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 3.13 us: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 77.9 ms: 1.14x slower                                                 |
| mdp                        | 2.63 sec                                               | 3.08 sec: 1.17x slower                                                |
| bench_thread_pool          | 842 us                                                 | 1.01 ms: 1.19x slower                                                 |
| chameleon                  | 7.41 ms                                                | 8.87 ms: 1.20x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 203 ms: 1.20x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 128 ms: 1.20x slower                                                  |
| raytrace                   | 312 ms                                                 | 379 ms: 1.22x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.84 ms: 1.24x slower                                                 |
| sympy_str                  | 300 ms                                                 | 379 ms: 1.26x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.1 ms: 1.28x slower                                                 |
| sympy_expand               | 478 ms                                                 | 614 ms: 1.28x slower                                                  |
| docutils                   | 2.77 sec                                               | 3.57 sec: 1.29x slower                                                |
| xml_etree_process          | 61.7 ms                                                | 80.1 ms: 1.30x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 116 ms: 1.30x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                | 4.41 us: 1.32x slower                                                 |
| meteor_contest             | 112 ms                                                 | 148 ms: 1.32x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 28.5 ms: 1.33x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 213 us: 1.35x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.62 sec: 1.37x slower                                                |
| 2to3                       | 274 ms                                                 | 379 ms: 1.38x slower                                                  |
| scimark_sor                | 129 ms                                                 | 179 ms: 1.39x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 77.5 ms: 1.41x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 156 ms: 1.42x slower                                                  |
| django_template            | 34.6 ms                                                | 49.6 ms: 1.43x slower                                                 |
| deltablue                  | 3.72 ms                                                | 5.36 ms: 1.44x slower                                                 |
| deepcopy                   | 371 us                                                 | 561 us: 1.51x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 3.61 sec: 1.55x slower                                                |
| float                      | 84.7 ms                                                | 131 ms: 1.55x slower                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 2.61 ms: 1.55x slower                                                 |
| scimark_fft                | 382 ms                                                 | 599 ms: 1.57x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 128 ms: 1.57x slower                                                  |
| sqlglot_parse              | 1.36 ms                                                | 2.15 ms: 1.58x slower                                                 |
| go                         | 139 ms                                                 | 222 ms: 1.59x slower                                                  |
| regex_compile              | 148 ms                                                 | 239 ms: 1.61x slower                                                  |
| chaos                      | 67.0 ms                                                | 111 ms: 1.66x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 1.30 sec: 1.67x slower                                                |
| scimark_lu                 | 118 ms                                                 | 200 ms: 1.70x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.69 sec: 1.71x slower                                                |
| pickle_pure_python         | 324 us                                                 | 556 us: 1.72x slower                                                  |
| richards_super             | 51.5 ms                                                | 88.7 ms: 1.72x slower                                                 |
| nqueens                    | 83.3 ms                                                | 144 ms: 1.73x slower                                                  |
| fannkuch                   | 417 ms                                                 | 726 ms: 1.74x slower                                                  |
| comprehensions             | 21.8 us                                                | 38.1 us: 1.75x slower                                                 |
| mako                       | 11.9 ms                                                | 20.9 ms: 1.75x slower                                                 |
| pyflate                    | 482 ms                                                 | 849 ms: 1.76x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 405 us: 1.76x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 8.96 ms: 1.77x slower                                                 |
| richards                   | 45.8 ms                                                | 81.7 ms: 1.78x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 136 ms: 1.81x slower                                                  |
| deepcopy_memo              | 40.7 us                                                | 77.9 us: 1.91x slower                                                 |
| spectral_norm              | 115 ms                                                 | 223 ms: 1.94x slower                                                  |
| nbody                      | 97.0 ms                                                | 198 ms: 2.04x slower                                                  |
| logging_silent             | 104 ns                                                 | 223 ns: 2.13x slower                                                  |
| hexiom                     | 6.41 ms                                                | 15.2 ms: 2.37x slower                                                 |
| telco                      | 7.10 ms                                                | 182 ms: 25.65x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.32x slower                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 0.98x