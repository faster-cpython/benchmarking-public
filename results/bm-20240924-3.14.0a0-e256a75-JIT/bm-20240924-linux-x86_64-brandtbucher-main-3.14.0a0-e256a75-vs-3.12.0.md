# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 275 ms: 1.00x slower                                        |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                      |
| tornado_http   | 103 ms                                                 | 94.5 ms: 1.09x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 873 ms: 1.36x faster                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                        |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                        |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.2 ms: 1.22x faster                                       |
| nbody          | 97.0 ms                                                | 79.3 ms: 1.22x faster                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.05x faster                                        |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                       |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                        |
| regex_effbot   | 3.61 ms                                                | 3.83 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 77.2 ms: 1.15x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                        |
| unpickle             | 15.9 us                                                | 14.5 us: 1.09x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                       |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                        |
| json_loads           | 28.5 us                                                | 27.0 us: 1.05x faster                                       |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                        |
| pickle_dict          | 35.5 us                                                | 34.3 us: 1.04x faster                                       |
| unpickle_list        | 5.29 us                                                | 5.18 us: 1.02x faster                                       |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                       |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                       |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.01x slower                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.80 ms: 1.21x faster                                       |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.7 us: 1.53x faster                                       |
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                        |
| async_tree_none_tg         | 450 ms                                                 | 310 ms: 1.45x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 401 ms: 1.44x faster                                        |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 873 ms: 1.36x faster                                        |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 555 ms: 1.31x faster                                        |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                       |
| float                      | 84.7 ms                                                | 69.2 ms: 1.22x faster                                       |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                       |
| nbody                      | 97.0 ms                                                | 79.3 ms: 1.22x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.16 ms: 1.22x faster                                       |
| mako                       | 11.9 ms                                                | 9.80 ms: 1.21x faster                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 61.9 ms: 1.21x faster                                       |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                      |
| richards                   | 45.8 ms                                                | 39.4 ms: 1.16x faster                                       |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 77.2 ms: 1.15x faster                                       |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                      |
| richards_super             | 51.5 ms                                                | 45.2 ms: 1.14x faster                                       |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                       |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                       |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                       |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                        |
| unpickle                   | 15.9 us                                                | 14.5 us: 1.09x faster                                       |
| tornado_http               | 103 ms                                                 | 94.5 ms: 1.09x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                       |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                        |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                        |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                        |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.05x faster                                       |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                        |
| regex_compile              | 148 ms                                                 | 142 ms: 1.05x faster                                        |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                        |
| pickle_dict                | 35.5 us                                                | 34.3 us: 1.04x faster                                       |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                       |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                      |
| async_generators           | 463 ms                                                 | 450 ms: 1.03x faster                                        |
| gc_traversal               | 3.79 ms                                                | 3.70 ms: 1.03x faster                                       |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                      |
| unpickle_list              | 5.29 us                                                | 5.18 us: 1.02x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                       |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                       |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                       |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                        |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                        |
| bench_thread_pool          | 842 us                                                 | 835 us: 1.01x faster                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                       |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.00x faster                                        |
| 2to3                       | 274 ms                                                 | 275 ms: 1.00x slower                                        |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.01x slower                                        |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                      |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                       |
| pickle_list                | 5.08 us                                                | 5.16 us: 1.01x slower                                       |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                       |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                        |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                        |
| nqueens                    | 83.3 ms                                                | 86.4 ms: 1.04x slower                                       |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                       |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                        |
| generators                 | 31.2 ms                                                | 32.8 ms: 1.05x slower                                       |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                       |
| sqlglot_optimize           | 54.8 ms                                                | 58.0 ms: 1.06x slower                                       |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                        |
| regex_effbot               | 3.61 ms                                                | 3.83 ms: 1.06x slower                                       |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                       |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                      |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                       |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.74 ms: 1.18x slower                                       |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                       |
| unpack_sequence            | 54.0 ns                                                | 107 ns: 1.98x slower                                        |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.092x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x