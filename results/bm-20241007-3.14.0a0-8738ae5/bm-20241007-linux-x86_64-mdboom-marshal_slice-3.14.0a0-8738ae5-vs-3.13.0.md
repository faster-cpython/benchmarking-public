# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 8738ae5
- commit date: 2024-10-07
- overall geometric mean: 1.00x faster
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                           |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                         |
| html5lib       | 64.5 ms                                                | 61.4 ms: 1.05x faster                                          |
| tornado_http   | 91.5 ms                                                | 90.2 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                           |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                           |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                           |
| asyncio_tcp               | 488 ms                                                 | 472 ms: 1.03x faster                                           |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                           |
| async_tree_io_tg          | 825 ms                                                 | 916 ms: 1.11x slower                                           |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.8 ms: 1.02x faster                                          |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                           |
| nbody          | 85.7 ms                                                | 86.9 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                          |
| regex_compile  | 131 ms                                                 | 129 ms: 1.01x faster                                           |
| regex_v8       | 25.3 ms                                                | 25.4 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.2 ms: 1.02x faster                                          |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| tomli_loads          | 2.11 sec                                               | 2.09 sec: 1.01x faster                                         |
| pickle_list          | 5.01 us                                                | 4.96 us: 1.01x faster                                          |
| json_loads           | 27.0 us                                                | 26.9 us: 1.00x faster                                          |
| pickle_dict          | 33.2 us                                                | 33.4 us: 1.01x slower                                          |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                          |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                           |
| pickle_pure_python   | 300 us                                                 | 305 us: 1.02x slower                                           |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.02x slower                                           |
| unpickle             | 14.9 us                                                | 15.6 us: 1.05x slower                                          |
| unpickle_list        | 4.96 us                                                | 5.30 us: 1.07x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| python_startup_no_site | 6.99 ms                                                | 7.01 ms: 1.00x slower                                          |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.4 ms: 1.02x faster                                          |
| django_template | 34.4 ms                                                | 33.9 ms: 1.02x faster                                          |
| genshi_xml      | 50.3 ms                                                | 49.6 ms: 1.02x faster                                          |
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                          |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-8738ae5 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 263 us: 1.34x faster                                           |
| deepcopy_memo             | 38.0 us                                                | 30.5 us: 1.25x faster                                          |
| go                        | 142 ms                                                 | 120 ms: 1.18x faster                                           |
| deepcopy_reduce           | 3.17 us                                                | 2.71 us: 1.17x faster                                          |
| async_tree_memoization_tg | 465 ms                                                 | 402 ms: 1.16x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                           |
| async_tree_none           | 354 ms                                                 | 322 ms: 1.10x faster                                           |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.66 ms: 1.08x faster                                          |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                          |
| pycparser                 | 1.19 sec                                               | 1.13 sec: 1.06x faster                                         |
| gc_traversal              | 3.81 ms                                                | 3.61 ms: 1.05x faster                                          |
| regex_effbot              | 3.88 ms                                                | 3.69 ms: 1.05x faster                                          |
| html5lib                  | 64.5 ms                                                | 61.4 ms: 1.05x faster                                          |
| generators                | 28.8 ms                                                | 27.7 ms: 1.04x faster                                          |
| 2to3                      | 265 ms                                                 | 255 ms: 1.04x faster                                           |
| thrift                    | 796 us                                                 | 767 us: 1.04x faster                                           |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                           |
| telco                     | 8.45 ms                                                | 8.16 ms: 1.04x faster                                          |
| asyncio_tcp               | 488 ms                                                 | 472 ms: 1.03x faster                                           |
| pprint_safe_repr          | 744 ms                                                 | 721 ms: 1.03x faster                                           |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                           |
| scimark_fft               | 369 ms                                                 | 360 ms: 1.02x faster                                           |
| sympy_str                 | 274 ms                                                 | 267 ms: 1.02x faster                                           |
| genshi_text               | 22.9 ms                                                | 22.4 ms: 1.02x faster                                          |
| pprint_pformat            | 1.51 sec                                               | 1.48 sec: 1.02x faster                                         |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.02x faster                                           |
| float                     | 78.5 ms                                                | 76.8 ms: 1.02x faster                                          |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                           |
| crypto_pyaes              | 73.0 ms                                                | 71.5 ms: 1.02x faster                                          |
| xml_etree_process         | 60.4 ms                                                | 59.2 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 563 ms: 1.02x faster                                           |
| richards_super            | 54.4 ms                                                | 53.5 ms: 1.02x faster                                          |
| django_template           | 34.4 ms                                                | 33.9 ms: 1.02x faster                                          |
| richards                  | 48.1 ms                                                | 47.4 ms: 1.02x faster                                          |
| json                      | 5.20 ms                                                | 5.12 ms: 1.02x faster                                          |
| genshi_xml                | 50.3 ms                                                | 49.6 ms: 1.02x faster                                          |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                          |
| sympy_expand              | 462 ms                                                 | 455 ms: 1.01x faster                                           |
| tornado_http              | 91.5 ms                                                | 90.2 ms: 1.01x faster                                          |
| regex_compile             | 131 ms                                                 | 129 ms: 1.01x faster                                           |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.77 sec: 1.01x faster                                         |
| mdp                       | 2.74 sec                                               | 2.71 sec: 1.01x faster                                         |
| nqueens                   | 80.6 ms                                                | 79.7 ms: 1.01x faster                                          |
| tomli_loads               | 2.11 sec                                               | 2.09 sec: 1.01x faster                                         |
| sqlglot_optimize          | 53.9 ms                                                | 53.4 ms: 1.01x faster                                          |
| pickle_list               | 5.01 us                                                | 4.96 us: 1.01x faster                                          |
| sqlite_synth              | 2.85 us                                                | 2.82 us: 1.01x faster                                          |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                           |
| mako                      | 11.1 ms                                                | 11.0 ms: 1.01x faster                                          |
| sympy_integrate           | 19.9 ms                                                | 19.8 ms: 1.01x faster                                          |
| json_loads                | 27.0 us                                                | 26.9 us: 1.00x faster                                          |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                          |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.00x faster                                           |
| python_startup_no_site    | 6.99 ms                                                | 7.01 ms: 1.00x slower                                          |
| regex_v8                  | 25.3 ms                                                | 25.4 ms: 1.00x slower                                          |
| scimark_sor               | 122 ms                                                 | 123 ms: 1.00x slower                                           |
| bpe_tokeniser             | 4.69 sec                                               | 4.71 sec: 1.00x slower                                         |
| sqlglot_normalize         | 107 ms                                                 | 108 ms: 1.01x slower                                           |
| pickle_dict               | 33.2 us                                                | 33.4 us: 1.01x slower                                          |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                           |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                           |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                          |
| raytrace                  | 262 ms                                                 | 265 ms: 1.01x slower                                           |
| sqlglot_transpile         | 1.57 ms                                                | 1.59 ms: 1.01x slower                                          |
| pickle                    | 11.6 us                                                | 11.7 us: 1.01x slower                                          |
| coverage                  | 83.7 ms                                                | 84.8 ms: 1.01x slower                                          |
| nbody                     | 85.7 ms                                                | 86.9 ms: 1.01x slower                                          |
| unpickle_pure_python      | 213 us                                                 | 216 us: 1.01x slower                                           |
| hexiom                    | 6.13 ms                                                | 6.22 ms: 1.02x slower                                          |
| pickle_pure_python        | 300 us                                                 | 305 us: 1.02x slower                                           |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                           |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                          |
| docutils                  | 2.58 sec                                               | 2.64 sec: 1.02x slower                                         |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                          |
| chaos                     | 58.4 ms                                                | 59.8 ms: 1.02x slower                                          |
| dulwich_log               | 63.0 ms                                                | 64.6 ms: 1.03x slower                                          |
| scimark_monte_carlo       | 66.3 ms                                                | 68.2 ms: 1.03x slower                                          |
| pyflate                   | 460 ms                                                 | 476 ms: 1.03x slower                                           |
| deltablue                 | 3.15 ms                                                | 3.26 ms: 1.04x slower                                          |
| fannkuch                  | 381 ms                                                 | 398 ms: 1.05x slower                                           |
| unpickle                  | 14.9 us                                                | 15.6 us: 1.05x slower                                          |
| bench_thread_pool         | 815 us                                                 | 853 us: 1.05x slower                                           |
| unpickle_list             | 4.96 us                                                | 5.30 us: 1.07x slower                                          |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                           |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                          |
| async_tree_io_tg          | 825 ms                                                 | 916 ms: 1.11x slower                                           |
| unpack_sequence           | 42.4 ns                                                | 57.9 ns: 1.37x slower                                          |
| bench_mp_pool             | 24.0 ms                                                | 56.0 ms: 2.33x slower                                          |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (9): logging_simple, xml_etree_generate, regex_dna, logging_format, asyncio_websockets, xml_etree_parse, async_generators, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x