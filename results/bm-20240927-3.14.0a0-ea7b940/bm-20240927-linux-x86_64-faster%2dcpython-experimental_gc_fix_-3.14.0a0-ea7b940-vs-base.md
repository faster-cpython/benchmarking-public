# Results vs. base

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.00x faster
- HPT reliability: 93.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 268 ms: 1.05x slower                                                            |
| docutils       | 2.65 sec                                                              | 2.61 sec: 1.01x faster                                                          |
| html5lib       | 63.7 ms                                                               | 68.0 ms: 1.07x slower                                                           |
| tornado_http   | 90.1 ms                                                               | 91.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 883 ms                                                                | 650 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 874 ms                                                                | 656 ms: 1.33x faster                                                            |
| async_tree_memoization_tg  | 390 ms                                                                | 342 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 498 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 521 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 303 ms                                                                | 278 ms: 1.09x faster                                                            |
| async_tree_memoization     | 396 ms                                                                | 365 ms: 1.08x faster                                                            |
| async_tree_none            | 317 ms                                                                | 300 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| asyncio_websockets         | 555 ms                                                                | 560 ms: 1.01x slower                                                            |
| asyncio_tcp                | 472 ms                                                                | 479 ms: 1.02x slower                                                            |
| coroutines                 | 22.6 ms                                                               | 23.0 ms: 1.02x slower                                                           |
| async_generators           | 438 ms                                                                | 455 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.09x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| nbody          | 88.0 ms                                                               | 89.6 ms: 1.02x slower                                                           |
| float          | 77.1 ms                                                               | 94.2 ms: 1.22x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 237 ms                                                                | 229 ms: 1.04x faster                                                            |
| regex_effbot   | 3.87 ms                                                               | 3.77 ms: 1.03x faster                                                           |
| regex_compile  | 128 ms                                                                | 130 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_dict          | 34.6 us                                                               | 33.6 us: 1.03x faster                                                           |
| pickle               | 11.6 us                                                               | 11.4 us: 1.02x faster                                                           |
| pickle_list          | 5.14 us                                                               | 5.06 us: 1.02x faster                                                           |
| pickle_pure_python   | 303 us                                                                | 307 us: 1.01x slower                                                            |
| tomli_loads          | 2.09 sec                                                              | 2.13 sec: 1.02x slower                                                          |
| unpickle_pure_python | 216 us                                                                | 221 us: 1.02x slower                                                            |
| unpickle             | 14.7 us                                                               | 15.1 us: 1.03x slower                                                           |
| xml_etree_generate   | 85.3 ms                                                               | 87.9 ms: 1.03x slower                                                           |
| unpickle_list        | 5.16 us                                                               | 5.41 us: 1.05x slower                                                           |
| xml_etree_parse      | 155 ms                                                                | 163 ms: 1.05x slower                                                            |
| xml_etree_process    | 58.7 ms                                                               | 61.9 ms: 1.05x slower                                                           |
| xml_etree_iterparse  | 104 ms                                                                | 134 ms: 1.28x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                           |
| django_template | 34.5 ms                                                               | 34.2 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| genshi_xml      | 50.8 ms                                                               | 52.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240926-linux-x86_64-python-2c472d36b776636fb008-3.14.0a0-2c472d3 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 883 ms                                                                | 650 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 874 ms                                                                | 656 ms: 1.33x faster                                                            |
| pylint                     | 320 ms                                                                | 279 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 390 ms                                                                | 342 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed_tg | 559 ms                                                                | 498 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                                | 521 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 303 ms                                                                | 278 ms: 1.09x faster                                                            |
| async_tree_memoization     | 396 ms                                                                | 365 ms: 1.08x faster                                                            |
| async_tree_none            | 317 ms                                                                | 300 ms: 1.06x faster                                                            |
| regex_dna                  | 237 ms                                                                | 229 ms: 1.04x faster                                                            |
| json                       | 5.11 ms                                                               | 4.96 ms: 1.03x faster                                                           |
| pickle_dict                | 34.6 us                                                               | 33.6 us: 1.03x faster                                                           |
| regex_effbot               | 3.87 ms                                                               | 3.77 ms: 1.03x faster                                                           |
| telco                      | 8.52 ms                                                               | 8.33 ms: 1.02x faster                                                           |
| pickle                     | 11.6 us                                                               | 11.4 us: 1.02x faster                                                           |
| scimark_fft                | 364 ms                                                                | 357 ms: 1.02x faster                                                            |
| create_gc_cycles           | 1.73 ms                                                               | 1.70 ms: 1.02x faster                                                           |
| pickle_list                | 5.14 us                                                               | 5.06 us: 1.02x faster                                                           |
| genshi_text                | 22.7 ms                                                               | 22.3 ms: 1.02x faster                                                           |
| docutils                   | 2.65 sec                                                              | 2.61 sec: 1.01x faster                                                          |
| logging_simple             | 5.74 us                                                               | 5.66 us: 1.01x faster                                                           |
| django_template            | 34.5 ms                                                               | 34.2 ms: 1.01x faster                                                           |
| generators                 | 27.9 ms                                                               | 27.6 ms: 1.01x faster                                                           |
| crypto_pyaes               | 72.2 ms                                                               | 71.6 ms: 1.01x faster                                                           |
| unpack_sequence            | 45.9 ns                                                               | 45.6 ns: 1.01x faster                                                           |
| raytrace                   | 268 ms                                                                | 266 ms: 1.01x faster                                                            |
| hexiom                     | 6.29 ms                                                               | 6.25 ms: 1.01x faster                                                           |
| sympy_sum                  | 148 ms                                                                | 148 ms: 1.01x faster                                                            |
| dulwich_log                | 64.9 ms                                                               | 64.6 ms: 1.01x faster                                                           |
| sympy_integrate            | 19.6 ms                                                               | 19.6 ms: 1.00x faster                                                           |
| spectral_norm              | 114 ms                                                                | 114 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl            | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| bench_thread_pool          | 791 us                                                                | 793 us: 1.00x slower                                                            |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| thrift                     | 765 us                                                                | 769 us: 1.01x slower                                                            |
| sqlglot_normalize          | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| deepcopy_memo              | 30.4 us                                                               | 30.6 us: 1.01x slower                                                           |
| pprint_pformat             | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                          |
| scimark_sor                | 123 ms                                                                | 124 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 53.4 ms                                                               | 53.8 ms: 1.01x slower                                                           |
| asyncio_websockets         | 555 ms                                                                | 560 ms: 1.01x slower                                                            |
| deepcopy                   | 259 us                                                                | 262 us: 1.01x slower                                                            |
| typing_runtime_protocols   | 160 us                                                                | 161 us: 1.01x slower                                                            |
| pickle_pure_python         | 303 us                                                                | 307 us: 1.01x slower                                                            |
| pprint_safe_repr           | 710 ms                                                                | 718 ms: 1.01x slower                                                            |
| tornado_http               | 90.1 ms                                                               | 91.1 ms: 1.01x slower                                                           |
| comprehensions             | 16.6 us                                                               | 16.8 us: 1.01x slower                                                           |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| python_startup             | 10.5 ms                                                               | 10.7 ms: 1.01x slower                                                           |
| gc_traversal               | 3.84 ms                                                               | 3.89 ms: 1.01x slower                                                           |
| regex_compile              | 128 ms                                                                | 130 ms: 1.01x slower                                                            |
| tomli_loads                | 2.09 sec                                                              | 2.13 sec: 1.02x slower                                                          |
| pathlib                    | 15.9 ms                                                               | 16.2 ms: 1.02x slower                                                           |
| asyncio_tcp                | 472 ms                                                                | 479 ms: 1.02x slower                                                            |
| coroutines                 | 22.6 ms                                                               | 23.0 ms: 1.02x slower                                                           |
| sqlglot_parse              | 1.28 ms                                                               | 1.30 ms: 1.02x slower                                                           |
| nbody                      | 88.0 ms                                                               | 89.6 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                               | 11.3 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 216 us                                                                | 221 us: 1.02x slower                                                            |
| deltablue                  | 3.25 ms                                                               | 3.32 ms: 1.02x slower                                                           |
| unpickle                   | 14.7 us                                                               | 15.1 us: 1.03x slower                                                           |
| sqlglot_transpile          | 1.58 ms                                                               | 1.62 ms: 1.03x slower                                                           |
| xml_etree_generate         | 85.3 ms                                                               | 87.9 ms: 1.03x slower                                                           |
| genshi_xml                 | 50.8 ms                                                               | 52.6 ms: 1.03x slower                                                           |
| logging_silent             | 101 ns                                                                | 104 ns: 1.03x slower                                                            |
| async_generators           | 438 ms                                                                | 455 ms: 1.04x slower                                                            |
| pycparser                  | 1.13 sec                                                              | 1.18 sec: 1.04x slower                                                          |
| 2to3                       | 256 ms                                                                | 268 ms: 1.05x slower                                                            |
| pyflate                    | 458 ms                                                                | 480 ms: 1.05x slower                                                            |
| unpickle_list              | 5.16 us                                                               | 5.41 us: 1.05x slower                                                           |
| xml_etree_parse            | 155 ms                                                                | 163 ms: 1.05x slower                                                            |
| xml_etree_process          | 58.7 ms                                                               | 61.9 ms: 1.05x slower                                                           |
| html5lib                   | 63.7 ms                                                               | 68.0 ms: 1.07x slower                                                           |
| mdp                        | 2.51 sec                                                              | 2.71 sec: 1.08x slower                                                          |
| bpe_tokeniser              | 4.80 sec                                                              | 5.29 sec: 1.10x slower                                                          |
| float                      | 77.1 ms                                                               | 94.2 ms: 1.22x slower                                                           |
| xml_etree_iterparse        | 104 ms                                                                | 134 ms: 1.28x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (20): scimark_lu, scimark_sparse_mat_mult, nqueens, fannkuch, sympy_expand, deepcopy_reduce, json_loads, sympy_str, bench_mp_pool, richards_super, sqlite_synth, python_startup_no_site, richards, json_dumps, regex_v8, chaos, logging_format, scimark_monte_carlo, coverage, go

# HPT report

- Reliability score: 93.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x