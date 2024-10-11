# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                | 259 ms: 1.03x slower                                                     |
| docutils       | 2.63 sec                                                              | 2.66 sec: 1.01x slower                                                   |
| html5lib       | 61.4 ms                                                               | 62.5 ms: 1.02x slower                                                    |
| tornado_http   | 90.6 ms                                                               | 92.5 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                   |
| asyncio_tcp                | 477 ms                                                                | 483 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                                | 578 ms: 1.02x slower                                                     |
| async_generators           | 433 ms                                                                | 444 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                                | 560 ms: 1.03x slower                                                     |
| async_tree_io              | 933 ms                                                                | 960 ms: 1.03x slower                                                     |
| async_tree_none            | 323 ms                                                                | 334 ms: 1.04x slower                                                     |
| async_tree_none_tg         | 308 ms                                                                | 320 ms: 1.04x slower                                                     |
| coroutines                 | 23.4 ms                                                               | 25.3 ms: 1.08x slower                                                    |
| async_tree_memoization     | 391 ms                                                                | 427 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                     |
| float          | 77.6 ms                                                               | 79.4 ms: 1.02x slower                                                    |
| nbody          | 88.2 ms                                                               | 93.2 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 25.0 ms                                                               | 24.3 ms: 1.03x faster                                                    |
| regex_effbot   | 3.64 ms                                                               | 3.56 ms: 1.02x faster                                                    |
| regex_compile  | 127 ms                                                                | 131 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_list      | 5.42 us                                                               | 5.23 us: 1.04x faster                                                    |
| pickle             | 11.7 us                                                               | 11.4 us: 1.02x faster                                                    |
| pickle_list        | 5.15 us                                                               | 5.06 us: 1.02x faster                                                    |
| pickle_dict        | 34.6 us                                                               | 34.1 us: 1.01x faster                                                    |
| xml_etree_generate | 86.3 ms                                                               | 86.6 ms: 1.00x slower                                                    |
| xml_etree_process  | 59.8 ms                                                               | 60.3 ms: 1.01x slower                                                    |
| json_dumps         | 11.6 ms                                                               | 11.8 ms: 1.01x slower                                                    |
| tomli_loads        | 2.08 sec                                                              | 2.12 sec: 1.02x slower                                                   |
| pickle_pure_python | 306 us                                                                | 315 us: 1.03x slower                                                     |
| unpickle           | 14.5 us                                                               | 15.4 us: 1.06x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.01 ms                                                               | 7.03 ms: 1.00x slower                                                    |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 22.1 ms                                                               | 22.5 ms: 1.02x slower                                                    |
| mako            | 11.4 ms                                                               | 11.8 ms: 1.04x slower                                                    |
| django_template | 33.9 ms                                                               | 35.5 ms: 1.05x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241011-linux-x86_64-python-0135848059162ad81478-3.14.0a0-0135848 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_sparse_mat_mult    | 4.90 ms                                                               | 4.70 ms: 1.04x faster                                                    |
| gc_traversal               | 3.91 ms                                                               | 3.77 ms: 1.04x faster                                                    |
| unpickle_list              | 5.42 us                                                               | 5.23 us: 1.04x faster                                                    |
| regex_v8                   | 25.0 ms                                                               | 24.3 ms: 1.03x faster                                                    |
| regex_effbot               | 3.64 ms                                                               | 3.56 ms: 1.02x faster                                                    |
| pickle                     | 11.7 us                                                               | 11.4 us: 1.02x faster                                                    |
| pickle_list                | 5.15 us                                                               | 5.06 us: 1.02x faster                                                    |
| scimark_lu                 | 114 ms                                                                | 112 ms: 1.01x faster                                                     |
| pickle_dict                | 34.6 us                                                               | 34.1 us: 1.01x faster                                                    |
| create_gc_cycles           | 1.79 ms                                                               | 1.78 ms: 1.01x faster                                                    |
| unpack_sequence            | 46.9 ns                                                               | 46.6 ns: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                                | 188 ms: 1.00x slower                                                     |
| python_startup_no_site     | 7.01 ms                                                               | 7.03 ms: 1.00x slower                                                    |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                   |
| python_startup             | 10.5 ms                                                               | 10.6 ms: 1.00x slower                                                    |
| xml_etree_generate         | 86.3 ms                                                               | 86.6 ms: 1.00x slower                                                    |
| go                         | 120 ms                                                                | 121 ms: 1.00x slower                                                     |
| bench_mp_pool              | 55.9 ms                                                               | 56.2 ms: 1.00x slower                                                    |
| meteor_contest             | 107 ms                                                                | 108 ms: 1.00x slower                                                     |
| xml_etree_process          | 59.8 ms                                                               | 60.3 ms: 1.01x slower                                                    |
| hexiom                     | 6.27 ms                                                               | 6.32 ms: 1.01x slower                                                    |
| asyncio_tcp                | 477 ms                                                                | 483 ms: 1.01x slower                                                     |
| json_dumps                 | 11.6 ms                                                               | 11.8 ms: 1.01x slower                                                    |
| docutils                   | 2.63 sec                                                              | 2.66 sec: 1.01x slower                                                   |
| sympy_integrate            | 19.9 ms                                                               | 20.2 ms: 1.02x slower                                                    |
| genshi_text                | 22.1 ms                                                               | 22.5 ms: 1.02x slower                                                    |
| comprehensions             | 16.8 us                                                               | 17.1 us: 1.02x slower                                                    |
| sympy_sum                  | 148 ms                                                                | 151 ms: 1.02x slower                                                     |
| dulwich_log                | 64.2 ms                                                               | 65.4 ms: 1.02x slower                                                    |
| deepcopy                   | 261 us                                                                | 266 us: 1.02x slower                                                     |
| html5lib                   | 61.4 ms                                                               | 62.5 ms: 1.02x slower                                                    |
| deltablue                  | 3.23 ms                                                               | 3.29 ms: 1.02x slower                                                    |
| spectral_norm              | 111 ms                                                                | 114 ms: 1.02x slower                                                     |
| bench_thread_pool          | 841 us                                                                | 858 us: 1.02x slower                                                     |
| tornado_http               | 90.6 ms                                                               | 92.5 ms: 1.02x slower                                                    |
| tomli_loads                | 2.08 sec                                                              | 2.12 sec: 1.02x slower                                                   |
| richards                   | 46.3 ms                                                               | 47.3 ms: 1.02x slower                                                    |
| mdp                        | 2.56 sec                                                              | 2.61 sec: 1.02x slower                                                   |
| raytrace                   | 262 ms                                                                | 267 ms: 1.02x slower                                                     |
| float                      | 77.6 ms                                                               | 79.4 ms: 1.02x slower                                                    |
| sqlglot_normalize          | 107 ms                                                                | 109 ms: 1.02x slower                                                     |
| nqueens                    | 80.0 ms                                                               | 82.0 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 67.3 ms                                                               | 69.0 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                                | 578 ms: 1.02x slower                                                     |
| bpe_tokeniser              | 4.67 sec                                                              | 4.79 sec: 1.03x slower                                                   |
| pathlib                    | 15.9 ms                                                               | 16.3 ms: 1.03x slower                                                    |
| async_generators           | 433 ms                                                                | 444 ms: 1.03x slower                                                     |
| regex_compile              | 127 ms                                                                | 131 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                                | 560 ms: 1.03x slower                                                     |
| 2to3                       | 252 ms                                                                | 259 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                               | 1.63 ms: 1.03x slower                                                    |
| deepcopy_reduce            | 2.70 us                                                               | 2.78 us: 1.03x slower                                                    |
| thrift                     | 781 us                                                                | 802 us: 1.03x slower                                                     |
| telco                      | 7.85 ms                                                               | 8.06 ms: 1.03x slower                                                    |
| richards_super             | 52.5 ms                                                               | 54.0 ms: 1.03x slower                                                    |
| async_tree_io              | 933 ms                                                                | 960 ms: 1.03x slower                                                     |
| sqlglot_optimize           | 53.3 ms                                                               | 54.9 ms: 1.03x slower                                                    |
| pickle_pure_python         | 306 us                                                                | 315 us: 1.03x slower                                                     |
| typing_runtime_protocols   | 159 us                                                                | 164 us: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                               | 1.32 ms: 1.04x slower                                                    |
| async_tree_none            | 323 ms                                                                | 334 ms: 1.04x slower                                                     |
| sympy_str                  | 266 ms                                                                | 276 ms: 1.04x slower                                                     |
| mako                       | 11.4 ms                                                               | 11.8 ms: 1.04x slower                                                    |
| logging_simple             | 5.59 us                                                               | 5.80 us: 1.04x slower                                                    |
| sympy_expand               | 454 ms                                                                | 472 ms: 1.04x slower                                                     |
| async_tree_none_tg         | 308 ms                                                                | 320 ms: 1.04x slower                                                     |
| pyflate                    | 470 ms                                                                | 490 ms: 1.04x slower                                                     |
| fannkuch                   | 401 ms                                                                | 418 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.50 sec                                                              | 1.57 sec: 1.05x slower                                                   |
| pprint_safe_repr           | 730 ms                                                                | 763 ms: 1.05x slower                                                     |
| chaos                      | 59.3 ms                                                               | 62.1 ms: 1.05x slower                                                    |
| django_template            | 33.9 ms                                                               | 35.5 ms: 1.05x slower                                                    |
| logging_format             | 6.10 us                                                               | 6.40 us: 1.05x slower                                                    |
| crypto_pyaes               | 71.7 ms                                                               | 75.5 ms: 1.05x slower                                                    |
| scimark_sor                | 124 ms                                                                | 131 ms: 1.05x slower                                                     |
| nbody                      | 88.2 ms                                                               | 93.2 ms: 1.06x slower                                                    |
| pycparser                  | 1.13 sec                                                              | 1.20 sec: 1.06x slower                                                   |
| unpickle                   | 14.5 us                                                               | 15.4 us: 1.06x slower                                                    |
| coroutines                 | 23.4 ms                                                               | 25.3 ms: 1.08x slower                                                    |
| async_tree_memoization     | 391 ms                                                                | 427 ms: 1.09x slower                                                     |
| generators                 | 26.7 ms                                                               | 29.2 ms: 1.09x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (16): async_tree_io_tg, xml_etree_parse, logging_silent, sqlite_synth, deepcopy_memo, coverage, json_loads, asyncio_websockets, unpickle_pure_python, xml_etree_iterparse, regex_dna, json, genshi_xml, scimark_fft, pylint, async_tree_memoization_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x