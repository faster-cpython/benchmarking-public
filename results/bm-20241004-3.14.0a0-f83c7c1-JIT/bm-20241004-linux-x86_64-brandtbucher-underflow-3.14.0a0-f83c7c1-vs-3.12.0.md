# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: f83c7c1
- commit date: 2024-10-04
- overall geometric mean: 1.04x faster
- HPT reliability: 98.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 291 ms: 1.06x slower                                             |
| docutils       | 2.77 sec                                               | 3.07 sec: 1.11x slower                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                             |
| async_tree_io              | 1.16 sec                                               | 890 ms: 1.30x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                             |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.5 ms: 1.19x faster                                            |
| float          | 84.7 ms                                                | 71.3 ms: 1.19x faster                                            |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.67 ms: 1.02x slower                                            |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                             |
| regex_compile  | 148 ms                                                 | 155 ms: 1.04x slower                                             |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 89.2 ms                                                | 77.0 ms: 1.16x faster                                            |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                             |
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                           |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                            |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                             |
| unpickle             | 15.9 us                                                | 14.6 us: 1.09x faster                                            |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                            |
| unpickle_list        | 5.29 us                                                | 5.14 us: 1.03x faster                                            |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                            |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                             |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                            |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                            |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                     |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                            |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                            |
| django_template | 34.6 ms                                                | 41.1 ms: 1.19x slower                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.6 us: 1.53x faster                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                             |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.45x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                             |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 877 ms: 1.35x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 557 ms: 1.30x faster                                             |
| async_tree_io              | 1.16 sec                                               | 890 ms: 1.30x faster                                             |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 60.0 ms: 1.25x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                            |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.24x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                            |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                             |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                            |
| nbody                      | 97.0 ms                                                | 81.5 ms: 1.19x faster                                            |
| float                      | 84.7 ms                                                | 71.3 ms: 1.19x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 77.0 ms: 1.16x faster                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                            |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                            |
| richards                   | 45.8 ms                                                | 40.6 ms: 1.13x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                           |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                             |
| richards_super             | 51.5 ms                                                | 46.2 ms: 1.12x faster                                            |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                            |
| logging_format             | 7.23 us                                                | 6.52 us: 1.11x faster                                            |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                             |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                            |
| fannkuch                   | 417 ms                                                 | 380 ms: 1.10x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                            |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                             |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.09x faster                                            |
| logging_simple             | 6.46 us                                                | 5.99 us: 1.08x faster                                            |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                             |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                             |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                           |
| json                       | 5.26 ms                                                | 5.05 ms: 1.04x faster                                            |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                            |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                            |
| unpickle_list              | 5.29 us                                                | 5.14 us: 1.03x faster                                            |
| gc_traversal               | 3.79 ms                                                | 3.69 ms: 1.03x faster                                            |
| go                         | 139 ms                                                 | 136 ms: 1.02x faster                                             |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                            |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                             |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                             |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                            |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                             |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                           |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                             |
| regex_effbot               | 3.61 ms                                                | 3.67 ms: 1.02x slower                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                            |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                             |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                            |
| asyncio_tcp                | 491 ms                                                 | 502 ms: 1.02x slower                                             |
| regex_compile              | 148 ms                                                 | 155 ms: 1.04x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                             |
| telco                      | 7.10 ms                                                | 7.51 ms: 1.06x slower                                            |
| 2to3                       | 274 ms                                                 | 291 ms: 1.06x slower                                             |
| logging_silent             | 104 ns                                                 | 111 ns: 1.07x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                            |
| bench_thread_pool          | 842 us                                                 | 902 us: 1.07x slower                                             |
| dulwich_log                | 68.5 ms                                                | 73.6 ms: 1.07x slower                                            |
| sympy_str                  | 300 ms                                                 | 323 ms: 1.08x slower                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.83 ms: 1.09x slower                                            |
| hexiom                     | 6.41 ms                                                | 6.97 ms: 1.09x slower                                            |
| pycparser                  | 1.18 sec                                               | 1.30 sec: 1.10x slower                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                            |
| docutils                   | 2.77 sec                                               | 3.07 sec: 1.11x slower                                           |
| sympy_expand               | 478 ms                                                 | 537 ms: 1.12x slower                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.54 ms: 1.13x slower                                            |
| generators                 | 31.2 ms                                                | 35.3 ms: 1.13x slower                                            |
| sympy_sum                  | 169 ms                                                 | 191 ms: 1.13x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 126 ms: 1.14x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 63.8 ms: 1.16x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                            |
| django_template            | 34.6 ms                                                | 41.1 ms: 1.19x slower                                            |
| coverage                   | 72.7 ms                                                | 86.5 ms: 1.19x slower                                            |
| sympy_integrate            | 21.4 ms                                                | 26.1 ms: 1.22x slower                                            |
| unpack_sequence            | 54.0 ns                                                | 106 ns: 1.96x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 60.9 ms: 2.54x slower                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                     |

Benchmark hidden because not significant (3): pprint_pformat, pickle_list, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-f83c7c1-JIT/bm-20241004-linux-x86_64-brandtbucher-underflow-3.14.0a0-f83c7c1.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.24% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x