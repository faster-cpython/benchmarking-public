# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: exit_operand
- machine: linux-x86_64
- commit hash: d4c66d7
- commit date: 2024-07-24
- overall geometric mean: 1.04x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                              |
| html5lib       | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                               |
| tornado_http   | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                      | 1.01x faster                                                        |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                               |
| nbody          | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                               |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                      | 1.08x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                               |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                |
| regex_dna      | 221 ms                                                     | 229 ms: 1.03x slower                                                |
| regex_effbot   | 3.67 ms                                                    | 3.94 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                      | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|---------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 148 ms: 1.09x faster                                                |
| xml_etree_generate  | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                               |
| tomli_loads         | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                              |
| xml_etree_iterparse | 107 ms                                                     | 100 ms: 1.07x faster                                                |
| xml_etree_process   | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                               |
| json_dumps          | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                               |
| json_loads          | 28.9 us                                                    | 28.2 us: 1.03x faster                                               |
| pickle_pure_python  | 305 us                                                     | 298 us: 1.02x faster                                                |
| Geometric mean      | (ref)                                                      | 1.05x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                               |
| python_startup_no_site | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                      | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                               |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                               |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                               |
| genshi_xml      | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 29.4 us: 1.35x faster                                               |
| deepcopy                   | 367 us                                                     | 277 us: 1.33x faster                                                |
| scimark_fft                | 392 ms                                                     | 313 ms: 1.25x faster                                                |
| richards                   | 50.9 ms                                                    | 41.0 ms: 1.24x faster                                               |
| richards_super             | 57.4 ms                                                    | 47.1 ms: 1.22x faster                                               |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.36 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.35 us                                                    | 2.85 us: 1.17x faster                                               |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                |
| mako                       | 11.2 ms                                                    | 9.79 ms: 1.15x faster                                               |
| crypto_pyaes               | 77.5 ms                                                    | 68.0 ms: 1.14x faster                                               |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.9 ms: 1.14x faster                                               |
| async_tree_memoization_tg  | 444 ms                                                     | 391 ms: 1.13x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                |
| float                      | 78.9 ms                                                    | 70.8 ms: 1.11x faster                                               |
| pyflate                    | 484 ms                                                     | 437 ms: 1.11x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.54 sec: 1.11x faster                                              |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                |
| nbody                      | 88.3 ms                                                    | 80.4 ms: 1.10x faster                                               |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.09x faster                                                |
| mdp                        | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                              |
| fannkuch                   | 402 ms                                                     | 368 ms: 1.09x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 860 ms: 1.09x faster                                                |
| xml_etree_generate         | 87.4 ms                                                    | 80.7 ms: 1.08x faster                                               |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 565 ms: 1.08x faster                                                |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                               |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                              |
| pprint_pformat             | 1.56 sec                                                   | 1.45 sec: 1.07x faster                                              |
| xml_etree_iterparse        | 107 ms                                                     | 100 ms: 1.07x faster                                                |
| gc_traversal               | 3.98 ms                                                    | 3.72 ms: 1.07x faster                                               |
| telco                      | 8.41 ms                                                    | 7.91 ms: 1.06x faster                                               |
| pprint_safe_repr           | 758 ms                                                     | 715 ms: 1.06x faster                                                |
| logging_format             | 6.47 us                                                    | 6.10 us: 1.06x faster                                               |
| xml_etree_process          | 61.2 ms                                                    | 57.9 ms: 1.06x faster                                               |
| async_tree_io              | 939 ms                                                     | 891 ms: 1.05x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                               |
| html5lib                   | 67.2 ms                                                    | 63.9 ms: 1.05x faster                                               |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                               |
| logging_simple             | 5.74 us                                                    | 5.54 us: 1.04x faster                                               |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                               |
| thrift                     | 823 us                                                     | 797 us: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                               |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.03x faster                                               |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.02x faster                                                |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                               |
| json                       | 5.31 ms                                                    | 5.18 ms: 1.02x faster                                               |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                              |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.61 ms: 1.01x faster                                               |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                               |
| generators                 | 29.6 ms                                                    | 29.4 ms: 1.01x faster                                               |
| tornado_http               | 94.6 ms                                                    | 94.1 ms: 1.01x faster                                               |
| asyncio_tcp                | 508 ms                                                     | 505 ms: 1.01x faster                                                |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                               |
| logging_silent             | 105 ns                                                     | 105 ns: 1.00x slower                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                               |
| regex_v8                   | 25.1 ms                                                    | 25.3 ms: 1.01x slower                                               |
| sqlglot_optimize           | 55.5 ms                                                    | 56.1 ms: 1.01x slower                                               |
| pycparser                  | 1.16 sec                                                   | 1.17 sec: 1.01x slower                                              |
| python_startup_no_site     | 7.11 ms                                                    | 7.19 ms: 1.01x slower                                               |
| regex_compile              | 137 ms                                                     | 139 ms: 1.02x slower                                                |
| scimark_sor                | 127 ms                                                     | 130 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 165 us                                                     | 168 us: 1.02x slower                                                |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                              |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                               |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.03x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 69.8 ms: 1.04x slower                                               |
| scimark_lu                 | 122 ms                                                     | 127 ms: 1.04x slower                                                |
| hexiom                     | 6.30 ms                                                    | 6.62 ms: 1.05x slower                                               |
| async_generators           | 442 ms                                                     | 465 ms: 1.05x slower                                                |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                               |
| sympy_expand               | 473 ms                                                     | 506 ms: 1.07x slower                                                |
| regex_effbot               | 3.67 ms                                                    | 3.94 ms: 1.07x slower                                               |
| sympy_integrate            | 20.5 ms                                                    | 22.3 ms: 1.09x slower                                               |
| nqueens                    | 81.4 ms                                                    | 88.7 ms: 1.09x slower                                               |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                |
| pylint                     | 317 ms                                                     | 353 ms: 1.11x slower                                                |
| genshi_xml                 | 51.6 ms                                                    | 57.8 ms: 1.12x slower                                               |
| deltablue                  | 3.25 ms                                                    | 3.64 ms: 1.12x slower                                               |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                        |

Benchmark hidden because not significant (5): dask, coroutines, 2to3, bench_thread_pool, unpickle_pure_python
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x