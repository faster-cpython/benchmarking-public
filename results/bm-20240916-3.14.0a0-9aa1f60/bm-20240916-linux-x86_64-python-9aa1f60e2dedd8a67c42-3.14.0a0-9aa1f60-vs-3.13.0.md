# Results vs. 3.13.0

- fork: python
- ref: 9aa1f60e2dedd8a67c42
- machine: linux-x86_64
- commit hash: 9aa1f60
- commit date: 2024-09-16
- overall geometric mean: 1.012x faster
- HPT reliability: 91.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                 |
| tornado_http   | 91.2 ms                                                | 90.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 385 ms: 1.20x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 399 ms: 1.10x faster                                                  |
| async_tree_none            | 350 ms                                                 | 326 ms: 1.07x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 303 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 555 ms: 1.03x faster                                                  |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| async_tree_io              | 838 ms                                                 | 862 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 566 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 911 ms: 1.06x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.0 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.7 ms                                                | 88.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.68 ms: 1.02x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 87.2 ms: 1.00x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 158 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                 |
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                 |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                 |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 385 ms: 1.20x faster                                                  |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.19x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.9 ms: 1.17x faster                                                 |
| json                       | 5.32 ms                                                | 4.80 ms: 1.11x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 399 ms: 1.10x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.49 ms: 1.09x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                 |
| async_tree_none            | 350 ms                                                 | 326 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 303 ms: 1.05x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 71.3 ms: 1.05x faster                                                 |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                  |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                 |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 555 ms: 1.03x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.05 sec: 1.03x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.03x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.68 ms: 1.02x faster                                                 |
| float                      | 78.7 ms                                                | 77.0 ms: 1.02x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                  |
| subparsers                 | 15.5 ms                                                | 15.1 ms: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                  |
| bench_thread_pool          | 818 us                                                 | 802 us: 1.02x faster                                                  |
| richards_super             | 53.7 ms                                                | 52.7 ms: 1.02x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                  |
| richards                   | 47.5 ms                                                | 46.8 ms: 1.02x faster                                                 |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                                |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 727 ms                                                 | 719 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 452 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                 |
| tornado_http               | 91.2 ms                                                | 90.5 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 87.2 ms: 1.00x slower                                                 |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                  |
| pyflate                    | 470 ms                                                 | 475 ms: 1.01x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                 |
| coverage                   | 82.8 ms                                                | 83.9 ms: 1.01x slower                                                 |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                 |
| nbody                      | 87.7 ms                                                | 88.8 ms: 1.01x slower                                                 |
| many_optionals             | 857 us                                                 | 868 us: 1.01x slower                                                  |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.32 us: 1.02x slower                                                 |
| spectral_norm              | 113 ms                                                 | 115 ms: 1.02x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                  |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 158 ms: 1.03x slower                                                  |
| async_tree_io              | 838 ms                                                 | 862 ms: 1.03x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                 |
| telco                      | 8.40 ms                                                | 8.67 ms: 1.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                  |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 566 ms: 1.04x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.05x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 911 ms: 1.06x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.98 sec: 1.06x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                                 |
| k_core                     | 2.37 sec                                               | 3.50 sec: 1.48x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (13): djangocms, scimark_fft, logging_simple, regex_dna, dulwich_log, bench_mp_pool, nqueens, json_dumps, asyncio_websockets, logging_silent, sqlalchemy_imperative, sphinx, pylint
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
Ignored benchmarks (13) of results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 91.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x