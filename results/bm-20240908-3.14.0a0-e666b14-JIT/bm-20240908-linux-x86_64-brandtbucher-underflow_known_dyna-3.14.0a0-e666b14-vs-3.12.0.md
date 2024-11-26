# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: e666b14
- commit date: 2024-09-08
- overall geometric mean: 1.064x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 288 ms: 1.05x slower                                                        |
| docutils       | 2.77 sec                                               | 3.23 sec: 1.17x slower                                                      |
| tornado_http   | 103 ms                                                 | 104 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 412 ms: 1.39x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                       |
| float          | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.00x faster                                                       |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                        |
| regex_compile  | 148 ms                                                 | 154 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 89.2 ms                                                | 77.2 ms: 1.15x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 53.9 ms: 1.15x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                        |
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                       |
| unpickle             | 15.9 us                                                | 14.9 us: 1.07x faster                                                       |
| pickle_dict          | 35.5 us                                                | 34.7 us: 1.02x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| unpickle_list        | 5.29 us                                                | 5.24 us: 1.01x faster                                                       |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                       |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                        |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 37.8 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 25.2 us: 1.61x faster                                                       |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 317 ms: 1.42x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 412 ms: 1.39x faster                                                        |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 416 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 910 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 66.5 ms: 1.23x faster                                                       |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                        |
| mako                       | 11.9 ms                                                | 9.75 ms: 1.22x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 80.7 ms: 1.20x faster                                                       |
| float                      | 84.7 ms                                                | 71.4 ms: 1.19x faster                                                       |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.16x faster                                                       |
| richards_super             | 51.5 ms                                                | 44.3 ms: 1.16x faster                                                       |
| richards                   | 45.8 ms                                                | 39.4 ms: 1.16x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.2 ms: 1.15x faster                                                       |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.41 ms: 1.15x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 53.9 ms: 1.15x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                        |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                      |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                                        |
| raytrace                   | 312 ms                                                 | 284 ms: 1.10x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.89 us: 1.10x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                       |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.07x faster                                                       |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 71.4 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                       |
| go                         | 139 ms                                                 | 135 ms: 1.03x faster                                                        |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                        |
| pickle_dict                | 35.5 us                                                | 34.7 us: 1.02x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| unpickle_list              | 5.29 us                                                | 5.24 us: 1.01x faster                                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.00x faster                                                       |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| nqueens                    | 83.3 ms                                                | 84.0 ms: 1.01x slower                                                       |
| tornado_http               | 103 ms                                                 | 104 ms: 1.01x slower                                                        |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                       |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                        |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| regex_compile              | 148 ms                                                 | 154 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.75 ms: 1.04x slower                                                       |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                                       |
| logging_silent             | 104 ns                                                 | 109 ns: 1.05x slower                                                        |
| 2to3                       | 274 ms                                                 | 288 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                        |
| generators                 | 31.2 ms                                                | 33.2 ms: 1.06x slower                                                       |
| sympy_str                  | 300 ms                                                 | 322 ms: 1.07x slower                                                        |
| django_template            | 34.6 ms                                                | 37.8 ms: 1.09x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.10x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.49 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 121 ms: 1.10x slower                                                        |
| dulwich_log                | 68.5 ms                                                | 75.4 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| sympy_expand               | 478 ms                                                 | 533 ms: 1.12x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.32 sec: 1.12x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 61.6 ms: 1.12x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 190 ms: 1.13x slower                                                        |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                       |
| hexiom                     | 6.41 ms                                                | 7.42 ms: 1.16x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 24.9 ms: 1.16x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.23 sec: 1.17x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                       |
| unpack_sequence            | 54.0 ns                                                | 145 ns: 2.68x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, pidigits
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240908-3.14.0a0-e666b14-JIT/bm-20240908-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-e666b14.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.064x faster
# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x