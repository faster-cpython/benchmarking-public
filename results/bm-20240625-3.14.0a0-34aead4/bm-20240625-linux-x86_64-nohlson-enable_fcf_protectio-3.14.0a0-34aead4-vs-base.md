# Results vs. base

- fork: nohlson
- ref: enable_fcf_protectio
- machine: linux-x86_64
- commit hash: 34aead4
- commit date: 2024-06-25
- overall geometric mean: 1.00x slower
- HPT reliability: 54.94%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                                | 265 ms: 1.00x slower                                                   |
| html5lib       | 66.9 ms                                                               | 67.6 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io          | 977 ms                                                                | 920 ms: 1.06x faster                                                   |
| async_tree_memoization | 452 ms                                                                | 481 ms: 1.06x slower                                                   |
| async_tree_io_tg       | 888 ms                                                                | 984 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 90.8 ms                                                               | 88.2 ms: 1.03x faster                                                  |
| float          | 77.8 ms                                                               | 77.1 ms: 1.01x faster                                                  |
| pidigits       | 188 ms                                                                | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                | 132 ms: 1.01x slower                                                   |
| regex_effbot   | 3.70 ms                                                               | 3.76 ms: 1.02x slower                                                  |
| regex_dna      | 227 ms                                                                | 232 ms: 1.02x slower                                                   |
| regex_v8       | 25.2 ms                                                               | 26.9 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_list        | 5.55 us                                                               | 5.31 us: 1.04x faster                                                  |
| pickle               | 11.7 us                                                               | 11.5 us: 1.02x faster                                                  |
| pickle_list          | 5.17 us                                                               | 5.12 us: 1.01x faster                                                  |
| tomli_loads          | 2.11 sec                                                              | 2.13 sec: 1.01x slower                                                 |
| unpickle_pure_python | 214 us                                                                | 216 us: 1.01x slower                                                   |
| json_dumps           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| pickle_pure_python   | 299 us                                                                | 304 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_generate, json_loads, pickle_dict, xml_etree_process, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                                  |
| python_startup         | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                                  |
| django_template | 34.1 ms                                                               | 34.7 ms: 1.02x slower                                                  |
| genshi_xml      | 50.6 ms                                                               | 51.6 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240619-linux-x86_64-python-1e4815692f6c8a37a397-3.14.0a0-1e48156 | bm-20240625-linux-x86_64-nohlson-enable_fcf_protectio-3.14.0a0-34aead4 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 977 ms                                                                | 920 ms: 1.06x faster                                                   |
| unpickle_list            | 5.55 us                                                               | 5.31 us: 1.04x faster                                                  |
| scimark_lu               | 116 ms                                                                | 113 ms: 1.03x faster                                                   |
| nbody                    | 90.8 ms                                                               | 88.2 ms: 1.03x faster                                                  |
| spectral_norm            | 115 ms                                                                | 112 ms: 1.03x faster                                                   |
| async_generators         | 439 ms                                                                | 430 ms: 1.02x faster                                                   |
| coroutines               | 22.8 ms                                                               | 22.4 ms: 1.02x faster                                                  |
| richards                 | 48.6 ms                                                               | 47.6 ms: 1.02x faster                                                  |
| pickle                   | 11.7 us                                                               | 11.5 us: 1.02x faster                                                  |
| chaos                    | 60.6 ms                                                               | 59.6 ms: 1.02x faster                                                  |
| richards_super           | 54.4 ms                                                               | 53.6 ms: 1.02x faster                                                  |
| thrift                   | 806 us                                                                | 793 us: 1.02x faster                                                   |
| logging_silent           | 102 ns                                                                | 101 ns: 1.02x faster                                                   |
| comprehensions           | 16.8 us                                                               | 16.5 us: 1.01x faster                                                  |
| pprint_safe_repr         | 744 ms                                                                | 735 ms: 1.01x faster                                                   |
| pprint_pformat           | 1.52 sec                                                              | 1.50 sec: 1.01x faster                                                 |
| pickle_list              | 5.17 us                                                               | 5.12 us: 1.01x faster                                                  |
| asyncio_tcp              | 481 ms                                                                | 477 ms: 1.01x faster                                                   |
| float                    | 77.8 ms                                                               | 77.1 ms: 1.01x faster                                                  |
| sqlite_synth             | 2.92 us                                                               | 2.89 us: 1.01x faster                                                  |
| genshi_text              | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                                  |
| fannkuch                 | 396 ms                                                                | 393 ms: 1.01x faster                                                   |
| deltablue                | 3.22 ms                                                               | 3.20 ms: 1.01x faster                                                  |
| sqlglot_parse            | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                                  |
| nqueens                  | 79.2 ms                                                               | 78.8 ms: 1.00x faster                                                  |
| raytrace                 | 266 ms                                                                | 265 ms: 1.00x faster                                                   |
| pidigits                 | 188 ms                                                                | 187 ms: 1.00x faster                                                   |
| gc_traversal             | 3.75 ms                                                               | 3.76 ms: 1.00x slower                                                  |
| 2to3                     | 265 ms                                                                | 265 ms: 1.00x slower                                                   |
| create_gc_cycles         | 1.73 ms                                                               | 1.73 ms: 1.00x slower                                                  |
| deepcopy_memo            | 29.4 us                                                               | 29.5 us: 1.00x slower                                                  |
| dulwich_log              | 64.2 ms                                                               | 64.4 ms: 1.00x slower                                                  |
| generators               | 28.8 ms                                                               | 29.0 ms: 1.00x slower                                                  |
| python_startup_no_site   | 6.91 ms                                                               | 6.94 ms: 1.00x slower                                                  |
| python_startup           | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                  |
| sqlglot_optimize         | 53.8 ms                                                               | 54.1 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl          | 1.77 sec                                                              | 1.78 sec: 1.01x slower                                                 |
| tomli_loads              | 2.11 sec                                                              | 2.13 sec: 1.01x slower                                                 |
| scimark_fft              | 366 ms                                                                | 369 ms: 1.01x slower                                                   |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                   |
| mdp                      | 2.53 sec                                                              | 2.55 sec: 1.01x slower                                                 |
| unpickle_pure_python     | 214 us                                                                | 216 us: 1.01x slower                                                   |
| telco                    | 8.16 ms                                                               | 8.24 ms: 1.01x slower                                                  |
| html5lib                 | 66.9 ms                                                               | 67.6 ms: 1.01x slower                                                  |
| json                     | 5.27 ms                                                               | 5.34 ms: 1.01x slower                                                  |
| regex_compile            | 130 ms                                                                | 132 ms: 1.01x slower                                                   |
| json_dumps               | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                  |
| deepcopy                 | 259 us                                                                | 262 us: 1.01x slower                                                   |
| hexiom                   | 6.08 ms                                                               | 6.17 ms: 1.01x slower                                                  |
| pickle_pure_python       | 299 us                                                                | 304 us: 1.02x slower                                                   |
| regex_effbot             | 3.70 ms                                                               | 3.76 ms: 1.02x slower                                                  |
| django_template          | 34.1 ms                                                               | 34.7 ms: 1.02x slower                                                  |
| genshi_xml               | 50.6 ms                                                               | 51.6 ms: 1.02x slower                                                  |
| regex_dna                | 227 ms                                                                | 232 ms: 1.02x slower                                                   |
| bpe_tokeniser            | 4.79 sec                                                              | 4.92 sec: 1.03x slower                                                 |
| typing_runtime_protocols | 160 us                                                                | 165 us: 1.03x slower                                                   |
| pycparser                | 1.13 sec                                                              | 1.18 sec: 1.05x slower                                                 |
| scimark_sor              | 125 ms                                                                | 132 ms: 1.06x slower                                                   |
| async_tree_memoization   | 452 ms                                                                | 481 ms: 1.06x slower                                                   |
| regex_v8                 | 25.2 ms                                                               | 26.9 ms: 1.07x slower                                                  |
| async_tree_io_tg         | 888 ms                                                                | 984 ms: 1.11x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (36): async_tree_none_tg, async_tree_none, xml_etree_parse, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, sympy_expand, pathlib, pylint, meteor_contest, xml_etree_generate, go, pyflate, dask, docutils, tornado_http, json_loads, pickle_dict, crypto_pyaes, sympy_integrate, deepcopy_reduce, bench_thread_pool, bench_mp_pool, scimark_sparse_mat_mult, xml_etree_process, coverage, mako, sympy_sum, scimark_monte_carlo, logging_format, sqlglot_transpile, asyncio_websockets, xml_etree_iterparse, logging_simple, sympy_str, async_tree_memoization_tg, unpickle

# HPT report

- Reliability score: 54.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x