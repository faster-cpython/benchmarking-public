# Results vs. 3.12.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.39x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 423 ms: 1.48x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.38 sec: 1.18x slower                                                      |
| tornado_http   | 121 ms                                                       | 169 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.35x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 885 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 367 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 469 ms: 1.15x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 940 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 631 ms: 1.11x faster                                                        |
| async_tree_none            | 452 ms                                                       | 416 ms: 1.09x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 515 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 675 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| float          | 76.6 ms                                                      | 140 ms: 1.83x slower                                                        |
| nbody          | 88.0 ms                                                      | 194 ms: 2.21x slower                                                        |
| Geometric mean | (ref)                                                        | 1.56x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| regex_compile  | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| pickle_list          | 4.43 us                                                      | 4.50 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| unpickle             | 14.8 us                                                      | 16.8 us: 1.13x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.29 us: 1.13x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 113 ms: 1.31x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 14.0 ms: 1.37x slower                                                       |
| tomli_loads          | 2.16 sec                                                     | 3.31 sec: 1.53x slower                                                      |
| xml_etree_process    | 58.4 ms                                                      | 91.9 ms: 1.57x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 585 us: 1.84x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 396 us: 1.89x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.5 ms: 1.50x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 66.9 ms: 1.75x slower                                                       |
| mako            | 10.0 ms                                                      | 21.5 ms: 2.15x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.94x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 3.48 ms                                                      | 2.81 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 1.05 sec                                                     | 885 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 367 ms: 1.17x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 469 ms: 1.15x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 940 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 631 ms: 1.11x faster                                                        |
| async_tree_none            | 452 ms                                                       | 416 ms: 1.09x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 515 ms: 1.06x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 675 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 32.2 us: 1.01x faster                                                       |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| pickle_list                | 4.43 us                                                      | 4.50 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 1.70 ms: 1.07x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.98 us: 1.07x slower                                                       |
| generators                 | 37.4 ms                                                      | 41.4 ms: 1.11x slower                                                       |
| unpickle                   | 14.8 us                                                      | 16.8 us: 1.13x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.29 us: 1.13x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 27.0 ms: 1.14x slower                                                       |
| deepcopy                   | 368 us                                                       | 424 us: 1.15x slower                                                        |
| json                       | 5.12 ms                                                      | 5.93 ms: 1.16x slower                                                       |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.86 sec: 1.17x slower                                                      |
| docutils                   | 2.87 sec                                                     | 3.38 sec: 1.18x slower                                                      |
| json_loads                 | 24.4 us                                                      | 29.0 us: 1.19x slower                                                       |
| asyncio_tcp                | 378 ms                                                       | 457 ms: 1.21x slower                                                        |
| coroutines                 | 23.0 ms                                                      | 28.0 ms: 1.22x slower                                                       |
| async_generators           | 390 ms                                                       | 488 ms: 1.25x slower                                                        |
| mdp                        | 2.57 sec                                                     | 3.26 sec: 1.27x slower                                                      |
| scimark_fft                | 301 ms                                                       | 388 ms: 1.29x slower                                                        |
| meteor_contest             | 128 ms                                                       | 166 ms: 1.29x slower                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 113 ms: 1.31x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.52 ms: 1.31x slower                                                       |
| deepcopy_memo              | 36.8 us                                                      | 48.4 us: 1.32x slower                                                       |
| comprehensions             | 21.9 us                                                      | 29.3 us: 1.34x slower                                                       |
| sympy_integrate            | 23.9 ms                                                      | 32.1 ms: 1.34x slower                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 4.53 us: 1.34x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 89.2 ms: 1.36x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 11.8 ms: 1.37x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 14.0 ms: 1.37x slower                                                       |
| tornado_http               | 121 ms                                                       | 169 ms: 1.39x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.74 sec: 1.41x slower                                                      |
| nqueens                    | 89.9 ms                                                      | 128 ms: 1.42x slower                                                        |
| sympy_str                  | 302 ms                                                       | 447 ms: 1.48x slower                                                        |
| 2to3                       | 285 ms                                                       | 423 ms: 1.48x slower                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 120 ms: 1.49x slower                                                        |
| telco                      | 6.96 ms                                                      | 10.4 ms: 1.49x slower                                                       |
| python_startup             | 11.6 ms                                                      | 17.5 ms: 1.50x slower                                                       |
| tomli_loads                | 2.16 sec                                                     | 3.31 sec: 1.53x slower                                                      |
| regex_compile              | 144 ms                                                       | 223 ms: 1.55x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 180 ms: 1.55x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 91.9 ms: 1.57x slower                                                       |
| sqlglot_optimize           | 57.5 ms                                                      | 90.5 ms: 1.58x slower                                                       |
| sympy_sum                  | 162 ms                                                       | 259 ms: 1.60x slower                                                        |
| coverage                   | 66.7 ms                                                      | 109 ms: 1.63x slower                                                        |
| logging_format             | 7.48 us                                                      | 12.4 us: 1.65x slower                                                       |
| sympy_expand               | 484 ms                                                       | 807 ms: 1.67x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 1.35 sec: 1.67x slower                                                      |
| pprint_pformat             | 1.65 sec                                                     | 2.81 sec: 1.70x slower                                                      |
| logging_simple             | 6.71 us                                                      | 11.5 us: 1.71x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 261 us: 1.72x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 1.66 ms: 1.74x slower                                                       |
| pyflate                    | 439 ms                                                       | 767 ms: 1.75x slower                                                        |
| django_template            | 38.2 ms                                                      | 66.9 ms: 1.75x slower                                                       |
| fannkuch                   | 350 ms                                                       | 619 ms: 1.77x slower                                                        |
| richards                   | 45.7 ms                                                      | 81.4 ms: 1.78x slower                                                       |
| spectral_norm              | 91.6 ms                                                      | 164 ms: 1.79x slower                                                        |
| float                      | 76.6 ms                                                      | 140 ms: 1.83x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 585 us: 1.84x slower                                                        |
| sqlglot_transpile          | 1.78 ms                                                      | 3.35 ms: 1.89x slower                                                       |
| unpickle_pure_python       | 210 us                                                       | 396 us: 1.89x slower                                                        |
| richards_super             | 51.3 ms                                                      | 97.4 ms: 1.90x slower                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 131 ms: 1.90x slower                                                        |
| chaos                      | 64.0 ms                                                      | 122 ms: 1.91x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 11.5 ms: 1.93x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 187 ns: 1.98x slower                                                        |
| go                         | 150 ms                                                       | 301 ms: 2.01x slower                                                        |
| raytrace                   | 298 ms                                                       | 605 ms: 2.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 2.83 ms: 2.05x slower                                                       |
| mako                       | 10.0 ms                                                      | 21.5 ms: 2.15x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 217 ms: 2.20x slower                                                        |
| nbody                      | 88.0 ms                                                      | 194 ms: 2.21x slower                                                        |
| scimark_sor                | 109 ms                                                       | 258 ms: 2.37x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 130 ns: 2.45x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 8.17 ms: 2.53x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.39x slower                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.07x