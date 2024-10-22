# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 1c27106
- commit date: 2024-08-08
- overall geometric mean: 1.02x slower
- HPT reliability: 70.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 281 ms: 1.06x slower                                                   |
| docutils       | 2.58 sec                                               | 3.09 sec: 1.20x slower                                                 |
| html5lib       | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                  |
| tornado_http   | 91.5 ms                                                | 110 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                   |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                   |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 879 ms: 1.06x slower                                                   |
| asyncio_tcp               | 488 ms                                                 | 535 ms: 1.10x slower                                                   |
| async_tree_io             | 843 ms                                                 | 935 ms: 1.11x slower                                                   |
| coroutines                | 22.5 ms                                                | 25.5 ms: 1.13x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                  |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.41 ms: 1.14x faster                                                  |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                  |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                  |
| xml_etree_process    | 60.4 ms                                                | 56.1 ms: 1.08x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.97 sec: 1.07x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 99.6 ms: 1.02x faster                                                  |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                                   |
| json_loads           | 27.0 us                                                | 28.5 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                  |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                  |
| genshi_text     | 22.9 ms                                                | 25.3 ms: 1.10x slower                                                  |
| genshi_xml      | 50.3 ms                                                | 56.9 ms: 1.13x slower                                                  |
| django_template | 34.4 ms                                                | 39.5 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240808-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-1c27106 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                  | 352 us                                                 | 275 us: 1.28x faster                                                   |
| deepcopy_memo             | 38.0 us                                                | 30.0 us: 1.27x faster                                                  |
| scimark_fft               | 369 ms                                                 | 309 ms: 1.19x faster                                                   |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.33 ms: 1.16x faster                                                  |
| async_tree_memoization_tg | 465 ms                                                 | 403 ms: 1.15x faster                                                   |
| regex_effbot              | 3.88 ms                                                | 3.41 ms: 1.14x faster                                                  |
| scimark_monte_carlo       | 66.3 ms                                                | 59.2 ms: 1.12x faster                                                  |
| crypto_pyaes              | 73.0 ms                                                | 66.4 ms: 1.10x faster                                                  |
| float                     | 78.5 ms                                                | 71.6 ms: 1.10x faster                                                  |
| telco                     | 8.45 ms                                                | 7.72 ms: 1.09x faster                                                  |
| deepcopy_reduce           | 3.17 us                                                | 2.93 us: 1.08x faster                                                  |
| xml_etree_generate        | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                  |
| mako                      | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                  |
| xml_etree_process         | 60.4 ms                                                | 56.1 ms: 1.08x faster                                                  |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                   |
| tomli_loads               | 2.11 sec                                               | 1.97 sec: 1.07x faster                                                 |
| nbody                     | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                  |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.06x faster                                                   |
| pathlib                   | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                  |
| mdp                       | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                 |
| spectral_norm             | 115 ms                                                 | 110 ms: 1.05x faster                                                   |
| regex_v8                  | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                  |
| async_tree_none           | 354 ms                                                 | 338 ms: 1.05x faster                                                   |
| async_tree_none_tg        | 320 ms                                                 | 308 ms: 1.04x faster                                                   |
| bpe_tokeniser             | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                 |
| regex_dna                 | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| fannkuch                  | 381 ms                                                 | 369 ms: 1.03x faster                                                   |
| scimark_sor               | 122 ms                                                 | 119 ms: 1.03x faster                                                   |
| meteor_contest            | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pprint_safe_repr          | 744 ms                                                 | 726 ms: 1.03x faster                                                   |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.03x faster                                                  |
| xml_etree_iterparse       | 102 ms                                                 | 99.6 ms: 1.02x faster                                                  |
| json                      | 5.20 ms                                                | 5.10 ms: 1.02x faster                                                  |
| richards                  | 48.1 ms                                                | 47.6 ms: 1.01x faster                                                  |
| richards_super            | 54.4 ms                                                | 54.0 ms: 1.01x faster                                                  |
| gc_traversal              | 3.81 ms                                                | 3.81 ms: 1.00x slower                                                  |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                   |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| python_startup            | 10.6 ms                                                | 10.7 ms: 1.01x slower                                                  |
| chaos                     | 58.4 ms                                                | 59.5 ms: 1.02x slower                                                  |
| html5lib                  | 64.5 ms                                                | 65.8 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.83 sec: 1.02x slower                                                 |
| python_startup_no_site    | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                  |
| comprehensions            | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| pickle_pure_python        | 300 us                                                 | 310 us: 1.03x slower                                                   |
| unpickle_pure_python      | 213 us                                                 | 222 us: 1.04x slower                                                   |
| nqueens                   | 80.6 ms                                                | 84.4 ms: 1.05x slower                                                  |
| json_loads                | 27.0 us                                                | 28.5 us: 1.06x slower                                                  |
| async_generators          | 433 ms                                                 | 457 ms: 1.06x slower                                                   |
| regex_compile             | 131 ms                                                 | 139 ms: 1.06x slower                                                   |
| 2to3                      | 265 ms                                                 | 281 ms: 1.06x slower                                                   |
| async_tree_io_tg          | 825 ms                                                 | 879 ms: 1.06x slower                                                   |
| go                        | 142 ms                                                 | 151 ms: 1.07x slower                                                   |
| typing_runtime_protocols  | 159 us                                                 | 171 us: 1.08x slower                                                   |
| thrift                    | 796 us                                                 | 859 us: 1.08x slower                                                   |
| sqlglot_parse             | 1.27 ms                                                | 1.37 ms: 1.08x slower                                                  |
| sqlglot_normalize         | 107 ms                                                 | 117 ms: 1.09x slower                                                   |
| sqlglot_transpile         | 1.57 ms                                                | 1.72 ms: 1.09x slower                                                  |
| asyncio_tcp               | 488 ms                                                 | 535 ms: 1.10x slower                                                   |
| bench_thread_pool         | 815 us                                                 | 893 us: 1.10x slower                                                   |
| sqlglot_optimize          | 53.9 ms                                                | 59.2 ms: 1.10x slower                                                  |
| genshi_text               | 22.9 ms                                                | 25.3 ms: 1.10x slower                                                  |
| async_tree_io             | 843 ms                                                 | 935 ms: 1.11x slower                                                   |
| coverage                  | 83.7 ms                                                | 93.6 ms: 1.12x slower                                                  |
| create_gc_cycles          | 1.61 ms                                                | 1.80 ms: 1.12x slower                                                  |
| raytrace                  | 262 ms                                                 | 293 ms: 1.12x slower                                                   |
| genshi_xml                | 50.3 ms                                                | 56.9 ms: 1.13x slower                                                  |
| hexiom                    | 6.13 ms                                                | 6.94 ms: 1.13x slower                                                  |
| coroutines                | 22.5 ms                                                | 25.5 ms: 1.13x slower                                                  |
| django_template           | 34.4 ms                                                | 39.5 ms: 1.15x slower                                                  |
| sympy_expand              | 462 ms                                                 | 541 ms: 1.17x slower                                                   |
| logging_simple            | 5.66 us                                                | 6.63 us: 1.17x slower                                                  |
| sympy_str                 | 274 ms                                                 | 325 ms: 1.19x slower                                                   |
| logging_format            | 6.25 us                                                | 7.47 us: 1.19x slower                                                  |
| generators                | 28.8 ms                                                | 34.4 ms: 1.20x slower                                                  |
| docutils                  | 2.58 sec                                               | 3.09 sec: 1.20x slower                                                 |
| tornado_http              | 91.5 ms                                                | 110 ms: 1.21x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 25.1 ms: 1.26x slower                                                  |
| pylint                    | 313 ms                                                 | 408 ms: 1.30x slower                                                   |
| deltablue                 | 3.15 ms                                                | 4.13 ms: 1.31x slower                                                  |
| sympy_sum                 | 150 ms                                                 | 197 ms: 1.32x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (8): logging_silent, async_tree_cpu_io_mixed_tg, async_tree_memoization, pprint_pformat, pyflate, async_tree_cpu_io_mixed, bench_mp_pool, pycparser
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 70.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x