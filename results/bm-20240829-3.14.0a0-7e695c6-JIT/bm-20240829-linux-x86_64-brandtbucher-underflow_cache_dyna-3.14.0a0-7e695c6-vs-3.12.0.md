# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_cache_dyna
- machine: linux-x86_64
- commit hash: 7e695c6
- commit date: 2024-08-29
- overall geometric mean: 1.06x faster
- HPT reliability: 97.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                        |
| docutils       | 2.77 sec                                               | 3.30 sec: 1.19x slower                                                      |
| tornado_http   | 103 ms                                                 | 99.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 901 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.3 ms: 1.22x faster                                                       |
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 154 ms: 1.04x slower                                                        |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                       |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 77.1 ms: 1.16x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.05x faster                                                        |
| json_dumps           | 10.4 ms                                                | 9.94 ms: 1.05x faster                                                       |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                       |
| django_template | 34.6 ms                                                | 38.9 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.1 us: 1.56x faster                                                       |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 411 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 410 ms: 1.40x faster                                                        |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 901 ms: 1.31x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 936 ms: 1.24x faster                                                        |
| nbody                      | 97.0 ms                                                | 79.3 ms: 1.22x faster                                                       |
| mako                       | 11.9 ms                                                | 9.74 ms: 1.22x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 61.7 ms: 1.22x faster                                                       |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 67.5 ms: 1.21x faster                                                       |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 101 ms: 1.17x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 77.1 ms: 1.16x faster                                                       |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.40 ms: 1.15x faster                                                       |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.13x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.73 us: 1.13x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                                       |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                       |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                        |
| logging_silent             | 104 ns                                                 | 94.7 ns: 1.10x faster                                                       |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                      |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.05x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 9.94 ms: 1.05x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                      |
| tornado_http               | 103 ms                                                 | 99.5 ms: 1.03x faster                                                       |
| bench_thread_pool          | 842 us                                                 | 830 us: 1.01x faster                                                        |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                       |
| async_generators           | 463 ms                                                 | 465 ms: 1.01x slower                                                        |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                       |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 503 ms: 1.03x slower                                                        |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                        |
| regex_compile              | 148 ms                                                 | 154 ms: 1.04x slower                                                        |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                       |
| sympy_sum                  | 169 ms                                                 | 180 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.80 ms: 1.07x slower                                                       |
| sympy_str                  | 300 ms                                                 | 321 ms: 1.07x slower                                                        |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 110 ms                                                 | 120 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 59.7 ms: 1.09x slower                                                       |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                                       |
| generators                 | 31.2 ms                                                | 34.3 ms: 1.10x slower                                                       |
| sympy_expand               | 478 ms                                                 | 528 ms: 1.10x slower                                                        |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                       |
| sympy_integrate            | 21.4 ms                                                | 23.7 ms: 1.11x slower                                                       |
| django_template            | 34.6 ms                                                | 38.9 ms: 1.12x slower                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.53 ms: 1.12x slower                                                       |
| scimark_sor                | 129 ms                                                 | 154 ms: 1.19x slower                                                        |
| docutils                   | 2.77 sec                                               | 3.30 sec: 1.19x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.42 sec: 1.20x slower                                                      |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.21x slower                                                       |
| go                         | 139 ms                                                 | 173 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (4): pidigits, bench_mp_pool, coroutines, json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240829-3.14.0a0-7e695c6-JIT/bm-20240829-linux-x86_64-brandtbucher-underflow_cache_dyna-3.14.0a0-7e695c6.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.42% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x