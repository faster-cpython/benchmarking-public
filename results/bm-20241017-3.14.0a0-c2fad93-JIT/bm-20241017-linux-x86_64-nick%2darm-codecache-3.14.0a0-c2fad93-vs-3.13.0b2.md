# Results vs. 3.13.0b2

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.02x slower                                           |
| docutils       | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                         |
| html5lib       | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                          |
| tornado_http   | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                      | 1.01x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.15x faster                                           |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                           |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                           |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 561 ms: 1.05x faster                                           |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                          |
| float          | 78.9 ms                                                    | 74.3 ms: 1.06x faster                                          |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.07x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 138 ms: 1.01x slower                                           |
| regex_dna      | 221 ms                                                     | 229 ms: 1.03x slower                                           |
| regex_effbot   | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                          |
| regex_v8       | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                      | 1.04x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                          |
| xml_etree_generate   | 87.4 ms                                                    | 78.6 ms: 1.11x faster                                          |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                           |
| tomli_loads          | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                         |
| xml_etree_iterparse  | 107 ms                                                     | 99.5 ms: 1.08x faster                                          |
| json_loads           | 28.9 us                                                    | 26.8 us: 1.08x faster                                          |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                          |
| unpickle_list        | 5.34 us                                                    | 5.11 us: 1.05x faster                                          |
| unpickle             | 15.1 us                                                    | 14.6 us: 1.03x faster                                          |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                           |
| pickle_pure_python   | 305 us                                                     | 304 us: 1.01x faster                                           |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.00x faster                                          |
| pickle_dict          | 34.8 us                                                    | 35.0 us: 1.01x slower                                          |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                          |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                          |
| python_startup         | 10.8 ms                                                    | 11.9 ms: 1.10x slower                                          |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                          |
| django_template | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                          |
| genshi_text     | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                          |
| genshi_xml      | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                          |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.8 us: 1.48x faster                                          |
| deepcopy                   | 367 us                                                     | 262 us: 1.40x faster                                           |
| scimark_fft                | 392 ms                                                     | 303 ms: 1.29x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                          |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.40 ms: 1.20x faster                                          |
| richards                   | 50.9 ms                                                    | 42.6 ms: 1.19x faster                                          |
| crypto_pyaes               | 77.5 ms                                                    | 67.0 ms: 1.16x faster                                          |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.15x faster                                           |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                           |
| mako                       | 11.2 ms                                                    | 9.87 ms: 1.14x faster                                          |
| xml_etree_process          | 61.2 ms                                                    | 54.8 ms: 1.12x faster                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.51 sec: 1.11x faster                                         |
| nbody                      | 88.3 ms                                                    | 79.3 ms: 1.11x faster                                          |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                           |
| xml_etree_generate         | 87.4 ms                                                    | 78.6 ms: 1.11x faster                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                          |
| telco                      | 8.41 ms                                                    | 7.64 ms: 1.10x faster                                          |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                           |
| tomli_loads                | 2.12 sec                                                   | 1.93 sec: 1.10x faster                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 555 ms: 1.10x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                         |
| coverage                   | 93.1 ms                                                    | 84.9 ms: 1.10x faster                                          |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.10x faster                                          |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                           |
| go                         | 145 ms                                                     | 132 ms: 1.09x faster                                           |
| logging_silent             | 105 ns                                                     | 96.0 ns: 1.09x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 697 ms: 1.09x faster                                           |
| async_tree_memoization     | 463 ms                                                     | 429 ms: 1.08x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 99.5 ms: 1.08x faster                                          |
| json_loads                 | 28.9 us                                                    | 26.8 us: 1.08x faster                                          |
| pyflate                    | 484 ms                                                     | 453 ms: 1.07x faster                                           |
| sqlite_synth               | 2.99 us                                                    | 2.81 us: 1.06x faster                                          |
| float                      | 78.9 ms                                                    | 74.3 ms: 1.06x faster                                          |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.47 sec: 1.06x faster                                         |
| thrift                     | 823 us                                                     | 780 us: 1.05x faster                                           |
| logging_format             | 6.47 us                                                    | 6.14 us: 1.05x faster                                          |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                           |
| json                       | 5.31 ms                                                    | 5.06 ms: 1.05x faster                                          |
| async_tree_io              | 939 ms                                                     | 897 ms: 1.05x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 561 ms: 1.05x faster                                           |
| unpickle_list              | 5.34 us                                                    | 5.11 us: 1.05x faster                                          |
| html5lib                   | 67.2 ms                                                    | 64.4 ms: 1.04x faster                                          |
| spectral_norm              | 116 ms                                                     | 111 ms: 1.04x faster                                           |
| fannkuch                   | 402 ms                                                     | 385 ms: 1.04x faster                                           |
| unpickle                   | 15.1 us                                                    | 14.6 us: 1.03x faster                                          |
| chaos                      | 61.3 ms                                                    | 59.5 ms: 1.03x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.58 us: 1.03x faster                                          |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                           |
| scimark_sor                | 127 ms                                                     | 124 ms: 1.03x faster                                           |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.03x faster                                          |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                           |
| asyncio_tcp                | 508 ms                                                     | 498 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                         |
| asyncio_websockets         | 567 ms                                                     | 559 ms: 1.01x faster                                           |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                           |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                          |
| pickle_pure_python         | 305 us                                                     | 304 us: 1.01x faster                                           |
| python_startup_no_site     | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                          |
| dulwich_log                | 67.2 ms                                                    | 66.9 ms: 1.00x faster                                          |
| pickle_list                | 5.11 us                                                    | 5.08 us: 1.00x faster                                          |
| tornado_http               | 94.6 ms                                                    | 94.9 ms: 1.00x slower                                          |
| pickle_dict                | 34.8 us                                                    | 35.0 us: 1.01x slower                                          |
| regex_compile              | 137 ms                                                     | 138 ms: 1.01x slower                                           |
| 2to3                       | 274 ms                                                     | 278 ms: 1.02x slower                                           |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                          |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                          |
| comprehensions             | 16.6 us                                                    | 17.1 us: 1.03x slower                                          |
| regex_dna                  | 221 ms                                                     | 229 ms: 1.03x slower                                           |
| regex_effbot               | 3.67 ms                                                    | 3.81 ms: 1.04x slower                                          |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                           |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                           |
| docutils                   | 2.83 sec                                                   | 2.96 sec: 1.05x slower                                         |
| async_generators           | 442 ms                                                     | 463 ms: 1.05x slower                                           |
| pycparser                  | 1.16 sec                                                   | 1.22 sec: 1.05x slower                                         |
| django_template            | 34.8 ms                                                    | 36.7 ms: 1.05x slower                                          |
| genshi_text                | 23.7 ms                                                    | 25.0 ms: 1.06x slower                                          |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                           |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.07x slower                                           |
| regex_v8                   | 25.1 ms                                                    | 26.8 ms: 1.07x slower                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 59.7 ms: 1.07x slower                                          |
| bench_thread_pool          | 834 us                                                     | 897 us: 1.08x slower                                           |
| gc_traversal               | 3.98 ms                                                    | 4.29 ms: 1.08x slower                                          |
| nqueens                    | 81.4 ms                                                    | 89.3 ms: 1.10x slower                                          |
| python_startup             | 10.8 ms                                                    | 11.9 ms: 1.10x slower                                          |
| hexiom                     | 6.30 ms                                                    | 6.99 ms: 1.11x slower                                          |
| sympy_sum                  | 156 ms                                                     | 176 ms: 1.13x slower                                           |
| sympy_integrate            | 20.5 ms                                                    | 23.4 ms: 1.14x slower                                          |
| genshi_xml                 | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                          |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                           |
| generators                 | 29.6 ms                                                    | 35.4 ms: 1.19x slower                                          |
| create_gc_cycles           | 1.82 ms                                                    | 2.60 ms: 1.43x slower                                          |
| bench_mp_pool              | 23.9 ms                                                    | 84.4 ms: 3.53x slower                                          |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                   |

Benchmark hidden because not significant (2): sqlglot_parse, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-linux-x86_64-nick%2darm-codecache-3.14.0a0-c2fad93.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x