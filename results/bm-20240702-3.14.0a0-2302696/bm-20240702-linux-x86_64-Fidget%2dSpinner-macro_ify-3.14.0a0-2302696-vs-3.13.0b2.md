# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: macro_ify
- machine: linux-x86_64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 262 ms: 1.05x faster                                                 |
| docutils       | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                               |
| html5lib       | 67.2 ms                                                    | 65.7 ms: 1.02x faster                                                |
| tornado_http   | 94.6 ms                                                    | 90.3 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                      | 1.04x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                 |
| async_tree_io              | 939 ms                                                     | 844 ms: 1.11x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.5 ms: 1.03x faster                                                |
| pidigits       | 191 ms                                                     | 187 ms: 1.03x faster                                                 |
| nbody          | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                      | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 130 ms: 1.05x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                |
| regex_dna      | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                      | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_loads           | 28.9 us                                                    | 27.5 us: 1.05x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 156 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.03x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.03x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                         |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                |
| genshi_xml      | 51.6 ms                                                    | 49.8 ms: 1.04x faster                                                |
| django_template | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                                |
| mako            | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                      | 1.03x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 263 us: 1.40x faster                                                 |
| deepcopy_memo              | 39.7 us                                                    | 30.0 us: 1.32x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 378 ms: 1.18x faster                                                 |
| async_tree_none            | 378 ms                                                     | 323 ms: 1.17x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 405 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.65 ms: 1.13x faster                                                |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.57 ms: 1.11x faster                                                |
| async_tree_io              | 939 ms                                                     | 844 ms: 1.11x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.51 sec: 1.11x faster                                               |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                 |
| richards                   | 50.9 ms                                                    | 46.1 ms: 1.10x faster                                                |
| pathlib                    | 17.3 ms                                                    | 15.7 ms: 1.10x faster                                                |
| scimark_fft                | 392 ms                                                     | 357 ms: 1.10x faster                                                 |
| richards_super             | 57.4 ms                                                    | 52.2 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                 |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 73.1 ms: 1.06x faster                                                |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                |
| bench_thread_pool          | 834 us                                                     | 788 us: 1.06x faster                                                 |
| docutils                   | 2.83 sec                                                   | 2.68 sec: 1.06x faster                                               |
| regex_compile              | 137 ms                                                     | 130 ms: 1.05x faster                                                 |
| create_gc_cycles           | 1.82 ms                                                    | 1.72 ms: 1.05x faster                                                |
| json_loads                 | 28.9 us                                                    | 27.5 us: 1.05x faster                                                |
| tornado_http               | 94.6 ms                                                    | 90.3 ms: 1.05x faster                                                |
| 2to3                       | 274 ms                                                     | 262 ms: 1.05x faster                                                 |
| sympy_str                  | 282 ms                                                     | 270 ms: 1.04x faster                                                 |
| dulwich_log                | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                                |
| asyncio_tcp                | 508 ms                                                     | 487 ms: 1.04x faster                                                 |
| genshi_text                | 23.7 ms                                                    | 22.7 ms: 1.04x faster                                                |
| logging_simple             | 5.74 us                                                    | 5.52 us: 1.04x faster                                                |
| sympy_integrate            | 20.5 ms                                                    | 19.7 ms: 1.04x faster                                                |
| sympy_sum                  | 156 ms                                                     | 150 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 66.6 ms: 1.04x faster                                                |
| thrift                     | 823 us                                                     | 792 us: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 53.5 ms: 1.04x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                               |
| fannkuch                   | 402 ms                                                     | 387 ms: 1.04x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 156 ms: 1.04x faster                                                 |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                 |
| genshi_xml                 | 51.6 ms                                                    | 49.8 ms: 1.04x faster                                                |
| dask                       | 369 ms                                                     | 357 ms: 1.03x faster                                                 |
| spectral_norm              | 116 ms                                                     | 112 ms: 1.03x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 78.8 ms: 1.03x faster                                                |
| generators                 | 29.6 ms                                                    | 28.7 ms: 1.03x faster                                                |
| float                      | 78.9 ms                                                    | 76.5 ms: 1.03x faster                                                |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.03x faster                                               |
| go                         | 145 ms                                                     | 140 ms: 1.03x faster                                                 |
| typing_runtime_protocols   | 165 us                                                     | 160 us: 1.03x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                               |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                               |
| async_generators           | 442 ms                                                     | 431 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.03x faster                                                 |
| raytrace                   | 267 ms                                                     | 260 ms: 1.03x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 85.2 ms: 1.03x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.03x faster                                                 |
| django_template            | 34.8 ms                                                    | 33.9 ms: 1.03x faster                                                |
| pidigits                   | 191 ms                                                     | 187 ms: 1.03x faster                                                 |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                 |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                |
| sympy_expand               | 473 ms                                                     | 461 ms: 1.02x faster                                                 |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.02x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 59.8 ms: 1.02x faster                                                |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.7 ms: 1.02x faster                                                |
| scimark_sor                | 127 ms                                                     | 125 ms: 1.02x faster                                                 |
| nbody                      | 88.3 ms                                                    | 86.4 ms: 1.02x faster                                                |
| regex_dna                  | 221 ms                                                     | 217 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 743 ms: 1.02x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                |
| telco                      | 8.41 ms                                                    | 8.27 ms: 1.02x faster                                                |
| hexiom                     | 6.30 ms                                                    | 6.20 ms: 1.01x faster                                                |
| mako                       | 11.2 ms                                                    | 11.1 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.11 ms                                                    | 7.02 ms: 1.01x faster                                                |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                |
| coverage                   | 93.1 ms                                                    | 92.3 ms: 1.01x faster                                                |
| logging_silent             | 105 ns                                                     | 104 ns: 1.00x faster                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                    | 23.6 ms: 1.02x slower                                                |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                         |

Benchmark hidden because not significant (3): pylint, comprehensions, tomli_loads
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.00x