# Results vs. 3.12.0

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.03x faster
- HPT reliability: 92.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 317 ms: 1.43x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 794 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 814 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| float          | 76.6 ms                                                      | 78.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 239 ms                                                       | 233 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 212 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.8 us: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.37 sec: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| django_template | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 317 ms: 1.43x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 306 ms: 1.41x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 397 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 794 ms: 1.33x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 287 us: 1.28x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 814 ms: 1.28x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 568 ms: 1.22x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.91 us: 1.16x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 858 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                       |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.84 us: 1.09x faster                                                       |
| async_generators           | 390 ms                                                       | 362 ms: 1.08x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.29 us: 1.07x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.1 ms: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.7 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.2 ms: 1.05x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.9 ms: 1.04x faster                                                       |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| sympy_str                  | 302 ms                                                       | 292 ms: 1.04x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                                        |
| regex_dna                  | 239 ms                                                       | 233 ms: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 87.9 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 101 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 804 ms: 1.00x faster                                                        |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 86.7 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 58.1 ms: 1.01x slower                                                       |
| fannkuch                   | 350 ms                                                       | 354 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 212 us: 1.01x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.8 us: 1.02x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                       |
| float                      | 76.6 ms                                                      | 78.4 ms: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 60.1 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.3 ns: 1.03x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| docutils                   | 2.87 sec                                                     | 2.97 sec: 1.04x slower                                                      |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.04x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.6 ms: 1.04x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.37 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.34 ms: 1.04x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.23 ms: 1.05x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 97.0 ms: 1.06x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.7 ms: 1.09x slower                                                       |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                        |
| pyflate                    | 439 ms                                                       | 479 ms: 1.09x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.37 sec: 1.10x slower                                                      |
| richards_super             | 51.3 ms                                                      | 56.9 ms: 1.11x slower                                                       |
| richards                   | 45.7 ms                                                      | 51.0 ms: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.33 ms: 1.20x slower                                                       |
| go                         | 150 ms                                                       | 183 ms: 1.22x slower                                                        |
| coverage                   | 66.7 ms                                                      | 82.6 ms: 1.24x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.98 ms: 1.25x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.38 ms: 1.26x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, regex_effbot, asyncio_websockets, xml_etree_parse, pickle_pure_python
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-pythonperf2-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 92.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x