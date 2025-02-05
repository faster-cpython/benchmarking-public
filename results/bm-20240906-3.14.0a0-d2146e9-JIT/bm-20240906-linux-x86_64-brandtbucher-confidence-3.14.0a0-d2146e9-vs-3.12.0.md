# Results vs. 3.12.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d2146e9
- commit date: 2024-09-06
- overall geometric mean: 1.088x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                              |
| docutils       | 2.77 sec                                               | 3.00 sec: 1.08x slower                                            |
| tornado_http   | 103 ms                                                 | 96.1 ms: 1.07x faster                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                              |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 893 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                              |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                              |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                             |
| nbody          | 97.0 ms                                                | 81.2 ms: 1.19x faster                                             |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.13x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                             |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                              |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 78.3 ms: 1.14x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                              |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                              |
| unpickle             | 15.9 us                                                | 14.8 us: 1.07x faster                                             |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                              |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                             |
| unpickle_list        | 5.29 us                                                | 5.40 us: 1.02x slower                                             |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                             |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.79 ms: 1.21x faster                                             |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.0 us: 1.51x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 396 ms: 1.46x faster                                              |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 313 ms: 1.44x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 407 ms: 1.41x faster                                              |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 893 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 549 ms: 1.32x faster                                              |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 568 ms: 1.28x faster                                              |
| async_tree_io              | 1.16 sec                                               | 929 ms: 1.24x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 66.4 ms: 1.23x faster                                             |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                              |
| mako                       | 11.9 ms                                                | 9.79 ms: 1.21x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                            |
| richards_super             | 51.5 ms                                                | 42.9 ms: 1.20x faster                                             |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                             |
| nbody                      | 97.0 ms                                                | 81.2 ms: 1.19x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 62.9 ms: 1.19x faster                                             |
| richards                   | 45.8 ms                                                | 38.7 ms: 1.18x faster                                             |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                             |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                             |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.43 ms: 1.14x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 78.3 ms: 1.14x faster                                             |
| pyflate                    | 482 ms                                                 | 424 ms: 1.14x faster                                              |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                              |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                              |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                             |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 700 ms: 1.11x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                            |
| unpickle                   | 15.9 us                                                | 14.8 us: 1.07x faster                                             |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                              |
| tornado_http               | 103 ms                                                 | 96.1 ms: 1.07x faster                                             |
| go                         | 139 ms                                                 | 131 ms: 1.07x faster                                              |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                              |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                             |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                             |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                              |
| asyncio_tcp                | 491 ms                                                 | 486 ms: 1.01x faster                                              |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                              |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                             |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| bench_thread_pool          | 842 us                                                 | 839 us: 1.00x faster                                              |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                             |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| sympy_str                  | 300 ms                                                 | 302 ms: 1.01x slower                                              |
| dulwich_log                | 68.5 ms                                                | 69.4 ms: 1.01x slower                                             |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                              |
| unpickle_list              | 5.29 us                                                | 5.40 us: 1.02x slower                                             |
| nqueens                    | 83.3 ms                                                | 85.1 ms: 1.02x slower                                             |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                             |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                              |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                            |
| pickle_list                | 5.08 us                                                | 5.29 us: 1.04x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 58.3 ms: 1.06x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 22.8 ms: 1.06x slower                                             |
| generators                 | 31.2 ms                                                | 33.2 ms: 1.06x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.84 ms: 1.07x slower                                             |
| sympy_expand               | 478 ms                                                 | 511 ms: 1.07x slower                                              |
| docutils                   | 2.77 sec                                               | 3.00 sec: 1.08x slower                                            |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                             |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                             |
| coverage                   | 72.7 ms                                                | 86.8 ms: 1.19x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                             |
| unpack_sequence            | 54.0 ns                                                | 109 ns: 2.02x slower                                              |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (4): pycparser, bench_mp_pool, sqlglot_transpile, pickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.14.0a0-d2146e9-JIT/bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.088x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x