# Results vs. 3.12.0

- fork: brandtbucher
- ref: deopt_tracing
- machine: linux-x86_64
- commit hash: 282ab23
- commit date: 2024-09-12
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                                 |
| docutils       | 2.77 sec                                               | 2.94 sec: 1.06x slower                                               |
| tornado_http   | 103 ms                                                 | 94.7 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                |
| nbody          | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 77.2 ms: 1.15x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                                |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                 |
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                                |
| json_loads           | 28.5 us                                                | 27.3 us: 1.04x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.19 us: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.8 us: 1.52x faster                                                |
| async_tree_none            | 472 ms                                                 | 314 ms: 1.50x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.47x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 861 ms: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 845 ms: 1.37x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 553 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                |
| mako                       | 11.9 ms                                                | 9.84 ms: 1.21x faster                                                |
| nbody                      | 97.0 ms                                                | 80.2 ms: 1.21x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 62.3 ms: 1.21x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 77.2 ms: 1.15x faster                                                |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                                |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 54.2 ms: 1.14x faster                                                |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                                |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                 |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.12x faster                                                 |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                 |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                 |
| tornado_http               | 103 ms                                                 | 94.7 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                 |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                 |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                 |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                 |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                                |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.04x faster                                                |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                               |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                |
| unpickle_list              | 5.29 us                                                | 5.19 us: 1.02x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                                 |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                 |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                                 |
| nqueens                    | 83.3 ms                                                | 83.5 ms: 1.00x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 3.83 ms: 1.01x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 496 ms: 1.01x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.14 us: 1.01x slower                                                |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 57.8 ms: 1.06x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                                |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                 |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                |
| docutils                   | 2.77 sec                                               | 2.94 sec: 1.06x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.87 ms: 1.07x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.10x slower                                                |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.00x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (3): pprint_pformat, bench_mp_pool, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-282ab23-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.091x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x