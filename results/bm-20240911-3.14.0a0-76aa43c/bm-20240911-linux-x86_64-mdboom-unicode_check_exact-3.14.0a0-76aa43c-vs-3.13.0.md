# Results vs. 3.13.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.01x faster
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 255 ms: 1.04x faster                                                 |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                               |
| html5lib       | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                |
| tornado_http   | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                 |
| async_tree_none           | 354 ms                                                 | 313 ms: 1.13x faster                                                 |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 475 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 559 ms: 1.03x faster                                                 |
| async_generators          | 433 ms                                                 | 427 ms: 1.01x faster                                                 |
| async_tree_io             | 843 ms                                                 | 861 ms: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 871 ms: 1.05x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 85.7 ms                                                | 89.4 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.53 ms: 1.10x faster                                                |
| regex_v8       | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                                 |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                |
| tomli_loads         | 2.11 sec                                               | 2.08 sec: 1.02x faster                                               |
| xml_etree_generate  | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                |
| xml_etree_parse     | 156 ms                                                 | 154 ms: 1.01x faster                                                 |
| pickle              | 11.6 us                                                | 11.4 us: 1.01x faster                                                |
| json_loads          | 27.0 us                                                | 26.7 us: 1.01x faster                                                |
| pickle_pure_python  | 300 us                                                 | 301 us: 1.00x slower                                                 |
| pickle_list         | 5.01 us                                                | 5.06 us: 1.01x slower                                                |
| xml_etree_iterparse | 102 ms                                                 | 104 ms: 1.02x slower                                                 |
| unpickle            | 14.9 us                                                | 15.6 us: 1.05x slower                                                |
| pickle_dict         | 33.2 us                                                | 34.9 us: 1.05x slower                                                |
| unpickle_list       | 4.96 us                                                | 5.44 us: 1.10x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                |
| python_startup_no_site | 6.99 ms                                                | 6.97 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 11.2 ms: 1.00x slower                                                |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                |
| django_template | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                |
| genshi_xml      | 50.3 ms                                                | 52.2 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 261 us: 1.35x faster                                                 |
| deepcopy_memo             | 38.0 us                                                | 30.8 us: 1.23x faster                                                |
| go                        | 142 ms                                                 | 117 ms: 1.20x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.67 us: 1.19x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 391 ms: 1.13x faster                                                 |
| async_tree_none           | 354 ms                                                 | 313 ms: 1.13x faster                                                 |
| regex_effbot              | 3.88 ms                                                | 3.53 ms: 1.10x faster                                                |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                |
| mdp                       | 2.74 sec                                               | 2.58 sec: 1.06x faster                                               |
| json                      | 5.20 ms                                                | 4.92 ms: 1.06x faster                                                |
| pycparser                 | 1.19 sec                                               | 1.14 sec: 1.05x faster                                               |
| richards_super            | 54.4 ms                                                | 51.9 ms: 1.05x faster                                                |
| async_tree_none_tg        | 320 ms                                                 | 305 ms: 1.05x faster                                                 |
| richards                  | 48.1 ms                                                | 46.0 ms: 1.05x faster                                                |
| 2to3                      | 265 ms                                                 | 255 ms: 1.04x faster                                                 |
| gc_traversal              | 3.81 ms                                                | 3.66 ms: 1.04x faster                                                |
| pprint_safe_repr          | 744 ms                                                 | 718 ms: 1.04x faster                                                 |
| thrift                    | 796 us                                                 | 770 us: 1.03x faster                                                 |
| generators                | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                |
| bench_thread_pool         | 815 us                                                 | 789 us: 1.03x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 475 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 559 ms: 1.03x faster                                                 |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.02x faster                                               |
| spectral_norm             | 115 ms                                                 | 112 ms: 1.02x faster                                                 |
| html5lib                  | 64.5 ms                                                | 63.0 ms: 1.02x faster                                                |
| regex_v8                  | 25.3 ms                                                | 24.8 ms: 1.02x faster                                                |
| xml_etree_process         | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                |
| sympy_sum                 | 150 ms                                                 | 147 ms: 1.02x faster                                                 |
| nqueens                   | 80.6 ms                                                | 79.3 ms: 1.02x faster                                                |
| logging_silent            | 102 ns                                                 | 100 ns: 1.02x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.02x faster                                               |
| crypto_pyaes              | 73.0 ms                                                | 71.8 ms: 1.02x faster                                                |
| xml_etree_generate        | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                |
| async_generators          | 433 ms                                                 | 427 ms: 1.01x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.01x faster                                                |
| regex_dna                 | 220 ms                                                 | 217 ms: 1.01x faster                                                 |
| sympy_str                 | 274 ms                                                 | 270 ms: 1.01x faster                                                 |
| tornado_http              | 91.5 ms                                                | 90.4 ms: 1.01x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 154 ms: 1.01x faster                                                 |
| pickle                    | 11.6 us                                                | 11.4 us: 1.01x faster                                                |
| regex_compile             | 131 ms                                                 | 130 ms: 1.01x faster                                                 |
| json_loads                | 27.0 us                                                | 26.7 us: 1.01x faster                                                |
| float                     | 78.5 ms                                                | 77.7 ms: 1.01x faster                                                |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.98 ms: 1.01x faster                                                |
| raytrace                  | 262 ms                                                 | 259 ms: 1.01x faster                                                 |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.9 ms                                                | 53.7 ms: 1.00x faster                                                |
| python_startup_no_site    | 6.99 ms                                                | 6.97 ms: 1.00x faster                                                |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 301 us: 1.00x slower                                                 |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.00x slower                                                |
| meteor_contest            | 108 ms                                                 | 108 ms: 1.01x slower                                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                |
| chaos                     | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                |
| genshi_text               | 22.9 ms                                                | 23.1 ms: 1.01x slower                                                |
| typing_runtime_protocols  | 159 us                                                 | 161 us: 1.01x slower                                                 |
| django_template           | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                |
| pickle_list               | 5.01 us                                                | 5.06 us: 1.01x slower                                                |
| sqlglot_normalize         | 107 ms                                                 | 109 ms: 1.01x slower                                                 |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                |
| logging_simple            | 5.66 us                                                | 5.74 us: 1.01x slower                                                |
| xml_etree_iterparse       | 102 ms                                                 | 104 ms: 1.02x slower                                                 |
| hexiom                    | 6.13 ms                                                | 6.22 ms: 1.02x slower                                                |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                |
| logging_format            | 6.25 us                                                | 6.38 us: 1.02x slower                                                |
| async_tree_io             | 843 ms                                                 | 861 ms: 1.02x slower                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 67.8 ms: 1.02x slower                                                |
| dulwich_log               | 63.0 ms                                                | 64.5 ms: 1.02x slower                                                |
| docutils                  | 2.58 sec                                               | 2.66 sec: 1.03x slower                                               |
| pyflate                   | 460 ms                                                 | 474 ms: 1.03x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.84 sec: 1.03x slower                                               |
| coverage                  | 83.7 ms                                                | 86.5 ms: 1.03x slower                                                |
| scimark_sor               | 122 ms                                                 | 127 ms: 1.03x slower                                                 |
| genshi_xml                | 50.3 ms                                                | 52.2 ms: 1.04x slower                                                |
| nbody                     | 85.7 ms                                                | 89.4 ms: 1.04x slower                                                |
| coroutines                | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                |
| unpickle                  | 14.9 us                                                | 15.6 us: 1.05x slower                                                |
| pickle_dict               | 33.2 us                                                | 34.9 us: 1.05x slower                                                |
| async_tree_io_tg          | 825 ms                                                 | 871 ms: 1.05x slower                                                 |
| fannkuch                  | 381 ms                                                 | 403 ms: 1.06x slower                                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.71 ms: 1.06x slower                                                |
| unpickle_list             | 4.96 us                                                | 5.44 us: 1.10x slower                                                |
| unpack_sequence           | 42.4 ns                                                | 50.5 ns: 1.19x slower                                                |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (12): sympy_expand, telco, asyncio_websockets, comprehensions, unpickle_pure_python, bench_mp_pool, asyncio_tcp_ssl, json_dumps, sqlite_synth, async_tree_cpu_io_mixed_tg, scimark_fft, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x