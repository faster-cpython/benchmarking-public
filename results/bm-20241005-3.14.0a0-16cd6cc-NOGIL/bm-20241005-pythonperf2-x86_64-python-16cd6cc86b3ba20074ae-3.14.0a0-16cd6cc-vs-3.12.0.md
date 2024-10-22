# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.41x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 421 ms: 1.48x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.38 sec: 1.18x slower                                                      |
| tornado_http   | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| Geometric mean | (ref)                                                        | 1.34x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 882 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 371 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 475 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 939 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 636 ms: 1.10x faster                                                        |
| async_tree_none            | 452 ms                                                       | 422 ms: 1.07x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 519 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 681 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 141 ms: 1.84x slower                                                        |
| nbody          | 88.0 ms                                                      | 193 ms: 2.19x slower                                                        |
| Geometric mean | (ref)                                                        | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                       |
| regex_dna      | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| regex_compile  | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle               | 10.5 us                                                      | 9.98 us: 1.05x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 30.9 us: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.40 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 108 ms: 1.05x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.22 us: 1.12x slower                                                       |
| unpickle             | 14.8 us                                                      | 17.1 us: 1.16x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.5 us: 1.21x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 111 ms: 1.29x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 13.7 ms: 1.34x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 89.3 ms: 1.53x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.31 sec: 1.53x slower                                                      |
| pickle_pure_python   | 318 us                                                       | 579 us: 1.82x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 399 us: 1.91x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.24x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.4 ms: 1.50x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 65.4 ms: 1.71x slower                                                       |
| mako            | 10.0 ms                                                      | 21.3 ms: 2.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.91x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 882 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 371 ms: 1.16x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 475 ms: 1.14x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 939 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 636 ms: 1.10x faster                                                        |
| gc_traversal               | 3.48 ms                                                      | 3.19 ms: 1.09x faster                                                       |
| async_tree_none            | 452 ms                                                       | 422 ms: 1.07x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| pickle                     | 10.5 us                                                      | 9.98 us: 1.05x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 30.9 us: 1.05x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 519 ms: 1.05x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 377 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 681 ms: 1.02x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.40 us: 1.01x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.02x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.66 ms: 1.02x slower                                                       |
| regex_dna                  | 239 ms                                                       | 246 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 108 ms: 1.05x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.98 us: 1.07x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.72 ms: 1.08x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.22 us: 1.12x slower                                                       |
| generators                 | 37.4 ms                                                      | 42.1 ms: 1.12x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| deepcopy                   | 368 us                                                       | 423 us: 1.15x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.83 sec: 1.16x slower                                                      |
| unpickle                   | 14.8 us                                                      | 17.1 us: 1.16x slower                                                       |
| json                       | 5.12 ms                                                      | 5.94 ms: 1.16x slower                                                       |
| coroutines                 | 23.0 ms                                                      | 26.9 ms: 1.17x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.38 sec: 1.18x slower                                                      |
| asyncio_tcp                | 378 ms                                                       | 455 ms: 1.21x slower                                                        |
| json_loads                 | 24.4 us                                                      | 29.5 us: 1.21x slower                                                       |
| async_generators           | 390 ms                                                       | 479 ms: 1.23x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.19 sec: 1.24x slower                                                      |
| scimark_fft                | 301 ms                                                       | 384 ms: 1.28x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 111 ms: 1.29x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.48 ms: 1.30x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 49.0 us: 1.33x slower                                                       |
| meteor_contest             | 128 ms                                                       | 171 ms: 1.33x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 13.7 ms: 1.34x slower                                                       |
| comprehensions             | 21.9 us                                                      | 29.5 us: 1.34x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.55 us: 1.35x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 32.4 ms: 1.35x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 89.2 ms: 1.37x slower                                                       |
| tornado_http               | 121 ms                                                       | 166 ms: 1.37x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.70 sec: 1.38x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 128 ms: 1.43x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.2 ms: 1.47x slower                                                       |
| sympy_str                  | 302 ms                                                       | 445 ms: 1.47x slower                                                        |
| 2to3                       | 285 ms                                                       | 421 ms: 1.48x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 119 ms: 1.48x slower                                                        |
| python_startup             | 11.6 ms                                                      | 17.4 ms: 1.50x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 89.3 ms: 1.53x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 3.31 sec: 1.53x slower                                                      |
| regex_compile              | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 179 ms: 1.55x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 90.1 ms: 1.57x slower                                                       |
| coverage                   | 66.7 ms                                                      | 105 ms: 1.58x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 259 ms: 1.60x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.4 us: 1.65x slower                                                       |
| sympy_expand               | 484 ms                                                       | 805 ms: 1.66x slower                                                        |
| fannkuch                   | 350 ms                                                       | 583 ms: 1.66x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.35 sec: 1.67x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.79 sec: 1.68x slower                                                      |
| logging_simple             | 6.71 us                                                      | 11.3 us: 1.69x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 258 us: 1.70x slower                                                        |
| django_template            | 38.2 ms                                                      | 65.4 ms: 1.71x slower                                                       |
| pyflate                    | 439 ms                                                       | 754 ms: 1.72x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.65 ms: 1.74x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 161 ms: 1.75x slower                                                        |
| richards                   | 45.7 ms                                                      | 81.6 ms: 1.78x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 579 us: 1.82x slower                                                        |
| float                      | 76.6 ms                                                      | 141 ms: 1.84x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.34 ms: 1.88x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 130 ms: 1.88x slower                                                        |
| chaos                      | 64.0 ms                                                      | 121 ms: 1.89x slower                                                        |
| richards_super             | 51.3 ms                                                      | 97.8 ms: 1.90x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 399 us: 1.91x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 11.4 ms: 1.91x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 181 ns: 1.92x slower                                                        |
| go                         | 150 ms                                                       | 292 ms: 1.95x slower                                                        |
| raytrace                   | 298 ms                                                       | 596 ms: 2.00x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.82 ms: 2.05x slower                                                       |
| mako                       | 10.0 ms                                                      | 21.3 ms: 2.13x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 216 ms: 2.19x slower                                                        |
| nbody                      | 88.0 ms                                                      | 193 ms: 2.19x slower                                                        |
| scimark_sor                | 109 ms                                                       | 247 ms: 2.27x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.13 ms: 2.51x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 136 ns: 2.55x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 34.0 ms: 7.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.41x slower                                                                |
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.08x