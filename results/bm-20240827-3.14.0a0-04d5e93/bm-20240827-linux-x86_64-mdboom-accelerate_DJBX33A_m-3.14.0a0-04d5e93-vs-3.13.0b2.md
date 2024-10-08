# Results vs. 3.13.0b2

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-x86_64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| docutils       | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                |
| html5lib       | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 90.5 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                      | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 894 ms: 1.05x faster                                                  |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                 |
| float          | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                 |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 131 ms: 1.05x faster                                                  |
| regex_dna      | 221 ms                                                     | 220 ms: 1.00x faster                                                  |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                 |
| regex_v8       | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| xml_etree_generate   | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 212 us: 1.03x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 303 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                 |
| django_template | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                 |
| genshi_xml      | 51.6 ms                                                    | 51.9 ms: 1.00x slower                                                 |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-linux-x86_64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                                  |
| deepcopy_memo              | 39.7 us                                                    | 29.3 us: 1.36x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                    | 2.69 us: 1.24x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 392 ms: 1.18x faster                                                  |
| async_tree_none            | 378 ms                                                     | 322 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.68 ms: 1.13x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 400 ms: 1.11x faster                                                  |
| richards_super             | 57.4 ms                                                    | 51.9 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 305 ms: 1.10x faster                                                  |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                |
| richards                   | 50.9 ms                                                    | 46.4 ms: 1.10x faster                                                 |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                                 |
| scimark_fft                | 392 ms                                                     | 360 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 561 ms: 1.09x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 543 ms: 1.08x faster                                                  |
| logging_silent             | 105 ns                                                     | 97.7 ns: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                     | 257 ms: 1.07x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 784 us: 1.06x faster                                                  |
| generators                 | 29.6 ms                                                    | 27.9 ms: 1.06x faster                                                 |
| thrift                     | 823 us                                                     | 774 us: 1.06x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.11 us: 1.06x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.44 us: 1.06x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.05x faster                                                 |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                                |
| sympy_sum                  | 156 ms                                                     | 148 ms: 1.05x faster                                                  |
| sympy_str                  | 282 ms                                                     | 268 ms: 1.05x faster                                                  |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                 |
| tomli_loads                | 2.12 sec                                                   | 2.02 sec: 1.05x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.5 ms: 1.05x faster                                                 |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 894 ms: 1.05x faster                                                  |
| regex_compile              | 137 ms                                                     | 131 ms: 1.05x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 74.0 ms: 1.05x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 19.6 ms: 1.05x faster                                                 |
| tornado_http               | 94.6 ms                                                    | 90.5 ms: 1.05x faster                                                 |
| xml_etree_parse            | 162 ms                                                     | 155 ms: 1.04x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.72 sec: 1.04x faster                                                |
| pyflate                    | 484 ms                                                     | 466 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 58.9 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.57 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 55.5 ms                                                    | 53.5 ms: 1.04x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                 |
| bpe_tokeniser              | 5.02 sec                                                   | 4.85 sec: 1.04x faster                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.28 ms: 1.03x faster                                                 |
| nbody                      | 88.3 ms                                                    | 85.5 ms: 1.03x faster                                                 |
| sympy_expand               | 473 ms                                                     | 458 ms: 1.03x faster                                                  |
| hexiom                     | 6.30 ms                                                    | 6.10 ms: 1.03x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                |
| sqlglot_normalize          | 110 ms                                                     | 107 ms: 1.03x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 85.0 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 212 us: 1.03x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                 |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| float                      | 78.9 ms                                                    | 77.1 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.6 ms: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                  |
| async_generators           | 442 ms                                                     | 433 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 105 ms: 1.02x faster                                                  |
| raytrace                   | 267 ms                                                     | 261 ms: 1.02x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                 |
| json_loads                 | 28.9 us                                                    | 28.3 us: 1.02x faster                                                 |
| json                       | 5.31 ms                                                    | 5.21 ms: 1.02x faster                                                 |
| asyncio_websockets         | 567 ms                                                     | 557 ms: 1.02x faster                                                  |
| genshi_text                | 23.7 ms                                                    | 23.3 ms: 1.02x faster                                                 |
| django_template            | 34.8 ms                                                    | 34.3 ms: 1.02x faster                                                 |
| nqueens                    | 81.4 ms                                                    | 80.4 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.9 ms: 1.01x faster                                                 |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 165 us                                                     | 163 us: 1.01x faster                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.04 ms: 1.01x faster                                                 |
| pickle_pure_python         | 305 us                                                     | 303 us: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                 |
| regex_dna                  | 221 ms                                                     | 220 ms: 1.00x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 51.9 ms: 1.00x slower                                                 |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                 |
| mako                       | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                 |
| fannkuch                   | 402 ms                                                     | 406 ms: 1.01x slower                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.04x slower                                                |
| regex_v8                   | 25.1 ms                                                    | 26.2 ms: 1.04x slower                                                 |
| go                         | 145 ms                                                     | 162 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                          |

Benchmark hidden because not significant (3): async_tree_io, telco, pylint
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x