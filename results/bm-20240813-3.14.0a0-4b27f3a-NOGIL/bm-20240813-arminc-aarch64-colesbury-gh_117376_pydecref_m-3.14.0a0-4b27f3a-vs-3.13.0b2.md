# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-aarch64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 513 ms: 1.68x slower                                                       |
| docutils       | 3.10 sec                                                     | 4.09 sec: 1.32x slower                                                     |
| html5lib       | 66.1 ms                                                      | 120 ms: 1.82x slower                                                       |
| tornado_http   | 128 ms                                                       | 206 ms: 1.61x slower                                                       |
| Geometric mean | (ref)                                                        | 1.60x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 683 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 867 ms: 1.14x slower                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.14x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 914 ms: 1.15x slower                                                       |
| async_tree_none_tg         | 476 ms                                                       | 557 ms: 1.17x slower                                                       |
| async_tree_none            | 492 ms                                                       | 607 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 208 ms: 2.27x slower                                                       |
| nbody          | 114 ms                                                       | 281 ms: 2.46x slower                                                       |
| Geometric mean | (ref)                                                        | 1.77x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.51 ms: 1.10x faster                                                      |
| regex_v8       | 31.1 ms                                                      | 33.4 ms: 1.08x slower                                                      |
| regex_compile  | 128 ms                                                       | 254 ms: 1.98x slower                                                       |
| Geometric mean | (ref)                                                        | 1.18x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 183 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 147 ms                                                       | 158 ms: 1.08x slower                                                       |
| json_loads           | 32.1 us                                                      | 39.1 us: 1.22x slower                                                      |
| json_dumps           | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                      |
| xml_etree_generate   | 114 ms                                                       | 161 ms: 1.42x slower                                                       |
| xml_etree_process    | 80.8 ms                                                      | 131 ms: 1.62x slower                                                       |
| tomli_loads          | 2.57 sec                                                     | 4.20 sec: 1.63x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 541 us: 2.15x slower                                                       |
| pickle_pure_python   | 359 us                                                       | 783 us: 2.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.46x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 17.8 ms: 1.37x slower                                                      |
| python_startup_no_site | 8.60 ms                                                      | 11.9 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.38x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 104 ms: 1.73x slower                                                       |
| django_template | 42.3 ms                                                      | 82.2 ms: 1.94x slower                                                      |
| genshi_text     | 27.4 ms                                                      | 53.9 ms: 1.97x slower                                                      |
| mako            | 13.2 ms                                                      | 29.0 ms: 2.20x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.95x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.44 ms: 1.51x faster                                                      |
| create_gc_cycles           | 2.33 ms                                                      | 1.61 ms: 1.45x faster                                                      |
| regex_effbot               | 4.98 ms                                                      | 4.51 ms: 1.10x faster                                                      |
| xml_etree_parse            | 191 ms                                                       | 183 ms: 1.05x faster                                                       |
| bench_mp_pool              | 7.03 ms                                                      | 6.91 ms: 1.02x faster                                                      |
| asyncio_websockets         | 657 ms                                                       | 668 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 1.27 sec                                                     | 1.34 sec: 1.05x slower                                                     |
| regex_v8                   | 31.1 ms                                                      | 33.4 ms: 1.08x slower                                                      |
| xml_etree_iterparse        | 147 ms                                                       | 158 ms: 1.08x slower                                                       |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.43 sec: 1.10x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 683 ms: 1.13x slower                                                       |
| asyncio_tcp                | 584 ms                                                       | 661 ms: 1.13x slower                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 867 ms: 1.14x slower                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.14x slower                                                     |
| async_tree_memoization     | 645 ms                                                       | 739 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 914 ms: 1.15x slower                                                       |
| pathlib                    | 22.8 ms                                                      | 26.4 ms: 1.16x slower                                                      |
| async_tree_none_tg         | 476 ms                                                       | 557 ms: 1.17x slower                                                       |
| json_loads                 | 32.1 us                                                      | 39.1 us: 1.22x slower                                                      |
| async_tree_none            | 492 ms                                                       | 607 ms: 1.23x slower                                                       |
| deepcopy                   | 448 us                                                       | 560 us: 1.25x slower                                                       |
| json                       | 5.64 ms                                                      | 7.09 ms: 1.26x slower                                                      |
| telco                      | 10.0 ms                                                      | 12.8 ms: 1.28x slower                                                      |
| scimark_fft                | 445 ms                                                       | 572 ms: 1.28x slower                                                       |
| mdp                        | 3.33 sec                                                     | 4.32 sec: 1.30x slower                                                     |
| docutils                   | 3.10 sec                                                     | 4.09 sec: 1.32x slower                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.79 ms: 1.34x slower                                                      |
| coverage                   | 98.4 ms                                                      | 132 ms: 1.35x slower                                                       |
| coroutines                 | 29.0 ms                                                      | 39.1 ms: 1.35x slower                                                      |
| json_dumps                 | 13.1 ms                                                      | 17.8 ms: 1.36x slower                                                      |
| async_generators           | 488 ms                                                       | 668 ms: 1.37x slower                                                       |
| python_startup             | 13.0 ms                                                      | 17.8 ms: 1.37x slower                                                      |
| python_startup_no_site     | 8.60 ms                                                      | 11.9 ms: 1.38x slower                                                      |
| xml_etree_generate         | 114 ms                                                       | 161 ms: 1.42x slower                                                       |
| deepcopy_memo              | 50.8 us                                                      | 72.5 us: 1.43x slower                                                      |
| deepcopy_reduce            | 4.04 us                                                      | 6.00 us: 1.49x slower                                                      |
| meteor_contest             | 113 ms                                                       | 169 ms: 1.49x slower                                                       |
| pylint                     | 337 ms                                                       | 507 ms: 1.50x slower                                                       |
| generators                 | 37.1 ms                                                      | 56.6 ms: 1.52x slower                                                      |
| nqueens                    | 98.9 ms                                                      | 151 ms: 1.53x slower                                                       |
| tornado_http               | 128 ms                                                       | 206 ms: 1.61x slower                                                       |
| spectral_norm              | 141 ms                                                       | 227 ms: 1.61x slower                                                       |
| xml_etree_process          | 80.8 ms                                                      | 131 ms: 1.62x slower                                                       |
| bpe_tokeniser              | 5.83 sec                                                     | 9.51 sec: 1.63x slower                                                     |
| tomli_loads                | 2.57 sec                                                     | 4.20 sec: 1.63x slower                                                     |
| fannkuch                   | 451 ms                                                       | 738 ms: 1.64x slower                                                       |
| crypto_pyaes               | 82.0 ms                                                      | 136 ms: 1.66x slower                                                       |
| sympy_integrate            | 20.9 ms                                                      | 34.8 ms: 1.67x slower                                                      |
| bench_thread_pool          | 1.26 ms                                                      | 2.11 ms: 1.68x slower                                                      |
| 2to3                       | 305 ms                                                       | 513 ms: 1.68x slower                                                       |
| pycparser                  | 1.22 sec                                                     | 2.06 sec: 1.69x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 104 ms: 1.73x slower                                                       |
| thrift                     | 962 us                                                       | 1.70 ms: 1.77x slower                                                      |
| sqlglot_normalize          | 129 ms                                                       | 230 ms: 1.78x slower                                                       |
| typing_runtime_protocols   | 193 us                                                       | 347 us: 1.79x slower                                                       |
| pyflate                    | 557 ms                                                       | 1.01 sec: 1.81x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 120 ms: 1.82x slower                                                       |
| sqlglot_optimize           | 62.6 ms                                                      | 116 ms: 1.85x slower                                                       |
| pprint_pformat             | 1.93 sec                                                     | 3.61 sec: 1.87x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 1.75 sec: 1.88x slower                                                     |
| django_template            | 42.3 ms                                                      | 82.2 ms: 1.94x slower                                                      |
| sympy_str                  | 265 ms                                                       | 516 ms: 1.94x slower                                                       |
| genshi_text                | 27.4 ms                                                      | 53.9 ms: 1.97x slower                                                      |
| regex_compile              | 128 ms                                                       | 254 ms: 1.98x slower                                                       |
| logging_format             | 7.82 us                                                      | 15.6 us: 1.99x slower                                                      |
| logging_simple             | 7.21 us                                                      | 14.4 us: 1.99x slower                                                      |
| comprehensions             | 20.5 us                                                      | 41.0 us: 2.00x slower                                                      |
| richards                   | 55.9 ms                                                      | 116 ms: 2.07x slower                                                       |
| sympy_expand               | 457 ms                                                       | 952 ms: 2.08x slower                                                       |
| logging_silent             | 133 ns                                                       | 279 ns: 2.09x slower                                                       |
| scimark_monte_carlo        | 82.3 ms                                                      | 173 ms: 2.10x slower                                                       |
| scimark_sor                | 159 ms                                                       | 336 ms: 2.11x slower                                                       |
| unpickle_pure_python       | 251 us                                                       | 541 us: 2.15x slower                                                       |
| pickle_pure_python         | 359 us                                                       | 783 us: 2.18x slower                                                       |
| sympy_sum                  | 144 ms                                                       | 316 ms: 2.20x slower                                                       |
| mako                       | 13.2 ms                                                      | 29.0 ms: 2.20x slower                                                      |
| hexiom                     | 7.08 ms                                                      | 15.6 ms: 2.21x slower                                                      |
| richards_super             | 62.3 ms                                                      | 140 ms: 2.25x slower                                                       |
| float                      | 91.4 ms                                                      | 208 ms: 2.27x slower                                                       |
| chaos                      | 68.3 ms                                                      | 158 ms: 2.31x slower                                                       |
| nbody                      | 114 ms                                                       | 281 ms: 2.46x slower                                                       |
| scimark_lu                 | 141 ms                                                       | 353 ms: 2.50x slower                                                       |
| sqlglot_transpile          | 1.71 ms                                                      | 4.30 ms: 2.51x slower                                                      |
| sqlglot_parse              | 1.42 ms                                                      | 3.59 ms: 2.52x slower                                                      |
| raytrace                   | 297 ms                                                       | 803 ms: 2.71x slower                                                       |
| go                         | 161 ms                                                       | 442 ms: 2.75x slower                                                       |
| deltablue                  | 3.88 ms                                                      | 12.5 ms: 3.24x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.56x slower                                                               |

Benchmark hidden because not significant (2): pidigits, regex_dna
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.42x
- 95% likely to have a slowdown of 1.39x
- 99% likely to have a slowdown of 1.34x

# Memory
- memory change: 1.16x