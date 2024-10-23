# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.02x slower
- HPT reliability: 53.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 271 ms: 1.02x slower                                                |
| docutils       | 2.58 sec                                               | 2.88 sec: 1.12x slower                                              |
| html5lib       | 64.5 ms                                                | 67.1 ms: 1.04x slower                                               |
| tornado_http   | 91.5 ms                                                | 94.0 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 380 ms: 1.22x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                |
| async_tree_none            | 354 ms                                                 | 338 ms: 1.05x faster                                                |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                               |
| async_tree_io              | 843 ms                                                 | 861 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                                |
| async_generators           | 433 ms                                                 | 449 ms: 1.04x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 963 ms: 1.17x slower                                                |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 82.4 ms: 1.04x faster                                               |
| float          | 78.5 ms                                                | 75.6 ms: 1.04x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                               |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                               |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.3 ms: 1.11x faster                                               |
| xml_etree_process    | 60.4 ms                                                | 54.8 ms: 1.10x faster                                               |
| tomli_loads          | 2.11 sec                                               | 1.92 sec: 1.10x faster                                              |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| xml_etree_iterparse  | 102 ms                                                 | 100 ms: 1.02x faster                                                |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                               |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                               |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                               |
| python_startup         | 10.6 ms                                                | 11.8 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                               |
| django_template | 34.4 ms                                                | 35.4 ms: 1.03x slower                                               |
| genshi_text     | 22.9 ms                                                | 26.3 ms: 1.15x slower                                               |
| genshi_xml      | 50.3 ms                                                | 58.4 ms: 1.16x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 266 us: 1.33x faster                                                |
| deepcopy_memo              | 38.0 us                                                | 29.2 us: 1.30x faster                                               |
| richards                   | 48.1 ms                                                | 37.1 ms: 1.30x faster                                               |
| richards_super             | 54.4 ms                                                | 43.8 ms: 1.24x faster                                               |
| async_tree_memoization_tg  | 465 ms                                                 | 380 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.17 us                                                | 2.72 us: 1.17x faster                                               |
| scimark_fft                | 369 ms                                                 | 322 ms: 1.15x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 78.3 ms: 1.11x faster                                               |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                               |
| xml_etree_process          | 60.4 ms                                                | 54.8 ms: 1.10x faster                                               |
| tomli_loads                | 2.11 sec                                               | 1.92 sec: 1.10x faster                                              |
| telco                      | 8.45 ms                                                | 7.71 ms: 1.10x faster                                               |
| go                         | 142 ms                                                 | 130 ms: 1.09x faster                                                |
| pprint_safe_repr           | 744 ms                                                 | 689 ms: 1.08x faster                                                |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                              |
| crypto_pyaes               | 73.0 ms                                                | 68.4 ms: 1.07x faster                                               |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                              |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                               |
| pprint_pformat             | 1.51 sec                                               | 1.43 sec: 1.06x faster                                              |
| pycparser                  | 1.19 sec                                               | 1.13 sec: 1.06x faster                                              |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| json                       | 5.20 ms                                                | 4.93 ms: 1.05x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.05x faster                                               |
| async_tree_none            | 354 ms                                                 | 338 ms: 1.05x faster                                                |
| scimark_monte_carlo        | 66.3 ms                                                | 63.5 ms: 1.04x faster                                               |
| nbody                      | 85.7 ms                                                | 82.4 ms: 1.04x faster                                               |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                |
| float                      | 78.5 ms                                                | 75.6 ms: 1.04x faster                                               |
| regex_v8                   | 25.3 ms                                                | 24.4 ms: 1.04x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                |
| pyflate                    | 460 ms                                                 | 447 ms: 1.03x faster                                                |
| logging_format             | 6.25 us                                                | 6.08 us: 1.03x faster                                               |
| logging_simple             | 5.66 us                                                | 5.57 us: 1.02x faster                                               |
| xml_etree_iterparse        | 102 ms                                                 | 100 ms: 1.02x faster                                                |
| fannkuch                   | 381 ms                                                 | 375 ms: 1.02x faster                                                |
| json_loads                 | 27.0 us                                                | 26.6 us: 1.01x faster                                               |
| scimark_lu                 | 115 ms                                                 | 114 ms: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| coverage                   | 83.7 ms                                                | 84.3 ms: 1.01x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                               |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                               |
| comprehensions             | 16.4 us                                                | 16.7 us: 1.02x slower                                               |
| async_tree_io              | 843 ms                                                 | 861 ms: 1.02x slower                                                |
| 2to3                       | 265 ms                                                 | 271 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.02x slower                                                |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                                |
| tornado_http               | 91.5 ms                                                | 94.0 ms: 1.03x slower                                               |
| django_template            | 34.4 ms                                                | 35.4 ms: 1.03x slower                                               |
| deltablue                  | 3.15 ms                                                | 3.24 ms: 1.03x slower                                               |
| async_generators           | 433 ms                                                 | 449 ms: 1.04x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                               |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                |
| html5lib                   | 64.5 ms                                                | 67.1 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                                |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.05x slower                                               |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                                |
| dulwich_log                | 63.0 ms                                                | 66.5 ms: 1.06x slower                                               |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                               |
| sympy_expand               | 462 ms                                                 | 494 ms: 1.07x slower                                                |
| bench_thread_pool          | 815 us                                                 | 879 us: 1.08x slower                                                |
| sqlglot_optimize           | 53.9 ms                                                | 58.3 ms: 1.08x slower                                               |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                                |
| nqueens                    | 80.6 ms                                                | 89.4 ms: 1.11x slower                                               |
| docutils                   | 2.58 sec                                               | 2.88 sec: 1.12x slower                                              |
| python_startup             | 10.6 ms                                                | 11.8 ms: 1.12x slower                                               |
| hexiom                     | 6.13 ms                                                | 6.91 ms: 1.13x slower                                               |
| genshi_text                | 22.9 ms                                                | 26.3 ms: 1.15x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                               |
| genshi_xml                 | 50.3 ms                                                | 58.4 ms: 1.16x slower                                               |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 963 ms: 1.17x slower                                                |
| pylint                     | 313 ms                                                 | 367 ms: 1.17x slower                                                |
| generators                 | 28.8 ms                                                | 35.1 ms: 1.22x slower                                               |
| gc_traversal               | 3.81 ms                                                | 4.74 ms: 1.24x slower                                               |
| create_gc_cycles           | 1.61 ms                                                | 2.67 ms: 1.66x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                               |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, asyncio_websockets, logging_silent, chaos, thrift, async_tree_none_tg
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: sphinx

# HPT report

- Reliability score: 53.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x