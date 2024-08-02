# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: optimizer_off
- machine: linux-x86_64
- commit hash: 118726c
- commit date: 2024-06-29
- overall geometric mean: 1.04x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 272 ms: 1.01x faster                                                     |
| docutils       | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                   |
| html5lib       | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                    |
| tornado_http   | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                     |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 841 ms: 1.11x faster                                                     |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                      | 1.12x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                    |
| nbody          | 88.3 ms                                                    | 84.2 ms: 1.05x faster                                                    |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                      | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                    |
| regex_compile  | 137 ms                                                     | 137 ms: 1.00x slower                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                    |
| regex_dna      | 221 ms                                                     | 232 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|---------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 107 ms                                                     | 98.1 ms: 1.10x faster                                                    |
| tomli_loads         | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                   |
| xml_etree_generate  | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                    |
| xml_etree_process   | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                                    |
| json_loads          | 28.9 us                                                    | 27.4 us: 1.06x faster                                                    |
| json_dumps          | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| Geometric mean      | (ref)                                                      | 1.06x faster                                                             |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.45 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                    |
| django_template | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                    |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                    |
| genshi_xml      | 51.6 ms                                                    | 57.5 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.7 us: 1.38x faster                                                    |
| deepcopy                   | 367 us                                                     | 273 us: 1.34x faster                                                     |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.76 us: 1.21x faster                                                    |
| richards_super             | 57.4 ms                                                    | 47.5 ms: 1.21x faster                                                    |
| scimark_fft                | 392 ms                                                     | 326 ms: 1.21x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 376 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                    |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 409 ms: 1.13x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 297 ms: 1.13x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 68.4 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 841 ms: 1.11x faster                                                     |
| async_tree_io              | 939 ms                                                     | 845 ms: 1.11x faster                                                     |
| float                      | 78.9 ms                                                    | 71.2 ms: 1.11x faster                                                    |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.0 ms: 1.10x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 98.1 ms: 1.10x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.94 sec: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 539 ms: 1.09x faster                                                     |
| spectral_norm              | 116 ms                                                     | 107 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 566 ms: 1.08x faster                                                     |
| xml_etree_generate         | 87.4 ms                                                    | 81.8 ms: 1.07x faster                                                    |
| pyflate                    | 484 ms                                                     | 455 ms: 1.06x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.3 ms: 1.06x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 57.5 ms: 1.06x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                                     |
| fannkuch                   | 402 ms                                                     | 380 ms: 1.06x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.76 ms: 1.06x faster                                                    |
| json_loads                 | 28.9 us                                                    | 27.4 us: 1.06x faster                                                    |
| logging_simple             | 5.74 us                                                    | 5.46 us: 1.05x faster                                                    |
| nbody                      | 88.3 ms                                                    | 84.2 ms: 1.05x faster                                                    |
| thrift                     | 823 us                                                     | 788 us: 1.04x faster                                                     |
| telco                      | 8.41 ms                                                    | 8.07 ms: 1.04x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.8 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.83 sec: 1.04x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 64.7 ms: 1.04x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.75 ms: 1.04x faster                                                    |
| json                       | 5.31 ms                                                    | 5.12 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.03x faster                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.02x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                   |
| dask                       | 369 ms                                                     | 362 ms: 1.02x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 92.8 ms: 1.02x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                     |
| pycparser                  | 1.16 sec                                                   | 1.14 sec: 1.01x faster                                                   |
| 2to3                       | 274 ms                                                     | 272 ms: 1.01x faster                                                     |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                    |
| generators                 | 29.6 ms                                                    | 29.7 ms: 1.00x slower                                                    |
| regex_compile              | 137 ms                                                     | 137 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                    |
| go                         | 145 ms                                                     | 145 ms: 1.01x slower                                                     |
| python_startup             | 10.8 ms                                                    | 10.9 ms: 1.01x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.86 sec: 1.01x slower                                                   |
| logging_silent             | 105 ns                                                     | 106 ns: 1.01x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 56.4 ms: 1.01x slower                                                    |
| raytrace                   | 267 ms                                                     | 271 ms: 1.02x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                    |
| scimark_lu                 | 122 ms                                                     | 124 ms: 1.02x slower                                                     |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                                    |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                     |
| django_template            | 34.8 ms                                                    | 35.9 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 171 us: 1.04x slower                                                     |
| sympy_str                  | 282 ms                                                     | 295 ms: 1.04x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.45 ms: 1.05x slower                                                    |
| regex_dna                  | 221 ms                                                     | 232 ms: 1.05x slower                                                     |
| scimark_sor                | 127 ms                                                     | 134 ms: 1.05x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                                    |
| sympy_expand               | 473 ms                                                     | 500 ms: 1.06x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.0 ms: 1.07x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.75 ms: 1.07x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 87.8 ms: 1.08x slower                                                    |
| sympy_sum                  | 156 ms                                                     | 168 ms: 1.08x slower                                                     |
| pylint                     | 317 ms                                                     | 344 ms: 1.08x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 57.5 ms: 1.11x slower                                                    |
| deltablue                  | 3.25 ms                                                    | 3.63 ms: 1.12x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                             |

Benchmark hidden because not significant (5): pickle_pure_python, dulwich_log, bench_thread_pool, coverage, unpickle_pure_python
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x