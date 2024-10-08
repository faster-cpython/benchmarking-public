# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_100
- machine: linux-x86_64
- commit hash: 11fa189
- commit date: 2024-08-13
- overall geometric mean: 1.04x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 293 ms: 1.07x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                  |
| html5lib       | 67.2 ms                                                    | 65.3 ms: 1.03x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 94.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 335 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 435 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                            |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                   |
| float          | 78.9 ms                                                    | 74.0 ms: 1.07x faster                                                   |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                                   |
| regex_dna      | 221 ms                                                     | 211 ms: 1.05x faster                                                    |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 153 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 103 ms: 1.05x faster                                                    |
| xml_etree_process    | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                   |
| xml_etree_generate   | 87.4 ms                                                    | 85.4 ms: 1.02x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 214 us: 1.02x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                                   |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                   |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.90 ms: 1.14x faster                                                   |
| django_template | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                                   |
| deepcopy                   | 367 us                                                     | 265 us: 1.39x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                                   |
| richards                   | 50.9 ms                                                    | 40.5 ms: 1.26x faster                                                   |
| richards_super             | 57.4 ms                                                    | 45.9 ms: 1.25x faster                                                   |
| scimark_fft                | 392 ms                                                     | 318 ms: 1.23x faster                                                    |
| spectral_norm              | 116 ms                                                     | 99.9 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.54 ms: 1.16x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.90 ms: 1.14x faster                                                   |
| gc_traversal               | 3.98 ms                                                    | 3.51 ms: 1.13x faster                                                   |
| async_tree_none            | 378 ms                                                     | 335 ms: 1.13x faster                                                    |
| tomli_loads                | 2.12 sec                                                   | 1.89 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 397 ms: 1.12x faster                                                    |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                    |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.6 ms: 1.11x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                    |
| fannkuch                   | 402 ms                                                     | 367 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 540 ms: 1.09x faster                                                    |
| coverage                   | 93.1 ms                                                    | 85.6 ms: 1.09x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.75 ms: 1.09x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                   |
| nbody                      | 88.3 ms                                                    | 81.7 ms: 1.08x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 872 ms: 1.07x faster                                                    |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                    |
| float                      | 78.9 ms                                                    | 74.0 ms: 1.07x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 435 ms: 1.06x faster                                                    |
| xml_etree_parse            | 162 ms                                                     | 153 ms: 1.05x faster                                                    |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.49 ms: 1.05x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.15 us: 1.05x faster                                                   |
| regex_dna                  | 221 ms                                                     | 211 ms: 1.05x faster                                                    |
| logging_silent             | 105 ns                                                     | 99.7 ns: 1.05x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 103 ms: 1.05x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.05x faster                                                   |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 59.0 ms: 1.04x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                                   |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.03x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 65.3 ms: 1.03x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 738 ms: 1.03x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.89 sec: 1.03x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.17 ms: 1.03x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 85.4 ms: 1.02x faster                                                   |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 214 us: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.6 ms: 1.02x faster                                                   |
| bench_thread_pool          | 834 us                                                     | 821 us: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                    |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                                    |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                   |
| json                       | 5.31 ms                                                    | 5.25 ms: 1.01x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 94.2 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| raytrace                   | 267 ms                                                     | 269 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.58 sec: 1.01x slower                                                  |
| docutils                   | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                  |
| django_template            | 34.8 ms                                                    | 35.4 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.32 ms                                                    | 1.35 ms: 1.02x slower                                                   |
| go                         | 145 ms                                                     | 148 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 165 us                                                     | 169 us: 1.03x slower                                                    |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                    |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| sympy_str                  | 282 ms                                                     | 296 ms: 1.05x slower                                                    |
| sqlglot_transpile          | 1.63 ms                                                    | 1.72 ms: 1.05x slower                                                   |
| nqueens                    | 81.4 ms                                                    | 85.7 ms: 1.05x slower                                                   |
| sympy_expand               | 473 ms                                                     | 505 ms: 1.07x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 25.3 ms: 1.07x slower                                                   |
| 2to3                       | 274 ms                                                     | 293 ms: 1.07x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 59.6 ms: 1.07x slower                                                   |
| hexiom                     | 6.30 ms                                                    | 6.80 ms: 1.08x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 169 ms: 1.09x slower                                                    |
| genshi_xml                 | 51.6 ms                                                    | 56.3 ms: 1.09x slower                                                   |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.10x slower                                                   |
| pylint                     | 317 ms                                                     | 367 ms: 1.16x slower                                                    |
| generators                 | 29.6 ms                                                    | 34.8 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (4): async_tree_io, pickle_pure_python, comprehensions, pycparser
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x