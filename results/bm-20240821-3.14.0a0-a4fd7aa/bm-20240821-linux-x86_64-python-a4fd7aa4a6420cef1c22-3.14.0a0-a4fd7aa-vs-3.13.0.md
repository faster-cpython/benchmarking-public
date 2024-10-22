# Results vs. 3.13.0

- fork: python
- ref: a4fd7aa4a6420cef1c22
- machine: linux-x86_64
- commit hash: a4fd7aa
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 79.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 264 ms: 1.00x faster                                                  |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| html5lib       | 64.5 ms                                                | 63.6 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 90.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                  |
| asyncio_tcp               | 488 ms                                                 | 474 ms: 1.03x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 566 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 905 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (3): async_generators, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| nbody          | 85.7 ms                                                | 86.7 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                                  |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process   | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                 |
| xml_etree_generate  | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| tomli_loads         | 2.11 sec                                               | 2.08 sec: 1.01x faster                                                |
| pickle_pure_python  | 300 us                                                 | 306 us: 1.02x slower                                                  |
| xml_etree_iterparse | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| json_loads          | 27.0 us                                                | 28.4 us: 1.05x slower                                                 |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| genshi_text     | 22.9 ms                                                | 22.5 ms: 1.01x faster                                                 |
| genshi_xml      | 50.3 ms                                                | 49.9 ms: 1.01x faster                                                 |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 262 us: 1.35x faster                                                  |
| deepcopy_memo             | 38.0 us                                                | 29.8 us: 1.27x faster                                                 |
| deepcopy_reduce           | 3.17 us                                                | 2.66 us: 1.19x faster                                                 |
| async_tree_memoization_tg | 465 ms                                                 | 404 ms: 1.15x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 394 ms: 1.12x faster                                                  |
| async_tree_none           | 354 ms                                                 | 325 ms: 1.09x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.53 sec: 1.08x faster                                                |
| pathlib                   | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                 |
| logging_simple            | 5.66 us                                                | 5.47 us: 1.04x faster                                                 |
| telco                     | 8.45 ms                                                | 8.16 ms: 1.04x faster                                                 |
| bench_thread_pool         | 815 us                                                 | 789 us: 1.03x faster                                                  |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                 |
| asyncio_tcp               | 488 ms                                                 | 474 ms: 1.03x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 311 ms: 1.03x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 58.9 ms: 1.03x faster                                                 |
| generators                | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                 |
| xml_etree_generate        | 87.0 ms                                                | 85.0 ms: 1.02x faster                                                 |
| thrift                    | 796 us                                                 | 779 us: 1.02x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                 |
| logging_format            | 6.25 us                                                | 6.13 us: 1.02x faster                                                 |
| richards_super            | 54.4 ms                                                | 53.3 ms: 1.02x faster                                                 |
| regex_compile             | 131 ms                                                 | 129 ms: 1.02x faster                                                  |
| sympy_str                 | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| django_template           | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                 |
| richards                  | 48.1 ms                                                | 47.4 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 566 ms: 1.01x faster                                                  |
| genshi_text               | 22.9 ms                                                | 22.5 ms: 1.01x faster                                                 |
| tomli_loads               | 2.11 sec                                               | 2.08 sec: 1.01x faster                                                |
| html5lib                  | 64.5 ms                                                | 63.6 ms: 1.01x faster                                                 |
| nqueens                   | 80.6 ms                                                | 79.7 ms: 1.01x faster                                                 |
| tornado_http              | 91.5 ms                                                | 90.5 ms: 1.01x faster                                                 |
| sympy_sum                 | 150 ms                                                 | 148 ms: 1.01x faster                                                  |
| sympy_integrate           | 19.9 ms                                                | 19.7 ms: 1.01x faster                                                 |
| sympy_expand              | 462 ms                                                 | 457 ms: 1.01x faster                                                  |
| sqlglot_optimize          | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                 |
| genshi_xml                | 50.3 ms                                                | 49.9 ms: 1.01x faster                                                 |
| scimark_lu                | 115 ms                                                 | 114 ms: 1.01x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 72.5 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.78 sec: 1.01x faster                                                |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| spectral_norm             | 115 ms                                                 | 114 ms: 1.00x faster                                                  |
| float                     | 78.5 ms                                                | 78.1 ms: 1.00x faster                                                 |
| 2to3                      | 265 ms                                                 | 264 ms: 1.00x faster                                                  |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| go                        | 142 ms                                                 | 142 ms: 1.01x slower                                                  |
| raytrace                  | 262 ms                                                 | 264 ms: 1.01x slower                                                  |
| mako                      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                 |
| nbody                     | 85.7 ms                                                | 86.7 ms: 1.01x slower                                                 |
| gc_traversal              | 3.81 ms                                                | 3.86 ms: 1.01x slower                                                 |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                 |
| meteor_contest            | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| pyflate                   | 460 ms                                                 | 466 ms: 1.01x slower                                                  |
| regex_dna                 | 220 ms                                                 | 223 ms: 1.02x slower                                                  |
| sqlglot_transpile         | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                 |
| pickle_pure_python        | 300 us                                                 | 306 us: 1.02x slower                                                  |
| chaos                     | 58.4 ms                                                | 59.6 ms: 1.02x slower                                                 |
| typing_runtime_protocols  | 159 us                                                 | 162 us: 1.02x slower                                                  |
| json                      | 5.20 ms                                                | 5.32 ms: 1.02x slower                                                 |
| coverage                  | 83.7 ms                                                | 85.7 ms: 1.02x slower                                                 |
| logging_silent            | 102 ns                                                 | 105 ns: 1.03x slower                                                  |
| coroutines                | 22.5 ms                                                | 23.1 ms: 1.03x slower                                                 |
| hexiom                    | 6.13 ms                                                | 6.30 ms: 1.03x slower                                                 |
| scimark_sor               | 122 ms                                                 | 126 ms: 1.03x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                 |
| scimark_monte_carlo       | 66.3 ms                                                | 68.3 ms: 1.03x slower                                                 |
| bpe_tokeniser             | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                |
| deltablue                 | 3.15 ms                                                | 3.26 ms: 1.03x slower                                                 |
| xml_etree_iterparse       | 102 ms                                                 | 106 ms: 1.04x slower                                                  |
| regex_v8                  | 25.3 ms                                                | 26.2 ms: 1.04x slower                                                 |
| docutils                  | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                |
| json_loads                | 27.0 us                                                | 28.4 us: 1.05x slower                                                 |
| fannkuch                  | 381 ms                                                 | 407 ms: 1.07x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                 |
| async_tree_io_tg          | 825 ms                                                 | 905 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 936 ms: 1.11x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (13): pycparser, xml_etree_parse, async_generators, pprint_safe_repr, scimark_fft, asyncio_websockets, bench_mp_pool, sqlglot_normalize, pprint_pformat, unpickle_pure_python, json_dumps, async_tree_cpu_io_mixed_tg, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 79.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x