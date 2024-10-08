# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 268 ms: 1.02x faster                                                  |
| html5lib       | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 92.1 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| async_tree_io              | 939 ms                                                     | 844 ms: 1.11x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 847 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.13x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 75.6 ms: 1.17x faster                                                 |
| float          | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                 |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.03x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                 |
| regex_dna      | 221 ms                                                     | 230 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 99.0 ms: 1.08x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 81.7 ms: 1.07x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                 |
| json_loads           | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 295 us: 1.04x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                 |
| django_template | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 55.6 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 27.9 us: 1.42x faster                                                 |
| deepcopy                   | 367 us                                                     | 269 us: 1.36x faster                                                  |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                 |
| richards_super             | 57.4 ms                                                    | 45.8 ms: 1.25x faster                                                 |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.75 us: 1.22x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                  |
| nbody                      | 88.3 ms                                                    | 75.6 ms: 1.17x faster                                                 |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                 |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.57 ms: 1.15x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.6 ms: 1.14x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 407 ms: 1.14x faster                                                  |
| float                      | 78.9 ms                                                    | 69.7 ms: 1.13x faster                                                 |
| pyflate                    | 484 ms                                                     | 429 ms: 1.13x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                  |
| spectral_norm              | 116 ms                                                     | 104 ms: 1.12x faster                                                  |
| async_tree_io              | 939 ms                                                     | 844 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                |
| async_tree_io_tg           | 936 ms                                                     | 847 ms: 1.11x faster                                                  |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.56 sec: 1.09x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 99.0 ms: 1.08x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                 |
| logging_format             | 6.47 us                                                    | 5.99 us: 1.08x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 81.7 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 710 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.46 sec: 1.07x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 57.7 ms: 1.06x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.42 us: 1.06x faster                                                 |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                  |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                 |
| sqlglot_parse              | 1.32 ms                                                    | 1.26 ms: 1.05x faster                                                 |
| json                       | 5.31 ms                                                    | 5.09 ms: 1.04x faster                                                 |
| json_loads                 | 28.9 us                                                    | 27.7 us: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.84 sec: 1.04x faster                                                |
| pycparser                  | 1.16 sec                                                   | 1.12 sec: 1.04x faster                                                |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.04x faster                                                  |
| regex_compile              | 137 ms                                                     | 132 ms: 1.03x faster                                                  |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                  |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                  |
| tornado_http               | 94.6 ms                                                    | 92.1 ms: 1.03x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 65.4 ms: 1.03x faster                                                 |
| go                         | 145 ms                                                     | 141 ms: 1.03x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.88 ms: 1.02x faster                                                 |
| thrift                     | 823 us                                                     | 804 us: 1.02x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.02x faster                                                 |
| telco                      | 8.41 ms                                                    | 8.23 ms: 1.02x faster                                                 |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                     | 268 ms: 1.02x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.01x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 54.9 ms: 1.01x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                 |
| coverage                   | 93.1 ms                                                    | 92.5 ms: 1.01x faster                                                 |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                 |
| raytrace                   | 267 ms                                                     | 268 ms: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 110 ms                                                     | 111 ms: 1.01x slower                                                  |
| logging_silent             | 105 ns                                                     | 107 ns: 1.02x slower                                                  |
| sympy_str                  | 282 ms                                                     | 289 ms: 1.02x slower                                                  |
| hexiom                     | 6.30 ms                                                    | 6.45 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.02x slower                                                  |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                  |
| scimark_sor                | 127 ms                                                     | 131 ms: 1.03x slower                                                  |
| django_template            | 34.8 ms                                                    | 35.8 ms: 1.03x slower                                                 |
| sympy_expand               | 473 ms                                                     | 488 ms: 1.03x slower                                                  |
| scimark_lu                 | 122 ms                                                     | 126 ms: 1.04x slower                                                  |
| regex_dna                  | 221 ms                                                     | 230 ms: 1.04x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 163 ms: 1.05x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 21.7 ms: 1.06x slower                                                 |
| nqueens                    | 81.4 ms                                                    | 86.2 ms: 1.06x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 55.6 ms: 1.08x slower                                                 |
| deltablue                  | 3.25 ms                                                    | 3.55 ms: 1.09x slower                                                 |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (7): bench_thread_pool, docutils, dulwich_log, generators, coroutines, genshi_text, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x