# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 2bab2aa
- commit date: 2024-07-09
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                  |
| html5lib       | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                    |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                   |
| nbody          | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                   |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                   |
| regex_dna      | 221 ms                                                     | 229 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 99.0 ms: 1.08x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 206 us: 1.06x faster                                                    |
| json_loads           | 28.9 us                                                    | 27.4 us: 1.05x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 297 us: 1.03x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                   |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.3 us: 1.45x faster                                                   |
| deepcopy                   | 367 us                                                     | 271 us: 1.35x faster                                                    |
| richards                   | 50.9 ms                                                    | 39.8 ms: 1.28x faster                                                   |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                   |
| richards_super             | 57.4 ms                                                    | 45.7 ms: 1.26x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 58.2 ms: 1.19x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.46 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 377 ms: 1.18x faster                                                    |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.17x faster                                                    |
| mako                       | 11.2 ms                                                    | 9.82 ms: 1.14x faster                                                   |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 406 ms: 1.14x faster                                                    |
| float                      | 78.9 ms                                                    | 69.9 ms: 1.13x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.52 ms: 1.13x faster                                                   |
| pyflate                    | 484 ms                                                     | 429 ms: 1.13x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 68.8 ms: 1.13x faster                                                   |
| fannkuch                   | 402 ms                                                     | 357 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 299 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 846 ms: 1.11x faster                                                    |
| async_tree_io              | 939 ms                                                     | 852 ms: 1.10x faster                                                    |
| nbody                      | 88.3 ms                                                    | 80.2 ms: 1.10x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 694 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.0 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.44 sec: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.97 sec: 1.08x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 568 ms: 1.08x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.04 us: 1.07x faster                                                   |
| logging_silent             | 105 ns                                                     | 98.0 ns: 1.07x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 82.3 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.94 ms: 1.06x faster                                                   |
| unpickle_pure_python       | 218 us                                                     | 206 us: 1.06x faster                                                    |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.05x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.80 sec: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                   |
| json                       | 5.31 ms                                                    | 5.11 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.27 ms: 1.04x faster                                                   |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 65.1 ms: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                                    |
| pickle_pure_python         | 305 us                                                     | 297 us: 1.03x faster                                                    |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 92.6 ms: 1.02x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.60 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                  |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.01x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                                    |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                    |
| chaos                      | 61.3 ms                                                    | 61.0 ms: 1.01x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 831 us: 1.00x faster                                                    |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| dulwich_log                | 67.2 ms                                                    | 67.4 ms: 1.00x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.00x slower                                                    |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| coverage                   | 93.1 ms                                                    | 93.9 ms: 1.01x slower                                                   |
| coroutines                 | 23.2 ms                                                    | 23.5 ms: 1.02x slower                                                   |
| async_generators           | 442 ms                                                     | 450 ms: 1.02x slower                                                    |
| regex_effbot               | 3.67 ms                                                    | 3.74 ms: 1.02x slower                                                   |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.90 sec: 1.02x slower                                                  |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 165 us                                                     | 170 us: 1.03x slower                                                    |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 84.6 ms: 1.04x slower                                                   |
| sympy_str                  | 282 ms                                                     | 294 ms: 1.04x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.58 ms: 1.04x slower                                                   |
| sympy_expand               | 473 ms                                                     | 498 ms: 1.05x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 128 ms: 1.05x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 166 ms: 1.07x slower                                                    |
| pylint                     | 317 ms                                                     | 339 ms: 1.07x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.0 ms: 1.07x slower                                                   |
| deltablue                  | 3.25 ms                                                    | 3.52 ms: 1.08x slower                                                   |
| genshi_text                | 23.7 ms                                                    | 26.0 ms: 1.10x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (6): pycparser, regex_compile, 2to3, sqlglot_optimize, generators, comprehensions
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x