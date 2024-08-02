# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.51x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 406 ms: 1.48x slower                                                    |
| docutils       | 2.83 sec                                                   | 3.44 sec: 1.22x slower                                                  |
| html5lib       | 67.2 ms                                                    | 102 ms: 1.51x slower                                                    |
| tornado_http   | 94.6 ms                                                    | 139 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                      | 1.42x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io              | 939 ms                                                     | 979 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 678 ms: 1.15x slower                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 732 ms: 1.20x slower                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 536 ms: 1.21x slower                                                    |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                                                    |
| async_tree_memoization     | 463 ms                                                     | 586 ms: 1.27x slower                                                    |
| async_tree_none_tg         | 336 ms                                                     | 427 ms: 1.27x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.17x slower                                                            |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                    |
| float          | 78.9 ms                                                    | 141 ms: 1.78x slower                                                    |
| nbody          | 88.3 ms                                                    | 234 ms: 2.65x slower                                                    |
| Geometric mean | (ref)                                                      | 1.67x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.48 ms: 1.05x faster                                                   |
| regex_v8       | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                   |
| regex_compile  | 137 ms                                                     | 227 ms: 1.66x slower                                                    |
| Geometric mean | (ref)                                                      | 1.13x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                    |
| pickle_list          | 5.11 us                                                    | 4.90 us: 1.04x faster                                                   |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                   |
| unpickle             | 15.1 us                                                    | 16.2 us: 1.07x slower                                                   |
| unpickle_list        | 5.34 us                                                    | 5.73 us: 1.07x slower                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 118 ms: 1.10x slower                                                    |
| json_loads           | 28.9 us                                                    | 31.8 us: 1.10x slower                                                   |
| pickle_dict          | 34.8 us                                                    | 41.1 us: 1.18x slower                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 115 ms: 1.31x slower                                                    |
| json_dumps           | 10.7 ms                                                    | 14.2 ms: 1.33x slower                                                   |
| xml_etree_process    | 61.2 ms                                                    | 92.8 ms: 1.52x slower                                                   |
| tomli_loads          | 2.12 sec                                                   | 3.38 sec: 1.59x slower                                                  |
| unpickle_pure_python | 218 us                                                     | 423 us: 1.94x slower                                                    |
| pickle_pure_python   | 305 us                                                     | 611 us: 2.00x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.26x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 13.7 ms: 1.27x slower                                                   |
| python_startup_no_site | 7.11 ms                                                    | 9.18 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 86.7 ms: 1.68x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 41.6 ms: 1.76x slower                                                   |
| django_template | 34.8 ms                                                    | 62.9 ms: 1.81x slower                                                   |
| mako            | 11.2 ms                                                    | 21.6 ms: 1.92x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.79x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 3.98 ms                                                    | 2.78 ms: 1.43x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.37 ms: 1.32x faster                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 20.4 ms: 1.17x faster                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.48 ms: 1.05x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                    |
| pickle_list                | 5.11 us                                                    | 4.90 us: 1.04x faster                                                   |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 25.5 ms: 1.02x slower                                                   |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                   |
| async_tree_io              | 939 ms                                                     | 979 ms: 1.04x slower                                                    |
| unpickle                   | 15.1 us                                                    | 16.2 us: 1.07x slower                                                   |
| unpickle_list              | 5.34 us                                                    | 5.73 us: 1.07x slower                                                   |
| sqlite_synth               | 2.99 us                                                    | 3.25 us: 1.09x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 118 ms: 1.10x slower                                                    |
| json_loads                 | 28.9 us                                                    | 31.8 us: 1.10x slower                                                   |
| json                       | 5.31 ms                                                    | 5.98 ms: 1.13x slower                                                   |
| pathlib                    | 17.3 ms                                                    | 19.7 ms: 1.14x slower                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 678 ms: 1.15x slower                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 2.13 sec: 1.16x slower                                                  |
| telco                      | 8.41 ms                                                    | 9.83 ms: 1.17x slower                                                   |
| asyncio_tcp                | 508 ms                                                     | 600 ms: 1.18x slower                                                    |
| pickle_dict                | 34.8 us                                                    | 41.1 us: 1.18x slower                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 732 ms: 1.20x slower                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 536 ms: 1.21x slower                                                    |
| docutils                   | 2.83 sec                                                   | 3.44 sec: 1.22x slower                                                  |
| mdp                        | 2.79 sec                                                   | 3.42 sec: 1.23x slower                                                  |
| async_tree_none            | 378 ms                                                     | 472 ms: 1.25x slower                                                    |
| async_tree_memoization     | 463 ms                                                     | 586 ms: 1.27x slower                                                    |
| async_tree_none_tg         | 336 ms                                                     | 427 ms: 1.27x slower                                                    |
| python_startup             | 10.8 ms                                                    | 13.7 ms: 1.27x slower                                                   |
| async_generators           | 442 ms                                                     | 565 ms: 1.28x slower                                                    |
| pylint                     | 317 ms                                                     | 405 ms: 1.28x slower                                                    |
| scimark_fft                | 392 ms                                                     | 506 ms: 1.29x slower                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 9.18 ms: 1.29x slower                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 115 ms: 1.31x slower                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 6.94 ms: 1.32x slower                                                   |
| generators                 | 29.6 ms                                                    | 39.1 ms: 1.32x slower                                                   |
| dulwich_log                | 67.2 ms                                                    | 89.0 ms: 1.32x slower                                                   |
| json_dumps                 | 10.7 ms                                                    | 14.2 ms: 1.33x slower                                                   |
| meteor_contest             | 110 ms                                                     | 154 ms: 1.40x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.65 sec: 1.42x slower                                                  |
| coroutines                 | 23.2 ms                                                    | 33.0 ms: 1.42x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 29.5 ms: 1.44x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 139 ms: 1.47x slower                                                    |
| 2to3                       | 274 ms                                                     | 406 ms: 1.48x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 122 ms: 1.50x slower                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 117 ms: 1.51x slower                                                    |
| html5lib                   | 67.2 ms                                                    | 102 ms: 1.51x slower                                                    |
| xml_etree_process          | 61.2 ms                                                    | 92.8 ms: 1.52x slower                                                   |
| sympy_str                  | 282 ms                                                     | 438 ms: 1.55x slower                                                    |
| fannkuch                   | 402 ms                                                     | 626 ms: 1.56x slower                                                    |
| tomli_loads                | 2.12 sec                                                   | 3.38 sec: 1.59x slower                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 5.39 us: 1.61x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 266 us: 1.62x slower                                                    |
| deepcopy                   | 367 us                                                     | 598 us: 1.63x slower                                                    |
| richards                   | 50.9 ms                                                    | 83.6 ms: 1.64x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 91.4 ms: 1.65x slower                                                   |
| sympy_expand               | 473 ms                                                     | 778 ms: 1.65x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 182 ms: 1.65x slower                                                    |
| regex_compile              | 137 ms                                                     | 227 ms: 1.66x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 86.7 ms: 1.68x slower                                                   |
| pyflate                    | 484 ms                                                     | 813 ms: 1.68x slower                                                    |
| spectral_norm              | 116 ms                                                     | 195 ms: 1.68x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 262 ms: 1.68x slower                                                    |
| deepcopy_memo              | 39.7 us                                                    | 69.8 us: 1.76x slower                                                   |
| richards_super             | 57.4 ms                                                    | 101 ms: 1.76x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 41.6 ms: 1.76x slower                                                   |
| float                      | 78.9 ms                                                    | 141 ms: 1.78x slower                                                    |
| comprehensions             | 16.6 us                                                    | 29.7 us: 1.79x slower                                                   |
| django_template            | 34.8 ms                                                    | 62.9 ms: 1.81x slower                                                   |
| pprint_safe_repr           | 758 ms                                                     | 1.38 sec: 1.82x slower                                                  |
| pprint_pformat             | 1.56 sec                                                   | 2.85 sec: 1.83x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 130 ms: 1.88x slower                                                    |
| logging_format             | 6.47 us                                                    | 12.2 us: 1.88x slower                                                   |
| mako                       | 11.2 ms                                                    | 21.6 ms: 1.92x slower                                                   |
| logging_simple             | 5.74 us                                                    | 11.1 us: 1.93x slower                                                   |
| unpickle_pure_python       | 218 us                                                     | 423 us: 1.94x slower                                                    |
| logging_silent             | 105 ns                                                     | 203 ns: 1.94x slower                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 3.22 ms: 1.97x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 611 us: 2.00x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 12.7 ms: 2.02x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 2.74 ms: 2.08x slower                                                   |
| scimark_lu                 | 122 ms                                                     | 254 ms: 2.09x slower                                                    |
| chaos                      | 61.3 ms                                                    | 129 ms: 2.10x slower                                                    |
| scimark_sor                | 127 ms                                                     | 274 ms: 2.15x slower                                                    |
| go                         | 145 ms                                                     | 329 ms: 2.27x slower                                                    |
| raytrace                   | 267 ms                                                     | 628 ms: 2.35x slower                                                    |
| nbody                      | 88.3 ms                                                    | 234 ms: 2.65x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 8.80 ms: 2.70x slower                                                   |
| bench_thread_pool          | 834 us                                                     | 3.15 ms: 3.78x slower                                                   |
| coverage                   | 93.1 ms                                                    | 802 ms: 8.62x slower                                                    |
| thrift                     | 823 us                                                     | 13.6 ms: 16.53x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.51x slower                                                            |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, regex_dna
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.38x
- 95% likely to have a slowdown of 1.35x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.15x