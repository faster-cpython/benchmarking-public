# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 6b9055c
- commit date: 2024-08-14
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 353 ms: 1.24x slower                                                                |
| docutils       | 2.87 sec                                                     | 3.54 sec: 1.24x slower                                                              |
| tornado_http   | 121 ms                                                       | 127 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                        | 1.17x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 320 ms: 1.35x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 404 ms: 1.34x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 811 ms: 1.30x faster                                                                |
| async_tree_none            | 452 ms                                                       | 348 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 443 ms: 1.23x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 853 ms: 1.22x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                                                |
| Geometric mean             | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| float          | 76.6 ms                                                      | 93.8 ms: 1.22x slower                                                               |
| nbody          | 88.0 ms                                                      | 128 ms: 1.45x slower                                                                |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                                |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.14x slower                                                               |
| regex_compile  | 144 ms                                                       | 208 ms: 1.45x slower                                                                |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 116 ms: 1.12x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                               |
| xml_etree_generate   | 86.1 ms                                                      | 101 ms: 1.17x slower                                                                |
| xml_etree_process    | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                               |
| pickle_pure_python   | 318 us                                                       | 410 us: 1.29x slower                                                                |
| unpickle_pure_python | 210 us                                                       | 272 us: 1.30x slower                                                                |
| tomli_loads          | 2.16 sec                                                     | 2.87 sec: 1.33x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.17x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.12 ms: 1.06x slower                                                               |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                               |
| mako            | 10.0 ms                                                      | 14.6 ms: 1.46x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.30x slower                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 320 ms: 1.35x faster                                                                |
| async_tree_memoization_tg  | 540 ms                                                       | 404 ms: 1.34x faster                                                                |
| async_tree_io_tg           | 1.05 sec                                                     | 811 ms: 1.30x faster                                                                |
| async_tree_none            | 452 ms                                                       | 348 ms: 1.30x faster                                                                |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 561 ms: 1.24x faster                                                                |
| async_tree_memoization     | 544 ms                                                       | 443 ms: 1.23x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 853 ms: 1.22x faster                                                                |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.13x faster                                                               |
| deepcopy_reduce            | 3.37 us                                                      | 3.23 us: 1.04x faster                                                               |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                |
| deepcopy                   | 368 us                                                       | 355 us: 1.04x faster                                                                |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                                               |
| async_generators           | 390 ms                                                       | 385 ms: 1.01x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.67 us: 1.01x faster                                                               |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                                |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                              |
| asyncio_tcp                | 378 ms                                                       | 388 ms: 1.03x slower                                                                |
| asyncio_websockets         | 387 ms                                                       | 398 ms: 1.03x slower                                                                |
| bench_thread_pool          | 950 us                                                       | 982 us: 1.03x slower                                                                |
| tornado_http               | 121 ms                                                       | 127 ms: 1.04x slower                                                                |
| bench_mp_pool              | 4.76 ms                                                      | 4.99 ms: 1.05x slower                                                               |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 9.12 ms: 1.06x slower                                                               |
| mdp                        | 2.57 sec                                                     | 2.80 sec: 1.09x slower                                                              |
| raytrace                   | 298 ms                                                       | 325 ms: 1.09x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 116 ms: 1.12x slower                                                                |
| json                       | 5.12 ms                                                      | 5.78 ms: 1.13x slower                                                               |
| meteor_contest             | 128 ms                                                       | 145 ms: 1.13x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.14x slower                                                               |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                               |
| json_dumps                 | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                               |
| django_template            | 38.2 ms                                                      | 44.4 ms: 1.16x slower                                                               |
| xml_etree_generate         | 86.1 ms                                                      | 101 ms: 1.17x slower                                                                |
| sympy_sum                  | 162 ms                                                       | 192 ms: 1.18x slower                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 95.2 ms: 1.18x slower                                                               |
| sympy_integrate            | 23.9 ms                                                      | 28.5 ms: 1.19x slower                                                               |
| xml_etree_process          | 58.4 ms                                                      | 70.0 ms: 1.20x slower                                                               |
| coverage                   | 66.7 ms                                                      | 80.0 ms: 1.20x slower                                                               |
| generators                 | 37.4 ms                                                      | 45.3 ms: 1.21x slower                                                               |
| float                      | 76.6 ms                                                      | 93.8 ms: 1.22x slower                                                               |
| sqlglot_normalize          | 116 ms                                                       | 142 ms: 1.23x slower                                                                |
| sympy_str                  | 302 ms                                                       | 373 ms: 1.23x slower                                                                |
| docutils                   | 2.87 sec                                                     | 3.54 sec: 1.24x slower                                                              |
| 2to3                       | 285 ms                                                       | 353 ms: 1.24x slower                                                                |
| comprehensions             | 21.9 us                                                      | 27.2 us: 1.24x slower                                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 2.21 ms: 1.24x slower                                                               |
| chaos                      | 64.0 ms                                                      | 80.0 ms: 1.25x slower                                                               |
| pycparser                  | 1.23 sec                                                     | 1.54 sec: 1.25x slower                                                              |
| sqlglot_parse              | 1.38 ms                                                      | 1.73 ms: 1.26x slower                                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 72.5 ms: 1.26x slower                                                               |
| pprint_safe_repr           | 807 ms                                                       | 1.03 sec: 1.28x slower                                                              |
| pprint_pformat             | 1.65 sec                                                     | 2.11 sec: 1.28x slower                                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.04 ms: 1.28x slower                                                               |
| scimark_lu                 | 98.8 ms                                                      | 127 ms: 1.28x slower                                                                |
| telco                      | 6.96 ms                                                      | 8.95 ms: 1.29x slower                                                               |
| pickle_pure_python         | 318 us                                                       | 410 us: 1.29x slower                                                                |
| deepcopy_memo              | 36.8 us                                                      | 47.5 us: 1.29x slower                                                               |
| sympy_expand               | 484 ms                                                       | 626 ms: 1.29x slower                                                                |
| nqueens                    | 89.9 ms                                                      | 116 ms: 1.29x slower                                                                |
| unpickle_pure_python       | 210 us                                                       | 272 us: 1.30x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 200 us: 1.32x slower                                                                |
| tomli_loads                | 2.16 sec                                                     | 2.87 sec: 1.33x slower                                                              |
| go                         | 150 ms                                                       | 199 ms: 1.33x slower                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 93.7 ms: 1.36x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 4.76 ms: 1.37x slower                                                               |
| richards_super             | 51.3 ms                                                      | 71.2 ms: 1.39x slower                                                               |
| richards                   | 45.7 ms                                                      | 63.6 ms: 1.39x slower                                                               |
| pyflate                    | 439 ms                                                       | 613 ms: 1.40x slower                                                                |
| scimark_fft                | 301 ms                                                       | 426 ms: 1.42x slower                                                                |
| fannkuch                   | 350 ms                                                       | 496 ms: 1.42x slower                                                                |
| regex_compile              | 144 ms                                                       | 208 ms: 1.45x slower                                                                |
| nbody                      | 88.0 ms                                                      | 128 ms: 1.45x slower                                                                |
| mako                       | 10.0 ms                                                      | 14.6 ms: 1.46x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.62 ms: 1.57x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 5.24 ms: 1.62x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 154 ns: 1.63x slower                                                                |
| scimark_sor                | 109 ms                                                       | 181 ms: 1.66x slower                                                                |
| spectral_norm              | 91.6 ms                                                      | 155 ms: 1.69x slower                                                                |
| hexiom                     | 5.96 ms                                                      | 10.4 ms: 1.75x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                        |

Benchmark hidden because not significant (2): xml_etree_parse, regex_effbot
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240814-3.14.0a0-6b9055c-PYTHON_UOPS/bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 0.94x