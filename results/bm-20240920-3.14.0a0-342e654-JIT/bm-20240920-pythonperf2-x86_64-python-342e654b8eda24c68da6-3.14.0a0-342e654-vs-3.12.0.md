# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.022x faster
- HPT reliability: 77.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 310 ms: 1.09x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.38x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 801 ms: 1.31x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 801 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 73.7 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| regex_dna      | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 78.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| pickle_dict          | 32.5 us                                                      | 32.4 us: 1.00x faster                                                       |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.01x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.51 us: 1.02x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 213 us: 1.02x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.75 us: 1.02x slower                                                       |
| pickle               | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                                       |
| django_template | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 320 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 308 ms: 1.40x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 390 ms: 1.38x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 26.9 us: 1.37x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 401 ms: 1.36x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 801 ms: 1.31x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 801 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 544 ms: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 289 us: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 574 ms: 1.21x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.7 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.88 us: 1.17x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 70.6 ms: 1.14x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 82.3 ms: 1.11x faster                                                       |
| mako                       | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 78.7 ms: 1.09x faster                                                       |
| nbody                      | 88.0 ms                                                      | 81.1 ms: 1.09x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.07x faster                                                       |
| scimark_fft                | 301 ms                                                       | 283 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.96 ms: 1.06x faster                                                       |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.13 us: 1.05x faster                                                       |
| scimark_sor                | 109 ms                                                       | 104 ms: 1.05x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| float                      | 76.6 ms                                                      | 73.7 ms: 1.04x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.46 ms: 1.03x faster                                                       |
| async_generators           | 390 ms                                                       | 380 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.54 us: 1.03x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 96.5 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 807 ms                                                       | 789 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.72 us: 1.02x faster                                                       |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.12 sec: 1.02x faster                                                      |
| regex_dna                  | 239 ms                                                       | 235 ms: 1.02x faster                                                        |
| generators                 | 37.4 ms                                                      | 36.9 ms: 1.02x faster                                                       |
| deltablue                  | 3.24 ms                                                      | 3.19 ms: 1.01x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 143 ms: 1.00x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 376 ms: 1.00x faster                                                        |
| pickle_dict                | 32.5 us                                                      | 32.4 us: 1.00x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                      |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.60 sec: 1.01x slower                                                      |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                                        |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.01x slower                                                       |
| json                       | 5.12 ms                                                      | 5.20 ms: 1.02x slower                                                       |
| pickle_list                | 4.43 us                                                      | 4.51 us: 1.02x slower                                                       |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 213 us: 1.02x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.75 us: 1.02x slower                                                       |
| sympy_str                  | 302 ms                                                       | 309 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                        |
| pickle                     | 10.5 us                                                      | 10.8 us: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.9 ms: 1.03x slower                                                       |
| fannkuch                   | 350 ms                                                       | 361 ms: 1.03x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 168 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.03x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.97 ms: 1.04x slower                                                       |
| chaos                      | 64.0 ms                                                      | 66.6 ms: 1.04x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                       |
| raytrace                   | 298 ms                                                       | 316 ms: 1.06x slower                                                        |
| pyflate                    | 439 ms                                                       | 465 ms: 1.06x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.06x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 102 ns: 1.08x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.08x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 97.2 ms: 1.08x slower                                                       |
| sympy_expand               | 484 ms                                                       | 524 ms: 1.08x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 5.17 ms: 1.08x slower                                                       |
| 2to3                       | 285 ms                                                       | 310 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 1.94 ms: 1.09x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 26.3 ms: 1.10x slower                                                       |
| docutils                   | 2.87 sec                                                     | 3.16 sec: 1.10x slower                                                      |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.11x slower                                                        |
| django_template            | 38.2 ms                                                      | 43.1 ms: 1.13x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 65.6 ms: 1.14x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.4 ms: 1.15x slower                                                       |
| telco                      | 6.96 ms                                                      | 8.05 ms: 1.16x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.95 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 179 us: 1.18x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.91 ms: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 4.40 ms: 1.27x slower                                                       |
| unpack_sequence            | 53.2 ns                                                      | 91.8 ns: 1.73x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, tornado_http, scimark_monte_carlo
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.022x faster
# HPT report

- Reliability score: 77.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x