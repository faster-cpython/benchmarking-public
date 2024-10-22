# Results vs. 3.12.0

- fork: faster-cpython
- ref: refactor_refcnt_mort
- machine: linux-x86_64
- commit hash: 2fbc12f
- commit date: 2024-10-10
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                          |
| tornado_http   | 103 ms                                                 | 91.3 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                            |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 930 ms: 1.24x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                           |
| nbody          | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                           |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.57 ms: 1.01x faster                                                           |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.17 sec: 1.07x faster                                                          |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                           |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| pickle_dict          | 35.5 us                                                | 34.0 us: 1.04x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 224 us: 1.03x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 87.8 ms: 1.02x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.01x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.38 us: 1.02x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                           |
| django_template | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 311 ms: 1.45x faster                                                            |
| async_tree_none            | 472 ms                                                 | 327 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 405 ms: 1.42x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                            |
| deepcopy                   | 371 us                                                 | 268 us: 1.38x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 541 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 917 ms: 1.29x faster                                                            |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 32.2 us: 1.27x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 930 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                           |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                            |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                           |
| go                         | 139 ms                                                 | 123 ms: 1.14x faster                                                            |
| raytrace                   | 312 ms                                                 | 275 ms: 1.14x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.69 us: 1.13x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                            |
| tornado_http               | 103 ms                                                 | 91.3 ms: 1.12x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.11x faster                                                           |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                           |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                            |
| chaos                      | 67.0 ms                                                | 61.2 ms: 1.09x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 69.2 ms: 1.09x faster                                                           |
| unpack_sequence            | 54.0 ns                                                | 49.7 ns: 1.09x faster                                                           |
| json                       | 5.26 ms                                                | 4.85 ms: 1.09x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.17 sec: 1.07x faster                                                          |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                            |
| float                      | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                           |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                           |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                            |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 65.4 ms: 1.05x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                          |
| pickle_dict                | 35.5 us                                                | 34.0 us: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                           |
| nbody                      | 97.0 ms                                                | 93.0 ms: 1.04x faster                                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                           |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                           |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                          |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 224 us: 1.03x faster                                                            |
| scimark_fft                | 382 ms                                                 | 373 ms: 1.02x faster                                                            |
| asyncio_tcp                | 491 ms                                                 | 479 ms: 1.02x faster                                                            |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 87.8 ms: 1.02x faster                                                           |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.02x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.01x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.57 ms: 1.01x faster                                                           |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 54.5 ms: 1.01x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.39 ms: 1.00x faster                                                           |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                            |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                           |
| bench_thread_pool          | 842 us                                                 | 850 us: 1.01x slower                                                            |
| django_template            | 34.6 ms                                                | 35.0 ms: 1.01x slower                                                           |
| unpickle_list              | 5.29 us                                                | 5.38 us: 1.02x slower                                                           |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                           |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                            |
| richards                   | 45.8 ms                                                | 47.1 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                            |
| richards_super             | 51.5 ms                                                | 53.3 ms: 1.04x slower                                                           |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 3.98 ms: 1.05x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                           |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                           |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                                           |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 56.3 ms: 2.35x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (6): scimark_sor, asyncio_tcp_ssl, pyflate, pickle, pycparser, logging_silent
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241010-3.14.0a0-2fbc12f/bm-20241010-linux-x86_64-faster%2dcpython-refactor_refcnt_mort-3.14.0a0-2fbc12f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.97x