# Results vs. 3.12.0

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.083x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                          |
| tornado_http   | 103 ms                                                 | 91.7 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.48x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 859 ms: 1.38x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 874 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                           |
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                           |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                           |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| unpickle             | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                            |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 308 us: 1.05x faster                                                            |
| pickle_dict          | 35.5 us                                                | 34.1 us: 1.04x faster                                                           |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                           |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| unpickle_list        | 5.29 us                                                | 5.32 us: 1.01x slower                                                           |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 312 ms: 1.51x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 386 ms: 1.49x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 392 ms: 1.48x faster                                                            |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 859 ms: 1.38x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.35x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 874 ms: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 550 ms: 1.32x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 562 ms: 1.29x faster                                                            |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                           |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                            |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                            |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.14x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                                           |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                            |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                           |
| tornado_http               | 103 ms                                                 | 91.7 ms: 1.12x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.10 sec: 1.11x faster                                                          |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                            |
| nbody                      | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                           |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                           |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                                           |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                            |
| unpickle                   | 15.9 us                                                | 14.7 us: 1.08x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                           |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                            |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                          |
| unpack_sequence            | 54.0 ns                                                | 50.9 ns: 1.06x faster                                                           |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                           |
| pickle_pure_python         | 324 us                                                 | 308 us: 1.05x faster                                                            |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                           |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 65.5 ms: 1.05x faster                                                           |
| asyncio_tcp                | 491 ms                                                 | 469 ms: 1.05x faster                                                            |
| pickle_dict                | 35.5 us                                                | 34.1 us: 1.04x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                            |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                            |
| scimark_fft                | 382 ms                                                 | 368 ms: 1.04x faster                                                            |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.04x faster                                                           |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                           |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                            |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.02x faster                                                            |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                           |
| gc_traversal               | 3.79 ms                                                | 3.72 ms: 1.02x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                           |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                          |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                            |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                           |
| pyflate                    | 482 ms                                                 | 477 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.77 sec: 1.01x faster                                                          |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                            |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.08 ms: 1.00x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.32 us: 1.01x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 850 us: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                                            |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                           |
| richards                   | 45.8 ms                                                | 46.9 ms: 1.02x slower                                                           |
| richards_super             | 51.5 ms                                                | 53.2 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.75 ms: 1.04x slower                                                           |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                           |
| telco                      | 7.10 ms                                                | 8.00 ms: 1.13x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                           |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 56.1 ms: 2.34x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): django_template, spectral_norm
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-cb9433d/bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.083x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x