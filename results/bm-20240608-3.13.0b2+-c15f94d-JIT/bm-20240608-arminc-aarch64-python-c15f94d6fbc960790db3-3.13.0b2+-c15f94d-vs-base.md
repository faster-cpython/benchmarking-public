# Results vs. base

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                                                                              | 362 ms: 1.18x slower                                                                                                    |
| chameleon      | 8.94 ms                                                                                                             | 9.09 ms: 1.02x slower                                                                                                   |
| docutils       | 3.09 sec                                                                                                            | 3.54 sec: 1.15x slower                                                                                                  |
| html5lib       | 66.1 ms                                                                                                             | 72.6 ms: 1.10x slower                                                                                                   |
| tornado_http   | 126 ms                                                                                                              | 142 ms: 1.13x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.11x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.22 sec: 1.04x faster                                                                                                  |
| async_tree_none            | 490 ms                                                                                                              | 507 ms: 1.03x slower                                                                                                    |
| async_tree_memoization     | 645 ms                                                                                                              | 668 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 792 ms                                                                                                              | 827 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 798 ms: 1.05x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (3): async_tree_io, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 91.9 ms                                                                                                             | 90.0 ms: 1.02x faster                                                                                                   |
| nbody          | 113 ms                                                                                                              | 114 ms: 1.01x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.00x faster                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 30.5 ms                                                                                                             | 30.2 ms: 1.01x faster                                                                                                   |
| regex_effbot   | 4.89 ms                                                                                                             | 4.97 ms: 1.01x slower                                                                                                   |
| regex_dna      | 249 ms                                                                                                              | 260 ms: 1.05x slower                                                                                                    |
| regex_compile  | 129 ms                                                                                                              | 178 ms: 1.38x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.10x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                                                                             | 13.0 ms: 1.04x faster                                                                                                   |
| xml_etree_parse      | 194 ms                                                                                                              | 187 ms: 1.04x faster                                                                                                    |
| xml_etree_generate   | 117 ms                                                                                                              | 113 ms: 1.03x faster                                                                                                    |
| xml_etree_process    | 81.7 ms                                                                                                             | 80.2 ms: 1.02x faster                                                                                                   |
| json_loads           | 32.0 us                                                                                                             | 32.3 us: 1.01x slower                                                                                                   |
| unpickle_list        | 6.47 us                                                                                                             | 6.59 us: 1.02x slower                                                                                                   |
| tomli_loads          | 2.54 sec                                                                                                            | 2.63 sec: 1.04x slower                                                                                                  |
| pickle_pure_python   | 368 us                                                                                                              | 398 us: 1.08x slower                                                                                                    |
| unpickle_pure_python | 253 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (5): pickle, pickle_list, pickle_dict, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                             | 15.5 ms: 1.18x slower                                                                                                   |
| python_startup_no_site | 8.71 ms                                                                                                             | 11.1 ms: 1.28x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                               | 1.23x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.5 ms                                                                                                             | 13.0 ms: 1.04x faster                                                                                                   |
| django_template | 42.7 ms                                                                                                             | 50.5 ms: 1.18x slower                                                                                                   |
| genshi_text     | 27.6 ms                                                                                                             | 33.9 ms: 1.23x slower                                                                                                   |
| genshi_xml      | 62.1 ms                                                                                                             | 82.6 ms: 1.33x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.17x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json | results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json |
|----------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.28 sec                                                                                                            | 1.22 sec: 1.04x faster                                                                                                  |
| mako                       | 13.5 ms                                                                                                             | 13.0 ms: 1.04x faster                                                                                                   |
| json_dumps                 | 13.5 ms                                                                                                             | 13.0 ms: 1.04x faster                                                                                                   |
| xml_etree_parse            | 194 ms                                                                                                              | 187 ms: 1.04x faster                                                                                                    |
| xml_etree_generate         | 117 ms                                                                                                              | 113 ms: 1.03x faster                                                                                                    |
| sqlite_synth               | 3.91 us                                                                                                             | 3.81 us: 1.02x faster                                                                                                   |
| float                      | 91.9 ms                                                                                                             | 90.0 ms: 1.02x faster                                                                                                   |
| deepcopy_memo              | 50.1 us                                                                                                             | 49.2 us: 1.02x faster                                                                                                   |
| xml_etree_process          | 81.7 ms                                                                                                             | 80.2 ms: 1.02x faster                                                                                                   |
| regex_v8                   | 30.5 ms                                                                                                             | 30.2 ms: 1.01x faster                                                                                                   |
| json_loads                 | 32.0 us                                                                                                             | 32.3 us: 1.01x slower                                                                                                   |
| nbody                      | 113 ms                                                                                                              | 114 ms: 1.01x slower                                                                                                    |
| regex_effbot               | 4.89 ms                                                                                                             | 4.97 ms: 1.01x slower                                                                                                   |
| coverage                   | 98.0 ms                                                                                                             | 99.5 ms: 1.02x slower                                                                                                   |
| chameleon                  | 8.94 ms                                                                                                             | 9.09 ms: 1.02x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.24 sec                                                                                                            | 2.28 sec: 1.02x slower                                                                                                  |
| unpickle_list              | 6.47 us                                                                                                             | 6.59 us: 1.02x slower                                                                                                   |
| create_gc_cycles           | 2.34 ms                                                                                                             | 2.39 ms: 1.02x slower                                                                                                   |
| pathlib                    | 22.6 ms                                                                                                             | 23.2 ms: 1.02x slower                                                                                                   |
| gc_traversal               | 5.04 ms                                                                                                             | 5.16 ms: 1.03x slower                                                                                                   |
| telco                      | 9.86 ms                                                                                                             | 10.1 ms: 1.03x slower                                                                                                   |
| logging_format             | 7.75 us                                                                                                             | 7.98 us: 1.03x slower                                                                                                   |
| scimark_fft                | 446 ms                                                                                                              | 460 ms: 1.03x slower                                                                                                    |
| async_tree_none            | 490 ms                                                                                                              | 507 ms: 1.03x slower                                                                                                    |
| fannkuch                   | 447 ms                                                                                                              | 462 ms: 1.03x slower                                                                                                    |
| meteor_contest             | 113 ms                                                                                                              | 117 ms: 1.03x slower                                                                                                    |
| async_tree_memoization     | 645 ms                                                                                                              | 668 ms: 1.04x slower                                                                                                    |
| bench_thread_pool          | 1.28 ms                                                                                                             | 1.33 ms: 1.04x slower                                                                                                   |
| tomli_loads                | 2.54 sec                                                                                                            | 2.63 sec: 1.04x slower                                                                                                  |
| logging_simple             | 7.06 us                                                                                                             | 7.35 us: 1.04x slower                                                                                                   |
| mdp                        | 3.31 sec                                                                                                            | 3.45 sec: 1.04x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 792 ms                                                                                                              | 827 ms: 1.04x slower                                                                                                    |
| regex_dna                  | 249 ms                                                                                                              | 260 ms: 1.05x slower                                                                                                    |
| spectral_norm              | 141 ms                                                                                                              | 147 ms: 1.05x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 761 ms                                                                                                              | 798 ms: 1.05x slower                                                                                                    |
| dask                       | 373 ms                                                                                                              | 392 ms: 1.05x slower                                                                                                    |
| logging_silent             | 132 ns                                                                                                              | 139 ns: 1.05x slower                                                                                                    |
| flaskblogging              | 4.87 ms                                                                                                             | 5.14 ms: 1.05x slower                                                                                                   |
| generators                 | 37.4 ms                                                                                                             | 39.7 ms: 1.06x slower                                                                                                   |
| async_generators           | 486 ms                                                                                                              | 522 ms: 1.07x slower                                                                                                    |
| asyncio_tcp                | 586 ms                                                                                                              | 630 ms: 1.08x slower                                                                                                    |
| pyflate                    | 554 ms                                                                                                              | 596 ms: 1.08x slower                                                                                                    |
| aiohttp                    | 1.22 ms                                                                                                             | 1.32 ms: 1.08x slower                                                                                                   |
| raytrace                   | 299 ms                                                                                                              | 322 ms: 1.08x slower                                                                                                    |
| pickle_pure_python         | 368 us                                                                                                              | 398 us: 1.08x slower                                                                                                    |
| scimark_sor                | 161 ms                                                                                                              | 175 ms: 1.09x slower                                                                                                    |
| crypto_pyaes               | 81.6 ms                                                                                                             | 88.8 ms: 1.09x slower                                                                                                   |
| typing_runtime_protocols   | 192 us                                                                                                              | 209 us: 1.09x slower                                                                                                    |
| unpickle_pure_python       | 253 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| gunicorn                   | 1.24 ms                                                                                                             | 1.36 ms: 1.10x slower                                                                                                   |
| html5lib                   | 66.1 ms                                                                                                             | 72.6 ms: 1.10x slower                                                                                                   |
| scimark_monte_carlo        | 81.6 ms                                                                                                             | 90.0 ms: 1.10x slower                                                                                                   |
| deepcopy                   | 448 us                                                                                                              | 495 us: 1.11x slower                                                                                                    |
| go                         | 161 ms                                                                                                              | 179 ms: 1.12x slower                                                                                                    |
| sqlglot_optimize           | 62.0 ms                                                                                                             | 69.3 ms: 1.12x slower                                                                                                   |
| sqlglot_normalize          | 127 ms                                                                                                              | 142 ms: 1.12x slower                                                                                                    |
| tornado_http               | 126 ms                                                                                                              | 142 ms: 1.13x slower                                                                                                    |
| sqlglot_parse              | 1.40 ms                                                                                                             | 1.58 ms: 1.13x slower                                                                                                   |
| pycparser                  | 1.21 sec                                                                                                            | 1.38 sec: 1.13x slower                                                                                                  |
| bench_mp_pool              | 7.22 ms                                                                                                             | 8.22 ms: 1.14x slower                                                                                                   |
| sqlglot_transpile          | 1.75 ms                                                                                                             | 2.01 ms: 1.14x slower                                                                                                   |
| docutils                   | 3.09 sec                                                                                                            | 3.54 sec: 1.15x slower                                                                                                  |
| comprehensions             | 20.1 us                                                                                                             | 23.1 us: 1.15x slower                                                                                                   |
| deepcopy_reduce            | 4.00 us                                                                                                             | 4.60 us: 1.15x slower                                                                                                   |
| nqueens                    | 99.7 ms                                                                                                             | 117 ms: 1.17x slower                                                                                                    |
| pprint_safe_repr           | 943 ms                                                                                                              | 1.11 sec: 1.18x slower                                                                                                  |
| dulwich_log                | 61.0 ms                                                                                                             | 71.8 ms: 1.18x slower                                                                                                   |
| python_startup             | 13.2 ms                                                                                                             | 15.5 ms: 1.18x slower                                                                                                   |
| deltablue                  | 3.85 ms                                                                                                             | 4.55 ms: 1.18x slower                                                                                                   |
| 2to3                       | 306 ms                                                                                                              | 362 ms: 1.18x slower                                                                                                    |
| django_template            | 42.7 ms                                                                                                             | 50.5 ms: 1.18x slower                                                                                                   |
| sympy_expand               | 462 ms                                                                                                              | 547 ms: 1.19x slower                                                                                                    |
| pprint_pformat             | 1.93 sec                                                                                                            | 2.32 sec: 1.20x slower                                                                                                  |
| sympy_str                  | 268 ms                                                                                                              | 323 ms: 1.21x slower                                                                                                    |
| sympy_integrate            | 21.0 ms                                                                                                             | 25.6 ms: 1.22x slower                                                                                                   |
| genshi_text                | 27.6 ms                                                                                                             | 33.9 ms: 1.23x slower                                                                                                   |
| pylint                     | 338 ms                                                                                                              | 421 ms: 1.25x slower                                                                                                    |
| mypy2                      | 759 ms                                                                                                              | 948 ms: 1.25x slower                                                                                                    |
| python_startup_no_site     | 8.71 ms                                                                                                             | 11.1 ms: 1.28x slower                                                                                                   |
| hexiom                     | 7.06 ms                                                                                                             | 9.05 ms: 1.28x slower                                                                                                   |
| sympy_sum                  | 143 ms                                                                                                              | 185 ms: 1.29x slower                                                                                                    |
| chaos                      | 67.8 ms                                                                                                             | 88.0 ms: 1.30x slower                                                                                                   |
| scimark_lu                 | 141 ms                                                                                                              | 184 ms: 1.30x slower                                                                                                    |
| genshi_xml                 | 62.1 ms                                                                                                             | 82.6 ms: 1.33x slower                                                                                                   |
| regex_compile              | 129 ms                                                                                                              | 178 ms: 1.38x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (16): pickle, coroutines, pickle_list, pickle_dict, pidigits, unpickle, richards, xml_etree_iterparse, thrift, asyncio_websockets, richards_super, json, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, scimark_sparse_mat_mult

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.09x