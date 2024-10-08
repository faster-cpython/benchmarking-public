# Results vs. 3.13.0b2

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 277 ms: 1.01x slower                                           |
| docutils       | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                         |
| html5lib       | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                      | 1.00x slower                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                           |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                           |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                           |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                   |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                          |
| float          | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                          |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                           |
| Geometric mean | (ref)                                                      | 1.07x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                          |
| regex_dna      | 221 ms                                                     | 219 ms: 1.01x faster                                           |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                          |
| regex_compile  | 137 ms                                                     | 143 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                      | 1.00x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                          |
| xml_etree_process   | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                          |
| xml_etree_parse     | 162 ms                                                     | 144 ms: 1.12x faster                                           |
| tomli_loads         | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                         |
| json_loads          | 28.9 us                                                    | 26.6 us: 1.09x faster                                          |
| xml_etree_iterparse | 107 ms                                                     | 99.1 ms: 1.08x faster                                          |
| json_dumps          | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                          |
| unpickle            | 15.1 us                                                    | 14.5 us: 1.04x faster                                          |
| unpickle_list       | 5.34 us                                                    | 5.17 us: 1.03x faster                                          |
| pickle_dict         | 34.8 us                                                    | 34.1 us: 1.02x faster                                          |
| pickle_list         | 5.11 us                                                    | 5.20 us: 1.02x slower                                          |
| Geometric mean      | (ref)                                                      | 1.06x faster                                                   |

