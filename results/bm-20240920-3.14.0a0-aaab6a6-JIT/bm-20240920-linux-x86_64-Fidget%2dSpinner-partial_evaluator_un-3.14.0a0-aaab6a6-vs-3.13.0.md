# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.00x slower
- HPT reliability: 54.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                            |
| docutils       | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                          |
| html5lib       | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                           |
| tornado_http   | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                            |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.01x slower                                                            |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                            |
| async_tree_io              | 843 ms                                                 | 862 ms: 1.02x slower                                                            |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                           |
| nbody          | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| regex_effbot   | 3.88 ms                                                | 3.92 ms: 1.01x slower                                                           |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                            |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 76.7 ms: 1.13x faster                                                           |
| xml_etree_process    | 60.4 ms                                                | 53.7 ms: 1.12x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                          |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 102 ms                                                 | 98.1 ms: 1.04x faster                                                           |
| unpickle             | 14.9 us                                                | 14.4 us: 1.03x faster                                                           |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 309 us: 1.03x slower                                                            |
| pickle_list          | 5.01 us                                                | 5.17 us: 1.03x slower                                                           |
| pickle_dict          | 33.2 us                                                | 34.4 us: 1.04x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.29 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                           |
| genshi_text     | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                           |
| genshi_xml      | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.9 us: 1.41x faster                                                           |
| deepcopy                   | 352 us                                                 | 260 us: 1.36x faster                                                            |
| richards                   | 48.1 ms                                                | 39.6 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 3.17 us                                                | 2.63 us: 1.20x faster                                                           |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.19x faster                                                            |
| richards_super             | 54.4 ms                                                | 45.7 ms: 1.19x faster                                                           |
| scimark_fft                | 369 ms                                                 | 320 ms: 1.15x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.37 ms: 1.15x faster                                                           |
| xml_etree_generate         | 87.0 ms                                                | 76.7 ms: 1.13x faster                                                           |
| float                      | 78.5 ms                                                | 69.4 ms: 1.13x faster                                                           |
| xml_etree_process          | 60.4 ms                                                | 53.7 ms: 1.12x faster                                                           |
| mako                       | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| async_tree_none            | 354 ms                                                 | 320 ms: 1.11x faster                                                            |
| crypto_pyaes               | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                          |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                          |
| pathlib                    | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                           |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                            |
| telco                      | 8.45 ms                                                | 7.88 ms: 1.07x faster                                                           |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| nbody                      | 85.7 ms                                                | 81.1 ms: 1.06x faster                                                           |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                          |
| scimark_lu                 | 115 ms                                                 | 110 ms: 1.05x faster                                                            |
| json                       | 5.20 ms                                                | 4.97 ms: 1.05x faster                                                           |
| xml_etree_iterparse        | 102 ms                                                 | 98.1 ms: 1.04x faster                                                           |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                           |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                                           |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                          |
| scimark_monte_carlo        | 66.3 ms                                                | 64.2 ms: 1.03x faster                                                           |
| unpickle                   | 14.9 us                                                | 14.4 us: 1.03x faster                                                           |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                           |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                            |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                           |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.01x faster                                                            |
| json_loads                 | 27.0 us                                                | 26.6 us: 1.01x faster                                                           |
| logging_simple             | 5.66 us                                                | 5.62 us: 1.01x faster                                                           |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| coverage                   | 83.7 ms                                                | 84.2 ms: 1.01x slower                                                           |
| regex_effbot               | 3.88 ms                                                | 3.92 ms: 1.01x slower                                                           |
| html5lib                   | 64.5 ms                                                | 65.1 ms: 1.01x slower                                                           |
| pyflate                    | 460 ms                                                 | 464 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                          |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                           |
| pprint_safe_repr           | 744 ms                                                 | 754 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 552 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                          |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                                            |
| python_startup_no_site     | 6.99 ms                                                | 7.12 ms: 1.02x slower                                                           |
| async_tree_io              | 843 ms                                                 | 862 ms: 1.02x slower                                                            |
| bench_thread_pool          | 815 us                                                 | 835 us: 1.02x slower                                                            |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.03x slower                                                           |
| gc_traversal               | 3.81 ms                                                | 3.91 ms: 1.03x slower                                                           |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                            |
| pickle_pure_python         | 300 us                                                 | 309 us: 1.03x slower                                                            |
| pickle_list                | 5.01 us                                                | 5.17 us: 1.03x slower                                                           |
| typing_runtime_protocols   | 159 us                                                 | 164 us: 1.03x slower                                                            |
| pickle_dict                | 33.2 us                                                | 34.4 us: 1.04x slower                                                           |
| tornado_http               | 91.5 ms                                                | 95.1 ms: 1.04x slower                                                           |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                                            |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                            |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                           |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                            |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                            |
| async_tree_io_tg           | 825 ms                                                 | 877 ms: 1.06x slower                                                            |
| nqueens                    | 80.6 ms                                                | 85.7 ms: 1.06x slower                                                           |
| unpickle_list              | 4.96 us                                                | 5.29 us: 1.07x slower                                                           |
| dulwich_log                | 63.0 ms                                                | 67.2 ms: 1.07x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                           |
| genshi_text                | 22.9 ms                                                | 24.6 ms: 1.07x slower                                                           |
| regex_compile              | 131 ms                                                 | 142 ms: 1.08x slower                                                            |
| sqlglot_optimize           | 53.9 ms                                                | 58.4 ms: 1.08x slower                                                           |
| sqlglot_transpile          | 1.57 ms                                                | 1.71 ms: 1.09x slower                                                           |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                            |
| create_gc_cycles           | 1.61 ms                                                | 1.75 ms: 1.09x slower                                                           |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                                            |
| hexiom                     | 6.13 ms                                                | 6.86 ms: 1.12x slower                                                           |
| generators                 | 28.8 ms                                                | 33.0 ms: 1.14x slower                                                           |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.97 sec: 1.15x slower                                                          |
| genshi_xml                 | 50.3 ms                                                | 58.1 ms: 1.15x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                            |
| pylint                     | 313 ms                                                 | 373 ms: 1.19x slower                                                            |
| unpack_sequence            | 42.4 ns                                                | 111 ns: 2.62x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_cpu_io_mixed, thrift, chaos, pickle, bench_mp_pool, asyncio_websockets, coroutines, logging_silent
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 54.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.64x