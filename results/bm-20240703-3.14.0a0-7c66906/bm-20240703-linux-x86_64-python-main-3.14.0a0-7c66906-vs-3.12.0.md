# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                  |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                |
| tornado_http   | 103 ms                                                 | 90.2 ms: 1.14x faster                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                  |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.40x faster                                  |
| async_tree_io              | 1.16 sec                                               | 827 ms: 1.40x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                  |
| Geometric mean             | (ref)                                                  | 1.42x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.5 ms: 1.12x faster                                 |
| float          | 84.7 ms                                                | 76.4 ms: 1.11x faster                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                  |
| regex_effbot   | 3.61 ms                                                | 3.79 ms: 1.05x slower                                 |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                  |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                  |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                 |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                  |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                 |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.09x slower                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                 |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                  |
| async_tree_none            | 472 ms                                                 | 321 ms: 1.47x faster                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                  |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.41x faster                                 |
| async_tree_io_tg           | 1.18 sec                                               | 842 ms: 1.40x faster                                  |
| async_tree_io              | 1.16 sec                                               | 827 ms: 1.40x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                  |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                 |
| raytrace                   | 312 ms                                                 | 254 ms: 1.23x faster                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                 |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                 |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                 |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                 |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                  |
| tornado_http               | 103 ms                                                 | 90.2 ms: 1.14x faster                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.4 ms: 1.13x faster                                 |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.7 ms: 1.13x faster                                 |
| nbody                      | 97.0 ms                                                | 86.5 ms: 1.12x faster                                 |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                  |
| float                      | 84.7 ms                                                | 76.4 ms: 1.11x faster                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.58 ms: 1.10x faster                                 |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                 |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                  |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                 |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                 |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                 |
| nqueens                    | 83.3 ms                                                | 78.1 ms: 1.07x faster                                 |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                  |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                 |
| bench_thread_pool          | 842 us                                                 | 791 us: 1.06x faster                                  |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                  |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                  |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.05x faster                                 |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                  |
| pprint_safe_repr           | 776 ms                                                 | 739 ms: 1.05x faster                                  |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                 |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                  |
| dask                       | 372 ms                                                 | 357 ms: 1.04x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.04x faster                                  |
| pyflate                    | 482 ms                                                 | 467 ms: 1.03x faster                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                |
| gc_traversal               | 3.79 ms                                                | 3.68 ms: 1.03x faster                                 |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                  |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                 |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                  |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                  |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                  |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                 |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                  |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                |
| regex_effbot               | 3.61 ms                                                | 3.79 ms: 1.05x slower                                 |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                  |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.09x slower                                 |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                 |
| telco                      | 7.10 ms                                                | 8.22 ms: 1.16x slower                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.17x slower                                 |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.27x slower                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                          |

Benchmark hidden because not significant (3): pycparser, bench_mp_pool, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x