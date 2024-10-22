# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_progress_needed_8
- machine: linux-x86_64
- commit hash: 95535e9
- commit date: 2024-07-13
- overall geometric mean: 1.09x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| docutils       | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                      |
| tornado_http   | 103 ms                                                 | 93.6 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                        |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 834 ms: 1.42x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                       |
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 138 ms: 1.08x faster                                                        |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                        |
| regex_effbot   | 3.61 ms                                                | 3.88 ms: 1.07x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 81.4 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                       |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                       |
| django_template | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 382 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 27.3 us: 1.49x faster                                                       |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 834 ms: 1.42x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                        |
| deepcopy                   | 371 us                                                 | 264 us: 1.40x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 858 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                        |
| richards                   | 45.8 ms                                                | 36.3 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                       |
| richards_super             | 51.5 ms                                                | 41.1 ms: 1.25x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                                       |
| nbody                      | 97.0 ms                                                | 79.7 ms: 1.22x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 62.0 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                       |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                        |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                       |
| logging_format             | 7.23 us                                                | 6.06 us: 1.19x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                       |
| chaos                      | 67.0 ms                                                | 57.1 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                       |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                        |
| fannkuch                   | 417 ms                                                 | 361 ms: 1.16x faster                                                        |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                        |
| tornado_http               | 103 ms                                                 | 93.6 ms: 1.10x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 81.4 ms: 1.10x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                       |
| regex_compile              | 148 ms                                                 | 138 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                        |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                       |
| gc_traversal               | 3.79 ms                                                | 3.58 ms: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 742 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                      |
| sympy_str                  | 300 ms                                                 | 290 ms: 1.03x faster                                                        |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                        |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                                        |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.6 ms: 1.03x faster                                                       |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                        |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 826 us: 1.02x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                        |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                       |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                        |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                        |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.02x slower                                                       |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                        |
| sympy_integrate            | 21.4 ms                                                | 21.9 ms: 1.02x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.58 ms: 1.03x slower                                                       |
| sympy_expand               | 478 ms                                                 | 493 ms: 1.03x slower                                                        |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                        |
| mdp                        | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                      |
| nqueens                    | 83.3 ms                                                | 86.6 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 57.4 ms: 1.05x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.05x slower                                                        |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.88 ms: 1.07x slower                                                       |
| docutils                   | 2.77 sec                                               | 3.02 sec: 1.09x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                       |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                       |
| coverage                   | 72.7 ms                                                | 92.2 ms: 1.27x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240713-3.14.0a0-95535e9-JIT/bm-20240713-linux-x86_64-brandtbucher-no_progress_needed_8-3.14.0a0-95535e9.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x