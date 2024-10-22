# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.00x faster
- HPT reliability: 56.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                   |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.17x slower                                                 |
| html5lib       | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                  |
| tornado_http   | 91.5 ms                                                | 97.0 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                   |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 309 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 567 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| asyncio_tcp               | 488 ms                                                 | 495 ms: 1.01x slower                                                   |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                  |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 898 ms: 1.09x slower                                                   |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                  |
| nbody          | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.71 ms: 1.05x faster                                                  |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 221 ms: 1.00x slower                                                   |
| regex_compile  | 131 ms                                                 | 142 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                  |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process    | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.03x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| pickle               | 11.6 us                                                | 11.6 us: 1.01x slower                                                  |
| pickle_list          | 5.01 us                                                | 5.18 us: 1.04x slower                                                  |
| unpickle_list        | 4.96 us                                                | 5.16 us: 1.04x slower                                                  |
| json_loads           | 27.0 us                                                | 28.2 us: 1.05x slower                                                  |
| pickle_dict          | 33.2 us                                                | 34.9 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                  |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                  |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                  |
| genshi_xml      | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 26.0 us: 1.46x faster                                                  |
| deepcopy                  | 352 us                                                 | 264 us: 1.34x faster                                                   |
| richards_super            | 54.4 ms                                                | 42.6 ms: 1.28x faster                                                  |
| scimark_fft               | 369 ms                                                 | 305 ms: 1.21x faster                                                   |
| deepcopy_reduce           | 3.17 us                                                | 2.64 us: 1.20x faster                                                  |
| richards                  | 48.1 ms                                                | 40.0 ms: 1.20x faster                                                  |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.23 ms: 1.19x faster                                                  |
| spectral_norm             | 115 ms                                                 | 99.7 ms: 1.15x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 405 ms: 1.15x faster                                                   |
| mako                      | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                  |
| float                     | 78.5 ms                                                | 70.3 ms: 1.12x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process         | 60.4 ms                                                | 55.3 ms: 1.09x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 66.9 ms: 1.09x faster                                                  |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                                   |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                 |
| logging_silent            | 102 ns                                                 | 94.5 ns: 1.08x faster                                                  |
| nbody                     | 85.7 ms                                                | 79.5 ms: 1.08x faster                                                  |
| go                        | 142 ms                                                 | 132 ms: 1.08x faster                                                   |
| unpickle_pure_python      | 213 us                                                 | 199 us: 1.07x faster                                                   |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| scimark_sor               | 122 ms                                                 | 115 ms: 1.06x faster                                                   |
| telco                     | 8.45 ms                                                | 7.97 ms: 1.06x faster                                                  |
| bpe_tokeniser             | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                 |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.06x faster                                                   |
| regex_effbot              | 3.88 ms                                                | 3.71 ms: 1.05x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.66 ms: 1.04x faster                                                  |
| xml_etree_iterparse       | 102 ms                                                 | 98.6 ms: 1.03x faster                                                  |
| async_tree_none_tg        | 320 ms                                                 | 309 ms: 1.03x faster                                                   |
| pprint_safe_repr          | 744 ms                                                 | 724 ms: 1.03x faster                                                   |
| thrift                    | 796 us                                                 | 778 us: 1.02x faster                                                   |
| sqlite_synth              | 2.85 us                                                | 2.79 us: 1.02x faster                                                  |
| regex_v8                  | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                  |
| pyflate                   | 460 ms                                                 | 450 ms: 1.02x faster                                                   |
| fannkuch                  | 381 ms                                                 | 376 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 567 ms: 1.01x faster                                                   |
| logging_format            | 6.25 us                                                | 6.19 us: 1.01x faster                                                  |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                  |
| html5lib                  | 64.5 ms                                                | 64.8 ms: 1.00x slower                                                  |
| regex_dna                 | 220 ms                                                 | 221 ms: 1.00x slower                                                   |
| python_startup            | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| pickle                    | 11.6 us                                                | 11.6 us: 1.01x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.5 us: 1.01x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 495 ms: 1.01x slower                                                   |
| pycparser                 | 1.19 sec                                               | 1.21 sec: 1.02x slower                                                 |
| coroutines                | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                  |
| json                      | 5.20 ms                                                | 5.30 ms: 1.02x slower                                                  |
| chaos                     | 58.4 ms                                                | 59.7 ms: 1.02x slower                                                  |
| scimark_monte_carlo       | 66.3 ms                                                | 67.8 ms: 1.02x slower                                                  |
| deltablue                 | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                  |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.02x slower                                                  |
| coverage                  | 83.7 ms                                                | 86.0 ms: 1.03x slower                                                  |
| bench_thread_pool         | 815 us                                                 | 842 us: 1.03x slower                                                   |
| pickle_list               | 5.01 us                                                | 5.18 us: 1.04x slower                                                  |
| typing_runtime_protocols  | 159 us                                                 | 165 us: 1.04x slower                                                   |
| unpickle_list             | 4.96 us                                                | 5.16 us: 1.04x slower                                                  |
| raytrace                  | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| 2to3                      | 265 ms                                                 | 276 ms: 1.04x slower                                                   |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                                   |
| json_loads                | 27.0 us                                                | 28.2 us: 1.05x slower                                                  |
| django_template           | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                  |
| pickle_dict               | 33.2 us                                                | 34.9 us: 1.05x slower                                                  |
| nqueens                   | 80.6 ms                                                | 85.2 ms: 1.06x slower                                                  |
| tornado_http              | 91.5 ms                                                | 97.0 ms: 1.06x slower                                                  |
| genshi_text               | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                  |
| async_generators          | 433 ms                                                 | 460 ms: 1.06x slower                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                  |
| sqlglot_parse             | 1.27 ms                                                | 1.37 ms: 1.08x slower                                                  |
| regex_compile             | 131 ms                                                 | 142 ms: 1.09x slower                                                   |
| sqlglot_transpile         | 1.57 ms                                                | 1.71 ms: 1.09x slower                                                  |
| async_tree_io_tg          | 825 ms                                                 | 898 ms: 1.09x slower                                                   |
| dulwich_log               | 63.0 ms                                                | 68.5 ms: 1.09x slower                                                  |
| sympy_str                 | 274 ms                                                 | 299 ms: 1.09x slower                                                   |
| sympy_expand              | 462 ms                                                 | 507 ms: 1.10x slower                                                   |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 938 ms: 1.11x slower                                                   |
| hexiom                    | 6.13 ms                                                | 6.88 ms: 1.12x slower                                                  |
| genshi_xml                | 50.3 ms                                                | 57.3 ms: 1.14x slower                                                  |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                  |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.15x slower                                                   |
| generators                | 28.8 ms                                                | 33.3 ms: 1.15x slower                                                  |
| docutils                  | 2.58 sec                                               | 3.01 sec: 1.17x slower                                                 |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                   |
| unpack_sequence           | 42.4 ns                                                | 111 ns: 2.63x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (7): pprint_pformat, logging_simple, pickle_pure_python, asyncio_websockets, bench_mp_pool, async_tree_cpu_io_mixed_tg, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 56.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x