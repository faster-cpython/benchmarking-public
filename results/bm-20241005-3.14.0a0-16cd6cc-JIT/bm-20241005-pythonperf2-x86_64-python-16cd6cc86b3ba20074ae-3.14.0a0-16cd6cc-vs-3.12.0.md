# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.06x slower
- HPT reliability: 65.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                      |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 324 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                       |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| float          | 76.6 ms                                                      | 75.5 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                       |
| regex_dna      | 239 ms                                                       | 252 ms: 1.06x slower                                                        |
| regex_compile  | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 26.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 78.4 ms: 1.10x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 30.4 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.23 us: 1.05x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.9 ms: 1.04x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| unpickle_list        | 4.66 us                                                      | 4.58 us: 1.02x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.01x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                      |
| unpickle             | 14.8 us                                                      | 15.2 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 41.8 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_none            | 452 ms                                                       | 324 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 392 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 779 ms: 1.35x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 406 ms: 1.34x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.2 us: 1.31x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 813 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 300 us: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 575 ms: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| comprehensions             | 21.9 us                                                      | 18.8 us: 1.17x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 71.1 ms: 1.13x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.9 ms: 1.10x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 78.4 ms: 1.10x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.15 ms: 1.09x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                       |
| scimark_fft                | 301 ms                                                       | 280 ms: 1.08x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.4 us: 1.07x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 755 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.5 ms: 1.05x faster                                                       |
| nbody                      | 88.0 ms                                                      | 83.6 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                      |
| pickle_list                | 4.43 us                                                      | 4.23 us: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 55.9 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.26 us: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.7 ms: 1.02x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                       |
| scimark_sor                | 109 ms                                                       | 107 ms: 1.02x faster                                                        |
| unpickle_list              | 4.66 us                                                      | 4.58 us: 1.02x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.02x faster                                                       |
| float                      | 76.6 ms                                                      | 75.5 ms: 1.01x faster                                                       |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.01x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.62 us: 1.01x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 68.2 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.21 ms: 1.01x faster                                                       |
| async_generators           | 390 ms                                                       | 392 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 390 ms: 1.01x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                      |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                                        |
| mdp                        | 2.57 sec                                                     | 2.60 sec: 1.01x slower                                                      |
| generators                 | 37.4 ms                                                      | 38.4 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                        |
| go                         | 150 ms                                                       | 154 ms: 1.03x slower                                                        |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.2 us: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.3 ns: 1.03x slower                                                       |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 330 us: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.75 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                        |
| chaos                      | 64.0 ms                                                      | 67.3 ms: 1.05x slower                                                       |
| regex_dna                  | 239 ms                                                       | 252 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                       | 153 ms: 1.06x slower                                                        |
| sympy_str                  | 302 ms                                                       | 322 ms: 1.06x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 174 ms: 1.07x slower                                                        |
| raytrace                   | 298 ms                                                       | 320 ms: 1.07x slower                                                        |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.61 ms: 1.09x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.8 ms: 1.09x slower                                                       |
| sympy_expand               | 484 ms                                                       | 532 ms: 1.10x slower                                                        |
| 2to3                       | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.54 ms: 1.12x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.22 sec: 1.12x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 101 ms: 1.12x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.6 ms: 1.13x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 27.3 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 135 ms: 1.16x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.87 ms: 1.17x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 7.08 ms: 1.19x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 185 us: 1.22x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 70.2 ms: 1.22x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.30 ms: 1.24x slower                                                       |
| coverage                   | 66.7 ms                                                      | 84.0 ms: 1.26x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 89.3 ns: 1.68x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.87 sec: 392.70x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 65.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x