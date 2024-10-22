# Results vs. 3.13.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d343f97
- commit date: 2024-09-06
- overall geometric mean: 1.01x faster
- HPT reliability: 96.21%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 265 ms                                                 | 256 ms: 1.04x faster                                  |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                |
| html5lib       | 64.5 ms                                                | 62.2 ms: 1.04x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                  |
| async_tree_memoization    | 442 ms                                                 | 387 ms: 1.14x faster                                  |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                  |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.02x faster                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                  |
| async_generators          | 433 ms                                                 | 439 ms: 1.01x slower                                  |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                 |
| async_tree_io_tg          | 825 ms                                                 | 892 ms: 1.08x slower                                  |
| async_tree_io             | 843 ms                                                 | 927 ms: 1.10x slower                                  |
| Geometric mean            | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 78.5 ms                                                | 77.8 ms: 1.01x faster                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| nbody          | 85.7 ms                                                | 86.3 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                 |
| regex_v8       | 25.3 ms                                                | 24.5 ms: 1.03x faster                                 |
| regex_compile  | 131 ms                                                 | 128 ms: 1.03x faster                                  |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.6 ms: 1.03x faster                                 |
| xml_etree_generate  | 87.0 ms                                                | 85.2 ms: 1.02x faster                                 |
| tomli_loads         | 2.11 sec                                               | 2.08 sec: 1.01x faster                                |
| pickle              | 11.6 us                                                | 11.6 us: 1.00x slower                                 |
| json_dumps          | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| pickle_list         | 5.01 us                                                | 5.16 us: 1.03x slower                                 |
| xml_etree_iterparse | 102 ms                                                 | 106 ms: 1.04x slower                                  |
| json_loads          | 27.0 us                                                | 28.4 us: 1.05x slower                                 |
| unpickle_list       | 4.96 us                                                | 5.25 us: 1.06x slower                                 |
| pickle_dict         | 33.2 us                                                | 35.4 us: 1.07x slower                                 |
| Geometric mean      | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_parse, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                 |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 22.1 ms: 1.03x faster                                 |
| genshi_xml      | 50.3 ms                                                | 48.7 ms: 1.03x faster                                 |
| django_template | 34.4 ms                                                | 34.2 ms: 1.01x faster                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x faster                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-main-3.14.0a0-d343f97 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 258 us: 1.37x faster                                  |
| deepcopy_memo             | 38.0 us                                                | 29.7 us: 1.28x faster                                 |
| go                        | 142 ms                                                 | 118 ms: 1.20x faster                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.69 us: 1.18x faster                                 |
| async_tree_memoization_tg | 465 ms                                                 | 398 ms: 1.17x faster                                  |
| async_tree_memoization    | 442 ms                                                 | 387 ms: 1.14x faster                                  |
| async_tree_none           | 354 ms                                                 | 323 ms: 1.10x faster                                  |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                 |
| regex_effbot              | 3.88 ms                                                | 3.62 ms: 1.07x faster                                 |
| gc_traversal              | 3.81 ms                                                | 3.56 ms: 1.07x faster                                 |
| async_tree_none_tg        | 320 ms                                                 | 306 ms: 1.04x faster                                  |
| pprint_safe_repr          | 744 ms                                                 | 713 ms: 1.04x faster                                  |
| pycparser                 | 1.19 sec                                               | 1.15 sec: 1.04x faster                                |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.83 ms: 1.04x faster                                 |
| html5lib                  | 64.5 ms                                                | 62.2 ms: 1.04x faster                                 |
| generators                | 28.8 ms                                                | 27.8 ms: 1.04x faster                                 |
| richards_super            | 54.4 ms                                                | 52.5 ms: 1.04x faster                                 |
| 2to3                      | 265 ms                                                 | 256 ms: 1.04x faster                                  |
| richards                  | 48.1 ms                                                | 46.5 ms: 1.04x faster                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 555 ms: 1.03x faster                                  |
| genshi_text               | 22.9 ms                                                | 22.1 ms: 1.03x faster                                 |
| genshi_xml                | 50.3 ms                                                | 48.7 ms: 1.03x faster                                 |
| regex_v8                  | 25.3 ms                                                | 24.5 ms: 1.03x faster                                 |
| thrift                    | 796 us                                                 | 772 us: 1.03x faster                                  |
| bench_thread_pool         | 815 us                                                 | 790 us: 1.03x faster                                  |
| xml_etree_process         | 60.4 ms                                                | 58.6 ms: 1.03x faster                                 |
| scimark_lu                | 115 ms                                                 | 112 ms: 1.03x faster                                  |
| regex_compile             | 131 ms                                                 | 128 ms: 1.03x faster                                  |
| pprint_pformat            | 1.51 sec                                               | 1.47 sec: 1.02x faster                                |
| telco                     | 8.45 ms                                                | 8.27 ms: 1.02x faster                                 |
| xml_etree_generate        | 87.0 ms                                                | 85.2 ms: 1.02x faster                                 |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                  |
| scimark_fft               | 369 ms                                                 | 363 ms: 1.02x faster                                  |
| asyncio_tcp               | 488 ms                                                 | 481 ms: 1.02x faster                                  |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.01x faster                                |
| sympy_integrate           | 19.9 ms                                                | 19.6 ms: 1.01x faster                                 |
| sqlglot_optimize          | 53.9 ms                                                | 53.3 ms: 1.01x faster                                 |
| sympy_expand              | 462 ms                                                 | 457 ms: 1.01x faster                                  |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                  |
| float                     | 78.5 ms                                                | 77.8 ms: 1.01x faster                                 |
| sqlglot_normalize         | 107 ms                                                 | 107 ms: 1.01x faster                                  |
| spectral_norm             | 115 ms                                                 | 114 ms: 1.01x faster                                  |
| django_template           | 34.4 ms                                                | 34.2 ms: 1.01x faster                                 |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.00x faster                                |
| raytrace                  | 262 ms                                                 | 260 ms: 1.00x faster                                  |
| mako                      | 11.1 ms                                                | 11.1 ms: 1.00x faster                                 |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.00x slower                                 |
| hexiom                    | 6.13 ms                                                | 6.14 ms: 1.00x slower                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.00x slower                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.00x slower                                |
| pickle                    | 11.6 us                                                | 11.6 us: 1.00x slower                                 |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                  |
| nbody                     | 85.7 ms                                                | 86.3 ms: 1.01x slower                                 |
| nqueens                   | 80.6 ms                                                | 81.2 ms: 1.01x slower                                 |
| json_dumps                | 10.4 ms                                                | 10.5 ms: 1.01x slower                                 |
| sqlglot_transpile         | 1.57 ms                                                | 1.59 ms: 1.01x slower                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.05 ms: 1.01x slower                                 |
| regex_dna                 | 220 ms                                                 | 223 ms: 1.01x slower                                  |
| async_generators          | 433 ms                                                 | 439 ms: 1.01x slower                                  |
| sqlite_synth              | 2.85 us                                                | 2.89 us: 1.02x slower                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 67.4 ms: 1.02x slower                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.29 ms: 1.02x slower                                 |
| logging_simple            | 5.66 us                                                | 5.77 us: 1.02x slower                                 |
| deltablue                 | 3.15 ms                                                | 3.21 ms: 1.02x slower                                 |
| comprehensions            | 16.4 us                                                | 16.7 us: 1.02x slower                                 |
| dulwich_log               | 63.0 ms                                                | 64.6 ms: 1.03x slower                                 |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                  |
| docutils                  | 2.58 sec                                               | 2.66 sec: 1.03x slower                                |
| pickle_list               | 5.01 us                                                | 5.16 us: 1.03x slower                                 |
| json                      | 5.20 ms                                                | 5.35 ms: 1.03x slower                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.84 sec: 1.03x slower                                |
| pyflate                   | 460 ms                                                 | 475 ms: 1.03x slower                                  |
| coroutines                | 22.5 ms                                                | 23.3 ms: 1.03x slower                                 |
| coverage                  | 83.7 ms                                                | 86.6 ms: 1.03x slower                                 |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                  |
| json_loads                | 27.0 us                                                | 28.4 us: 1.05x slower                                 |
| unpickle_list             | 4.96 us                                                | 5.25 us: 1.06x slower                                 |
| pickle_dict               | 33.2 us                                                | 35.4 us: 1.07x slower                                 |
| create_gc_cycles          | 1.61 ms                                                | 1.72 ms: 1.07x slower                                 |
| fannkuch                  | 381 ms                                                 | 410 ms: 1.08x slower                                  |
| async_tree_io_tg          | 825 ms                                                 | 892 ms: 1.08x slower                                  |
| async_tree_io             | 843 ms                                                 | 927 ms: 1.10x slower                                  |
| unpack_sequence           | 42.4 ns                                                | 50.4 ns: 1.19x slower                                 |
| Geometric mean            | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed_tg, bench_mp_pool, typing_runtime_protocols, tornado_http, meteor_contest, pickle_pure_python, logging_format, crypto_pyaes, chaos, xml_etree_parse, unpickle_pure_python, logging_silent, unpickle, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 96.21% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x