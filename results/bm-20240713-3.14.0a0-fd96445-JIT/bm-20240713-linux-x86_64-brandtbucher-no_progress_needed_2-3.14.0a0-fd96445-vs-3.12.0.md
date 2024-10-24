# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed_2
- machine: linux-x86_64
- commit hash: fd96445
- commit date: 2024-07-13
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                                        |
| docutils       | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                      |
| tornado_http   | 103 ms                                                 | 93.2 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                        |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 855 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                       |
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                        |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.05x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                       |
| django_template | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.51x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                                        |
| async_tree_none            | 472 ms                                                 | 330 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 412 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 855 ms: 1.38x faster                                                        |
| deepcopy                   | 371 us                                                 | 276 us: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 893 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 60.5 ms: 1.24x faster                                                       |
| mako                       | 11.9 ms                                                | 9.60 ms: 1.24x faster                                                       |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                        |
| nbody                      | 97.0 ms                                                | 79.4 ms: 1.22x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                      |
| richards                   | 45.8 ms                                                | 37.7 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                       |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                       |
| richards_super             | 51.5 ms                                                | 43.9 ms: 1.17x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                       |
| chaos                      | 67.0 ms                                                | 57.3 ms: 1.17x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                        |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.45 ms: 1.14x faster                                                       |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                        |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| tornado_http               | 103 ms                                                 | 93.2 ms: 1.10x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.42 ms: 1.09x faster                                                       |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.1 ms: 1.07x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.05x faster                                                       |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.65 ms: 1.04x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 66.1 ms: 1.04x faster                                                       |
| sympy_str                  | 300 ms                                                 | 291 ms: 1.03x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                      |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                        |
| bench_thread_pool          | 842 us                                                 | 828 us: 1.02x faster                                                        |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                        |
| json                       | 5.26 ms                                                | 5.18 ms: 1.01x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                        |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                       |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 21.9 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                       |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.03x slower                                                       |
| sympy_expand               | 478 ms                                                 | 497 ms: 1.04x slower                                                        |
| docutils                   | 2.77 sec                                               | 2.88 sec: 1.04x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                                       |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.69 ms: 1.04x slower                                                       |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.2 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (2): json_loads, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-fd96445-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_2-3.14.0a0-fd96445.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x