Benchmark hidden because not significant (3): unpickle_pure_python, pickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                          |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                          |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                          |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                          |
| genshi_xml      | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                          |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.9 us: 1.48x faster                                          |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                           |
| scimark_fft                | 392 ms                                                     | 310 ms: 1.26x faster                                           |
| deepcopy_reduce            | 3.35 us                                                    | 2.66 us: 1.26x faster                                          |
| richards_super             | 57.4 ms                                                    | 46.9 ms: 1.22x faster                                          |
| richards                   | 50.9 ms                                                    | 42.6 ms: 1.19x faster                                          |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.42 ms: 1.19x faster                                          |
| crypto_pyaes               | 77.5 ms                                                    | 65.8 ms: 1.18x faster                                          |
| bpe_tokeniser              | 5.02 sec                                                   | 4.32 sec: 1.16x faster                                         |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                           |
| async_tree_none            | 378 ms                                                     | 331 ms: 1.14x faster                                           |
| spectral_norm              | 116 ms                                                     | 102 ms: 1.14x faster                                           |
| xml_etree_generate         | 87.4 ms                                                    | 77.2 ms: 1.13x faster                                          |
| xml_etree_process          | 61.2 ms                                                    | 54.4 ms: 1.12x faster                                          |
| xml_etree_parse            | 162 ms                                                     | 144 ms: 1.12x faster                                           |
| mako                       | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                          |
| telco                      | 8.41 ms                                                    | 7.56 ms: 1.11x faster                                          |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                         |
| pyflate                    | 484 ms                                                     | 439 ms: 1.10x faster                                           |
| async_tree_memoization_tg  | 444 ms                                                     | 403 ms: 1.10x faster                                           |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                         |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                           |
| nbody                      | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                          |
| float                      | 78.9 ms                                                    | 72.2 ms: 1.09x faster                                          |
| scimark_monte_carlo        | 69.2 ms                                                    | 63.3 ms: 1.09x faster                                          |
| coverage                   | 93.1 ms                                                    | 85.3 ms: 1.09x faster                                          |
| fannkuch                   | 402 ms                                                     | 369 ms: 1.09x faster                                           |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                          |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.09x faster                                           |
| sqlite_synth               | 2.99 us                                                    | 2.75 us: 1.09x faster                                          |
| json_loads                 | 28.9 us                                                    | 26.6 us: 1.09x faster                                          |
| async_tree_none_tg         | 336 ms                                                     | 310 ms: 1.08x faster                                           |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                          |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                           |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 570 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 549 ms: 1.07x faster                                           |
| json_dumps                 | 10.7 ms                                                    | 10.0 ms: 1.07x faster                                          |
| pprint_safe_repr           | 758 ms                                                     | 712 ms: 1.06x faster                                           |
| thrift                     | 823 us                                                     | 783 us: 1.05x faster                                           |
| gc_traversal               | 3.98 ms                                                    | 3.78 ms: 1.05x faster                                          |
| asyncio_tcp                | 508 ms                                                     | 485 ms: 1.05x faster                                           |
| meteor_contest             | 110 ms                                                     | 105 ms: 1.04x faster                                           |
| unpickle                   | 15.1 us                                                    | 14.5 us: 1.04x faster                                          |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                          |
| logging_format             | 6.47 us                                                    | 6.20 us: 1.04x faster                                          |
| html5lib                   | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                          |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.04x faster                                         |
| logging_silent             | 105 ns                                                     | 101 ns: 1.04x faster                                           |
| unpickle_list              | 5.34 us                                                    | 5.17 us: 1.03x faster                                          |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                           |
| chaos                      | 61.3 ms                                                    | 59.4 ms: 1.03x faster                                          |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                          |
| json                       | 5.31 ms                                                    | 5.19 ms: 1.02x faster                                          |
| pickle_dict                | 34.8 us                                                    | 34.1 us: 1.02x faster                                          |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                         |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                          |
| logging_simple             | 5.74 us                                                    | 5.66 us: 1.02x faster                                          |
| regex_dna                  | 221 ms                                                     | 219 ms: 1.01x faster                                           |
| create_gc_cycles           | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                          |
| deltablue                  | 3.25 ms                                                    | 3.23 ms: 1.01x faster                                          |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                          |
| 2to3                       | 274 ms                                                     | 277 ms: 1.01x slower                                           |
| pickle_list                | 5.11 us                                                    | 5.20 us: 1.02x slower                                          |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                          |
| comprehensions             | 16.6 us                                                    | 17.0 us: 1.02x slower                                          |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                          |
| sqlglot_parse              | 1.32 ms                                                    | 1.36 ms: 1.03x slower                                          |
| sqlglot_transpile          | 1.63 ms                                                    | 1.69 ms: 1.03x slower                                          |
| docutils                   | 2.83 sec                                                   | 2.93 sec: 1.04x slower                                         |
| raytrace                   | 267 ms                                                     | 277 ms: 1.04x slower                                           |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                           |
| regex_compile              | 137 ms                                                     | 143 ms: 1.05x slower                                           |
| sqlglot_normalize          | 110 ms                                                     | 116 ms: 1.05x slower                                           |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                           |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.07x slower                                           |
| nqueens                    | 81.4 ms                                                    | 86.7 ms: 1.07x slower                                          |
| bench_thread_pool          | 834 us                                                     | 890 us: 1.07x slower                                           |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                          |
| sqlglot_optimize           | 55.5 ms                                                    | 60.4 ms: 1.09x slower                                          |
| hexiom                     | 6.30 ms                                                    | 6.97 ms: 1.11x slower                                          |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.12x slower                                           |
| genshi_xml                 | 51.6 ms                                                    | 58.3 ms: 1.13x slower                                          |
| sympy_integrate            | 20.5 ms                                                    | 23.3 ms: 1.14x slower                                          |
| generators                 | 29.6 ms                                                    | 35.0 ms: 1.18x slower                                          |
| pylint                     | 317 ms                                                     | 375 ms: 1.18x slower                                           |
| bench_mp_pool              | 23.9 ms                                                    | 61.2 ms: 2.56x slower                                          |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                   |

Benchmark hidden because not significant (9): async_tree_io_tg, unpickle_pure_python, async_tree_io, tornado_http, pickle, dulwich_log, pycparser, pickle_pure_python, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241007-3.14.0a0-0e19ac7-JIT/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: unpack_sequence

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x