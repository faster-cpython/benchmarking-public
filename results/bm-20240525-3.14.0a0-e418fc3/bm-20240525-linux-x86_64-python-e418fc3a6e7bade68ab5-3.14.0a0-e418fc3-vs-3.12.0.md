# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| chameleon      | 7.41 ms                                                | 7.01 ms: 1.06x faster                                                 |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                |
| tornado_http   | 103 ms                                                 | 93.9 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 352 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 452 ms: 1.27x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.25x faster                                                  |
| async_tree_none            | 472 ms                                                 | 381 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 967 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.6 ms: 1.15x faster                                                 |
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                 |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| regex_dna      | 212 ms                                                 | 222 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                 |
| unpickle             | 15.9 us                                                | 15.4 us: 1.03x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| pickle_dict          | 35.5 us                                                | 35.7 us: 1.00x slower                                                 |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.35 us: 1.01x slower                                                 |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| django_template | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 352 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 452 ms: 1.27x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.25x faster                                                  |
| async_tree_none            | 472 ms                                                 | 381 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 588 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 967 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                 |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| nbody                      | 97.0 ms                                                | 84.6 ms: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                                 |
| logging_format             | 7.23 us                                                | 6.43 us: 1.12x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.80 us: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                 |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                  |
| tornado_http               | 103 ms                                                 | 93.9 ms: 1.09x faster                                                 |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.09x faster                                                |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                                  |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                  |
| scimark_fft                | 382 ms                                                 | 359 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                  |
| chameleon                  | 7.41 ms                                                | 7.01 ms: 1.06x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 741 ms: 1.05x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 39.0 us: 1.04x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 65.7 ms: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                  |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                  |
| unpickle                   | 15.9 us                                                | 15.4 us: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                 |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                  |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                  |
| deepcopy                   | 371 us                                                 | 364 us: 1.02x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.28 us: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 830 us: 1.01x faster                                                  |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 106 ms: 1.01x faster                                                  |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 55.0 ms: 1.00x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.81 ms: 1.00x slower                                                 |
| pickle_dict                | 35.5 us                                                | 35.7 us: 1.00x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.09 ms: 1.01x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                 |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.35 us: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| django_template            | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 566 ms: 1.03x slower                                                  |
| scimark_sor                | 129 ms                                                 | 133 ms: 1.03x slower                                                  |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 508 ms: 1.04x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.04x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.98 us: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| richards                   | 45.8 ms                                                | 48.6 ms: 1.06x slower                                                 |
| richards_super             | 51.5 ms                                                | 54.8 ms: 1.06x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                 |
| telco                      | 7.10 ms                                                | 8.59 ms: 1.21x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.79 ms: 1.21x slower                                                 |
| coverage                   | 72.7 ms                                                | 91.1 ms: 1.25x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (5): dask, sqlglot_normalize, xml_etree_parse, bench_mp_pool, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x