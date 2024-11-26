# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.086x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                         |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                       |
| tornado_http   | 103 ms                                                 | 89.8 ms: 1.14x faster                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.48x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                         |
| async_tree_io              | 1.16 sec                                               | 879 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                         |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.1 ms: 1.11x faster                                        |
| float          | 84.7 ms                                                | 76.3 ms: 1.11x faster                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.11x faster                                       |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.08x faster                                         |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.7 ms: 1.05x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                        |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                        |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                         |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                        |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                        |
| unpickle_list        | 5.29 us                                                | 5.34 us: 1.01x slower                                        |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                        |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| django_template | 34.6 ms                                                | 34.1 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 389 ms: 1.48x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.47x faster                                         |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 869 ms: 1.36x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 552 ms: 1.32x faster                                         |
| async_tree_io              | 1.16 sec                                               | 879 ms: 1.31x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                         |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                        |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                        |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                         |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                        |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                        |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                         |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                         |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                        |
| tornado_http               | 103 ms                                                 | 89.8 ms: 1.14x faster                                        |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                        |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 73.2 ms: 1.12x faster                                        |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                        |
| nbody                      | 97.0 ms                                                | 87.1 ms: 1.11x faster                                        |
| float                      | 84.7 ms                                                | 76.3 ms: 1.11x faster                                        |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.11x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                        |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                       |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.08x faster                                         |
| unpack_sequence            | 54.0 ns                                                | 50.3 ns: 1.07x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                        |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                        |
| dulwich_log                | 68.5 ms                                                | 64.7 ms: 1.06x faster                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                         |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.7 ms: 1.05x faster                                        |
| asyncio_tcp                | 491 ms                                                 | 468 ms: 1.05x faster                                         |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                         |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                        |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                        |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                        |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                       |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                       |
| bench_thread_pool          | 842 us                                                 | 809 us: 1.04x faster                                         |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                         |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                         |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                        |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                         |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.03x faster                                        |
| hexiom                     | 6.41 ms                                                | 6.26 ms: 1.02x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                         |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                        |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                         |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.01x faster                                        |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                         |
| pickle_list                | 5.08 us                                                | 5.12 us: 1.01x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                        |
| unpickle_list              | 5.29 us                                                | 5.34 us: 1.01x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                         |
| richards                   | 45.8 ms                                                | 46.4 ms: 1.01x slower                                        |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                        |
| gc_traversal               | 3.79 ms                                                | 3.88 ms: 1.02x slower                                        |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                        |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                        |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                         |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                       |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                         |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                        |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                        |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                        |
| telco                      | 7.10 ms                                                | 8.40 ms: 1.18x slower                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                 |

Benchmark hidden because not significant (4): pickle, bench_mp_pool, coroutines, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-linux-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.086x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x