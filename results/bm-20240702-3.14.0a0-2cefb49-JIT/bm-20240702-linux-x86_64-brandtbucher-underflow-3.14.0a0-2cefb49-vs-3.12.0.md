# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 2cefb49
- commit date: 2024-07-02
- overall geometric mean: 1.07x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                             |
| docutils       | 2.77 sec                                               | 3.03 sec: 1.09x slower                                           |
| tornado_http   | 103 ms                                                 | 97.0 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                             |
| async_tree_io              | 1.16 sec                                               | 853 ms: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                             |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 80.2 ms: 1.21x faster                                            |
| float          | 84.7 ms                                                | 70.6 ms: 1.20x faster                                            |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                             |
| regex_effbot   | 3.61 ms                                                | 4.03 ms: 1.12x slower                                            |
| regex_dna      | 212 ms                                                 | 238 ms: 1.12x slower                                             |
| regex_v8       | 23.1 ms                                                | 26.7 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                  | 1.08x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                           |
| pickle_pure_python   | 324 us                                                 | 296 us: 1.10x faster                                             |
| xml_etree_generate   | 89.2 ms                                                | 82.1 ms: 1.09x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.08x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                            |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                            |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.85 ms: 1.21x faster                                            |
| django_template | 34.6 ms                                                | 35.7 ms: 1.03x slower                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.52x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 298 ms: 1.51x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 28.3 us: 1.44x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 845 ms: 1.40x faster                                             |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                             |
| async_tree_io              | 1.16 sec                                               | 853 ms: 1.36x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 543 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 58.2 ms: 1.29x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                            |
| nbody                      | 97.0 ms                                                | 80.2 ms: 1.21x faster                                            |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                             |
| mako                       | 11.9 ms                                                | 9.85 ms: 1.21x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 67.9 ms: 1.21x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                            |
| float                      | 84.7 ms                                                | 70.6 ms: 1.20x faster                                            |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                             |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                            |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                            |
| fannkuch                   | 417 ms                                                 | 360 ms: 1.16x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.45 ms: 1.14x faster                                            |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                           |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                             |
| pickle_pure_python         | 324 us                                                 | 296 us: 1.10x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                             |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 82.1 ms: 1.09x faster                                            |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.08x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                            |
| logging_silent             | 104 ns                                                 | 97.2 ns: 1.07x faster                                            |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.07x faster                                            |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                           |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                             |
| tornado_http               | 103 ms                                                 | 97.0 ms: 1.06x faster                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                            |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                            |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                            |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                           |
| generators                 | 31.2 ms                                                | 30.8 ms: 1.01x faster                                            |
| async_generators           | 463 ms                                                 | 458 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                             |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                            |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                             |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                            |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 55.8 ms: 1.02x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                            |
| go                         | 139 ms                                                 | 143 ms: 1.02x slower                                             |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.03x slower                                             |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                           |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                             |
| django_template            | 34.6 ms                                                | 35.7 ms: 1.03x slower                                            |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                             |
| dulwich_log                | 68.5 ms                                                | 71.3 ms: 1.04x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                            |
| nqueens                    | 83.3 ms                                                | 86.7 ms: 1.04x slower                                            |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                            |
| scimark_lu                 | 118 ms                                                 | 127 ms: 1.08x slower                                             |
| sympy_expand               | 478 ms                                                 | 518 ms: 1.08x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                             |
| docutils                   | 2.77 sec                                               | 3.03 sec: 1.09x slower                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| regex_effbot               | 3.61 ms                                                | 4.03 ms: 1.12x slower                                            |
| regex_dna                  | 212 ms                                                 | 238 ms: 1.12x slower                                             |
| telco                      | 7.10 ms                                                | 7.97 ms: 1.12x slower                                            |
| deltablue                  | 3.72 ms                                                | 4.19 ms: 1.13x slower                                            |
| regex_v8                   | 23.1 ms                                                | 26.7 ms: 1.15x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                            |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.28x slower                                            |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (3): dask, bench_mp_pool, sympy_sum
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240702-3.14.0a0-2cefb49-JIT/bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x