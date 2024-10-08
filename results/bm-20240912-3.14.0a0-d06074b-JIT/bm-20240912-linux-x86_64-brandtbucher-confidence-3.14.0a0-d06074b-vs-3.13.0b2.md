# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 273 ms: 1.00x faster                                              |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                            |
| html5lib       | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                             |
| tornado_http   | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                      | 1.00x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 393 ms: 1.18x faster                                              |
| async_tree_memoization_tg  | 444 ms                                                     | 384 ms: 1.16x faster                                              |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                              |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                              |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                              |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                             |
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.11x faster                                             |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                      | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                             |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                              |
| regex_effbot   | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                      | 1.01x slower                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|---------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                             |
| xml_etree_process   | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                             |
| xml_etree_parse     | 162 ms                                                     | 145 ms: 1.11x faster                                              |
| tomli_loads         | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                            |
| xml_etree_iterparse | 107 ms                                                     | 98.3 ms: 1.09x faster                                             |
| json_loads          | 28.9 us                                                    | 27.0 us: 1.07x faster                                             |
| json_dumps          | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                             |
| unpickle_list       | 5.34 us                                                    | 5.07 us: 1.05x faster                                             |
| unpickle            | 15.1 us                                                    | 14.4 us: 1.05x faster                                             |
| pickle_pure_python  | 305 us                                                     | 304 us: 1.00x faster                                              |
| pickle_dict         | 34.8 us                                                    | 34.9 us: 1.00x slower                                             |
| pickle              | 11.5 us                                                    | 11.7 us: 1.02x slower                                             |
| pickle_list         | 5.11 us                                                    | 5.24 us: 1.03x slower                                             |
| Geometric mean      | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                             |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                             |
| genshi_text     | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                             |
| genshi_xml      | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                             |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.0 us: 1.47x faster                                             |
| deepcopy                   | 367 us                                                     | 259 us: 1.42x faster                                              |
| richards_super             | 57.4 ms                                                    | 43.3 ms: 1.32x faster                                             |
| richards                   | 50.9 ms                                                    | 39.3 ms: 1.30x faster                                             |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.11 ms: 1.28x faster                                             |
| scimark_fft                | 392 ms                                                     | 308 ms: 1.27x faster                                              |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                             |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 393 ms: 1.18x faster                                              |
| crypto_pyaes               | 77.5 ms                                                    | 66.0 ms: 1.17x faster                                             |
| async_tree_memoization_tg  | 444 ms                                                     | 384 ms: 1.16x faster                                              |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.16x faster                                              |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                             |
| xml_etree_generate         | 87.4 ms                                                    | 76.9 ms: 1.14x faster                                             |
| bpe_tokeniser              | 5.02 sec                                                   | 4.43 sec: 1.13x faster                                            |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                             |
| pyflate                    | 484 ms                                                     | 430 ms: 1.13x faster                                              |
| xml_etree_process          | 61.2 ms                                                    | 54.6 ms: 1.12x faster                                             |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                              |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                             |
| async_tree_none_tg         | 336 ms                                                     | 303 ms: 1.11x faster                                              |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.11x faster                                             |
| go                         | 145 ms                                                     | 131 ms: 1.10x faster                                              |
| coverage                   | 93.1 ms                                                    | 84.4 ms: 1.10x faster                                             |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.10x faster                                              |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                              |
| async_tree_io              | 939 ms                                                     | 858 ms: 1.09x faster                                              |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                            |
| xml_etree_iterparse        | 107 ms                                                     | 98.3 ms: 1.09x faster                                             |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                             |
| sqlite_synth               | 2.99 us                                                    | 2.78 us: 1.08x faster                                             |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                              |
| fannkuch                   | 402 ms                                                     | 375 ms: 1.07x faster                                              |
| async_tree_io_tg           | 936 ms                                                     | 873 ms: 1.07x faster                                              |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                             |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                              |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                              |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                             |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                            |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                             |
| json                       | 5.31 ms                                                    | 5.01 ms: 1.06x faster                                             |
| unpickle_list              | 5.34 us                                                    | 5.07 us: 1.05x faster                                             |
| telco                      | 8.41 ms                                                    | 8.00 ms: 1.05x faster                                             |
| mdp                        | 2.79 sec                                                   | 2.66 sec: 1.05x faster                                            |
| unpickle                   | 15.1 us                                                    | 14.4 us: 1.05x faster                                             |
| thrift                     | 823 us                                                     | 789 us: 1.04x faster                                              |
| html5lib                   | 67.2 ms                                                    | 64.6 ms: 1.04x faster                                             |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                             |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                              |
| chaos                      | 61.3 ms                                                    | 59.2 ms: 1.04x faster                                             |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                              |
| asyncio_tcp                | 508 ms                                                     | 494 ms: 1.03x faster                                              |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                             |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                             |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                             |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                             |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                            |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                              |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.01x faster                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                             |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.00x faster                                              |
| 2to3                       | 274 ms                                                     | 273 ms: 1.00x faster                                              |
| gc_traversal               | 3.98 ms                                                    | 3.98 ms: 1.00x slower                                             |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                             |
| tornado_http               | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                             |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                             |
| bench_thread_pool          | 834 us                                                     | 838 us: 1.01x slower                                              |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                             |
| sqlglot_parse              | 1.32 ms                                                    | 1.34 ms: 1.01x slower                                             |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                             |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                              |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                              |
| pickle_list                | 5.11 us                                                    | 5.24 us: 1.03x slower                                             |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                              |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                             |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                             |
| nqueens                    | 81.4 ms                                                    | 84.1 ms: 1.03x slower                                             |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                              |
| regex_effbot               | 3.67 ms                                                    | 3.82 ms: 1.04x slower                                             |
| genshi_text                | 23.7 ms                                                    | 24.8 ms: 1.05x slower                                             |
| sqlglot_optimize           | 55.5 ms                                                    | 58.2 ms: 1.05x slower                                             |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                            |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                              |
| sympy_expand               | 473 ms                                                     | 500 ms: 1.06x slower                                              |
| hexiom                     | 6.30 ms                                                    | 6.88 ms: 1.09x slower                                             |
| genshi_xml                 | 51.6 ms                                                    | 56.4 ms: 1.09x slower                                             |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                              |
| generators                 | 29.6 ms                                                    | 32.9 ms: 1.11x slower                                             |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                             |
| pylint                     | 317 ms                                                     | 375 ms: 1.18x slower                                              |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                      |

Benchmark hidden because not significant (6): unpickle_pure_python, deltablue, logging_silent, regex_dna, dulwich_log, pycparser
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-d06074b-JIT/bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x