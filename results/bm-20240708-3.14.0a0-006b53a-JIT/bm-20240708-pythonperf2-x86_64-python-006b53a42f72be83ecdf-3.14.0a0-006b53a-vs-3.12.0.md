# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-x86_64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.01x faster
- HPT reliability: 80.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.08 sec: 1.08x slower                                                      |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 793 ms: 1.33x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                        |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 99.4 ms: 1.04x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 216 us: 1.03x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.22 ms: 1.09x faster                                                       |
| django_template | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 387 ms: 1.40x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 793 ms: 1.33x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 410 ms: 1.33x faster                                                        |
| async_tree_none            | 452 ms                                                       | 342 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 541 ms: 1.29x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.6 us: 1.29x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 818 ms: 1.27x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                       |
| deepcopy                   | 368 us                                                       | 307 us: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 581 ms: 1.20x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 69.8 ms: 1.15x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.99 us: 1.13x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 84.0 ms: 1.09x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.22 ms: 1.09x faster                                                       |
| generators                 | 37.4 ms                                                      | 34.5 ms: 1.08x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.8 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.5 ms: 1.07x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.97 ms: 1.06x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| scimark_fft                | 301 ms                                                       | 289 ms: 1.04x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.45 us: 1.04x faster                                                       |
| logging_format             | 7.48 us                                                      | 7.19 us: 1.04x faster                                                       |
| fannkuch                   | 350 ms                                                       | 337 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 99.4 ms: 1.04x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 920 us: 1.03x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                       |
| float                      | 76.6 ms                                                      | 75.2 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 795 ms: 1.02x faster                                                        |
| async_generators           | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| regex_dna                  | 239 ms                                                       | 237 ms: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                      |
| raytrace                   | 298 ms                                                       | 296 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| xml_etree_process          | 58.4 ms                                                      | 58.7 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.2 ms: 1.01x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 394 ms: 1.02x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.1 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                                       |
| sympy_str                  | 302 ms                                                       | 310 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| richards_super             | 51.3 ms                                                      | 52.7 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 216 us: 1.03x slower                                                        |
| pyflate                    | 439 ms                                                       | 455 ms: 1.04x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 93.5 ms: 1.04x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 9.02 ms: 1.04x slower                                                       |
| json                       | 5.12 ms                                                      | 5.39 ms: 1.05x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 100 ns: 1.06x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 25.5 ms: 1.07x slower                                                       |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.08 sec: 1.08x slower                                                      |
| sympy_expand               | 484 ms                                                       | 523 ms: 1.08x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                                       |
| go                         | 150 ms                                                       | 163 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 62.9 ms: 1.10x slower                                                       |
| django_template            | 38.2 ms                                                      | 42.1 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.11x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.68 ms: 1.12x slower                                                       |
| scimark_sor                | 109 ms                                                       | 123 ms: 1.13x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.69 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.09 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.96 ms: 1.23x slower                                                       |
| coverage                   | 66.7 ms                                                      | 83.8 ms: 1.26x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.67 ms: 1.34x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (6): xml_etree_parse, richards, tornado_http, asyncio_tcp, dask, bench_mp_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf2-x86_64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 80.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x