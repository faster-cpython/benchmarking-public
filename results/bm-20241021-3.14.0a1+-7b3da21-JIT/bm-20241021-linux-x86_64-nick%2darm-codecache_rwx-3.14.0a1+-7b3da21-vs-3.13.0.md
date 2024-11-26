# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.014x faster
- HPT reliability: 62.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 271 ms: 1.02x slower                                                |
| docutils       | 2.59 sec                                               | 2.88 sec: 1.11x slower                                              |
| html5lib       | 64.2 ms                                                | 67.1 ms: 1.05x slower                                               |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.10x slower                                              |
| tornado_http   | 92.4 ms                                                | 94.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                |
| async_tree_none            | 351 ms                                                 | 338 ms: 1.04x faster                                                |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                                |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 963 ms: 1.12x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.4 ms: 1.06x faster                                               |
| float          | 79.2 ms                                                | 75.6 ms: 1.05x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.08x faster                                               |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                               |
| regex_compile  | 132 ms                                                 | 135 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.11x faster                                              |
| xml_etree_generate   | 86.7 ms                                                | 78.3 ms: 1.11x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 54.8 ms: 1.11x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                |
| json_dumps           | 10.6 ms                                                | 10.8 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.05x faster                                               |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                               |
| django_template | 35.2 ms                                                | 35.4 ms: 1.01x slower                                               |
| genshi_text     | 23.5 ms                                                | 26.3 ms: 1.12x slower                                               |
| genshi_xml      | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                                |
| deepcopy_memo              | 39.1 us                                                | 29.2 us: 1.34x faster                                               |
| richards                   | 48.7 ms                                                | 37.1 ms: 1.31x faster                                               |
| richards_super             | 54.9 ms                                                | 43.8 ms: 1.25x faster                                               |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.18x faster                                               |
| scimark_fft                | 364 ms                                                 | 322 ms: 1.13x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.92 sec: 1.11x faster                                              |
| xml_etree_generate         | 86.7 ms                                                | 78.3 ms: 1.11x faster                                               |
| telco                      | 8.54 ms                                                | 7.71 ms: 1.11x faster                                               |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                               |
| xml_etree_process          | 60.6 ms                                                | 54.8 ms: 1.11x faster                                               |
| go                         | 144 ms                                                 | 130 ms: 1.10x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 68.4 ms: 1.10x faster                                               |
| json                       | 5.36 ms                                                | 4.93 ms: 1.09x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                               |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.4 ms: 1.08x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.42 sec: 1.07x faster                                              |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                              |
| scimark_monte_carlo        | 67.4 ms                                                | 63.5 ms: 1.06x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.77 ms: 1.06x faster                                               |
| pprint_safe_repr           | 728 ms                                                 | 689 ms: 1.06x faster                                                |
| nbody                      | 87.0 ms                                                | 82.4 ms: 1.06x faster                                               |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.05x faster                                               |
| pyflate                    | 471 ms                                                 | 447 ms: 1.05x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| logging_format             | 6.40 us                                                | 6.08 us: 1.05x faster                                               |
| float                      | 79.2 ms                                                | 75.6 ms: 1.05x faster                                               |
| pprint_pformat             | 1.49 sec                                               | 1.43 sec: 1.04x faster                                              |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                |
| async_tree_none            | 351 ms                                                 | 338 ms: 1.04x faster                                                |
| regex_dna                  | 218 ms                                                 | 212 ms: 1.03x faster                                                |
| logging_simple             | 5.72 us                                                | 5.57 us: 1.03x faster                                               |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                               |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                               |
| thrift                     | 809 us                                                 | 800 us: 1.01x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| coverage                   | 84.0 ms                                                | 84.3 ms: 1.00x slower                                               |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                |
| django_template            | 35.2 ms                                                | 35.4 ms: 1.01x slower                                               |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                                |
| chaos                      | 58.1 ms                                                | 58.6 ms: 1.01x slower                                               |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                               |
| tornado_http               | 92.4 ms                                                | 94.0 ms: 1.02x slower                                               |
| 2to3                       | 267 ms                                                 | 271 ms: 1.02x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                               |
| regex_compile              | 132 ms                                                 | 135 ms: 1.02x slower                                                |
| raytrace                   | 267 ms                                                 | 272 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 861 ms: 1.02x slower                                                |
| json_dumps                 | 10.6 ms                                                | 10.8 ms: 1.02x slower                                               |
| async_generators           | 436 ms                                                 | 449 ms: 1.03x slower                                                |
| dulwich_log                | 64.3 ms                                                | 66.5 ms: 1.03x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                               |
| html5lib                   | 64.2 ms                                                | 67.1 ms: 1.05x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.05x slower                                               |
| sympy_expand               | 463 ms                                                 | 494 ms: 1.07x slower                                                |
| bench_thread_pool          | 822 us                                                 | 879 us: 1.07x slower                                                |
| sympy_str                  | 275 ms                                                 | 296 ms: 1.08x slower                                                |
| sqlglot_optimize           | 53.7 ms                                                | 58.3 ms: 1.08x slower                                               |
| gc_traversal               | 4.37 ms                                                | 4.74 ms: 1.08x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.10x slower                                              |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                               |
| docutils                   | 2.59 sec                                               | 2.88 sec: 1.11x slower                                              |
| genshi_text                | 23.5 ms                                                | 26.3 ms: 1.12x slower                                               |
| hexiom                     | 6.16 ms                                                | 6.91 ms: 1.12x slower                                               |
| async_tree_io_tg           | 857 ms                                                 | 963 ms: 1.12x slower                                                |
| nqueens                    | 78.4 ms                                                | 89.4 ms: 1.14x slower                                               |
| genshi_xml                 | 50.9 ms                                                | 58.4 ms: 1.15x slower                                               |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.15x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                               |
| pylint                     | 313 ms                                                 | 367 ms: 1.17x slower                                                |
| generators                 | 29.0 ms                                                | 35.1 ms: 1.21x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.48x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, meteor_contest, coroutines, deltablue, logging_silent, typing_runtime_protocols, async_tree_none_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 62.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x