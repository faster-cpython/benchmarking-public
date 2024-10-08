# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: ujb0_project_confide
- machine: linux-x86_64
- commit hash: d467f6c
- commit date: 2024-09-04
- overall geometric mean: 1.00x faster
- HPT reliability: 67.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 294 ms: 1.07x slower                                                        |
| docutils       | 2.83 sec                                                   | 3.52 sec: 1.24x slower                                                      |
| html5lib       | 67.2 ms                                                    | 74.3 ms: 1.11x slower                                                       |
| tornado_http   | 94.6 ms                                                    | 118 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                      | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 341 ms: 1.11x faster                                                        |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 444 ms                                                     | 416 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                        |
| async_tree_io              | 939 ms                                                     | 961 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.06x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 68.7 ms: 1.15x faster                                                       |
| nbody          | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                      | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 218 ms: 1.02x faster                                                        |
| regex_effbot   | 3.67 ms                                                    | 3.65 ms: 1.00x faster                                                       |
| regex_v8       | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                       |
| regex_compile  | 137 ms                                                     | 152 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                      | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 218 us                                                     | 193 us: 1.13x faster                                                        |
| xml_etree_process    | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                       |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.11x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 9.72 ms: 1.10x faster                                                       |
| xml_etree_generate   | 87.4 ms                                                    | 80.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                       |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                        |
| tomli_loads          | 2.12 sec                                                   | 2.15 sec: 1.02x slower                                                      |
| json_loads           | 28.9 us                                                    | 29.6 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.58 ms: 1.17x faster                                                       |
| genshi_text     | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                       |
| genshi_xml      | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                       |
| django_template | 34.8 ms                                                    | 40.5 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-linux-x86_64-brandtbucher-ujb0_project_confide-3.14.0a0-d467f6c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.3 us: 1.51x faster                                                       |
| deepcopy                   | 367 us                                                     | 263 us: 1.39x faster                                                        |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.25x faster                                                       |
| richards                   | 50.9 ms                                                    | 41.4 ms: 1.23x faster                                                       |
| richards_super             | 57.4 ms                                                    | 47.1 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.34 ms: 1.22x faster                                                       |
| scimark_monte_carlo        | 69.2 ms                                                    | 57.9 ms: 1.20x faster                                                       |
| crypto_pyaes               | 77.5 ms                                                    | 66.0 ms: 1.17x faster                                                       |
| mako                       | 11.2 ms                                                    | 9.58 ms: 1.17x faster                                                       |
| float                      | 78.9 ms                                                    | 68.7 ms: 1.15x faster                                                       |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                        |
| unpickle_pure_python       | 218 us                                                     | 193 us: 1.13x faster                                                        |
| scimark_lu                 | 122 ms                                                     | 108 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                       |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.11x faster                                                        |
| async_tree_none            | 378 ms                                                     | 341 ms: 1.11x faster                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 4.53 sec: 1.11x faster                                                      |
| nbody                      | 88.3 ms                                                    | 79.9 ms: 1.10x faster                                                       |
| json_dumps                 | 10.7 ms                                                    | 9.72 ms: 1.10x faster                                                       |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                                       |
| xml_etree_generate         | 87.4 ms                                                    | 80.1 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 758 ms                                                     | 695 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                       |
| async_tree_memoization     | 463 ms                                                     | 427 ms: 1.08x faster                                                        |
| mdp                        | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.82 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 444 ms                                                     | 416 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 551 ms: 1.07x faster                                                        |
| logging_silent             | 105 ns                                                     | 98.3 ns: 1.07x faster                                                       |
| scimark_sor                | 127 ms                                                     | 120 ms: 1.06x faster                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.06x faster                                                      |
| coverage                   | 93.1 ms                                                    | 87.9 ms: 1.06x faster                                                       |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 336 ms                                                     | 321 ms: 1.05x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.82 ms: 1.04x faster                                                       |
| genshi_text                | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                       |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                        |
| chaos                      | 61.3 ms                                                    | 59.9 ms: 1.02x faster                                                       |
| thrift                     | 823 us                                                     | 810 us: 1.02x faster                                                        |
| regex_dna                  | 221 ms                                                     | 218 ms: 1.02x faster                                                        |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                        |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                       |
| asyncio_websockets         | 567 ms                                                     | 560 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.83 sec: 1.01x faster                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.65 ms: 1.00x faster                                                       |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                       |
| pickle_pure_python         | 305 us                                                     | 310 us: 1.01x slower                                                        |
| tomli_loads                | 2.12 sec                                                   | 2.15 sec: 1.02x slower                                                      |
| logging_format             | 6.47 us                                                    | 6.59 us: 1.02x slower                                                       |
| async_tree_io              | 939 ms                                                     | 961 ms: 1.02x slower                                                        |
| json_loads                 | 28.9 us                                                    | 29.6 us: 1.03x slower                                                       |
| coroutines                 | 23.2 ms                                                    | 23.8 ms: 1.03x slower                                                       |
| async_generators           | 442 ms                                                     | 457 ms: 1.03x slower                                                        |
| nqueens                    | 81.4 ms                                                    | 84.5 ms: 1.04x slower                                                       |
| regex_v8                   | 25.1 ms                                                    | 26.1 ms: 1.04x slower                                                       |
| asyncio_tcp                | 508 ms                                                     | 530 ms: 1.04x slower                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.9 ms: 1.04x slower                                                       |
| logging_simple             | 5.74 us                                                    | 6.00 us: 1.04x slower                                                       |
| raytrace                   | 267 ms                                                     | 284 ms: 1.07x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 893 us: 1.07x slower                                                        |
| 2to3                       | 274 ms                                                     | 294 ms: 1.07x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 3.56 ms: 1.09x slower                                                       |
| html5lib                   | 67.2 ms                                                    | 74.3 ms: 1.11x slower                                                       |
| regex_compile              | 137 ms                                                     | 152 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 125 ms: 1.13x slower                                                        |
| genshi_xml                 | 51.6 ms                                                    | 59.2 ms: 1.15x slower                                                       |
| generators                 | 29.6 ms                                                    | 34.1 ms: 1.15x slower                                                       |
| django_template            | 34.8 ms                                                    | 40.5 ms: 1.16x slower                                                       |
| pycparser                  | 1.16 sec                                                   | 1.35 sec: 1.17x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 7.40 ms: 1.18x slower                                                       |
| sympy_expand               | 473 ms                                                     | 559 ms: 1.18x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 67.6 ms: 1.22x slower                                                       |
| sympy_str                  | 282 ms                                                     | 345 ms: 1.22x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 118 ms: 1.24x slower                                                        |
| docutils                   | 2.83 sec                                                   | 3.52 sec: 1.24x slower                                                      |
| go                         | 145 ms                                                     | 181 ms: 1.25x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.75 ms: 1.33x slower                                                       |
| sqlglot_transpile          | 1.63 ms                                                    | 2.19 ms: 1.34x slower                                                       |
| sympy_integrate            | 20.5 ms                                                    | 27.5 ms: 1.34x slower                                                       |
| sympy_sum                  | 156 ms                                                     | 217 ms: 1.39x slower                                                        |
| pylint                     | 317 ms                                                     | 483 ms: 1.52x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.00x faster                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, create_gc_cycles, pyflate, json, comprehensions, typing_runtime_protocols
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 67.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.21x