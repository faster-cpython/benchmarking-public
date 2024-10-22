# Results vs. base

- fork: mpage
- ref: gh_115999_thread_loc
- machine: linux-x86_64
- commit hash: adb59ef
- commit date: 2024-10-04
- overall geometric mean: 1.01x faster
- HPT reliability: 99.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 391 ms                                                                | 393 ms: 1.00x slower                                                 |
| html5lib       | 95.2 ms                                                               | 93.9 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| coroutines                 | 31.6 ms                                                               | 30.1 ms: 1.05x faster                                                |
| async_generators           | 551 ms                                                                | 531 ms: 1.04x faster                                                 |
| async_tree_none            | 413 ms                                                                | 402 ms: 1.03x faster                                                 |
| async_tree_memoization     | 515 ms                                                                | 505 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 669 ms                                                                | 656 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 611 ms                                                                | 603 ms: 1.01x faster                                                 |
| async_tree_memoization_tg  | 462 ms                                                                | 457 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl            | 2.05 sec                                                              | 2.07 sec: 1.01x slower                                               |
| asyncio_tcp                | 553 ms                                                                | 558 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_io_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 224 ms                                                                | 189 ms: 1.19x faster                                                 |
| float          | 141 ms                                                                | 137 ms: 1.03x faster                                                 |
| pidigits       | 184 ms                                                                | 183 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.52 ms                                                               | 3.54 ms: 1.01x slower                                                |
| regex_dna      | 215 ms                                                                | 217 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads        | 3.24 sec                                                              | 3.17 sec: 1.02x faster                                               |
| json_dumps         | 13.1 ms                                                               | 12.8 ms: 1.02x faster                                                |
| xml_etree_parse    | 151 ms                                                                | 150 ms: 1.01x faster                                                 |
| xml_etree_process  | 87.3 ms                                                               | 86.8 ms: 1.00x faster                                                |
| xml_etree_generate | 109 ms                                                                | 108 ms: 1.00x faster                                                 |
| unpickle_list      | 5.47 us                                                               | 5.49 us: 1.00x slower                                                |
| json_loads         | 30.1 us                                                               | 30.3 us: 1.01x slower                                                |
| pickle             | 10.6 us                                                               | 10.7 us: 1.01x slower                                                |
| pickle_dict        | 32.7 us                                                               | 33.0 us: 1.01x slower                                                |
| pickle_list        | 4.68 us                                                               | 4.75 us: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.36 ms                                                               | 9.52 ms: 1.02x slower                                                |
| python_startup         | 14.0 ms                                                               | 14.3 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 20.8 ms                                                               | 20.7 ms: 1.01x faster                                                |
| django_template | 59.0 ms                                                               | 59.7 ms: 1.01x slower                                                |
| genshi_xml      | 81.3 ms                                                               | 83.2 ms: 1.02x slower                                                |
| genshi_text     | 38.9 ms                                                               | 39.9 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241005-linux-x86_64-python-a5fc50994a3fae46d0c3-3.14.0a0-a5fc509 | bm-20241004-linux-x86_64-mpage-gh_115999_thread_loc-3.14.0a0-adb59ef |
|----------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody                      | 224 ms                                                                | 189 ms: 1.19x faster                                                 |
| scimark_fft                | 487 ms                                                                | 422 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult    | 6.77 ms                                                               | 5.88 ms: 1.15x faster                                                |
| spectral_norm              | 186 ms                                                                | 163 ms: 1.14x faster                                                 |
| chaos                      | 122 ms                                                                | 112 ms: 1.09x faster                                                 |
| raytrace                   | 593 ms                                                                | 564 ms: 1.05x faster                                                 |
| scimark_sor                | 264 ms                                                                | 251 ms: 1.05x faster                                                 |
| coroutines                 | 31.6 ms                                                               | 30.1 ms: 1.05x faster                                                |
| async_generators           | 551 ms                                                                | 531 ms: 1.04x faster                                                 |
| fannkuch                   | 606 ms                                                                | 585 ms: 1.04x faster                                                 |
| coverage                   | 112 ms                                                                | 108 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 121 ms                                                                | 117 ms: 1.03x faster                                                 |
| float                      | 141 ms                                                                | 137 ms: 1.03x faster                                                 |
| bpe_tokeniser              | 6.52 sec                                                              | 6.34 sec: 1.03x faster                                               |
| scimark_lu                 | 228 ms                                                                | 221 ms: 1.03x faster                                                 |
| async_tree_none            | 413 ms                                                                | 402 ms: 1.03x faster                                                 |
| logging_format             | 11.5 us                                                               | 11.2 us: 1.03x faster                                                |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                               |
| tomli_loads                | 3.24 sec                                                              | 3.17 sec: 1.02x faster                                               |
| sqlglot_parse              | 2.65 ms                                                               | 2.60 ms: 1.02x faster                                                |
| async_tree_memoization     | 515 ms                                                                | 505 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 669 ms                                                                | 656 ms: 1.02x faster                                                 |
| json_dumps                 | 13.1 ms                                                               | 12.8 ms: 1.02x faster                                                |
| go                         | 272 ms                                                                | 267 ms: 1.02x faster                                                 |
| logging_simple             | 10.4 us                                                               | 10.2 us: 1.02x faster                                                |
| sqlglot_optimize           | 85.8 ms                                                               | 84.5 ms: 1.02x faster                                                |
| deltablue                  | 8.33 ms                                                               | 8.21 ms: 1.02x faster                                                |
| html5lib                   | 95.2 ms                                                               | 93.9 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed_tg | 611 ms                                                                | 603 ms: 1.01x faster                                                 |
| nqueens                    | 116 ms                                                                | 114 ms: 1.01x faster                                                 |
| telco                      | 10.0 ms                                                               | 9.92 ms: 1.01x faster                                                |
| comprehensions             | 28.7 us                                                               | 28.4 us: 1.01x faster                                                |
| async_tree_memoization_tg  | 462 ms                                                                | 457 ms: 1.01x faster                                                 |
| pathlib                    | 19.3 ms                                                               | 19.1 ms: 1.01x faster                                                |
| pprint_pformat             | 2.59 sec                                                              | 2.58 sec: 1.01x faster                                               |
| deepcopy_reduce            | 4.26 us                                                               | 4.23 us: 1.01x faster                                                |
| logging_silent             | 197 ns                                                                | 195 ns: 1.01x faster                                                 |
| hexiom                     | 11.8 ms                                                               | 11.7 ms: 1.01x faster                                                |
| xml_etree_parse            | 151 ms                                                                | 150 ms: 1.01x faster                                                 |
| mako                       | 20.8 ms                                                               | 20.7 ms: 1.01x faster                                                |
| xml_etree_process          | 87.3 ms                                                               | 86.8 ms: 1.00x faster                                                |
| xml_etree_generate         | 109 ms                                                                | 108 ms: 1.00x faster                                                 |
| pidigits                   | 184 ms                                                                | 183 ms: 1.00x faster                                                 |
| crypto_pyaes               | 111 ms                                                                | 110 ms: 1.00x faster                                                 |
| 2to3                       | 391 ms                                                                | 393 ms: 1.00x slower                                                 |
| unpickle_list              | 5.47 us                                                               | 5.49 us: 1.00x slower                                                |
| pprint_safe_repr           | 1.25 sec                                                              | 1.25 sec: 1.00x slower                                               |
| create_gc_cycles           | 1.39 ms                                                               | 1.39 ms: 1.00x slower                                                |
| regex_effbot               | 3.52 ms                                                               | 3.54 ms: 1.01x slower                                                |
| sympy_sum                  | 264 ms                                                                | 265 ms: 1.01x slower                                                 |
| json_loads                 | 30.1 us                                                               | 30.3 us: 1.01x slower                                                |
| dulwich_log                | 87.0 ms                                                               | 87.6 ms: 1.01x slower                                                |
| sympy_integrate            | 29.2 ms                                                               | 29.4 ms: 1.01x slower                                                |
| meteor_contest             | 140 ms                                                                | 141 ms: 1.01x slower                                                 |
| richards                   | 77.3 ms                                                               | 78.0 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 2.05 sec                                                              | 2.07 sec: 1.01x slower                                               |
| asyncio_tcp                | 553 ms                                                                | 558 ms: 1.01x slower                                                 |
| regex_dna                  | 215 ms                                                                | 217 ms: 1.01x slower                                                 |
| pickle                     | 10.6 us                                                               | 10.7 us: 1.01x slower                                                |
| pickle_dict                | 32.7 us                                                               | 33.0 us: 1.01x slower                                                |
| deepcopy                   | 404 us                                                                | 408 us: 1.01x slower                                                 |
| django_template            | 59.0 ms                                                               | 59.7 ms: 1.01x slower                                                |
| thrift                     | 1.21 ms                                                               | 1.22 ms: 1.01x slower                                                |
| pickle_list                | 4.68 us                                                               | 4.75 us: 1.02x slower                                                |
| python_startup_no_site     | 9.36 ms                                                               | 9.52 ms: 1.02x slower                                                |
| python_startup             | 14.0 ms                                                               | 14.3 ms: 1.02x slower                                                |
| genshi_xml                 | 81.3 ms                                                               | 83.2 ms: 1.02x slower                                                |
| genshi_text                | 38.9 ms                                                               | 39.9 ms: 1.02x slower                                                |
| pycparser                  | 1.56 sec                                                              | 1.60 sec: 1.03x slower                                               |
| richards_super             | 92.9 ms                                                               | 95.6 ms: 1.03x slower                                                |
| bench_mp_pool              | 64.0 ms                                                               | 66.3 ms: 1.04x slower                                                |
| generators                 | 36.4 ms                                                               | 38.0 ms: 1.04x slower                                                |
| unpack_sequence            | 144 ns                                                                | 150 ns: 1.05x slower                                                 |
| gc_traversal               | 2.71 ms                                                               | 2.90 ms: 1.07x slower                                                |
| bench_thread_pool          | 3.12 ms                                                               | 3.44 ms: 1.10x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (22): sqlglot_normalize, xml_etree_iterparse, async_tree_none_tg, sympy_expand, sqlglot_transpile, unpickle, async_tree_io_tg, unpickle_pure_python, regex_v8, async_tree_io, pyflate, deepcopy_memo, docutils, regex_compile, sympy_str, asyncio_websockets, typing_runtime_protocols, pickle_pure_python, pylint, sqlite_synth, json, tornado_http

# HPT report

- Reliability score: 99.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x