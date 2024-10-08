# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_mem_10000
- machine: linux-x86_64
- commit hash: 398f45a
- commit date: 2024-08-13
- overall geometric mean: 1.03x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 301 ms: 1.10x slower                                                      |
| html5lib       | 67.2 ms                                                    | 70.0 ms: 1.04x slower                                                     |
| tornado_http   | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                      | 1.04x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 837 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                      |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                     |
| float          | 78.9 ms                                                    | 74.6 ms: 1.06x faster                                                     |
| pidigits       | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.06x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                     |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                     |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                      | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 154 ms: 1.05x faster                                                      |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 59.5 ms: 1.03x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                      |
| xml_etree_generate   | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.73 ms: 1.16x faster                                                     |
| django_template | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 61.2 ms: 1.19x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_10000-3.14.0a0-398f45a |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                     |
| deepcopy                   | 367 us                                                     | 261 us: 1.41x faster                                                      |
| scimark_fft                | 392 ms                                                     | 311 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                     |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                     |
| richards_super             | 57.4 ms                                                    | 46.3 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.49 ms: 1.17x faster                                                     |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 66.6 ms: 1.16x faster                                                     |
| mako                       | 11.2 ms                                                    | 9.73 ms: 1.16x faster                                                     |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 837 ms: 1.12x faster                                                      |
| pyflate                    | 484 ms                                                     | 433 ms: 1.12x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 301 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.3 ms: 1.11x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 110 ms: 1.11x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                                    |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                     |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                                      |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.81 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 546 ms: 1.08x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.2 ms: 1.07x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.75 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.0 ms: 1.06x faster                                                     |
| float                      | 78.9 ms                                                    | 74.6 ms: 1.06x faster                                                     |
| thrift                     | 823 us                                                     | 779 us: 1.06x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                                     |
| async_tree_io              | 939 ms                                                     | 892 ms: 1.05x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 154 ms: 1.05x faster                                                      |
| create_gc_cycles           | 1.82 ms                                                    | 1.74 ms: 1.04x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.56 us: 1.03x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 59.5 ms: 1.03x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                     |
| logging_silent             | 105 ns                                                     | 103 ns: 1.02x faster                                                      |
| pidigits                   | 191 ms                                                     | 188 ms: 1.02x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.95 sec: 1.02x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 86.1 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                      |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                                      |
| bench_thread_pool          | 834 us                                                     | 823 us: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                    |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                                      |
| asyncio_tcp                | 508 ms                                                     | 504 ms: 1.01x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.77 sec: 1.01x faster                                                    |
| pprint_safe_repr           | 758 ms                                                     | 753 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.11 ms                                                    | 7.14 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| tornado_http               | 94.6 ms                                                    | 95.6 ms: 1.01x slower                                                     |
| go                         | 145 ms                                                     | 147 ms: 1.01x slower                                                      |
| raytrace                   | 267 ms                                                     | 271 ms: 1.01x slower                                                      |
| regex_effbot               | 3.67 ms                                                    | 3.76 ms: 1.02x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.6 ms: 1.02x slower                                                     |
| async_generators           | 442 ms                                                     | 454 ms: 1.03x slower                                                      |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.03x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.37 ms: 1.04x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 172 us: 1.04x slower                                                      |
| html5lib                   | 67.2 ms                                                    | 70.0 ms: 1.04x slower                                                     |
| sympy_str                  | 282 ms                                                     | 297 ms: 1.05x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.9 ms: 1.06x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.40 ms: 1.06x slower                                                     |
| sympy_expand               | 473 ms                                                     | 504 ms: 1.07x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.83 ms: 1.08x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 25.8 ms: 1.09x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 171 ms: 1.10x slower                                                      |
| 2to3                       | 274 ms                                                     | 301 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 61.0 ms: 1.10x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.80 ms: 1.10x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 22.9 ms: 1.11x slower                                                     |
| pylint                     | 317 ms                                                     | 365 ms: 1.15x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 61.2 ms: 1.19x slower                                                     |
| generators                 | 29.6 ms                                                    | 35.2 ms: 1.19x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (5): json_loads, pickle_pure_python, comprehensions, docutils, json
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x