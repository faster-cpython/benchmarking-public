# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.025x faster
- HPT reliability: 82.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| tornado_http   | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 790 ms: 1.33x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| float          | 76.6 ms                                                      | 78.2 ms: 1.02x slower                                                       |
| nbody          | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.3 us: 1.08x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.28 us: 1.03x faster                                                       |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                        |
| json_loads           | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 59.4 ms: 1.02x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 229 us: 1.09x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.63 sec: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 310 ms: 1.39x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.39x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 400 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 790 ms: 1.33x faster                                                        |
| deepcopy                   | 368 us                                                       | 284 us: 1.30x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 807 ms: 1.29x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 543 ms: 1.28x faster                                                        |
| generators                 | 37.4 ms                                                      | 29.6 ms: 1.27x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 29.3 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 570 ms: 1.22x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.21x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 857 us: 1.11x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.2 ms: 1.10x faster                                                       |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                                        |
| go                         | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 30.3 us: 1.08x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.98 us: 1.07x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.38 us: 1.05x faster                                                       |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.05x faster                                                       |
| raytrace                   | 298 ms                                                       | 286 ms: 1.04x faster                                                        |
| tornado_http               | 121 ms                                                       | 117 ms: 1.04x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.28 us: 1.03x faster                                                       |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                                      |
| regex_compile              | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                      |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                                      |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 52.6 ns: 1.01x faster                                                       |
| chaos                      | 64.0 ms                                                      | 63.4 ms: 1.01x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 89.1 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 802 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 116 ms                                                       | 116 ms: 1.01x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 57.9 ms: 1.01x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| scimark_fft                | 301 ms                                                       | 305 ms: 1.01x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 66.4 ms: 1.02x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.4 ms: 1.02x slower                                                       |
| float                      | 76.6 ms                                                      | 78.2 ms: 1.02x slower                                                       |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                        |
| asyncio_websockets         | 387 ms                                                       | 397 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.16 ms: 1.03x slower                                                       |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                                       |
| nbody                      | 88.0 ms                                                      | 91.6 ms: 1.04x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 96.7 ms: 1.06x slower                                                       |
| deltablue                  | 3.24 ms                                                      | 3.42 ms: 1.06x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 99.7 ns: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 229 us: 1.09x slower                                                        |
| pyflate                    | 439 ms                                                       | 483 ms: 1.10x slower                                                        |
| scimark_sor                | 109 ms                                                       | 120 ms: 1.10x slower                                                        |
| richards_super             | 51.3 ms                                                      | 57.0 ms: 1.11x slower                                                       |
| richards                   | 45.7 ms                                                      | 50.9 ms: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 176 us: 1.16x slower                                                        |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.34 ms: 1.20x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.63 sec: 1.22x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 1.99 ms: 1.25x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, sqlite_synth, scimark_lu, unpickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 82.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x