# Results vs. 3.12.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d343f97
- commit date: 2024-09-06
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                  |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                |
| tornado_http   | 103 ms                                                 | 91.6 ms: 1.12x faster                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 387 ms: 1.49x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 892 ms: 1.33x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                  |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                  |
| Geometric mean             | (ref)                                                  | 1.38x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.3 ms: 1.12x faster                                 |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                  |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                 |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                  |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                  |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                 |
| unpickle             | 15.9 us                                                | 15.2 us: 1.04x faster                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                  |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                 |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                 |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                 |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                 |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                 |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 387 ms: 1.49x faster                                  |
| async_tree_none_tg         | 450 ms                                                 | 306 ms: 1.47x faster                                  |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                  |
| async_tree_io_tg           | 1.18 sec                                               | 892 ms: 1.33x faster                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 555 ms: 1.31x faster                                  |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                 |
| async_tree_io              | 1.16 sec                                               | 927 ms: 1.25x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                 |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                 |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                  |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                  |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                 |
| logging_format             | 7.23 us                                                | 6.26 us: 1.15x faster                                 |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                 |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                  |
| nbody                      | 97.0 ms                                                | 86.3 ms: 1.12x faster                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                 |
| tornado_http               | 103 ms                                                 | 91.6 ms: 1.12x faster                                 |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                 |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.12x faster                                 |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                 |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                 |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                  |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                  |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                 |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                  |
| unpack_sequence            | 54.0 ns                                                | 50.4 ns: 1.07x faster                                 |
| bench_thread_pool          | 842 us                                                 | 790 us: 1.07x faster                                  |
| gc_traversal               | 3.79 ms                                                | 3.56 ms: 1.07x faster                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                 |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                 |
| async_generators           | 463 ms                                                 | 439 ms: 1.05x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                 |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                  |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                 |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                  |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                  |
| unpickle                   | 15.9 us                                                | 15.2 us: 1.04x faster                                 |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                  |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                  |
| asyncio_tcp                | 491 ms                                                 | 481 ms: 1.02x faster                                  |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                  |
| pyflate                    | 482 ms                                                 | 475 ms: 1.02x faster                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                  |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                 |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                 |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                 |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                 |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                  |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                  |
| pickle_list                | 5.08 us                                                | 5.16 us: 1.01x slower                                 |
| richards                   | 45.8 ms                                                | 46.5 ms: 1.01x slower                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                 |
| json                       | 5.26 ms                                                | 5.35 ms: 1.02x slower                                 |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                 |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                 |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                  |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                 |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.16x slower                                 |
| telco                      | 7.10 ms                                                | 8.27 ms: 1.17x slower                                 |
| coverage                   | 72.7 ms                                                | 86.6 ms: 1.19x slower                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                          |

Benchmark hidden because not significant (4): spectral_norm, xml_etree_iterparse, bench_mp_pool, pickle
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.14.0a0-d343f97/bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.085x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x