# Results vs. 3.12.0

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.057x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                       |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 619 ms: 1.70x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 621 ms: 1.68x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 264 ms: 1.63x faster                                                       |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 342 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 488 ms: 1.43x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.8 ms: 1.08x faster                                                      |
| pidigits       | 265 ms                                                       | 256 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                                      |
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                       |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                       |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.2 ms: 1.07x faster                                                      |
| xml_etree_generate   | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                      |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                     |
| json_loads           | 24.4 us                                                      | 23.5 us: 1.04x faster                                                      |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                      |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                      |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                      |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 619 ms: 1.70x faster                                                       |
| async_tree_io              | 1.04 sec                                                     | 621 ms: 1.68x faster                                                       |
| async_tree_memoization_tg  | 540 ms                                                       | 323 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 431 ms                                                       | 264 ms: 1.63x faster                                                       |
| async_tree_none            | 452 ms                                                       | 280 ms: 1.61x faster                                                       |
| async_tree_memoization     | 544 ms                                                       | 342 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 488 ms: 1.43x faster                                                       |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 501 ms: 1.39x faster                                                       |
| deepcopy                   | 368 us                                                       | 277 us: 1.33x faster                                                       |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                      |
| generators                 | 37.4 ms                                                      | 29.2 ms: 1.28x faster                                                      |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                      |
| go                         | 150 ms                                                       | 125 ms: 1.19x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 3.37 us                                                      | 2.87 us: 1.18x faster                                                      |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.13x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 72.7 ms: 1.11x faster                                                      |
| raytrace                   | 298 ms                                                       | 270 ms: 1.10x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                      |
| logging_format             | 7.48 us                                                      | 6.80 us: 1.10x faster                                                      |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.8 ms: 1.10x faster                                                      |
| regex_effbot               | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                                      |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                      |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                       |
| float                      | 76.6 ms                                                      | 70.8 ms: 1.08x faster                                                      |
| logging_simple             | 6.71 us                                                      | 6.22 us: 1.08x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 96.2 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.65 sec                                                     | 1.55 sec: 1.07x faster                                                     |
| xml_etree_generate         | 86.1 ms                                                      | 81.3 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 807 ms                                                       | 763 ms: 1.06x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.7 ms: 1.06x faster                                                      |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.7 ms: 1.06x faster                                                      |
| sqlglot_normalize          | 116 ms                                                       | 110 ms: 1.05x faster                                                       |
| chaos                      | 64.0 ms                                                      | 60.9 ms: 1.05x faster                                                      |
| sqlglot_optimize           | 57.5 ms                                                      | 54.8 ms: 1.05x faster                                                      |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                     |
| mdp                        | 2.57 sec                                                     | 2.45 sec: 1.05x faster                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.70 ms: 1.05x faster                                                      |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                      |
| nqueens                    | 89.9 ms                                                      | 86.2 ms: 1.04x faster                                                      |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.04x faster                                                      |
| json_loads                 | 24.4 us                                                      | 23.5 us: 1.04x faster                                                      |
| pidigits                   | 265 ms                                                       | 256 ms: 1.03x faster                                                       |
| bench_thread_pool          | 950 us                                                       | 923 us: 1.03x faster                                                       |
| spectral_norm              | 91.6 ms                                                      | 89.2 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                       |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                     |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                       |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                       |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                                      |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                     |
| pyflate                    | 439 ms                                                       | 435 ms: 1.01x faster                                                       |
| json                       | 5.12 ms                                                      | 5.08 ms: 1.01x faster                                                      |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x slower                                                       |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                       |
| hexiom                     | 5.96 ms                                                      | 6.01 ms: 1.01x slower                                                      |
| deltablue                  | 3.24 ms                                                      | 3.28 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                      |
| dulwich_log                | 65.4 ms                                                      | 66.5 ms: 1.02x slower                                                      |
| richards_super             | 51.3 ms                                                      | 52.3 ms: 1.02x slower                                                      |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.9 ns: 1.04x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 9.05 ms: 1.05x slower                                                      |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 165 us: 1.09x slower                                                       |
| telco                      | 6.96 ms                                                      | 7.66 ms: 1.10x slower                                                      |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                      |
| async_generators           | 390 ms                                                       | 433 ms: 1.11x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                      |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.73 ms: 1.12x slower                                                      |
| coverage                   | 66.7 ms                                                      | 81.2 ms: 1.22x slower                                                      |
| mypy2                      | 830 ms                                                       | 1.01 sec: 1.22x slower                                                     |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                      |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                      |
| gc_traversal               | 3.48 ms                                                      | 6.37 ms: 1.83x slower                                                      |
| bench_mp_pool              | 4.76 ms                                                      | 1.48 sec: 311.55x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (4): sympy_expand, nbody, scimark_fft, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-pythonperf2-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x