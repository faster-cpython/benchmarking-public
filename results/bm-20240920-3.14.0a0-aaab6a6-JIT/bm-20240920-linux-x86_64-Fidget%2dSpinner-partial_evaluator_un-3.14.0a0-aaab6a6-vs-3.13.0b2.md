# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.04x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                            |
| docutils       | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                          |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                           |
| tornado_http   | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                            |
| async_tree_io              | 939 ms                                                     | 862 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                            |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.07x faster                                                            |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                           |
| nbody          | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                           |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                      | 1.08x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| regex_dna      | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                            |
| regex_effbot   | 3.67 ms                                                    | 3.92 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                      | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.7 ms: 1.14x faster                                                           |
| xml_etree_process    | 61.2 ms                                                    | 53.7 ms: 1.14x faster                                                           |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                     | 98.1 ms: 1.09x faster                                                           |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                          |
| json_loads           | 28.9 us                                                    | 26.6 us: 1.09x faster                                                           |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                           |
| unpickle             | 15.1 us                                                    | 14.4 us: 1.05x faster                                                           |
| pickle_dict          | 34.8 us                                                    | 34.4 us: 1.01x faster                                                           |
| unpickle_pure_python | 218 us                                                     | 216 us: 1.01x faster                                                            |
| unpickle_list        | 5.34 us                                                    | 5.29 us: 1.01x faster                                                           |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                           |
| pickle_pure_python   | 305 us                                                     | 309 us: 1.01x slower                                                            |
| pickle_list          | 5.11 us                                                    | 5.17 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| genshi_text     | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                           |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                           |
| genshi_xml      | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                                           |
| deepcopy                   | 367 us                                                     | 260 us: 1.41x faster                                                            |
| richards                   | 50.9 ms                                                    | 39.6 ms: 1.29x faster                                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.63 us: 1.27x faster                                                           |
| richards_super             | 57.4 ms                                                    | 45.7 ms: 1.26x faster                                                           |
| scimark_fft                | 392 ms                                                     | 320 ms: 1.23x faster                                                            |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.37 ms: 1.21x faster                                                           |
| async_tree_none            | 378 ms                                                     | 320 ms: 1.18x faster                                                            |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                           |
| async_tree_memoization     | 463 ms                                                     | 403 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 444 ms                                                     | 389 ms: 1.14x faster                                                            |
| xml_etree_generate         | 87.4 ms                                                    | 76.7 ms: 1.14x faster                                                           |
| xml_etree_process          | 61.2 ms                                                    | 53.7 ms: 1.14x faster                                                           |
| float                      | 78.9 ms                                                    | 69.4 ms: 1.14x faster                                                           |
| mako                       | 11.2 ms                                                    | 9.92 ms: 1.13x faster                                                           |
| bpe_tokeniser              | 5.02 sec                                                   | 4.46 sec: 1.13x faster                                                          |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                            |
| coverage                   | 93.1 ms                                                    | 84.2 ms: 1.11x faster                                                           |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                            |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                     | 98.1 ms: 1.09x faster                                                           |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                           |
| go                         | 145 ms                                                     | 132 ms: 1.09x faster                                                            |
| async_tree_io              | 939 ms                                                     | 862 ms: 1.09x faster                                                            |
| nbody                      | 88.3 ms                                                    | 81.1 ms: 1.09x faster                                                           |
| spectral_norm              | 116 ms                                                     | 107 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                                           |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                            |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                          |
| json_loads                 | 28.9 us                                                    | 26.6 us: 1.09x faster                                                           |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.2 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 569 ms: 1.07x faster                                                            |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                                            |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                                            |
| telco                      | 8.41 ms                                                    | 7.88 ms: 1.07x faster                                                           |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                            |
| json                       | 5.31 ms                                                    | 4.97 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.07x faster                                                            |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                           |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                           |
| chaos                      | 61.3 ms                                                    | 58.4 ms: 1.05x faster                                                           |
| unpickle                   | 15.1 us                                                    | 14.4 us: 1.05x faster                                                           |
| pyflate                    | 484 ms                                                     | 464 ms: 1.04x faster                                                            |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                            |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                                            |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.03x faster                                                           |
| regex_v8                   | 25.1 ms                                                    | 24.3 ms: 1.03x faster                                                           |
| html5lib                   | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                           |
| coroutines                 | 23.2 ms                                                    | 22.5 ms: 1.03x faster                                                           |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                            |
| logging_simple             | 5.74 us                                                    | 5.62 us: 1.02x faster                                                           |
| asyncio_tcp                | 508 ms                                                     | 497 ms: 1.02x faster                                                            |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                            |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                            |
| gc_traversal               | 3.98 ms                                                    | 3.91 ms: 1.02x faster                                                           |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                          |
| pickle_dict                | 34.8 us                                                    | 34.4 us: 1.01x faster                                                           |
| unpickle_pure_python       | 218 us                                                     | 216 us: 1.01x faster                                                            |
| unpickle_list              | 5.34 us                                                    | 5.29 us: 1.01x faster                                                           |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                           |
| tornado_http               | 94.6 ms                                                    | 95.1 ms: 1.00x slower                                                           |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                           |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                           |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                            |
| pickle_pure_python         | 305 us                                                     | 309 us: 1.01x slower                                                            |
| pickle_list                | 5.11 us                                                    | 5.17 us: 1.01x slower                                                           |
| regex_dna                  | 221 ms                                                     | 226 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.03x slower                                                           |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.03x slower                                                            |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                            |
| async_generators           | 442 ms                                                     | 456 ms: 1.03x slower                                                            |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                            |
| genshi_text                | 23.7 ms                                                    | 24.6 ms: 1.04x slower                                                           |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.04x slower                                                           |
| docutils                   | 2.83 sec                                                   | 2.97 sec: 1.05x slower                                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                                           |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                           |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                            |
| regex_effbot               | 3.67 ms                                                    | 3.92 ms: 1.07x slower                                                           |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                            |
| hexiom                     | 6.30 ms                                                    | 6.86 ms: 1.09x slower                                                           |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                            |
| generators                 | 29.6 ms                                                    | 33.0 ms: 1.11x slower                                                           |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                           |
| genshi_xml                 | 51.6 ms                                                    | 58.1 ms: 1.13x slower                                                           |
| pylint                     | 317 ms                                                     | 373 ms: 1.18x slower                                                            |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                                    |

Benchmark hidden because not significant (6): pprint_safe_repr, pycparser, typing_runtime_protocols, comprehensions, bench_thread_pool, dulwich_log
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240920-3.14.0a0-aaab6a6-JIT/bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.59x