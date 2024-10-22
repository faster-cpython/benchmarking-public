# Results vs. base

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-x86_64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.00x faster
- HPT reliability: 98.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.34 sec                                                              | 3.33 sec: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines             | 32.1 ms                                                               | 31.6 ms: 1.02x faster                                                    |
| async_tree_none        | 412 ms                                                                | 406 ms: 1.02x faster                                                     |
| async_tree_io          | 906 ms                                                                | 892 ms: 1.02x faster                                                     |
| async_tree_memoization | 517 ms                                                                | 510 ms: 1.01x faster                                                     |
| async_tree_io_tg       | 840 ms                                                                | 830 ms: 1.01x faster                                                     |
| async_tree_none_tg     | 350 ms                                                                | 347 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl        | 2.07 sec                                                              | 2.05 sec: 1.01x faster                                                   |
| async_generators       | 559 ms                                                                | 557 ms: 1.00x faster                                                     |
| asyncio_tcp            | 561 ms                                                                | 568 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 142 ms                                                                | 139 ms: 1.02x faster                                                     |
| pidigits       | 184 ms                                                                | 184 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                               | 26.0 ms: 1.00x faster                                                    |
| regex_effbot   | 3.51 ms                                                               | 3.54 ms: 1.01x slower                                                    |
| regex_dna      | 218 ms                                                                | 220 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads          | 32.4 us                                                               | 31.6 us: 1.02x faster                                                    |
| tomli_loads         | 3.26 sec                                                              | 3.22 sec: 1.01x faster                                                   |
| xml_etree_generate  | 110 ms                                                                | 110 ms: 1.01x faster                                                     |
| xml_etree_process   | 88.8 ms                                                               | 88.3 ms: 1.01x faster                                                    |
| pickle_pure_python  | 572 us                                                                | 575 us: 1.01x slower                                                     |
| xml_etree_iterparse | 113 ms                                                                | 114 ms: 1.01x slower                                                     |
| xml_etree_parse     | 149 ms                                                                | 153 ms: 1.02x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.7 ms                                                               | 13.7 ms: 1.00x faster                                                    |
| python_startup_no_site | 9.31 ms                                                               | 9.30 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 39.6 ms                                                               | 39.9 ms: 1.01x slower                                                    |
| mako            | 21.0 ms                                                               | 21.1 ms: 1.01x slower                                                    |
| django_template | 59.2 ms                                                               | 59.8 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240813-linux-x86_64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-linux-x86_64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 6.95 ms                                                               | 6.69 ms: 1.04x faster                                                    |
| fannkuch                 | 625 ms                                                                | 605 ms: 1.03x faster                                                     |
| spectral_norm            | 189 ms                                                                | 183 ms: 1.03x faster                                                     |
| generators               | 37.4 ms                                                               | 36.4 ms: 1.03x faster                                                    |
| json_loads               | 32.4 us                                                               | 31.6 us: 1.02x faster                                                    |
| nqueens                  | 119 ms                                                                | 117 ms: 1.02x faster                                                     |
| telco                    | 10.4 ms                                                               | 10.2 ms: 1.02x faster                                                    |
| json                     | 6.04 ms                                                               | 5.93 ms: 1.02x faster                                                    |
| float                    | 142 ms                                                                | 139 ms: 1.02x faster                                                     |
| meteor_contest           | 143 ms                                                                | 141 ms: 1.02x faster                                                     |
| coroutines               | 32.1 ms                                                               | 31.6 ms: 1.02x faster                                                    |
| async_tree_none          | 412 ms                                                                | 406 ms: 1.02x faster                                                     |
| async_tree_io            | 906 ms                                                                | 892 ms: 1.02x faster                                                     |
| pathlib                  | 19.2 ms                                                               | 18.9 ms: 1.01x faster                                                    |
| async_tree_memoization   | 517 ms                                                                | 510 ms: 1.01x faster                                                     |
| tomli_loads              | 3.26 sec                                                              | 3.22 sec: 1.01x faster                                                   |
| async_tree_io_tg         | 840 ms                                                                | 830 ms: 1.01x faster                                                     |
| pyflate                  | 773 ms                                                                | 765 ms: 1.01x faster                                                     |
| async_tree_none_tg       | 350 ms                                                                | 347 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl          | 2.07 sec                                                              | 2.05 sec: 1.01x faster                                                   |
| mdp                      | 3.21 sec                                                              | 3.19 sec: 1.01x faster                                                   |
| sympy_str                | 425 ms                                                                | 422 ms: 1.01x faster                                                     |
| pycparser                | 1.63 sec                                                              | 1.62 sec: 1.01x faster                                                   |
| xml_etree_generate       | 110 ms                                                                | 110 ms: 1.01x faster                                                     |
| xml_etree_process        | 88.8 ms                                                               | 88.3 ms: 1.01x faster                                                    |
| sympy_integrate          | 28.8 ms                                                               | 28.7 ms: 1.00x faster                                                    |
| async_generators         | 559 ms                                                                | 557 ms: 1.00x faster                                                     |
| docutils                 | 3.34 sec                                                              | 3.33 sec: 1.00x faster                                                   |
| regex_v8                 | 26.0 ms                                                               | 26.0 ms: 1.00x faster                                                    |
| python_startup           | 13.7 ms                                                               | 13.7 ms: 1.00x faster                                                    |
| pidigits                 | 184 ms                                                                | 184 ms: 1.00x faster                                                     |
| python_startup_no_site   | 9.31 ms                                                               | 9.30 ms: 1.00x faster                                                    |
| crypto_pyaes             | 113 ms                                                                | 113 ms: 1.00x slower                                                     |
| gc_traversal             | 3.02 ms                                                               | 3.03 ms: 1.00x slower                                                    |
| deltablue                | 8.34 ms                                                               | 8.38 ms: 1.00x slower                                                    |
| pickle_pure_python       | 572 us                                                                | 575 us: 1.01x slower                                                     |
| scimark_monte_carlo      | 124 ms                                                                | 125 ms: 1.01x slower                                                     |
| scimark_sor              | 266 ms                                                                | 268 ms: 1.01x slower                                                     |
| raytrace                 | 598 ms                                                                | 603 ms: 1.01x slower                                                     |
| sqlglot_optimize         | 85.9 ms                                                               | 86.6 ms: 1.01x slower                                                    |
| deepcopy                 | 417 us                                                                | 421 us: 1.01x slower                                                     |
| genshi_text              | 39.6 ms                                                               | 39.9 ms: 1.01x slower                                                    |
| logging_format           | 11.6 us                                                               | 11.7 us: 1.01x slower                                                    |
| thrift                   | 1.22 ms                                                               | 1.23 ms: 1.01x slower                                                    |
| xml_etree_iterparse      | 113 ms                                                                | 114 ms: 1.01x slower                                                     |
| mako                     | 21.0 ms                                                               | 21.1 ms: 1.01x slower                                                    |
| pprint_pformat           | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                                   |
| pprint_safe_repr         | 1.27 sec                                                              | 1.28 sec: 1.01x slower                                                   |
| regex_effbot             | 3.51 ms                                                               | 3.54 ms: 1.01x slower                                                    |
| go                       | 306 ms                                                                | 309 ms: 1.01x slower                                                     |
| django_template          | 59.2 ms                                                               | 59.8 ms: 1.01x slower                                                    |
| typing_runtime_protocols | 249 us                                                                | 251 us: 1.01x slower                                                     |
| regex_dna                | 218 ms                                                                | 220 ms: 1.01x slower                                                     |
| asyncio_tcp              | 561 ms                                                                | 568 ms: 1.01x slower                                                     |
| logging_simple           | 10.3 us                                                               | 10.4 us: 1.01x slower                                                    |
| richards_super           | 95.4 ms                                                               | 97.2 ms: 1.02x slower                                                    |
| deepcopy_memo            | 52.2 us                                                               | 53.2 us: 1.02x slower                                                    |
| richards                 | 78.3 ms                                                               | 80.1 ms: 1.02x slower                                                    |
| xml_etree_parse          | 149 ms                                                                | 153 ms: 1.02x slower                                                     |
| deepcopy_reduce          | 4.28 us                                                               | 4.39 us: 1.02x slower                                                    |
| logging_silent           | 191 ns                                                                | 197 ns: 1.03x slower                                                     |
| coverage                 | 111 ms                                                                | 116 ms: 1.04x slower                                                     |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (27): pylint, scimark_lu, unpickle_pure_python, async_tree_cpu_io_mixed, sympy_expand, hexiom, regex_compile, bpe_tokeniser, scimark_fft, async_tree_cpu_io_mixed_tg, comprehensions, sympy_sum, 2to3, create_gc_cycles, bench_mp_pool, chaos, sqlglot_normalize, nbody, asyncio_websockets, sqlglot_parse, bench_thread_pool, html5lib, async_tree_memoization_tg, genshi_xml, sqlglot_transpile, tornado_http, json_dumps

# HPT report

- Reliability score: 98.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x